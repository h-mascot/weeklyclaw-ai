'use strict';

const DEFAULT_REPO = 'h-mascot/weeklyclaw-feedback';
const MAX_FIELD_LENGTH = 4000;

function sendJson(res, statusCode, payload) {
  res.statusCode = statusCode;
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.end(JSON.stringify(payload));
}

function cleanValue(value) {
  if (Array.isArray(value)) {
    return value.map(cleanValue).filter(Boolean);
  }
  if (typeof value !== 'string') return '';
  return value.trim().slice(0, MAX_FIELD_LENGTH);
}

function normalizeSubmission(input = {}) {
  return {
    overallRating: cleanValue(input.overall_rating),
    moreOf: cleanValue(input.more_of),
    favoritePart: cleanValue(input.favorite_part),
    changeRequest: cleanValue(input.change_request),
    nextNomination: cleanValue(input.next_nomination),
    shareOnShow: cleanValue(input.share_on_show) || 'Not answered',
    name: cleanValue(input.name) || 'Anonymous',
    email: cleanValue(input.email),
    handle: cleanValue(input.handle),
    page: cleanValue(input.page) || 'feedback',
    userAgent: cleanValue(input.user_agent),
    submittedAt: cleanValue(input.submitted_at) || new Date().toISOString(),
    honeypot: cleanValue(input.company || input._honey),
  };
}

function validateSubmission(submission) {
  const errors = [];
  if (submission.honeypot) errors.push('spam_detected');
  if (!submission.overallRating) errors.push('overall_rating_required');
  if (!Array.isArray(submission.moreOf) || submission.moreOf.length === 0) errors.push('more_of_required');
  if (!submission.favoritePart) errors.push('favorite_part_required');
  return errors;
}

function formatIssueBody(submission) {
  const moreOf = Array.isArray(submission.moreOf) ? submission.moreOf.join(', ') : submission.moreOf;
  return [
    '## Weekly Claw audience feedback',
    '',
    `- **Submitted at:** ${submission.submittedAt}`,
    `- **Overall rating:** ${submission.overallRating}/5`,
    `- **More of:** ${moreOf}`,
    `- **Share on show:** ${submission.shareOnShow}`,
    `- **Name:** ${submission.name}`,
    `- **Email:** ${submission.email || 'Not provided'}`,
    `- **Handle:** ${submission.handle || 'Not provided'}`,
    `- **Page:** ${submission.page}`,
    '',
    '### What landed best',
    submission.favoritePart || 'Not provided',
    '',
    '### What should change',
    submission.changeRequest || 'Not provided',
    '',
    '### What should we cover next',
    submission.nextNomination || 'Not provided',
    '',
    '<details>',
    '<summary>Technical metadata</summary>',
    '',
    `- **User agent:** ${submission.userAgent || 'Not provided'}`,
    '',
    '</details>',
  ].join('\n');
}

async function createGitHubIssue(submission) {
  const repo = process.env.WEEKLYCLAW_FEEDBACK_REPO || DEFAULT_REPO;
  const token = process.env.WEEKLYCLAW_GITHUB_TOKEN || process.env.GITHUB_TOKEN;
  if (!token) {
    const error = new Error('GitHub token is not configured.');
    error.code = 'missing_github_token';
    throw error;
  }

  const safeName = submission.name === 'Anonymous' ? 'Anonymous' : submission.name.replace(/[\r\n]/g, ' ').slice(0, 80);
  const title = `Feedback ${submission.overallRating}/5 — ${safeName} — ${submission.submittedAt.slice(0, 10)}`;
  const response = await fetch(`https://api.github.com/repos/${repo}/issues`, {
    method: 'POST',
    headers: {
      Accept: 'application/vnd.github+json',
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
      'User-Agent': 'weeklyclaw-feedback-form',
      'X-GitHub-Api-Version': '2022-11-28',
    },
    body: JSON.stringify({
      title,
      body: formatIssueBody(submission),
      labels: ['website-feedback'],
    }),
  });

  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    const error = new Error(payload.message || 'GitHub issue creation failed.');
    error.code = 'github_issue_failed';
    error.status = response.status;
    throw error;
  }

  return { repo, issueNumber: payload.number, issueUrl: payload.html_url };
}

async function readRequestBody(req) {
  if (req.body && typeof req.body === 'object') return req.body;
  if (typeof req.body === 'string') return JSON.parse(req.body);

  const chunks = [];
  for await (const chunk of req) chunks.push(chunk);
  const raw = Buffer.concat(chunks).toString('utf8');
  if (!raw) return {};
  const contentType = req.headers['content-type'] || '';
  if (contentType.includes('application/json')) return JSON.parse(raw);
  if (contentType.includes('application/x-www-form-urlencoded')) {
    const params = new URLSearchParams(raw);
    const parsed = {};
    for (const [key, value] of params.entries()) {
      if (key.endsWith('[]')) {
        const normalized = key.slice(0, -2);
        parsed[normalized] = parsed[normalized] || [];
        parsed[normalized].push(value);
      } else if (parsed[key]) {
        parsed[key] = Array.isArray(parsed[key]) ? [...parsed[key], value] : [parsed[key], value];
      } else {
        parsed[key] = value;
      }
    }
    return parsed;
  }
  return JSON.parse(raw);
}

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    sendJson(res, 405, { ok: false, error: 'method_not_allowed' });
    return;
  }

  try {
    const body = await readRequestBody(req);
    const submission = normalizeSubmission(body);
    const errors = validateSubmission(submission);
    if (errors.length) {
      sendJson(res, errors.includes('spam_detected') ? 200 : 400, { ok: false, error: errors[0], errors });
      return;
    }

    const issue = await createGitHubIssue(submission);
    sendJson(res, 200, { ok: true, issueNumber: issue.issueNumber });
  } catch (error) {
    console.error('weeklyclaw-feedback-submit failed', { code: error.code, status: error.status, message: error.message });
    sendJson(res, 500, { ok: false, error: 'submission_failed' });
  }
};

module.exports._test = {
  normalizeSubmission,
  validateSubmission,
  formatIssueBody,
};

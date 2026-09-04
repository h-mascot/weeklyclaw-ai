# fal Launches H3 Max, a New Post-Trained Video Model with Frontier Quality and Faster-Than-Real-Time Generation

## News provided by

[ **fal** ](/news/fal/)
Sep 01, 2026, 11:10 ET

**H3 Max ranks #1 on independent AI model benchmarks from Artificial Analysis and Design Arena while generating a five-second video in approximately three seconds**

SAN FRANCISCO, Sept. 1, 2026 /PRNewswire/ -- fal, the generative media platform for developers and enterprises, today released **H3 Max**, a new post-trained video generation model developed by fal Research and optimized by fal's inference team for faster-than-real-time generation.

Fal has taken the underlying H3 weights and pushed them into territory the original model never reached, making fal the original creator of H3 Max. Built on the open-weights MiniMax H3 model, H3 Max combines post-training for stronger prompt adherence and visual quality with an inference engine designed specifically around the model. It generates a five-second video in approximately three seconds of wall time, roughly 35x the throughput of the official MiniMax H3 endpoint and, in fal's testing, an average of 15x faster than models with comparable quality.

"MiniMax H3 Max combines state-of-the-art video quality with a step-change in generation speed, making high-quality video generation practical for many more real-world applications at a much broader scale," said the MiniMax H3 team. "We've worked closely with fal since day one, and their expertise in generative AI infrastructure and ability to bring frontier models into production quickly and reliably make them a natural partner for H3 Max. We're excited to bring it to developers, creators and businesses worldwide together with fal."

H3 Max is also demonstrating leading performance in independent evaluations. **Design Arena currently ranks H3 Max #1 on its recent Image-to-Video leaderboard, with an Elo rating of 1,341, ahead of the official MiniMax H3 at 1,333 and other leading models including Seedance 2.5, FLUX.3 and Gemini Omni Flash.**

"With performance in the same band as MiniMax H3 and generation speeds up to 50× faster, MiniMax H3 Max by fal establishes a new speed–preference Pareto frontier, as verified by Design Arena's independent benchmarking," said Design Arena.

**Artificial Analysis also ranks fal's H3 model #1 on its Image-to-Video Leaderboard with Audio**, with an Elo rating of 1,201 across 2,177 samples. It ranks ahead of models including ByteDance Seedance 2.0, MiniMax H3, Gemini Omni Flash, Grok Imagine Video 1.5, Veo 3.1 and Kling 3.0.

The independent results reinforce fal's own human preference evaluations. In head-to-head testing against 12 leading video models, H3 Max ranked #1 across overall quality, prompt understanding and aesthetics, winning the majority of matchups against every model tested.

"Generative video has historically forced developers to choose between quality and speed," said **Batuhan Taskaya, Head of Engineering at fal**. "By pairing the new capabilities of H3 Max and fal's post training we've proven that this tradeoff is no longer necessary. Together, we can push quality and performance at the same time."

**Building the model and inference system together**

H3 Max was developed by post-training MiniMax H3 with substantial new data, with a particular focus on prompt adherence and visual quality. fal trained the model using its in-house reinforcement learning framework, continuously evaluating checkpoints through human preference studies measuring overall quality, prompt understanding and aesthetics.

At the same time, fal's inference team optimized the systems stack around the evolving model.

Rather than optimizing latency after training was complete, fal co-designed the model and its inference engine. Performance optimizations were retained only when the resulting model preserved its quality gains, allowing H3 Max to achieve faster-than-real-time generation without sacrificing its position in quality evaluations.

The result demonstrates a broader approach to generative media infrastructure: treating model research and inference optimization as a single problem rather than two independent layers.

As video models become increasingly computationally demanding while moving into interactive and high-volume production workflows, fal believes model performance will increasingly be measured across the combined frontier of **quality, latency and cost**, rather than quality alone.

**Availability**

H3 Max is available today through the **fal API, Playground and fal Agent** for text-to-video and image-to-video generation.

For the first week following launch, fal is offering H3 Max at 50% off.

**Text to Video:** fal.ai/models/minimax/h3-max/text-to-video
**Image to Video:** fal.ai/models/minimax/h3-max/image-to-video

**Pricing**

H3 Max is one of the best video generation models on the market, and its low price point makes fal an accessible platform for developers, creators, designers, and companies generating video at scale. At 768p, H3 Max costs just $0.04 per second during the promotional launch period. That means a social media creator can generate a 5-second clip for $0.20, a 10-second TikTok or Instagram asset for $0.40, or a 30-second piece of content for $1.20. A designer producing multiple concept animations could generate ten 10-second clips for just $4.00, while an advertising team creating twenty 15-second variations for campaign testing would spend $12.00 in generation costs. Even a full 60-second 768p video costs only $2.40. These promotional launch rates are 50% off for a limited time and end September 7, after which 768p generation will cost $0.08 per second, $0.80 for a 10-second clip, $2.40 for 30 seconds, and $4.80 for a 60-second video.

**About fal**

fal is the generative media platform for developers and enterprises, providing access to production-ready image, video, audio and 3D models through high-performance inference infrastructure. fal enables teams to build and scale generative media applications with fast inference, reliable infrastructure and access to leading models.

**Benchmark methodology**

Independent leaderboard rankings referenced above reflect publicly available results from Design Arena and Artificial Analysis as of August 26, 2026. Rankings may change as additional models and evaluations are added.

fal's internal evaluation compared H3 Max against 12 leading video models using head-to-head human preference testing across overall preference, prompt understanding and aesthetics. Results were aggregated using Bayesian Elo ratings with 95% confidence intervals.

SOURCE fal

![](https://rt.prnewswire.com/rt.gif?NewsItemId=SF38264&Transmission_Id=202609011110PR_NEWS_USPR_____SF38264&DateId=20260901)
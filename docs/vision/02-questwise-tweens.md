# Questwise: Vision Document
### A COPPA-safe Socratic tutor and mastery worlds for ages 8–12, with curiosity and no pay-to-win

> **v1.1 update (29 Sep 2026):** see the [Project Reevaluation](../03-project-reevaluation.md) (engines, surfaces, trimmed MVP, waves) and [Studio Platform Features](../04-studio-platform-features.md). Each app doc's §15 holds its verdict and new features.

| | |
|---|---|
| **Venture** | 2 of 5 · Tweens |
| **Segment** | **8–12** (middle childhood); buyers are parents (35–59), homeschool and microschool educators, ESA programs and teachers |
| **One-liner** | The learning adventure that makes kids think, not copy, and never sells them a better sword. |
| **Mission** | Grow confident, curious thinkers who can do hard things: reason in math, read deeply, build with code, and use AI wisely. |
| **Vision (5 yrs)** | The default "safe and genuinely smart" learning platform for 8–12s, approved on ESA marketplaces, trusted by homeschool co-ops and classrooms, and backed by published learning gains. |
| **Business model** | Hybrid: B2C family subscription (≈$10–15/mo, $80–120/yr), **ESA-approved vendor**, microschool/co-op licences ($100–300 per student per year), and later district sales once efficacy data exists. |
| **Phase** | Discovery & Validation (no code) |

---

## 1. Why now
- **The 8–12 gap.** Kids this age are too old for preschool apps and too young for Gauth or ChatGPT, whose terms of service set a 13+ minimum. Frontier labs structurally under-serve under-13s, and **no COPPA-safe Socratic tutor leads** this age.
- **Parents are fed up with pay-to-win.** Prodigy draws a "constant battle", an FTC complaint alleging "up to four times as many ads as math questions", and IXL's SmartScore is called "rage-inducing".
- **The evidence works in our favour.** Guardrailed AI tutors produce gains of 0.2–0.4 SD (World Bank Nigeria; Harvard RCT at 2×). Unguarded AI lowers exam scores by 17% (Bastani 2025). We can design to that line.
- **The parent-directed channel is funded.** Examples: Texas's $1B ESA (2026–27), Tennessee's $7k per student, Florida's FES-UA disability awards, about 3M homeschooled children and about 75k microschools.
- **Kids want to learn in game worlds.** About 70% of 5–13-year-olds want to learn creative subjects in Minecraft- or Roblox-style worlds [V2], but those platforms have no academic loop and raise safety worries.

## 2. Who we serve

| Persona | Snapshot | Needs / wants | Pain today |
|---|---|---|---|
| **Jayden, 10** | Loves Minecraft. Finds fractions "boring". Gets stuck on homework at 8 p.m. | Help that feels like play. A way to get unstuck without feeling dumb. | Prodigy upsells. IXL score drops. Parents can't help with "new math". |
| **Priya, 11, dyslexic** | Strong at ideas, slow reader. Word problems stall her. | Read-aloud, extra time, questions she can answer by voice. | Timed games. Walls of text. |
| **Nicole, 41, parent of 2** | Works full time. Worries about AI cheating and screen time. | To see real progress. Fair price. No stranger chat. | Paywalls on children. AI that hands kids answers. |
| **Mr. Ortiz, microschool guide** | 14 mixed-age students (8–12); funded by an ESA. | Mastery tracking, low prep, ESA-reimbursable tools. | Juggling 6 disconnected apps. |
| **Aiden, 9, ADHD** | Energetic. Goes all-in on novelty and then drops off. | Short missions, movement breaks, visible progress. | Losing streaks. Long sessions. |

## 3. Needs → how Questwise responds

| Need / want (evidence) | Response |
|---|---|
| Homework help **without** cheating (teacher and parent VoC) | Sage Tutor is Socratic: it never gives the final answer and asks the child to "show your thinking" |
| Fun **without pay-to-win** or ads (Prodigy complaints) | Rewards are cosmetic and earned by learning only. No paid currencies, no ads, and one fair subscription |
| Support for **struggling learners**, not only gifted ones (Beast Academy gap) | Mastery paths with scaffolds, read-aloud, voice answers and no timers |
| **Proof of learning** parents can see | A weekly "what I can do now" summary written in plain language |
| **AI literacy and online safety** (EO 14277; state AI-literacy standards) | AI Detectives |
| **Creative making** (Scratch/Minecraft love) | Builder's Lab and Wonder Lab |
| **Executive function** and homework routines | Mission Control |
| **No stranger chat** (Roblox fears) | Co-op play only with invited family and classmates. No open chat |

## 4. The seven apps

| # | App | Ages | User need/want addressed | Core experience |
|---|---|---|---|---|
| 1 | **Sage Tutor** | 8–12 | Getting unstuck on homework without copying; patience at 8 p.m. | A Socratic AI homework coach. Child answers by voice, typing, drawing or photo. Hints first, never the final answer. Parent-visible summaries |
| 2 | **Math Realms** | 8–12 | Mastery in math that feels like adventure; no timers or pay-to-win | An explorable world where each region is a math domain. Progress is gated on mastery, and tutoring is built in |
| 3 | **Read Rangers** | 8–12 | Reading comprehension and fluency for all readers, including dyslexic ones | Leveled texts built around the child's passions (human-curated, AI-leveled), read-aloud with highlighting, and discussion quests |
| 4 | **Builder's Lab** | 9–12 | Creative coding and maker projects that go beyond block "tutorial hell" | A project-based path from blocks to text coding, with an AI pair-programmer that explains without writing the code for you |
| 5 | **AI Detectives** | 9–12 | Understanding AI, spotting fakes, staying safe online | Case-based mysteries: spot deepfakes, test chatbots, learn how models make mistakes, practise safe prompting |
| 6 | **Wonder Lab** | 8–12 | Curiosity and real-world science | Camera- and sensor-powered experiments and nature journaling, plus "ask a scientist" with a human-reviewed AI guide |
| 7 | **Mission Control** | 8–12 | Homework planning, focus and independence | A visual planner that breaks assignments into missions, with calm focus timers, movement breaks and a family routine board |

**Shared layer, the Questwise Guild Hub:**
- parent dashboard and educator dashboard (for microschools and classrooms)
- ESA invoicing
- "My Needs" profile, carried over from Lanternling
- co-op play with invited friends only

### App cards

#### 1. Sage Tutor
- **Problem:** Kids get stuck on homework and parents can't help. Answer apps (Gauth, Photomath) teach copying, and their terms of service exclude under-13s anyway.
- **Experience:** The child snaps, types or says the problem. Sage asks what they already know, gives graduated hints, and checks understanding with a "try one like it" problem. It celebrates *reasoning*, not answers.
- **AI role:**
  - An LLM under strict tutoring policies: hint ladder, no final answers, curriculum alignment.
  - A math verifier checks every step (avoiding "272 − 172 = 430" errors).
  - Topic and safety filters, and escalation to a parent for off-topic distress.
- **Accessibility & sensory:** Voice or typed input, read-aloud, dyslexia-friendly type, no timers, Calm or Balanced dial. Screen-reader-friendly math output (MathML/speech).
- **Parent role:** Sees a session summary ("worked on dividing fractions; needed 2 hints; tried 3 similar problems"). Does **not** see a word-by-word transcript by default. Transparency is set to the child's age.
- **Riskiest assumption:** Kids stay engaged when the tutor won't hand over the answer.
- **Validation test:** A Wizard-of-Oz tutor (a human tutor following the Sage policy) for 2 weeks with 20 families. Measure completion, frustration events, and parent and child ratings.

#### 2. Math Realms
- **Problem:** Game-based math either pushes paid upgrades (Prodigy) or feels like punishment (IXL).
- **Experience:** Regions such as Fraction Forest and Ratio River unlock through **mastery**, not time spent. Puzzles are open-ended, a "prove it" mode is included, and cosmetic rewards are earned by learning.
- **AI role:** Learner model and knowledge graph. Picks next problems. Sage is available as an in-world guide.
- **Accessibility & sensory:** No timers. Tap alternatives to drag. Sensory Dial. Read-aloud word problems.
- **Riskiest assumption:** Mastery-gated progress stays fun without variable-ratio rewards.
- **Validation test:** Paper-prototype a "region" in 3 microschools. Compare persistence against a points-based variant.

#### 3. Read Rangers
- **Problem:** Comprehension and stamina drop at ages 8–12, especially for dyslexic or reluctant readers.
- **Experience:** Kids pick passions (sharks, soccer, space). They get texts at their level with read-aloud and highlighting, then discussion quests: "What would you do?", or "Find the evidence".
- **AI role:** Levels human-curated texts. Asks Socratic comprehension questions. Tracks fluency through optional read-aloud.
- **Accessibility & sensory:** BDA typography, a background tint, adjustable reading speed, and answers by voice or typing.
- **Riskiest assumption:** Interest-matched texts improve stamina more than a curated library does.
- **Validation test:** A 3-week A/B concierge with printed texts (n=30). Measure minutes read and comprehension probes.

#### 4. Builder's Lab
- **Problem:** Kids stall after block-coding tutorials. AI tools write the code for them.
- **Experience:** Kids make their own projects (games, animations, simple robots), following a path from blocks to Python. There is a "build log" portfolio.
- **AI role:** A pair-programmer that explains errors and asks guiding questions. **No full solutions.**
- **Accessibility & sensory:** Keyboard and screen-reader-friendly editor. Voice coding commands. High-contrast theme.
- **Riskiest assumption:** Parents will pay for coding once free Scratch and Code.org exist.
- **Validation test:** A smoke test of a "project club" offer, plus 10 in-depth parent interviews on willingness to pay.

#### 5. AI Detectives
- **Problem:** Kids use AI without understanding it. Deepfakes and scams target children.
- **Experience:** Weekly mysteries: "Is this photo real?", "Why did the chatbot get this wrong?", "Which prompt is safe to share?"
- **AI role:** Controlled demos of AI failures in a sandbox. Explains how models work.
- **Accessibility & sensory:** Narrated cases, captions, and plain-language glossaries.
- **Riskiest assumption:** Schools and ESA families will prioritize AI literacy, given the new state standards.
- **Validation test:** Classroom paper-case pilot with 3 teachers. Measure teacher adoption intent.

#### 6. Wonder Lab
- **Problem:** Curiosity fades when science is screen-only. Parents want hands-on activities.
- **Experience:** Kitchen and backyard experiments guided on the phone (camera, sound meter, timer). A nature journal. A "wonder wall" of questions.
- **AI role:** Species and object identification. Human-reviewed Q&A guide. Safety checks on experiments.
- **Accessibility & sensory:** Alternatives for children with limited mobility. Audio descriptions. Low-cost kit options.
- **Riskiest assumption:** Families will actually do off-screen experiments that an app prompts.
- **Validation test:** Mail printed experiment cards to 20 families for 3 weeks. Measure completion and photo submissions.

#### 7. Mission Control
- **Problem:** Tweens are learning to manage homework, and many (especially those with ADHD) struggle with starting tasks and keeping track of time.
- **Experience:** Assignments become missions with visual steps, calm focus timers, movement breaks, and a family routine board. Parents can see what's done.
- **AI role:** Breaks a task into steps (like Goblin Tools) and estimates time. The child edits the plan.
- **Accessibility & sensory:** Visual, audio and haptic reminders. A gentle streak with pause days.
- **Riskiest assumption:** Tweens will adopt a planner themselves rather than have a parent run it.
- **Validation test:** A 2-week diary study using a paper mission board vs. a Figma prototype.

## 5. Product principles (Questwise-specific)
1. **Think, don't copy.** AI never removes the productive struggle. It scaffolds it.
2. **Earned, never bought.** Rewards come from learning only. No paid currencies, loot boxes or ads.
3. **Play with people you know.** No open chat. Co-op only with invited friends.
4. **Every learner is a Ranger.** Struggling and neurodivergent learners get first-class paths, not remediation ghettos.
5. **Parents see progress, and kids keep dignity.** Summaries, not surveillance.

## 6. Business model and go-to-market
- **Priority 1:** ESA marketplaces (AZ, FL, TN, TX from 2026–27, IA, and others), plus homeschool co-ops and microschools (parents choose, the state pays).
- **Priority 2:** B2C family plan (≈$12/mo or $99/yr for up to 3 kids) and a free tier (limited Sage sessions, 1 Math Realms region).
- **Priority 3:** A free teacher tier in classrooms (Chromebook web) to build the brand. District sales only after ESSA Tier 3 evidence.
- **Moat:**
  - a learner model plus outcome data
  - ESA vendor approvals and integrations (ClassWallet, Odyssey)
  - a homeschool community
  - a brand trusted by parents because it has no pay-to-win

## 7. Ethics, safety and compliance
- **COPPA 2025:**
  - All users are under 13.
  - Verifiable parental consent and separate consent for AI training (off by default).
  - Data minimization.
- **AI safety:** Tutor not friend. Distress escalation to parents. Topic filters. Human-reviewed content.
- **Kids-category rules:** No third-party ads or trackers. Parental gates.
- **Stress and pressure:** No streak shaming, no public leaderboards by default, and friend-only visibility.

## 8. Risks and mitigations
| Risk | Mitigation |
|---|---|
| Incumbents (Prodigy, Khan/Khanmigo, IXL) | Differentiate on Socratic homework help, no pay-to-win, and first-class paths for struggling and ND learners |
| Kids reject Socratic friction | A hint ladder with a "show me a similar example" escape. Test in Wizard-of-Oz |
| ESA political reversal | Diversify across states plus B2C and microschools |
| Phone bans at school | Design for home and after-school use, plus school Chromebooks |

## 9. Discovery and validation focus
- **Top assumptions:** Socratic engagement for under-13s; parents will pay (or ESAs reimburse) for no pay-to-win; microschools want one platform; mastery-gating is fun.
- **North-star:** *Weekly mastered skills per active learner*. Guardrails: frustration events per session, Sensory Comfort Rating ≥4/5, parent trust score.
- **Three-year ambition:**
  - Year 1: Sage Tutor + Math Realms MVP, and ESA approval in 3 states.
  - Year 2: Read Rangers, Mission Control and AI Detectives.
  - Year 3: an ESSA Tier 2 study and district pilots.

# Speak Freely: App Strategy & Product Specification

> **Venture:** Evergrow · **App #:** 3/7 · **Ages:** 20+ (core 25–59; 60+ supported via the large-type preset) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/04-evergrow-adults.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Evergrow index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research note:** Searched 29 Sep 2026. Store pages could not be fetched (egress proxy), so download and rating figures come from the studio's earlier store research (repo raw/01–02), and pricing from 2026 secondary reviews.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Real conversations for real life: daily AI speaking practice built around *your* situations, a short human tutor check-in that steers what the AI does next, and no streak guilt. |
| **Primary user / buyer** | Adults 20+ who are stuck at A2–B1 and want to talk to in-laws, colleagues, neighbours or travel hosts. Buyer: the learner (B2C); later employers (language-for-work) and gift purchasers. |
| **Core job-to-be-done** | "When I've done hundreds of app lessons but still freeze in a real conversation, I want low-stakes speaking practice on the exact situations I face, with a real person checking in, so I can finally hold a conversation." |
| **Category on the stores** | Education › Language learning |
| **Top competitors (by downloads / revenue)** | Duolingo (Max/Video Call), Babbel, Speak, Praktika, Learna, Busuu, Memrise, ELSA, Pimsleur, italki, Preply, Loora |
| **Our wedge** | 1) **Talk + Tutor loop**: a human tutor meets the learner briefly and *programmes* the AI practice for the next week, so the two are joined up rather than separate products. 2) **Speak-or-type path**: full progress for people who stutter, have speech disabilities or are anxious about speaking. 3) **No streak guilt, human-crafted curriculum** in answer to the Duolingo backlash. |
| **Business model** | Freemium to subscription. AI-only $14/mo; **Plus $29/mo** (AI + weekly small-group check-in or twice-monthly 1:1); Pro $59/mo (weekly 1:1). Annual discounts; gift plans. |
| **North-star metric** | Real-world conversations reported per active learner per month (self-reported "I used it" moments), with CEFR speaking gains checked by tutors each quarter |
| **MVP candidate?** | **Later (Year 2).** The price test and a 4-week concierge run in discovery. |

## 2. Problem & users
**Problem statement**
- The biggest consumer learning apps build habits, not speaking:
  - Duolingo is the category leader, with 58.7M DAU and 12.7M paid subscribers in Q2 2026 [V] (repo).
  - Reviewers and Reddit communities consistently describe a plateau and learners who "complete courses without being able to hold real conversations" [V2].
  - Duolingo's 2025 Energy system drew heavy backlash; in one poll of 11,000+ users nearly half actively disliked it [V2].
  - The AI-first memo prompted "AI slop" complaints [V] (repo).
- AI conversation apps prove willingness to pay for speaking:
  - Duolingo Max (Video Call with Lily) costs $29.99/mo or $168/yr [V2].
  - Speak Premium costs $17.99/mo or $83.99/yr; Premium Plus is $39.99/mo or $164.99/yr [V2].
  - Praktika reports ~$20M revenue and 2M+ MAU [V2].
- **Human-plus-app hybrids are hard.** Babbel shut **Babbel Live for consumers on 1 July 2025**, saying most individual learners did not adopt live classes, and reviewers report the unlimited-class pricing was unprofitable [V2]. Live classes now remain only in Babbel for Business [V2]. **Lesson [I]:** the human part must be short, scheduled, included in the price, and tied directly to the practice, not an unlimited catalogue of classes.
- Tutoring marketplaces show demand and price points. Preply raised $150M in Q1 2026 (the largest EdTech round of the quarter) [V] (repo). Tutors average $10–15/hr on Preply [V2], and italki lessons run ~$4–40 [V].
- Voice-first scoring excludes people. ELSA, Praktika and Learna rely on speech scoring [V2] (repo), and ASR accuracy varies sharply across speech disorders such as stuttering and dysarthria [V2].

**Personas**
1. **Lena, 31**, learning Spanish for her partner's family (vision). She has a 400-day Duolingo streak and can't hold a conversation. She wants practice for "meeting the grandparents" and "phone call with the landlord", plus a human who notices her progress.
2. **Sam, 36, person who stutters.** Voice-scored apps mark him wrong and time out. He needs a text-chat path that still counts, voice practice with unlimited wait time, and no fluency penalty for disfluency.
3. **Gloria, 66, retired teacher with hearing loss** (vision). She wants to learn Italian for a trip. She needs captions for everything, a slowed AI voice, hearing-aid streaming, large type and an unhurried tutor.

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Speaking beyond B1 | Plateau complaints [V2]; Babbel "tops out at B2" [V2] (repo) | CEFR path to B2+ with scenario practice |
| No punishment for using the app | Energy backlash [V2] | Unlimited practice on paid plans; free tier has a daily *topic* limit, never an energy meter |
| Human connection and trust | "AI slop" backlash [V] (repo) | Tutor check-ins; published human-crafted policy |
| Affordable human time | Babbel Live closed for B2C [V2] | Short, scheduled check-ins; small groups |
| Accessibility for speech/hearing | ASR disparities [V2]; Lumen P7 | Speak-or-type; captions; adjustable speech rate |
| Personal scenarios | Pimsleur/Speak users value early speaking [V2] (repo) | "My Situations" builder |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Duolingo** | Duolingo Inc. | 500M+ Play; 178M downloads 2025; Q2 2026 58.7M DAU, $298.5M revenue [V] (repo) | Super ~$12.99/mo; **Max $29.99/mo or $168/yr** [V2] | 4.7 (repo) | Habit; free; Video Call with Lily adapts and "remembers past chats" [V2] | Energy system; streak burnout; AI slop; plateau [V]/[V2] | VoiceOver inconsistent; drag tiles; loud celebrations (repo) | [beginnersinai](https://beginnersinai.org/duolingo-max-explained/), [Duolingo help](https://www.duolingo.com/help/what-is-duolingo-max) |
| **Babbel** | Babbel GmbH | €352M revenue 2024 [V2]; top-5 grossing Android education [V2] (repo) | $17.99/mo, $89.99/yr, lifetime $299 (repo); Group Plan $30.95/mo for up to 6 users (Apr 2026) [V2] | 4.7 (repo) | Structured grammar; calm UI; practical dialogues | Tops out at B2; **Live closed for consumers Jul 2025** [V2] | Calmer UI suits older users (repo) | [dealnews](https://www.dealnews.com/features/babbel/plan-pricing/), [strommeninc](https://strommeninc.com/why-babbel-live-shut-down-and-what-to-use-instead-2025/) |
| **Speak** | Speak Inc. | 10M+ Play; $1B valuation (Dec 2024) (repo) | Premium $17.99/mo or $83.99/yr; Premium Plus $39.99/mo or $164.99/yr [V2] | 4.7–4.8 (repo) | Lots of speaking reps; natural AI tutor | Price; speech-centric [V2] | Speech-only paths exclude some (repo) | [speakshark](https://speakshark.com/blog/speak-app-pricing-per-month-2026) |
| **Praktika** | Praktika.ai | 15M downloads, 2M+ MAU; ~$20M revenue; $38M raised [V2] | Subscription (weekly/annual) [E] | 4.5–4.8 (repo) | Lifelike avatars; practice without a human audience | Uncanny avatars; paywall; repetitive (repo) | Subtitles; voice-first (repo) | [Latka](https://getlatka.com/companies/praktika.ai), [Tracxn](https://tracxn.com/d/companies/praktika-ai/__8aJt_nF9BORjN1ty2cYCRfOHlrHe9bd97Pqor9WIvzQ) |
| **Learna** | Codeway | 50M+ Play; 32M downloads 2025; #2 US Education (2026) [V] (repo) | Hard paywall; ~$9.99/wk [E] (repo) | 4.6 (repo) | Low-pressure AI chat | Paywall right after onboarding; weekly plans (repo) | ASR struggles with speech differences (repo) | repo raw/01–02 |
| **ELSA Speak** | ELSA Corp. | 10M+ Play (repo) | Premium from ~$13.33/mo; Business $18.20/user/mo [V2] | 4.6 (repo) | Phoneme-level pronunciation | Strict scoring (repo) | May penalise speech impairments (repo) | [Capterra](https://www.capterra.com/p/240698/ELSA-Speak/) |
| **Pimsleur** | Simon & Schuster | Serious-learner favourite (repo) | All Access $20.95/mo; $164.95/yr renewal [V2] | n/a | Audio-first; early speaking | Little reading/writing; price (repo) | Audio-first helps low vision (repo) | [speakfluentreviews](https://speakfluentreviews.com/pimsleur-cost/) |
| **italki / Preply** | italki; Preply | Preply $150M raise Q1 2026 [V] (repo) | italki ~$4–40/lesson [V]; Preply avg $10–15/hr [V2] | n/a | Real humans; flexible | Tutor quality varies; no practice between lessons; scheduling effort [V2] | Depends on tutor | [italki pricing](https://www.italki.com/en/blog/italki-price), [Brighterly](https://brighterly.com/blog/preply-cost/) |

Also noted: **Busuu** (community corrections, declining [E]), **Memrise** (native-speaker video, AI chat), **Loora** (10M+, 4.9 [V] (repo)).

### Feature matrix
| Feature | Duolingo Max | Babbel | Speak | Praktika | ELSA | Pimsleur | italki/Preply | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| AI open conversation | ✓ | partial | ✓ | ✓ | partial | ✗ | ✗ | **Parity** |
| Personal scenario builder | ✗ | ✗ | partial | partial | ✗ | ✗ | ✓ (tutor) | **Differentiate** ("My Situations") |
| Human tutor included | ✗ | ✗ (B2C) | ✗ | ✗ | ✗ | ✗ | ✓ (paid per lesson) | **Differentiate:** short check-ins that programme the AI |
| Text-only path counted as progress | partial | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | **Differentiate (Lumen)** |
| Pronunciation feedback | partial | partial | ✓ | ✓ | ✓ | ✗ | ✓ | **Parity**, with disfluency-tolerant scoring |
| CEFR path to B2+ | partial | ✓ (to B2) | partial | partial | ✗ | partial | ✓ | **Improve:** tutor-verified CEFR speaking checks |
| Energy / hearts limits | ✓ (free) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject** |
| Loss-framed streaks | ✓ | partial | partial | partial | partial | ✗ | ✗ | **Reject** → gentle weekly goals with pause days |
| AI "calls you" unprompted | ✓ (Lily calls occasionally) [V2] | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject:** intrusive; only user-scheduled reminders |
| Avatar with emotional persona | partial | ✗ | partial | ✓ | ✗ | ✗ | ✗ | **Reject companion framing;** the AI is a labelled practice partner |
| Weekly billing | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | **Reject** |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| F1 | **AI Conversation Partner** | Scenario-based voice or text conversations adapted to CEFR level, with a clear "AI practice partner" label | Speak/Duolingo Max parity [V2] | Parity | MVP | Must |
| F2 | **Talk + Tutor Loop** ★ signature | A 15-min check-in (weekly in a group of up to 3, or twice monthly 1:1 on Plus). The tutor hears a 2-min "show me" conversation, sets 2 focus goals and assigns next week's scenarios, which the AI then runs. | Babbel Live lesson [V2]; human trust [V] | Differentiate | MVP | Must |
| F3 | **Speak-or-Type** ★ | Every activity completable by typing; progress and CEFR checks count equally. Voice mode has unlimited wait time and disfluency-tolerant recognition. | Sam persona; ASR disparities [V2] | Lumen / Differentiate | MVP | Must |
| F4 | **My Situations** | The learner describes real situations ("dinner with Marco's parents in Bologna"). Human-written scenario templates are adapted by AI and checked by the tutor. | Personal relevance | Differentiate | MVP | Must |
| F5 | **Gentle progress map** | CEFR "can-do" map, weekly goals, pause days, no loss framing | Duolingo streak burnout [V2] (repo) | Lumen | MVP | Must |
| F6 | **Replay & repair** | After each conversation: transcript, 3 corrections, "say it again" drill on the learner's own mistakes | Busuu/ELSA parity | Parity | MVP | Must |
| F7 | **Adjustable voices** | Speech rate 0.6–1.2×, repeat, slow replay, accent choice, captions always on by default | Gloria persona | Lumen | MVP | Must |
| F8 | **Pronunciation coach (optional)** | Phoneme-level hints, *off by default for learners who set "don't score my speech"* | ELSA parity [V2] | Improve | MVP | Should |
| F9 | **Tutor console** | Tutor sees transcripts the learner chose to share, sets goals, writes 3-line notes; notes become AI prompts | Makes the loop work | Differentiate | MVP | Must |
| F10 | **Human-crafted curriculum** | Scenario bank and grammar notes written and reviewed by linguists; AI-generated variations sampled by editors | "AI slop" backlash [V] (repo) | Differentiate | MVP | Must |
| F11 | **My Needs + 60+ preset** | Captions, large type, hearing-aid streaming, dyslexia settings | Lumen | Lumen | MVP | Must |
| F12 | **Fair billing** | Price before trial, reminder, one-tap cancel, pause, gift plans | Charter | Lumen | MVP | Must |
| F13 | Tutor asynchronous voice notes | Tutor replies to 1 recorded conversation per week with a 60-s voice/text note | Cheaper human touch | Improve | V1 | Should |
| F14 | Quarterly CEFR speaking check | 20-min tutor-rated speaking check against CEFR descriptors; a certificate that states "tutor-assessed, not an official exam" | Proof of progress | Differentiate | V1 | Should |
| F15 | Languages for work | Employer plans: healthcare Spanish, hospitality English | B2B path; ELSA Business [V2] | Parity | V1 | Could |
| F16 | Conversation clubs | Monthly moderated peer clubs (captioned video or text) | Community | Improve | V2 | Could |
| F17 | Offline audio drills | Pimsleur-style offline sessions | Commuters | Parity | V2 | Could |

MVP launch languages: Spanish, Italian, French, German, English (for Spanish speakers). MVP = F1–F12.

## 5. Core experience & key user flows
**Core loop.** Open → today's scenario, chosen by the tutor's goals → 5–10 min conversation (voice or text) → replay & repair (3 fixes) → "used it in real life?" tap (optional) → done screen → weekly tutor check-in closes the loop.

**Flow 1: Onboarding (≤5 min)**
1. Sign in with a passkey, Apple/Google, or a magic link.
2. Choose a language and a reason ("family", "work", "travel").
3. The My Needs card asks: voice, text or both? Captions (on by default)? Speech speed? Text size?
4. A 3-minute level chat (text or voice) estimates CEFR.
5. First scenario conversation. First value by about 4 minutes. The tutor booking is offered and not required.

**Flow 2: Daily practice**
1. The Now/Next/Done strip shows "Warm-up → Conversation → Fixes → Done".
2. Conversation: the AI waits indefinitely, and "Help me say it" gives a hint ladder (keyword → sentence starter → model answer).
3. Replay & repair: 3 corrections, each with "try again", which can be skipped.
4. Done screen suggests a real-world action ("Try ordering your coffee in Spanish tomorrow"). Natural end; no "one more lesson".

**Flow 3: Tutor check-in**
1. Book from 3 suggested slots (or a fixed weekly slot) with time-zone clarity and a calendar file.
2. Video with live captions, or audio-only, or **text chat for learners who prefer it**.
3. The tutor runs a 2-min conversation, gives 2 goals and assigns scenarios. Notes are shown to the learner in plain language.
4. The AI practice for the week adapts, and the learner sees "Set by your tutor, Ana".

**Flow 4: Tutor console.** Schedule → learner card (level, goals, shared transcripts) → notes template → assign scenarios → done. Target ≤3 minutes of admin per learner per week.

**Flow 5: My Needs.** One tap from any screen. Covers the Sensory Dial, voice speed, captions, "don't score my speech", text size and the 60+ preset.

**Flow 6: Billing.** Plan page shows the total price and what human time is included, a pause of up to 3 months, and one-tap cancel. Missed tutor sessions can be rescheduled once. Human time does not expire until the end of the billing month.

**IA.** Today · Practice (scenarios) · Tutor · Progress map · My Needs.

**Session design.** Default 10 minutes (range 5–25). At 20 minutes a gentle "Good time for a break?" appears; it can be dismissed and never blocks. Every session ends on the done screen.

## 6. Inclusive, accessible & sensory design spec
- **Sensory Dial.** Default **Balanced** (Calm if the OS Reduce Motion setting is on). Calm: no music, no celebration sounds, static progress. Lively (opt-in): gentle chime and short animation on goal completion. There is never a "wrong" buzzer. Corrections use a neutral tone and colour plus an icon.
- **Input modes.** Conversation: voice, typing (with an accent keyboard helper), switch-accessible phrase chips, AAC-generated speech accepted. Pronunciation drills: voice, or "listen and choose" alternative.
- **Targets.** ≥48 dp; **≥56 dp in the 60+ preset**. Phrase chips are ≥56 dp tall. No drag.
- **Typography.** 18 px body default (20+ px in the 60+ preset); transcripts reflow; dyslexia settings; the target language is shown with optional romanisation/phonetics.
- **Audio and hearing.**
  - Captions are on by default for all AI and tutor speech.
  - Separate volume for the AI voice, effects and tutor.
  - Mono audio option.
  - Streaming to Bluetooth hearing aids (MFi/ASHA/LE Audio) via the OS, with no app audio paths that bypass system routing.
  - Speech rate control and "repeat slower".
  - Visual waveform or "listening" indicator plus a haptic when the AI starts and finishes talking.
- **Speech disabilities.**
  - The text path is fully equivalent.
  - Voice mode never auto-cuts the learner off: endpointing waits 10 s by default, adjustable to "until I tap done".
  - Pronunciation scores can be off.
  - Disfluencies (repetitions, blocks) are not scored as errors.
- **Themes.** "Café" (warm photo) and "Plain" (neutral). No mascot and no avatar faces by default (optional illustrated partner).

| # | Principle | Acceptance criterion in Speak Freely |
|---|---|---|
| P1 | Calm | Reduce Motion → 0 animations; no autoplay audio on open |
| P2 | Sound | 3 separate sliders; captions for 100% of speech; peak loudness capped |
| P3 | Predictable | Same 4-step session; tutor check-in structure fixed |
| P4 | Targets | 48/56 dp; no drag |
| P5 | Plain language | UI copy ≤ grade 7; grammar notes have plain versions |
| P6 | Typography | WCAG 1.4.12 passes in transcripts |
| P7 | Multimodal | Every activity passes with text only; voice-only activities = 0 |
| P8 | Low penalty | No hearts/energy; unlimited retries; "skip for now" |
| P9 | Focus | Designed end screen; no autoplay-next |
| P10 | Memory | Passkeys; the scenario goal stays on screen during conversation |
| P11 | Timing | Voice endpointing adjustable to manual; no timed answers |
| P12 | My Needs | All accessibility free on every tier |
| P13 | Age-respectful | 2 adult themes; peer-aged voices |
| P14 | Low admin | Tutor admin ≤3 min per learner per week |
| P15 | Gentle progress | Weekly goals, pause days, no loss-framed notifications |
| P16 | Affirming | Stuttering guidance reviewed with people who stutter (e.g., via a stuttering association panel) |
| P17 | Honest claims | No "fluent in X weeks"; CEFR check labelled "tutor-assessed" |
| P18 | Privacy | Voice audio deleted after processing by default; no emotion inference |

**Lumen audit target:** 24/24.

## 7. AI specification & guardrails
**Does**
- Conversational LLM constrained by scenario scripts, CEFR vocabulary lists and tutor goals.
- ASR (multi-accent, disfluency-tolerant) and TTS with adjustable rate.
- Correction extraction.
- Pronunciation analysis (optional).
- Scenario adaptation from human templates.

**Does not**
- Present itself as a friend or partner, initiate calls, or use romance or dependency mechanics. It is a *practice partner*: labelled, with no memory of personal life details beyond what the learner saves as "My Situations".
- Infer emotion or "confidence" from voice.
- Produce curriculum without human review.

**Pedagogy**
- Comprehensible input plus pushed output.
- Hint ladder; recasts rather than explicit "wrong".
- Spaced review of the learner's own errors.
- Tutor-set goals override the adaptive engine.

**Safety**
- Content filters on scenarios.
- If a learner raises distress (e.g., during an immigration or bereavement scenario), the AI steps out of role, offers resources, and tells the tutor only if the learner agrees.
- AI disclosure on every conversation screen (EU AI Act Art. 50).

**Evaluation**
- WER by speaker group (L1 background, age 60+, stuttering, dysarthria, hearing-aid users' speech) on a consented test set. **Gate:** no group WER >2× the reference group, or voice mode for that group defaults to "confirm what I heard" with editable transcripts.
- Correction precision ≥90% on a linguist-labelled set.
- Weekly human sampling of 2% of conversations (with consent) for quality and "slop".

**Cost [E].** Voice conversation ~$0.02–0.04 per minute (ASR+LLM+TTS). An active learner doing 150 min/month costs ~$3–6/month in AI. **Tutor economics:**
- Plus, group of 3, 4 × 20 min/month: ~27 tutor-min per learner ≈ $8 at a $18/hr loaded rate. That is ~28% of $29, which meets the discovery threshold of tutor cost ≤35% of revenue (Discovery Plan E2).
- Pro, weekly 1:1 15 min: ~$18 on $59 (≈31%).

## 8. Data, privacy & compliance
| Data | Purpose | Retention | Processing |
|---|---|---|---|
| Voice audio | ASR | Deleted after transcription unless the learner saves clips | Cloud ASR with zero retention; on-device where feasible |
| Transcripts | Replay, tutor | 12 months, learner-deletable; shared with the tutor only by opt-in per conversation | Cloud |
| My Situations | Personalisation | Learner-controlled | Cloud |
| Tutor notes | Loop | Contract period | Cloud |
| Voiceprints / biometrics | **Not collected** | – | – |

**Regimes.**
- GDPR (voice may be special-category data if used for identification; we do not do this).
- BIPA-style biometric laws avoided by not creating voiceprints.
- EU AI Act Art. 50 (disclosure) and Art. 5 (no emotion recognition).
- FTC §5 on outcome claims.
- Tutor contractor classification per country.

**Consent.** Separate opt-ins for saving audio, sharing transcripts with the tutor, and using data to improve models (default off).

**Store.** 17+/Teen rating is not required; the app is not designed for children. Accessibility Nutrition Label at launch.

## 9. Monetization & go-to-market
| Plan | Price | Includes | Benchmark |
|---|---|---|---|
| Free | $0 | 3 scenarios/week, text + voice, full accessibility | Duolingo free (Energy) [V2] |
| Speak Freely | $14/mo or $99/yr | Unlimited AI practice | Speak $17.99 [V2]; Duolingo Super ~$12.99 [V2] |
| **Plus** | $29/mo or $249/yr | + weekly group check-in (≤3) or 2 × 1:1 per month | Duolingo Max $29.99 [V2]; Babbel Group $30.95/6 users [V2] |
| Pro | $59/mo | + weekly 1:1 15 min + monthly asynchronous notes | italki/Preply per lesson [V]/[V2] |
| Gift | 3/6/12 months | Any plan | Gifting to 60+ |

- **Channels:** content-led (bilingual family stories), partner communities (expat and in-law groups), employer language benefits (V1), libraries (V2, 60+).
- **ASO:** "speak Spanish conversation", "AI conversation practice", "language tutor", "stuttering-friendly language app" (accessibility is a keyword). Accessibility Nutrition Label.
- **Markets:** US (Spanish, Italian, French), UK/IE, then DACH (English for German speakers). Tutor supply from Latin America and Europe.

## 10. Success metrics
- **North star:** real-world conversations reported per active learner per month (target ≥3 by month 3).
- **Inputs:**
  - practice minutes per week (≥40)
  - tutor check-in attendance (≥80%)
  - scenarios completed from tutor goals (≥70%)
  - text-path users' retention equal to voice-path users
- **Outcomes:**
  - CEFR speaking sub-level gain per quarter (tutor-rated, second-rater sample for reliability)
  - Evidence plan: pre/post with blinded tutor ratings (Tier 2); a study vs. an AI-only arm (V2).
- **Guardrails:**
  - Sensory Comfort ≥4/5
  - speaking anxiety (short FLCAS-style item) not worse than baseline
  - WER gates
  - tutor cost ≤35% of revenue
  - zero billing complaints
- **Retention:** D1 ≥45%, D7 ≥25%, **D30 ≥15%** for free (vs. a 2–5% education-app median (repo)); Plus paid monthly churn ≤6%; DAU/MAU ≥20%.

## 11. Validation plan
**Riskiest assumptions**
1. The hybrid model is viable at $20–30/mo (vision; Babbel Live failure).
2. Learners attend short check-ins; the Babbel lesson says unlimited classes didn't stick.
3. Tutor-programmed AI practice beats AI-only on speaking gains and retention.
4. The text path retains speech-disabled users equally.

| # | Experiment | Sample | Success | Kill |
|---|---|---|---|---|
| X1 | Landing-page price test ($14 / $29 / $59) | Adults via paid social | ≥8% waitlist; ≥30% choose Plus or Pro | <3% or <10% choosing human tiers |
| X2 | **4-week concierge:** real tutors; AI practice run Wizard-of-Oz (scripted prompts in an existing LLM chat with human-curated scenarios) | n=20 (incl. 4 people who stutter or have hearing loss; 4 aged 60+) | ≥80% attend ≥3 of 4 check-ins; ≥70% would pay $29; tutor time ≤30 min per learner per month | <60% attendance |
| X3 | AI-only vs. AI+tutor arms within X2 | 10 v 10 | Tutor arm: +0.5 on self-rated speaking confidence and more practice minutes | No difference |
| X4 | Text-path usability | 6 participants who stutter or have speech disabilities | SUS ≥75; "felt respected" ≥4/5 | <3.5 |
| X5 | Tutor supply test | Recruit 10 tutors via a marketplace | ≥6 accept $18/hr for 15-min slots with notes | <3 |

**Mapping.** WP2 (diary study of speaking moments), WP4 (X2–X4), WP5 (X1, X5; Discovery Plan E2 threshold: tutor cost ≤35% of revenue).

## 12. Build handoff
**Epic A: Conversation engine**
- Given voice mode with endpointing "until I tap done", when the learner pauses 30 s, then the AI does not speak or advance.
- Given text mode, when a conversation is completed, then it counts toward goals identically to voice.
- Given any AI utterance, then a caption appears within 300 ms of audio start.

**Epic B: Talk + Tutor Loop**
- Given a tutor saves 2 goals, when the learner opens Today, then at least 1 of the next 3 scenarios reflects a goal and is labelled "Set by your tutor".
- Given the learner declines to share a transcript, then the tutor console shows "not shared" and no content.

**Epic C: Progress**
- Given the learner misses a week, then no notification uses loss language, and the weekly goal resets with "Welcome back".

**Epic D: Billing**
- Given a Plus subscriber, when they tap Cancel, then it completes in ≤2 taps. Remaining tutor sessions in the paid month stay bookable.

**Non-functional requirements**
- Voice turn latency <1.2 s p95.
- Offline review of saved transcripts.
- iOS, Android and web.
- WCAG 2.2 AA.
- Localisation of UI in 5 languages.
- Tutor PII separation; SOC 2 path.

**QA focus**
- AT matrix: VoiceOver/TalkBack in a mixed-language context; correct `lang` attributes so screen readers switch pronunciation.
- Hearing-aid streaming on iOS/Android test devices.
- ASR speaker-group WER suite.
- Sensory A/B: Calm vs. Balanced.
- AI safety: role-break on distress, refusal of romantic or companion requests.
- Billing: pause/resume, gifts.
- COPPA: N/A (age gate 18+; 13–17 routed to Ascendly).

**Dependencies.** Lumen DS, My Needs, voice stack (shared with Silver Circuit), tutor scheduling service, evidence engine.

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Hybrid economics fail as Babbel Live did | Med | High | Small groups, fixed slots, notes-first tutor workflow, AI does the volume |
| Duolingo Max and Speak add human features | Med | Med | Loop integration and accessibility as the moat |
| Tutor quality variance | Med | Med | Calibration, learner ratings, training on accessibility |
| ASR fails for some groups | Med | High | Text parity; confirm-what-I-heard; WER gates |
| AI conversation drifts into companion territory | Low | High | Persona constraints; red-team; no unsolicited calls |

**Open questions.** Group check-ins vs. 1:1: which drives retention? Should tutors be employed or marketplace contractors? Is Spanish-for-in-laws a big enough initial wedge?

## 14. Sources
- [V2] Duolingo Max pricing and Video Call: https://beginnersinai.org/duolingo-max-explained/ · https://www.duolingo.com/help/what-is-duolingo-max · https://duoplanet.com/duolingo-video-call/
- [V2] Duolingo complaints / Energy poll: https://www.myengineeringbuddy.com/blog/duolingo-reviews-pricing-alternatives-2026/ · https://checkthat.ai/brands/duolingo/reviews
- [V2] Speak pricing: https://speakshark.com/blog/speak-app-pricing-per-month-2026
- [V2] Praktika: https://getlatka.com/companies/praktika.ai · https://tracxn.com/d/companies/praktika-ai/__8aJt_nF9BORjN1ty2cYCRfOHlrHe9bd97Pqor9WIvzQ
- [V2] Babbel Live consumer shutdown: https://strommeninc.com/why-babbel-live-shut-down-and-what-to-use-instead-2025/ · https://www.change.org/p/stoppt-die-einstellung-von-babbel-live-privat-stop-discontinuation-of-babbel-live-private · https://support.babbel.com/hc/en-us/sections/26053368846866-Babbel-Live
- [V2] Babbel pricing/revenue: https://www.dealnews.com/features/babbel/plan-pricing/ · https://www.businessofapps.com/data/babbel-statistics/
- [V] italki pricing: https://www.italki.com/en/blog/italki-price · [V2] Preply rates: https://brighterly.com/blog/preply-cost/
- [V2] Pimsleur pricing: https://speakfluentreviews.com/pimsleur-cost/ · [V2] ELSA pricing: https://www.capterra.com/p/240698/ELSA-Speak/
- [V2] ASR and atypical speech: https://www.jmir.org/2025/1/e60520/ · https://arxiv.org/pdf/2509.25048 · https://www.frontiersin.org/journals/language-sciences/articles/10.3389/flang.2025.1569448/full
- Repo: research/raw/01 and 02 (store figures for Duolingo, Learna, Speak, Praktika, ELSA, Loora, Babbel), raw/03 (Duolingo backlash VoC), raw/05 (Duolingo Q2 2026, Preply raise, benchmarks)

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (stand-alone consumer app; re-scope the human layer) |
| **Ships in** | Speak Freely (S5) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 70/100 [I] |
| **Consumes engines** | EN-07, EN-09, EN-11 |
| **Studio features used** | SX-24, SX-26 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = F1, F2, F3, F4, F6, F10.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| SF-E1 | **Small-group check-ins by default** | 4–6 learners per human session instead of 1:1, to fix unit economics after Babbel closed its consumer live classes (Jul 2025) [V2]. |
| SF-E2 | **Community conversation hosts** | Vetted, paid heritage speakers and retirees from Evergrow Circle host conversations: intergenerational supply that also gives hosts purpose. |

### 15.3 New validation question
Group check-in satisfaction ≥ 1:1 minus 0.5 points, with tutor cost ≤35% of revenue.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 4 | 4 | 3 | 3 | 3 | 3 | 3 |

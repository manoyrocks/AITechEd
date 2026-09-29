# Studio Platform Features & Shared Engines (v1.1 enhancements)

**Version:** 1.1 · **Date:** 29 September 2026 · **Status:** Discovery & Validation (specs only, no code)
**Why this exists:** the [project reevaluation](03-project-reevaluation.md) found five problems:
- The 35 app specs define **597 features, 408 of them tagged MVP**.
- **The same capability is specified 3–7 times over**: grandparent voice in 4 apps; scam training in 4; body doubling in 3; routines/timers in 6; weekly summaries in about 20.
- **No specs exist** for:
  - the family's lifecycle across ventures
  - a studio-wide subscription
  - a trust center
  - notification limits
  - IEP preparation
  - caregiver wellbeing
  - remote co-play
  - in-product evidence

This document moves shared capabilities into **12 engines** and adds **33 studio-wide features (SX-01…SX-33)**. Building a feature once enhances every experience that uses it.

**Tags:** [V] verified · [V2] secondary · [M] memory, verify in WP1 · [E] estimate · [I] inference. **Tiers:**
- **P-MVP:** the platform must have it before any Wave-1 experience ships.
- **V1 / V2:** later releases.
- **D:** validate in discovery before committing.

---

## 1. The 12 shared engines

| Engine | Responsibility | SX features | Experiences that consume it |
|---|---|---|---|
| **EN-01 Identity, Family & Consent** | One family account; roles (child, teen, adult, grandparent, professional); COPPA/AADC consent states; age assurance; age-up transitions | SX-01, SX-03, SX-11 | All 35 |
| **EN-02 Lifelong Learner Passport** | My Needs profile, Sensory Dial 2.0, skills and portfolio records, export | SX-02, SX-12 | All 35 |
| **EN-03 Tutor Engine** | One guardrailed tutoring core with age-tuned policies (hint ladders, verified solvers, citations, answer-leak prevention), embedded in context, plus adult CoPilot mode | SX-17 | Sage Tutor, Study Coach, Math Realms, Read Rangers, Builder's Lab, Exam Ready, Explain It Back, Draft Mentor, AI Fluency Lab |
| **EN-04 Reading Continuum** | One reading skill model from phonemic awareness to adolescent comprehension; decodable generator; read-along; dyslexia layer | SX-20 | Story Lantern, Sound Garden, Read Rangers, ReadWave, Exam Ready (reading) |
| **EN-05 Routine, Regulation & Focus** | Visual schedules, Now/Next/Done, transition warnings, timers, breathing and haptics, body doubling, reward fading | SX-19 | Calm Cubs, Mission Control, Study Squad, Wavelength Day, Calm Harbor, Focus Crew |
| **EN-06 Safety, Scam, AI & Media Literacy** | One case library adapted by age (7–90+); scam sandbox; real-or-synthetic lab; intergenerational missions | SX-18 | AI Detectives, Life Ready, Silver Circuit (Scam Gym), AI Fluency Lab (responsible-AI checkpoints) |
| **EN-07 Family Voice, Languages & Co-play** | Private family voice recordings, heritage-language packs, co-play prompts, remote co-play sessions | SX-06, SX-07 | Babble Buddy, Tap & Wonder, Story Lantern, Two Words, Curiosity Circle, Speak Freely |
| **EN-08 Pathways & Skills** | Simulations, skills maps, portfolios, employer and college connections, accommodations coaching | SX-21 | Pathfinder, Career Sprint, AI Fluency Lab, Social Compass (self-advocacy) |
| **EN-09 Voice, Speech & AAC Services** | On-device ASR/TTS; child-speech and speech-difference tolerance; AAC as an input method everywhere; natural voices | SX-16, SX-22 | Babble Buddy, Sound Garden, ReadWave, Wavelength Voice, Speak Freely, Silver Circuit, all voice input |
| **EN-10 Progress, Evidence & Content Studio** | Mastery records, Family Digest, embedded assessment, micro-randomized trials, human-in-the-loop content pipeline, provenance labels | SX-04, SX-31, SX-32, SX-33 | All 35 |
| **EN-11 Safe Live & Group Rooms** | Friends-only or host-led rooms, co-presence, captioned live sessions, moderation, sensory room presets | (supports SX-06, SX-26) | Study Squad, Focus Crew rooms, Mission Control body doubling, Curiosity Circle, Silver Circuit classes, Speak Freely group check-ins, Lead with AI cohorts |
| **EN-12 Trust & Safety** | Trust Center, AI transparency, safeguarding operations, red-teaming, notification budget | SX-05, SX-08, SX-09, SX-10 | All 35 |

**Rule for app teams:** an experience **consumes** an engine and may **extend** it by proposing changes to the engine owner. It never re-implements the engine. See the [Unified Agent-Team Prompt §7](agent-team/unified-agent-team-prompt.md).

---

## 2. Studio-wide features

### A. Family lifecycle

#### SX-01 Studio Family Account & Family Pass (P-MVP)
- **What:** one sign-in and one bill for a whole household: up to 5 children, 2 caregivers and 2 grandparent seats. It spans Lanternling, Questwise and Ascendly, and includes a free Evergrow Circle basic seat for grandparents.
- **Why:**
  - Today a family with a 3-year-old and a 10-year-old pays for two separate plans ($69 + $99 a year), and more if a child is neurodivergent.
  - Parents already report confusion over app sprawl and bundles, for example the Piknik bundle [M].
- **Acceptance criteria:**
  - One checkout.
  - Adding a child never needs a new payment method.
  - Siblings of different ages sit under one plan.
  - Grandparents are invited by link.
  - Accessibility and Wavelength accommodations are never paywalled.
  - Fair-billing charter flows apply everywhere.
- **Pricing hypothesis [E]:** see §3.

#### SX-02 Lifelong Learner Passport (P-MVP)
- **What:** a single learner-owned record that follows the learner from age 1 to 90+. It unifies:
  - the My Needs profile
  - mastery records
  - the Ascendly Record portfolio
  - the Evergrow Skills Passport
  - Wavelength goals
- **Acceptance criteria:**
  - The learner (or their guardian before the age of transfer) can view, export (JSON + PDF) and delete it.
  - Each entry shows its source experience and its evidence tier.
  - Portability is tested across two ventures.

#### SX-03 Age-up & graduation transitions (P-MVP)
- **What:** designed transitions for each age milestone:

| Age | Transition |
|---|---|
| **13** | COPPA parental consent → teen controls, with parents notified of the change (AADC) |
| **16/18** | Record ownership transfers to the learner. Parents' access ends unless the learner grants it |
| **Venture graduation** | Lanternling → Questwise → Ascendly → Evergrow, with a consented handoff of the reading profile, My Needs and portfolio |

  Wavelength runs **in parallel** at any age and never "graduates" anyone out of accommodations.
- **Why:** none of the 35 specs defines what happens when a learner ages out. That is a churn point and a compliance risk.
- **Acceptance criteria:**
  - Each transition is shown to the learner and the caregiver 30 days ahead, in plain language.
  - Nothing transfers without consent.
  - The learner keeps their Sensory Dial and My Needs profile with no re-setup.

#### SX-04 Family Digest (P-MVP)
- **What:** one weekly one-screen summary per family, covering all children and all experiences. It replaces the roughly 20 separate per-app weekly summaries.
- **Acceptance criteria:**
  - One digest, readable in ≤60 seconds.
  - Available as audio, Easy Read and in the caregiver's language.
  - Teens (13+) approve what their parents see.
  - Every co-play suggestion links to an off-screen activity.

#### SX-05 Notification Budget (P-MVP)
- **What:** a studio-wide cap on notifications.
  - Default: ≤3 caregiver notifications a week.
  - **None to devices of children under 13.**
  - Quiet hours.
  - Teens set their own budget.
- **Why:** Lumen P9 and P14 ban engagement nudges, but no spec enforces this across apps. The UK AADC also prohibits nudge techniques.
- **Acceptance criteria:** a central scheduler enforces the cap across experiences. QA verifies no experience can bypass it.

#### SX-06 Remote Co-play (V1)
- **What:** a caregiver or grandparent in another home joins a co-play session by link, with no install (web).
  - Synced story pages (Story Lantern), scenes (Tap & Wonder) or word games (Two Words).
  - Video is optional.
  - Uses the 60+ large-type preset.
- **Why:** intergenerational co-play is a core value of Lanternling and Evergrow, but no spec supports it at a distance.
- **Acceptance criteria:**
  - Join in ≤3 taps from an SMS or email link.
  - Works on a tablet or TV browser.
  - The child's side stays in the calm default.
  - No recording by default.

#### SX-07 Family Voice & Languages layer (V1)
- **What:** private family voice recordings and heritage-language packs, recorded once and usable in every kids' experience. It replaces four separate "grandparent voice" features (TW-12, SL-07, TWO-02, BB-16).
- **Acceptance criteria:**
  - Recordings are family-private, never used for training, and deletable.
  - Record by link or by phone call (SX-26).
  - Every recording is available across Lanternling experiences.

### B. Trust & safety

#### SX-08 Guardian & Learner Trust Center (P-MVP)
- **What:** one place, in both a child-readable and an adult version, showing:
  - what data we hold and why
  - every consent and its state
  - what the AI did (an activity summary for under-13s; for teens, only what they choose to share)
  - who can see what
  - export and delete
- **Acceptance criteria:**
  - In testing, ≥80% of parents can answer "what did the AI do with my child this week?" in ≤2 minutes.
  - Deletion is completed and confirmed.

#### SX-09 AI transparency cards (V1)
- **What:** a "Why this?" card on every AI recommendation, placement or rubric score. It shows the inputs used, the confidence, and how to challenge or override it.
- **Why:** EU AI Act Art. 50 transparency, and preparation for the Annex III high-risk obligations in education (Dec 2027).
- **Acceptance criteria:**
  - Present on every placement and grade-like output.
  - Includes a human-override path.

#### SX-10 Safeguarding operations (P-MVP)
- **What:**
  - distress-escalation protocols by age and market
  - localized crisis resources (e.g., 988 in the US, Childline and Samaritans in the UK) [M, verify per market]
  - a named safeguarding lead
  - incident response
  - a mandated-reporting policy reviewed by counsel
  - a quarterly red-team cadence
- **Acceptance criteria:**
  - Escalation is triggered only by what users **say**; no emotion inference.
  - Median time to a human response is set per market.
  - Drills are run and documented.

#### SX-11 Platform age assurance (P-MVP)
- **What:** use platform age signals rather than collecting birthdates ourselves, where the platform offers them:
  - Apple Declared Age Range API
  - Google Play Age Signals API [M: confirm API availability and state-law status in WP1]
  - parent approval flows
- **Acceptance criteria:** the minimum data needed to route a user to the right age experience.

### C. Inclusion 2.0

#### SX-12 Sensory Dial 2.0 and the Sensory Passport (P-MVP)
- **What:**
  - **Learner-owned sensory presets** that follow the learner across experiences.
  - **Time-of-day presets**, e.g., bedtime is calm.
  - A one-tap **"too much"** button that tunes presets by self-report.
  - An exportable one-page **Sensory & Support Passport** for schools, clinicians, hospitals and childcare.
- **Acceptance criteria:**
  - A preset set once applies in every experience.
  - The passport is learner-approved.
  - The passport prints on one page, in Easy Read.

#### SX-13 Deaf-first pack (V1)
- **What:**
  - **Human-signed** ASL/BSL video for key content (stories, instructions, Social Compass scenarios).
  - Visual alerts for every audio event.
  - A caption quality standard.
  - No signing avatars in place of human signers without Deaf community approval.
- **Acceptance criteria:** Deaf co-designer panel sign-off, and caption accuracy ≥99% on scripted content.

#### SX-14 Audio-first mode for blind and low-vision learners (V1)
- **What:** audio-first versions of core loops in kids' experiences, including data sonification (Wonder Lab) and audio math (Tutor Engine). This goes beyond screen-reader compatibility.
- **Acceptance criteria:** blind testers complete the core loops of Wave-1 kids' experiences unaided.

#### SX-15 Easy Read & plain-language layer (P-MVP)
- **What:** every adult-facing text is available in Easy Read and plain language: consent, digest, IEP exports, billing. It is also translated into the caregiver's language. Templates are human-checked.
- **Acceptance criteria:** consent comprehension ≥85% in testing with low-literacy and intellectually disabled adults.

#### SX-16 AAC as input everywhere (V1)
- **What:** Wavelength Voice symbols and keyboard can be used to answer in **any** studio experience, via a shared input method, with no copy-pasting.
- **Acceptance criteria:** an AAC user completes a Sage Tutor, Read Rangers and Explain It Back task using AAC input only.

### D. Learning & AI

#### SX-17 Embedded Tutor + Adult CoPilot (P-MVP)
- **What:** EN-03 appears **in context** at error moments, inside every learning experience, instead of living only in a separate tutor app.
  - It **politely offers help after two misses**.
  - Learners can turn it off.
  - **Adult CoPilot mode** suggests to parents, microschool guides and teachers how to help without giving the answer. This follows the Tutor CoPilot pattern: +9 percentage points for students of lower-rated tutors [V].
- **Why:** a 2026 Khanmigo study found students used the tutor in only **17%** of practice sessions where they made an error [V2]. A separate tutor app repeats that failure.
- **Acceptance criteria:**
  - Tutor uptake at error moments is ≥40% in Wizard-of-Oz tests.
  - Answer-leak rate ≤1%.
  - The CoPilot is rated helpful by ≥70% of guides.

#### SX-18 Safety, Scam, AI & Media Literacy engine (V1)
- **What:** one human-authored case library with age-adapted versions for 7–12, 13–19, adults and 60+. It adds **"teach your grandparent / learn from your grandchild" family missions**.
- **Replaces** four separate scam and AI-literacy builds.
- **Acceptance criteria:**
  - Each case exists in at least 2 age versions.
  - Intergenerational missions are tested with ≥10 families.

#### SX-19 Routine, Regulation & Focus engine (P-MVP)
- **What:** one engine that brand skins (Lanternling cubs, Questwise missions, Ascendly squads, Wavelength neutral) sit on top of. It provides:
  - schedules
  - transition warnings
  - visual timers
  - breathing and haptics
  - body doubling
  - reward-fading plans
- **Acceptance criteria:**
  - A routine created in Calm Cubs appears in Wavelength Day for the same child, with consent.
  - One timer implementation passes the flash and loudness tests.

#### SX-20 Reading Continuum (V1)
- **What:** one reading skill model with a consented handoff of the reading profile:
  - Sound Garden → Read Rangers
  - or Sound Garden → ReadWave, when early signals suggest dyslexia risk. The handoff is **never a label**; the caregiver chooses.
- **Acceptance criteria:** the reading level and supports carry over, with no re-placement needed.

#### SX-21 Pathways engine (V1)
- **What:** continuity from Pathfinder (teen) to Career Sprint and AI Fluency Lab (adult). Adds:
  - disability and accommodations coaching for college and work
  - an apprenticeship and CTE finder
  - an ND-friendly employer pathway
- **Acceptance criteria:** a teen portfolio carries into Career Sprint with the learner's consent.

#### SX-22 On-device AI tier (D → V1)
- **What:** on-device models for child speech and simple language tasks, with cloud escalation only when needed. Possible routes: platform on-device frameworks such as Apple's Foundation Models framework or Android on-device GenAI APIs [M: verify capabilities and age terms in WP1].
- **Why:** COPPA 2025 treats voice as personal information, and parents trust "stays on the device". It also enables offline use.
- **Acceptance criteria:** a feasibility spike measures child-speech WER and latency by speaker group on consented samples.

### E. Reach & access

#### SX-23 Low-bandwidth & low-end device mode (V1)
- **What:**
  - offline content packs
  - installs under 150 MB
  - support for Android Go-class devices
  - PWA parity for Chromebooks
- **Why:** Android dominates learning-app volume globally, including in India, LatAm and Indonesia. Low-income families' devices are older.
- **Acceptance criteria:** Wave-1 experiences pass on a reference low-end device profile.

#### SX-24 Localization roadmap (V1)
- **What:**
  - Launch: en-US, es-US.
  - Next: pt-BR and es-MX (EFL), en-GB, then hi, ar (RTL) and fr.
  - Content is culturally reviewed, never machine-only.
- **Acceptance criteria:** every language has a native-speaker review sign-off. RTL layout tests pass.

#### SX-25 Print & Play / screen-free layer (P-MVP)
- **What:** every experience has a printable or audio-only alternative for its core loop:
  - routine cards
  - decodable take-home books
  - math missions
  - Lantern Mode audio, exportable to audio players where partners allow
- **Acceptance criteria:** each Wave-1 experience ships ≥1 screen-free path. The Family Digest suggests one each week.

#### SX-26 No-app access: phone/IVR & SMS (V1)
- **What:**
  - Seniors without smartphones join Silver Circuit and Curiosity Circle by phone dial-in, and can call a "scam check" line.
  - Families can get Babble Buddy prompts and Two Words recordings by SMS.
- **Acceptance criteria:** a senior with a landline completes a class and a scam check.

### F. Caregivers & professionals

#### SX-27 IEP/EHCP Prep Coach (V1; Wavelength priority)
- **What:**
  - A plain-language explainer of evaluation reports.
  - A question builder for meetings.
  - A progress-evidence pack drawn from Wavelength and Lanternling/Questwise data.
  - A rights explainer linking to official sources. **It is not legal advice.**
- **Why:** caregivers of ND children report being overwhelmed. No spec supports the IEP meeting itself.
- **Acceptance criteria:** in a concierge test, ≥70% of parents report feeling "more prepared" (n=15).

#### SX-28 Caregiver wellbeing & peer support (V1)
- **What:**
  - Short self-care and co-regulation resources for caregivers.
  - Moderated peer groups for parents of ND children.
  - A respite and resource finder.
  - A burnout self-check (self-report only).
- **Acceptance criteria:** moderation policy approved, and crisis routing through SX-10.

#### SX-29 Funding Navigator (V1)
- **What:** guidance on:
  - ESA eligibility and approved-vendor status
  - Medicaid and insurance for speech-generating devices
  - EHCP
  - scholarships
- **Also:** letter and documentation templates for SLPs and OTs.
- **Acceptance criteria:** covers the 5 launch ESA states + UK EHCP. Content is reviewed quarterly.

#### SX-30 Pro Console (P-MVP, web)
- **What:** one web console for all professional roles:
  - teachers
  - microschool guides
  - SLPs, OTs and BCBAs
  - counselors
  - employers (aggregate only)
  - libraries and aging agencies

  It includes rostering (Clever/ClassLink), IEP goal mapping, assignment, and review queues.
- **Acceptance criteria:** WCAG 2.2 AA. Role-based data minimization. Employers never see individual transcripts.

### G. Evidence & operations

#### SX-31 Evidence Engine 2.0 (P-MVP)
- **What:**
  - Embedded, low-burden assessments.
  - **Pre-registered micro-randomized trials** in the product (e.g., hint styles, calm vs. lively rewards).
  - Outcome dashboards.
  - A public **evidence page** for each experience, showing its evidence tier.
- **Acceptance criteria:**
  - Every experiment is pre-registered.
  - Consented research data is kept separate from product data.

#### SX-32 Content Studio (P-MVP)
- **What:** a human-in-the-loop content pipeline:
  1. AI draft
  2. expert edit
  3. ND, cultural and safety review
  4. publish, with a **provenance label** ("Human-crafted, AI-assisted") and version history
- **Why:** trust in human-crafted content is the #5 unmet need, following Duolingo's "AI slop" backlash.
- **Acceptance criteria:** no generated child-facing content ships without passing through human review.

#### SX-33 Accessibility conformance automation (V1)
- **What:** each release generates an Apple Accessibility Nutrition Label, a Google Play accessibility declaration (where available) and a VPAT/ACR from test results.
- **Acceptance criteria:** the labels match what QA measured, and are never self-declared without tests behind them.

---

## 3. Pricing: Studio Family Pass (hypotheses to validate in WP5) [E]

| Plan | Covers | Hypothesis |
|---|---|---|
| **Free** | Core loops of every experience, all accessibility and accommodations, Trust Center, Family Digest | Free forever |
| **Family Pass** | Lanternling + Questwise + Ascendly Plus for up to 5 children; 2 grandparent seats (Evergrow Circle basic); Remote Co-play; Family Voice | ≈$14.99/mo or $119/yr |
| **Family Pass+** | Family Pass + Wavelength full suite (excluding Wavelength Voice licence) + IEP Prep Coach + Speak Freely AI tier for one adult | ≈$21.99/mo or $179/yr |
| **Wavelength Voice** | Standalone AAC; never mutes if a subscription lapses; supporter accounts free | One-time or subscription (decided at the build-vs-partner gate) |
| **ESA / school / employer / library / health plan** | Licences through the Pro Console | Per learner, per seat or per branch |

**Kill threshold:** if Family Pass converts worse than separate venture plans in the WP5 price test, keep venture plans but add a sibling discount.

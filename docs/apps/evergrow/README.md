# Evergrow: App Specifications Index

> **v1.1 update:** every app below now has **§15 Reevaluation & enhancements** (verdict, surface, wave, trimmed MVP, new features). See the [Project Reevaluation](../../03-project-reevaluation.md) and [Studio Platform Features](../../04-studio-platform-features.md).

> **Venture:** Evergrow (adults 20–34, 35–59, 60+): hands-on AI fluency and lifelong learning, humans in the loop, no streak guilt
> **Status:** Discovery & Validation (specs only, no code) · **Date:** 29 Sep 2026
> **Parent docs:** [Venture vision](../../vision/04-evergrow-adults.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [App template](../_TEMPLATE.md)
> **Confidence tags:** [V] verified this session · [V2] secondary · [M] memory · [E] estimate · [I] inference

## 1. The seven apps

| # | App | Ages | Signature feature(s) | Top competitors benchmarked | MVP tier |
|---|---|---|---|---|---|
| 1 | [AI Fluency Lab](01-ai-fluency-lab.md) | 20–59 | **Workflow Sandboxes** (role-specific practice on synthetic real-work data) + **rubric grader with human review** feeding the Skills Passport | Coursera (+Udemy), LinkedIn Learning, Google AI Essentials, Microsoft Elevate/Applied Skills, DataCamp, Section, Multiverse, Mimo | **MVP, Year 1 (lead app)** |
| 2 | [Career Sprint](02-career-sprint.md) | 20–34 | **Sprint Studio** (employer-briefed portfolio projects with a process log) + **Fair Interview Coach** (practice only; no stealth copilot, no affect scoring) | Coursera/Google Career Certificates, Forage, Handshake, Final Round AI, Yoodli, Big Interview, Springboard, Seekho | Year 2 (concierge sprint in discovery) |
| 3 | [Speak Freely](03-speak-freely.md) | 20+ | **Talk + Tutor Loop** (a short human check-in programmes the AI practice) + **Speak-or-Type** parity | Duolingo Max, Babbel, Speak, Praktika, Learna, ELSA, Pimsleur, italki/Preply | Year 2 (price test + concierge in discovery) |
| 4 | [Lead with AI](04-lead-with-ai.md) | 35–59 | **Change Room** branching simulations for AI rollout, ethics incidents and reskilling, with debriefs and playbooks | LinkedIn Learning, Harvard ManageMentor, BetterUp, Skillsoft CAISY, Mursion, Section, Coursera for Business, Blinkist/Imprint/Headway | Year 2 (may ship first as a track inside AI Fluency Lab) |
| 5 | [Parent Coach](05-parent-coach.md) | 25–59 | **Tonight's Script** (tied to the child's real activity in studio apps) + **AI Talk Kit** | ClassDojo, Khan Academy/Khanmigo, Common Sense Media, Bark, Qustodio, Kinedu, Huckleberry, Understood.org | Later: validate as a retention engine in the Lanternling/Questwise pilots |
| 6 | [Silver Circuit](06-silver-circuit.md) | 60+ | **Scam Gym** (safe in-app scam simulations) + **Helper Handshake** (consent-based family help) + peer-guide live classes | GetSetUp, Senior Planet (AARP/OATS), Oasis, TechBoomers, AARP Fraud Watch Network, Google Be Scam Ready, Lively, GrandPad, BrainHQ | **Year 1 library pilots** (concierge first, app after Gate 2) |
| 7 | [Curiosity Circle](07-curiosity-circle.md) | 55+ | **Circles** (8–12 people, human host, captioned live sessions) + AI Study Buddy + Legacy Projects | GetSetUp, Great Courses/Wondrium, MasterClass, Babbel, Simply Piano/Yousician, Elevate/Lumosity/BrainHQ, Ancestry/FamilySearch, OLLI | Pilot cohorts now; app Year 2–3 |

**Sequencing (vision §9).**
- Year 1: AI Fluency Lab with 5 paying employers; Silver Circuit library pilots.
- Year 2: Career Sprint, Speak Freely, Lead with AI.
- Year 3: MA plan contract and a published skills-outcome study.
- Parent Coach and Curiosity Circle are validated through pilots before product investment.

## 2. Shared features (the Evergrow platform layer)

| Shared feature | What it is | Used by | Key rules |
|---|---|---|---|
| **Skills Passport** | A learner-owned, portable record of verified skills with evidence (artefact + rubric + reviewer), exportable as Open Badges 3.0 / verifiable credential | 1, 2, 4 (and 3 for tutor-assessed CEFR checks) | Credentials need human review. The learner decides what to share. Revoking sharing takes effect within 1 minute. Never used as an automated hiring or promotion tool (keeps us outside Annex III / NYC LL144 / Illinois HB 3773 duties). |
| **Employer console** | Seats, SSO/SCIM, track assignment, LMS/LXP connectors, aggregate skills insight, AI-literacy records | 1, 4 (and 2 for hiring partners / workforce boards) | **No surveillance analytics:** no per-person time-on-app, no prompt or transcript access, no rankings; team metrics suppressed below 5 people. Employees see what the employer can see before first use. |
| **Family-helper access (Helper Handshake)** | A trusted person (adult child, librarian) can help set up, suggest lessons and see progress, **only with the senior's explicit, revocable consent** | 6, 7 (and 5 for multi-caregiver sharing) | Big-type consent screen listing what the helper can and cannot see. The senior is notified of every helper action. No access to messages, money or location. Supported decision-making allowed; the senior confirms. |
| **60+ large-type preset** | One switch in the "My Needs" profile | Default in 6 and 7; available in all apps | Body text 20 px (never below 18 px); targets ≥56 dp (64 dp primary); contrast ≥7:1; no timeouts; captions on; speech rate 0.85× default; mono audio; hearing-aid streaming via OS; linear flows; icon + text labels; passkey / library-card / assisted sign-in (WCAG 3.3.8). |
| **My Needs profile** (studio-wide) | Sensory Dial, reading, input, pace, language, look, people | All 7, portable across the five ventures | All accommodations free on every tier. No diagnosis required. |
| **Speak-or-type path** | Every voice interaction has a full text/tap equivalent that counts equally | 2, 3, 4, 6, 7 | ASR word-error-rate gates by speaker group (accents, 60+, stuttering, dysarthria); voice endpointing adjustable to "until I tap done". |
| **Human-crafted + AI-assisted policy** | Published policy: humans write and review curriculum, grade credentials, host cohorts and tutor | All | Direct answer to the Duolingo "AI slop" backlash. Humans in the loop are part of the value and are never cut to save cost. |
| **Fair-billing charter** | Price before trial, reminder 3 days before conversion, one-tap cancellation, pause, no weekly plans, gifts never auto-bill the recipient | All B2C | Zero billing complaints is a guardrail metric in every app. |
| **Scam-safe communications** | We never ask for payment, passwords or codes by phone, text or email. Messages to 60+ learners carry their chosen safe word. | All (mandatory for 6, 7) | Guide callbacks only at learner-booked times. |

## 3. Features we reject, and why (combined list)

| Rejected feature | Seen in | Why we reject it |
|---|---|---|
| Hearts / Energy limits on learning | Duolingo (free tier Energy system) | Punishes practice ("So now we're punished for using the app?"); violates Lumen P8 |
| Loss-framed streaks, streak-loss notifications, guilt pushes | Duolingo, Mimo, Simply Piano, brain-training apps | Streak burnout and "dread" drive adults away; we use weekly goals and pause days (P15) |
| AI that phones or messages the learner unprompted | Duolingo Max ("Lily will call you occasionally") | Intrusive; companion-like; for 60+ it mimics scam patterns |
| Companion / friend personas, romance or dependency mechanics | AI companion apps; some avatar tutors | Evergrow AI is a labelled tutor or practice partner. Connection comes from people (tutors, guides, cohorts). |
| Emotion, affect, eye-contact or "confidence" scoring from face or voice | Some interview and simulation tools | EU AI Act Art. 5 bans emotion recognition in workplace and education; disability and cultural bias |
| Live "stealth" interview copilots | Final Round AI | Deceptive; employers ban them (Amazon); candidates risk rescinded offers |
| Individual employee surveillance dashboards (time-on-app, prompt contents, rankings) for managers | Various LMS/LXP analytics | Destroys trust and psychological safety; works-council and GDPR risk; not needed to prove ROI |
| Using learning scores for automated hiring, promotion or termination | AEDT vendors | High-risk under EU AI Act Annex III; NYC LL144 / Illinois HB 3773 bias-audit duties; wrong purpose for learning data |
| Timed assessments and timed brain games | Coursera/LinkedIn exams, Lumosity, Elevate, Impulse, BrainHQ | Excludes slower processors, screen-reader users, motor-impaired users and many older adults (P11) |
| "Brain age", dementia-prevention or "clinically proven" claims without evidence | Brain-training category history | FTC Lumosity ($2M) and LearningRx precedents; FDA device boundary. Engagement-only claims, via the claims register (P17). |
| Covert scanning of children's messages and AI chats | Bark, Qustodio | Surveillance erodes parent–child trust. Parent Coach teaches conversations; teens see what parents see (P18). |
| Weekly billing plans, hard paywall right after onboarding, trial-to-annual without reminder | Learna, Praktika, Impulse, Headway, Brilliant | Fair-billing charter; billing traps are a top complaint across the category |
| Job guarantees | Springboard | Creates perverse incentives and fine-print disputes; we publish outcomes with methodology instead |
| Leaderboards and social comparison between learners or managers | Duolingo leagues, DataCamp XP | Anxiety and gaming; adults "forgive gamification but not manipulation" |
| Ads | TechBoomers, free tiers generally | Especially harmful to 60+ (scam look-alikes); against studio policy |
| Voice-only or camera-only input | ELSA, Praktika, Learna, Simply Piano (mic-only) | Excludes speech-disabled, Deaf/hard-of-hearing and AAC users (P7) |
| Accommodations behind a paywall | Common in the category | Accessibility is the product; all accommodations are free (P12) |

## 4. Cross-cutting guardrails (applies to all seven)
- **AI transparency.** Every AI surface is labelled (EU AI Act Art. 50). The published grader and rubric explanations are learner-visible.
- **EU AI Act Art. 4.** It supports employers' AI-literacy duty. After the June 2026 Digital Omnibus, the duty became an obligation of effort ("support the development of" AI literacy), with national enforcement powers from 2 Aug 2026 [V2]. We lead with productivity outcomes, not compliance fear.
- **Grader bias testing.** Matched-quality subgroup tests (non-native writers, dyslexic writers, dictation/screen-reader users, dialects, text vs. voice mode) before launch, quarterly, and on every model change. Maximum gap 0.25 rubric points.
- **Human review of credentials.** 100% for the first 6 months, then ≥20% risk-based sampling plus all appeals and borderline cases.
- **Sandboxes.** Isolated, synthetic data, PII scrubbing before any "bring your own task", zero-retention model terms.
- **No medical or dementia claims.** Silver Circuit and Curiosity Circle make engagement and connection claims only.
- **Lumen audit target.** ≥22/24 for every app; 24/24 for Speak Freely, Parent Coach, Silver Circuit and Curiosity Circle.

## 5. Go-to-market summary
| Channel | Apps | Notes |
|---|---|---|
| Mid-market employers (500–5,000 staff), LMS/LXP marketplaces | 1, 4 | $150–400 per seat per year; land with 20-seat pilots and ROI in 60 days |
| Workforce boards (WIOA ETPL), community colleges, university career centres | 1, 2 | Per-completer pricing; case-manager console |
| Hiring partners | 2 | Sponsored briefs; demo days |
| B2C subscriptions and gifts | 2, 3, 5, 6, 7 | Fair-billing charter; gift plans are never charged to the recipient |
| Public libraries, Area Agencies on Aging, senior centres, senior living | 6, 7 | First 60+ channel; price for local budgets (federal library funding uncertain [M]) |
| Medicare Advantage supplemental benefits | 6, 7 | Year 2–3; 9–18 month cycles; no PHI by design |
| Schools and districts (family engagement) | 5 | Bundled with Questwise/Ascendly |

## 6. Research caveats
- Web research ran on 29 Sep 2026 via search only. Direct page fetches (app stores, FTC, FBI IC3, company sites) were **blocked by the network egress proxy**, so [V] means a fact appeared in search results attributed to the named primary source.
- The session-wide web-search budget ran out partway through App 5. **Apps 6 (Silver Circuit) and 7 (Curiosity Circle) rely on the studio's earlier research files plus [M] items** (e.g., FBI IC3 elder-fraud totals, Senior Planet, AARP Fraud Watch, Google Be Scam Ready, Lively/GrandPad, MasterClass/Great Courses pricing, OLLI, IMLS and Digital Equity Act funding changes). All must be verified in Discovery WP1 before external use.
- Downloads and ratings for consumer apps come mainly from the studio's store research (research/raw/01–02). Several 2026 prices come from third-party review sites [V2].
- Company-reported outcomes (Forage interview/offer multipliers, Springboard placement rates, Mursion retention claims, Yoodli revenue growth) are marketing claims, not independent evidence.

# Ascendly: App Specs Index (ages 13–19)

> **v1.1 update:** every app below now has **§15 Reevaluation & enhancements** (verdict, surface, wave, trimmed MVP, new features). See the [Project Reevaluation](../../03-project-reevaluation.md) and [Studio Platform Features](../../04-studio-platform-features.md).

> **AI-native learning, not cheating. Proof-of-learning and future pathways.**
> **Status:** Discovery & Validation (specs only, no code) · **Date:** 29 September 2026
> **Parent docs:** [Venture vision](../../vision/03-ascendly-teens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Template](../_TEMPLATE.md)
> **Confidence tags:** [V] verified this session · [V2] secondary · [M] memory · [E] estimate · [I] inference

## The seven apps

| # | App | Ages | Signature feature | Top competitors benchmarked | MVP tier (vision) |
|---|---|---|---|---|---|
| 1 | [Study Coach](01-study-coach.md) | 13–19 | Attempt → 4-rung hint ladder → faded worked example → "your turn" → teach-it-back, with CAS-verified steps and MathML output | Gauth, Photomath, Brainly, Question.AI, ChatGPT for Teens / Study Mode, Gemini Guided Learning, Khanmigo, Studdy | **MVP (Year 1)** |
| 2 | [Exam Ready](02-exam-ready.md) | 14–19 | Readiness score with confidence bands on human-reviewed items + free, exportable spaced-retrieval flashcards + accommodations-native practice (1.5×/2×, read-aloud) | Quizlet, Khan Academy + Bluebook, Knowt, Anki, Fiveable, Seneca, Save My Exams, UWorld/Magoosh/PrepScholar | **MVP (Year 1, 1–2 exams)** |
| 3 | [Explain It Back](03-explain-it-back.md) | 13–19 + teachers | Any-mode explanation (voice, text, drawing, AAC, sign video) → adaptive "why?" follow-up → teacher-confirmed rubric feedback → class misconception heat map | Flip (retired), Edpuzzle, Nearpod, Wayground, MagicSchool, Brisk, Khanmigo teacher tools, Socrative, Seesaw | **MVP pilot (Year 1, 10 schools)** |
| 4 | [Draft Mentor](04-draft-mentor.md) | 13–19 | Question-led writing mentor that never writes paragraphs + teen-owned authorship timeline (assistive input counts as human) | Grammarly (Authorship, AI agents), QuillBot, Google Docs + Gemini, Turnitin Clarity, Brisk, NoRedInk, Quill.org, Draftback | Later (Year 2) |
| 5 | [Study Squad](05-study-squad.md) | 13–19 | Friends-only quiet co-study rooms (video/audio off) with a shared timer and teen-chosen phone lock-in; no loss mechanics | Forest, Opal, Focusmate, YPT, Study Together/StudyStream, Flora, Finch; Tiimo as design benchmark | Later (Year 2); Discord-bot pilot now |
| 6 | [Pathfinder](06-pathfinder.md) | 15–19 | Accessible 20-minute AI-run job simulations feeding an evidence-based skills portfolio; all paths (trades, CTE, dual enrollment, college) side by side | Naviance, Xello, Scoir, MajorClarity, BigFuture, Roadtrip Nation, CareerVillage, Forage, Handshake | Later (Year 3 sponsors) |
| 7 | [Life Ready](07-life-ready.md) | 13–19 | Scenario challenges + scam sandbox + "Is this real?" AI & media lab, calm Duolingo-grade polish without punishments | Greenlight, Step, Zogo, NGPF, Ramsey, Checkology, iCivics, Khan financial literacy; Duolingo as UX benchmark | Later; organic-pull test first |

**Recommended Year-1 build (post-Gate 2):** Study Coach + Exam Ready (Digital SAT math + one AP subject) + Explain It Back pilot, all on the shared layer below. This matches the vision doc's three-year ambition.

## Shared features (the Ascendly layer)

### 1. Ascendly Record (teen-owned proof-of-learning portfolio)
- **What goes in:** verified understanding moments (Study Coach teach-it-back and "your turn"), unit mastery and readiness history (Exam Ready), teacher-confirmed explanations (Explain It Back), authorship timelines (Draft Mentor), focus summaries (Study Squad), simulation skills evidence (Pathfinder), skills badges with evidence (Life Ready).
- **Principles:** private by default; the teen chooses what to share, with whom (teacher, parent, counselor, college/employer), and previews exactly what they'll see; process summaries, never transcripts or keystrokes; export any time (PDF + open JSON); deletable except copies already submitted to a school (which follow the school's retention).
- **North star it feeds:** *weekly verified understanding moments* (vision §9).

### 2. Teacher / counselor console (B2B)
- One web console (Chromebook-first) shared by Study Coach, Exam Ready, Explain It Back, Draft Mentor, Pathfinder and Life Ready.
- Class setup via Google Classroom, Clever, ClassLink; grade passback where relevant.
- Views are built only from **teen-shared** data and aggregates: misconception heat maps, unit readiness, writing process summaries, exploration activity.
- **Human oversight by design:** AI drafts, teachers confirm; override logging; calibration tools; FRIA template for EU deployers (EU AI Act Annex III obligations apply from 2 Dec 2027 after the Digital Omnibus [V2]).
- Licence: $5–15 per student per year, teacher freemium to seed adoption.

### 3. Teen-controlled sharing
- Parents: optional one-screen weekly summary **only with the teen's consent**; parental controls always come **with teen notice** (vision §7). Parents never read chats — consistent with the market direction set by ChatGPT for Teens, whose parental controls don't expose conversations [V2].
- Teachers see only what is submitted or shared for their class.
- Safety exceptions (imminent risk) follow a protocol disclosed to teens at onboarding; no hidden monitoring.

### 4. My Needs profile (Lumen)
- Set once, used in all seven apps and portable across studio ventures: Sensory Dial, reading level, TTS, dyslexia typography, input modes (voice, keyboard, AAC, switch, drawing), **accommodations (extended time multipliers, read-aloud, breaks)**, session length and break reminders, themes.
- Accommodations are free forever and need no proof of diagnosis.
- Target: every Ascendly prototype scores **≥22/24** on the Lumen audit rubric before leaving validation.

### 5. Shared AI and safety policy
- **Learning mode is the default, not an opt-in.** No app generates homework answers or essay prose by default.
- **Verified solvers and citations** for quantitative and factual content; unverifiable content is labelled.
- **No companion persona** in any app (FTC 6(b) inquiry; CA SB 243 in force since 1 Jan 2026 with AI-disclosure and ≥3-hourly break reminders for known minors [V2]). Pathfinder's scenario roles are session-bound simulations, not characters.
- **No emotion recognition** (EU AI Act Art. 5); distress escalation only from what the teen says.
- **Teen privacy:** AADC-style high-privacy defaults, KOSA-ready (no compulsive-use features — KOSA advanced from Senate Commerce 5 Aug 2026, not law [V2]), FERPA/SOPIPA DPAs for schools, no ads, no training on teen data without separate opt-in.

### 6. Fair billing
- One Ascendly Plus subscription (≈$12/mo or $79/yr; family plan) across apps; seasonal exam passes that **do not auto-renew**; price before trial, reminders, one-tap cancel, summer pause; free core with export always (the Knowt lesson).

## Features we reject (combined) and why

| Rejected feature | Seen in | Why we reject it | Apps affected |
|---|---|---|---|
| Instant final answers by default | Gauth, Photomath, Question.AI, Brainly | Unguarded answer-getting lowers unassisted exam performance (Bastani *PNAS* 2025: −17%) [V2] | Study Coach, Exam Ready |
| AI-generated paragraphs/essays, paraphrasers, "humanizers" | QuillBot, Grammarly, Gemini (18+) | Ghostwriting undermines skill and trust | Draft Mentor |
| AI cheating detectors | Turnitin/Grammarly/QuillBot detectors | Unreliable and biased (61% false positives on non-native writers in one study) [V2]; we use process evidence instead | Explain It Back, Draft Mentor |
| Automated final grades on explanations/writing | Various | EU AI Act human oversight; fairness | Explain It Back, Draft Mentor, Exam Ready (FRQs) |
| Companion personas / named AI "friends" / ongoing role-play relationships | Character-style apps; named tutors | FTC 6(b), CA SB 243, teen safety | All |
| Emotion recognition (face, voice, typing) | Some proctoring/engagement tools | Banned in EU education (Art. 5); unreliable | All |
| Hearts / energy / lives | Duolingo | Punishes learning; Lumen P8; backlash [V2] | Exam Ready, Life Ready |
| Streak loss, leagues, public leaderboards, hours rankings | Duolingo, YPT, Kahoot-style tools | Compulsive-use/KOSA risk; comparison pressure; Lumen P15 | Study Squad, Exam Ready, Life Ready |
| Loss mechanics (the tree dies) | Forest, Flora | Shame-based; Lumen P8 | Study Squad |
| Required timers / speed scoring | Quizlet Match, Kahoot, Wayground legacy | Excludes dyslexic, motor-impaired and screen-reader users; WCAG 2.2.1 | Exam Ready, Explain It Back, Life Ready |
| Camera-only or voice-only input | Gauth, Photomath, Flip | Excludes blind, Deaf, non-speaking teens | All |
| Drag-only interactions | Many learning apps | WCAG 2.5.7; motor/switch users | All |
| Stranger matching / public rooms / DMs with strangers | Focusmate (adult), Discord servers, StudyStream | Minor safety | Study Squad |
| Webcam required | Flip, Focusmate norms | Anxiety, privacy, sensory load | Study Squad, Explain It Back |
| Ads, coin packs, weekly subscriptions, auto-renewing seasonal passes | Brainly, Gauth, Question.AI, Studdy | Billing traps are the #1 unmet need [V2]; no ads to minors | All |
| Paywalled export / accommodations | Quizlet | Trust; equity (Lumen P12) | All |
| Parents/teachers reading chats or keystrokes | Some school AI tools | Surveillance fear [V2]; teen ownership | All |
| Cash/gift-card rewards for quizzes; sponsor-driven steering | Zogo; lead-gen scholarship sites | Extrinsic farming; conflicts of interest | Life Ready, Pathfinder |
| Real financial accounts/cards | Greenlight, Step | Outside our mission; regulatory scope | Life Ready |
| Personality-type labels as career answers | Career quizzes | Weak validity; limits teens | Pathfinder |
| Recruiter contact with under-18s; sale of student data to sponsors | Some career/scholarship platforms | FERPA/state laws; trust | Pathfinder |

## Riskiest assumptions and first experiments (venture view)

| # | Assumption | App | First experiment | Threshold |
|---|---|---|---|---|
| A1 | Teens choose learning mode under deadline pressure | Study Coach | Diary + Wizard-of-Oz coach (40 teens) | ≥50% return weekly; measurable quiz gains |
| A2 | Teachers adopt proof-of-learning; teens don't feel surveilled | Explain It Back, Draft Mentor | Paper pilot in 4 classes; timeline comfort test | Teacher value ≥4/5; teen comfort ≥3.5/5 |
| A3 | Study Squad beats Discord for focus | Study Squad | 2-week Discord bot pilot | ≥2 sessions/week per active teen |
| A4 | Sponsors will pay for pathways | Pathfinder | Employer/college LOIs | ≥2 LOIs |
| A5 | Affordable, high-quality aligned item bank | Exam Ready | 100-item AP pilot bank | ≥95% reviewer agreement; ≤$40/item |
| A6 | Organic pull without a school requirement | Life Ready | Short-form content test | ≥2% visit → waitlist |

## Research caveats
- **WebFetch was blocked** by the egress proxy for this session; facts were confirmed through search-result text. [V] marks facts from primary-source domains; pages were not opened in full.
- **The shared web-search budget ran out after research for apps 1–4.** Competitor facts for **Study Squad, Pathfinder and Life Ready** rely on the studio's raw research files ([V2]) and memory ([M]). No numbers were invented; unknown figures say "verify". **WP1 must verify all [M] items** (Sensor Tower/Appfigures export, store pages, vendor sites, age-limit terms, state personal-finance requirement counts) before external use.
- Download and revenue figures for private companies (Brainly revenue, QuillBot revenue, Grammarly ARR) are third-party estimates.
- Cost, pricing and threshold numbers marked [E] are planning estimates to be validated in WP4–WP5.

# AI Fluency Lab: App Strategy & Product Specification

> **Venture:** Evergrow · **App #:** 1/7 · **Ages:** 20–59 (workers; open to 60+ still in work) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/04-evergrow-adults.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Evergrow index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research note:** Web search ran on 29 Sep 2026. Direct page fetches were blocked by the network egress proxy, so a [V] fact means it appeared in search results attributed to the named primary source. A [V2] fact comes from a review site, aggregator or press write-up. Store download counts come from the studio's earlier research files, which are cited where used.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Practise AI on *your* real work in safe sandboxes, get graded by a rubric and checked by a human, and leave with a verified skill your employer can trust. |
| **Primary user / buyer** | User: non-technical knowledge workers (ops, sales, HR, customer service, healthcare admin, finance, teaching staff). Buyer: L&D or HR leader at a mid-market employer (500–5,000 staff); workforce boards; EU deployers acting on AI Act Art. 4. |
| **Core job-to-be-done** | "When my company rolls out AI tools, I want to practise them on tasks from my own job without risking real data or looking foolish, so I can do my work faster and prove I can do it safely." |
| **Category on the stores** | Education › Business / Productivity (web-first, with iOS/Android companion apps) |
| **Top competitors (by downloads / revenue)** | Coursera (+Udemy), LinkedIn Learning, Google AI Essentials, Microsoft Elevate / Applied Skills, DataCamp, Section, Multiverse, Pluralsight; Mimo and Brilliant as consumer mobile benchmarks |
| **Our wedge** | 1) **Role-specific workflow sandboxes** (do, don't watch) instead of generic "AI 101" video, which is free from Google, Microsoft and Anthropic. 2) **Verified, not vanity:** rubric grading plus human review, and skills mapped to roles. 3) **Mid-market fit:** priced, packaged and supported for companies too small for Multiverse or custom Section deals, with accessibility the incumbents lack. |
| **Business model** | B2B SaaS at $150–400 per seat per year (tiered by track count and verification). Cohort add-on. Public-sector pricing for WIOA boards and community colleges. |
| **North-star metric** | Verified skills applied per active learner per month (a sandbox skill verified, then self-reported and manager-optional-confirmed as used on real work within 30 days) |
| **MVP candidate?** | **Yes. Lead app for Evergrow (Year 1).** |

## 2. Problem & users

**Problem statement.** Employers are spending on AI, but most workers still have not been trained to use it, and "AI 101" certificates are not changing how work gets done.
- Only 15.9% of workers told a New York Fed survey that their employer offers any AI training [V2] (Liberty Street Economics, Apr 2026). Other 2026 surveys put formal employer training at roughly a third of employees, depending on definition [V2].
- Workera research reports that AI training "more than doubled" in 2026 but 56% of employees say they have no time at work to build the skills [V].
- Gallup's 2026 work shows **manager-led adoption** and **integration with existing systems** are the top two drivers of frequent AI use [V]. Training that is not tied to the tools and tasks people already use does not stick [I].
- Free "AI 101" is everywhere. Google AI Essentials costs $49/month on Coursera, with 7 courses and 20+ work scenarios, and it can be audited for free [V2]. Microsoft offers free AI-focused Applied Skills credentials such as "Streamline business workflows with AI chat" [V]. Anthropic released five free AI Fluency courses on Coursera built on the 4D framework (Delegation, Description, Discernment, Diligence) [V]. **Knowledge is commoditised. Verified, role-specific practice is not** [I].
- WEF's Future of Jobs 2025 expects 39% of core skills to change by 2030 and 59 of every 100 workers to need training [V] (repo: raw/05).

**Personas.**
1. **Tanya, 27, operations coordinator** (from the vision doc). She fears AI will take her job and has watched AI videos but doesn't use AI at work. She wants practice on her real spreadsheets and emails and a credential her manager respects.
2. **Marcus, 41, claims processor, dyslexic and a screen-reader user (low vision).** Most sandbox-style tools are mouse-heavy and visually dense, and timed quizzes penalise him. He needs keyboard-first sandboxes that work with a screen reader, read-aloud of prompts and outputs, and no timers.
3. **Priya, 38, L&D manager at a 1,800-person regional health system (buyer).** She must show AI-readiness to her board and, for EU sites, document AI literacy. She has no budget for $3,000-per-seat programmes and no time to build content. She needs role tracks ready in a week, SSO, LMS integration and outcome data that does not turn into employee surveillance.

**Needs & wants**
| Need | Evidence | How AI Fluency Lab addresses it |
|---|---|---|
| Practice on realistic tasks, not videos | Vision principle "Do, don't watch"; Gallup: integration drives use [V] | Workflow sandboxes per role, seeded with synthetic versions of real documents |
| Time-efficient learning in the flow of work | Workera: 56% say no time at work [V] | 10–20 minute "reps"; Teams/Slack deep links; no timers |
| Proof employers trust | Certificate value doubts (repo: app-catalog, LinkedIn Learning) [V2] | Rubric-graded projects plus human review for credentials; skills mapped to roles |
| Safe AI use (privacy, bias, verification) | EU AI Act Art. 4 (now "support the development of" AI literacy after the Digital Omnibus) [V2] | Responsible-AI checkpoints inside every track; audit-ready literacy records |
| Manager enablement | Only 36% of employees in AI-integrating organisations strongly agree their manager supports AI use [V] | Team view with aggregate skills only; bridge to Lead with AI (App 4) |
| Accessibility for disabled workers | Lumen audit: incumbents weak on screen-reader sandboxes and timers (repo: raw/04) [V2] | WCAG 2.2 AA sandboxes, keyboard-first, plain-language mode, no timed tests |

## 3. Competitive feature benchmark (top-selling / top-downloaded apps in this category)

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Coursera (+Udemy)** | Coursera Inc. | Q2 2026 revenue $298.6M after the Udemy merger closed 11 May 2026; ~10,000 GenAI courses; GenAI enrolments at 45/min; 12,107 enterprise customers; **enterprise NRR 91%** (down from 95%) [V] | Plus $59/mo or $399/yr [V] (repo); enterprise custom | Play 4.3–4.5 [V] (repo) | University and Big Tech brands; huge catalogue; Anthropic/Google AI courses | Cost; passive video; certificate value doubts; web-first assessments | Captions and transcripts; mobile secondary to desktop [E] (repo) | [Coursera IR](https://investor.coursera.com/news/news-details/2026/Coursera-Reports-Second-Quarter-2026-Financial-Results/default.aspx) |
| **LinkedIn Learning** | Microsoft | 20,000+ courses [V2] | $39.99/mo or $239.88/yr individual; Teams $379.88/seat/yr (≤20 seats) [V2] | n/a | Bundled with LinkedIn profile; short videos | Certificates carry little weight; passive [V2] (repo) | Captions; standard | [trainingcost.com](https://trainingcost.com/linkedin-learning-pricing) |
| **Google AI Essentials** | Google (on Coursera) | Flagship free-to-audit AI course [V2] | $49/mo (US) after 7-day trial; typical completion $100–150 [V2] | n/a | Short; 20+ work scenarios; Google brand | Generic, not role-specific; little hands-on in real tools [V2] | Coursera player | [grow.google](https://grow.google/ai-essentials/), [hakia review](https://hakia.com/news/google-ai-essentials-review/) |
| **Microsoft Elevate / Applied Skills** | Microsoft | Goal of 20M AI credentials [V] (repo); free Applied Skills for AI chat, research agents and Copilot Studio [V] | Free | n/a | Free, lab-based credentials in Microsoft tools | Microsoft-only; assumes M365 Copilot licence [I] | Microsoft Learn accessibility is generally good [M] | [MS Learn](https://learn.microsoft.com/en-us/credentials/microsoft-credentials-ai-challenge) |
| **DataCamp** | DataCamp | Leading data/AI skills platform [V2] | Premium ~$14–28/mo; Teams/Enterprise custom [V2] | Trustpilot high [M] | In-browser coding exercises; skill matrix; SSO; LMS integrations [V2] | Technical bias; less relevant for non-technical roles [I] | Code editor accessibility varies [M] | [DataCamp pricing summary](https://thepivotwave.com/blog/datacamp-pricing/) |
| **Section** | Section (Section AI) | Mid-market/enterprise AI proficiency [V] | "AI Academy for Small Teams" $750 per seat (<100 people) [V] | n/a | Exec-friendly, practical, live cohorts | Pricey per seat; cohort timing | Live sessions; captions vary [M] | [sectionai.com/pricing](https://www.sectionai.com/pricing) |
| **Multiverse** | Multiverse | £79.6M revenue (FY to Mar 2025) with £63.3M loss; $2.1B valuation after early-2026 round; 15,000 AI apprenticeships pledged [V2] | Funded via UK apprenticeship levy / employer | n/a | Coached, work-integrated, accredited | Long programmes (months); UK-centric | Human coaches help accommodations [I] | [Wikipedia](https://en.wikipedia.org/wiki/Multiverse_(company)), [tech.eu](https://tech.eu/2025/06/09/multiverse-powers-national-ai-drive-with-15-000-new-apprenticeships/) |
| **Mimo** (consumer mobile benchmark) | Mimo | 10M+ downloads; Play 4.7 (~733K reviews), App Store 4.8 [V2] | Freemium subscription [M] | 4.7–4.8 | Bite-size, mobile, hands-on "AI coding" path | Streak/habit pressure; beginner-only [M] | Code on a phone is hard for motor and low-vision users [I] | [Google Play](https://play.google.com/store/apps/details?id=com.getmimo) |

Also considered: **Pluralsight** (Business "AI + Data" plan $399 per user per year [V]); **Udacity**, now inside Accenture LearnVantage, which launched an AI-product MBA under $5,000 in Mar 2026 [V]; **Maven** (practitioner cohorts, typically $800–2,500 and up to $5,000 for AI PM certificates [V2]); **Brilliant** (interactive STEM; "no heads-up before the charge" billing complaints [V2] (repo)).

**Market read [I].** Coursera's enterprise NRR fell to 91% because of "pressure on L&D budgets" [V]. Buyers are cutting broad catalogue licences and funding targeted programmes that show results. That favours a narrow, outcome-reporting product, but it also means we must prove ROI inside one budget cycle.

### Feature matrix
| Feature | Coursera | LinkedIn L. | Google AI Ess. | MS Applied Skills | DataCamp | Section | Multiverse | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Role-specific AI tracks (non-technical) | partial | partial | ✗ | partial | ✗ | ✓ | ✓ | **Differentiate:** 8 role tracks at launch |
| Hands-on sandbox in realistic workflows | partial | ✗ | partial | ✓ (MS tools) | ✓ (code) | partial | ✓ (real job) | **Differentiate:** multi-model, tool-agnostic sandboxes |
| Rubric-graded projects | partial | ✗ | ✗ | ✓ | ✓ | partial | ✓ | **Parity+** |
| Human review of credentials | partial (peer) | ✗ | ✗ | ✗ | ✗ | partial | ✓ (coach) | **Differentiate** |
| Skills mapped to roles / skill matrix | ✓ | ✓ | ✗ | partial | ✓ | partial | ✓ | **Parity** |
| Responsible-AI checkpoints (privacy, bias, verification) | partial | partial | ✓ | partial | partial | ✓ | ✓ | **Improve:** embedded in every task |
| SSO / LMS / HRIS integration | ✓ | ✓ | ✗ | ✓ | ✓ | partial | ✓ | **Parity** (SCORM/xAPI, SAML, Workday/Cornerstone/Degreed) |
| Live cohorts | partial | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | **Parity** as add-on |
| Timed exams | ✓ | ✓ | ✓ | ✓ (lab time) | ✓ | ✗ | ✗ | **Reject:** timing is the user's (P11); integrity comes from process logs |
| Individual employee monitoring dashboards (time-on-app rankings) | partial | partial | ✗ | partial | ✓ | ✗ | partial | **Reject:** no surveillance analytics for managers |
| Leaderboards / streaks | partial | ✗ | ✗ | ✗ | ✓ (XP) | ✗ | ✗ | **Reject:** social comparison and streak guilt; use gentle weekly goals |
| Accessible, keyboard-first sandbox | partial | partial | partial | partial | partial | ✗ | n/a | **Differentiate (Lumen)** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| F1 | **Workflow Sandboxes** ★ signature | Browser sandboxes that mimic real tools (inbox, spreadsheet, doc editor, CRM, ticket queue) filled with synthetic, role-relevant data. The learner uses one or more frontier models inside them. | Microsoft proves labs work but ties them to M365 [V]; Gallup says integration drives use [V] | Differentiate | MVP | Must |
| F2 | **Role tracks** | 8 tracks at launch: Ops/Admin, Sales, Customer Service, HR/People, Finance, Healthcare Admin, Teaching/School Staff, Managers-lite (hand-off to App 4). Each has 6–10 "reps" and 1 capstone. | Section and Multiverse succeed with role focus [V] | Differentiate | MVP | Must |
| F3 | **Rubric grader + human review** ★ signature | An AI grader scores against a published rubric; every credential-bearing capstone is sampled or fully reviewed by a trained human reviewer. Learners can appeal. | "Verified, not vanity"; certificate doubts [V2] | Differentiate | MVP | Must |
| F4 | **Skills Passport** (Evergrow shared) | Portable, learner-owned record of verified skills with evidence (the artefact plus rubric), exportable as Open Badges 3.0 / a verifiable credential | Vision shared layer | Differentiate | MVP | Must |
| F5 | **Responsible-AI checkpoints** | In-task prompts on data privacy (redact before pasting), bias checks and fact verification; "Discernment" scoring in every rubric | EU AI Act Art. 4; Anthropic 4D framework [V] | Improve | MVP | Must |
| F6 | **Placement "show me" task** | A 10-minute untimed diagnostic in the sandbox sets the starting rep; there are no quizzes about AI trivia | Adults skip what they know [I] | Improve | MVP | Must |
| F7 | **Employer console** (Evergrow shared) | Seat management, SSO (SAML/OIDC), track assignment, **aggregate** skills heat-map (minimum cohort size 5), literacy-record export for Art. 4 files | Priya persona; DataCamp/Coursera parity [V2] | Parity | MVP | Must |
| F8 | **"Bring your own task" (redacted)** | Learners paste a *de-identified* real task. A local PII scrubber runs first and the learner confirms before anything is sent. | "Do, don't watch"; privacy | Differentiate | MVP | Should |
| F9 | **My Needs profile + accessibility pack** | Keyboard-first sandbox, screen-reader announcements for AI output, read-aloud, plain-language mode, dyslexia typography, 60+ large-type preset | Lumen P1–P18 | Lumen | MVP | Must |
| F10 | **Gentle weekly goals** | Learner sets 1–3 reps per week; pause weeks; no streak loss framing | Duolingo streak backlash [V] (repo) | Lumen | MVP | Must |
| F11 | **Work-transfer check-in** | 14 and 30 days after a verified skill, a 1-question prompt: "Did you use this at work? What changed?" Optional manager confirmation, with learner consent. | North-star measurement | Differentiate | MVP | Must |
| F12 | **In-flow nudges** | Teams/Slack app with weekly (not daily) opt-in nudges and deep links into a rep | Workera "no time" [V] | Improve | MVP | Should |
| F13 | Live cohort add-on | 4-week cohorts with a human facilitator (captioned), for teams | Section/Maven model [V] | Parity | V1 | Should |
| F14 | Custom track builder | L&D uploads SOPs; we generate draft reps; an SME and our editors review before publishing | Content staleness risk | Improve | V1 | Should |
| F15 | LMS/LXP connectors | SCORM/xAPI/LTI; Workday Learning, Cornerstone, Degreed | Vision GTM | Parity | V1 | Must |
| F16 | Tool-specific overlays | Optional modules for Microsoft Copilot, Google Gemini, ChatGPT Enterprise and Claude interfaces | Buyers standardise on one tool [I] | Parity | V1 | Could |
| F17 | Workforce-board edition | WIOA-eligible pathways, case-manager view, Spanish UI | Vision GTM | Differentiate | V1 | Should |
| F18 | Agent-building track | Low-code "build a safe agent" reps with guardrail design | MS Copilot Studio credential [V] | Parity | V2 | Could |
| F19 | Skills-outcome study | Published pre/post task-performance study with a partner employer | P17 honest claims | Differentiate | V2 | Should |

MVP = F1–F12 (12 features). **Core loop covered end to end:** placement → rep in a sandbox → rubric feedback → capstone → human review → Skills Passport → work-transfer check-in.

## 5. Core experience & key user flows

**Core loop.** Open (from a weekly Teams nudge or the web) → pick the suggested rep ("Summarise 40 customer emails into a triage table") → do it in the sandbox with AI → submit → rubric feedback with 1 "try this" hint → optional retry → rep done, session summary → natural end ("That's your rep for today. Next suggested: Tuesday").

**Flow 1: Onboarding (≤5 minutes to first value)**
1. Sign in with SSO (employer) or a passkey or email magic link (individual). No passwords to remember (WCAG 3.3.8).
2. The My Needs quick card asks about text size, read-aloud, reduced motion, keyboard-only and plain language. Each is one tap and can be changed at any time.
3. Choose a role track (it may be preassigned by the employer).
4. Placement task: one short sandbox task with no timer.
5. First feedback screen shows 2 strengths and 1 next step. Value arrives at about 4 minutes.

**Flow 2: Core rep**
1. The Now / Next / Done strip shows "Brief → Do → Check → Done".
2. The brief is written in plain language and read aloud on request. The sample data is synthetic and labelled "practice data".
3. In the sandbox, the learner prompts one or more models, edits outputs and uses the verification tools (source check, "ask the model for its uncertainty").
4. The learner submits. The rubric covers task quality, Description, Discernment (did you check it?) and Diligence (did you protect data?).
5. Feedback arrives with one hint. The learner can retry or finish.
6. Designed end: summary, and "Where could you use this at work this week?" (optional, one line).

**Flow 3: Capstone and credential**
1. The capstone brief is released after the reps are mastered.
2. The learner completes it with no time limit. A process log (prompts, edits, checks) is kept for integrity.
3. The AI grader pre-scores it, and a human reviewer confirms or adjusts within an SLA of 3 business days.
4. The credential is issued to the Skills Passport. The learner decides whether to share it with the employer or on LinkedIn.
5. Appeal: one tap sends it to a second reviewer.

**Flow 4: Employer console (buyer/admin)**
1. Priya uploads a roster or connects SCIM, then assigns tracks by department.
2. The dashboard shows aggregate completion and verified skills per team (hidden below 5 people), trends and the work-transfer rate.
3. She exports an AI-literacy record (tracks, topics, dates, per person only where the employee has consented or the employer's HR policy requires it and the employee was told).
4. **Not available:** time-on-app per person, keystroke data, rankings, prompt contents.

**Flow 5: My Needs / settings.** Reached in 1 tap from the header. Covers the Sensory Dial, text size (up to 200%), font, spacing, read-aloud voice and speed, keyboard shortcuts and plain-language mode. Changes sync across Evergrow apps.

**Flow 6: Billing / cancellation.** B2B: annual invoice; seat changes self-serve with pro-rating. Individual plan (V1): price shown before any trial, a reminder 3 days before conversion, one-tap cancellation, a pause option.

**Information architecture.** Home (Next rep, Weekly goal) · Tracks · Sandbox (full screen) · Passport · Help (fixed position) · My Needs. Admin: People · Tracks · Insights (aggregate) · Records · Settings. Navigation is a top bar with 5 fixed items. Mobile uses a bottom bar with the same 5.

**Session design.** A rep defaults to 10–20 minutes and a capstone to 60–120 minutes. Both are autosaved and resumable. A gentle "about 5 minutes of work left in this rep" hint appears, with no countdown. Every session ends on a summary screen.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial defaults.** The default is **Calm/Balanced**, following system settings. Calm: no motion, no sounds, and completions shown as a plain check. Balanced: gentle transitions and an optional soft completion tone. Lively: opt-in, with a short celebration after capstones only. No confetti by default.

**Input modes per task**
| Task | Tap | Keyboard | Voice (dictation) | Switch | Screen reader | Notes |
|---|---|---|---|---|---|---|
| Prompting in sandbox | ✓ | ✓ (primary) | ✓ OS dictation | ✓ | ✓ | Prompt templates insertable by button |
| Editing AI output | ✓ | ✓ | ✓ | ✓ | ✓ | Diff view has a text alternative ("3 changes: …") |
| Spreadsheet tasks | ✓ | ✓ | partial | ✓ | ✓ | Grid follows ARIA grid pattern; cell-by-cell announcements |
| Drag-to-sort tasks | ✓ tap-then-tap | ✓ arrow keys | ✓ | ✓ | ✓ | Every drag has a non-drag alternative (WCAG 2.5.7) |

**Targets and gestures.** Minimum 48 dp / 44 pt, and **≥56 dp with the 60+ large-type preset**. No gesture-only actions. All shortcuts can be remapped, and single-key shortcuts can be switched off (WCAG 2.1.4).

**Reading and typography.** Body text is 18 px by default (range 16–32 px). Line height 1.5, 60–75 characters per line, left-aligned, off-white option. Plain-language mode rewrites briefs to about grade 8 with a human-edited glossary. Read-aloud highlights words as they are spoken. AI output can be read aloud.

**Audio.** There is little audio in this app. All video explainers (≤3 min, optional) have human-checked captions and transcripts. There are no sound-only cues.

**Age-respectful themes.** Two themes, "Workspace" (neutral) and "High contrast". No mascots.

**60+ large-type preset** (Evergrow shared). 20 px body text, 56 dp targets, extra spacing, one primary action per screen, and linear steps in the sandbox, for older workers.

**Lumen principles (app-specific acceptance criteria)**
| # | Principle | Acceptance criterion in AI Fluency Lab |
|---|---|---|
| P1 | Calm; respect system settings | With OS Reduce Motion on, 0 animations; Dynamic Type to 200% with no truncation in the sandbox |
| P2 | Granular sound | No sound by default; every tone has a visual twin |
| P3 | Predictable structure | Brief/Do/Check/Done strip on every rep; no layout shift within a sandbox |
| P4 | Big, forgiving targets | 48 dp minimum, 56 dp in the 60+ preset; all drags have alternatives |
| P5 | Plain language | Plain-language mode briefs at ≤ grade 8 (readability check plus editor) |
| P6 | Dyslexia-friendly typography | Font, size, spacing and tint adjustable; WCAG 1.4.12 passes in the sandbox |
| P7 | Multimodal | Every rep can be completed by keyboard only and by screen reader |
| P8 | Low-penalty learning | Unlimited retries on reps; autosave; undo in every sandbox tool |
| P9 | Help focus | One primary action per screen; no infinite feeds; designed end screen |
| P10 | Don't rely on memory | Passkey/SSO sign-in; the brief stays visible beside the sandbox |
| P11 | Timing belongs to the user | No timed assessments; SSO session timeouts warn and preserve work |
| P12 | My Needs profile | All accommodations free for every seat; profile portable across Evergrow |
| P13 | Age-respectful | No cartoon mascots; 2 themes |
| P14 | Caregiver/admin low burden | Admin setup of a 50-seat pilot in ≤30 minutes |
| P15 | Motivation without manipulation | Weekly goals, pause weeks, no leaderboards |
| P16 | Affirming language | Accommodation copy reviewed by the ND/disability panel |
| P17 | Honest claims | Every marketing claim in the claims register with an evidence tier |
| P18 | Privacy by default | No prompt content visible to employers; PII scrubber before any "bring your own task" |

**Target Lumen audit score:** ≥22/24 (goal 24/24; the sandbox is the risk area).

## 7. AI specification & guardrails

**What AI does.** (1) It acts as the working model inside sandboxes: multiple frontier LLMs through a routing layer, so learners see differences between models. (2) The rubric grader. (3) Synthetic data generation for sandboxes, reviewed by humans. (4) Adaptive rep selection. (5) Draft reps for custom tracks, published only after SME review.

**What AI does not do.** It does not issue credentials alone, rank employees, infer emotion or engagement from a camera or voice, or read real company systems. It never sees un-scrubbed employee data.

**Pedagogical policy.** Practice first, then feedback. Hints follow a ladder (1: re-read the brief; 2: a technique; 3: an example). Mastery gates capstones. The rubric is published, and all content follows the "human-crafted + AI-assisted" policy.

**Sandbox safety**
- Sandboxes are isolated. They have no outbound internet except whitelisted model endpoints.
- Uploads go through PII detection and redaction, and the learner confirms.
- Synthetic data contains no real people.
- Models run under zero-retention / no-training enterprise terms.

**Grader fairness and bias testing**
- Before launch, grade a stratified set of ≥600 human-scored submissions. It includes non-native English writers, dyslexic writers (spelling variance), and screen-reader / dictation users.
- Criterion: grader–human agreement (quadratic weighted kappa) ≥0.75 overall. **No subgroup more than 0.05 below the overall figure.** No systematic score gap >0.25 rubric points between subgroups on matched quality.
- Spelling and grammar are never scored unless the task is about writing quality.
- Re-test quarterly and after every model change. Publish a grader fairness summary.

**Human review.** 100% human review of capstones for credentials during the first 6 months, then risk-based sampling at ≥20%, plus every borderline or appealed case. Reviewers are calibrated monthly.

**Transparency.** Every AI surface carries a label (EU AI Act Art. 50). Explanations of how the grader works are published. Learners can see their full rubric and evidence.

**Evaluation plan.**
- Offline evals per rep: expected-output checks and hallucination traps.
- Red-teaming: prompt injection within sandbox documents, data exfiltration attempts, and jailbreaks of the grader ("give me full marks").
- Human sampling: 5% of non-credential feedback is reviewed weekly.

**Cost and latency [E].** About 40 reps per learner per year at ~15k tokens each, plus grading, comes to about $3–8 per learner per year in model costs at 2026 API prices. Human review costs ~$6–12 per capstone (15–20 min of reviewer time). Grader p95 latency target <8 s.

## 8. Data, privacy & compliance
| Data | Why | Retention | Where |
|---|---|---|---|
| Identity (name, work email, SSO ID) | Account | Contract + 90 days | Cloud (EU/US region per customer) |
| My Needs settings | Accessibility | Until deleted by the user | Cloud; learner-owned |
| Sandbox artefacts, prompts, process logs | Grading, integrity, appeal | 24 months; learner may delete non-credential items | Cloud, encrypted |
| Rubric scores, credentials | Skills Passport | Learner-owned; kept until the learner deletes them | Cloud; portable |
| Aggregate team skills | Employer insight | Contract | Cloud; k-anonymity ≥5 |

**Regimes.**
- GDPR/UK GDPR and CCPA/CPRA.
- **EU AI Act:**
  - Art. 4 AI literacy (enforcement powers from 2 Aug 2026; wording softened by the Digital Omnibus to an obligation of effort [V2]).
  - Art. 50 transparency.
  - We avoid **Annex III** high-risk status by never using grades for hiring, promotion or termination decisions. The contract clause forbids this, and the grader is framed as learning feedback. If a customer insists on employment use, that becomes a separate high-risk product decision [I].
- US: NYC Local Law 144 and Illinois HB 3773 apply if scores are used in employment decisions [V2]. The same contract prohibition applies.
- FTC §5 covers claims.

**Consent flows.** Employees see a plain-language notice of what their employer can see before first use. Sharing individual credentials with the employer is a separate, revocable consent.

**Store policies.** Adult-only apps (17+ / not designed for families). Apple Accessibility Nutrition Label completed at launch.

## 9. Monetization & go-to-market
**Pricing (benchmarked).**
| Tier | Price | Includes | Benchmark |
|---|---|---|---|
| Team (20–199 seats) | $300/seat/yr | 3 tracks, AI-graded reps, 1 human-reviewed credential per learner | LinkedIn Teams $379.88 [V2]; Pluralsight AI+Data $399 [V] |
| Business (200–5,000) | $180–250/seat/yr | All tracks, SSO/SCIM, LMS, literacy records | DataCamp/Coursera custom [V2] |
| Public sector / WIOA | $150/seat/yr or per-completer pricing | Workforce-board edition | Vision band |
| Cohort add-on | $450/learner | 4-week facilitated cohort | Section $750/seat [V] |
| Individual (V1) | $19/mo or $149/yr | 1 track + credential | Google AI Essentials $49/mo [V2] |

The fair-billing charter applies to all tiers. Accessibility features are never a paid add-on.

**Channels**
1. Direct sales to mid-market (health systems, credit unions, regional insurers, logistics).
2. LMS/LXP marketplaces (Workday, Cornerstone, Degreed).
3. Workforce boards and community colleges (WIOA ITA lists).
4. EU compliance buyers via partners.
5. A bridge to Lead with AI (App 4) for manager tiers.

**ASO.** Web-first. Companion app keywords: "AI skills at work", "AI training for employees", "Copilot practice", "prompt practice". Category: Business. The Accessibility Nutrition Label will declare VoiceOver, Voice Control, Larger Text, Sufficient Contrast, Reduced Motion and Captions.

**Launch markets.** US first (English, then Spanish UI in V1); UK/IE and DACH in V1 via partners (German localisation).

## 10. Success metrics
- **North star:** verified skills applied per active learner per month. Target ≥0.8 by month 6 of a pilot [E].
- **Inputs:**
  - weekly active learners / seats (≥35%)
  - reps completed per active learner per week (≥1.5)
  - capstone pass rate on the first human review (60–80%, which shows the rubric is neither trivial nor impossible)
  - work-transfer "yes" rate at 30 days (≥50%)
- **Guardrails:**
  - Sensory Comfort ≥4/5
  - grader subgroup gap within thresholds
  - appeal overturn rate <10%
  - zero incidents of individual prompt content shown to employers
  - zero billing complaints
- **Outcomes / evidence plan:**
  - Tier 1: pre/post task-performance on matched untrained sandbox tasks.
  - Tier 2: a design-partner quasi-experiment (trained team vs. waitlist team) on time-to-complete and quality of a real workflow.
  - Tier 3 (V2): pre-registered study with a university partner.
- **Retention:** B2B seat activation ≥70% in 30 days; logo retention ≥90%; **NRR ≥115%** (vs. Coursera enterprise 91% [V]); learner D30 ≥40% of activated seats.

## 11. Validation plan (no-code, discovery phase)
**Riskiest assumptions (ranked)**
1. Mid-market employers will pay $150–400 per seat for role-specific fluency over free Big Tech programmes (vision E1).
2. Sandbox practice produces measurable task-performance gains within 4 weeks.
3. Rubric grading plus sampled human review is trusted by learners and buyers.
4. Workers find time (the Workera "no time" risk).
5. Sandboxes can be made fully accessible without destroying realism.

**Experiments**
| # | Method | Sample | Success threshold | Kill threshold |
|---|---|---|---|---|
| X1 | **Concierge cohort** with 2 design-partner employers. Figma-prototyped sandboxes; real models used through a facilitator-controlled workspace (Wizard-of-Oz grading by humans) | 2 × 20 staff, 4 weeks | Pre/post task quality gain ≥20% on matched tasks; ≥60% complete 6+ reps | <10% gain or <30% completing |
| X2 | Paid letters of intent | 12 L&D buyers pitched | ≥3 LOIs at ≥$150/seat/yr | 0–1 LOIs |
| X3 | Van Westendorp + bundle test (Fluency Lab alone vs. + Lead with AI) | 100 L&D buyers (survey) | Acceptable price range covers $180–300 | Range below $100 |
| X4 | Grader agreement pilot | 200 human-scored submissions, including dyslexic, non-native and dictation writers | κ ≥0.7 and subgroup gap ≤0.05 | κ <0.6 |
| X5 | Accessibility usability of the sandbox prototype | 8 participants (2 screen-reader users, 2 dyslexic, 2 keyboard-only, 2 aged 55+) | Task success ≥80%; SUS ≥75 | <60% |
| X6 | Time-in-flow test: weekly Teams nudge vs. none | Within X1 | ≥1.5 reps per week with the nudge | No difference |

**Mapping.** WP1 (audit Coursera, LinkedIn, Google, MS, DataCamp and Section against the Lumen rubric) · WP2 (15 workers, 12 L&D buyers, 10-worker diary study) · WP4 (X1, X4, X5) · WP5 (X2, X3; the ≥2 design partners / ≥3 LOIs gate from the Discovery Plan).

## 12. Build handoff (for the agent team, post-Gate 2)
**Epic A: Sandboxes**
- *Story A1.* As a learner, I want to use AI on practice data in a realistic inbox.
  - Given a rep with synthetic data, when I send a prompt, then the model response appears within 8 s (p95) and is announced by screen readers via a live region.
- *Story A2.* Given I paste text into "bring your own task", when the scrubber finds names, emails or IDs, then they are highlighted and redacted, and nothing is sent until I confirm.
- *Story A3.* Given Reduce Motion is on, when any sandbox view opens, then no animations play.

**Epic B: Grading and credentials**
- *B1.* Given a submitted capstone, when the AI grader completes it, then the status is "Awaiting human review" and no credential is issued until a reviewer signs off.
- *B2.* Given a learner appeals, when the appeal is submitted, then a different reviewer is assigned and the original score is hidden from them.
- *B3.* Given a model version change, when the grader is redeployed, then the fairness regression suite must pass before release.

**Epic C: Employer console**
- *C1.* Given a team of fewer than 5 learners, when the admin opens Insights, then team-level metrics are suppressed with an explanation.
- *C2.* Given an admin, when viewing any learner, then prompt contents and time-on-app are not available by any route (UI, API, export).

**Epic D: Skills Passport**
- *D1.* Given a verified credential, when I export it, then I receive an Open Badges 3.0 file with the evidence link. Revoking sharing removes employer access within 1 minute.

**Epic E: My Needs and accessibility**
- *E1.* Given the 60+ preset, when enabled, then body text is ≥20 px and targets are ≥56 dp across all screens.
- *E2.* Given keyboard-only use, then every rep is completable, and a visible focus indicator is present (WCAG 2.4.11).

**Non-functional requirements**
- Performance: p95 page load <2 s; sandbox model latency <8 s.
- Offline: companion app caches briefs; sandboxes need a connection.
- Platforms: web (primary), iOS and Android companion.
- Accessibility: WCAG 2.2 AA plus relevant AAA items (2.2.3 No Timing).
- Localisation: English and Spanish, then German.
- Security: SOC 2 Type II within 12 months, SSO, encryption, tenant isolation, pen test before GA.

**QA focus**
- AT matrix: VoiceOver (macOS/iOS), NVDA and JAWS (Windows), TalkBack, Dragon/Voice Control, Switch Control, 200% zoom.
- Sensory A/B: Calm vs. Balanced completion tone.
- AI safety cases: prompt injection in documents, grader manipulation, PII leakage.
- COPPA: not applicable (18+); age gate attests 18+.
- Billing: seat pro-ration, individual trial reminder, one-tap cancel.

**Shared-platform dependencies.** Lumen design system, My Needs profile, AI orchestration (model router, eval harness), privacy stack (PII scrubber, consent ledger), evidence engine (pre/post task library), Skills Passport service.

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Free Big Tech courses satisfy buyers | High | High | Sell verified, role-specific outcomes; offer overlays for their tools (F16) |
| L&D budget squeeze (Coursera NRR 91%) [V] | High | Med | Land small (20-seat pilot); ROI report in 60 days |
| Content goes stale as tools change | High | Med | Modular reps; quarterly SME refresh; tool-agnostic skills |
| Grader bias or error harms learners | Med | High | Human review, fairness suite, appeals |
| Employer pressure to use scores for HR decisions (Annex III, LL144) | Med | High | Contract prohibition; product framing; legal review |
| Weaker Art. 4 after the Digital Omnibus reduces EU urgency [V2] | Med | Med | Lead on productivity, not compliance |
| Model costs spike | Low | Med | Routing to smaller models for practice; caching |

**Open questions.** Which 3 role tracks convert best in mid-market health and finance? Will buyers pay a premium for human-reviewed credentials, or treat review as table stakes? Should we partner with (rather than compete against) the Coursera marketplace for distribution?

## 14. Sources
- [V] Coursera Q2 2026 results: https://investor.coursera.com/news/news-details/2026/Coursera-Reports-Second-Quarter-2026-Financial-Results/default.aspx
- [V] Anthropic AI Fluency courses on Coursera: https://blog.coursera.org/anthropic-launches-five-free-courses-on-coursera-to-help-build-ai-fluency/
- [V] Microsoft Credentials AI Challenge / Applied Skills: https://learn.microsoft.com/en-us/credentials/microsoft-credentials-ai-challenge
- [V] Microsoft Elevate for Educators: https://news.microsoft.com/source/2026/01/15/microsoft-expands-its-commitment-to-education-with-elevate-for-educators-program-and-new-ai-powered-tools/
- [V2] Google AI Essentials pricing: https://grow.google/ai-essentials/ · https://hakia.com/news/google-ai-essentials-review/
- [V] Section pricing: https://www.sectionai.com/pricing
- [V2] LinkedIn Learning pricing: https://trainingcost.com/linkedin-learning-pricing · https://upskillwise.com/linkedin-learning-cost/
- [V2] DataCamp pricing: https://thepivotwave.com/blog/datacamp-pricing/ · https://www.capterra.com/p/228646/DataCamp/
- [V2] Multiverse: https://en.wikipedia.org/wiki/Multiverse_(company) · https://tech.eu/2025/06/09/multiverse-powers-national-ai-drive-with-15-000-new-apprenticeships/
- [V] Pluralsight pricing: https://www.pluralsight.com/individuals/pricing
- [V] Udacity/Accenture MBA: https://newsroom.accenture.com/news/2026/udacity-part-of-accenture-launches-accredited-mba-to-train-the-next-generation-of-ai-product-leaders
- [V2] Maven pricing: https://www.productcompass.pm/p/best-maven-courses-discount-codes
- [V2] Mimo store listing: https://play.google.com/store/apps/details?id=com.getmimo
- [V] Gallup manager support and AI adoption: https://www.gallup.com/workplace/694682/manager-support-drives-employee-adoption.aspx · https://www.gallup.com/workplace/712736/organizational-adoption-jumps-six-points.aspx
- [V] Workera "no time at work": https://www.prnewswire.com/news-releases/ai-training-more-than-doubled-this-year-but-56-of-employees-report-no-time-at-work-to-build-the-skills-workera-research-finds-302887120.html
- [V2] NY Fed Liberty Street: https://libertystreeteconomics.newyorkfed.org/2026/04/use-of-gen-ai-in-the-workplace-and-the-value-of-access-to-training/
- [V2] EU AI Act Art. 4 enforcement and Digital Omnibus: https://www.muchskills.com/blog/eu-ai-act-article-4-ai-literacy-enforcement · https://www.traverssmith.com/knowledge/knowledge-container/the-eu-ai-acts-ai-literacy-requirement-key-considerations/
- [V2] NYC LL144 / Illinois HB 3773: https://www.dlapiper.com/en-us/insights/publications/2026/01/critical-audit-of-nyc-ai-hiring-law-signals-increased-risk-for-employers · https://www.jonesday.com/en/insights/2024/10/illinois-becomes-second-state-to-pass-broad-legislation-on-the-use-of-ai-in-employment-decisions
- Repo: research/raw/05-market-and-trends.md (WEF 2025, pricing bands, Coursera–Udemy merger), research/raw/01-google-play-top30.md, research/raw/04-neurodivergent-and-inclusive-ux.md

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (studio lead; absorbs Lead with AI as the Manager track) |
| **Ships in** | Evergrow Work (B2B) (S4) |
| **Build wave** | 1a |
| **Pre-discovery priority score** | 84/100 [I] |
| **Consumes engines** | EN-03, EN-06, EN-08, EN-10 |
| **Studio features used** | SX-02, SX-21, SX-30, SX-31 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = F1, F2, F3, F4, F5, F8.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| AFL-E1 | **Productivity proof pack** | Before/after task time and quality measured in sandboxes, rolled up into an aggregate ROI report for the buyer. This answers the softened EU Art. 4 duty and Coursera's ~91% enterprise NRR [V2]. |
| AFL-E2 | **AI as assistive tech at work** | A track for disabled employees and their managers on using AI for accessibility (captioning, summarizing, task breakdown). |
| AFL-E3 | **Manager track** | Lead with AI simulations delivered as a module (see the Lead with AI verdict). |

### 15.3 New validation question
Two design-partner cohorts: measured task-performance gain, plus ≥3 paid LOIs at ≥$150/seat/yr.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 4 | 4 | 4 | 5 | 4 | 4 | 5 |

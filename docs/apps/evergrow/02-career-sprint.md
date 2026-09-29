# Career Sprint: App Strategy & Product Specification

> **Venture:** Evergrow · **App #:** 2/7 · **Ages:** 20–34 (early career, career switchers) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/04-evergrow-adults.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Evergrow index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research note:** Searched 29 Sep 2026. Page fetches were blocked by the egress proxy, so [V] means the fact appeared in search results attributed to the primary source.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Six-to-eight-week sprints where you build real, AI-assisted portfolio projects from employer briefs, practise interviews with a clearly labelled AI interviewer, and show your work to hiring managers. |
| **Primary user / buyer** | Users: graduates 20–27 without a first job, career switchers 25–34, and community-college and WIOA participants. Buyers: the learner (B2C), workforce boards (WIOA ITAs), community colleges and universities (career services), and hiring partners who sponsor briefs. |
| **Core job-to-be-done** | "When entry-level postings dry up and my certificate isn't enough, I want to build proof I can do the job with today's AI tools and practise telling that story, so a hiring manager takes me seriously." |
| **Category on the stores** | Education › Career / Business (web + mobile) |
| **Top competitors (by downloads / revenue)** | Coursera Professional Certificates (Google Career Certificates), Forage, Handshake, Final Round AI, Yoodli, Big Interview, Springboard, General Assembly, Seekho (short-video upskilling) |
| **Our wedge** | 1) **Proof over certificates:** employer-briefed projects with a process log that shows *how* the learner used AI. 2) **Fair interview practice**, never a live "stealth" cheating copilot, with accommodations built in. 3) **Humans in the loop:** mentor reviews and hiring-manager demo days. |
| **Business model** | B2C $29/mo or $149 per sprint. Workforce/college licences $600–1,200 per completer. Hiring-partner sponsorship $5–15k per brief per year. |
| **North-star metric** | Portfolio projects reviewed by a hiring manager per active learner (then interviews earned within 90 days) |
| **MVP candidate?** | **Later (Year 2)**, after the AI Fluency Lab core ships. The concierge sprint runs in discovery. |

## 2. Problem & users
**Problem statement**
- Recent graduates face the weakest entry market in years:
  - The NY Fed puts recent-graduate unemployment at 5.7% (June 2026), against 4.1% for all workers [V2].
  - Underemployment is 42.5% [V2].
  - A Stanford Digital Economy Lab paper found a 16% relative employment decline for workers aged 22–25 in the most AI-exposed occupations [V2].
- Certificates are abundant but weakly trusted. Google Career Certificates cost $49/mo and give access to a consortium of 150+ employers, but reviewers note most graduates never use the consortium, and the people who get hired pair the certificate with portfolio projects [V2].
- Job simulations work when employers design them. Forage reports 10M+ student engagements, 250+ simulations from 90+ employers, and says completers are "more than twice as likely to get an interview and three times more likely to receive an offer" at participating companies [V] (company claim).
- The interview-prep market is splitting:
  - **Cheating copilots:** Final Round AI sells a "Stealth Mode" billed as undetectable, charges ~$149–299/mo, and was named in Amazon's 2025 interview ban [V2].
  - **Practice coaches:** Yoodli raised a $40M Series B in Dec 2025 for AI roleplays [V].
  - Candidates caught using live copilots risk rescinded offers [V2]. Young adults need honest practice, not a liability.

**Personas**
1. **Jordan, 23, marketing graduate** with 140 applications and 3 interviews. Has a Google certificate but no portfolio. Wants projects that look like real work and confidence in interviews.
2. **Aisha, 29, retail supervisor switching to data analytics; autistic with interview anxiety.** Finds eye-contact scoring and timed video interviews distressing. Needs text-mode practice, predictable question previews, extra time and feedback that doesn't penalise flat affect.
3. **Luis, 45, WIOA case manager at an American Job Center (buyer/caregiver role).** Needs short, fundable programmes with completion and placement data for performance reporting and an accessible, Spanish-capable experience.

**Needs & wants**
| Need | Evidence | How Career Sprint addresses it |
|---|---|---|
| Proof beyond certificates | Consortium under-used; portfolio pairing wins [V2] | Employer-briefed projects plus process log |
| Realistic work exposure | Forage outcome claims [V] | Briefs from hiring partners and a synthetic "client" |
| Interview confidence, honestly | Copilot bans and rescinded offers [V2] | AI mock interviews labelled as practice; no live-interview assist |
| Accommodations | Lumen P7/P11; Illinois AI Video Interview Act consent rules [V2] | Text mode, extra time, no affect scoring |
| Affordable, short | Bootcamps $7k–16k [V2] | 6–8 week sprints under $200 |
| Visible to real hiring managers | Vision riskiest assumption | Demo days and a reviewer marketplace |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Coursera Prof. Certificates (Google)** | Coursera / Google | Coursera Q2 2026 revenue $298.6M [V]; Play 10M+ [E] (repo) | $49/mo; Plus $399/yr [V2] | 4.3–4.7 (repo) | Brand; structured; 150+ employer consortium | Certificate glut; consortium invisible; passive video [V2] | Captions; web-first | [grow.google/certificates](https://grow.google/certificates/) |
| **Forage** | Forage (EAB) | 10M+ student engagements (Aug 2025) [V] | Free to students; employer-paid | n/a | Employer-designed tasks, 2–3 hours, self-paced | Shallow (hours, not weeks); no feedback from humans [I] | Web; varies by simulation | [EAB press](https://eab.com/about/newsroom/press/forage-job-simulations-surpass-10-million-student-engagements/) |
| **Handshake** | Handshake | Dominant US campus job network [M] | Free to students | Play listing active [V] | Jobs + employer messaging; AI career tools; paid "Handshake AI" projects [V] | Noise; ghosting [M] | Standard | [Handshake AI features](https://support.joinhandshake.com/hc/en-us/articles/38856960612631-About-AI-powered-features-in-Handshake-for-students) |
| **Final Round AI** | Final Round AI | Claims 10M+ users; $6.88M seed [V2] | Copilot ~$149–299/mo [V2] | Trustpilot 2.9 (277 reviews, 18 Sep 2026) [V2] | Real-time answer help; mock interviews | Billing complaints; reliability; **ethics: "undetectable" stealth mode**; Amazon ban [V2] | Desktop overlay; not designed for AT [I] | [loopcv review](https://blog.loopcv.pro/final-round-ai-review/), [favtutor](https://favtutor.com/articles/final-round-ai-review/) |
| **Yoodli** | Yoodli | $40M Series B (Dec 2025); ~$60M raised; customers include SAP, Google, Snowflake, Korn Ferry [V] | Free tier; enterprise [M] | n/a | Private speech/roleplay feedback; filler-word stats | Metrics can feel reductive [I] | Transcripts; voice-centric | [GeekWire](https://www.geekwire.com/2025/ai-roleplay-startup-yoodli-raises-40m-reports-900-revenue-growth/) |
| **Big Interview** | Big Interview | Widely licensed by universities (e.g., Yale, UConn) [V] | $39/1 mo, $99/3 mo, $299 lifetime [V] | G2 listed [V2] | Structured curriculum + video practice | Dated UI; generic [M] | Video-centric | [biginterview.com pricing](https://www.biginterview.com/pricing/personal) |
| **Springboard** | Springboard | Reports 91% of eligible grads get offers within 1 year (company) [V2] | ~$7,000–16,200; job guarantee with conditions [V2] | Course Report listed | Mentors; job guarantee | Price; fine print on guarantee [V2] | Standard | [MentorCruise review](https://mentorcruise.com/blog/springboard-review-2026-the-job-guarantee-fine-print-cost-and-who-qualifies/) |
| **Seekho** (short-video benchmark) | Seekho (India) | 100M+ lifetime downloads; 92M in 2025; 4M paid subscribers; FY25 revenue ₹141.5 crore [V2] (repo + press) | Low INR subscription | ~4.3–4.5 [E] | Reels-style practical career videos; 28–29 min/day [V2] | Subscription pressure after trial [E] | Vernacular audio; caption quality varies | [Digital Terminal](https://digitalterminal.in/trending/seekho-app-crosses-100-million-downloads-adds-2175-million-users-in-2025) |

Also relevant: **General Assembly** (multiple layoff rounds reported by employees [V2]; the bootcamp model is under strain [I]); **Pramp** (free peer mock interviews [M]).

### Feature matrix
| Feature | Coursera PC | Forage | Handshake | Final Round | Yoodli | Big Interview | Springboard | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Multi-week portfolio project | partial | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Differentiate:** employer-briefed, 6–8 weeks |
| Employer-designed tasks | partial | ✓ | partial | ✗ | ✗ | ✗ | partial | **Parity+** |
| Human mentor feedback | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Parity** (group mentoring, lower cost) |
| AI mock interview | ✗ | ✗ | partial | ✓ | ✓ | ✓ | partial | **Improve:** accommodations, transparent rubric |
| Live-interview "copilot" | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | **Reject:** deception; employers ban it |
| Eye-contact / facial-affect scoring | ✗ | ✗ | ✗ | partial | partial | ✗ | ✗ | **Reject:** emotion recognition; disability bias |
| Process log (how AI was used) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Hiring-manager review / demo day | partial (consortium) | partial | ✓ (jobs) | ✗ | ✗ | ✗ | partial | **Differentiate** |
| Job guarantee | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Reject for MVP:** creates perverse incentives; publish outcomes instead |
| Weekly subscription plans | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | **Reject:** fair-billing charter |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| F1 | **Sprint Studio** ★ signature | 6–8 week project sprints (for example "AI-assisted market analysis for a regional credit union") with a brief, milestones, sample data and a clear definition of done | Portfolio beats certificates [V2] | Differentiate | MVP | Must |
| F2 | **Process log** ★ | Auto-captured timeline of drafts, prompts used, checks made and human edits. The learner curates what to show. | Hiring managers want to see judgement, not just AI output [I] | Differentiate | MVP | Must |
| F3 | **Fair Interview Coach** ★ | AI interviewer (labelled "AI practice interviewer") for behavioural, case and role-specific questions. Rubric feedback on structure (STAR), evidence and clarity. Question preview, pause, extra time and text mode. **No affect or eye-contact scoring.** | Yoodli/Big Interview parity [V]; ethics | Improve | MVP | Must |
| F4 | **Mentor reviews** | Two 30-minute group reviews per sprint (captioned video, or text-only asynchronous) with an industry mentor | Springboard's valued mentors [V2] | Parity | MVP | Must |
| F5 | **Portfolio page** | Public, accessible web page of projects with process highlights; connects to the Skills Passport | Proof | Differentiate | MVP | Must |
| F6 | **Skills Passport** (shared) | Verified skills from sprints; carries AI Fluency Lab credentials | Shared layer | Differentiate | MVP | Must |
| F7 | **Hiring-partner showcase** | A monthly demo day (live and recorded) plus a reviewer queue where partner hiring managers rate portfolios on a short rubric | Riskiest assumption | Differentiate | MVP | Must |
| F8 | **Story Builder** | Turns project evidence into CV bullets and interview stories. The learner writes; AI suggests; nothing is fabricated (claims link to evidence). | Integrity | Improve | MVP | Should |
| F9 | **Weekly plan + gentle goals** | Milestone plan with pause weeks; no streaks | Lumen P15 | Lumen | MVP | Must |
| F10 | **My Needs + accommodations** | Text interview mode, extra time, captions, plain-language briefs, 60+ preset, screen-reader-ready editors | Aisha persona; Lumen | Lumen | MVP | Must |
| F11 | **Peer pods** | Groups of 4–6 learners with a shared channel and weekly check-in (moderated) | Completion in cohorts ≥50% vs MOOCs 5–15% [M] (repo) | Parity | MVP | Should |
| F12 | Case-manager console | WIOA and college dashboards: enrolment, milestones, completion and placement self-reports (with consent) | Luis persona | Differentiate | V1 | Must |
| F13 | Sprint library expansion | 20+ briefs across ops, marketing, data, CX, healthcare admin, IT support | Scale | Parity | V1 | Must |
| F14 | Employer-sponsored sprints | Partners co-design briefs and interview top completers | Sponsorship revenue | Differentiate | V1 | Should |
| F15 | Short-video micro-lessons | 60–120 s captioned how-tos inside each milestone (Seekho-style, not an infinite feed) | Seekho engagement [V2] | Improve | V1 | Could |
| F16 | Spanish UI + briefs | Localisation | WIOA reach | Parity | V1 | Should |
| F17 | Outcomes report | Published placement and interview rates by cohort, with methodology | P17; replaces "job guarantee" | Differentiate | V2 | Should |

MVP = F1–F11. **Core loop:** choose a sprint → weekly milestones → mentor review → portfolio → interview practice → showcase → interview earned.

## 5. Core experience & key user flows
**Core loop.** Monday plan → work session on a milestone (30–90 min) → submit → AI feedback plus a peer comment → Friday pod check-in → week summary → end. Interview practice sessions (15 min) are unlocked from week 3.

**Flow 1: Onboarding (≤5 min to first value)**
1. Passkey or Google/Apple sign-in, or a magic link.
2. My Needs quick card, including "I'd like interview accommodations" with no diagnosis required.
3. Pick a goal role (8 choices) and see 3 matched sprints with time per week shown.
4. Do the 5-minute "starter task" from the brief and get instant feedback. First value delivered.

**Flow 2: Sprint milestone**
1. The milestone brief shows the definition of done and example quality.
2. The learner works in their own tools or in the built-in workspace; AI tools are allowed and logged.
3. They submit the artefact plus the process log.
4. Rubric feedback arrives, including an AI-use rubric: disclosed, verified, improved by a human.
5. Optional resubmit, then milestone done, then the week summary.

**Flow 3: Fair Interview Coach**
1. Choose the type (behavioural, role case, "walk me through your project").
2. Set accommodations: text or voice, question preview on/off, time per answer (unlimited by default).
3. The AI interviewer asks 5 questions; a "Pause" button is always available.
4. Feedback on structure, evidence from the portfolio and clarity, with 1 thing to try next. There is no score for "confidence", eye contact or tone.
5. Transcript saved; delete at any time.

**Flow 4: Case-manager / college view (V1)**
- The case manager invites participants.
- They see milestone progress and flags ("no activity 10 days"), with the participant's consent notice shown.
- They export a WIOA-ready completion report.

**Flow 5: My Needs.** One tap from the header. Accommodation settings carry into the interview coach and mentor sessions (for example, mentors are told "prefers text chat").

**Flow 6: Billing.** Per-sprint price shown up front. No weekly plans. Refund within 14 days if fewer than 2 milestones are submitted. One-tap cancellation of the monthly plan.

**IA.** Home (This week) · Sprint · Interview · Portfolio · Pod · My Needs. Bottom navigation on mobile, top on web.

**Session design.** Milestone sessions are self-paced and autosave. Interviews default to 5 questions (about 15 min). Each session ends with a summary and "next step on {day}".

## 6. Inclusive, accessible & sensory design spec
- **Sensory Dial.** Default **Balanced**, following the OS. Calm: no animation, no sounds, and milestone completion shown as a check. Lively (opt-in): short celebration at sprint completion only.
- **Input modes.** Interview: voice, typed text or AAC-generated speech; the learner can switch mid-interview. Projects: keyboard, dictation, screen reader. Reordering tasks (Kanban) has a tap-then-tap and a keyboard alternative.
- **Targets.** ≥48 dp (≥56 dp with the 60+ preset); no gesture-only actions.
- **Typography.** 18 px body by default; dyslexia settings (font, spacing, tint); briefs available in plain language (≤ grade 8) and read aloud.
- **Audio.** Mentor sessions have live captions plus human-corrected captions on recordings. The interviewer voice speed is adjustable (0.7–1.3×). No sound-only cues. Headphone and hearing-aid streaming is supported via the OS.
- **Speech-disability text path.** A full text interview mode gives the same feedback, and a certificate of practice shows no difference between modes.
- **Themes.** "Studio" (neutral) and high contrast.

| # | Lumen principle | Acceptance criterion in Career Sprint |
|---|---|---|
| P1 | Calm/system settings | Reduce Motion → 0 animations; 200% text without truncation |
| P2 | Granular sound | Interviewer voice, effects and notifications on separate controls; visual twin for all cues |
| P3 | Predictable | Weekly plan structure identical each week; the interview flow is always "Setup → 5 questions → Feedback" |
| P4 | Targets | 48/56 dp; Kanban alternatives |
| P5 | Plain language | Brief summaries ≤ grade 8; jargon glossary |
| P6 | Dyslexia typography | WCAG 1.4.12 passes in the editor and portfolio |
| P7 | Multimodal | Interview accepts voice, text and AAC; projects accept any file type |
| P8 | Low penalty | Unlimited interview retakes; feedback framed as "try next" |
| P9 | Focus | No feed; one primary action per screen |
| P10 | Memory | Passkeys; the brief is visible alongside the work |
| P11 | Timing | Interview answer time unlimited by default; the user can choose realistic timing |
| P12 | My Needs | Accommodations free and require no diagnosis |
| P13 | Age-respectful | Professional look; no mascots |
| P14 | Caregiver/case-manager burden | Case-manager setup ≤10 min per cohort |
| P15 | Motivation | Weekly goals, pause weeks, no leaderboards |
| P16 | Affirming | Neurodivergent candidates' guidance co-written with an ND panel (for example, disclosure choices) |
| P17 | Honest claims | No "job guarantee"; outcome data with methodology |
| P18 | Privacy | Interview audio processed and discarded after transcription by default; no emotion inference |

**Lumen audit target:** ≥22/24.

## 7. AI specification & guardrails
**Does**
- AI interviewer (LLM plus ASR/TTS) with role question banks written by humans.
- Rubric feedback on artefacts and answers.
- Story Builder suggestions tied to evidence.
- Brief variants from employer inputs, reviewed by humans.

**Does not**
- Assist during real interviews: no overlay, no "stealth" mode, and a detection-friendly design.
- Score emotion, facial expression, eye contact or "confidence" (EU AI Act Art. 5 bans emotion recognition in workplace and education [V] (repo)).
- Rank candidates for employers.
- Write the portfolio for the learner (the process log shows human contribution).

**Pedagogical policy**
- Feedback ladder: question → hint → example.
- Mastery on milestones.
- Human mentor review at two points in each sprint.

**Safety and fairness**
- ASR word-error-rate testing by accent group, and for stuttering and dysarthric speech, before launch. Research shows large ASR performance gaps across speech disorders [V2]. Target: no group WER above 2× the baseline, and text mode is always one tap away.
- Rubric grader bias tests on dialect, non-native English, and neurodivergent answer styles (matched-quality pairs). Maximum gap 0.25 rubric points.
- Distress: if a learner writes about crisis or hopelessness during job-search stress, show resources and a human contact option. This is self-report based, never inferred.

**Hiring-partner boundary.** Partners see only portfolios the learner publishes. Partner ratings are feedback to the learner, **not** an automated screening tool. This keeps us outside NYC Local Law 144 / Illinois HB 3773 AEDT duties [V2] and EU AI Act Annex III employment uses. Legal review is needed before any "shortlist" feature.

**Evaluation.** 300 human-rated mock interviews for rubric agreement (κ ≥0.7). Red-teaming covers learners asking the coach to fabricate experience and employers requesting candidate rankings.

**Cost [E].** A 15-minute voice interview costs ~$0.15–0.40 in ASR+LLM+TTS. Per sprint, including feedback: ~$4–8 in AI and ~$25–40 in mentor time (group of 8).

## 8. Data, privacy & compliance
| Data | Purpose | Retention | Processing |
|---|---|---|---|
| Account, goals, My Needs | Service | Until deletion | Cloud |
| Artefacts, process logs | Portfolio, feedback | Learner-controlled | Cloud; public only if published |
| Interview audio | Transcription | Deleted after transcription (default) | Cloud ASR under zero-retention terms |
| Transcripts, feedback | Practice history | Learner-deletable | Cloud |
| WIOA reporting fields (V1) | Programme reporting | Per contract/state rules | Cloud; consented |

**Regimes.**
- GDPR/CCPA.
- EU AI Act: Art. 50 disclosure; Art. 5 (no emotion recognition); Annex III avoided by design.
- US AEDT laws if partners use data in hiring decisions: prohibited by contract.
- Illinois AI Video Interview Act if recorded video were used for evaluation by employers. We do not share interview recordings.
- FTC §5 on outcome claims.
- WIOA data-sharing agreements.

**Consent.** A separate consent covers publishing a portfolio and allowing partner review. Revocable.

## 9. Monetization & go-to-market
| Offer | Price | Benchmark |
|---|---|---|
| Sprint (B2C) | $149 per sprint or $29/mo (incl. interview coach) | Big Interview $39/mo [V]; Coursera PC ~$150–300 total [V2] |
| Interview coach only | $12/mo | Final Round ~$149+/mo [V2] |
| Workforce/college licence | $600–1,200 per completer (ITA-eligible) | Springboard $7k+ [V2] |
| Hiring-partner brief sponsorship | $5–15k per brief per year | Forage is employer-funded [V] |

- **Channels:** community colleges and university career centres (Big Interview's channel [V]); American Job Centers and WIOA ETPL listing; hiring-partner co-marketing; creator partnerships on short video; AI Fluency Lab alumni.
- **ASO:** "portfolio projects", "mock interview practice", "career change", "AI job skills". Education category. Accessibility Nutrition Label completed.
- **Markets:** US first; UK V1 (graduate schemes); Spanish UI in V1.

## 10. Success metrics
- **North star:** hiring-manager-reviewed projects per active learner. Target ≥1 per completed sprint.
- **Inputs:**
  - sprint completion (≥55%)
  - mentor reviews attended (≥80%)
  - interview practice sessions per learner (≥4)
  - portfolios published (≥70% of completers)
- **Outcomes:**
  - interviews earned within 90 days (self-report + partner confirmation; target ≥35% of completers [E])
  - offers within 180 days (tracked, not promised)
  - Evidence plan: cohort comparison with waitlisted applicants in the WIOA pilot (Tier 2).
- **Guardrails:**
  - Sensory Comfort ≥4/5
  - accommodation users' satisfaction equal to others (±0.3)
  - ASR WER gap thresholds
  - zero billing complaints
  - zero incidents of the coach fabricating experience in shipped suggestions
- **Retention:** sprint-based; D30 ≥60% of enrolled (in-sprint); re-enrolment in a second sprint ≥25%.

## 11. Validation plan
**Riskiest assumptions**
1. Hiring partners value sprint portfolios (vision).
2. Learners complete 6–8 weeks without a job guarantee.
3. Workforce boards will fund it per completer.
4. Accommodation-first interview practice is as useful as "realistic" timed practice.

| # | Experiment | Sample | Success | Kill |
|---|---|---|---|---|
| X1 | **Concierge sprint:** 1 brief, mentors via video, AI interviewer as Wizard-of-Oz (a human reads scripted questions) | 15 learners, 5 hiring managers reviewing portfolios | ≥3 of 5 managers say they would interview ≥30% of completers; ≥60% completion | <2 managers positive or <40% completion |
| X2 | Portfolio blind test: portfolio + process log vs. certificate-only CV | 20 hiring managers, 40 profiles | Portfolio profiles get ≥1.5× interview intent | No difference |
| X3 | Interview accommodation test (text vs. voice; timed vs. untimed) | 16 participants incl. 6 ND/disabled | Perceived usefulness ≥4/5 in all conditions | Accommodated modes rated <3.5 |
| X4 | Price smoke test ($149 sprint vs. $29/mo vs. $49/mo) | Landing page, adults only | ≥8% waitlist; ≥30% choose paid | <3% |
| X5 | WIOA channel discovery | 6 workforce boards | ≥2 willing to list on ETPL after the pilot | 0 |

**Mapping.** WP2 (15 workers aged 20–34), WP4 (X1–X3), WP5 (X4–X5).

## 12. Build handoff
**Epic A: Sprint Studio**
- Given an enrolled learner, when they open a milestone, then the brief, definition of done and example are visible without scrolling at 200% zoom on desktop.
- Given a submission, when feedback is generated, then it includes an AI-use rubric row and at least one evidence-linked comment.

**Epic B: Fair Interview Coach**
- Given a learner selects text mode, when the interview starts, then no microphone permission is requested.
- Given any interview, when feedback is shown, then no score for emotion, tone or eye contact exists in the UI, API or data model.
- Given answer time "unlimited", when the learner is silent for 60 s, then no auto-advance occurs, and a gentle "Take your time. Tap Continue when ready." appears.

**Epic C: Portfolio & Passport**
- Given a published project, when a partner opens it, then it passes axe-core with 0 serious issues, and the process log summary is readable by screen reader.

**Epic D: Showcase**
- Given a hiring manager rates a portfolio, when the learner views it, then the rating appears as feedback and is never used to rank learners for other partners.

**Epic E: Billing**
- Given a monthly subscriber, when they tap Cancel, then cancellation completes in ≤2 taps with no retention offer interstitial beyond one optional pause.

**Non-functional requirements**
- Performance: interview turn latency <1.5 s p95 (voice).
- Platforms: web, iOS and Android.
- Accessibility: WCAG 2.2 AA.
- Localisation: EN and ES.
- Security: SOC 2 path; public portfolio pages have no tracking pixels.

**QA focus**
- AT matrix: VoiceOver, TalkBack, NVDA, Voice Control, Switch.
- ASR by speaker group.
- AI safety: fabrication requests, candidate-ranking attempts, distress disclosures.
- Billing: sprint refund rules, cancel flow.
- COPPA: N/A (18+).

**Shared dependencies.** Lumen DS, My Needs, AI orchestration (voice stack), Skills Passport, evidence engine (outcome tracking), consent ledger.

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Hiring managers don't engage | Med | High | Sponsor-paid briefs; small reviewer asks (5 min per portfolio) |
| Entry-level market keeps shrinking | High | High | Target roles where AI-augmented juniors are hired; career-switch focus |
| Learners want a guarantee | Med | Med | Transparent outcomes; refund on early exit |
| Coach misused to prepare fabricated stories | Med | Med | Evidence-linked Story Builder; fabrication refusals |
| AEDT regulation if partners use ratings | Low | High | Contract, product boundaries |
| Mentor cost | Med | Med | Group reviews; asynchronous text reviews |

**Open questions.** Which roles have hiring managers who still hire juniors in 2026–27? Can sprints qualify for WIOA ETPL in the first states quickly enough? Should the interview coach be free to drive acquisition?

## 14. Sources
- [V2] NY Fed / NPR on graduate unemployment: https://www.npr.org/2026/08/18/nx-s1-5910677/recent-college-graduates-employment-job-artificial-intelligence · https://www.rezi.ai/posts/entry-level-jobs-and-ai-2026-report
- [V] Forage 10M engagements: https://eab.com/about/newsroom/press/forage-job-simulations-surpass-10-million-student-engagements/ · outcome claim via https://careerhub.students.duke.edu/blog/2026/01/10/forage-upskill-through-job-simulations/
- [V2] Google Career Certificates: https://grow.google/certificates/ · https://skillscouter.com/is-a-google-career-certificate-worth-it/
- [V2] Final Round AI: https://blog.loopcv.pro/final-round-ai-review/ · https://favtutor.com/articles/final-round-ai-review/ · https://www.experthire.io/blog/ai-cheating-in-interviews
- [V] Yoodli Series B: https://www.geekwire.com/2025/ai-roleplay-startup-yoodli-raises-40m-reports-900-revenue-growth/
- [V] Big Interview pricing: https://www.biginterview.com/pricing/personal
- [V] Handshake AI features: https://support.joinhandshake.com/hc/en-us/articles/38856960612631-About-AI-powered-features-in-Handshake-for-students · https://joinhandshake.com/blog/students/handshake-google-ai-plus-2026/
- [V2] Springboard: https://mentorcruise.com/blog/springboard-review-2026-the-job-guarantee-fine-print-cost-and-who-qualifies/
- [V2] General Assembly layoffs (employee reviews): https://www.glassdoor.com/Reviews/General-Assembly-Reviews-E459214.htm
- [V2] Seekho: https://digitalterminal.in/trending/seekho-app-crosses-100-million-downloads-adds-2175-million-users-in-2025 · https://inc42.com/startups/how-seekho-escaped-a-near-death-blow-to-build-an-inr-600-cr-edutainment-powerhouse/
- [V2] AEDT laws: https://www.dlapiper.com/en-us/insights/publications/2026/01/critical-audit-of-nyc-ai-hiring-law-signals-increased-risk-for-employers · https://introl.com/blog/illinois-ai-video-interview-law-employer-notification-2026
- [V2] ASR and atypical speech: https://www.jmir.org/2025/1/e60520/ · https://arxiv.org/pdf/2509.25048
- [V] Coursera Q2 2026: https://investor.coursera.com/news/news-details/2026/Coursera-Reports-Second-Quarter-2026-Financial-Results/default.aspx
- Repo: research/raw/01, raw/02 (Seekho, Coursera, Udemy), raw/05 (cohort completion benchmarks), raw/04 (EU AI Act Art. 5)

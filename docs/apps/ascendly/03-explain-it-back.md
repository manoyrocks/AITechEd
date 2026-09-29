# Explain It Back: App Strategy & Product Specification

> **Venture:** Ascendly · **App #:** 3/7 · **Ages:** 13–19 (plus teachers) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/03-ascendly-teens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research note:** WebFetch was blocked this session. [V] means confirmed in search-result text from the primary source's domain.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Show what you understand in 90 seconds — by voice, text, drawing or AAC — and build a proof-of-learning portfolio teachers can trust. |
| **Primary user / buyer** | Teens (users). **Teachers** (daily users and champions). **Schools/districts** (buyers of the proof-of-learning licence). |
| **Core job-to-be-done** | Teen: "When my teacher can't tell whether I did my own work, I want a quick way to show I really understand, so I get credit for my thinking." Teacher: "When I can't trust take-home work, I want fast evidence of each student's thinking, so I can keep assigning homework and target re-teaching." |
| **Category on the stores** | Education (13+), with a web teacher console. |
| **Top competitors** | Flip (discontinued 2024), Edpuzzle, Nearpod, Formative, Seesaw, Pear Deck, Brisk, MagicSchool, Khanmigo teacher tools, Socrative, Mote, Wayground (ex-Quizizz) |
| **Our wedge** | 1. **Proof of process, not detection:** short explanations beat unreliable AI detectors (false-positive problems for non-native writers [V2]). 2. **Any-mode answers** (voice, text, drawing, AAC, sign video) with identical rubrics — oral assessment without the oral-exam equity problems. 3. **Human in charge:** AI drafts rubric feedback and a misconception heat map; the teacher confirms any grade (EU AI Act-ready). 4. **Teen owns the portfolio** and chooses what leaves the classroom. |
| **Business model** | Teacher freemium (free for up to 3 classes). School/district licence $5–15/student/yr bundled with Study Coach. B2C: included in Ascendly Plus (personal portfolio). |
| **North-star metric** | Weekly verified understanding moments (teacher-confirmed or rubric-passed explanations) per active student. |
| **MVP candidate?** | **Yes** — Year 1 pilot in 10 schools. |

## 2. Problem & users

**Problem statement.** Teachers can no longer trust take-home work. One teacher told a news outlet in Sept 2026: "The cheating is off the charts. It's the worst I've seen in my entire career," and teachers report "anything you send home, you have to assume is being AI'ed" [V2: KTVZ/Stacker, 22 Sep 2026]. AI detectors are unreliable: a Stanford-led study found GPT detectors misclassified over 61% of essays by non-native English writers as AI-generated [V2: The Markup, Wikipedia]; Vanderbilt disabled Turnitin's AI detector in 2023 [V2]. Universities and some schools are reviving oral exams, but oral exams "may heighten anxiety, disadvantage non-native speakers, and produce inconsistent opportunities" unless criteria and accommodations are standardised [V2: The Conversation/phys.org, Aug 2026]. Microsoft's Flip, the most-used student video-response tool, went view-only on 1 Jul 2024 and closed fully in Oct 2024 [V2: Wikipedia, Windows Central], leaving a gap for short student explanations. Teens, meanwhile, fear surveillance ("it sends it to your teacher… scary") [V2: raw 03].

**Personas**
| Persona | Snapshot | Needs |
|---|---|---|
| **Mr. Chen, 10th-grade chemistry** | 150 students; has cut homework. | Fast evidence of thinking; misconception heat map; ≤10 min review per class. |
| **Aaliyah, 16** | Works hard, resents being suspected of AI use. | A way to show she understands, on her terms. |
| **Sam, 14, non-speaking autistic, uses AAC** | Understands science well; oral tasks exclude him. | Answer by AAC or typed text with the same rubric and no time pressure. |
| **Lina, 17, Deaf, ASL user** | Voice tasks don't fit. | Sign-video or text submissions, captioned teacher feedback. |
| **Ms. Park, instructional coach** | Wants an AI-era homework policy that is fair. | Assignment templates, integrity-by-design, data for PLCs. |

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Trustworthy evidence of understanding | Teachers assume homework is AI'ed [V2] | 60–120 s explanations with process prompts (why/how/what if) that are hard to outsource |
| Alternatives to detectors | 61% false positive on non-native writers [V2] | No AI detection; evidence from explanation + follow-up question |
| Equity in oral assessment | Oral exams disadvantage some students [V2] | Any mode, same rubric; untimed by default; accommodations from My Needs |
| Low grading load | 150+ students per teacher | AI draft feedback, class heat map, confirm-in-one-tap |
| Teen privacy | Surveillance fear [V2] | Teen previews what's submitted; portfolio private by default beyond the assignment |
| Replacement for Flip | Flip retired 2024 [V2] | Short-response recording with captions and threads, school-safe |

## 3. Competitive feature benchmark

| App | Publisher | Scale / grossing signal | Price | Rating | Loved features | Complaints | A11y / sensory | Source |
|---|---|---|---|---|---|---|---|---|
| **Flip (discontinued)** | Microsoft | Was the default student video tool; view-only from 1 Jul 2024, closed Oct 2024 [V2] | Was free | n/a | Student voice/video, teacher prompts, easy | Retired into Teams; videos lost if not exported | Captions; camera-centric | wikipedia.org; windowscentral.com |
| **Edpuzzle** | Edpuzzle | Widely used interactive-video platform [M] | Free; Pro from ≈$11.50–13.75/mo; schools custom [V2] | G2/Capterra high [V2] | Embedded questions in video; tracking | Free-tier storage limits | Captions depend on video source [E] | saasworthy.com; getapp.com |
| **Nearpod** | Renaissance | Large US K-12 footprint [M] | Gold $159/yr; Platinum $397/yr [V2] | n/a | Interactive lessons, drawing, open-ended responses | Cost; teacher-paced only | Mixed; slide-based [E] | nearpod.com/pricing |
| **Wayground (ex-Quizizz)** | Wayground | Used in 90% of US schools (company claim, Jun 2025) [V2: PR Newswire] | Freemium; school plans | n/a | Quiz games, AI accommodations (read-aloud, dyslexia font) | Speed-scoring legacy | Added dyslexia font, read-aloud [V2] | thejournal.com; prnewswire.com |
| **MagicSchool (MagicStudent)** | MagicSchool AI | 5M+ educators, 13,000+ schools; $45M Series B (Feb 2025) [V2] | Free; Plus ≈$8.33/mo; enterprise | n/a | 80+ teacher tools, rubric generation, student AI with teacher guardrails | Tool sprawl; quality varies [I] | Web; standard [E] | magicschool.ai; fast.io |
| **Brisk Teaching** | Brisk | 1M Chrome users; claims 2M+ teachers; $15M Series A (Mar 2025) [V2] | Free; premium/school | Chrome Web Store high [V2] | Inline AI feedback on Google Docs; "Boost" student activities | Feedback not scored/synced [V2] | Works in Docs [E] | chromewebstore.google.com; buildfastwithai.com |
| **Khanmigo teacher tools** | Khan Academy + Microsoft | Free for teachers in 49 countries [V2] | Free (teachers) | n/a | 25+ educator tools, rubric and lesson help | Student side paid outside districts | Khan a11y strong [V2] | microsoft.com/education blog |
| **Socrative** | Showbie | Long-standing quick-check tool [M] | PRO K-12 $89.99/yr [V2] | n/a | Fast exit tickets, short answers | Dated UI; limited media | Basic [E] | myengineeringbuddy.com |

**Also relevant:** Seesaw (multimodal portfolios with drawing, voice, video; free + custom plans [V2]) — strong for K-5, rarely used in high school [M]. Mote (voice comments in Google tools) [M]. Formative and Pear Deck (Renaissance/GoGuardian) — real-time checks [M].

**Feature matrix**

| Feature | Flip (legacy) | Edpuzzle | Nearpod | Wayground | MagicSchool | Brisk | Seesaw | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Student voice/video response | ✓ | ✗ | ◐ | ✗ | ✗ | ✗ | ✓ | **Parity** |
| Drawing response | ✗ | ✗ | ✓ | ◐ | ✗ | ✗ | ✓ | **Parity** |
| AAC / sign-video / text with same rubric | ✗ | ✗ | ◐ | ✗ | ✗ | ✗ | ◐ | **Differentiate** |
| AI rubric feedback on explanations | ✗ | ◐ | ✗ | ◐ | ✓ | ✓ (writing) | ◐ | **Improve**: teacher-confirmed, calibrated |
| Adaptive follow-up question ("why?") | ✗ | ✗ | ✗ | ✗ | ◐ | ✗ | ✗ | **Differentiate** |
| Class misconception heat map | ✗ | ◐ | ◐ | ◐ | ✗ | ✗ | ✗ | **Differentiate** |
| AI detection of cheating | ✗ | ✗ | ✗ | ✗ | ◐ | ◐ | ✗ | **Reject** (unreliable, biased) |
| Automated final grade | ✗ | ✓ (MC) | ✓ (MC) | ✓ (MC) | ◐ | ✗ | ✗ | **Reject** for explanations: teacher confirms |
| Student-owned portfolio beyond the class | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ◐ | **Differentiate** (Ascendly Record) |
| Captions on all media | ✓ | ◐ | ◐ | ◐ | n/a | n/a | ◐ | **Parity+** (auto + editable) |
| Webcam required | ◐ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject** (camera always optional) |
| Timed responses / speed scores | ✗ | ✗ | ◐ | ✓ | ✗ | ✗ | ✗ | **Reject** in core |
| Peer comments on public video wall | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **V2**, opt-in, moderated, text-only default |
| LMS/Classroom sync | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Parity** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| EB-01 | **Explain prompt library** | Teacher picks or writes prompts ("Explain why the reaction is exothermic"); AI suggests prompts aligned to a standard, teacher edits. | MagicSchool parity | Parity | MVP | Must |
| EB-02 | **Any-mode response tray** ★ | Voice (auto-captioned), typed text, drawing with labels, AAC text, sign video, photo of handwritten work. Camera never required. | Equity; Flip gap | Differentiate / Lumen | MVP | Must |
| EB-03 | **Adaptive "why?" follow-up** ★ | One AI follow-up question tailored to the response ("What would happen if…?"), answered in any mode. Hard to outsource; reveals depth. | Oral-exam benefit without live pressure [V2] | Differentiate | MVP | Must |
| EB-04 | **Rubric feedback draft** | AI scores against a 3–4 criterion rubric, quotes the evidence, flags possible misconceptions; labelled "draft". | Grading load | Improve | MVP | Must |
| EB-05 | **Teacher confirm-in-one-tap** ★ | Teacher sees draft + evidence, accepts, edits or overrides; only confirmed results become grades. Overrides train calibration for that class. | EU AI Act human oversight | Differentiate | MVP | Must |
| EB-06 | **Class misconception heat map** ★ | Clusters of misconceptions across the class with example (anonymised) snippets; "re-teach" suggestions. | Mr. Chen persona | Differentiate | MVP | Must |
| EB-07 | **Student preview & re-record** | Teen reviews and can redo before submitting; no penalty for retries. | Anxiety; P8 | Lumen | MVP | Must |
| EB-08 | **Accommodations from My Needs** | Untimed by default; teacher can set a soft window; extended time, read-aloud prompts, alternative modes flow automatically. | 504/IEP | Lumen | MVP | Must |
| EB-09 | **Portfolio save (Ascendly Record)** | Teen saves best explanations to their own Record; shares beyond the class only by choice. | Vision principle 3 | Differentiate | MVP | Must |
| EB-10 | **Google Classroom / LMS roster + grade passback** | Rostering via Classroom, Clever/ClassLink; confirmed scores pass back. | Adoption | Parity | MVP | Must |
| EB-11 | **Captions & transcripts** | Auto captions (editable by the student) on every voice/video response and teacher voice feedback. | Deaf/HoH | Lumen | MVP | Must |
| EB-12 | **Teacher voice/text feedback** | Teacher replies by short voice note (auto-captioned) or text. | Mote/Flip parity | Parity | MVP | Should |
| EB-13 | Study Coach bridge | Failed explanation → "practise this with Coach" link; passed Coach teach-it-back can be submitted as evidence. | Cross-app loop | Differentiate | V1 | Should |
| EB-14 | Department calibration | Teachers co-score 10 samples; system reports inter-rater agreement and AI drift. | Assessment quality | Improve | V1 | Should |
| EB-15 | Integrity policy templates | Per-assignment AI-use policy shown to students (e.g., "AI allowed for brainstorming only"). | Turnitin Clarity parity | Parity | V1 | Should |
| EB-16 | Parent summary (teen-approved) | Weekly one-screen summary of topics explained, if the teen consents. | Parents | Improve | V1 | Could |
| EB-17 | Peer explanation gallery | Opt-in, moderated, text-first; peers leave structured "I learned…" comments. | Flip parity | Parity | V2 | Could |
| EB-18 | College/career portfolio export | Teen exports selected explanations to Pathfinder / college applications. | Pathways | Differentiate | V2 | Could |

★ = signature. **Signature: any-mode explanation → adaptive "why?" → teacher-confirmed rubric feedback → class misconception heat map.** MVP = 12 features.

## 5. Core experience & key user flows

**Core loop (student):** assignment appears → read/listen to prompt → choose mode → explain → preview/redo → answer one "why?" follow-up → submit → feedback (after teacher confirms, or instant draft if teacher allows) → optionally save to Record.

**Core loop (teacher):** assign prompt (≤2 min) → responses arrive → review heat map → confirm drafts in bulk (with spot checks) → re-teach suggestion → done.

**Flow 1: Student onboarding (≤5 min)** — school SSO → one-screen privacy explainer ("Your teacher sees what you submit for this assignment. Nothing else. You can see exactly what they see.") → Sensory Dial and preferred response mode → practice prompt ("Explain how a bike brake works") with no grade.

**Flow 2: Core submission**
1. Prompt shown with read-aloud.
2. Teen picks Voice. Records 75 s; auto captions appear; teen edits one mis-heard word.
3. Follow-up: "You said heat is released. Where does that energy come from?" Teen answers by text.
4. Preview → Submit. Confirmation shows what the teacher will see.

**Flow 3: Teacher review**
1. Heat map: 40% of class confuse "bond breaking releases energy".
2. Teacher opens 3 example responses, adjusts one AI score, bulk-confirms the rest after sampling (default policy: teacher must open ≥20% or all flagged low-confidence items).
3. Re-teach card generated; teacher assigns a short follow-up prompt to the cluster.

**Flow 4: My Needs** — response-mode defaults, extended time, captions, read-aloud, Dial, "don't show me a score, just feedback" option.

**Flow 5: Billing (B2B)** — teacher free tier (3 classes); school licence via quote; no student payments ever inside a school deployment.

**IA:** Student: Assignments · My Explanations (Record) · My Needs. Teacher (web-first): Classes · Assign · Review (heat map + queue) · Calibration · Settings.

**Session design:** a submission takes 3–8 minutes. No timer by default. Designed end: "Submitted. You explained 3 ideas well; one to revisit."

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial:** Calm — no recording animations beyond a static "recording" label and a text timer (hideable); no sounds. Balanced — gentle level meter while recording. Lively — animated waveform, optional confirmation chime.

**Input modes per task**
| Task | Voice | Text | Drawing | AAC | Sign video | Handwriting photo | Switch |
|---|---|---|---|---|---|---|---|
| Main explanation | ✓ | ✓ | ✓ (with text labels) | ✓ | ✓ | ✓ | ✓ (via text/AAC) |
| Follow-up "why?" | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Teacher feedback | voice (captioned) or text | | | | | | |

The rubric evaluates **content, not delivery**: fluency, accent, speech rate, stuttering, grammar (unless the prompt is a language task) and handwriting neatness are explicitly excluded from scoring.

**Targets and gestures:** 44 pt / 48 dp; record button large and also triggered by keyboard; drawing canvas has shape/label tools and a text alternative ("describe your diagram").

**Reading/typography:** prompts at the profile's reading level where the teacher allows paraphrase; read-aloud; BDA defaults.

**Extended time:** untimed by default; soft windows only when a teacher sets them; accommodations override windows automatically (no teacher action needed per assignment).

**ADHD focus:** one step per screen; a 3-step strip (Explain → Why? → Submit); drafts auto-save; "sentence starters" to reduce blank-page paralysis.

**Anxiety and privacy:** practice mode unlimited and never graded; retries allowed; camera always optional; video visible only to the teacher unless shared.

**Age-respectful themes:** Minimal Light / Dark / High Contrast.

**Lumen principles**
| # | Acceptance criterion in Explain It Back |
|---|---|
| P1 | Recording UI static under Reduce Motion; Dial in 1 tap |
| P2 | Recording start/stop shown visually and haptically, never sound-only |
| P3 | Same 3-step strip on every assignment |
| P4 | Record, stop, redo, submit reachable by single tap and keyboard |
| P5 | Follow-up questions ≤25 words at profile reading level |
| P6 | BDA defaults in prompts and transcripts |
| P7 | ≥5 response modes available on every prompt unless the teacher restricts for a documented reason |
| P8 | Unlimited redo before submit; no penalty for retries |
| P9 | No feeds; submission ends with a summary |
| P10 | Prompt stays visible while answering |
| P11 | No uncontrollable time limits; accommodations override windows |
| P12 | Accommodations free and portable |
| P13 | Mature visual design |
| P14 | Teacher creates first assignment in ≤5 min |
| P15 | No leaderboards; growth shown privately |
| P16 | ND panel reviews rubric language; delivery-neutral scoring verified |
| P17 | No "detects cheating" or "proves authorship" claims; evidence tier stated |
| P18 | DPIA; no emotion inference from voice/video; video retention limits |

**Target Lumen score:** ≥22/24.

## 7. AI specification & guardrails

**AI does:** transcribe (ASR) and caption; generate one follow-up question per response; draft rubric scores with quoted evidence and a confidence value; cluster misconceptions across a class; suggest prompts and re-teach activities.

**AI does not:** assign final grades; detect "AI-written" content; analyse tone, emotion, facial expression, eye movement or voice stress (EU AI Act Art. 5 bans emotion recognition in education [V2: raw 05]); judge delivery (accent, fluency); share responses beyond the assignment.

**Models:** ASR robust to teen, accented and atypical speech (vendor + fine-tune on consented data only); LLM with rubric-grounded scoring prompts; embedding clustering for misconceptions; sign-video is **not** machine-interpreted at MVP — the teacher views it directly (captioned by the student if they choose) [I: sign-language recognition not reliable enough].

**Pedagogical policy:** prompts target explanation (why/how), transfer (what if) and error analysis; rubrics have 3–4 criteria with anchor examples; follow-ups probe the weakest criterion.

**Human oversight (EU AI Act Annex III-ready):** AI evaluation of learning outcomes is high-risk from **2 Dec 2027** [V2: Gibson Dunn]; we implement now: teacher confirmation for all grades; logging of AI drafts vs final; override reasons; per-class drift monitoring; FRIA template for EU deployers; clear student notice and the right to request human re-review.

**Safety:** no persona; AI disclosure on every AI-generated follow-up and feedback; distress statements in responses route to the school's designated safeguarding contact under the district protocol (students told at onboarding) and show crisis resources; content moderation on any peer-visible content (V2).

**Evaluation plan**
| Eval | Threshold |
|---|---|
| AI vs teacher rubric agreement | Quadratic-weighted κ ≥0.7 per criterion before drafts are shown; below that, AI gives comments only, no draft score |
| Delivery-neutrality | Score gap between matched content in fluent vs. accented/stuttered/AAC-synthesised speech ≤0.1 rubric points |
| ASR WER by speaker group | Published per group; fallback prompts if WER >15% for a speaker |
| Misconception cluster validity | ≥80% teacher agreement that clusters are meaningful |
| Follow-up question quality | ≥4/5 teacher rating on 200 samples |

**Cost [E]:** ~$0.01–0.04 per response (ASR + 2 LLM calls); ~$0.50–2 per student per year at typical use — viable at $5–15/student.

## 8. Data, privacy & compliance

| Data | Why | Retention | Where |
|---|---|---|---|
| Voice/video responses | Assessment | End of school year + 60 days unless saved to Record by the teen; video deletable by teen after grading | Cloud, encrypted, district region |
| Transcripts, drawings, text | Assessment | Same | Cloud |
| AI drafts, teacher overrides | Oversight logs | 3 years (audit) de-identified after 1 year | Cloud |
| Heat-map aggregates | Instruction | School year | Cloud |

**Regimes:** FERPA (school-official), SOPIPA and state laws (NY Ed Law 2-d, IL SOPPA, etc.), signed NDPA; COPPA not applicable to 13+ but we exclude under-13s; biometric laws (IL BIPA, TX) — **no voiceprints or face templates are created**, and we document this; UK AADC / GDPR for UK schools; EU AI Act Annex III + Art. 50; KOSA-ready; ADA Title II web rule for public-school deployers.

**Consent:** district DPA; student notice + teen-facing privacy explainer; separate teen consent to keep items in their personal Record after the course ends; no model training on responses without district and student opt-in (default off).

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Teacher Free | $0 | Up to 3 classes, all response modes, AI drafts, heat map |
| School | $5–15/student/yr (with Study Coach) | Unlimited classes, calibration, LMS passback, admin, DPA, SSO |
| District | Custom | Data warehouse export, FRIA support, PD |
| Personal (B2C) | In Ascendly Plus | Private portfolio practice |

Benchmarks: Nearpod $159–397/teacher/yr; Edpuzzle Pro ≈$138–165/yr; MagicSchool Plus ≈$100/yr; Khanmigo districts $10+/student [V2].

**Channels:** teacher communities and conferences (ISTE, NSTA), instructional coaches, "AI-era homework" PD workshops, state AI-guidance partners; Google Workspace Marketplace; Clever/ClassLink libraries. **ASO/SEO:** "Flip alternative", "oral assessment AI", "proof of learning", "AI-proof homework". Accessibility Nutrition Label after audit; publish a VPAT/ACR for procurement.

**Markets:** US first; UK (post-AADC review) V1; EU only after Annex III compliance package.

## 10. Success metrics
- **North star:** weekly verified understanding moments per active student (target ≥2 in pilot classes).
- **Inputs:** assignments per teacher per week (≥2); submission rate (≥75%); % teacher drafts confirmed within 48 h (≥80%); follow-up completion (≥90%).
- **Guardrails:** teen comfort ≥3.5/5 (A2 threshold) rising to ≥4; teacher value ≥4/5; delivery-neutrality gap ≤0.1; zero instances of AI grades released without teacher confirmation; Sensory Comfort ≥4/5.
- **Outcomes:** unit-test performance in pilot vs comparison classes; teacher time saved (self-report + logs).
- **Retention:** teacher W4 retention ≥60%; school renewal ≥85%.

## 11. Validation plan (no-code)

**Riskiest assumptions**
1. Teachers adopt proof-of-learning as homework (A2).
2. Teens don't feel surveilled (A2).
3. AI drafts are accurate enough to save teachers time.
4. Schools will pay.

**Experiments**
| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | Co-design sessions | 8 teachers (incl. 2 special ed) | Rubric + prompt templates agreed; ≥6/8 would pilot | <4/8 |
| E2 | **Paper/Google-Forms pilot** (students record voice memos or write; tutors apply rubric manually; teacher gets a hand-built heat map) | 4 classes (~120 students) | Teacher value ≥4/5; teen comfort ≥3.5/5; submission ≥70% | Teacher value <3 or comfort <3 |
| E3 | Wizard-of-Oz AI drafts (trained raters produce "AI" drafts under policy) | Same classes | Teachers accept ≥70% of drafts with minor edits; time per class review ≤15 min | — |
| E4 | Any-mode equity test | 10 students incl. AAC, Deaf, dyslexic, blind | All complete; scores match content not mode | Any group unable to complete |
| E5 | Purchase intent | 10 school leaders | ≥2 show purchase intent (WP5 threshold) | 0 |

**Mapping:** WP2 (teacher/counselor interviews), WP4 (E1–E4), WP5 (E5: "≥8 teachers commit to a pilot; ≥2 school leaders show purchase intent").

## 12. Build handoff

**Epic A: Assign**
- Given I'm a teacher with a synced class, When I choose a prompt and rubric, Then I can assign in ≤3 taps and students see it in their queue.

**Epic B: Respond in any mode**
- Given a student uses an AAC app that outputs text, When they submit, Then the response is scored with the same rubric as a voice response.
- Given a student records voice, When recording ends, Then captions appear and can be edited before submit.

**Epic C: Follow-up**
- Given a submitted response, When the AI generates a follow-up, Then exactly one question ≤25 words appears with AI disclosure, And the student can answer in any mode.

**Epic D: Review and oversight**
- Given AI draft scores exist, When a teacher bulk-confirms, Then the system requires they have opened ≥20% of responses and all low-confidence ones, And unconfirmed drafts are never shown as grades to students.
- Given a teacher overrides a score, Then the override and optional reason are logged.

**Epic E: Heat map**
- Given ≥10 responses, When the teacher opens Review, Then misconception clusters appear with counts and anonymised examples.

**Epic F: Privacy**
- Given a student, When they open "What my teacher sees", Then they see an exact preview of the teacher view.

**NFRs:** upload resilient on poor networks (resumable, offline recording queue); iOS, Android, web (Chromebook first-class); WCAG 2.2 AA; VPAT; captions within 30 s of upload; data residency options; SOC 2 path.

**QA focus:** AT matrix (VoiceOver, TalkBack, ChromeVox, Switch, AAC apps as input, braille); delivery-neutrality tests; AI safety (distress in responses, prompt injection inside student text); no-emotion-inference audit; FERPA role permissions; grade passback correctness; biometric non-creation audit.

**Platform dependencies:** Lumen answer tray (shared any-mode component); My Needs; AI orchestration (rubric scoring service, ASR, clustering); privacy stack (district DPAs, retention); evidence engine; Ascendly Record; teacher console shell (shared with Draft Mentor and Exam Ready).

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Teachers see it as extra work | Medium | High | Templates, heat map, bulk confirm; E2/E3 gates |
| Teens feel watched | Medium | High | Preview, no detection, private Record, co-design |
| AI scoring bias by speech/language | Medium | High | Delivery-neutral rubric; per-group evals; human confirmation |
| Students outsource explanations (script read-aloud) | Medium | Medium | Adaptive follow-up; in-class spot checks; evidence, not proof |
| Big platforms bundle it (Google Classroom, MagicSchool) | High | Medium | Depth in any-mode equity, oversight, Record portability |

**Open questions:** Should follow-ups ever be live (synchronous) for high-stakes tasks? What minimum sampling rule for bulk confirmation is acceptable to teachers? Can sign-language responses get peer/teacher captioning support?

## 14. Sources
- Flip retirement — https://en.wikipedia.org/wiki/Flip_(software) ; https://www.windowscentral.com/software-apps/from-flipgrid-to-flip-to-a-foot-in-the-grave-say-farewell-to-microsofts-standalone-education-focused-video-app [V2]
- Teacher cheating quotes — https://ktvz.com/stacker-k-12/2026/09/22/the-end-of-homework-teachers-grapple-with-cheating-in-the-age-of-ai/ [V2]
- Oral exams comeback — https://phys.org/news/2026-08-oral-exams-comeback-ai-problems.html ; https://theconversation.com/oral-exams-are-making-a-comeback-to-stop-ai-cheating-but-they-have-their-own-problems-289707 [V2]
- AI detector bias — https://themarkup.org/machine-learning/2023/08/14/ai-detection-tools-falsely-accuse-international-students-of-cheating ; https://www.vanderbilt.edu/brightspace/2023/08/16/guidance-on-ai-detection-and-why-were-disabling-turnitins-ai-detector/ [V2]; Turnitin's counter-study — https://www.turnitin.com/blog/new-research-turnitin-s-ai-detector-shows-no-statistically-significant-bias-against-english-language-learners [V]
- Edpuzzle/Nearpod pricing — https://www.saasworthy.com/product/edpuzzle/pricing ; https://nearpod.com/pricing [V2]
- Wayground rebrand — https://www.prnewswire.com/news-releases/quizizz-becomes-wayground-announces-new-ai-and-curriculum-supports-302489367.html ; https://thejournal.com/articles/2025/06/24/quizizz-rebrands-as-wayground-announces-new-ai-features.aspx [V2]
- MagicSchool — https://www.magicschool.ai/blog-posts/series-b-fundraise-for-teacher-ai [V]; https://fast.io/resources/magic-ai-review-2026/ [V2]
- Brisk — https://chromewebstore.google.com/detail/brisk-teaching-ai-that-wo/pcblbflgdkdfdjpjifeppkljdnaekohj ; https://www.buildfastwithai.com/ai-tools/brisk-teaching [V2]
- Khanmigo teacher tools — https://www.microsoft.com/en-us/education/blog/2024/08/khanmigo-for-teachers-your-free-ai-powered-teaching-tool/ [V2]
- Socrative/Seesaw pricing — https://www.myengineeringbuddy.com/blog/socrative-reviews-alternatives-pricing-offerings/ ; https://www.getapp.com/education-childcare-software/a/seesaw/ [V2]
- EU AI Act Omnibus — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ ; https://uniwise.eu/resources/blog/the-eu-ai-act-and-assessment-december-2027-is-not-a-snooze-button [V2]
- Studio raw research 03, 05 [V2]

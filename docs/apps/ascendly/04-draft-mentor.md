# Draft Mentor: App Strategy & Product Specification

> **Venture:** Ascendly · **App #:** 4/7 · **Ages:** 13–19 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/03-ascendly-teens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research note:** WebFetch was blocked this session. [V] means confirmed in search-result text from the primary source's own domain.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A writing mentor that asks the questions a great English teacher would, never writes your paragraphs, and lets you prove the words are yours. |
| **Primary user / buyer** | Teens 13–19 (users). Teachers (assign, review authorship). Schools (licence). Parents (Plus). |
| **Core job-to-be-done** | "When I have an essay due and a blank page, I want help getting my ideas organised and my argument stronger without AI writing it for me, so I get better at writing and nobody can accuse me of cheating." |
| **Category on the stores** | Education / Productivity (13+); Google Docs add-on + web editor + mobile companion. |
| **Top competitors** | Grammarly (incl. Authorship and AI agents), QuillBot, Google Docs + Gemini, Turnitin Clarity, Brisk, NoRedInk, Quill.org, Hemingway, Speechify, Draftback |
| **Our wedge** | 1. **Mentor, not ghostwriter:** questions, structure and evidence feedback; no generated paragraphs by default (teacher can set policy). 2. **Teen-controlled authorship timeline:** the process record belongs to the teen, who shares it by choice — the opposite of surveillance-first tools. 3. **Accessibility-first writing:** dictation, read-back, dyslexia-aware spelling support and focus mode are free, and dictation/AAC input counts as human authorship. |
| **Business model** | Free core (mentor limits per week, timeline, all accessibility). Ascendly Plus $12/mo / $79/yr. School licence $5–15/student/yr (with Explain It Back). |
| **North-star metric** | Weekly "revision moments": substantive student revisions made in response to mentor questions (measured by the timeline), per active writer. |
| **MVP candidate?** | **Later** (Year 2 in the vision doc); run discovery now because the Google Docs add-on vs stand-alone decision shapes the platform. |

## 2. Problem & users

**Problem statement.** Writing is where AI ghostwriting is easiest and most corrosive. 12th-grade NAEP reading scores in 2024 were the lowest ever recorded, with 32% below Basic [V2: NAGB, nationsreportcard.gov]. Teens have tools that *write* (Gemini, ChatGPT, QuillBot's paraphraser used by ~25–35M monthly users [V2: fueler.io, voiceflow]) and tools that *police* (AI detectors, which misclassified over 61% of non-native writers' essays as AI in one study [V2: The Markup]). The market is moving toward **process transparency**: Grammarly Authorship classifies text as typed, AI-generated, AI-modified or pasted and offers a playback [V: grammarly.com]; Turnitin Clarity (launched 4 Mar 2025) gives faculty writing time and edit history in a composition space [V: turnitin.com]; Draftback (500K+ users) replays Google Docs history, mostly used by teachers to catch AI use [V2: Chrome Web Store]. These tools mostly serve the **institution**. Nothing puts the teen in charge of both the learning (mentoring) and the evidence (timeline). Google also restricts Gemini "Help me write" in Docs to users 18+ in education editions [V2: flintk12], so under-18s lack a sanctioned in-editor writing coach.

**Personas**
| Persona | Snapshot | Needs |
|---|---|---|
| **Aaliyah, 16, AP Lang** | Strong ideas, weak structure; was wrongly flagged by a detector once. | Structure help; a way to show her process. |
| **Jordan, 17, dyslexic** | Dictates drafts; spelling support tools get flagged as "AI-modified". | Dictation and spelling help that count as his authorship. |
| **Diego, 18, first-gen, college essay** | Doesn't know what admissions essays should sound like. | Coaching on voice and story without an AI-written essay. |
| **Ms. Rivera, 11th-grade English** | 140 essays per cycle; unsure what's authentic. | Assignment-level AI policy, process summaries, less time policing. |

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Help without ghostwriting | Ghostwriting undermines skill (vision); NAEP decline [V2] | Question-led mentoring; no generated prose by default |
| Protection from false accusations | Detector bias [V2] | Teen-owned authorship timeline, shareable as evidence |
| Stay in Google Docs | Most school writing happens in Docs [I]; riskiest assumption | Docs add-on first, stand-alone editor second (validated in E1) |
| Accessibility supports that don't count as cheating | Grammarly categorises "AI-modified" text [V] | Assistive inputs (dictation, AAC, word prediction, spell-correct) labelled "assistive — student-authored" |
| Teacher clarity on AI use | Clarity sets AI use per assignment [V] | Per-assignment policy card, visible to student |

## 3. Competitive feature benchmark

| App | Publisher | Scale / grossing signal | Price | Rating | Loved | Complaints | A11y / sensory | Source |
|---|---|---|---|---|---|---|---|---|
| **Grammarly (Authorship, AI agents)** | Superhuman Platform Inc. (rebranded Oct 2025) | 40M+ DAU; ~$700M ARR (reported) [V2] | Free; Pro $12/mo annual ($144/yr) [V2] | High store ratings [M] | Corrections everywhere; Authorship playback; AI Grader and Citation Finder agents (Aug 2025) [V] | AI rewrite temptation; upsell; Authorship requires extension/tracking [I] | Works across apps; adds cognitive load (many suggestions) [I] | grammarly.com; sqmagazine.co.uk |
| **QuillBot** | Learneo (Course Hero) | 75M registered, ~25M MAU claimed; ~$100M revenue est. [V2/E] | Free; Premium ≈$8–10/mo [M] | High [M] | Paraphraser, summariser, "humanizer" | Used to disguise AI text; paywall [I] | Web/mobile [E] | fueler.io; voiceflow.com |
| **Google Docs + Gemini** | Google | Default school editor [M] | Free / Workspace Edu | n/a | Version history; Classroom integration; teacher AI feedback drafting (Feb 2026) [V] | "Help me write" 18+ only in Edu [V2] | Strong a11y baseline, voice typing [M] | workspaceupdates.googleblog.com; flintk12.com |
| **Turnitin Clarity** | Turnitin | Launched Mar 2025; university pilots Spring 2026 [V] | Institutional | n/a | Composition space; writing time + edit history; AI feedback when permitted [V] | Surveillance perception; institution-only [I] | Pilots assessing accessibility [V2: Colorado] | turnitin.com; oit.colorado.edu |
| **Brisk** | Brisk Teaching | 1M Chrome users; 2M+ teachers claimed [V2] | Free; premium | High | Inline Docs feedback; "Inspect writing" replay [M] | Teacher-centric | In Docs [E] | chromewebstore.google.com |
| **NoRedInk** | NoRedInk | Grades 3–12 classrooms; NWP partnership 2025 [V2] | Free core; Premium schools | n/a | Interest-based grammar/writing practice | Drill feel [M] | Web [E] | eschoolnews.com |
| **Quill.org** | Nonprofit | ~3M students/yr, 10% of US schools (Project Evident 2025) [V2] | Free | n/a | Free sentence-level coaching with instant feedback | Sentence-level only [I] | Web; read-aloud limited [E] | quill.org |
| **Draftback** | Independent | 500K+ users [V2] | Free | n/a | Replays Doc history; local processing | Used to catch students [V2] | n/a | draftback.com |

**Also:** Hemingway (readability highlighting, one-time/desktop + AI plans) [M]; Speechify (55M users, 4.7 iOS, ~$139/yr; read-back for proofreading) [V2].

**Feature matrix**

| Feature | Grammarly | QuillBot | Docs+Gemini | Turnitin Clarity | Brisk | Quill.org | Draftback | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Grammar/spelling correction | ✓ | ✓ | ✓ | ◐ | ✗ | ◐ | ✗ | **Parity** (assistive, labelled) |
| Paraphrase / rewrite my text | ✓ | ✓ | ✓ (18+) | ✗ | ◐ | ✗ | ✗ | **Reject** by default; teacher can allow "suggest a rewording of one sentence" with labelling |
| Generate paragraphs/essays | ✓ | ✓ | ✓ (18+) | ✗ | ◐ | ✗ | ✗ | **Reject** (core principle) |
| "Humanizer" to evade detection | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject** |
| Socratic questions on argument/evidence | ◐ | ✗ | ◐ | ◐ | ◐ | ◐ | ✗ | **Differentiate** |
| Rubric-based feedback | ✓ (AI Grader) | ✗ | ◐ | ✓ | ✓ | ◐ | ✗ | **Parity**, framed as questions not grades |
| Source finding + citation | ✓ (Citation Finder) | ✓ | ◐ | ✗ | ✗ | ✗ | ✗ | **Improve**: teen finds sources; mentor checks credibility and citation format |
| Process/authorship record | ✓ | ✗ | ◐ (version history) | ✓ | ◐ | ✗ | ✓ | **Parity**, teen-owned |
| Teen controls who sees record | ✓ (share report) | n/a | ✗ | ✗ (faculty) | ✗ | n/a | ✗ (anyone with edit access) | **Differentiate** |
| Assistive input counted as human | ✗ (dictation fine; AI-modified flagged) | n/a | ✓ | ? | n/a | n/a | n/a | **Differentiate** |
| Per-assignment AI policy | ◐ | ✗ | ◐ | ✓ | ◐ | ✗ | ✗ | **Parity** |
| Dyslexia-aware spelling + read-back | ◐ | ✗ | ◐ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Focus/distraction-free mode | ◐ | ✗ | ✗ | ◐ | ✗ | ✗ | ✗ | **Parity+** |
| AI-detection score | ◐ (separate detector) | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | **Reject** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| DM-01 | **Docs add-on + web editor** | Mentor sidebar inside Google Docs (primary) and a minimal web editor (for non-Docs schools and mobile). | Riskiest assumption; Docs is where writing happens [I] | Parity | V1-MVP | Must |
| DM-02 | **Brainstorm by questions** ★ | Mentor asks 3–6 questions to surface the teen's own ideas; captures answers as notes the teen owns. | Mentor, not ghostwriter | Differentiate | MVP | Must |
| DM-03 | **Outline builder** | Teen drags—or taps "move up/down"—their own notes into claim/evidence/reasoning blocks; mentor questions gaps. | Structure need | Improve | MVP | Must |
| DM-04 | **Argument & evidence feedback** ★ | Paragraph-level questions ("Which sentence proves this claim?") and rubric-aligned comments; no rewritten text. | Grammarly AI Grader parity, pedagogically safer | Differentiate | MVP | Must |
| DM-05 | **Authorship timeline (teen-owned)** ★ | Records typing, dictation, pastes (with source prompt), mentor interactions; playback; summary card. Stored in the teen's Record; shared only by teen action or assignment submission they approve. | Grammarly Authorship/Clarity parity with teen control | Differentiate | MVP | Must |
| DM-06 | **Assistive-input labelling** | Dictation, AAC, word prediction and spell-correct logged as "assistive — student-authored". | Jordan persona; equity | Differentiate / Lumen | MVP | Must |
| DM-07 | **Per-assignment AI policy card** | Teacher sets allowed help levels (Questions only / + sentence-level suggestions / + source help); shown at top of the doc. | Clarity parity | Parity | MVP | Must |
| DM-08 | **Read-back & dictation** | TTS read-back with highlighting for proofreading; dictation with punctuation commands. | Speechify parity; dyslexia | Lumen | MVP | Must |
| DM-09 | **Dyslexia-aware spelling** | Phonetic-misspelling correction (Ghotit-style) with explanations; optional. | Dyslexic writers | Lumen | MVP | Should |
| DM-10 | **Focus mode** | One paragraph visible, hidden toolbars, optional timer, "park an idea" list. | ADHD | Lumen | MVP | Should |
| DM-11 | **Source credibility coach** | Teen pastes a source; mentor asks lateral-reading questions and formats the citation (MLA/APA/Chicago). | Citation Finder alternative | Improve | MVP | Should |
| DM-12 | **Teacher process summary** | Teacher sees, for submitted work: writing sessions, time span, % typed/dictated/pasted, mentor questions used — not keystrokes. | Ms. Rivera persona | Differentiate | MVP | Must |
| DM-13 | Revision challenges | Mentor proposes one revision goal per session ("strengthen your counterargument"); timeline marks completion. | North star | Improve | V1 | Should |
| DM-14 | College essay mode | Story-mining questions, voice feedback, admissions-norm guidance; strict no-generation. | Diego persona | Differentiate | V1 | Should |
| DM-15 | Peer review workflow | Structured peer comments (glow/grow) with moderation. | Classroom practice | Parity | V1 | Could |
| DM-16 | Microsoft Word add-in | Same sidebar in Word. | Market coverage | Parity | V2 | Could |
| DM-17 | Multilingual writers | Home-language brainstorming, English drafting; translation of mentor questions. | ELL equity | Improve | V2 | Could |

★ = signature. **Signature: question-led mentoring plus a teen-owned authorship timeline.** MVP = 12 features.

## 5. Core experience & key user flows

**Core loop:** open assignment → see AI policy card → brainstorm (questions) → outline → draft (typing/dictation) → mentor feedback (questions) → revise → proofread by read-back → submit with timeline summary (teen approves) → natural end.

**Flow 1: Onboarding (≤5 min)** — install add-on from school Marketplace or open web editor → privacy card ("Your timeline is yours. It's saved only while you work in Draft Mentor. You choose who sees it.") → Dial and input preferences → sample 3-question brainstorm on the teen's actual assignment.

**Flow 2: Core writing session**
1. Teen opens "Persuasive essay: phone bans". Policy card: "Questions + source help allowed."
2. Mentor: "What's one thing you've seen happen when phones are banned?" Teen answers by voice. Notes appear in the sidebar.
3. Outline builder: teen orders notes into claim/evidence.
4. Teen drafts. Mentor comments on paragraph 2: "Your claim says bans improve focus. Which evidence shows that?"
5. Teen revises; timeline logs a revision moment.
6. Read-back highlights a missing word. Session summary: "2 revisions, 38 min writing. Next: counterargument."

**Flow 3: Pasted text** — if the teen pastes >25 words, the add-on asks "Where is this from?" (quote with citation / my own notes / AI tool / other). Label is stored. No accusation.

**Flow 4: Teacher view** — teacher opens a submitted essay's process summary card and optional playback (only if the teen included it). Class dashboard shows mentor question types used and common feedback themes.

**Flow 5: My Needs** — dictation language, read-back voice, dyslexia spelling on/off, font/spacing, focus mode default, Dial.

**Flow 6: Billing** — Plus via web (no in-app purchase needed for add-on); fair-billing charter; school licence removes all student payments.

**IA:** Sidebar tabs: Mentor · Outline · Sources · Timeline · My Needs. Web editor adds Documents list.

**Session design:** teen-chosen; optional 25-minute focus sprints; wrap-up prompt "Want to note where to start next time?"

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial:** Calm — no animations, suggestions appear only when requested ("Ask mentor" button), no underlines except spelling; Balanced — gentle highlight of mentor comments; Lively — animated timeline and progress ring. Default: Calm for the editor (writing needs quiet) [I].

**Input modes:** typing, dictation (with voice commands), AAC text input, word prediction, switch access via OS, handwriting-to-text on tablets, keyboard-only navigation of the sidebar (all mentor actions have shortcuts).

**Targets/gestures:** 44 pt/48 dp; outline reordering by drag **or** up/down buttons (WCAG 2.5.7).

**Reading/typography:** mentor questions at profile reading level (grade 6–8 default); BDA defaults in the web editor; respects Docs zoom and high-contrast; read-back with word highlight and speed control.

**Extended time:** no timers unless chosen; timeline never shows "time taken" to teachers as a performance measure — only as authorship span.

**ADHD focus:** focus mode; chunked tasks ("next: write your topic sentence"); park-it list; body-doubling link to Study Squad.

**Assistive authorship guarantee:** dictation, AAC, predictive text and spelling correction are categorised as student-authored; the teacher summary explains this in plain language.

**Age-respectful themes:** Paper (light), Ink (dark), High Contrast.

**Lumen principles**
| # | Acceptance criterion in Draft Mentor |
|---|---|
| P1 | No animations under Reduce Motion; mentor never auto-pops |
| P2 | No sounds by default; read-back on its own slider |
| P3 | Sidebar tabs fixed; policy card always at top |
| P4 | All outline actions possible without drag |
| P5 | Mentor questions ≤30 words at profile reading level |
| P6 | Web editor meets BDA defaults; Docs zoom respected |
| P7 | Brainstorm accepts voice, text, AAC |
| P8 | No scores on drafts by default; feedback as questions |
| P9 | No streaks; session ends with a "next time" note |
| P10 | Notes and outline visible while drafting |
| P11 | No time limits |
| P12 | Dictation, read-back, dyslexia spelling free |
| P13 | Mature themes |
| P14 | Teacher sets policy in ≤1 min per assignment |
| P15 | Revision goals chosen by teen |
| P16 | ND panel reviews mentor tone |
| P17 | Never claims to "prove" authorship; timeline is evidence, not proof |
| P18 | Keystroke-level data never leaves device unless teen shares playback; DPIA |

**Target Lumen score:** ≥22/24.

## 7. AI specification & guardrails

**AI does:** generate brainstorming questions from the prompt and the teen's answers; analyse structure (claim/evidence/reasoning) and ask targeted questions; rubric-aligned comments; source credibility questions and citation formatting; spelling correction; summarise the timeline.

**AI does not (default policy):** write sentences, paragraphs, thesis statements or conclusions; paraphrase the teen's text; produce "model essays" on the teen's topic; detect AI; estimate grades. Teachers may enable *sentence-level suggestions* (one sentence at a time, clearly labelled and logged as "AI-suggested, student-accepted").

**Pedagogical policy:** questions first; one focus per paragraph; feedback tied to the teacher's rubric; the teen must act (revise or dismiss with reason) for the mentor to move on.

**Safety:** no persona; AI disclosure in the sidebar; personal-narrative essays may include sensitive disclosures (college essays, memoirs) — the mentor responds supportively, shows crisis resources if risk language appears, and does **not** notify anyone automatically in B2C; school deployments follow the district protocol disclosed at onboarding. No emotion inference.

**Hallucination controls:** citation formatter uses metadata lookups (DOI/ISBN/URL), never invents sources; mentor cannot assert facts about the teen's topic except via cited retrieval.

**Evaluation plan**
| Eval | Threshold |
|---|---|
| Ghostwriting leakage (red team: 500 "just write it" attempts) | ≤1% produce >15 consecutive words of new prose |
| Feedback usefulness (teacher raters, 200 drafts) | ≥4/5 |
| Question quality vs. teacher-written questions | Not inferior in blind rating |
| Timeline classification accuracy (typed/dictated/pasted/AI-suggested) | ≥98% |
| Bias: feedback tone/quality across dialects and ELL writing | No significant difference in rated helpfulness |

**Cost [E]:** ~$0.02–0.06 per writing session.

## 8. Data, privacy & compliance

| Data | Why | Retention | Where |
|---|---|---|---|
| Document text (in Docs) | Mentoring | Not stored by us beyond the session; Docs remains the source | Google (school domain) + transient processing |
| Timeline events | Authorship record | Teen-owned; stored in Record; deletable (unless already submitted to a teacher, where the school copy follows school retention) | On-device buffer → cloud Record |
| Mentor notes/outline | Continuity | Teen-owned | Cloud |
| Teacher policy settings | Assignment | School year | Cloud |

**Regimes:** FERPA/SOPIPA; Google Workspace Marketplace policies for education add-ons and OAuth scopes (least privilege: per-file access); COPPA (13+ only); UK AADC; state design codes; KOSA-ready; EU AI Act (feedback that steers learning may fall within Annex III — implement human oversight: teacher sets policy and reviews); keystroke logging treated as sensitive — minimisation (we store events, not raw keystrokes).

**Consent:** teen consents to timeline recording each document (on by default within Draft Mentor, visible indicator, can pause — pausing is shown in the summary); separate consent to share playback.

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Free | $0 | Mentor questions (≈20 per week), timeline, read-back, dictation, dyslexia spelling, citations |
| Plus | $12/mo or $79/yr | Unlimited mentoring, college-essay mode, all Ascendly Plus |
| School | $5–15/student/yr | Policy cards, teacher summaries, dashboard, SSO, DPA |

Benchmarks: Grammarly Pro $144/yr; QuillBot Premium ~$100/yr [M]; Speechify ~$139/yr [V2]; Brisk and MagicSchool freemium [V2].

**Channels:** English departments and NCTE/NWP communities; Google Workspace Marketplace; "false AI accusation" content (teens protecting themselves); college-essay season content (Aug–Dec). **ASO/SEO:** "essay help without AI writing", "prove you wrote it", "writing coach for students", "dyslexia writing tool". Accessibility Nutrition Label + VPAT.

**Markets:** US first; UK V2 (GCSE English).

## 10. Success metrics
- **North star:** weekly revision moments per active writer (target ≥4).
- **Inputs:** brainstorm completion (≥60%); feedback → revision rate (≥40% of mentor questions lead to a revision); timeline share rate at submission (≥50% in school deployments).
- **Guardrails:** ghostwriting leakage ≤1%; teen privacy comfort ≥4/5; Sensory Comfort ≥4/5; zero incidents of timeline shared without teen action.
- **Outcomes:** rubric score change draft-1 → final and across assignments (teacher-scored); pilot comparison on an in-class timed essay.
- **Retention:** teen W4 ≥40% in assignment-driven cohorts; teacher term retention ≥70%.

## 11. Validation plan (no-code)

**Riskiest assumptions**
1. Teens will write inside our tool rather than plain Google Docs (vision).
2. Teens accept a timeline if they own it.
3. Question-only mentoring is useful enough under deadline pressure.
4. Teachers trust process summaries more than detectors.

**Experiments**
| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | Concept test: Docs add-on vs stand-alone (clickable Figma of both) | 30 teens, 10 teachers | ≥70% prefer the add-on (decides architecture); both concepts ≥3.5/5 desirability | Both <3/5 |
| E2 | Wizard-of-Oz mentor in a shared Doc (trained writing tutors comment only with questions under policy) | 20 teens over 2 assignments | ≥60% revise in response to ≥2 questions; teen usefulness ≥4/5 | <30% revise |
| E3 | Timeline comfort (Figma playback + ownership explainer) | 30 teens | Comfort ≥3.5/5 with teen control; ≥ +1 point vs "teacher-owned" variant | Comfort <3 |
| E4 | Teacher trust test: detector score vs process summary on 10 sample essays | 10 teachers | ≥7/10 prefer process summary for decisions | — |
| E5 | Dyslexic writers' accessibility round | 6 dyslexic teens | Task success ≥90%; assistive labelling understood | — |

**Mapping:** WP1 (audit of Grammarly Authorship, Clarity, Brisk), WP2, WP4 (E1–E3, E5), WP5 (teacher/school interest).

## 12. Build handoff

**Epic A: Mentor questions**
- Given the policy is "Questions only", When a teen asks "write my intro", Then the mentor declines in one friendly sentence and asks a question that helps them start, And no generated prose is shown.

**Epic B: Timeline**
- Given timeline recording is on, When the teen pastes 40 words, Then a source prompt appears, And the paste is labelled by the teen's choice.
- Given the teen dictates, Then the text is labelled "assistive — student-authored".
- Given the teen pauses recording, Then the summary shows the paused interval without judgement.

**Epic C: Sharing**
- Given a submission, When the teen opens Share, Then they preview the teacher summary and choose whether to include playback.

**Epic D: Policy**
- Given a teacher sets "sentence-level suggestions allowed", When the teen accepts a suggestion, Then it is labelled "AI-suggested, student-accepted" in the timeline.

**Epic E: Accessibility**
- Given VoiceOver/ChromeVox, When navigating the sidebar, Then every mentor comment is reachable, announced with its paragraph reference, and actionable by keyboard.

**NFRs:** sidebar response ≤2 s p50; minimal OAuth scopes; works on Chromebooks with 4 GB RAM; WCAG 2.2 AA; English MVP; SOC 2 path.

**QA focus:** AT matrix incl. ChromeVox and Docs screen-reader mode; ghostwriting jailbreaks (role-play, "translate this", "continue my sentence", prompt injection in the essay); timeline tamper tests; privacy (no teacher access without share); dictation WER by speaker group.

**Platform dependencies:** Lumen; My Needs; AI orchestration (writing-mentor policy engine); privacy stack; Ascendly Record; teacher console.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Teens won't leave plain Docs | High | High | Add-on-first; E1 decides |
| Google/Grammarly bundle similar features | High | High | Teen ownership, assistive-authorship fairness, question-only pedagogy |
| Timeline gamed (typing out AI text by hand) | Medium | Medium | Timeline is evidence, not proof; pair with Explain It Back follow-ups |
| Question-only help frustrates under deadline | Medium | High | Fast, specific questions; teacher-allowed sentence suggestions |
| Keystroke data sensitivity | Low | High | Event-level only; on-device buffer; teen control |

**Open questions:** Should the timeline be verifiable (signed) for college admissions use? How to handle collaborative writing? Do teachers want playback or only summaries?

## 14. Sources
- Grammarly Authorship — https://www.grammarly.com/blog/company/grammarly-launches-grammarly-authorship/ ; https://www.grammarly.com/blog/academic-writing/grammarly-authorship-just-got-a-major-update/ [V]
- Grammarly AI agents (AI Grader, Citation Finder) — https://www.grammarly.com/blog/company/grammarly-launches-ai-agents/ [V]; https://siliconangle.com/2025/08/18/grammarly-leans-writing-assistance-agents-students-professionals/ [V2]
- Grammarly/Superhuman scale and pricing — https://sqmagazine.co.uk/grammarly-ai-statistics/ ; https://www.eesel.ai/blog/grammarly-pricing ; https://www.grammarly.com/blog/company/announcing-company-rebrand-to-superhuman/ [V2]
- Turnitin Clarity — https://www.turnitin.com/press/turnitin-launches-turnitin-clarity-bringing-transparency-and-integrity-insights-to-education [V]; https://oit.colorado.edu/services/consulting-professional-services/academic-technology-initiatives-team/technology-evaluations-pilots/turnitin-clarity [V2]
- QuillBot statistics — https://fueler.io/blog/quillbot-usage-revenue-valuation-growth-statistics ; https://www.voiceflow.com/blog/quillbot-ai [V2]
- Gemini in Docs age limits — https://flintk12.com/blog/gemini-for-students-keep-lock-down-or-replace [V2]; teacher feedback drafting — https://workspaceupdates.googleblog.com/2026/02/educators-now-get-help-drafting-personalized-guidance-on-written-assignments-with-AI.html?m=1 [V]
- Draftback — https://draftback.com/ ; https://chromewebstore.google.com/detail/draftback/nnajoiemfpldioamchanognpjmocgkbg?hl=en-US [V2]
- Quill.org / NoRedInk — https://www.quill.org/ ; https://www.eschoolnews.com/uncategorized/2025/04/09/noredink-and-the-national-writing-project-partner-to-inspire-the-next-generation-of-writers-in-the-age-of-gen-ai/ [V2]
- Speechify — https://apps.apple.com/us/app/speechify-text-to-speech-pdf/id1209815023 ; https://www.roborhythms.com/speechify-review-2026/ [V2]
- NAEP 2024 grade 12 reading — https://www.nationsreportcard.gov/reports/reading/2024/g12/ [V]; https://www.chalkbeat.org/2025/09/09/naep-scores-12th-grade-math-reading-declines/ [V2]
- AI detector bias — https://themarkup.org/machine-learning/2023/08/14/ai-detection-tools-falsely-accuse-international-students-of-cheating [V2]
- Brisk — https://chromewebstore.google.com/detail/brisk-teaching-ai-that-wo/pcblbflgdkdfdjpjifeppkljdnaekohj [V2]
- Studio raw 04 (Ghotit dyslexia writing tools) [V2]

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep |
| **Ships in** | Ascendly app (S3) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 75/100 [I] |
| **Consumes engines** | EN-03, EN-10 |
| **Studio features used** | SX-09, SX-24 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = DM-02, DM-04, DM-05, DM-06, DM-07.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| DM-E1 | **AI-use disclosure draft** | An AI-use statement drafted from the authorship timeline, which the teen edits and chooses whether to submit. |
| DM-E2 | **Home-language drafting** | Multilingual writers draft in their strongest language, then revise into English (DM-17 promoted to V1). |

### 15.3 New validation question
Docs add-on vs. stand-alone editor preference, n=30 teens and 10 teachers.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 5 | 3 | 4 | 4 | 3 | 3 | 4 | 3 |

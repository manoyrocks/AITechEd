# Exam Ready: App Strategy & Product Specification

> **Venture:** Ascendly · **App #:** 2/7 · **Ages:** 14–19 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/03-ascendly-teens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research note:** WebFetch was blocked this session. [V] means the fact appeared in search-result text from the primary source's own domain; pages were not opened in full.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Exam prep that tells you honestly how ready you are, practises the way memory actually works, and never locks your flashcards away. |
| **Primary user / buyer** | Teens 14–19 preparing for SAT/ACT, AP, IB, GCSE/A-level or state tests (user). Parents (seasonal pass payer). Schools (licence for AP/state-test cohorts). |
| **Core job-to-be-done** | "When an exam is weeks away and I don't know where I stand, I want a plan and practice that shows me what I actually know, so I can spend limited time where it counts and walk in calm." |
| **Category on the stores** | Education (13+). |
| **Top competitors (by downloads / revenue)** | Quizlet, Khan Academy + College Board Bluebook, Knowt, Anki, Seneca, Save My Exams, Fiveable, Magoosh / UWorld / PrepScholar / Kaplan / Princeton Review |
| **Our wedge** | 1. **Readiness score with confidence bands**, built on human-reviewed, exam-aligned items (not AI slop). 2. **Free, exportable flashcards and spaced retrieval forever** (the Knowt trust play, done without ads). 3. **Accommodations-native practice:** extended time (1.5×/2×), read-aloud, screen-reader items and no required timers, matching 504/IEP and College Board accommodations. |
| **Business model** | Free core (flashcards, spaced review, diagnostic, one exam's practice bank sample). Seasonal exam passes $50–150 per exam season. Included in Ascendly Plus ($12/mo or $79/yr) for one exam at a time. School licence $5–15/student/yr. |
| **North-star metric** | Weekly "retrieval wins": items answered correctly on spaced review after ≥1 day's delay, per active teen. |
| **MVP candidate?** | **Yes.** Year 1: 1–2 exams (recommend Digital SAT math + one AP subject). |

## 2. Problem & users

**Problem statement.** Good test prep is either free but scattered (Khan Academy + Bluebook + YouTube + Reddit) or expensive (UWorld $299–449, PrepScholar $397–495/yr, Magoosh from $129 [V2: PrepScholar, Test Prep Insight]). Flashcard tools that teens rely on have moved behind paywalls: Quizlet locked Learn and Test modes behind Plus in 2022, and in 2026 free users face capped Learn rounds [V2: nibble-app, myengineeringbuddy]. A Trustpilot reviewer said Quizlet "removed the option to export your flashcards" [V2: raw 03], and students migrated to Knowt, which now reports 7M+ students [V2: Play listing] but faces "features moving behind the Ultra paywall" complaints [V2: coursebox]. Retrieval practice and spacing work: meta-analyses report medium effects for testing (g≈0.50) and larger effects at delays over a day (g≈0.69) [V2: Springer/ERIC via search]. Most apps still teach by re-reading and speed games. Timed modes (Quizlet Match, Kahoot) exclude slower readers and screen-reader users [V2: raw 01].

**Personas**
| Persona | Snapshot | Needs |
|---|---|---|
| **Aaliyah, 16, SAT + AP Chem** | Wants a 1400+. Uses Bluebook, Khan and Quizlet. Doesn't know if she's "ready". | An honest readiness score, a weekly plan, and practice that matches the real exam. |
| **Jordan, 17, dyslexic, 504 plan (1.5× time, read-aloud)** | Practice apps time him out; he never practises with his real accommodations. | Practice that runs at 1.5× by default, with read-aloud and a dyslexia-friendly layout that mirrors test day. |
| **Priya, 15, GCSE (UK)** | Seneca is free but feels repetitive. Save My Exams costs money. | Exam-board-specific retrieval, past-paper-style questions, calm revision. |
| **Ms. Diaz, AP Biology teacher** | Wants to know which units her class is weak on, 6 weeks out. | Class readiness by unit, no extra grading. |

**Needs & wants**
| Need | Evidence | How Exam Ready addresses it |
|---|---|---|
| Know where I stand | "Ready?" is the top anxiety for test prep [I]; Bluebook gives scores but no longitudinal plan [I] | Diagnostic + readiness score with confidence band, updated after every session |
| Free, portable flashcards | Quizlet paywall and export anger; Knowt migration [V2: raw 03] | Free unlimited decks, import from Quizlet/Anki/CSV, export anytime (CSV, Anki .apkg) |
| Practice that matches the exam | Forum stack is Khan + Bluebook [V2: raw 03]; AP exams now in Bluebook (16 fully digital, 12 hybrid in 2026 [V2: collegehelpguide]) | Human-reviewed, blueprint-aligned items; digital-format practice mirrors Bluebook tools (calculator, annotation, flagging) |
| Practise with my accommodations | SAT extended time is 1.5× or 2× (3h21m or 4h28m plus breaks) [V: College Board accommodations] | My Needs stores accommodations; timers off by default; mocks run at the chosen multiplier |
| Affordable | UWorld/PrepScholar $299–495 [V2] | $50–150 season pass; free core |
| Trustworthy content | Duolingo "AI slop" backlash [V2: raw 03] | Human-authored/reviewed banks; AI variations only within reviewed templates |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Quizlet** | Quizlet Inc. | 50M+ Play; 26M downloads in 2025 [V2] | Free (ads, capped Learn); Plus $7.99/mo or $35.99/yr; Plus Unlimited $44.99/yr [V2] | 4.7 Play (~916K) [V2] | Huge shared-set library; Learn mode; AI study guides | Paywall creep; export removed; "cashgrab" | TTS on cards; timed Match hard with AT [V2: raw 01] | nibble-app.com; myengineeringbuddy.com |
| **Khan Academy + Bluebook** | Khan Academy / College Board | Khan 10M+ Play [V2]; Bluebook is the official SAT/AP testing app | Free | Khan ≈4.1–4.7 [V2] | Official, free, personalised SAT skills; full-length adaptive practice tests in Bluebook [V] | Full-length SAT tests moved off Khan to Bluebook only [V2]; dated mobile UX | Khan "fully accessible with VO" (AppleVis) [V2]; Bluebook supports accommodations in practice [V] | satsuite.collegeboard.org; blog.collegeboard.org |
| **Knowt** | Knowt | 500K+ Play (4.5, 8.8K reviews); 4.7 iOS (11K); claims 7M+ students [V2] | Free core with ads; Ultra paid tier [V2] | 4.5–4.7 | Quizlet import; free Learn mode and practice tests; AI notes → cards | Ads; features drifting behind Ultra [V2] | Standard; no dyslexia settings noted [E] | play.google.com; coursebox.ai |
| **Anki** | Ankitects → transitioning to AnkiHub (Feb 2026) [V2] | Default for med students and language learners [V2: raw 03] | Free except AnkiMobile $24.99 one-time [V2] | n/a | FSRS scheduler built-in since 23.10 [V2]; open source; ownership of data | Steep UI; card creation is the bottleneck [V2: raw 03] | Customisable; screen-reader support varies by client [E] | mindomax.com; flica.app |
| **Fiveable** | Fiveable | Leading AP-specific brand; 42 AP subjects [V] | $79/yr or $29/mo; $129/yr with printing [V] | n/a | AP study guides, FRQ practice with AI grading, cram sessions | Price for teens; AI grading trust [I] | Web-first [E] | fiveable.me/pricing |
| **Seneca Learning** | Seneca | 14M+ students claimed; 1,500+ exam-board courses [V2] | Free; Premium add-ons | ≈4.x Play [E] | Free, exam-board specific, adaptive quizzes | Repetitive; gamified [V2: TSR] | Web and app; read-aloud in premium [M] | senecalearning.com; cognito.org |
| **Save My Exams** | Save My Exams | Large UK GCSE/A-level library [V2] | ≈£48/yr [V2] | n/a | Examiner-written notes, topic questions, past papers | Paid; text-heavy | Web-first [E] | cognito.org; savemyexams.com |
| **Magoosh / UWorld / PrepScholar** | Various | Premium SAT/ACT prep | Magoosh from $129; UWorld $299–449; PrepScholar $397–495/yr [V2] | n/a | Explanations; question quality (UWorld) | Price; short access windows (UWorld 30-day tier) [V2] | Web-first; varies | testprepinsight.com; blog.prepscholar.com |

**Feature matrix** (✓ yes · ✗ no · ◐ partial)

| Feature | Quizlet | Khan+Bluebook | Knowt | Anki | Fiveable | Seneca | UWorld | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Free unlimited flashcards | ◐ | n/a | ✓ | ✓ | ✗ | ◐ | ✗ | **Parity** |
| Import from Quizlet/Anki | ✗ | ✗ | ✓ | ◐ | ✗ | ✗ | ✗ | **Parity** |
| Export any time | ✗ | ✗ | ◐ | ✓ | ✗ | ✗ | ✗ | **Differentiate** (charter promise) |
| Evidence-based spaced scheduler (FSRS-class) | ◐ | ◐ | ◐ | ✓ | ✗ | ◐ | ✗ | **Parity with Anki**, zero-config |
| Diagnostic → personal plan | ◐ | ✓ | ◐ | ✗ | ✓ | ◐ | ◐ | **Improve** (plan adapts to calendar) |
| Readiness score with confidence band | ✗ | ◐ (practice score) | ✗ | ✗ | ◐ (score calculator) | ✗ | ◐ | **Differentiate** |
| Official full-length adaptive practice | ✗ | ✓ | ✗ | ✗ | ◐ | ✗ | ◐ | **Integrate, don't duplicate**: link to Bluebook; import results manually |
| Human-reviewed, blueprint-aligned item bank | ◐ | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | **Parity** (moat over time) |
| AI-generated questions from notes | ✓ | ✗ | ✓ | ✗ | ◐ | ✗ | ✗ | **Improve**: allowed for personal decks only, clearly labelled, not counted in readiness |
| FRQ/essay scoring | ✗ | ✗ | ✗ | ✗ | ✓ (AI) | ✗ | ✗ | **V1**: AI draft score + rubric, human-review flag, never "official" |
| Error analysis ("why you got it wrong") | ◐ | ✓ | ◐ | ✗ | ◐ | ◐ | ✓ | **Improve** (misconception tags) |
| Extended-time mocks (1.5×/2×) | ✗ | ✓ (Bluebook, approved students) | ✗ | n/a | ✗ | ✗ | ◐ | **Differentiate** (no approval needed to practise) |
| Timed speed games / leaderboards | ✓ | ✗ | ✓ (Knowt Play) | ✗ | ✗ | ◐ | ✗ | **Reject** in core loop (Lumen P8/P11); optional untimed class review games only |
| Streaks with loss | ◐ | ✗ | ◐ | ✗ | ✗ | ◐ | ✗ | **Reject**. Weekly goals, pause days |
| Ads | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | **Reject** |
| Dyslexia typography / read-aloud items | ◐ | ◐ | ✗ | ◐ | ✗ | ◐ | ◐ | **Differentiate** |
| Teacher class readiness view | ◐ | ✓ | ◐ | ✗ | ✓ | ✓ | ✗ | **Parity** (V1) |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| ER-01 | **Exam + date setup** | Pick exam(s), test date, weekly hours, and accommodations (pulled from My Needs). | Planning; accommodations parity | Parity | MVP | Must |
| ER-02 | **Adaptive diagnostic** | 20–35 minute untimed-by-default diagnostic across the exam blueprint; can be split over days. | Khan/Fiveable parity | Parity | MVP | Must |
| ER-03 | **Readiness score with confidence band** ★ | Predicted score range per section (e.g., "Math 560–620, 80% band"), narrowing as evidence grows. Shows *why* (which units drive uncertainty). Never a single hard number. | No competitor gives honest uncertainty [I] | Differentiate | MVP | Must |
| ER-04 | **Personal weekly plan** | Plan built from readiness gaps and available hours; re-plans after missed days without guilt. | Anxiety reduction; P15 | Improve | MVP | Must |
| ER-05 | **Spaced retrieval engine** ★ | FSRS-class scheduler for all cards and bank items; daily review capped to the teen's chosen minutes. | Retrieval/spacing evidence [V2] | Parity (Anki) | MVP | Must |
| ER-06 | **Free flashcards with import/export** ★ | Unlimited decks; import Quizlet (paste/CSV), Anki (.apkg), CSV; export any time. | Quizlet anger, Knowt migration [V2] | Differentiate | MVP | Must |
| ER-07 | **Human-reviewed item bank (pilot exam)** | Blueprint-aligned items authored by credentialed writers, double-reviewed, with distractor rationales. AI only generates *variants* inside reviewed templates. | Content trust; riskiest assumption | Parity / moat | MVP | Must |
| ER-08 | **Error analysis + Study Coach handoff** | Each miss tagged with a misconception; "Work through this with Coach" opens the hint ladder, not the answer. | Cross-app loop | Differentiate | MVP | Must |
| ER-09 | **Accommodations-native practice** ★ | Timers off by default; optional mock timing at 1×/1.5×/2×/custom; read-aloud items; breaks as needed; mirrors Bluebook tools (line reader, highlighter, flag, calculator). | 504/IEP; College Board accommodations [V] | Differentiate / Lumen | MVP | Must |
| ER-10 | **Accessible items** | Every item has alt text for figures, MathML, data tables for graphs, and no drag-and-drop item types. | Marcus/Jordan personas | Lumen | MVP | Must |
| ER-11 | **Optional timed section mock** | Section-length mocks at the chosen multiplier with a calm visual timer (hideable). Full-length official practice → Bluebook link. | Realism without coercion | Improve | MVP | Should |
| ER-12 | **Gentle progress** | Weekly minutes goal, pause days, mastery map by unit; no streak loss. | Lumen P15 | Lumen | MVP | Must |
| ER-13 | **Record entry: mastery evidence** | Unit mastery and readiness history saved to the teen-owned Ascendly Record; shareable. | Vision shared layer | Differentiate | MVP | Should |
| ER-14 | Bluebook score import | Teen types in section scores from official practice tests to calibrate readiness. | Official-data calibration | Improve | V1 | Should |
| ER-15 | FRQ/essay practice with rubric feedback | AP FRQ and IB/GCSE extended responses; AI draft score shown with band and rubric lines; teacher can review. | Fiveable parity | Parity | V1 | Should |
| ER-16 | Teacher class readiness | Unit heat map for a class, from teen-shared data only. | Ms. Diaz persona | Parity | V1 | Should |
| ER-17 | More exams | ACT, 4–6 AP subjects, GCSE (AQA/Edexcel/OCR) maths and sciences, IB. | Market expansion | Parity | V1 | Should |
| ER-18 | Test-day readiness kit | Checklists, accommodation confirmation reminder, calm-breathing card (no clinical claims). | Anxiety | Improve | V1 | Could |
| ER-19 | Study-group review (untimed) | Friends review a shared deck together in Study Squad; no speed scoring. | Social study | Differentiate | V2 | Could |
| ER-20 | State tests and EOC exams | Aligned banks for state end-of-course exams sold to districts. | B2B | Parity | V2 | Could |

★ = signature. **Signature: the Readiness score with confidence bands, powered by free spaced retrieval and accommodations-native practice.** MVP = 13 features.

## 5. Core experience & key user flows

**Core loop:** open → "Today" shows N minutes of review and 1 focus unit → retrieval set (cards + items mixed) → feedback and error analysis → readiness update ("band narrowed by 20 points") → natural end with "next session: Thursday".

**Flow 1: Onboarding (≤5 min to first value)**
1. Choose exam and date (or "not sure yet").
2. Accommodations question, phrased neutrally: "Do you practise with extra time, read-aloud or other supports? You don't need to prove anything." Pre-filled from My Needs if present.
3. Import existing flashcards (optional).
4. First 5-question mini-diagnostic → first rough readiness band ("wide for now; it narrows as you practise").

**Flow 2: Core daily session (default 20 min, teen-chosen)**
1. Today card: "12 minutes review + 8 minutes Unit 4 (Stoichiometry)".
2. Mixed retrieval: one item per screen, answer tray (tap choices, type, dictate, math keyboard).
3. Wrong answer → why it's wrong (distractor rationale), misconception tag, "Try a similar one" or "Work it through with Coach".
4. Session summary: what improved, readiness change with band, next session scheduled. Stop.

**Flow 3: Optional mock section**
1. Teen chooses section and time multiplier (default from My Needs).
2. Pre-mock screen: tools list (calculator, line reader, flag), break rules, timer visibility toggle.
3. Mock runs; timer can be hidden; breaks on request.
4. Results: score range, time per item (private), units to review. No leaderboard.

**Flow 4: Teacher view (V1)** — teacher creates a class code; teens choose to share readiness by unit; teacher sees unit heat map and top misconceptions; can assign a focus unit (appears as a suggestion, not a mandate).

**Flow 5: My Needs** — accommodations (time multiplier, read-aloud, breaks, calculator on all sections if applicable), typography, Sensory Dial, input modes, daily review cap.

**Flow 6: Billing** — seasonal pass purchase shows exact dates covered (e.g., "until 31 May 2027") and **does not auto-renew**; Plus users get one exam included. Refund if the test is cancelled or moved.

**IA:** Today · Practice (units, mocks) · Cards (decks, import/export) · Progress (readiness, mastery map) · My Needs. Four-tab bar plus a settings entry.

**Session design:** default 20 minutes; teen-set; "2 more cards" transition warning; review cap prevents "review debt" pile-up (overdue cards are re-scheduled, not stacked).

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial**
| Level | Exam Ready changes |
|---|---|
| Calm (default if OS Reduce Motion) | No animation; no sounds; correct/incorrect shown by icon + word (never colour alone); mastery map static |
| Balanced (default) | Gentle card flip (cross-fade under Reduce Motion); optional soft tone |
| Lively | Animated mastery map fill; short skippable celebration at weekly goal |

**Input modes:** every item accepts tap and keyboard; grid-in and numeric items accept typed, dictated and math-keyboard input; no drag-and-drop item types (ordering items use "move up/down" buttons); switch scanning supported for choice items.

**Targets and gestures:** 44 pt / 48 dp; answer choices full-width; swipe-to-flip cards always has a button alternative.

**Reading and typography:** items keep official wording (reading level cannot change exam items), but *instructions, feedback and rationales* follow the reading-level dial. Read-aloud on all items including math (MathML speech). Dyslexia defaults (BDA 2023). Line reader and masking tool (mirrors Bluebook). Passage text reflows at 200–400% zoom.

**Extended time (504/IEP) spec:** multipliers 1×, 1.25×, 1.5×, 2×, custom, and "untimed". Stored in My Needs. Mocks display "Your time: 1.5×" at start. Break count and length configurable. Matches College Board's options (time and one-half; double time) [V].

**ADHD focus:** one item per screen; review capped by minutes, not count; "park this" for doubts; focus mode hides navigation; optional body-doubling link to Study Squad.

**Audio:** read-aloud voice slider; no music; visual equivalents for all cues.

**Age-respectful themes:** Minimal Light, Night Dark, High Contrast. No mascots.

**Lumen principles**
| # | Acceptance criterion in Exam Ready |
|---|---|
| P1 | Reduce Motion → card flips become instant; Dial in 1 tap |
| P2 | No audio-only feedback; all sounds off by default |
| P3 | Item layout identical across all item types; progress "7 of 15" always visible |
| P4 | No drag items; all tasks single-tap or keyboard |
| P5 | Feedback/rationales at profile reading level; official item text unchanged and labelled "exam wording" |
| P6 | BDA defaults; spacing override works in passages and tables |
| P7 | ≥2 input modes per item type; switch path verified for multiple choice |
| P8 | No lives/penalties; wrong answers give rationale; items can be retried later |
| P9 | Review cap enforced; no "one more" prompts; session summary always shown |
| P10 | Passage and question visible together (split view) with no memory demand |
| P11 | Timers off by default; every timer adjustable or removable (WCAG 2.2.1) |
| P12 | Accommodations free; flow to mocks automatically |
| P13 | Mature themes; no childish rewards |
| P14 | Teacher class set-up ≤5 min; one-screen class view |
| P15 | Weekly goals with pause days; no streak loss |
| P16 | ND panel reviews test-anxiety copy |
| P17 | Readiness score validity published (calibration error) before marketing "predicts your score" |
| P18 | No sale of test-taker data; no profiling for ads; DPIA done |

**Target Lumen score:** ≥22/24.

## 7. AI specification & guardrails

**AI does:** schedules review (FSRS-class model, deterministic not LLM); estimates readiness (item-response-theory model on calibrated items, Bayesian band); tags errors with misconceptions (LLM, constrained to a reviewed taxonomy); writes rationale paraphrases at the reading level (reviewed templates); generates item *variants* from reviewed templates (numbers, contexts) that pass automatic solver checks; drafts FRQ feedback (V1).

**AI does not:** author new item types without human review; count AI-generated personal-deck questions in readiness; claim an "official" or "guaranteed" score; use timing data to profile or shame; infer anxiety from behaviour.

**Pedagogical policy:** retrieval before re-reading; interleaving across units after initial mastery; feedback immediately after each item in practice, deferred in mocks; mastery gating by unit (3 correct spaced retrievals over ≥2 days).

**Readiness model:** IRT calibration from pilot responses (target ≥200 responses per item before the item counts at full weight); readiness band = 80% credible interval; shows "insufficient evidence" when band > 150 points (SAT scale) [E]. Calibrated against Bluebook practice scores the teen imports (V1).

**Safety:** AI disclosure on generated content; no persona; distress routing if a teen writes about crisis in any free-text field (same shared policy as Study Coach); no emotion inference.

**Hallucination controls:** variants solved by CAS; answer key must match; items with any disagreement go to human review. Humanities rationales only from reviewed text.

**Evaluation plan**
| Eval | Threshold |
|---|---|
| Item reviewer agreement (key + alignment) | ≥95% agreement between two reviewers; disagreements adjudicated |
| Variant correctness | 100% CAS-verified before release; 1% human spot-check with zero errors |
| Readiness calibration | Predicted band contains actual Bluebook/official score ≥75% of the time in the pilot |
| Misconception tagging | ≥85% agreement with teacher tags |
| FRQ AI scoring (V1) | Within 1 rubric point of teacher score ≥80% of cases; always "draft" |

**Cost [E]:** scheduling and IRT are cheap; LLM used for rationales/tags ≈$0.002–0.01 per session. Item authoring is the real cost: ~$15–40 per reviewed item [E], so a 1,500-item SAT math bank ≈$25–60K.

## 8. Data, privacy & compliance

| Data | Why | Retention | Where |
|---|---|---|---|
| Responses, timing | Scheduling, readiness | Account lifetime; deletable | Cloud |
| Accommodations | Accessibility | Until deleted; never shared without consent | Synced |
| Imported decks | Study | Teen-owned; exportable | Cloud |
| Official score entries | Calibration | Until deleted | Cloud |
| Class sharing | Teacher view | School year + 1 year | Cloud (FERPA) |

**Regimes:** COPPA 2025 (13+ only); FERPA/SOPIPA and state student-privacy laws for school licences; UK AADC / state design codes; KOSA-ready (no compulsive features); EU AI Act — readiness estimation that steers learning is within Annex III "evaluating learning outcomes / steering the learning process" (high-risk from **2 Dec 2027** [V2: Gibson Dunn]); we log, explain, and keep human override. **Trademark/licensing:** "SAT", "AP" and "Bluebook" are College Board marks; use nominative references only and never imply endorsement; no reproduction of released items without a licence.

**Consent:** teen consent; school DPAs; accommodations data treated as sensitive (explicit opt-in to share with a teacher).

**Stores:** Teen rating; no ad SDKs.

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Free | $0 | Unlimited flashcards, import/export, spaced review, diagnostic, readiness (wide band), 50 bank items per exam, all accommodations |
| Exam Pass | $50 (one AP/GCSE subject) – $150 (SAT or ACT full), one season, **no auto-renew** | Full bank, mocks, error analysis, readiness with narrow band |
| Plus | $12/mo or $79/yr | One exam pass included + all Ascendly Plus features |
| School | $5–15/student/yr | Class readiness, assignments, all exams for a cohort |

Benchmarks: Quizlet Plus $35.99/yr; Fiveable $79/yr; Magoosh $129; UWorld $299–449; PrepScholar $397+ [V2]. We price under premium prep and on par with Fiveable.

**Channels:** organic short-form ("how ready am I really?"), AP teacher communities, school counselors, libraries; import tool as an acquisition wedge ("bring your Quizlet sets"). **ASO keywords:** "SAT prep free", "AP practice", "flashcards export", "spaced repetition", "extended time practice". Accessibility Nutrition Label filled after audit.

**Markets:** US (SAT, AP) first; UK GCSE/A-level V1; IB V2.

## 10. Success metrics
- **North star:** weekly retrieval wins per active teen (target ≥40).
- **Inputs:** diagnostic completion (≥70%); plan adherence (≥50% of planned minutes); import usage (≥20% of new users); error-analysis → Coach handoffs.
- **Guardrails:** Sensory Comfort ≥4/5; readiness calibration ≥75%; zero auto-renew complaints (passes don't renew); test-anxiety self-report does not rise over the season; review-debt never exceeds 2× daily cap.
- **Outcomes:** pilot comparison of score change (official practice test 1 → final) vs matched Khan-only users; publish method and results (ESSA Tier 3 → 2).
- **Retention:** seasonal; target D30 ≥25% among teens with a test date within 90 days; DAU/MAU ≥30% in the final 6 weeks before an exam.

## 11. Validation plan (no-code)

**Riskiest assumptions**
1. A sufficiently high-quality aligned item bank can be built affordably (vision doc).
2. Teens trust and act on a *range* rather than a single predicted score.
3. Teens pay for a non-renewing pass when Khan + Bluebook are free.
4. Accommodations-native practice is valued by 504/IEP teens and their parents.

**Experiments**
| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | 100-item pilot bank for one AP subject (e.g., AP Chemistry), written by 3 writers, double-reviewed | 3 writers, 4 reviewers, 60 students | Reviewer agreement ≥95%; student-rated quality ≥4/5; cost/item ≤$40 | Agreement <85% or cost >$80/item |
| E2 | Readiness-band comprehension test (Figma) | 25 teens | ≥80% correctly interpret "560–620"; ≥60% prefer range + reasons | <50% interpret correctly |
| E3 | Accommodations concierge: 504/IEP teens practise with 1.5× timing and read-aloud in accessible HTML mocks | 12 teens with accommodations | SUS ≥75; ≥75% say it "feels like test day" | — |
| E4 | Pass fake-door (SAT pass $99 vs $149) | ~2,000 parent visitors | ≥8% waitlist; ≥25% choose pass | <3% |
| E5 | Quizlet import smoke test | 30 teens | ≥70% complete import in <2 min | — |

**Mapping:** WP1 (item-bank cost research, pricing teardown), WP2 (teen and teacher interviews), WP4 (E1–E3, E5), WP5 (E4).

## 12. Build handoff

**Epic A: Setup and diagnostic**
- Given I set my accommodations to 1.5× in My Needs, When I start a mock, Then the timer shows my adjusted time and I can hide it.
- Given I stop the diagnostic halfway, When I return, Then I resume at the same item with answers saved.

**Epic B: Retrieval engine**
- Given I have 120 overdue cards and a 15-minute cap, When I open Today, Then I see ≤15 minutes of review and the rest are rescheduled without a "you're behind" message.

**Epic C: Readiness**
- Given fewer than 30 calibrated responses, When I view readiness, Then I see "wide band — keep practising" and the band width in points.
- Given I import an official practice score, When readiness recalculates, Then the band updates and the change is explained in one sentence.

**Epic D: Flashcards import/export**
- Given a Quizlet set pasted as text, When I import, Then terms and definitions map correctly for ≥95% of rows and I can fix the rest.
- Given any deck, When I tap Export, Then I get CSV and .apkg files with no paywall.

**Epic E: Item accessibility**
- Given VoiceOver is on, When I open a graph item, Then I hear the alt text and can open a data table, And the math is read via MathML speech.

**NFRs:** item load ≤300 ms; offline review of downloaded decks and banks (sync later); iOS, Android, web; WCAG 2.2 AA; English (US/UK) MVP; security per studio stack; item-bank IP protected (watermarking, rate limits).

**QA focus:** AT matrix (VoiceOver, TalkBack, ChromeVox, Switch Control, Dynamic Type max, braille for math); timer-accommodation cases (1×, 1.5×, 2×, untimed, breaks); sensory A/B on mastery map; AI variant correctness; COPPA age gate; pass non-renewal and refund on test cancellation.

**Platform dependencies:** Lumen system (answer tray, typography); My Needs (accommodations); AI orchestration (CAS, tagging); evidence engine (calibration and score-gain study); Ascendly Record.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Item-bank cost/quality | High | High | Start with 1–2 exams; E1 gate; teacher-writer marketplace later |
| Khan + Bluebook "good enough and free" | High | Medium | Integrate (score import), don't compete on official tests; differentiate on readiness, cards, accommodations |
| Readiness mis-calibration harms trust | Medium | High | Ranges, publish calibration, "insufficient evidence" state |
| College Board trademark/licensing | Medium | Medium | Legal review; original items only |
| Seasonal churn | High | Medium | Passes, school licences, year-round cards |

**Open questions:** Which first AP subject maximises demand × verifiability? Should passes be refundable after the score release? How to handle GCSE exam-board variants efficiently?

## 14. Sources
- Quizlet pricing/paywall — https://nibble-app.com/blog/quizlet-cost ; https://www.myengineeringbuddy.com/blog/quizlet-reviews-alternatives-pricing-offerings/ [V2]
- Knowt listings — https://play.google.com/store/apps/details?id=com.knowt.app&hl=en_US ; https://apps.apple.com/us/app/knowt-ai-flashcards-notes/id6463744184 [V2]; Knowt vs Quizlet — https://www.coursebox.ai/blog/quizlet-vs-knowt [V2]
- College Board accommodations (extended time) — https://accommodations.collegeboard.org/how-accommodations-work/for-each-test/sat [V]
- Bluebook practice tests — https://satsuite.collegeboard.org/practice/practice-tests/bluebook [V]; Khan/College Board — https://blog.collegeboard.org/college-board-khan-academy-for-better-sat-prep [V]
- AP exams in Bluebook 2026 — https://www.collegehelpguide.com/blog/ap-exams-digital-2026-bluebook-what-changed/ [V2]; https://newsroom.collegeboard.org/college-board-transitions-most-ap-exams-digital-may [V]
- Fiveable pricing — https://fiveable.me/pricing [V]
- Anki pricing/ownership — https://www.mindomax.com/is-anki-free ; https://flica.app/article/is-anki-free [V2]
- Seneca / Save My Exams — https://cognito.org/blog/save-my-exams-vs-seneca ; https://senecalearning.com/en-gb/ [V2]
- Premium prep pricing — https://blog.prepscholar.com/prepscholar-vs-uworld-sat-prep ; https://testprepinsight.com/comparisons/magoosh-vs-kaplan-sat-act/ [V2]
- Retrieval/spacing meta-analyses — https://link.springer.com/article/10.1007/s10648-025-10035-1 ; https://pdf.retrievalpractice.org/MetaAnalysisGuide.pdf [V2]
- EU AI Act Omnibus — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ [V2]
- Studio raw research 01–05 and app-catalog.csv [V2]

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (lead) |
| **Ships in** | Ascendly app (S3) |
| **Build wave** | 1d |
| **Pre-discovery priority score** | 83/100 [I] |
| **Consumes engines** | EN-03, EN-04, EN-10 |
| **Studio features used** | SX-17, SX-31 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = ER-02, ER-03, ER-05, ER-06, ER-07, ER-09.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| ER-E1 | **Accommodations request helper** | Explains the exam board's accommodations and access-arrangements process, with a checklist to work through with the counselor. Guidance only. |
| ER-E2 | **Squad sync** | Turns the study plan into Study Squad sessions (EN-11). |

### 15.3 New validation question
Item-bank quality: reviewer agreement ≥0.8 on a 100-item pilot bank.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 5 | 5 | 4 | 4 | 4 | 3 | 3 | 4 |

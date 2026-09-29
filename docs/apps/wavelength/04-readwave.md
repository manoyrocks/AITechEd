# ReadWave: App Strategy & Product Specification

> **Venture:** Wavelength · **App #:** 4/7 · **Ages:** 5–14 (with mature themes for teen struggling readers) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/05-wavelength-neurodivergent.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary, or carried over from studio raw research · [M] memory · [E] estimate · [I] inference
> **Evidence tiers:** E1 FDA/RCT on product · E2 peer-reviewed product studies · E3 evidence-based method, product untested · E4 testimonials/contested

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Structured literacy that respects the reader: explicit, cumulative phonics and spelling with read-along that is patient with every voice, and stories that don't treat a 12-year-old like a 5-year-old. |
| **Primary user / buyer** | Users: dyslexic and struggling readers 5–14 (incl. ADHD, DLD, autistic hyperlexic-decoding gaps). Buyers: parents (B2C/ESA), dyslexia tutors, SENCOs/reading specialists (school licence). |
| **Core job-to-be-done** | "When reading feels like a wall, I want practice that goes step by step and never makes me feel stupid, so I can read the things *I* care about." Parent: "I want the structured literacy my tutor uses, between sessions, at a price I can manage." |
| **Category on the stores** | Education › Reading (Kids 6–8 / 9–11 age bands where applicable). |
| **Top competitors** | Nessy Reading & Spelling, Lexia Core5, Amira, Microsoft Reading Coach (free), Learning Ally, Speechify, Teach Your Monster to Read, HOMER; also Dyslexia Quest, Reading Horizons, Barton-based apps, Ghotit |
| **Our wedge** | 1) **Age-respectful structured literacy:** mature decodable texts (sport, gaming, science, comics-style) at early decoding levels, where Nessy is designed for 6–11 and seen as cartoonish for older kids [V/V2]. 2) **Speech-difference-tolerant read-along:** tap-to-read fallback, no penalty for accent, stutter or articulation, and teacher-verified miscues rather than auto-scores. 3) **Tutor-connected:** follows the scope and sequence the child's OG/structured-literacy tutor uses (lesson alignment), rather than competing with it. |
| **Business model** | Family plan; ReadWave tier ≈$9.99/mo or $79/yr [E]; tutor licence; school licence per student. |
| **North-star metric** | Weekly minutes of successful decoding practice (items read accurately, with any input mode) per active learner, with fluency gains measured monthly. |
| **MVP candidate?** | **Later** (Year 2 per vision sequencing). Spec prepared now for Gate 2 evaluation. |

## 2. Problem & users
**Problem statement.**
- Dyslexia affects an estimated 5–20% of people depending on definition [V2, raw 04]. Specific learning disability is the largest IDEA category [M].
- The **structured, explicit, cumulative phonics** part of Orton-Gillingham-style teaching is well supported. The *multisensory* component is not proven as the active ingredient: the Stevens et al. 2021 meta-analysis found non-significant, positive-direction effects [V2, raw 04].
- **Pain points today:**
  - Tutors are expensive, and apps are either cartoonish for older students (Nessy [V2]) or school-only (Lexia, Amira).
  - Access tools (Speechify, Learning Ally) help with reading *access* but not decoding. Learning Ally requires professional documentation of a print disability [V] ([Learning Ally](https://learningally.org/solutions-for-home/home-school-resources-join)). Speechify draws billing complaints and requires annual commitment [V2] ([roborhythms](https://www.roborhythms.com/speechify-review-2026/)).
- Read-aloud AI is error-prone for children:
  - Commercial ASR has had ≈30% weighted WER on school-age children with language disorders [V] ([ASHA JSLHR](https://pubs.asha.org/doi/10.1044/2021_JSLHR-21-00096)).
  - Even strong models post ~10% word-level WER on child reading speech in research settings [V2] ([arXiv 2406.07060](https://arxiv.org/pdf/2406.07060)).
  - AI reading tutors in schools have drawn public frustration (SFUSD coverage, Sept 2026 [V, headline only: https://sfstandard.com/pacific-standard-time/2026/09/25/pst-sf-amira-ai-in-schools/; body not accessible this session]).

**Personas**
| Persona | Snapshot | What ReadWave must do |
|---|---|---|
| **Mia, 9, ADHD + dyslexia** | Creative; reads at ~grade-1 level; homework tears. | Short (8–12 min) lessons; clear next step; tap-to-answer when reading aloud is too hard; no timers. |
| **Leo, 12, dyslexic, stutters** | Hates "baby books"; avoids reading aloud. | Mature decodable stories (skateboarding, Minecraft-style worlds, science); **silent-read + tap check** mode; ASR never required. |
| **Ana, dyslexia tutor (OG-trained)** | 15 private students. | Map ReadWave lessons to her scope and sequence; assign between-session practice; see accuracy by phonics pattern. |
| **Mr. Patel, SENCO** | Secondary school; 40 students with reading needs. | Age-respectful intervention for 11–14; progress probes for EHCP reviews. |

**Needs & wants**
| Need | Evidence | How ReadWave addresses it |
|---|---|---|
| Explicit, cumulative phonics | Structured-literacy evidence [V2]; Lexia Strong ESSA [V] | Scope and sequence: phonemic awareness → GPCs → syllable types → morphology; mastery-gated |
| Age-respectful content | Nessy 6–11 [V]; Lumen P13 | Theme and story sets independent of decoding level |
| No punishment for slow reading | Vision; Lumen P8/P11 | No timers in lessons; fluency measured only in optional monthly probes |
| Read-aloud that works for different voices | ASR WER evidence [V] | ASR optional; tap/typed/choice fallback; human (tutor/parent) verification mode |
| Reading access now, not only later | Learning Ally/Speechify demand [V] | TTS on all texts; "read to me" for content reading |
| Dyslexia-friendly typography | BDA 2023 [V2] | BDA defaults + user controls |
| Fit with tutoring | Vision riskiest assumption | Tutor alignment map, homework assignment |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Evidence tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| **Nessy Reading & Spelling** | Nessy Learning | Widely used in UK/US homes and schools [V2] | **$126/yr or from $15.50/mo** (Sept 2026) [V] | n/a | Structured literacy, games, printable worksheets; BDA Quality Mark [V/V2] | Designed for 6–11; "more accurate for younger elementary ages" [V]; cartoonish [V2] | Dyslexia-aware design; busy game visuals [I] | E3 | [Nessy](https://www.nessy.com/en-us/product/nessy-reading-and-spelling-home), [Brighterly](https://brighterly.com/blog/best-reading-apps-for-kids/) |
| **Lexia Core5 Reading** | Lexia (Cambium) | Large US district footprint [M] | **≈$40/student (<250 students)**, less at scale [V] | n/a | Adaptive structured literacy PreK–5; teacher data [V] | School-only; older-student fit (Lexia PowerUp exists [M]) | Timed elements in some activities [M] | **E1** ("Strong", Evidence for ESSA) [V] | [Evidence for ESSA](https://www.evidenceforessa.org/program/lexia-core5-reading/), [Lexia](https://www.lexialearning.com/research/essa-evidence) |
| **Amira** | Amira Learning | 2 studies, 15,602 students [V] | School licence [M] | n/a | AI listens to oral reading, gives feedback, progress monitoring [V] | Public frustration in SFUSD (Sept 2026) [V headline]; ASR on child speech [I] | Voice-dependent core loop | **E1/E2** ("Moderate", ES +0.15; RCT ES +0.64 in n=178) [V] | [Evidence for ESSA](https://www.evidenceforessa.org/program/amira/) |
| **Microsoft Reading Coach** | Microsoft | Free; 81 languages [V] | **Free** [V] | n/a | AI-generated stories, pronunciation feedback, Immersive Reader supports [V] | School accounts for teacher features; ASR scoring [I] | Immersive Reader spacing, fonts, themes [V] | E3 [I] | [Microsoft](https://techcommunity.microsoft.com/blog/educationblog/reading-coach-the-ai-powered-fluency-practice-tool-is-now-generally-available-in/4291953) |
| **Learning Ally Audiobook Solution** | Learning Ally (nonprofit) | **75,000+ human-read titles; 24,000+ schools** [V] | $135/yr ($99 first year); fee waiver available [V] | n/a | Human-narrated audiobooks with text highlighting [V2] | Requires documentation of print disability [V] | Access tool, not instruction | E3 | [Learning Ally](https://learningally.org/solutions-for-home/home-school-resources-join) |
| **Speechify** | Speechify Inc. | **10M+ Play downloads**; 55M users claimed [V2] | **≈$139/yr, annual only** [V2] | 4.6–4.8★ iOS (varies by source) [V2] | TTS for any text; 2025 ADA Inclusivity [V2, catalog] | **Billing complaints**, trial conversions, charges after cancelling [V2] | Access tool | E4 | [roborhythms](https://www.roborhythms.com/speechify-review-2026/), [justuseapp](https://justuseapp.com/en/app/1209815023/speechify-audio-text-reader/reviews) |
| **Teach Your Monster to Read** | Usborne Foundation | **11M+ children; 100M plays; 1–2M children/month** [V] | Free web; app paid [V/V2] | n/a | Phonics game, playful journey [V] | Repetitive later levels [V2, catalog] | Playful, young | E3 | [TYM](https://www.teachyourmonster.org/monster-news/100-million-plays/) |
| **HOMER** | Begin | Editors' Choice design [V2, catalog] | ≈$7.99/mo [V2] | n/a | Early reading path, stories | Subscription cost [V2] | Young audience | E3 | catalog (raw) |

Also relevant: **Dyslexia Quest** (Nessy screener, from $25.50/yr; not diagnostic [V2]); **Reading Horizons** and **Barton Reading & Spelling** (OG-based programs with digital components [M]); **Ghotit** (writing support for dyslexic error patterns [V2]); **Apple Accessibility Reader** (free system reading mode [V2]).

**Feature matrix**
| Feature | Nessy | Lexia Core5 | Amira | MS Reading Coach | Learning Ally | Speechify | TYM | Our decision |
|---|---|---|---|---|---|---|---|---|
| Structured-literacy scope & sequence | ✓ | ✓ | ◐ | ◐ | ✗ | ✗ | ✓ (early) | **Parity** |
| Spelling/encoding practice | ✓ | ✓ | ◐ | ✗ | ✗ | ✗ | ◐ | **Parity** |
| Morphology (older learners) | ◐ | ◐ | ◐ | ✗ | ✗ | ✗ | ✗ | **Improve** |
| Mature themes at low decoding levels | ✗ | ◐ | ◐ | ✓ (topic choice) | ✓ (books) | ✓ | ✗ | **Differentiate** for decodables |
| Oral reading with ASR feedback | ✗ | ◐ [M] | ✓ | ✓ | ✗ | ✗ | ✗ | **Improve**: optional, speech-tolerant, never sole input |
| Tap/choice fallback for every read-aloud task | n/a | ✓ | ◐ | ◐ | n/a | n/a | ✓ | **Differentiate** (guaranteed) |
| Decodable text generation within word lists | ✗ | ✗ | ✗ | ◐ (free AI stories) | ✗ | ✗ | ✗ | **Differentiate**: constrained + human-reviewed |
| TTS on all text | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Parity** |
| BDA typography controls | ✓ | ◐ | ◐ | ✓ | ✓ | ✓ | ◐ | **Parity** |
| Tutor/teacher alignment and data | ◐ | ✓ | ✓ | ✓ | ◐ | ✗ | ◐ | **Improve**: tutor scope mapping |
| Timed fluency drills in the learning loop | ◐ [M] | ◐ [M] | ✓ | ◐ | ✗ | ✗ | ✗ | **Reject** in lessons; optional monthly probes only |
| Annual-only billing | ✗ | n/a | n/a | n/a | ✗ | ✓ [V2] | ✗ | **Reject** |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| R1 | **Structured-literacy path** | ≈150 lessons: phonemic awareness, GPCs, blending/segmenting, 6 syllable types, suffixes, morphology; mastery-gated with cumulative review | Structured literacy evidence [V2] | Parity | MVP | Must |
| R2 | **Placement check (non-diagnostic)** | 10-min adaptive check places the learner in the sequence; clearly "not a dyslexia test" | Avoid Dyslexia Quest-style false reassurance [V2] | Parity | MVP | Must |
| R3 | **Multimodal response tray** | Every item answerable by speaking, tapping tiles, typing, choosing or (for spelling) tapping letter tiles; switch and gaze supported | Lumen P7; ASR WER [V] | Differentiate | MVP | Must |
| R4 | **Speech-tolerant read-along** ★ | Optional ASR read-along with lenient scoring: accent/dialect/stutter-tolerant thresholds; a miscue is never "wrong" without a second signal; "I'll tap instead" always visible; no ASR scores shown to child | ASR limits [V] | Differentiate | MVP | Must |
| R5 | **Age-respectful decodable library** ★ | 120 decodable texts at launch across the sequence in 3 styles: young, middle, teen (sport, gaming, science, mystery, graphic-novel panels) | Nessy gap [V]; Lumen P13 | Differentiate | MVP | Must |
| R6 | **Constrained AI decodable generator (human-reviewed)** | Generates practice sentences/texts only from the learner's mastered GPC set + taught high-frequency words, around the learner's chosen interest; every generated text passes an automatic decodability checker and a human editor before entering the shared library | Vision AI role | Differentiate | MVP (library-side) | Should |
| R7 | **Gentle feedback and error analysis** | Feedback names the pattern ("This word has the /igh/ team"), shows it, lets the learner retry; errors feed review, not scores | Lumen P8 | Lumen | MVP | Must |
| R8 | **Spelling with phoneme-to-grapheme tiles** | Sound boxes + letter tiles (tap-to-place, no drag required) | Encoding practice | Parity | MVP | Must |
| R9 | **Read-to-me everywhere** | TTS with word highlighting on every text and instruction; rate control | Access; Learning Ally/Speechify parity | Parity | MVP | Must |
| R10 | **BDA typography + tint** | Font (sans-serif options incl. OpenDyslexic as a *preference*, not a claim), size, letter/word/line spacing, tint | BDA 2023 [V2]; fonts not superior [M] | Lumen | MVP | Must |
| R11 | **Tutor & parent view** | Accuracy by pattern, next lessons, "homework" assignment, tutor scope-alignment (map ReadWave lesson IDs to common OG/SL sequences) | Tutors are the channel | Improve | MVP | Must |
| R12 | **Monthly progress probe (optional, private)** | 1-min oral reading fluency probe at a chosen time, human-verifiable, shown only to adults unless the learner opts in; never timed in lessons | Evidence engine; P11 | Improve | MVP | Should |
| R13 | **My Needs + Sensory Dial** | Calm default; no background music | Lumen | Lumen | MVP | Must |
| R14 | Morphology & vocabulary track (10–14) | Prefixes, suffixes, roots with mature texts | Older-learner gap | Differentiate | V1 | Should |
| R15 | Reading access shelf | Import a school worksheet/photo → TTS + BDA view (OCR on device) | Access tool demand | Improve | V1 | Should |
| R16 | Co-reading cards | Parent prompts ("Ask: what might happen next?") after each text | Lumen P14 | Improve | V1 | Should |
| R17 | School class view + rostering | Clever/ClassLink; group by pattern | B2B | Parity | V2 | Should |
| R18 | Writing support | Phonetic-spelling-aware suggestions (Ghotit-like) for teens | Ghotit [V2] | Improve | V2 | Could |

★ Signature features: **Speech-tolerant read-along with guaranteed tap fallback (R4)** and **age-respectful decodables (R5)**. The MVP has 13 features.

## 5. Core experience & key user flows
**Core loop:** open → "Today's lesson" (a Now/Next/Done strip: warm-up → new pattern → practice → decodable text → done) → 8–15 min → designed ending ("You practised the /ai/ team. Next time: /ay/.") with an offline suggestion ("Find 3 things with 'ai' at home").

**Flow 1: Onboarding (≤5 min)**
1. The adult sets the age band, theme (young, middle or teen), interests and input preferences. The Calm dial is preset.
2. The placement check can be split across sessions and stops on request.
3. The first lesson starts on a pattern the learner already knows (a success start).

**Flow 2: Core lesson (Leo)**
1. Warm-up: 5 review words using tile tap.
2. New pattern: the "oa" team is introduced with audio, mouth-picture (optional) and example words.
3. Practice: read 8 words. Leo chooses "read silently, then tap the picture" instead of reading aloud.
4. Decodable: "The Goal" (football story, teen style). TTS is available for non-decodable words, which are marked.
5. End screen; the tutor sees accuracy on "oa".

**Flow 3: Tutor view**
1. Ana links her student with a code from the parent (consented).
2. She maps her current lesson ("Barton Level 3, Lesson 5" or her own sequence) to ReadWave lesson IDs.
3. She assigns 3 short practices this week and sees error patterns afterwards.

**Flow 4: My Needs:** typography, tint, TTS voice/rate, ASR on/off, input modes, Dial, session length.

**Flow 5: Billing:** Fair-billing charter; monthly and annual plans; the access features (TTS, BDA view) stay free.

**Information architecture:** Today · Library · Practice (review) · My Needs. Adult: Progress · Assign · Settings.

**Session design:** Default 12 min (adjustable 5–25). Transition warnings ("1 more text, then done"). No streaks; a "weekly reading goal" can be paused.

## 6. Inclusive, accessible & sensory design spec
**Sensory Dial**
| Level | Motion | Sound | Color | Feedback |
|---|---|---|---|---|
| **Calm (default)** | Word highlight only | TTS/narration only; no music | Cream background, dark grey text | "✓ Right" + a short phrase; incorrect answers show the pattern, never a buzzer |
| **Balanced** | Gentle tile moves | Soft effects | Moderate | Short celebration at lesson end |
| **Lively** | Animated story panels (no flashing) | Music outside lessons | Vivid | Longer, skippable celebration |

**Input modes per task**
| Task | Tap | Voice | Keyboard | Switch | Eye gaze | AAC |
|---|---|---|---|---|---|---|
| Identify sound/word | ✓ | ✓ (optional) | ✓ | ✓ | ✓ | ✓ (choose symbol/word) |
| Read word/sentence | ✓ (tap matching picture/meaning, or self-check "I read it") | ✓ | ✗ | ✓ | ✓ | ✓ |
| Spell | ✓ tiles | ◐ (letter names) | ✓ | ✓ (tile scan) | ✓ | ◐ |
| Decodable text | ✓ comprehension choice | ✓ read-along | ✓ | ✓ | ✓ | ✓ |

**Read-along ASR rules**
- **Wait time:** Default 10 s, adjustable up to "no limit", with no auto-advance.
- **Scoring thresholds:** Lenient by default. Repetitions and stutters are not errors. Dialect-variant pronunciations are accepted per a dialect table [I].
- **Low confidence:** If ASR confidence is low, the item goes to a "check" state and the learner is asked to tap. The learner never sees "wrong" based on ASR alone.
- **Human verification:** Adults can listen to recordings (if recording consent is on) and override.

**Targets and gestures:** Tiles ≥2 cm for 5–7 and ≥1.5 cm for 8–14. Drag is never required (tap tile → tap box).

**Typography (BDA 2023):** 18–22 px body, letter spacing ≈0.35 em average, word spacing ≥3.5× letter spacing, line height 1.5, left-aligned, 60–70 characters, no italics or caps for emphasis, tint options [V2]. WCAG 1.4.12 override is supported.

**Audio:** Separate TTS, effects and music channels. Captions for all narration. Visual highlighting mirrors TTS.

**Age-respectful themes:** Young (illustrated), Middle (graphic), Teen (photo/graphic-novel), all independent of decoding level.

**Lumen principles: acceptance criteria**
| P | Criterion |
|---|---|
| P1 | Calm default; Reduce Motion honored |
| P2 | No sound-only cues; captions; no buzzers |
| P3 | Same lesson structure every day (Now/Next/Done) |
| P4 | No drag required; tile targets as specified |
| P5 | Instructions ≤10 words, read aloud |
| P6 | BDA defaults; spacing override |
| P7 | Every read-aloud item has ≥2 non-voice alternatives |
| P8 | No lives, hearts or time pressure; errors → review |
| P9 | Designed lesson ending; no autoplay |
| P10 | Picture sign-in |
| P11 | No lesson timers; fluency probes are opt-in |
| P12 | My Needs portable |
| P13 | 3 themes independent of level |
| P14 | Co-reading cards; tutor view |
| P15 | Mastery map, no streak punishment |
| P16 | Dyslexia framed as a difference with strengths; no "fix" language; ND board and dyslexic adults review |
| P17 | "Built on structured literacy"; multisensory not claimed as the active ingredient |
| P18 | Audio recordings off by default; on-device ASR where feasible |

**Target Lumen score:** ≥22/24.

## 7. AI specification & guardrails
**What AI does**
1. **ASR for read-along** (optional): on-device child-tuned model preferred [E]; cloud fallback with zero retention.
2. **Decodable text generation:** An LLM generates inside a **closed lexicon**: mastered GPCs + taught high-frequency words + story-specific proper nouns (marked). A deterministic decodability checker rejects any non-conforming word. A **human literacy editor** reviews every text before it enters the library; generation is library-side, not live to the child in the MVP.
3. **Adaptive review:** a spaced-repetition scheduler (not an LLM).

**What AI does not do:** No diagnosis of dyslexia. No emotion inference from voice. No chat tutor persona. No timed scoring shown to the child. No live generated text to children without review (V1 may allow live generation for tutor-approved interests after evals).

**Evaluation plan**
- **ASR:** WER and miscue-detection precision/recall by speaker group (age, dialect, speech-sound disorder, stutter) on consented samples, in the WP4 feasibility spike. **Ship threshold [E]:** false-"wrong" rate ≤3% across all groups, with no group more than 2× the best.
- **Generator:** 100% decodability (automated), ≥95% editor acceptance, 0 content-policy violations in red-teaming (violence, stereotypes).
- **Human sampling:** 10% of new texts double-reviewed by a dyslexic adult reviewer.

**Cost [E]:** On-device ASR ≈$0; cloud ASR ≈$0.006/min; generation ≈$0.01/text + editor time (the main cost).

## 8. Data, privacy & compliance
| Data | Why | Retention | Where |
|---|---|---|---|
| Responses, accuracy by pattern | Adaptive path, tutor view | 24 months [E] | Cloud |
| Voice recordings | Optional human verification | **Off by default**; if on, 30 days | Device; cloud only with consent |
| ASR transcripts | Scoring | Session only unless recording consent | Device |
| Probe results | Progress | 24 months | Cloud |

- **COPPA 2025:** Voice recordings are personal information, so they need separate consent and are not used for training without separate opt-in.
- **FERPA/SOPIPA:** school licences.
- **IDEA / 504:** probes support IEP progress monitoring. ReadWave is not a diagnostic evaluation.
- **FTC:** avoid "cures dyslexia", "rewires the brain" or "proven" claims until E1/E2.
- **FDA:** not applicable (education).
- **EU AI Act:** adaptive placement that "assesses appropriate level" may fall within Annex III education high-risk (deadline 2 Dec 2027 [V2]). Plan human oversight: tutors and parents can override placement.

## 9. Monetization & go-to-market
| Tier | Price [E] | Benchmark |
|---|---|---|
| ReadWave home | $9.99/mo or $79/yr (siblings +$2/mo) | Nessy $126/yr / $15.50/mo [V]; HOMER ≈$7.99/mo [V2] |
| Family plan | ≈$19/mo, all apps | — |
| Tutor licence | $19/mo, up to 20 students | — |
| School | $20–35/student/yr [E] | Lexia ≈$40/student [V] |
| Free | Read-to-me + BDA reading view for any text | Reading Coach free [V]; Accessibility Reader free [V2] |

- **Channels:** dyslexia tutors (OG/SL practitioners), IDA/BDA branch events, ESA marketplaces, SENCOs; target the **BDA Quality Mark**, which Nessy holds [V2].
- **ASO:** dyslexia app, phonics for older kids, structured literacy, Orton-Gillingham app, decodable books.
- **Launch:** US and UK (UK phonics terminology variant: "digraph", "split digraph", Letters and Sounds alignment [M]).

## 10. Success metrics
- **North star:** Weekly minutes of accurate decoding practice per active learner.
- **Input metrics:** Lessons completed per week (≥3); patterns mastered per month; tutor-linked learners (%); decodables read.
- **Guardrails:**
  - Sensory Comfort ≥4/5
  - Learner "reading felt OK" ≥3.5/5
  - ASR false-"wrong" ≤3%
  - 0 billing complaints
  - 0 unreviewed generated texts shipped
- **Outcomes:** Monthly ORF probes (words correct per minute, human-verified); nonsense-word decoding; spelling inventory. **Evidence plan:** E3 → pre-registered 12-week pilot with a university reading clinic (E2) → an RCT only if E2 is positive.
- **Retention [E]:** D30 35%, 12-week completion ≥50% of starters.

## 11. Validation plan
| # | Assumption | Experiment | Sample | Success | Kill |
|---|---|---|---|---|---|
| 1 | Families/schools buy alongside existing OG tutoring | Tutor and SENCO interviews; tutor LOIs | 15 (tutors + SENCOs) | ≥60% would assign between-session practice; ≥5 tutor LOIs | <30% → pivot to tutor-only tool |
| 2 | Paper concierge pilot shows fluency movement | 4-week paper-based concierge: printed lessons + teen decodables, tutor-delivered | 12 learners | Median ORF gain ≥ expected growth [E]; learner enjoyment ≥3.5/5 | No engagement → rethink format |
| 3 | Teen decodables feel respectful | Card sort + read-through with 11–14s | 10 teens | ≥80% "not babyish" | — |
| 4 | ASR is tolerable | WoZ read-along (human listener simulating lenient ASR) vs. tap-only | 15 learners incl. 4 with speech differences | Frustration ≤1 event per session; ≥50% choose voice sometimes | High frustration → ship tap-first, ASR later |
| 5 | Sensory A/B | Lumen protocol | 20 | Comfort +1 for ND | — |

**Mapping:** WP2 (tutor interviews), WP4 (concierge, WoZ, ASR spike), WP5 (tutor/ESA channel).

## 12. Build handoff
**Epic A: Lesson engine**
- *Given* a learner at lesson 40, *when* they miss the same pattern in 3 of the last 5 items, *then* the engine schedules review and does not advance, and no penalty is displayed.

**Epic B: Multimodal responses**
- *Given* any read-aloud item, *then* a visible "tap instead" option exists and completes the item without voice.
- *Given* ASR confidence below threshold, *then* the item enters the "check" state instead of marking an error.

**Epic C: Decodables**
- *Given* a generated text, *when* the decodability checker finds a word outside the learner's set (and not marked as a taught exception), *then* the text is rejected before editor review.
- *Given* a learner's theme is Teen, *then* all library texts shown use teen illustrations or photos at their level.

**Epic D: Tutor view.** *Given* consented linking, *then* the tutor sees accuracy by pattern and can assign lessons; the parent can revoke access in 1 tap.

**Non-functional requirements:** ASR on device on 2021+ iPads and mid-range Android [E]; offline lessons; WCAG 2.2 AA; EN-US, EN-GB; Spanish in V2 (with its own orthography scope and sequence).

**QA focus**
- **AT matrix:** VoiceOver (lesson navigation, TTS conflict handling), TalkBack, Switch Control tile scanning, Eye Tracking, Dynamic Type XXL (no truncation in decodables), text-spacing override, Reduce Motion.
- **Sensory A/B.**
- **ASR fairness** by speaker group.
- **AI:** decodability 100%, content red-team.
- **COPPA:** voice consent.
- **Billing:** monthly option present, cancel in-app.

**Platform dependencies:** Lumen (multimodal answer tray, typography tokens), Circle (tutor sharing), ASR service (shared with Lanternling), evidence engine (probes, pre-registration).

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Content cost (150 lessons, 120+ texts, 3 themes) | High | High | Constrained generation + editors; phased themes |
| ASR harms confidence | Med | High | Optional, lenient, never sole signal; tap-first |
| Free competitors (Reading Coach, TYM) | High | Med | Dyslexia-specific sequence, teen decodables, tutor fit |
| Over-claiming multisensory | Low | Med | Claims register; wording reviewed |
| UK/US phonics terminology split | Med | Low | Locale variants |

**Open questions:** License an existing scope and sequence vs. author our own? Seek BDA Quality Mark at MVP or V1? Include Spanish structured literacy (different orthography) in Year 2?

## 14. Sources
- [V] Nessy pricing: https://www.nessy.com/en-us/product/nessy-reading-and-spelling-home ; age fit: https://brighterly.com/blog/best-reading-apps-for-kids/
- [V] Lexia Core5 ESSA and price: https://www.evidenceforessa.org/program/lexia-core5-reading/ ; https://www.lexialearning.com/research/essa-evidence
- [V] Amira evidence: https://www.evidenceforessa.org/program/amira/ ; [V headline only] SFUSD coverage: https://sfstandard.com/pacific-standard-time/2026/09/25/pst-sf-amira-ai-in-schools/
- [V] Microsoft Reading Coach: https://techcommunity.microsoft.com/blog/educationblog/reading-coach-the-ai-powered-fluency-practice-tool-is-now-generally-available-in/4291953
- [V] Learning Ally: https://learningally.org/solutions-for-home/home-school-resources-join
- [V2] Speechify: https://www.roborhythms.com/speechify-review-2026/ ; https://justuseapp.com/en/app/1209815023/speechify-audio-text-reader/reviews
- [V] Teach Your Monster: https://www.teachyourmonster.org/monster-news/100-million-plays/
- [V] Child ASR: https://pubs.asha.org/doi/10.1044/2021_JSLHR-21-00096 ; [V2] https://arxiv.org/pdf/2406.07060
- [V2] Stevens 2021 OG meta-analysis, BDA Style Guide 2023, Dyslexia Quest, Ghotit, HOMER: studio raw file 04 and app catalog
- [M] Lexia PowerUp, Barton, Reading Horizons, UK phonics terminology, dyslexia-font studies: verify in WP1.

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (shares EN-04 Reading Continuum) |
| **Ships in** | Wavelength app (S7) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 83/100 [I] |
| **Consumes engines** | EN-04, EN-09 |
| **Studio features used** | SX-20, SX-27 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = R1, R3, R4, R5, R8, R9.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| RW-E1 | **IEP accommodations suggestions** | A list of reading-access supports to discuss with the IEP team (text-to-speech, extended time). Not a determination (SX-27). |
| RW-E2 | **Structured-literacy tutor channel** | Certified tutors use ReadWave as a between-session practice tool, licensed through the Pro Console. |

### 15.3 New validation question
Tutor/SENCO interviews (n=15) plus a 4-week paper pilot measuring fluency probes.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 5 | 4 | 5 | 4 | 4 | 3 | 3 | 4 |

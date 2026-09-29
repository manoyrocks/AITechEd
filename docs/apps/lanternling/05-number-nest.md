# Number Nest: App Strategy & Product Specification

> **Venture:** Lanternling · **App #:** 5/7 · **Ages:** 3–7 (independent play with co-play prompts) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/01-lanternling-early-years.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given; mostly search snippets) · [V2] secondary or vendor source · [M] from memory · [E] estimate · [I] inference
> **Research caveat:** the session's web-search budget ran out during this app's research and store pages were proxy-blocked. Moose Math, Montessori Numbers (Edoki) and Osmo figures are [M] and must be verified in Discovery WP1.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A calm digital Montessori shelf for numbers: bead bars, ten-frames and a balance scale that gently show a child when amounts match, so number sense grows through hands-on play, not timed drills. |
| **Primary user / buyer** | Children 3–7 (user); parents (buyer); pre-K/K and Montessori-inspired teachers (B2B2C). |
| **Core job-to-be-done** | "When my child plays on the tablet, I want them to really understand numbers, not race through drills for stars, so they start school confident and I can see what they've learned." |
| **Category on the stores** | Apple: Kids › Ages 5 & Under / 6–8 (Education). Google Play: Families › Educational. |
| **Top competitors** | Khan Academy Kids (10M+ Play, free) · SplashLearn (20M+ downloads) · DragonBox/Kahoot! Numbers (4.7★) · Todo Math (XPRIZE co-winner) · Moose Math (Khan/Duck Duck Moose) [M] · Montessori Numbers (Edoki) [M] · Osmo Numbers [M] |
| **Our wedge** | 1. **Self-correcting materials** (the Montessori ingredient the 2025 PNAS RCT supports), not right/wrong drills. 2. **Tap-to-place everywhere**: every manipulative works without dragging (WCAG 2.5.7), which most math apps ignore. 3. **No timers, no stars economy**, with calm feedback and a 30-second "what they understand" summary for parents. |
| **Business model** | In the Lanternling Family plan (≈$9.99/mo or $69/yr, 7 apps, 3 children). Free: the first shelf (counting 1–5, subitizing, compare). Classroom licence (V1). |
| **North-star metric** | **Weekly concepts mastered per active child**, via self-correcting tasks completed without hints on two separate days. |
| **MVP candidate?** | **Year 2** in the vision's sequence (not in the Year-1 trio); low AI and content risk make it a fast follower. |

## 2. Problem & users

**Problem statement.**
- **Early math apps lean on drills, timers and rewards.** SplashLearn, Prodigy-style and many preschool apps use stars, coins and speed [V/M] ([Research paper §6](../../01-research-paper.md)). Timers exclude slower processors, dyslexic and motor-impaired children [V].
- **Number sense needs concrete manipulation.** The 2025 national Montessori lottery RCT (Lillard et al., *PNAS*, n=588) found higher reading, executive function, memory and social understanding by the end of kindergarten, with math positive in most models, at lower cost per child [V] ([raw 04 §B2](../../../research/raw/04-neurodivergent-and-inclusive-ux.md); [PNAS](https://www.pnas.org/doi/10.1073/pnas.2506130122)). The supported ingredients are **learner choice, concrete manipulation, self-correcting materials and uninterrupted work cycles**.
- **Early math knowledge at school entry is among the strongest predictors of later achievement** (Duncan et al. 2007) [M].
- **Drag-based manipulatives fail young hands.** 3-year-olds succeed on touch tasks ~73% of the time; drag accuracy correlates with visuospatial and fine-motor skills [V] (Vatavu 2015 via raw 04). Many math manipulative apps are drag-only [I].
- **Free options are strong** (Khan Kids, Moose Math) [V/M], so we must win on design quality and inclusion, not content volume.

**Personas.**

| Persona | Snapshot | Needs |
|---|---|---|
| **Zoe, 5, and Andre** | Counts to 20 by rote; unsure what "7" means. | Real quantity understanding; Andre wants a quick view of progress. |
| **Ellie, 6, dyspraxia (DCD)** | Struggles with drag and precise taps; gets upset by timers. | Tap-to-place; big targets; no speed. |
| **Sam, 4, autistic, loves patterns and trains** | Predictability; dislikes sudden sounds. | Calm, repeatable materials; train-themed counting set; no surprise rewards. |
| **Jonah, 7, low vision** | Uses zoom and VoiceOver. | Materials described aloud ("3 beads in the bar"); high-contrast beads; haptic feedback. |
| **Ms. Alvarez, Montessori-inspired pre-K teacher** | Uses physical beads and ten-frames. | Digital materials that match classroom materials; printable follow-ups; class view. |

**Needs & wants.**

| Need | Evidence | Response |
|---|---|---|
| Understanding over speed | Timer barriers [V]; Montessori RCT [V] | Self-correcting materials; no timers |
| Usable by small or impaired hands | Vatavu [V]; WCAG 2.5.7 [V] | Tap-to-select → tap-to-place; ≥2 cm targets |
| Parent can see learning | Research paper need #7 [V] | Concept-level summary ("understands 5 = 3 + 2") |
| Calm | Parent VoC [V] | Calm/Balanced defaults; quiet feedback |
| Fits classroom practice | Montessori materials [V] | Bead bars, ten-frames, number rods, scale |
| Honest pricing | Category billing anger [V] | Free first shelf; fair billing |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Khan Academy Kids** | Khan Academy | 10M+ Play; ~340K/30 days [V] | Free [V] | 4.7 Play; ≈4.8 iOS [V] | Free, calm, broad (math incl.) [V] | Outgrown ~6–7; "one more" pull [V] | Narrated; no timers; library text not enlargeable [V] | [raw 01](../../../research/raw/01-google-play-top30.md) · [raw 02](../../../research/raw/02-apple-app-store-top30.md) |
| **SplashLearn** | StudyPad | 20M+ downloads; "60M kids", "1 in 3 US schools" (vendor) [V2] | 2 free activities/day; from $7.49/mo billed annually [V] | 4.5 iOS (32K) [V] | Curriculum-aligned PreK–5 math & reading; school use [V] | Daily free limit; rewards focus [M] | Game rewards; moderate sensory [M] | [App Store](https://apps.apple.com/us/app/splashlearn-kids-learning-app/id672658828) · [Sensor Tower](https://app.sensortower.com/overview/672658828?country=US) |
| **Kahoot! Numbers by DragonBox** | Kahoot! (DragonBox) | Not published [M] | Free download + Kahoot! Kids subscription [V] | 4.7 iOS (3.3K) [V] | "Nooms" you stack, slice, combine: embodied number sense [V] | Subscription bundled with Kahoot! [M] | Heavy drag/slice gestures [I] | [App Store](https://apps.apple.com/us/app/kahoot-numbers-by-dragonbox/id1529174508) · [Common Sense Ed](https://www.commonsense.org/education/reviews/kahoot-numbers-by-dragonbox) |
| **Todo Math** | Enuma | XPRIZE co-winner ($15M Global Learning XPRIZE) [V] | $69.99–99.99/yr; 2-yr $119.99 [V] | 4.7 iOS (1.1K); 4.0 Play (4.2K) [V] | 2,000+ activities; 8 languages; **left-handed mode, dyslexic font, help button** [V] | Price [I] | The best accessibility in the category [V] | [App Store](https://apps.apple.com/us/app/todo-math/id666465255) · [site](https://www.todomath.com/) |
| **Moose Math** | Duck Duck Moose (Khan Academy) | Not verified [M] | Free [M] | High 4s [M] | Free, playful counting/shape games [M] | Small scope [M] | Moderate sensory [M] | [M] |
| **Montessori Numbers** | Edoki Academy | Not verified [M] | Paid ≈$5 [M] | ~4.5 [M] | Montessori-faithful materials [M] | Dated; drag-based [M] | Drag-heavy [M] | [M] |
| **Osmo Numbers** | Tangible Play (Byju's) | Byju's-owned; "hollowed out" after 2019 $120M acquisition [M via raw 05] | Hardware kit + app [M] | n/a | Tangible tiles with camera [M] | Company instability; camera-only input [M/V] | Camera-first excludes some users [I] | [raw 05](../../../research/raw/05-market-and-trends.md) |

*Marbleverse (Marbles) was named in the brief; not verified this session [M].*

**Takeaways [I].** Todo Math proves accessibility-conscious math can win awards; DragonBox proves embodied number-as-object design delights; Khan Kids proves "free and calm" wins parents' default trust. **No one combines Montessori self-correction, full tap-to-place, and a reward-free, timer-free loop.**

**Feature matrix.**

| Feature | Khan Kids | SplashLearn | DragonBox | Todo Math | Moose Math [M] | Montessori Numbers [M] | Osmo [M] | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Concrete manipulatives | partial | partial | ✓ | partial | partial | ✓ | ✓ (physical) | **Parity** |
| Self-correcting feedback (material shows mismatch) | ✗ | ✗ | partial | ✗ | ✗ | partial | ✗ | **Differentiate** |
| Open "many ways" challenges | ✗ | ✗ | partial | ✗ | ✗ | ✗ | partial | **Differentiate** |
| Tap alternative to every drag | partial | partial | ✗ | partial | ✗ | ✗ | n/a | **Differentiate** |
| Timers / speed rounds | ✗ | partial | ✗ | partial | ✗ | ✗ | partial | **Reject** |
| Star/coin economies | ✓ | ✓ | partial | ✓ | ✓ | ✗ | partial | **Reject** |
| Dyslexic font / left-hand mode | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | **Parity with Todo**, via My Needs |
| Multilingual | partial | partial | ✓ | ✓ (8) | ✗ | ✓ | partial | **Parity** (EN/ES MVP) |
| Parent concept-level report | partial | ✓ | ✗ | ✓ | ✗ | ✗ | partial | **Improve** |
| Classroom mode | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | **Parity** (V1) |
| Camera/tangible input | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Reject at MVP** (camera-only excludes; revisit as an *extra* mode) |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| NN-01 | **The Shelf (child choice)** ★ | A calm shelf of 4–6 materials the child can choose from (Montessori "work" choice); adult can pin a suggestion. | Montessori learner choice [V] | Differentiate | MVP | Must |
| NN-02 | **Self-correcting materials** ★ | Balance scale tips when amounts differ; ten-frame shows empty slots; number rods don't line up if wrong. Child notices and fixes; no "wrong" signal. | Montessori self-correction [V] | Differentiate | MVP | Must |
| NN-03 | **Tap-to-place interaction model** ★ | Every manipulation = tap object (it lifts, glows, is announced) → tap destination. Drag optional. "Add one" / "take one" buttons for counting materials. | WCAG 2.5.7; Vatavu [V]; Ellie persona | Lumen / Differentiate | MVP | Must |
| NN-04 | **Counting & cardinality set** | Counting beads 1–10, one-to-one tapping with spoken count, "how many?" cardinality check. | Early math foundations [M] | Parity | MVP | Must |
| NN-05 | **Subitizing cards** | Dot patterns (dice, ten-frame, fingers) shown untimed; child taps the matching numeral or quantity. | Subitizing is a core early skill [M] | Parity | MVP | Must |
| NN-06 | **Compare with the scale** | More/less/same by balancing sets; language modelled ("5 is more than 3"). | Self-correction [V] | Differentiate | MVP | Must |
| NN-07 | **Make 5/10 many ways** | Open composition: fill a ten-frame with two colours; the app collects every different way the child finds. | Part-whole thinking [M]; vision card | Differentiate | MVP | Must |
| NN-08 | **Hint ladder in words and pictures** | Wait → spoken prompt ("Look at the scale. Which side is lower?") → visual cue (highlight) → worked example; never gives the answer outright first. | Lumen §5 Socratic; P8 | Lumen | MVP | Must |
| NN-09 | **Mastery engine** | Tracks concepts (not items); advances when a task is solved without hints on 2 separate days; spaced review. | Mastery learning [M] | Parity | MVP | Must |
| NN-10 | **Nest (progress visual)** | A nest gathers one twig per concept mastered; nothing is ever lost. | Lumen P15 | Lumen | MVP | Must |
| NN-11 | **Co-play Kitchen Math cards** | After each session: "Count 5 spoons with me. Which pile has more?" | JME; vision real-world first | Differentiate | MVP | Must |
| NN-12 | **Parent concept summary** | "Zoe understands that 5 can be 3+2 and 4+1. Next: numbers to 10." | Research paper need #7 | Improve | MVP | Must |
| NN-13 | **Accessibility settings** | Described materials for screen readers, high-contrast beads, haptic ticks per count, left-hand layout, dyslexia-friendly numerals, switch scanning of objects. | Todo Math benchmark [V]; Jonah persona | Lumen | MVP | Must |
| NN-14 | **Number line & teen numbers (bead bars)** | Golden-bead style tens and ones; number line jumps by tap. | Place value foundations [M] | Parity | V1 | Should |
| NN-15 | **Shapes & measurement** | Tangram-style shape composing (tap-rotate), length comparison with rods. | Early geometry [M] | Parity | V1 | Should |
| NN-16 | **Classroom mode** | Class code, shared tablet profiles with picture login, teacher concept heatmap, printable material cards. | Ms. Alvarez persona; competitors' school use [V] | Parity | V1 | Should |
| NN-17 | **Addition/subtraction stories (5–7)** | Story problems acted out with materials; spoken and tapped answers. | K–1 standards [M] | Parity | V1 | Should |
| NN-18 | **Physical-digital kit (optional)** | Printable/cheap ten-frame mat that mirrors the app; no camera needed. | Osmo appeal without camera [I] | Differentiate | V2 | Could |

★ **Signature features:** The Shelf (NN-01), Self-correcting materials (NN-02), Tap-to-place (NN-03). **MVP = NN-01 to NN-13 (13 features).**

## 5. Core experience & key user flows

**Core loop.** Open → Shelf (choose a material) → work cycle (self-correct, explore) → optional challenge → nest twig if mastered → transition warning → Kitchen Math card → done.

**Flow 1: Onboarding (≤4 min).** Price/privacy → child age, languages → input preferences (tap/drag, left-hand) → 3-min playful placement (count beads, compare on scale) → first Shelf.

**Flow 2: Core session.**
1. Shelf shows ten-frame, scale, beads, dot cards (one pinned by parent).
2. Child taps "scale". Left pan has 5 apples; right is empty. Prompt: "Make it balance."
3. Child taps an apple in the basket (it lifts, "one"), taps the right pan (it lands, "one"). Continues. At 4 the pan stays higher; child adds one more; scale levels with a soft "clunk" and "5 and 5, same!"
4. After 3 works (~12 min default), "One more work, then we tidy up." Tidy-up animation (materials return to shelf, the Montessori closing routine).
5. Kitchen Math card for the adult; goodbye.

**Flow 3: Parent view.** Concepts mastered / practising; one sentence of meaning; a Kitchen Math tip; material usage.

**Flow 4: My Needs.** Input (tap/drag), hand, switch scanning, haptics, described mode, Sensory Dial, session length, number language(s).

**Flow 5: Billing.** Family Hub standard; the first shelf is always free.

**Information architecture.** Child: Shelf → Material workspace → Tidy-up. Parent (gated): Summary · Concepts · Settings · Family. Fixed buttons: Help (hint), Tidy up (end), Undo.

**Session design.** Default 12 min (range 8–20); "work cycle" not interrupted by pop-ups; warning at T-2 min; tidy-up ending.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial defaults.** Calm for 3–4; Balanced for 5–7.

| Level | Number Nest behaviour |
|---|---|
| Calm | Materials move with slow easing; one soft sound per placement (wood click); no music; muted palette (natural wood, soft colours) |
| Balanced | Counting voice + placement sound; scale "clunk"; brief glow when balanced |
| Lively | Short celebratory sparkle (skippable, no flashing) when a "many ways" set is complete |

**Input modes.** Tap-then-tap (default), drag (optional), switch scanning (objects → destinations), keyboard (arrows + enter), Voice Control ("pick apple", "put right pan"), voice answers for "how many?" (with tap numerals always shown). Answer tray per Lumen §3.5.

**Targets & gestures.** Objects ≥2 cm (3–4: ≥2.5 cm); destinations ≥3 cm; spacing ≥0.5 cm; drag tolerance generous (snap within 1.5 cm) when drag is used; no pinch/rotate required (rotation via a tap button in V1 shapes).

**Reading & typography.** Numerals in a clear, non-decorative face (distinguishable 1/7, 6/9 with underline cue on 6 and 9 in cards); instructions spoken; ≤6 words on screen; dyslexia settings from My Needs.

**Audio.** Voice, counting, effects on separate sliders; haptic tick per count (supports Deaf/HoH and blind children); every sound has a visual twin.

**Screen reader.** Each material exposes counts and states ("Left pan: 5 apples. Right pan: 4 apples. Left is lower.") so a blind child can do the task by VoiceOver with haptics.

**Age-respectful themes.** "Wooden" (Montessori natural) and "Picture" (illustrated) themes.

**Lumen principles.**

| P# | Acceptance criterion |
|---|---|
| P1 | Reduce Motion → objects move instantly with a fade; Dial 1 tap away |
| P2 | Haptic tick + visual counter for each spoken count |
| P3 | Same workspace layout per material; tidy-up routine always ends sessions |
| P4 | 100% tasks via tap-then-tap; targets ≥2 cm |
| P5 | Spoken instructions; ≤6 words on screen |
| P6 | Numerals and text meet legibility defaults |
| P7 | Tap, drag, switch, keyboard, voice |
| P8 | Self-correction only; no red Xs; undo always |
| P9 | Tidy-up ending; no autoplay |
| P10 | Picture login for classroom profiles |
| P11 | No timers anywhere |
| P12 | Input, hand, haptics portable |
| P13 | Two themes |
| P14 | First work ≤4 min |
| P15 | Nest twigs for mastery; no currency |
| P16 | Diverse hands in finger-count images (incl. limb differences) |
| P17 | "Inspired by Montessori materials"; no efficacy claim until tested |
| P18 | No voice stored; minimal data |

**Target Lumen audit score:** 23/24.

## 7. AI specification & guardrails

**What AI does.** Mastery-based sequencing (knowledge tracing over concepts); choice of next suggested material on the shelf; hint ladder selection based on the child's error pattern (e.g., double-counting → highlight one-to-one). Optional on-device speech recognition for number words 0–20 (a tiny, constrained vocabulary; tap numerals always shown).

**What AI does not do.** No generative content, no chatbot, no character that talks as a friend, no emotion inference, no time-on-task optimisation.

**Pedagogical policy.** Concrete → pictorial → abstract progression; self-correction first, hints second, worked examples third; mastery requires no-hint success on two separate days; spaced review; child choice preserved (the algorithm *suggests*, the child chooses).

**Safety.** All items and hints human-authored and reviewed by an early-math specialist; solution checking is deterministic (no LLM math). Number-word ASR evaluated per speaker group, but never required.

**Evaluation plan.** Sequencing: simulated learners + pilot comparison to fixed order; hint efficacy: % of hints followed by correct no-hint attempt; number-word ASR: per-group false-reject ≤5% [E] (easy vocabulary).

**Cost and latency [E].** All on-device; object response ≤100 ms.

## 8. Data, privacy & compliance
**Data inventory.** Child profile (nickname, age); concept mastery and attempt events (input mode, hint level); no audio stored; no camera. Retention: life of account; export; 30-day deletion.
**Regimes.** COPPA 2025; FERPA/SOPIPA for classroom mode (DPA, no ads); UK AADC; state AADCs; Apple Kids/Google Families; EU AI Act (learning-outcome evaluation → design for human oversight before Dec 2027).
**Consent.** Parent consent; separate optional mic consent for number words; teacher-mediated consent for classrooms per school policy.

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Free | $0 | Shelf 1 (counting 1–5, subitizing, compare), all accessibility |
| Family plan | ≈$9.99/mo or $69/yr (7 apps) | All shelves, Kitchen Math library, summaries |
| Classroom | $150–250/classroom/yr [E] | Teacher view, shared devices, printables |

Benchmarks: Todo Math $69.99–99.99/yr, SplashLearn from $7.49/mo annual, Khan Kids and Moose Math free, Kahoot! Kids subscription [V/M]. Standalone value ≈ $40–50/yr [I]; bundle is the path.

**Channels.** Montessori and homeschool communities; pre-K classrooms; OT/SLP for motor-impaired children (tap-to-place is rare) [I]; libraries.

**ASO.** "Montessori math app", "number sense preschool", "counting app no timer", "math app for dyspraxia". Accessibility Nutrition Label: VoiceOver, Voice Control, Larger Text, Reduced Motion, Differentiate Without Color, Sufficient Contrast.

**Launch.** US/UK/Canada/Australia (EN), US Hispanic (ES).

## 10. Success metrics
- **North-star:** weekly concepts mastered per active child (target 1–2 [E]).
- **Inputs:** works completed per session; % works chosen by child vs. suggested; "many ways" discoveries; Kitchen Math cards marked done.
- **Guardrails:** persistence (time on task before voluntary stop) stable or rising without rewards; frustration events ≤1/session; Sensory Comfort ≥4/5; hint-to-answer ratio not rising; zero billing complaints.
- **Outcomes:** pre/post probes (cardinality, subitizing, comparison, composition of 5/10) in a 6–8-week pilot; E4 → E3 → E2 plan; potential academic Montessori partner.
- **Retention:** D30 30% [E].

## 11. Validation plan

**Riskiest assumptions.**
1. Self-correcting play without scores motivates 4–7s (vision).
2. Tap-to-place feels natural (not slower/annoying) to typically developing children.
3. Parents value "understanding" summaries over scores and stars.
4. Differentiation vs. free Khan Kids is clear enough to pay for.

| # | Method | Sample | Success | Kill / rethink |
|---|---|---|---|---|
| E1 | **Paper-prototype manipulatives** (physical scale, ten-frames, cards mimicking app flow) in pre-K | 16 children (≥4 ND/disabled) | Persistence ≥8 min on self-chosen work without rewards in ≥70% | <40% → add child-chosen decor/collections |
| E2 | **Figma tap-to-place vs. drag** A/B | 20 children aged 3–7 incl. 3 with motor differences | Tap success ≥95%; typically developing children rate tap ≥ drag | Tap rated worse by >30% → drag default with tap alt |
| E3 | **Calm vs. Lively** sensory A/B | Same 20 | Calm comfort ≥4/5; no persistence loss | Persistence loss >20% → Balanced default for 5–7 |
| E4 | **Parent summary test** (concept vs. score format) | n≈200 parents | Concept format preferred ≥60%; understood ≥80% | Else hybrid |
| E5 | **Teacher interviews** | 6 pre-K/Montessori teachers | ≥3 would pilot | <2 → deprioritise classroom mode |

**Mapping.** E1 → WP4 paper prototypes; E2–E3 → WP4 Figma + sensory A/B + accessibility round; E4 → WP2 survey; E5 → WP2 interviews / WP5 channel.

## 12. Build handoff

**Epic NN-E1: Manipulative engine.**
- **Given** any material, **when** the child taps an object, **then** it lifts, is announced by screen reader and voice ("apple"), and the valid destinations highlight.
- **Given** an object is selected, **when** the child taps a valid destination, **then** it moves there within 150 ms; tapping elsewhere deselects it (no penalty).
- **Given** drag is enabled and the child releases within 1.5 cm of a destination, **then** it snaps there.
- **Given** switch access, **then** scanning cycles objects, then destinations, with adjustable scan speed and no timeout.

**Epic NN-E2: Self-correction.**
- **Given** the scale has 5 vs. 4, **then** the heavier side tips at a visible angle, VoiceOver announces "left is lower", and no negative sound plays.
- **Given** amounts match, **then** the scale levels with one soft sound and haptic.

**Epic NN-E3: Shelf, session, ending.**
- **Given** the session length is 12 min, **when** 10 min pass, **then** "one more work" warning shows; after it the tidy-up routine ends the session.
- **Given** the child chose a material, **then** the algorithm never replaces it mid-work.

**Epic NN-E4: Mastery & parent summary.**
- **Given** a concept is solved without hints on two separate days, **then** it is marked mastered and a twig is added.
- **Given** a week ends, **then** the parent summary uses concept sentences, not percentages.

**Non-functional.** 60 fps on 2018 iPad / 2019 Android tablets; offline; iOS/iPadOS, Android; web (parent/teacher); WCAG 2.2 AA; EN/ES; zero third-party SDKs.

**QA focus.** AT matrix: Switch scanning, VoiceOver with haptics (blind child task completion), Voice Control, keyboard, left-hand layout, Dynamic Type in parent area. Motor testing with DCD and CP participants. Sensory A/B. COPPA: no audio, minimal events. Billing: free shelf always accessible.

**Platform dependencies.** Lumen (answer tray, Dial, strip); My Needs (input, hand, haptics); Family Hub; evidence engine (math probes).

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Free incumbents (Khan Kids) sufficient for parents | H | M | Inclusion + Montessori depth; bundle; classroom |
| Motivation without rewards | M | M | E1; collections tied to learning (nest) |
| Tap-to-place slower for typical kids | M | L | Drag optional; per-child default |
| Classroom sales cycle long | M | M | Start with family plan; teachers as advocates |
| Unverified competitor data | H | L | WP1 Sensor Tower export |

**Open questions.** Should Number Nest merge with Sound Garden as a single "Lanternling Learn" app for 4–7 (fewer apps for parents)? Is a printable mat enough "tangible" appeal vs. Osmo? Which UK/US numeracy standards to align to first?

## 14. Sources
- [V] Montessori RCT (Lillard et al. 2025): https://www.pnas.org/doi/10.1073/pnas.2506130122 (via raw 04)
- [V] Vatavu 2015 toddler touch (via raw 04): https://www.sciencedirect.com/science/article/abs/pii/S1071581914001426
- [V] SplashLearn: https://apps.apple.com/us/app/splashlearn-kids-learning-app/id672658828 · https://app.sensortower.com/overview/672658828?country=US
- [V] Kahoot! Numbers by DragonBox: https://apps.apple.com/us/app/kahoot-numbers-by-dragonbox/id1529174508 · https://www.commonsense.org/education/reviews/kahoot-numbers-by-dragonbox
- [V] Todo Math: https://apps.apple.com/us/app/todo-math/id666465255 · https://www.todomath.com/
- [V] Khan Academy Kids data: [raw 01](../../../research/raw/01-google-play-top30.md) · [raw 02](../../../research/raw/02-apple-app-store-top30.md)
- [M] Osmo/Byju's (raw 05): [raw 05](../../../research/raw/05-market-and-trends.md)
- [M] Moose Math, Montessori Numbers (Edoki), Marbleverse; Duncan et al. 2007 (early math predicts later achievement): to verify in WP1

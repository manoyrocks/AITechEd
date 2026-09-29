# Project Reevaluation & Enhancement Plan (v1.1)

**Date:** 29 September 2026 · **Status:** Discovery & Validation (specs only, no code)
**Scope:** a critical review of everything in this repository:
- the research paper
- the Lumen framework
- the 5 vision docs
- the discovery plan
- the 35 app specs
- the agent-team prompt

It is followed by enhancements to functions and features.

**Companion:** [Studio Platform Features & Shared Engines](04-studio-platform-features.md) (12 engines, 33 studio features, Family Pass pricing).
**Per-app changes:** every app doc now ends with **§15 Reevaluation & enhancements (v1.1)**, generated from [`tools/reevaluation_data.py`](../tools/reevaluation_data.py).

**Tags:** [V] verified · [V2] secondary · [M] memory, verify in WP1 · [E] estimate · [I] analyst inference.

---

## 1. Verdict in one paragraph

The **thesis holds**, and so does the design stance:
- inclusive and calm by default
- learners the frontier labs avoid
- human-reviewed AI
- fair billing
- honest evidence

The research supports all of these. The **execution plan does not hold as written**:
- 35 separate apps with **597 specified features (408 tagged MVP)** cannot be validated on a $1.0–1.5M, 16-week discovery budget, or built by a startup studio.
- The same capabilities are specified many times over.
- The family's journey across ages and ventures is not designed at all.
- The trust layer that differentiates us exists as principles, not as product.

**The fix:**
1. Keep all 35 as **experiences**, but build them on **12 shared engines**.
2. Ship them in **10 surfaces instead of 35 store apps**: 8 store apps, the Studio Family Hub and a Pro Console.
3. **Trim app-specific MVP scope from 408 to 183 features.**
4. **Add 33 studio-wide features** that close the gaps, plus **79 app-specific enhancements**.

---

## 2. What holds up (keep)

| Strength | Evidence in repo | Keep because |
|---|---|---|
| Segment gaps: 1–3, 8–12, 60+ and ND are under-served | Research paper §4.4, both store top-30s | Consistent across all 3 evidence streams |
| "Tutor, not friend", Socratic by default | Bastani 2025 (−17% unguarded) [V]; FTC 6(b) [V] | Evidence and regulation both point the same way |
| Lumen P1–P18, Sensory Dial, My Needs | Nothing in the top 30 does this (§6) | Clearest differentiator, and platforms reward it |
| Neurodiversity-affirming Wavelength | Raw 04 §A6 | Trust with the community is the moat |
| No-code discovery with pre-registered thresholds | Discovery plan §5–§8 | Protects against confirmation bias |
| Honest billing and claims | Top complaint in almost every leading app | Cheap to do, and a strong trust signal |

---

## 3. Issues found

| # | Issue | Evidence (from this repo) | Consequence | Fix (v1.1) |
|---|---|---|---|---|
| I-1 | **Scope sprawl** | 35 specs, 597 features, 408 tagged MVP (counted from §4 tables) | Unbuildable. Discovery WP4 can realistically test ~15 concepts | Engines + trimmed MVP (183) + waves (§6) |
| I-2 | **Duplicated capabilities** | Grandparent voice ×4 (TW-12, SL-07, TWO-02, BB-16). Scam training ×4 (AD, LR, Scam Gym, AFL checkpoints). Body doubling ×3. Routines/timers ×6. Weekly summaries ≈20. My Needs/Sensory Dial rows in almost every spec | 3–7× build cost. Inconsistent UX. Divergent safety behavior | 12 shared engines ([04 §1](04-studio-platform-features.md)) |
| I-3 | **Store fragmentation** | 35 would-be store listings. Parents already complain about app sprawl and bundle confusion (Piknik) [M] | Weak ASO. 35× review load. Split ratings. Painful family setup | 10 surfaces (§4) |
| I-4 | **No lifecycle across ages** | 0 specs define age-up at 13, record ownership at 16/18, or graduation between ventures | Churn at every transition, and COPPA/AADC risk | SX-02 Passport, SX-03 Age-up transitions |
| I-5 | **Pricing doesn't add up for families** | Lanternling $69/yr + Questwise $99/yr + Wavelength $149/yr, and Evergrow ranging $9.99–$59/mo | ND families pay twice. Siblings across ventures pay twice | SX-01 Family Pass ([04 §3](04-studio-platform-features.md)) |
| I-6 | **Trust is a principle, not a product** | 0 specs with a trust center, AI activity log or notification cap | The differentiator is invisible to parents | SX-05, SX-08, SX-09, SX-10 |
| I-7 | **Tutor engagement risk** | NBER/Chalkbeat 2026: students used Khanmigo in only 17% of sessions with errors [V2]. Our tutors were separate apps | Repeats the known failure mode | SX-17 Embedded Tutor with at-error invitations |
| I-8 | **Caregiver needs under-served** | 0 specs for IEP meeting prep, caregiver wellbeing or funding navigation, though raw 04 documents caregiver overload | Misses the buyer's most acute pain | SX-27, SX-28, SX-29 |
| I-9 | **Reach gaps** | Low-bandwidth appears in only 5 docs. No remote co-play. No phone access for 60+ without smartphones | Excludes low-income, rural and older users, which undercuts the inclusion thesis | SX-06, SX-23, SX-24, SX-26 |
| I-10 | **Market shifts not yet reflected** | Babbel closed consumer live classes (Jul 2025) [V2]. Coursera enterprise NRR ≈91% [V2]. EU AI Act Art. 4 softened (Jun 2026) [V2] | Speak Freely economics. AI Fluency Lab positioning | SF-E1 group check-ins. AFL-E1 productivity proof pack |
| I-11 | **Evidence base still partly unverified** | Search budget ran out. Many competitor rows tagged [M]/[V2] (see [apps/README](apps/README.md)) | Numbers not investor-ready | WP1 unchanged, plus a verification checklist (§9) |
| I-12 | **High-risk builds with no build-vs-partner decision** | Wavelength Voice (AAC motor planning, SLP trust). Spark Switch (hardware). Child ASR | Long timelines and clinical-trust risk | WV-E1 build-vs-license gate. Hardware partners. SX-22 spike |

---

## 4. Architecture shift: 35 experiences → 12 engines → 10 surfaces

### 4.1 Engines
The full specification is in [04 §1](04-studio-platform-features.md). In summary:
- **EN-01** Identity, Family & Consent
- **EN-02** Lifelong Learner Passport
- **EN-03** Tutor
- **EN-04** Reading Continuum
- **EN-05** Routine, Regulation & Focus
- **EN-06** Safety, Scam, AI & Media Literacy
- **EN-07** Family Voice, Languages & Co-play
- **EN-08** Pathways & Skills
- **EN-09** Voice, Speech & AAC
- **EN-10** Progress, Evidence & Content Studio
- **EN-11** Safe Live & Group Rooms
- **EN-12** Trust & Safety

### 4.2 Surfaces (what actually ships to stores)
<!-- GEN:SURFACES -->
| Surface | Experiences |
|---|---|
| **S1 Lanternling app** | Babble Buddy, Tap & Wonder, Story Lantern, Sound Garden, Number Nest, Calm Cubs, Two Words |
| **S2 Questwise app** | Sage Tutor, Math Realms, Read Rangers, Builder's Lab, AI Detectives, Wonder Lab, Mission Control |
| **S3 Ascendly app** | Study Coach, Exam Ready, Explain It Back, Draft Mentor, Study Squad, Pathfinder, Life Ready |
| **S4 Evergrow Work (B2B)** | AI Fluency Lab, Career Sprint, Lead with AI |
| **S5 Speak Freely** | Speak Freely |
| **S6 Evergrow Circle (60+)** | Silver Circuit, Curiosity Circle |
| **S7 Wavelength app** | Wavelength Day, Calm Harbor, ReadWave, Focus Crew, Social Compass, Spark Switch |
| **S8 Wavelength Voice (AAC)** | Wavelength Voice |
| **S9 Studio Family Hub** | Parent Coach, Family Pass, Trust Center, Family Digest, IEP Prep Coach, wellbeing, Funding Navigator |
| **S10 Pro Console (web)** | Teacher, guide, SLP/OT/BCBA, counselor, employer (aggregate), library and aging-agency consoles for all experiences |
<!-- /GEN:SURFACES -->

**Why these ten:**
- **One app per age venture** keeps ASO, ratings and the child's experience coherent, and parents manage one app per child.
- **Wavelength Voice stays stand-alone.** AAC must be dependable, and needs dedicated-device mode, "never mute on lapse" and SLP-led setup.
- **Speak Freely stays stand-alone.** Consumer language learning has its own store category and search behavior.
- **Evergrow splits by buyer:** employers get Evergrow Work, and seniors and families get Evergrow Circle.
- **Caregivers and professionals get their own surfaces:** the Family Hub and the Pro Console. They are never sent into child apps.

**To validate:** in WP3, run a card-sort and preference test with parents, comparing one app with modes against separate apps.

### 4.3 Overlap resolutions
| Overlap | Resolution |
|---|---|
| Calm Cubs ↔ Calm Harbor ↔ Wavelength Day | One EN-05 engine with Lanternling and Wavelength skins. A routine follows the child with consent. |
| Mission Control ↔ Focus Crew ↔ Study Squad | One EN-05/EN-11 focus stack with three age skins |
| Sage Tutor ↔ Study Coach ↔ tutors inside Math Realms, Read Rangers, Builder's Lab and Exam Ready | One EN-03 with age policies. Embedded at error moments. |
| Sound Garden ↔ Read Rangers ↔ ReadWave | One EN-04 skill model. Consented handoff; never a label. |
| AI Detectives ↔ Life Ready ↔ Scam Gym | One EN-06 case library in 4 age editions, with intergenerational missions |
| Pathfinder ↔ Career Sprint | One EN-08 with a continuous portfolio |
| Lead with AI ↔ AI Fluency Lab | Manager track inside AI Fluency Lab |
| Parent Coach ↔ ~20 per-app parent summaries | Studio Family Hub plus the Family Digest |
| Silver Circuit ↔ Curiosity Circle | One Evergrow Circle app |
| Two Words ↔ grandparent voice in 3 other apps | The EN-07 Family Voice & Languages layer |

---

## 5. Per-app reevaluation (all 35)

**How to read this table:**
- **Scores** are pre-discovery analyst judgments [I] using the Discovery Plan §6 weights. They are inputs to Gate 1, not decisions.
- **Trimmed MVP** lists app-specific features only. Platform capabilities come from the engines.
- The full detail is in each app doc's **§15**.

<!-- GEN:PER_APP -->
| Venture | App | Verdict | Ships in | Wave | Score | Trimmed MVP | New features |
|---|---|---|---|---|---|---|---|
| Lanternling | [Babble Buddy](apps/lanternling/01-babble-buddy.md) | Keep (lead) | S1 | 1c | 86 | 6 (BB-01, BB-02, BB-03, BB-05, BB-06, BB-08) | BB-E1 Hands-free mode; BB-E2 Early-intervention signposting; BB-E3 Remote co-play invite |
| Lanternling | [Tap & Wonder](apps/lanternling/02-tap-and-wonder.md) | Merge → 'Wonder' toddler mode inside the Lanternling app | S1 | 2 | 65 | 5 (TW-01, TW-02, TW-03, TW-04, TW-13) | TW-E1 Two-touch co-play; TW-E2 Bedtime handoff |
| Lanternling | [Story Lantern](apps/lanternling/03-story-lantern.md) | Keep (lead) | S1 | 1c | 83 | 6 (SL-01, SL-02, SL-03, SL-04, SL-05, SL-09) | SL-E1 Remote bedtime; SL-E2 Human-signed story shelf; SL-E3 Audio-player export |
| Lanternling | [Sound Garden](apps/lanternling/04-sound-garden.md) | Keep (lead) | S1 | 1c | 85 | 6 (SG-01, SG-02, SG-03, SG-04, SG-05, SG-06) | SG-E1 Classroom small-group CoPilot; SG-E2 Take-home decodables; SG-E3 Reading-profile handoff |
| Lanternling | [Number Nest](apps/lanternling/05-number-nest.md) | Keep | S1 | 2 | 67 | 6 (NN-01, NN-02, NN-03, NN-04, NN-06, NN-07) | NN-E1 Math-talk Moment Cards; NN-E2 Paper mirror |
| Lanternling | [Calm Cubs](apps/lanternling/06-calm-cubs.md) | Merge → Lanternling skin on EN-05 Routine, Regulation & Focus engine | S1 | 2 | 77 | 5 (CC-01, CC-02, CC-03, CC-04, CC-08) | CC-E1 Childcare handoff card; CC-E2 Gentle pathway to more support |
| Lanternling | [Two Words](apps/lanternling/07-two-words.md) | Re-scope → Family Voice & Languages layer (SX-07) + a stand-alone EFL SKU (MX/BR) | S1 | 2 | 65 | 4 (TWO-01, TWO-02, TWO-04, TWO-07) | TWO-E1 Record by link or phone; TWO-E2 Community heritage packs |
| Questwise | [Sage Tutor](apps/questwise/01-sage-tutor.md) | Re-scope → Embedded Tutor (EN-03) in every Questwise experience + a homework mode | S2 | 1c | 85 | 6 (ST-02, ST-03, ST-04, ST-05, ST-07, ST-10) | ST-E1 At-error invitations; ST-E2 Guide & parent CoPilot; ST-E3 Worksheet-aware capture |
| Questwise | [Math Realms](apps/questwise/02-math-realms.md) | Keep (lead) | S2 | 1c | 80 | 6 (MR-01, MR-02, MR-03, MR-04, MR-05, MR-06) | MR-E1 Real-world math missions; MR-E2 Calm fluency |
| Questwise | [Read Rangers](apps/questwise/03-read-rangers.md) | Keep | S2 | 2 | 73 | 5 (RR-02, RR-03, RR-04, RR-05, RR-07) | RR-E1 Reading continuum; RR-E2 Synced audiobook + text shelf |
| Questwise | [Builder's Lab](apps/questwise/04-builders-lab.md) | Defer to Wave 3 → a 'Make with AI' module (free Scratch/Code.org dominate) | S2 | 3 | 55 | 4 (BL-02, BL-03, BL-04, BL-06) | BL-E1 Accessible coding as the wedge; BL-E2 Make an AI responsibly |
| Questwise | [AI Detectives](apps/questwise/05-ai-detectives.md) | Merge → age 9–12 edition of EN-06 Safety, Scam, AI & Media Literacy engine | S2 | 2 | 73 | 4 (AD-01, AD-02, AD-03, AD-04) | AD-E1 Teach-your-grandparent missions; AD-E2 Free classroom edition |
| Questwise | [Wonder Lab](apps/questwise/06-wonder-lab.md) | Defer to Wave 3 | S2 | 3 | 57 | 4 (WL-01, WL-02, WL-04, WL-07) | WL-E1 Data sonification; WL-E2 Privacy-safe citizen science |
| Questwise | [Mission Control](apps/questwise/07-mission-control.md) | Merge → Questwise skin on EN-05 Routine, Regulation & Focus engine | S2 | 2 | 77 | 6 (MC-01, MC-02, MC-04, MC-05, MC-10, MC-13) | MC-E1 Family homework agreement; MC-E2 Assignment import in MVP |
| Ascendly | [Study Coach](apps/ascendly/01-study-coach.md) | Re-scope → Embedded Tutor (EN-03) in Exam Ready / Explain It Back + a stand-alone mode | S3 | 1d | 77 | 6 (SC-02, SC-03, SC-04, SC-05, SC-06, SC-08) | SC-E1 Bring your AI chat; SC-E2 At-error invitations |
| Ascendly | [Exam Ready](apps/ascendly/02-exam-ready.md) | Keep (lead) | S3 | 1d | 83 | 6 (ER-02, ER-03, ER-05, ER-06, ER-07, ER-09) | ER-E1 Accommodations request helper; ER-E2 Squad sync |
| Ascendly | [Explain It Back](apps/ascendly/03-explain-it-back.md) | Keep (lead, B2B wedge) | S3 | 1d | 87 | 6 (EB-02, EB-03, EB-04, EB-05, EB-06, EB-10) | EB-E1 Explain in your home language; EB-E2 Oral-defense lite |
| Ascendly | [Draft Mentor](apps/ascendly/04-draft-mentor.md) | Keep | S3 | 2 | 75 | 5 (DM-02, DM-04, DM-05, DM-06, DM-07) | DM-E1 AI-use disclosure draft; DM-E2 Home-language drafting |
| Ascendly | [Study Squad](apps/ascendly/05-study-squad.md) | Merge → Ascendly skin on EN-05 + EN-11 (Focus & safe rooms) | S3 | 2 | 65 | 5 (SQ-01, SQ-02, SQ-03, SQ-05, SQ-09) | SQ-E1 OS focus integration; SQ-E2 Library virtual study hall |
| Ascendly | [Pathfinder](apps/ascendly/06-pathfinder.md) | Merge → teen edition of EN-08 Pathways & Skills (continuity with Career Sprint) | S3 | 3 | 64 | 4 (PF-01, PF-02, PF-03, PF-04) | PF-E1 Accommodations & disclosure coach; PF-E2 Apprenticeship & CTE finder |
| Ascendly | [Life Ready](apps/ascendly/07-life-ready.md) | Merge → teen edition of EN-06 Safety, Scam, AI & Media Literacy engine | S3 | 2 | 60 | 3 (LR-01, LR-02, LR-03) | LR-E1 Teach-a-grandparent missions; LR-E2 Live scam season |
| Evergrow | [AI Fluency Lab](apps/evergrow/01-ai-fluency-lab.md) | Keep (studio lead; absorbs Lead with AI as the Manager track) | S4 | 1a | 84 | 6 (F1, F2, F3, F4, F5, F8) | AFL-E1 Productivity proof pack; AFL-E2 AI as assistive tech at work; AFL-E3 Manager track |
| Evergrow | [Career Sprint](apps/evergrow/02-career-sprint.md) | Merge → adult edition of EN-08 Pathways & Skills, in Evergrow Work | S4 | 2 | 68 | 5 (F1, F2, F3, F5, F6) | CS-E1 Neurodivergent hiring pathway; CS-E2 Portfolio continuity |
| Evergrow | [Speak Freely](apps/evergrow/03-speak-freely.md) | Keep (stand-alone consumer app; re-scope the human layer) | S5 | 2 | 70 | 6 (F1, F2, F3, F4, F6, F10) | SF-E1 Small-group check-ins by default; SF-E2 Community conversation hosts |
| Evergrow | [Lead with AI](apps/evergrow/04-lead-with-ai.md) | Merge → Manager track inside AI Fluency Lab | S4 | 2 | 66 | 3 (F1, F2, F6) | LA-E1 Team AI charter builder; LA-E2 Aggregate-only analytics |
| Evergrow | [Parent Coach](apps/evergrow/05-parent-coach.md) | Re-scope → Studio Family Hub (cross-venture caregiver app) | S9 | 1b | 79 | 5 (F1, F2, F3, F5, F7) | PC-E1 IEP/EHCP Prep Coach; PC-E2 Caregiver wellbeing & peer support; PC-E3 Family Digest home |
| Evergrow | [Silver Circuit](apps/evergrow/06-silver-circuit.md) | Keep (lead) → merges with Curiosity Circle into the Evergrow Circle app | S6 | 1b | 86 | 6 (F1, F2, F3, F4, F6, F7) | SCir-E1 Phone/IVR access; SCir-E2 Grandkids teach missions; SCir-E3 Trusted-contact alert |
| Evergrow | [Curiosity Circle](apps/evergrow/07-curiosity-circle.md) | Merge → Evergrow Circle app (with Silver Circuit) | S6 | 2 | 75 | 4 (F1, F2, F3, F4) | CCir-E1 Intergenerational circles (V2 → V1); CCir-E2 Paid peer-host pathway (V2 → V1) |
| Wavelength | [Wavelength Day](apps/wavelength/01-wavelength-day.md) | Keep (lead) | S7 | 1b | 91 | 7 (D1, D2, D3, D4, D5, D8, D9) | WD-E1 About Me passport; WD-E2 Family wall mode |
| Wavelength | [Wavelength Voice](apps/wavelength/02-wavelength-voice.md) | Keep (stand-alone AAC) — build-vs-partner gate in discovery | S8 | 1b | 80 | 6 (V1, V2, V5, V7, V12, V14) | WV-E1 Build-vs-license gate; WV-E2 SGD funding letter kit; WV-E3 AAC input everywhere; WV-E4 Offline emergency phrases |
| Wavelength | [Calm Harbor](apps/wavelength/03-calm-harbor.md) | Keep (lead; shares EN-05 with Calm Cubs) | S7 | 1b | 83 | 6 (C1, C2, C3, C5, C8, C13) | CH-E1 Sensory passport for school; CH-E2 Classroom calm-corner kiosk (V1 → MVP) |
| Wavelength | [ReadWave](apps/wavelength/04-readwave.md) | Keep (shares EN-04 Reading Continuum) | S7 | 2 | 83 | 6 (R1, R3, R4, R5, R8, R9) | RW-E1 IEP accommodations suggestions; RW-E2 Structured-literacy tutor channel |
| Wavelength | [Focus Crew](apps/wavelength/05-focus-crew.md) | Keep (shares EN-05 with Mission Control / Study Squad) | S7 | 2 | 81 | 5 (F1, F2, F4, F5, F6) | FC-E1 Teacher check-in card; FC-E2 Homework-conflict scripts |
| Wavelength | [Social Compass](apps/wavelength/06-social-compass.md) | Keep (Wave 3, high sensitivity; ND board veto) | S7 | 3 | 74 | 4 (S1, S2, S3, S11) | SCo-E1 Peer-understanding module; SCo-E2 Self-advocacy handoff |
| Wavelength | [Spark Switch](apps/wavelength/07-spark-switch.md) | Keep (Wave 3; partner hardware) | S7 | 3 | 73 | 6 (P2, P3, P4, P6, P7, P10) | SS-E1 Remote therapist mode; SS-E2 Family music-making (V2 → V1) |
<!-- /GEN:PER_APP -->

### 5.1 Priority ranking (pre-discovery)
<!-- GEN:RANKING -->
| Rank | App | Venture | Score | Wave |
|---|---|---|---|---|
| 1 | Wavelength Day | Wavelength | 91 | 1b |
| 2 | Explain It Back | Ascendly | 87 | 1d |
| 3 | Babble Buddy | Lanternling | 86 | 1c |
| 4 | Silver Circuit | Evergrow | 86 | 1b |
| 5 | Sound Garden | Lanternling | 85 | 1c |
| 6 | Sage Tutor | Questwise | 85 | 1c |
| 7 | AI Fluency Lab | Evergrow | 84 | 1a |
| 8 | Story Lantern | Lanternling | 83 | 1c |
| 9 | Exam Ready | Ascendly | 83 | 1d |
| 10 | Calm Harbor | Wavelength | 83 | 1b |
| 11 | ReadWave | Wavelength | 83 | 2 |
| 12 | Focus Crew | Wavelength | 81 | 2 |
| 13 | Math Realms | Questwise | 80 | 1c |
| 14 | Wavelength Voice | Wavelength | 80 | 1b |
| 15 | Parent Coach | Evergrow | 79 | 1b |
| 16 | Calm Cubs | Lanternling | 77 | 2 |
| 17 | Mission Control | Questwise | 77 | 2 |
| 18 | Study Coach | Ascendly | 77 | 1d |
| 19 | Draft Mentor | Ascendly | 75 | 2 |
| 20 | Curiosity Circle | Evergrow | 75 | 2 |
| 21 | Social Compass | Wavelength | 74 | 3 |
| 22 | Read Rangers | Questwise | 73 | 2 |
| 23 | AI Detectives | Questwise | 73 | 2 |
| 24 | Spark Switch | Wavelength | 73 | 3 |
| 25 | Speak Freely | Evergrow | 70 | 2 |
| 26 | Career Sprint | Evergrow | 68 | 2 |
| 27 | Number Nest | Lanternling | 67 | 2 |
| 28 | Lead with AI | Evergrow | 66 | 2 |
| 29 | Tap & Wonder | Lanternling | 65 | 2 |
| 30 | Two Words | Lanternling | 65 | 2 |
| 31 | Study Squad | Ascendly | 65 | 2 |
| 32 | Pathfinder | Ascendly | 64 | 3 |
| 33 | Life Ready | Ascendly | 60 | 2 |
| 34 | Wonder Lab | Questwise | 57 | 3 |
| 35 | Builder's Lab | Questwise | 55 | 3 |
<!-- /GEN:RANKING -->

---

## 6. Revised build waves

These apply only after Gate 2 = BUILD.

| Wave | Contents | Rationale |
|---|---|---|
| **0: Platform core** | EN-01, EN-02, EN-03, EN-05, EN-10, EN-12. Family Pass (SX-01), Trust Center (SX-08), Family Digest (SX-04), Notification Budget (SX-05), Pro Console (SX-30) | Everything in Wave 1 depends on these |
| **1a** | Evergrow Work: AI Fluency Lab | Fastest revenue and fundability. Proves the tutor and assessment core with adults, before children |
| **1b** | Wavelength Day, Calm Harbor, Wavelength Voice (after the build-vs-partner gate); Studio Family Hub (Parent Coach + IEP Prep Coach); Evergrow Circle: Silver Circuit via library pilots | Highest scores. ESA/IDEA channels. The strongest proof of the inclusion thesis |
| **1c** | Questwise: Sage Tutor (embedded) + Math Realms. Lanternling: Babble Buddy, Story Lantern, Sound Garden | Consumes the proven child-safe tutor, voice and routine engines |
| **1d** | Ascendly: Exam Ready, Explain It Back, Study Coach (embedded) | B2B proof-of-learning wedge, sold alongside consumer exam prep |
| **2** | Tap & Wonder (mode), Number Nest, Calm Cubs (skin), Two Words (layer), Read Rangers, AI Detectives/Life Ready (EN-06), Mission Control/Study Squad (EN-05 skins), Draft Mentor, Career Sprint, Speak Freely, Lead with AI (track), Curiosity Circle, ReadWave, Focus Crew | Mostly skins or editions on engines that already exist |
| **3** | Builder's Lab, Wonder Lab, Pathfinder, Social Compass, Spark Switch | Lower viability or higher sensitivity. Needs partners (hardware, sponsors) or deep co-design |

---

## 7. Venture-level enhancements (summary)

| Venture | Key enhancements |
|---|---|
| **Lanternling** | One app with modes. Hands-free Babble Buddy. Remote bedtime. Family Voice layer. Take-home decodables. Early-intervention signposting. Childcare handoff card |
| **Questwise** | An embedded Sage at error moments, with an uptake target of ≥40% against the 17% baseline. Guide and parent CoPilot. Calm fluency. Family homework agreement. Teach-your-grandparent missions |
| **Ascendly** | "Bring your AI chat" learning checks. Explaining in the home language. Oral-defense lite. AI-use disclosure drafts. Accommodations request helper. Teen–adult pathway continuity |
| **Evergrow** | Productivity proof pack. AI as assistive tech at work. Small-group language check-ins with community hosts. Phone/IVR access for 60+. Trusted-contact scam alert. Merged Evergrow Circle |
| **Wavelength** | About Me passport. Family wall mode. AAC build-vs-license gate. SGD funding letter kit. AAC input everywhere. Offline emergency phrases. Classroom calm kiosk. Peer-understanding module (double empathy both ways). Remote therapist mode |
| **Studio** | 33 SX features ([04](04-studio-platform-features.md)), especially the Family Pass, Lifelong Learner Passport, age-up transitions, Trust Center, Notification Budget, Remote Co-play, Sensory Passport, IEP Prep Coach, on-device AI tier and Content Studio |

---

## 8. Changes to the Discovery & Validation Plan

These are applied in [discovery-validation-plan.md §13](discovery/discovery-validation-plan.md).
1. **WP3:** test **engines and flagship experiences, not 35 concepts.** Shortlist ≤2 flagships per venture plus the Wave-0 engines. Add a card-sort on "one app vs. many".
2. **WP4:** new pre-registered experiments:

| Experiment | Question | Threshold |
|---|---|---|
| Embedded tutor A/B (Wizard-of-Oz) | Does an at-error invitation beat a separate tutor entry point? | Uptake ≥40% (baseline 17%) |
| Remote co-play (n=15 families with distant grandparents) | Will distant grandparents co-play regularly? | ≥2 sessions/week. Grandparent SUS ≥75 |
| IEP Prep Coach concierge (n=15 ND parents) | Do parents feel more prepared? | ≥70% "more prepared" |
| Trust Center comprehension (n=20 parents) | Can parents find what the AI did? | ≥80% answer "what did the AI do?" in ≤2 min |
| Notification budget (diary, n=20 families) | Does engagement hold under the cap? | No drop in weekly active families with ≤3 notifications/week |
| Phone/IVR access (n=10 seniors with landlines) | Can seniors without smartphones take part? | Complete a class and a scam check |
| Family Pass vs. venture plans (WP5 price test) | Which converts better? | Family Pass converts ≥ separate plans |
| AAC build-vs-license analysis | What should Wavelength Voice build? | Decision memo at Gate 2 |
| SX-22 on-device ASR spike | Is on-device speech recognition good enough for children? | WER by speaker group within target |

3. **Budget:** roughly neutral. Fewer concept prototypes offset the new experiments.

---

## 9. Verification checklist before external use

These are the items the research agents flagged as [M] or [V2] that the argument depends on:
- NBER/Chalkbeat Khanmigo 17% finding (primary paper)
- Babbel live-class closure date
- Coursera enterprise NRR
- EU AI Act Art. 4 amendment text
- Apple Declared Age Range and Google Play Age Signals APIs (availability, terms)
- On-device model frameworks (capability, child-use terms)
- ESA vendor rules in the 5 launch states
- Medicaid SGD documentation requirements
- Competitor rows tagged [M] in the Lanternling, Ascendly, Evergrow and Wavelength specs

---

## 10. Updated top risks

| Risk | Change since v1.0 | Mitigation |
|---|---|---|
| Platform-first delays the first revenue | **New** | Wave 0 is kept minimal. 1a (B2B) runs on the tutor + assessment engines only |
| Merged surfaces hurt venture brand clarity | **New** | Venture brands stay visible as modes inside surfaces. Card-sort test in WP3 |
| Engine coupling (one bug affects many experiences) | **New** | Engine owners, contract tests, staged rollouts, kill switches per experience |
| Intergenerational features raise privacy complexity | **New** | Consent by role in EN-01. Family-private recordings. No recording by default |
| Scope creep returns via "enhancements" | **New** | Enhancements are tiered, and only the trimmed MVP enters Wave 1 |
| Earlier risks (COPPA, ASR, ESA politics, claims) | Unchanged | As in the vision docs |

---

## 11. Changelog (v1.0 → v1.1)

| File | Change |
|---|---|
| `docs/03-project-reevaluation.md` | **New.** This document |
| `docs/04-studio-platform-features.md` | **New.** 12 engines, 33 SX features, Family Pass pricing |
| `docs/apps/*/0*.md` (35 files) | **Added §15** with verdict, surface, wave, score, trimmed MVP, new features and a validation question |
| `tools/reevaluation_data.py` | **New.** The single source for §15 and the tables above. Re-run after editing |
| `docs/discovery/discovery-validation-plan.md` | Added §13 v1.1 changes |
| `docs/agent-team/unified-agent-team-prompt.md` | Added §7 (engines and surfaces) and made §15 and the platform doc required reading |
| `docs/01-research-paper.md`, `docs/vision/*.md`, `docs/apps/*/README.md`, `README.md` | v1.1 pointers |

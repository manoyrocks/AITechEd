# Wonder Lab: App Strategy & Product Specification

> **Venture:** Questwise · **App #:** 6/7 · **Ages:** 8–12 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/02-questwise-tweens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Questwise index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A hands-on science companion that turns kitchens, backyards and parks into labs: guided experiments using the phone's sensors, a nature journal, and a human-reviewed "ask a scientist" guide. |
| **Primary user / buyer** | User: 8–12. Buyer: parent (esp. homeschool), ESA family, microschool/co-op, later libraries and nature centres. |
| **Core job-to-be-done** | "When I wonder why something happens, I want to test it myself with stuff at home and record what I find, so I can feel like a real scientist and share discoveries with my family." |
| **Category on the stores** | Education (iOS Kids 9–11) · Google Play Education, Families |
| **Top competitors** | Mystery Science, Generation Genius, KiwiCo, Tinybop, Seek by iNaturalist, PictureThis, Sky Guide, BrainPOP, Toca Lab |
| **Our wedge** | 1) Off-screen by design: the phone guides and measures, the child does the science (vs. video-first Mystery Science/Generation Genius). 2) Kit-optional, household materials first (vs. $19–24/mo KiwiCo crates). 3) Accessible experiments with alternatives for limited mobility, blind and Deaf learners, with a human-reviewed AI guide and COPPA-safe species ID (Seek-style no-account privacy). |
| **Business model** | In Questwise Family ($99/yr). Optional low-cost kit partner (V2). ESA and co-op licences. |
| **North-star metric** | Weekly completed investigations (experiment or observation logged with a prediction and a result) per active learner. |
| **MVP candidate?** | **Later** (V1/V2); validation (mailed cards) now. |

## 2. Problem & users

**Problem statement.** Curiosity fades when science is screen-only, and parents want hands-on activities without buying crates every month or prepping for an hour.
- Leading homeschool science programmes are video-led: Mystery Science ($199/yr homeschool) and Generation Genius ($250–325/yr) are NGSS-aligned video programmes for K–5 (GG to grade 8) [V2 homeschoolfox/mysteryscience].
- Hands-on crates cost: KiwiCo Tinker Crate $18.50–23.95/mo [V2 KiwiCo support].
- Explorable science apps are delightful but screen-only or discontinued: Tinybop Explorer's Library (10-app bundle $24.99) [V2 Apple]; Toca Lab: Elements discontinued as standalone in Oct 2023, now only via subscription [V2 fandom/Wikipedia].
- Nature ID shows what kids love and what to avoid: Seek collects no personal data by default, needs no account, obscures location, and is free [V iNaturalist Seek privacy]; PictureThis gives 1–2 free IDs, then a $39.99/yr trial that auto-converts [V2 identifythis].
- Vision persona demand: parents want off-screen experiences; screen-time guilt shapes decisions [V raw paper §5].

**Personas**

| Persona | Snapshot | Needs | Pain |
|---|---|---|---|
| **Maya, 9** | Collects rocks and bugs | Experiments she can do alone | Videos, not doing |
| **Theo, 11, wheelchair user with limited fine motor** | Loves space | Experiments he can run and measure | Instructions assume two-handed pouring |
| **Ada, 10, blind** | Curious about sound and weather | Audio-first sensing | Visual-only science apps |
| **Rachel, homeschool parent of 3** | Mixed ages 7–12 | Low-prep, cheap, safe experiments; records for ESA portfolio | Crate costs; video passivity |
| **Ms. Lee, co-op science lead** | 18 kids on Thursdays | Group investigations, printable guides | Assembling materials |

**Needs & wants**

| Need | Evidence | Response |
|---|---|---|
| Hands-on, off-screen | Vision; screen-time guilt [V raw paper] | Screen only at start/measure/record; "phone down" steps |
| Low cost, low prep | KiwiCo pricing [V2] | 80% experiments use household items; shopping list shown upfront |
| Safe experiments | Parent persona | Safety tiers, adult-needed flags, AI safety check for kid variations |
| Accessible science | Theo, Ada | Sensor-based and audio alternatives; helper roles |
| Records/portfolio | ESA/homeschool need | Science journal export |

## 3. Competitive feature benchmark

| App | Publisher | Signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Mystery Science** | Discovery Education | Very popular with K–5 teachers/homeschoolers [M] | Homeschool $199/yr (discount to $179) [V2] | n/a | Short, question-driven video lessons + simple activities | Grades K–5 only; video-led [V2] | Captioned videos [M] | mysteryscience.com/pricing |
| **Generation Genius** | Generation Genius | Classroom + homeschool [M] | $250–325/yr homeschool [V2] | n/a | NGSS videos to grade 8 | Price; passive [I] | Captions [M] | generationgenius.com |
| **KiwiCo (Tinker Crate)** | KiwiCo | Leading STEM crate [M] | $18.50–23.95/mo [V2] | n/a | Physical builds, quality kits | Cost; clutter; one project/month | Fine-motor heavy [I] | KiwiCo support |
| **Tinybop Explorer's Library** | Tinybop | Award-winning series [V2] | 10-app bundle $24.99 [V2] | n/a | Wordless, beautiful explorables | Screen-only; not updated often [M] | Wordless helps ELL; motion-rich [I] | Apple bundle |
| **Seek by iNaturalist** | iNaturalist | Popular free nature ID [M] | Free [V] | n/a | Real-time ID, challenges, no account | Phone-only [V2] | Camera-first [I] | inaturalist.org Seek privacy |
| **PictureThis** | Glority | High-grossing plant ID [M] | $39.99/yr; 1–2 free IDs [V2] | n/a | Accurate plant ID | Trial auto-converts; aggressive paywall [V2] | Camera-first | identifythis.app |
| **Sky Guide** | Fifth Star Labs | 4.8 (375K ratings); Editors' Choice [V2] | Free + IAP; Pro $59.99/yr [V2] | 4.8 | Point-and-see sky map | Upsells [I] | Visual-first; night mode | Apple listing |
| **BrainPOP (science)** | BrainPOP | Classroom staple [M] | Family ≈$129/yr [V2] | n/a | Short videos + quizzes | Passive | Captions | homeschoolbuyersclub |

**Feature matrix**

| Feature | Mystery Sci. | Gen. Genius | KiwiCo | Tinybop | Seek | Sky Guide | Our decision |
|---|---|---|---|---|---|---|---|
| Hands-on experiments | ◐ | ◐ | ✓ | ✗ | ✓ (field) | ◐ | **Differentiate** (sensor-guided) |
| Phone sensors as instruments | ✗ | ✗ | ✗ | ✗ | ✓ (camera) | ✓ (motion) | **Differentiate** (sound, light, motion, timer, camera) |
| Nature ID | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | **Parity** (on-device, Seek-style privacy) |
| Science journal/portfolio | ✗ | ✗ | ✗ | ✗ | ◐ | ✗ | **Differentiate** |
| Ask-a-scientist Q&A | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** (human-reviewed AI) |
| NGSS alignment | ✓ | ✓ | ◐ | ◐ | ✗ | ✗ | **Parity** |
| Physical kit subscription | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | **V2 optional** partner |
| Paywalled after 1–2 uses | ✗ | ✗ | — | — | ✗ | ◐ | **Reject** |
| Location sharing | ✗ | ✗ | — | — | obscured | local | **Reject** precise location; coarse only, on-device |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| WL-01 | ⭐ **Guided investigations** | 60 launch experiments (kitchen, backyard, bathroom, park), each: question → prediction → do → measure → explain; "phone down" steps | Screen-only gap | Differentiate | MVP | Must |
| WL-02 | ⭐ **Sensor toolkit** | Sound meter, light meter, stopwatch (child-started), motion/tilt, magnifier, time-lapse camera; data graphs | Unique vs. video programmes | Differentiate | MVP | Must |
| WL-03 | **Materials & safety card** | Shopping list first; safety tier (solo / adult nearby / adult does step); hazards read aloud | Parent persona | Lumen | MVP | Must |
| WL-04 | ⭐ **Science journal** | Photo, drawing, voice memo (with consent), data, claim-evidence-reasoning; export PDF for ESA portfolios | Portfolio need | Differentiate | MVP | Must |
| WL-05 | **Nature ID (on-device)** | Species ID with no account and coarse location only; kid-safe species facts | Seek model [V] | Parity | MVP | Must |
| WL-06 | **Wonder wall** | Child posts questions; AI drafts answers checked against curated sources; sensitive/uncertain ones queued for human scientist review | Vision | Differentiate | MVP | Should |
| WL-07 | **Accessible alternatives** | Each investigation has a one-handed/seated variant, an audio-first variant, and a "helper role" for co-op | Theo/Ada personas | Lumen | MVP | Must |
| WL-08 | **NGSS mapping & guide packs** | Standards per investigation; co-op group sheets | Mystery Science parity | Parity | MVP | Must |
| WL-09 | **Parent summary + co-play card** | What was investigated, claim made, "ask at dinner" question | P14 | Parity | MVP | Must |
| WL-10 | **Sensory Dial + themes** | Calm/Balanced/Lively; "Field Notebook" and "Lab" themes | P1, P13 | Lumen | MVP | Must |
| WL-11 | Seasonal expeditions | Month-long projects (bird count, moon journal, weather station) | Engagement without streaks | Improve | V1 | Should |
| WL-12 | Sky mode | Constellation finder with audio descriptions | Sky Guide parity | Parity | V1 | Could |
| WL-13 | Co-op science fair | Invited friends share journal pages; preset feedback | Vision co-op | Differentiate | V1 | Should |
| WL-14 | Low-cost kit partner | $15–25 seasonal kits purchasable by parents/ESA | KiwiCo alternative | Improve | V2 | Could |
| WL-15 | Citizen science link | Opt-in (parent) export of observations to iNaturalist projects via parent account | Real-world science | Differentiate | V2 | Could |

**MVP (when built) = WL-01 to WL-10 (10).** **Signature features:** WL-01 guided investigations, WL-02 sensor toolkit, WL-04 science journal.

## 5. Core experience & key user flows

**Core loop:** wonder (pick a question) → gather materials → predict → do (phone down) → measure with sensors → record → explain (claim-evidence-reasoning) → share with family → natural end.

**Flow 1: Onboarding.** Parent VPC; sets safety level (solo experiments allowed? heat/sharp tools never without adult); location precision (off/coarse). Child picks interests and theme. First investigation "How loud is your house?" (sound meter) in 5 min.

**Flow 2: Core investigation ("Which fabric keeps ice frozen longest?").**
1. Question card read aloud; shopping list; safety tier "solo".
2. Predict: tap choice or say it.
3. Setup steps with pictures; "Phone down: check back in 10 minutes" (a child-started timer with a gentle chime; it's a measurement tool, not a pressure timer).
4. Record: photo + observations; data table.
5. Explain: "My claim… my evidence… because…" with Socratic nudges ("What might make your test unfair?").
6. Journal page saved; co-play card for family.

**Flow 3: Parent/guide view.** Journal highlights, NGSS covered, materials for next week, export for ESA/portfolio.

**Flow 4: My Needs.** Variant preference (seated, audio-first), sensor feedback as sound/haptic/visual, text size, Dial.

**Flow 5: Billing.** Questwise charter; no per-ID paywall.

**IA:** Wonder (question picker), Investigation, Journal, Toolkit, Wonder Wall, My Needs.

**Session design:** Investigations 15–40 min, mostly off-screen; the app ends each with a journal page and a real-world suggestion.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial:** Calm: static illustrations, no music, sensor readouts as numbers + simple bars. Balanced (default): gentle animations on the Wonder screen only; soft chime for timer end. Lively: animated graphs, celebratory "discovery" screen (skippable).

**Input modes:** tap, voice, typing, drawing (journal), camera (optional; every camera step has a non-camera alternative: describe, draw or choose), switch (V1).

**Sensor accessibility:** sound meter shows vibration/haptic intensity for Deaf learners; light meter and colour detection *speak* values for blind learners ("Brighter… brighter… 320 lux"); motion experiments playable by tilting a wheelchair tray or helper-held phone.

**Physical alternatives:** every experiment lists a seated/one-handed variant (pre-measured cups, clamps, squeeze bottles) and a "helper role" so a sibling or peer does manual steps while the child directs and measures.

**Reading:** grade 3–4; step cards with photo + text + audio; BDA typography.

**Timers:** only child-started measurement timers; never countdown pressure; can be replaced by "tell me when you're done".

**Age-respectful:** "Field Notebook" (sketch style) and "Lab" (clean, photographic).

**Safety as accessibility:** hazard statements always read aloud and shown with icons.

**Lumen acceptance criteria**

| P | Criterion |
|---|---|
| P1 | Reduce Motion → static investigation screens |
| P2 | Sensor readings available as voice, haptic and visual |
| P3 | Same 6-step investigation structure always |
| P4 | No drag; large step buttons usable with wet/messy hands (≥56 dp) |
| P5 | Steps audio; grade 3–4 |
| P6 | BDA defaults |
| P7 | Non-camera alternative for every camera step |
| P8 | "Surprising results" celebrated; no failed experiments |
| P9 | Journal page ending |
| P10 | Materials and step list always visible |
| P11 | No pressure timers |
| P12 | Variants free |
| P13 | 2 themes |
| P14 | Co-play card each investigation |
| P15 | Expeditions (V1) instead of streaks |
| P16 | Scientists shown include disabled and ND scientists |
| P17 | No "boosts STEM scores" claims |
| P18 | No precise location; no account for nature ID; on-device vision |

**Target Lumen score:** 23/24.

## 7. AI specification & guardrails

- **AI does:** on-device species/object ID (vision model); Wonder Wall answer drafts grounded in a curated science corpus (encyclopaedic, museum, government sources) with citations; safety check on kid-proposed experiment variations (flags heat, chemicals, electricity, ingestion); Socratic prompts on explanations.
- **AI does not:** approve dangerous variations; identify people or faces (face detection blurs people in journal photos); answer medical questions ("Is this mushroom safe to eat?" → always "Never eat wild plants or mushrooms; ask an adult" plus poison-control info); roleplay a scientist persona.
- **Human review:** Wonder Wall answers tagged "uncertain", "sensitive" (body, death, disasters), or low-confidence go to a paid science educator queue (target 48 h); all experiments authored and safety-reviewed by educators (with a chemistry safety checklist).
- **Safety:** tool not friend; disclosure ("Answer drafted by a computer, checked by our science team"); distress escalation via shared classifier; no emotion recognition.
- **Evaluation:** species ID accuracy on regional test sets, with "I'm not sure" below confidence threshold; Wonder Wall factuality audit (≥98% on sampled answers); safety-check red team (500 risky variations; target 100% flagged).
- **Cost [E]:** on-device ID negligible; Wonder Wall ≈$0.02 per question + human review ≈$1–2 per escalated question.

## 8. Data, privacy & compliance

Journal (photos, drawings, text, optional voice memos), sensor data, coarse location (optional, on-device only), Wonder Wall questions. Photos auto-blur faces; journal stays private to family/guide. Retention: journal life of account, exportable; Wonder Wall questions 12 months. COPPA 2025 (photos/voice with a child's image or voice are personal information; geolocation precise = PI, so we never collect it; AI training off); FERPA for co-ops/schools; state design codes (geolocation off by default); UK AADC geolocation standard. Kids category and Families policy; no external links without parental gate (e.g., iNaturalist export requires parent).

## 9. Monetization & go-to-market

- **Benchmarks:** Mystery Science $199/yr; Generation Genius $250–325/yr; KiwiCo ≈$222–287/yr; Tinybop $24.99 one-time bundle; Seek free; PictureThis $39.99/yr; Sky Guide Pro $59.99/yr.
- **Ours:** in Questwise Family ($99/yr for 3 kids) = far below video science programmes; optional kits V2; co-op licence.
- **Channels:** homeschool (science is a common ESA spend [I]); co-ops; nature centres/libraries (V2); B2C.
- **ASO:** "science experiments for kids at home", "kids science journal", "nature app for kids safe", "homeschool science".

## 10. Success metrics

- **North-star:** weekly completed investigations (≥1.5 per active learner).
- **Inputs:** % with prediction + result; photos/drawings per journal page; accessible-variant usage; co-play card use.
- **Guardrails:** 0 safety incidents reported; Wonder Wall factual error rate <2%; Sensory Comfort ≥4/5; zero precise-location collection.
- **Outcomes:** claim-evidence-reasoning rubric growth over a term; science attitudes survey.
- **Retention:** weekly active families 35% of subscribers in school months [E].

## 11. Validation plan

**Riskiest assumption:** families will actually do off-screen experiments an app prompts (vision).

| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | Mail printed experiment cards for 3 weeks (vision test) | 20 families | ≥60% complete ≥4 of 6 experiments; ≥50% submit photos | <30% |
| E2 | Accessibility variants test (paper + phone sensor apps already on devices) | 5 motor-impaired, 4 blind/low-vision, 3 Deaf kids | Each completes ≥2 investigations independently or as director | <50% |
| E3 | Wonder Wall concierge (staff answer via form within 48 h) | 30 kids | ≥2 questions/kid/month; parents rate answers ≥4/5 | <0.5 questions/kid |
| E4 | Co-op pilot | 2 co-ops, 4 weeks | Leads rate ≥4/5; prep ≤15 min | Prep >30 min |

Mapping: E1, E2 → WP4; E3 → WP4; E4 → WP5.

## 12. Build handoff

**Epic A: Investigation player** — **AC-A1:** Given an investigation, When opened, Then materials, safety tier and variants appear before step 1, and hazards are read aloud.

**Epic B: Sensor toolkit** — **AC-B1:** Given VoiceOver is on, When the light meter runs, Then values are spoken on change (throttled to 1/s) with a rising/falling tone option. **AC-B2:** Given Deaf mode, When the sound meter runs, Then haptic intensity reflects dB level.

**Epic C: Journal** — **AC-C1:** Given a photo containing a face, When saved, Then the face is blurred on-device before storage.

**Epic D: Nature ID** — **AC-D1:** Given no account, When ID runs, Then no image or location leaves the device.

**Epic E: Wonder Wall** — **AC-E1:** Given a question tagged sensitive or confidence <0.8, When submitted, Then it is queued for human review and the child sees "A scientist will check this".

**NFRs:** sensors on mid-range Android; offline investigations; iOS/Android (web for guides); WCAG 2.2 AA; EN/ES.

**QA focus:** AT matrix (spoken sensors, haptics); sensory A/B; AI safety (dangerous variations, edible-plant questions, face blur); COPPA (no precise location, no photos off-device without consent); billing.

**Platform dependencies:** Lumen, My Needs, AI orchestration (on-device vision, curated-corpus RAG, review queue), privacy stack, evidence engine.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Kid gets hurt doing an experiment | Low | Very high | Safety tiers, educator review, adult flags, insurance review |
| Families don't do off-screen work | Medium | High | E1 thresholds; co-op channel |
| Species ID errors (e.g., toxic plants) | Medium | High | "Not sure" threshold; never "edible" guidance |
| Sensor variance across phones | High | Low | Relative measurements; calibration step |

**Open questions:** Which kit partner? Human scientist review cost at scale? Should Wonder Lab share the Seek-style no-account mode for a free tier?

## 14. Sources
- [V2] Mystery Science pricing: https://mysteryscience.com/pricing · https://homeschoolfox.com/compare/generation-genius-vs-mystery-science
- [V2] Generation Genius pricing: https://www.generationgenius.com/subscribe/
- [V2] KiwiCo pricing: https://support.kiwico.com/en_us/how-much-do-subscriptions-cost-SkeKovxfw
- [V2] Tinybop bundle: https://apps.apple.com/us/app-bundle/tinybop-explorers-1-10/id1350802724
- [V2] Toca Lab: Elements discontinued standalone: https://tocalab.fandom.com/wiki/Elements
- [V] Seek privacy: https://www.inaturalist.org/pages/seek_privacy_policy · https://www.inaturalist.org/posts/37149-tech-tip-tuesday-using-seek
- [V2] PictureThis pricing: https://identifythis.app/picture-this-app-review
- [V2] Sky Guide: https://apps.apple.com/us/app/sky-guide/id576588894
- [V2] BrainPOP pricing: https://homeschoolbuyersclub.com/products/brainpop-family-access-2
- [M] Mystery Science popularity; Smithsonian apps are mostly single-purpose/visitor apps (partial [V2]: https://www.si.edu/newsdesk/releases/national-air-and-space-museum-releases-free-children-s-app-pilot-pals)

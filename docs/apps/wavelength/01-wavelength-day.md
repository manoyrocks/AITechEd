# Wavelength Day: App Strategy & Product Specification

> **Venture:** Wavelength · **App #:** 1/7 · **Ages:** 2–17 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/05-wavelength-neurodivergent.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source, or carried over from the studio raw research files without re-checking · [M] from memory · [E] estimate · [I] inference
> **Evidence tiers (raw file 04):** E1 FDA authorization and/or RCT on the product · E2 peer-reviewed non-RCT product studies · E3 built on an evidence-based method, product untested · E4 testimonials only or contested

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A calm, predictable day in pictures: Now / Next / Done strips, first–then boards and transition warnings that a caregiver can set up in five minutes and the learner can own. |
| **Primary user / buyer** | User: the neurodivergent learner (2–17). Buyer: parent/caregiver (B2C/ESA), special-education teacher (IDEA), SLP/OT (clinician licence). |
| **Core job-to-be-done** | "When my day changes or I have to stop something I love, I want to see what is happening now and what comes next, so I can feel ready and move on without panic." Caregiver: "When mornings fall apart, I want a visual routine running in five minutes, so I can stop making laminated cards at midnight." |
| **Category on the stores** | Education (primary), Productivity (secondary). Not Kids Category at launch because the app has caregiver and teen modes (see §8). |
| **Top competitors** | Choiceworks, First Then Visual Schedule / Visual Schedule Planner (Good Karma), Goally, Tiimo, Brili, Otsimo, Social Story Creator (Touch Autism), Birdhouse |
| **Our wedge** | 1) **Five-minute setup** through templates and AI drafting from one sentence, reviewed by the caregiver; Goally users report hours of setup [V2]. 2) **Cross-platform, one account for the whole team** (iOS, Android, web, print), where Choiceworks is iOS-only [V2]. 3) **Learner-owned and age-respectful:** a "planner" look for teens and a break card on every schedule, with no compliance tokens. |
| **Business model** | Included in the Wavelength Family plan (≈$19/mo or $149/yr); Day-only tier ≈$5.99/mo or $49/yr [E]; school licence per learner; free print-only tier. |
| **North-star metric** | Weekly transitions completed with the schedule that the learner or caregiver rates "went OK or better", per active learner. |
| **MVP candidate?** | **Yes.** It is part of the Year-1 trio (Day + Voice + Calm Harbor) in the vision doc. |

## 2. Problem & users
**Problem statement.** Unexpected change and transitions away from preferred activities are a frequent trigger of distress for autistic and ADHD children. **Visual supports** and **social narratives** are both established evidence-based practices in the NCAEP 2020 review: visual supports with 104 single-case and 2 group-design studies, and social narratives for social, communication and behavioral outcomes across ages 3–18 [V] ([NCAEP 2020](https://ncaep.fpg.unc.edu/wp-content/uploads/EBP-Report-2020.pdf)). The method works. The tools do not:
- Families make laminated cards by hand [V2, raw 03].
- The trusted apps are dated, iOS-only and one-time purchases with limited sync. Choiceworks is $39.99 on iOS only [V] ([App Store](https://apps.apple.com/us/app/choiceworks/id486210964)).
- The all-in-one option (Goally) needs a dedicated tablet plus a subscription, and users report hours of setup, crashes, and routines disappearing between devices [V] ([justuseapp](https://justuseapp.com/en/app/1262461227/goally/reviews)).
- Teen-friendly planners such as Tiimo are rated 9+ and are designed for self-managing users, not for a caregiver team supporting a 5-year-old [V] ([lifestack](https://lifestack.ai/blog/tiimo-pricing)).

**Personas**
| Persona | Snapshot | What Day must do |
|---|---|---|
| **Kai, 4, autistic, minimally speaking** | Loves water and letters. Distressed when bath time ends. Uses symbols. | A photo first–then board ("First bath, then towel song"); a calm visual countdown; a symbol he can tap to ask for "more" or "break"; works with his AAC (Voice). |
| **Ethan, 14, autistic, sensory-sensitive** | Hates "baby apps". School timetable changes cause anxiety. | A calendar-style planner view with no cartoons; a "change" marker that explains what moved and why; he controls what his parents can see. |
| **Lauren, 39, parent of Kai and Mia** | Time-poor; grandparents do school pickup twice a week. | Five-minute setup from a template or one sentence; one schedule shared with grandparents and Kai's teacher; printable cards for the car. |
| **Ms. Brooks, special-ed teacher** | 12 students on IEPs. | Push a class schedule to 12 learners, tweak per learner, export "independent transitions" for IEP progress notes. |

**Needs & wants**
| Need | Evidence | How Day addresses it |
|---|---|---|
| Predictability; knowing what's next | Visual supports are an EBP [V] (NCAEP 2020) | Now/Next/Done strip, first–then board, day overview |
| Warning before a transition | Lumen P3; vision doc | Calm countdown in visual, haptic and optional audio form; "2 more minutes, then shoes" |
| Handling unexpected change | Parent VoC [V2, raw 03] | "Change card": a marked, explained swap, never a silent edit |
| Low setup burden | Goally complaints [V] | Templates, AI draft from a sentence, photo capture with auto-crop, reuse across days |
| Works across the team and devices | Choiceworks iOS-only [V]; Goally sync bugs [V] | Circle sync (iOS, Android, web), offline-first, print |
| Age-respectful for teens | Lumen P13; NN/g teen findings [V2] | Planner theme and mature photo sets, independent of support level |
| Preparing for new events (dentist, first day) | Social narratives are an EBP [V] | AI-drafted social narratives, **always reviewed by a caregiver** before the learner sees them |
| Learner agency | UDL 3.0 learner agency [V2] | Choice boards, learner reorders "free" slots, break card always available |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Evidence tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| **Choiceworks** | Bee Visual | Long-time SLP/OT staple; 2026 Webby Honoree [V] | $39.99 one-time, no subscription [V] | 4.6★ (290 US ratings) [V] | Schedule, waiting and feelings boards; own photos, video and recorded audio; visual timers [V] | iOS-only; dated look [V2] | Simple and calm; no Android or web | E3 | [App Store](https://apps.apple.com/us/app/choiceworks/id486210964) |
| **First Then Visual Schedule (HD)** / **Visual Schedule Planner** | Good Karma Applications | Small-review niche apps [I] | FTVS HD $14.99; VSP $14.99 one-time [V]; FTVS iPhone $9.99 [V2] | FTVS HD 3.3★ (24 ratings) [V] | Cheap, simple, audio prompts | Minimal updates [V2] | Basic; no sensory controls documented | E3 | [BridgingApps](https://search.bridgingapps.org/apps/first-then-visual-schedule-hd), [AppAdvice](https://appadvice.com/app/visual-schedule-planner/488646282) |
| **Goally** | Goally | Play parent app 5K+ downloads, 4.1★ (76 reviews) [V] | Device ≈$199–249 + ≈$15–20/mo [V2] | 4.1★ Play [V] | Locked-down kid tablet; routines, AAC, rewards, remote AAC modeling [V] | **Hours of setup; crashes; routines vanish between devices** [V] | Dedicated device avoids YouTube; reward-heavy [I] | E3 | [Google Play](https://play.google.com/store/apps/details?id=com.mygoally.mygoally), [justuseapp](https://justuseapp.com/en/app/1262461227/goally/reviews) |
| **Tiimo** | Tiimo ApS | **4M+ downloads**; ≈90k downloads and ≈$200k revenue in a recent month (estimate) [V2]; 2025 iPhone App of the Year [V2] | $7.99/mo, $79.99/yr, family $119.99/yr (up to 5) [V2] | 4.6★ (≈18–20K ratings) [V] | Visual timeline, AI task breakdown, focus timers, calm aesthetic, co-designed with ND users [V] | Subscription; setup overhead [V2]; free tier limited [V2] | Rated 9+; strong calm design; iOS-first [V2] | E3 | [lifestack](https://lifestack.ai/blog/tiimo-pricing), [EducationalAppStore](https://www.educationalappstore.com/app/tiimo) |
| **Brili Routines (kids)** | Brili GmbH | Play 10K+ downloads, 3.9★ (231 reviews) [V] | $7.99/mo, $49.99/yr [V2] | 3.9★ [V] | Timers that adapt to the time left in the routine [V2] | Small team, less content [V2] | Visual/audio prompts; reward points | E3 | [Google Play](https://play.google.com/store/apps/details?id=co.brili.routines&hl=en-US) |
| **Otsimo Special Education** | Otsimo | Play 100K+ downloads; "400,000+ students" claimed [V] | $9.99/mo, $119.99/yr, $229.99 lifetime [V2] | 2.1–3.2★ Play depending on listing [V] | Breadth: games, social stories, AAC companion [V2] | Subscription friction; **ABA framing polarizing** [V2] | Bright game style [I] | E3 | [AppBrain](https://www.appbrain.com/app/otsimo-%7C-special-education/com.otsimo.app) |
| **Social Story Creator & Library** | Touch Autism | Established niche iOS title [I] | Free, 2 stories; unlock by IAP; Educators edition $29.99 [V] | n/a | Photo-based stories, library, sharing | Paywall after 2 stories [V] | Simple; iOS-only | E3 | [App Store](https://apps.apple.com/us/app/social-story-creator-library/id588180598) |
| **Birdhouse for Autism** | Birdhouse | Niche cross-platform [I] | Free Lite; Premium $9.99/mo [V] | n/a | Searchable journal: meds, sleep, therapies, moods; syncs across devices [V] | Tracks "ABC" behavior data [V], which is a compliance-tracker pattern | Parent-facing only | E4 | [Touch Autism review](http://touchautism.com/birdhouse-for-special-needs-app-review/) |

Also scanned: Autism iHelp (deliberately minimal photo sets) [V2]. Its lesson is that minimalism is a feature.

**Feature matrix** (✓ yes · ✗ no · ◐ partial; from store listings and reviews, verify in the WP1 hands-on audit)
| Feature | Choiceworks | Good Karma | Goally | Tiimo | Brili | Otsimo | Our decision |
|---|---|---|---|---|---|---|---|
| Now/Next schedule strip | ✓ | ✓ | ✓ | ✓ (timeline) | ✓ | ◐ | **Parity** |
| First–then board | ◐ | ✓ | ◐ | ✗ | ✗ | ✗ | **Parity** |
| Waiting board / visual timer | ✓ | ◐ | ✓ | ✓ | ✓ | ✗ | **Parity** |
| Own photos + recorded audio | ✓ | ✓ | ✓ | ◐ | ◐ | ◐ | **Parity** |
| Cross-platform (iOS + Android + web) | ✗ | ✗ | ◐ | ◐ | ✓ | ✓ | **Improve**: all three, plus print |
| Multi-caregiver sync | ✗ | ✗ | ✓ (buggy [V]) | ◐ (family plan) | ◐ | ◐ | **Improve**: offline-first and conflict-safe |
| Setup ≤5 min with templates | ◐ | ◐ | ✗ [V] | ◐ | ◐ | n/a | **Differentiate**: templates + AI draft |
| AI schedule draft from a sentence | ✗ | ✗ | ✗ | ✓ (tasks) | ✗ | ✗ | **Differentiate**: caregiver-confirmed |
| Social narratives | ✗ | ✗ | ◐ (video) | ✗ | ✗ | ✓ | **Differentiate**: AI-drafted, mandatory human review |
| "Change" card for unexpected changes | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Teen planner theme | ✗ | ✗ | ✗ | ✓ | ✓ (adult app) | ✗ | **Differentiate**: same data, age-respectful skin |
| Printable cards | ✗ | ✗ | ✗ | ✗ | ✗ | ◐ | **Differentiate** |
| Token/points rewards for completion | ◐ | ✗ | ✓ | ✗ | ✓ | ✓ | **Reject** compliance tokens. Learner-chosen "done" celebration only (P15) |
| ABC behavior tracking | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ (Birdhouse ✓) | **Reject**: compliance-tracker framing; replace with "what helped" notes |
| Dedicated locked device | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | **Reject** as a requirement. Use OS Guided Access / Screen Time instead |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| D1 | **Now / Next / Done strip** | 1–5 visible steps (set per learner); finished steps slide to Done with a calm check | Visual supports EBP [V]; all competitors | Parity | MVP | Must |
| D2 | **First–Then board** | Two-panel board; the "then" can be chosen by the learner from 2–4 options | Good Karma parity; learner agency | Parity | MVP | Must |
| D3 | **Calm transition warnings** | Visual shrinking-shape countdown (no flashing), optional haptic pulse, optional spoken cue in a chosen voice; warning times set per step | Lumen P3/P11; vision doc | Improve | MVP | Must |
| D4 | **Change card** ★ | When an adult edits today's plan, the learner sees a marked "Change" card: what moved, a picture of the new thing, optional reason. Never a silent swap | Unexpected change is a top trigger [V2, raw 03] | Differentiate | MVP | Must |
| D5 | **Break card, always there** | A fixed "I need a break" / "help" tile on every schedule, linking to Calm Harbor or a caregiver-set break | Affirming stance; self-advocacy | Lumen | MVP | Must |
| D6 | **Picture library + own photos + recorded audio** | Symbols (open-licensed set, e.g., Mulberry/ARASAAC [M]), real-photo pack, camera capture with auto-crop, record a caregiver's voice | Parity; Autism iHelp minimalism | Parity | MVP | Must |
| D7 | **Five-minute templates** | 40 templates (morning, bedtime, school day, swimming, haircut, car trip) in playful, neutral and mature photo styles | Goally setup complaints [V]; Lumen P14 | Differentiate | MVP | Must |
| D8 | **AI schedule draft** ★ | Caregiver types or says one sentence ("school day, swimming Tuesdays, Grandma picks up Thursdays"); the AI builds a draft from the template library; the caregiver edits and confirms before anything reaches the learner | Riskiest-assumption feature; Tiimo AI precedent [V] | Differentiate | MVP | Must |
| D9 | **AI-drafted social narratives with mandatory review** ★ | Caregiver picks an event; the AI drafts a 4–8 page narrative from a human-authored style guide; a review screen requires the caregiver to read every page and confirm or edit; ND-board-approved templates for 30 common events | Social narratives EBP [V]; AI guardrail | Differentiate | MVP | Must |
| D10 | **Circle sync + roles** | Parent, grandparent, teacher and therapist roles; offline-first; edits merge per step; the learner can see who sees what | Goally sync bugs [V]; Lumen P14 | Improve | MVP | Must |
| D11 | **Print & export** | One-tap PDF cards (2×2, 3×3, strip) for screen-free use | Laminated-card workflow [V2] | Differentiate | MVP | Should |
| D12 | **Age-respectful themes** | Playful, neutral, planner (teen) views of the same schedule data | Lumen P13 | Lumen | MVP | Must |
| D13 | **My Needs + Sensory Dial** | Shared hub profile; Calm default; input mode; reading level | Lumen P1/P12 | Lumen | MVP | Must |
| D14 | **Weekly one-screen summary** | "Transitions that went OK" (learner or caregiver tap rating), new routines tried; no behavior scores | Lumen P14; IEP evidence | Improve | MVP | Should |
| D15 | Choice boards | Learner chooses the order of "free" slots or the next activity | UDL 3.0 agency | Differentiate | V1 | Should |
| D16 | Watch / Wear OS glance + haptic warnings | Now/Next on the wrist | Tiimo precedent | Parity | V1 | Could |
| D17 | Classroom push | Teacher pushes a class schedule; per-learner tweaks | Ms. Brooks | Improve | V1 | Should |
| D18 | Step video self-modeling | Caregiver records the learner (or a sibling) doing the step; stored on device by default | Video modeling EBP [M] | Improve | V1 | Could |
| D19 | Voice link | Tap a schedule item to open the same symbol in Wavelength Voice; AAC core words on the Now card | Cross-app | Differentiate | V1 | Should |
| D20 | Calendar import (ICS / Google / Apple) | Teen planner reads school or family calendars | Teen autonomy | Parity | V2 | Could |
| D21 | IEP/EHCP goal link | Map a routine to an IEP goal ("independently transitions with visual support") and export | B2B | Differentiate | V2 | Should |

★ = signature features: **Change card (D4)**, **AI schedule draft (D8)** and **reviewed social narratives (D9)**. The MVP has 14 features (D1–D14) and covers the full loop: set up → run the day → transition → reflect.

## 5. Core experience & key user flows
**Core loop (learner):** open (or it is already on the Now card) → see Now → warning → move to Next → Done with a calm check → end-of-routine "All done" screen with a real-world suggestion.
**Core loop (caregiver):** pick a template or type a sentence → review the draft → share with the team → glance at the weekly summary.

**Flow 1: Onboarding (≤5 min to first value)**
1. The adult opens the app. The Sensory Dial on the first screen is preset to **Calm**. The price is shown before any trial.
2. "Who is this for?" Name or nickname, age band and preferred look (playful / neutral / planner). **No diagnosis field.**
3. Pick a template (for example, "Morning before school") or type one sentence for the AI draft.
4. Review the draft: swap pictures (camera or library) and set warning times, with defaults of 2 minutes and 30 seconds.
5. "Try it now" runs the first step. Invites to other caregivers are optional and can come later.

**Flow 2: Core session (Kai's bath)**
1. The first–then board shows "Bath → Towel song".
2. At 2 minutes, a shrinking circle appears and a soft haptic plays. A caregiver-recorded "2 more minutes, then towel" plays only if audio is on.
3. Kai may tap **More** (goes to the caregiver's device as a request, never auto-granted) or **Break**.
4. The timer ends. The Now card shows Towel song, with no alarm sound. Bath slides to Done.
5. The routine ends on "All done" with an offline suggestion ("Choose pajamas"). The app does not auto-advance into another routine.

**Flow 3: Caregiver/teacher view**
1. The Circle dashboard lists each learner's day and changes made by others.
2. The teacher pushes the "Assembly day" change. Parents see it in the summary. The learner sees a Change card the next time he opens the schedule.
3. The weekly summary shows transitions rated OK or better, new routines, and caregiver notes. Export to PDF/CSV for the IEP.

**Flow 4: My Needs / settings**
1. Sensory Dial: Calm, Balanced or Lively (Lively is opt-in). Fine-tune motion, sound channels, haptics and tint.
2. Input: tap, switch (1–2), eye gaze, keyboard, voice.
3. Reading: pre-reader (pictures + audio), early, fluent.
4. People: who can view or edit; the teen sees and approves.

**Flow 5: Billing & cancellation.** The Fair-billing charter applies: price shown before the trial, a reminder 3 days before conversion, **one-tap in-app cancel**, pause for summer, and the print-only tier stays free forever. Accommodations are never paywalled.

**Information architecture:** Learner app: Today (Now/Next/Done) · Boards (first–then, waiting, choice) · Stories · Break. Caregiver: Circle hub → Learners → Schedules / Stories / Summary / Settings. Navigation is a fixed bottom bar with at most 4 labeled items, and help sits in a fixed position (WCAG 3.2.6).

**Session design:** The schedule has no session length of its own. Each routine has a designed "All done" ending. Transition warnings are the default, and there is no autoplay into the next routine.

## 6. Inclusive, accessible & sensory design spec
**Sensory Dial in Day**
| Level | Motion | Sound | Color | Completion feedback | Density |
|---|---|---|---|---|---|
| **Calm (default)** | Steps fade (≤200 ms); countdown is a slowly shrinking shape; no bounce | Off by default; spoken cues only if the caregiver turns them on; soft attack; peak cap | Muted palette, off-white background | Quiet check mark plus a short phrase ("Done") | 1 Now card (Next shown small) |
| **Balanced** | Gentle slide | Voice + soft chime | Moderate | Check + 1-second sparkle (no flashing) | Now + Next + 1 more |
| **Lively (opt-in)** | Full transitions, still no flashing >3/s (WCAG 2.3.1) | Music allowed outside tasks | Vivid | Optional celebration, skippable | Up to 5 steps |

**Input modes per task**
| Task | Tap | Switch (1/2) | Eye gaze / head tracking | Keyboard | Voice | AAC |
|---|---|---|---|---|---|---|
| Mark step done | ✓ | ✓ (auto or step scan) | ✓ (dwell 0.8–3 s, adjustable) | ✓ | ✓ ("done") | ✓ (Voice core word "done") |
| Choose "then" / choice board | ✓ | ✓ | ✓ | ✓ | ◐ (fallback chips) | ✓ |
| Break / help | ✓ fixed corner | ✓ first item in the scan order | ✓ | ✓ shortcut | ✓ | ✓ |
| Build schedule (adult) | ✓ | ✓ | ◐ | ✓ | ✓ (dictate the sentence) | n/a |

- **Switch scanning:** Uses OS Switch Control and Switch Access, plus in-app scanning for learners who don't use OS scanning. Scan speed runs 0.5–5 s with a hold-to-select option. The Break tile is always first in the scan order.
- **Eye gaze:** Supports Apple Eye Tracking and compatible gaze hardware [M]. Dwell is adjustable with a visible, non-flashing dwell ring. Targets are ≥2.5 cm with ≥1 cm spacing in gaze mode.
- **Targets:** ≥2.5 cm for ages 2–4 and ≥2 cm for 5–7; platform standard (44 pt / 48 dp) or larger for teens. There are **no drag gestures**. Reordering uses tap-to-pick then tap-to-place (WCAG 2.5.7).
- **Reading:** Pre-reader mode uses pictures and audio labels. Text follows BDA defaults (sans-serif, ≥18 px, 1.5 line height) and literal wording ("Put on shoes", not "Let's hit the road").
- **Audio:** Separate voice, cue and music channels. Every cue has a visual and a haptic twin, and captions are available for recorded audio.
- **Age-respectful themes:** Playful (illustrated), Neutral (flat symbols), Planner (teen: calendar grid, photo or monochrome icons), all independent of support level.

**Lumen principles: Day acceptance criteria**
| P | Acceptance criterion in Day |
|---|---|
| P1 | First screen is Calm; with Reduce Motion on there are 0 non-essential animations |
| P2 | 100% of cues have visual and haptic twins; sound is off by default for the learner |
| P3 | The Now card never changes position; unexpected edits always appear as a Change card |
| P4 | All learner tasks can be done with single taps, a switch or dwell; no drag anywhere |
| P5 | All step labels read at or below the profile level; audio label available on every card |
| P6 | BDA typography; text spacing override works |
| P7 | Each learner action has ≥3 input modes (see table) |
| P8 | Undo on every step for 10 s; missed steps just move to Done without penalty |
| P9 | Every routine ends on "All done"; no autoplay into the next routine |
| P10 | Picture sign-in for learners; no codes to remember |
| P11 | Timers appear only if chosen; the learner can ask for "more" (a request, not a failure) |
| P12 | My Needs imported from Circle; all accommodations free |
| P13 | Three themes, independent of level |
| P14 | Median setup ≤5 min in testing; multi-caregiver invites |
| P15 | No points, tokens or streaks in MVP; learner-chosen celebration only |
| P16 | ND advisory board signs off all 40 templates and 30 narrative templates; no "good sitting / quiet hands" content |
| P17 | Marketing says "built on visual supports, an evidence-based practice"; never "reduces meltdowns" |
| P18 | Photos stored on device by default; AI prompts are stripped of names; no ads |

**Target Lumen audit score: ≥22/24** (we expect to lose points only on item 1 until full screen-reader testing of the story reader is done).

## 7. AI specification & guardrails
**What AI does**
1. **Schedule drafting (D8):** An LLM turns a caregiver sentence into structured steps by choosing only from the template and step library (constrained generation, closed vocabulary of steps plus free-text labels). The output is always a *draft* on the caregiver's device.
2. **Social narrative drafting (D9):** An LLM fills an ND-board-approved narrative template for an event using a human-authored **style guide**:
   - first person or the learner's chosen perspective
   - descriptive sentences outweigh directive ones
   - "I might feel…; I can…" options, never "I will be good"
   - no demands for eye contact, quiet hands or hiding stims
   - literal language
   - The generic term "social narrative" is used, because "Social Stories" is a trademarked approach [M].
3. **Picture matching:** Suggests symbols or photos for each step label (on-device embedding lookup).

**What AI does not do:** It does not message the learner directly, act as a chat persona or companion, infer emotions (no camera or voice affect), rate behavior, or publish anything to the learner without caregiver confirmation.

**Pedagogical and content policy**
- **Mandatory review gate:** A narrative cannot be assigned until the caregiver has opened every page and pressed "I've read and approve". Edits are tracked.
- **AI disclosure:** A small "Drafted with AI, reviewed by Lauren" line is shown to adults. It is optional on the learner view, because the learner-facing content is the caregiver's.
- **Blocked topics:** Medical procedures beyond everyday events (dentist, haircut, vaccination) generate a caution with a clinician-review suggestion. Content on restraint, seclusion or punishment is refused.
- **Distress:** Day does not detect distress. The Break card is always available, and the self-report "I feel…" check lives in Calm Harbor.

**Evaluation plan**
- An offline eval set of 300 caregiver sentences and 100 event types, scored by 2 SLP/OT reviewers and 1 ND advisor on accuracy, literalness, affirming stance and reading level. **Ship threshold:** ≥90% "usable with minor edits" and 0 affirming-policy violations in 100 red-team prompts (for example, "make a story about stopping flapping").
- Human sampling of 5% of production narratives (with consent), reviewed monthly by the ND board.

**Cost and latency [E]:** A small hosted LLM costs ≈$0.002–0.01 per draft, with <4 s p95 for a schedule and <10 s for an 8-page narrative. The template library means ≥60% of setups need no LLM call.

## 8. Data, privacy & compliance
| Data | Why | Retention | Where |
|---|---|---|---|
| Learner nickname, age band, theme | Personalization | While the account is active; 30 days after deletion request | Cloud (encrypted), minimized |
| Schedules, steps, labels | Core function | Same | Cloud sync, cached on device |
| Photos / recorded audio | Personal cards | Learner's choice; **on-device by default**, synced only if the caregiver enables it | Device; optional encrypted cloud |
| Transition ratings ("went OK") | Summary, IEP export | 24 months rolling [E] | Cloud |
| AI prompts | Drafting | Not retained by the vendor (zero-retention API contract); names stripped | Cloud processor under DPA |

**Regimes**
- **COPPA 2025 (full compliance since 22 Apr 2026)** [V2, raw 04]: verifiable parental consent; separate consent for any third-party disclosure; written security program and retention policy. **No child data is used for model training.**
- **FERPA / state student-privacy laws** for school accounts: school-official exception, DPA, no advertising.
- **IDEA:** Day can be listed as assistive technology in an IEP. Exports support progress monitoring.
- **UK AADC / Data (Use and Access) Act 2025:** high-privacy defaults, profiling off, no nudges.
- **EU AI Act:** no emotion recognition (Art. 5). Drafting tools are not high-risk under Annex III because they don't assess learners [I].
- **HIPAA:** applies only when a covered clinician uses the clinician licence to share PHI; BAA available.
- **FDA / FTC:** education and organization claims only. Visual supports are described as an evidence-based practice, not a treatment.

**Consent flows:** The adult creates the account, then gives VPC (card check or ID match via a vendor). Teens (13–17) co-own their profile and see who has access.

**Store policies:** Google Play "Designed for Families" applies to the learner app. On Apple, the combined app ships in Education with a parental gate for purchases, links and settings. A separate Kids-Category "Day Player" build is a V1 option [I].

## 9. Monetization & go-to-market
| Tier | Price [E] | Includes | Benchmark |
|---|---|---|---|
| **Print-only (free)** | $0 | Templates, print cards, 1 learner | Choiceworks has no free tier [V] |
| **Day** | $5.99/mo or $49/yr | Unlimited schedules, AI drafts, 3 caregivers | Tiimo $79.99/yr [V2]; Brili $49.99/yr [V2]; Choiceworks $39.99 one-time [V] |
| **Wavelength Family** | ≈$19/mo or $149/yr | All 7 apps, up to 5 learners | Goally ≈$15–20/mo plus device [V2] |
| **School** | $10–25/learner/yr [E] | Class push, IEP export, rostering | IDEA-funded |
| **Clinician** | $15/mo per practitioner [E] | Up to 40 client learners, BAA | — |

- **Channels:** ESA vendor lists (FL FES-UA first), special-ed teachers via district SPED, OT/SLP practices, and parent communities, partnering with autistic-led organizations rather than using them only for marketing.
- **ASO:** Keywords: visual schedule, first then, routine chart, autism schedule, transition timer, social narrative. Fill in the **Apple Accessibility Nutrition Label** at launch: VoiceOver, Voice Control, Larger Text, Sufficient Contrast, Reduced Motion, Captions.
- **Launch markets:** US and UK (English), then Spanish (US). Symbol sets must be localizable.

## 10. Success metrics
- **North star:** Weekly transitions rated "OK or better" with the schedule, per active learner.
- **Input metrics:** % of new accounts reaching first run in ≤5 min (target ≥70%); routines per learner (≥3 by week 2); caregivers per learner (≥1.8); Change cards used per week; narratives approved per month.
- **Guardrails:**
  - Sensory Comfort ≥4/5 (learner pictorial or caregiver proxy)
  - 0 billing complaints
  - AI narrative review pass ≥90%
  - 0 ND-policy violations shipped
  - sync-loss incidents = 0 (Goally lesson)
- **Outcome measures:** Caregiver-rated transition ease (pre/post, 5-point), learner self-report where possible, teacher-rated independent transitions. **Evidence plan:** E3 at launch → E2 via a pre-registered single-case multiple-baseline study with a university partner in Year 1.
- **Retention targets:** D1 60%, D7 45%, D30 35%, DAU/MAU ≥40% [E]. A utility app used daily should beat typical education-app benchmarks (raw 05 [V2]).

## 11. Validation plan (no-code)
| # | Riskiest assumption | Experiment | Sample | Success | Kill / pivot |
|---|---|---|---|---|---|
| 1 | AI drafting + templates give ≤5-min setup and keep caregiver trust (W1) | Timed setup: Figma prototype with WoZ AI vs. Choiceworks on a loaner iPad | 20 caregivers (≥8 of them ND themselves) | Median ≤5 min; SUS ≥75; trust ≥4/5 | Median >10 min or trust <3.5 → drop AI draft, keep templates |
| 2 | Caregivers actually review AI narratives rather than rubber-stamping | WoZ narratives with 2 seeded errors per story | 20 caregivers | ≥80% catch ≥1 seeded error | <50% → redesign the review gate (page-by-page confirm, highlighted AI text) |
| 3 | Change cards reduce distress at unexpected changes | 2-week paper diary with printed Change cards vs. usual practice (crossover) | 15 families | Caregiver-rated ease +1 point | No difference → keep as a Should |
| 4 | Teens will use the planner theme | Figma preference test | 12 ND teens | ≥70% prefer planner over the playful theme; "not babyish" ≥4/5 | — |
| 5 | Sensory A/B: Calm vs. Lively | Lumen protocol | 20 learners | Comfort +1 for ND participants | — |
| 6 | ESA and teachers pay | Smoke test + 8 SPED interviews | — | ≥8% waitlist; ≥3 teachers want to pilot | <3% → free-core model |

**Mapping:** WP2 diaries (#3), WP4 solution validation (#1, #2, #4, #5), WP5 channels (#6). Gate 1 (week 8) confirms the problem; Gate 2 (week 16) decides the build.

## 12. Build handoff (post-Gate 2)
**Epic A: Today view (learner)**
- *Given* a schedule with 5 steps and Calm mode, *when* the learner opens Day, *then* the Now card fills ≥50% of the screen, Next is shown smaller, and no animation plays if Reduce Motion is on.
- *Given* a step with a 2-minute warning, *when* 2 minutes remain, *then* a non-flashing countdown shape appears, a haptic plays if enabled, and no audio plays unless audio cues are on.
- *Given* switch mode with 1 switch, *when* scanning starts, *then* the Break tile is scanned first and scan speed matches the My Needs value.

**Epic B: Change card**
- *Given* a caregiver edits a step for today, *when* the learner next views Today, *then* a Change card shows the old picture with a "moved" mark, the new picture and optional reason audio, and the learner must tap "OK" (or switch-select it) before continuing.

**Epic C: Setup & templates**
- *Given* a new caregiver, *when* they choose the "Morning" template and accept the defaults, *then* a runnable schedule exists in ≤6 taps.
- *Given* a caregiver sentence, *when* the AI draft returns, *then* every step is editable, the draft is labeled "AI draft", and nothing is visible to the learner until "Confirm".

**Epic D: Social narratives**
- *Given* an AI-drafted narrative, *when* the caregiver has not opened every page, *then* "Assign" stays disabled.
- *Given* a prompt requesting stim suppression or eye contact, *when* drafting runs, *then* the model refuses with an explanation and offers an affirming template.

**Epic E: Circle sync.** *Given* two caregivers edit different steps offline, *when* both reconnect, *then* both edits persist and each author is shown. Same-step conflicts ask the latest editor to choose.

**Epic F: Print/export.** *Given* a schedule, *when* the caregiver taps Print, *then* a PDF with ≥3 cm cards and labels is generated on device.

**Non-functional requirements**
- **Performance:** Today renders in <1 s on a 2019-era Android tablet.
- **Offline:** Full learner offline use; sync queue.
- **Platforms:** iOS/iPadOS, Android, web (caregiver).
- **Accessibility:** WCAG 2.2 AA; Accessibility Nutrition Label.
- **Localization:** EN-US, EN-GB, ES; right-to-left ready.
- **Security:** Encryption at rest and in transit, SOC 2 roadmap, role-based access.

**QA focus**
- **AT matrix:** VoiceOver (iOS/iPadOS), TalkBack, Apple Switch Control (1 and 2 switches, auto and step scan), Android Switch Access, Apple Eye Tracking and one external gaze bar [M], Voice Control / Voice Access, Full Keyboard Access, Dynamic Type XXL / Android font 200%, Reduce Motion / Remove animations, Guided Access.
- **Sensory A/B:** Calm vs. Lively on 3 flows; photosensitivity check with a PEAT-style flash analysis [M] on every animation.
- **AI safety:** 100 red-team prompts (compliance or masking requests, medical, violent events); hallucinated steps; names leaking into logs.
- **COPPA:** VPC flow, consent revocation deletes data within 30 days, no third-party SDKs on the learner surface.
- **Billing:** Price before trial, reminder at T-3 days, one-tap cancel, pause, refund path.

**Studio platform dependencies:** Lumen design system (Sensory Dial, Now/Next strip), Circle hub (My Needs, roles, sharing), AI orchestration (constrained generation, policy filters), privacy stack (VPC, retention), evidence engine (summary metrics, export).

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Caregivers rubber-stamp AI narratives | Med | High | Page-by-page review gate, highlighted AI text, seeded-error testing |
| Perceived as a "compliance" tool by autistic adults | Med | High | No tokens; Break card; ND board veto; public co-design credits |
| Sync bugs (the Goally failure mode) | Med | High | Offline-first CRDT-style merge [I]; sync telemetry; QA soak tests |
| Commoditized by free OS tools (Reminders, Tiimo) | Med | Med | Team features, first–then, narratives, printing, younger learners |
| Symbol-set licensing | Low | Med | Open-licensed sets plus own photos; legal review |

**Open questions:** Should Day ship as a separate Kids-Category player app? Which symbol set do SLPs prefer (to align with Voice)? How much do teachers need a multi-student view in the MVP?

## 14. Sources
- [V] NCAEP 2020 EBP report: https://ncaep.fpg.unc.edu/wp-content/uploads/EBP-Report-2020.pdf
- [V] Choiceworks, App Store: https://apps.apple.com/us/app/choiceworks/id486210964 ; BridgingApps: https://search.bridgingapps.org/apps/choiceworks
- [V] First Then Visual Schedule HD: https://search.bridgingapps.org/apps/first-then-visual-schedule-hd ; Visual Schedule Planner: https://appadvice.com/app/visual-schedule-planner/488646282
- [V] Goally Play listing: https://play.google.com/store/apps/details?id=com.mygoally.mygoally ; reviews: https://justuseapp.com/en/app/1262461227/goally/reviews ; [V2] pricing: https://www.educationalappstore.com/app/goally
- [V2] Tiimo pricing and downloads: https://lifestack.ai/blog/tiimo-pricing ; [V] ratings: https://www.educationalappstore.com/app/tiimo ; https://www.tiimoapp.com/
- [V] Brili Play: https://play.google.com/store/apps/details?id=co.brili.routines&hl=en-US
- [V] Otsimo: https://www.appbrain.com/app/otsimo-%7C-special-education/com.otsimo.app ; [V2] pricing: https://www.educationalappstore.com/app/otsimo-special-education-aba
- [V] Social Story Creator & Library: https://apps.apple.com/us/app/social-story-creator-library/id588180598
- [V] Birdhouse: http://touchautism.com/birdhouse-for-special-needs-app-review/
- [V2] Studio raw research 03, 04, 05 (this repo): ../../../research/raw/
- [M] Symbol sets (Mulberry, ARASAAC), Carol Gray trademark, external eye-gaze compatibility: verify in WP1.

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (lead) |
| **Ships in** | Wavelength app (S7) |
| **Build wave** | 1b |
| **Pre-discovery priority score** | 91/100 [I] |
| **Consumes engines** | EN-05, EN-02, EN-10 |
| **Studio features used** | SX-12, SX-19, SX-25, SX-27 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = D1, D2, D3, D4, D5, D8, D9.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| WD-E1 | **About Me passport** | A learner-approved one-page communication, sensory and support profile for school, clinicians, hospitals and emergency responders (SX-12). |
| WD-E2 | **Family wall mode** | The shared visual schedule on a kitchen tablet or TV, in calm display mode. |

### 15.3 New validation question
Timed setup ≤5 min median against Choiceworks; passport usefulness rated by 10 teachers and 5 clinicians.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 5 | 5 | 5 | 4 | 4 | 4 | 4 | 5 |

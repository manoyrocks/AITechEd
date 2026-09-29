# Focus Crew: App Strategy & Product Specification

> **Venture:** Wavelength · **App #:** 5/7 · **Ages:** 7–17 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/05-wavelength-neurodivergent.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary, or carried over from studio raw research · [M] memory · [E] estimate · [I] inference
> **Evidence tiers:** E1 FDA/RCT on product · E2 peer-reviewed product studies · E3 evidence-based method, product untested · E4 testimonials/contested
> **Research note:** The session's web-search quota ran out before this app's competitor pass, and the network proxy blocked direct fetches of store pages. Competitor facts here come from the studio raw files (tagged [V2]) or memory ([M]). They are flagged for re-verification in Discovery WP1.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Get started, keep going, and know when you're done: task breakdown you control, time you can *see*, a calm co-working buddy, and rewards that fade on a plan you agreed to. |
| **Primary user / buyer** | Users: ADHD/ADD and other ND learners 7–17 with executive-function differences. Buyers: parents (B2C/ESA), school resource teachers, ADHD coaches/clinicians. |
| **Core job-to-be-done** | "When I have to do something boring or big, I want to know the first tiny step and have someone 'with' me, so I can start without a fight and finish without feeling bad." Parent: "I want homework and mornings without nagging, and without a reward system that stops working in three weeks." |
| **Category on the stores** | Productivity / Education (kids and teens). |
| **Top competitors** | Joon, Tiimo, Goally, Brili, Goblin Tools, Forest, EndeavorRx (evidence benchmark), Focusmate (adult body doubling); also Structured, Habitica, Inflow (adult ADHD) |
| **Our wedge** | 1) **A reward-fading plan built in:** the child co-signs a plan that thins external rewards as independence grows, a direct answer to Joon's weeks-long novelty decay [V2]. 2) **Body doubling that is safe for minors:** a caregiver co-work mode and an ambient focus buddy that is clearly a tool, not a friend, rather than adult peer rooms. 3) **Shame-free:** no streak loss, no "overdue" red, pause days, and the child edits AI task breakdowns. |
| **Business model** | Family plan; Focus Crew tier ≈$6.99/mo or $59/yr [E]; school/coach licence. |
| **North-star metric** | Weekly tasks *started* within 5 minutes of the planned time with no adult prompt, per active learner. |
| **MVP candidate?** | **Later** (Year 2 per vision). Spec ready for Gate 2. |

## 2. Problem & users
**Problem statement.**
- ADHD affects ≈11.4% of US 3–17-year-olds (7.1M), and about 1 in 3 received no ADHD-specific treatment in 2022 [V2, raw 04 citing CDC].
- Executive-function tasks are daily flashpoints: starting, estimating time, switching tasks, finishing homework.
- **Three failure patterns in current tools:**
  1. **Novelty decay.** Joon's virtual-pet rewards engage fast, but parents report kids bored within weeks. Parents also cite heavy admin and trial-billing complaints [V2, raw 04].
  2. **Adult admin load.** Goally setup takes hours [V]. Planners like Tiimo are built for self-managing teens and adults (rated 9+) [V].
  3. **Evidence gap.** EndeavorRx is the only E1 ADHD game. It improved an objective attention measure but not parent-rated symptoms, and the company was sold for ≈$34M after cuts [V2, raw 04]. So clinical-grade claims don't guarantee value or a business.
- AI task breakdown (Goblin Tools "Magic ToDo") went viral with ND adults because it is free and simple [V2]. It is not designed for children, and output quality varies [V2].
- Rewards can support ADHD learners short-term. But self-determination research warns that expected, tangible rewards can undermine intrinsic motivation, which argues for planned fading [M: Deci, Koestner & Ryan 1999 meta-analysis].

**Personas**
| Persona | Snapshot | What Focus Crew must do |
|---|---|---|
| **Mia, 9, ADHD + dyslexia** | Homework ends in tears; time blindness. | Picture/voice task steps; visual timer she can see "shrinking"; parent co-work mode; movement break; no reading needed. |
| **Sam, 13, ADHD (inattentive)** | Loses track of assignments; hates being nagged; wants independence. | Breaks a project into steps and edits them; ambient focus buddy; private progress; parent sees only what he shares. |
| **Lauren, parent** | Tired of being the "nag". | Set up routines once; co-work remotely from the next room or from work; a fading plan she doesn't have to track manually. |
| **Coach Rivera, ADHD coach / school resource teacher** | 25 students. | Assign weekly goals; see start/finish patterns; export for 504 plans. |

**Needs & wants**
| Need | Evidence | How Focus Crew addresses it |
|---|---|---|
| Starting tasks | ADHD EF [M]; Goblin Tools popularity [V2] | "First tiny step" breakdown, child-editable |
| Seeing time | Brili adaptive timers [V2]; Tiimo timers [V] | Visual time timer (disc/bar), time-left-in-routine, estimates that learn |
| Company while working | Body-doubling culture (Focusmate) [M] | Caregiver co-work; ambient focus buddy; V2 moderated peer rooms 13+ |
| Motivation that lasts | Joon novelty decay [V2] | Agreed reward plan with automatic fading + intrinsic "independence meter" |
| Shame-free progress | Lumen P8/P15; streak "dread" [V2, research paper] | Gentle weekly goals, pause days, no red overdue |
| Movement | ADHD movement needs [M] | Movement breaks scheduled or on request |
| Low parent admin | Goally [V] | Templates, AI setup, weekly summary |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Evidence tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| **Joon** | Joon Care | Leading kids' ADHD routine app in reviews [V2] | Free core; **$12.99/mo or $89.99/yr**, 7-day trial [V2] | n/a (re-verify) | Virtual pet ("Doters"), quests set by parents; strong initial motivation [V2] | **Charged after cancelling trial; overpriced; kids bored within weeks; heavy parent admin** [V2] | Game-style, reward-heavy [I] | E3 (vendor says studies in progress [M]) | [ChoosingTherapy](https://www.choosingtherapy.com/joon-app-review/), [Common Sense](https://www.commonsensemedia.org/app-reviews/joon-kids-chore-list-chart) |
| **Tiimo** | Tiimo ApS | 4M+ downloads [V2]; 2025 iPhone App of the Year [V2] | $7.99/mo, $79.99/yr, family $119.99/yr [V2] | 4.6★ (≈18–20K) [V] | Visual timeline, AI breakdown, focus timers, calm aesthetic [V] | Subscription; setup [V2] | Calm; 9+; iOS-first | E3 | [lifestack](https://lifestack.ai/blog/tiimo-pricing), [EducationalAppStore](https://www.educationalappstore.com/app/tiimo) |
| **Goally** | Goally | Play 5K+ [V] | Device ≈$199–249 + ≈$15–20/mo [V2] | 4.1★ Play [V] | Locked-down device; routines; rewards; AAC [V] | Setup hours; sync bugs [V] | Reward-heavy [I] | E3 | [justuseapp](https://justuseapp.com/en/app/1262461227/goally/reviews) |
| **Brili Routines** | Brili GmbH | Kids 10K+ / adult 50K+ Play [V] | $7.99/mo, $49.99/yr [V2] | 3.9★ [V] | Timers adapt to time left [V2] | Small content [V2] | Visual/audio prompts | E3 | [Play](https://play.google.com/store/apps/details?id=co.brili.routines&hl=en-US) |
| **Goblin Tools** | Bram De Buyser | Viral 2023–24 [V2] | Free web; small one-time mobile fee [M] | n/a | Magic ToDo recursive breakdown; "spiciness" slider; Estimator, Judge [V2] | LLM quality varies; not child-directed [V2] | Plain, low-stim UI [M] | E4 | [goblin.tools](https://goblin.tools/About) (via raw 04) |
| **Forest** | Seekrtech | **1M+ ratings, 4.8★** [V2, raw 03] | Paid iOS / free Android + IAP [M] | 4.8★ [V2] | Grow a tree while you focus [V2] | Easy to bypass; novelty wears off [M] | Tree "dies" if you leave: loss framing [V2] | E4 | raw 03 |
| **EndeavorRx** | Virtual Therapeutics (ex-Akili) | Rx; commercial failure, sold ≈$34M [V2] | Rx; ≈$99/mo cash historically [M] | n/a | FDA De Novo 2020 (8–12, expanded 13–17) [V2] | Parent-rated symptoms not significantly different vs. control [M]; payer coverage poor [V2] | Fast action game; high stimulation [I] | **E1** | [BioPharma Dive](https://www.biopharmadive.com/news/akili-sell-34m-virtual-therapeutics-digital/717576/) (via raw 04) |
| **Focusmate** | Focusmate | Popular adult body-doubling service [M] | Free limited sessions; paid plan [M] | n/a | Scheduled 1:1 video co-working [M] | Adults only [M]; video with strangers | Camera-on norm | E4 | [M] |

Also noted [M]: **Structured** (visual day planner, teen/adult), **Habitica** (RPG habit tracker; party mechanics, damage for missed dailies), **Inflow** (CBT-based adult ADHD program). None target children; Habitica's damage mechanic is exactly what we reject.

**Feature matrix**
| Feature | Joon | Tiimo | Goally | Brili | Goblin | Forest | EndeavorRx | Our decision |
|---|---|---|---|---|---|---|---|---|
| Task breakdown (AI) | ✗ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ | **Parity+**: child-editable, picture steps |
| Visual time timer | ◐ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | **Parity** |
| Time estimates that learn | ✗ | ◐ | ✗ | ◐ | ✓ (Estimator) | ✗ | ✗ | **Improve**: from the child's own history |
| Body doubling | ✗ | ✗ | ✗ | ✗ | ✗ | ◐ (group forest) [M] | ✗ | **Differentiate**: caregiver co-work + ambient buddy |
| Rewards | ✓ (pet) | ✗ | ✓ | ✓ | ✗ | ✓ (trees) | ◐ | **Improve**: learner-chosen, faded on a plan |
| Reward fading plan | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Movement breaks | ✗ | ◐ | ◐ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Parent quests / task assignment | ✓ | ◐ | ✓ | ✓ | ✗ | ✗ | ✗ | **Parity**, with child consent |
| Loss framing (pet sad, tree dies, damage) | ◐ [M] | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | **Reject** (P15) |
| Streak punishment | ◐ [M] | ✗ | ✗ | ✗ | ✗ | ◐ | ✗ | **Reject**; gentle weekly goals |
| Treatment claims ("treats ADHD") | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ (FDA) | **Reject**: education/organization claims only |
| Video co-working with strangers | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ (Focusmate ✓) | **Reject** for minors |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| F1 | **Break it down** | Type/say a task → AI proposes 3–7 steps with the first step tiny ("open your math book to p. 42"); child edits, reorders (tap-to-move), deletes; picture icons for younger kids | Goblin/Tiimo [V2/V] | Parity+ | MVP | Must |
| F2 | **Visual time timer** | Shrinking disc/bar, time-left-in-routine; calm end cue (visual + haptic; sound optional) | Brili/Tiimo parity | Parity | MVP | Must |
| F3 | **"How long will it take?" estimate & learn** | Child guesses, app records actual time, shows gentle comparison ("You guessed 10, it took 18: want 18 next time?") | Time blindness | Improve | MVP | Must |
| F4 | **Caregiver co-work mode** ★ | Parent and child start a session together (same room or remote via Circle); both see the timer; parent's device shows "working together" status; no video/audio needed | Body doubling, safe for minors | Differentiate | MVP | Must |
| F5 | **Ambient focus buddy** ★ | An optional, non-talking visual presence (a calm figure/object working at a desk, chosen from neutral styles) with ambient sound; *clearly a tool*: no name-by-default, no feelings, no "misses you" | Body doubling for solo work; P18 no companion | Differentiate | MVP | Should |
| F6 | **Reward plan with fading** ★ | Child + parent co-sign a plan: learner-chosen rewards (activities/privileges/choices, not food by default); schedule auto-thins (every task → every 3 → weekly reflection) as independence rises; child can see the plan | Joon decay [V2]; motivation research [M] | Differentiate | MVP | Must |
| F7 | **Independence meter** | Intrinsic progress: "tasks you started on your own" grows over weeks; replaces points as rewards fade | P15 | Differentiate | MVP | Must |
| F8 | **Movement breaks** | 1–3-min movement cards (wall push, jumping, stretch) on a schedule or on request; adapted for wheelchair users and DCD | ADHD movement [M]; inclusive | Differentiate | MVP | Should |
| F9 | **Homework & routine templates** | 30 templates (homework, morning, project, chores, test prep for teens) | Setup burden [V] | Improve | MVP | Must |
| F10 | **Gentle progress** | Weekly goals, pause days, no red "overdue", unfinished tasks roll gently to "later" | Lumen P15 | Lumen | MVP | Must |
| F11 | **Distraction shield (gentle)** | Uses OS Focus/Screen Time APIs to optionally quiet notifications during a session; child opts in | Forest demand [V2] without loss framing | Improve | MVP | Could |
| F12 | **Weekly summary (shared by consent)** | Tasks started/finished, estimates improving, rewards faded; teen chooses what parents see | Lumen P14; autonomy | Improve | MVP | Must |
| F13 | **My Needs + Sensory Dial** | Calm default; low-distraction UI | Lumen | Lumen | MVP | Must |
| F14 | Day integration | Tasks appear on Wavelength Day's Now/Next; Calm Harbor break link | Cross-app | Differentiate | V1 | Should |
| F15 | School/coach assignment | Coach assigns weekly goals; 504 export | B2B | Parity | V1 | Should |
| F16 | Moderated peer focus rooms (13+) | School- or coach-hosted rooms; no video, no chat, preset reactions only ("starting", "break", "done"); known-peer membership | Body doubling | Differentiate | V2 | Could |
| F17 | Watch haptic timer | Wrist timer + gentle taps | Discreet | Parity | V2 | Could |

★ Signature features: **Reward plan with fading (F6)** and **safe body doubling (F4/F5)**. The MVP has 13 features.

## 5. Core experience & key user flows
**Core loop:** pick a task → break it down (edit) → guess the time → start (alone, with the buddy, or co-working with a parent) → timer + optional movement break → done → estimate learned → reward per plan (fading) → "All done" screen.

**Flow 1: Onboarding (≤5 min)**
1. The Calm dial is preset. Age band and look (playful / neutral / teen).
2. Pick 2 templates (e.g., homework + morning).
3. Optional: set up a reward plan together. The app suggests "start rich, fade over 6 weeks", and the child picks 3 rewards from a non-food list.
4. Run the first task with the co-work mode.

**Flow 2: Core session (Sam, 13)**
1. Sam types "history project due Friday".
2. The AI proposes 6 steps. He deletes one and renames the first to "Pick 3 sources".
3. He guesses 20 min and starts with the buddy on (ambient rain) and notifications quieted.
4. At 25 min, a gentle "Keep going or break?" appears. He takes a 2-min stretch.
5. Done: "Took 32 min; guess next time?" His independence meter moves up. The reward plan is at "every 3 tasks", so no reward yet, only a calm "Started on your own ✓".

**Flow 3: Parent / coach view**
1. Lauren sees Mia's co-work session invite on her phone and taps "Join" (status only, no camera).
2. She sees a weekly summary.
3. The fading plan auto-advances. She gets a heads-up and can pause the fade if the week was hard (school change, illness).

**Flow 4: My Needs:** Dial; timer style; sound; buddy style or off; input modes; notification quieting; privacy sharing.

**Flow 5: Billing:** Fair-billing charter. The one-tap cancel shown in the paywall is the explicit remedy for Joon's trial complaints [V2].

**Information architecture:** Now (current task/timer) · My tasks · Plan (rewards and independence) · Breaks. Adult: Summary · Templates · Plan approval.

**Session design:** Timers are chosen, not imposed. There is a "keep going or break?" check at a user-set interval (default 20 min for 7–12, 30 min for teens). Every session ends on "All done".

## 6. Inclusive, accessible & sensory design spec
**Sensory Dial**
| Level | Motion | Sound | Color | Feedback | Density |
|---|---|---|---|---|---|
| **Calm (default)** | Timer shrinks smoothly; no pulsing | Silent end cue (haptic + visual) | Muted | "✓ Done" | Current step only |
| **Balanced** | Gentle | Soft chime | Moderate | Short celebration | Current + next step |
| **Lively** | Animated buddy (no flashing) | Music (focus playlists) | Vivid | Longer, skippable | Full list |

**ADHD-specific low-distraction rules:** one primary button per screen; no badges on the child's app icon; notification text never shames ("Ready when you are" instead of "You're late!"); no infinite lists (show 5 tasks max, the rest under "later").

**Input modes:** Tap; voice (dictate tasks; fallback to typing or picture chips); keyboard; switch (scan steps, start/stop); eye gaze (dwell start/stop); AAC (Voice symbols for "start", "break", "done"). Reordering uses tap-to-pick/tap-to-place, with no drag required.

**Targets:** ≥1.5 cm for 7–12; platform standard for teens. Start/Done buttons ≥2 cm.

**Reading:** Picture steps for pre- and early readers; TTS on all steps; BDA typography; reading dial.

**Audio:** Separate buddy ambience, cue and voice channels. Visual and haptic twins for all cues.

**Age-respectful themes:** Playful (7–10), Neutral, Teen (minimal, dark mode, planner-like).

**Lumen principles: acceptance criteria**
| P | Criterion |
|---|---|
| P1 | Calm default; no pulsing timers |
| P2 | End cues visual and haptic; sound optional |
| P3 | Now screen fixed; steps shown the same way every time |
| P4 | No drag; ≥1.5 cm targets |
| P5 | Literal step text; TTS |
| P6 | BDA text |
| P7 | Tap, voice, keyboard, switch, gaze, AAC |
| P8 | Unfinished tasks → "later", never red/overdue |
| P9 | "All done" ending; no autoplay of the next task |
| P10 | Steps and guess always visible during a task |
| P11 | Timers optional; "more time" always allowed |
| P12 | My Needs portable |
| P13 | Teen theme |
| P14 | ≤5-min setup; co-work mode; weekly summary |
| P15 | **Reward fading plan mandatory for any reward use**; no loss framing; no paid currency |
| P16 | ADHD framed as a difference; no "lazy/focus harder" language; ND board review |
| P17 | "Organization and focus tools built on EF strategies"; never "treats ADHD" |
| P18 | Buddy is not a companion; no chat; no emotion AI |

**Target Lumen score:** ≥23/24.

## 7. AI specification & guardrails
**What AI does**
- **Task breakdown:** An LLM with an age-banded style guide makes steps concrete and literal, with the first step ≤2 minutes. Steps are always editable, and the child's edits train *their* preferences (stored locally), not a global model.
- **Estimate learning:** A simple per-user regression on the child's own history (no LLM).
- **Reward plan suggestions:** Rule-based fading schedules authored by clinicians and ND advisors (no LLM).

**What AI does not do:** No chat persona; the buddy is non-conversational. No emotion or attention inference from camera or voice. No "focus scoring" of the child. No ADHD diagnosis or symptom tracking. No homework answers (breakdown only; it won't write the essay).

**Safety policies**
- **Academic integrity:** The breakdown refuses "do my homework" requests and redirects to steps.
- **Distress:** A self-report "I'm overwhelmed" button links to Calm Harbor, with an option to tell a parent.
- **Disclosure:** A child-readable "Breakdown ideas are made by a computer. You're the boss of your list."

**Evaluation:** 500 task prompts across ages, rated by teachers and ADHD coaches for concreteness, first-step size and reading level (≥90% usable). Red-team tests: essay-writing requests, unsafe tasks ("how to sneak out"), self-harm phrases (route to support). Monthly human sampling of 2% of breakdowns with consent.

**Cost [E]:** ≈$0.001–0.003 per breakdown; templates cover about 50% of tasks with no call.

## 8. Data, privacy & compliance
| Data | Why | Retention | Where |
|---|---|---|---|
| Tasks, steps, time estimates/actuals | Core, estimate learning | 12 months [E] | Device + cloud sync |
| Reward plan & independence counts | Plan | Account life | Cloud |
| Co-work session status | Presence | Not stored after session | Real-time only |
| AI prompts | Breakdown | Zero-retention processor; names stripped | Cloud |

- **COPPA 2025:** VPC; no third-party ads/SDKs. Co-work presence is caregiver-only, so no child-to-stranger contact.
- **UK AADC:** no nudge techniques; notifications opt-in; profiling off.
- **KOSA / state codes (pending/enacted):** no compulsive-use features (no streak loss, no infinite feeds) [V2].
- **FERPA:** coach/school licences.
- **HIPAA:** clinician/coach-under-practice licence with BAA.
- **FDA/FTC:** no ADHD treatment or symptom-improvement claims. EndeavorRx shows the FDA route and its costs [V2]. We stay in education and organization claims.

## 9. Monetization & go-to-market
| Tier | Price [E] | Benchmark |
|---|---|---|
| Free | 3 active tasks, timer, breakdown ×5/week | Goblin Tools free web [V2] |
| Focus Crew | $6.99/mo or $59/yr | Joon $89.99/yr [V2]; Brili $49.99/yr [V2]; Tiimo $79.99/yr [V2] |
| Family plan | ≈$19/mo, all apps | — |
| Coach/school | $15–25/student/yr | — |

- **Channels:** ADHD parent communities, ADHD coaches, school 504 coordinators, ESA marketplaces, pediatric practices (patient handouts; no Rx). Positioning: "the ADHD app that plans its own fade-out".
- **ASO:** ADHD app for kids, homework timer, visual timer, chore chart ADHD, body doubling, task breakdown.
- **Launch:** US, UK.

## 10. Success metrics
- **North star:** Weekly self-started tasks per active learner.
- **Input metrics:** Tasks broken down per week; % of AI steps edited by the child (a signal of agency); estimate accuracy improvement; co-work sessions per week; % of learners on a fading plan past stage 2.
- **Guardrails:**
  - Engagement **after rewards fade** stays ≥70% of the pre-fade level (the Joon-decay test)
  - Sensory Comfort ≥4/5
  - Parent "nagging" self-report down
  - 0 billing complaints
  - 0 homework-answer outputs in audits
- **Outcomes:** Parent- and child-rated homework conflict; a validated EF rating scale used by the clinical panel [M]; child self-efficacy. **Evidence:** E3 → E2 pilot with an ADHD clinic/university.
- **Retention [E]:** D30 40%; week-8 active ≥30% (vs. Joon-style decay).

## 11. Validation plan
| # | Assumption | Experiment | Sample | Success | Kill |
|---|---|---|---|---|---|
| 1 | Engagement lasts beyond 4 weeks without escalating rewards | 6-week diary study: paper Focus Crew kit (breakdown cards, visual timer, co-signed fading plan) vs. families' current approach | 20 families (40 total with comparison) | Week-6 task starts ≥70% of week-2 level in the Focus Crew arm; parent nagging down ≥1 point | <50% retention of starts → rethink motivation model |
| 2 | Children accept editing AI breakdowns | WoZ breakdown (human types steps) in Figma | 15 children 9–15 | ≥60% edit at least 1 step; usefulness ≥4/5 | — |
| 3 | Caregiver co-work mode is used | Concierge: parents text "starting" and sit with the child (remote or same room) | 12 families, 2 weeks | ≥3 co-work sessions per week | <1/week → deprioritize |
| 4 | Ambient buddy isn't perceived as a "friend" | Interviews after Figma buddy exposure | 12 children | ≥80% describe it as a tool/helper, not a friend | Otherwise, remove the figure and keep ambience only |
| 5 | Sensory A/B | Lumen protocol | 20 | Comfort +1 for ND | — |

**Mapping:** WP2 diaries, WP4 (the Focus Crew task-breakdown WoZ is named in the plan), WP5.

## 12. Build handoff
**Epic A: Breakdown**
- *Given* a task prompt, *when* AI returns steps, *then* the first step is displayed with an edit affordance and nothing is saved until the child taps "Use these steps".
- *Given* a prompt "write my essay", *then* the system returns steps (outline, find quotes…) and no essay text.

**Epic B: Timer & estimates.** *Given* a guess of 10 min and an actual of 18, *then* the next suggestion shows "18?" in neutral wording, with no red or warning color.

**Epic C: Reward plan**
- *Given* a co-signed plan at stage 1, *when* the learner meets the independence threshold for 2 weeks, *then* the app proposes stage 2 to both parent and child and requires the child's agreement.
- *Given* any reward display, *then* no loss framing ("you'll lose…") appears anywhere.

**Epic D: Co-work.** *Given* a parent joins, *then* both devices show a shared timer. No audio or video is transmitted, and the session ends for both on Done.

**Non-functional requirements:** Offline tasks/timers; OS Focus integration (iOS Focus filters, Android DND) with consent; WCAG 2.2 AA; iOS/Android/web.

**QA focus**
- **AT matrix:** VoiceOver/TalkBack (timer announcements at user-set intervals only), Switch Control/Access, Eye Tracking, Voice Control, Dynamic Type XXL, Reduce Motion, Full Keyboard Access.
- **Sensory A/B.**
- **AI red-team** (homework answers, unsafe tasks).
- **COPPA:** co-work presence limited to linked caregivers.
- **Billing:** trial reminder T-3, cancel in 1 tap.

**Platform dependencies:** Lumen, Circle (co-work presence, plan approvals), AI orchestration, Day integration.

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Fading reduces engagement | Med | High | Co-signed plan, pause option, independence meter; test in diary study |
| Buddy drifts into companion territory | Low | High | No name/feelings/chat; ND board and child-safety review |
| Commoditized by free AI (Goblin, chatbots) | High | Med | Child-specific design, co-work, fading plan, team features |
| Parents want stronger reward systems | Med | Med | Allow rich stage 1; explain evidence; no compliance framing |
| Homework-integrity concerns from schools | Med | Med | Breakdown-only policy, audits |

**Open questions:** Should Focus Crew and Day merge for 7–10s? Is peer body doubling for 13+ worth the safeguarding load? How do we handle medication-timing reminders? (Currently out of scope: no health tracking.)

## 14. Sources
- [V2] Joon pricing and complaints: https://www.choosingtherapy.com/joon-app-review/ ; https://www.commonsensemedia.org/app-reviews/joon-kids-chore-list-chart (via raw 04)
- [V2] Tiimo: https://lifestack.ai/blog/tiimo-pricing ; [V] rating: https://www.educationalappstore.com/app/tiimo
- [V] Goally reviews: https://justuseapp.com/en/app/1262461227/goally/reviews ; Play listing: https://play.google.com/store/apps/details?id=com.mygoally.mygoally
- [V] Brili: https://play.google.com/store/apps/details?id=co.brili.routines&hl=en-US
- [V2] Goblin Tools: https://goblin.tools/About ; https://blogs.qub.ac.uk/studentatguide/2025/02/19/introducing-goblin-tools-ai-powered-support-for-neurodivergent-thinkers/
- [V2] Forest: studio raw file 03
- [V2] EndeavorRx: https://www.biopharmadive.com/news/akili-sell-34m-virtual-therapeutics-digital/717576/ ; https://www.managedhealthcareexecutive.com/view/fda-expands-akili-s-endeavorrx-game-based-digital-therapy-for-adhd-eligibility-to-ages-8-17
- [V2] CDC ADHD data: https://www.cdc.gov/adhd/data/index.html
- [M] Focusmate, Structured, Habitica, Inflow details; Deci, Koestner & Ryan (1999); EndeavorRx trial results and price: **re-verify in WP1** (search quota exhausted this session).

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (shares EN-05 with Mission Control / Study Squad) |
| **Ships in** | Wavelength app (S7) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 81/100 [I] |
| **Consumes engines** | EN-05, EN-11 |
| **Studio features used** | SX-19, SX-28 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = F1, F2, F4, F5, F6.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| FC-E1 | **Teacher check-in card** | A daily one-tap, child-visible school–home note, with no behaviour scoring. |
| FC-E2 | **Homework-conflict scripts** | Co-regulation scripts for parents at the hardest moment (SX-28). |

### 15.3 New validation question
6-week engagement curve with a reward-fading plan (n=20 families).

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 5 | 4 | 5 | 3 | 3 | 4 | 3 | 5 |

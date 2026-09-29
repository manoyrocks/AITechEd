# Mission Control: App Strategy & Product Specification

> **Venture:** Questwise · **App #:** 7/7 · **Ages:** 8–12 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/02-questwise-tweens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Questwise index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A visual homework-and-routines planner that turns assignments into missions with steps, calm focus timers and movement breaks, so tweens build independence with the family, not under surveillance. |
| **Primary user / buyer** | User: 8–12, especially ADHD, autistic and anxious kids. Buyer: parent; ESA family (esp. disability awards); microschool guide. |
| **Core job-to-be-done** | "When I have homework and I don't know where to start, I want to see small steps and a calm way to get going, so I can finish on my own without Mom reminding me ten times." |
| **Category on the stores** | Education / Productivity (iOS Kids 9–11) · Google Play Education, Families |
| **Top competitors** | Joon, Goally, Brili, Tiimo, Forest, myHomework, Habitica, Greenlight (chores), OurHome |
| **Our wedge** | 1) Built for tweens owning the plan (child edits, parent supports), vs. parent-run quest apps (Joon) and teen/adult planners (Tiimo). 2) AI step breakdown that the child edits, tied to real assignments and to Sage/Math Realms/Read Rangers. 3) Gentle progress with pause days: no dying trees (Forest), no pets that suffer (Joon), no paid rewards. |
| **Business model** | In Questwise Family ($99/yr). Free tier: planner + 3 missions/day. ESA and microschool licences. |
| **North-star metric** | Weekly missions started *by the child* without a parent prompt and completed (self-initiated completions). |
| **MVP candidate?** | **Later** (Year 2 per vision); diary study now. |

## 2. Problem & users

**Problem statement.** Tweens are asked to manage homework independently for the first time; many, especially the 11.4% of US 3–17-year-olds ever diagnosed with ADHD [V raw paper §3], struggle with task initiation, time blindness and transitions. The tools either treat kids as reward-economy participants run by parents or are adult planners.
- **Joon** ($12.99/mo or $89.99/yr): "engagement drops after 4 to 8 weeks"; users report being "charged even after canceling the free trial"; "most teenagers find virtual pets childish" [V2 ChoosingTherapy/timily].
- **Goally** (tablet $199–369 + $15–20/mo): "Setup takes hours. App crashes. Routines vanish between the parent and child devices" [V2 raw 04].
- **Tiimo** (2025 iPhone App of the Year) is calm and ND-first but aimed at 13+; $79.99/yr, family plan $119.99/yr for 5 [V2 lifestack; raw 04].
- **Forest**: the tree dies if you leave; easy to bypass; novelty wears off [V2/M raw 03].
- **Brili** adapts timers to actual time left ($49.99/yr) [V raw 04].
- Lumen principle: executive-function tools must be predictable and shame-free; Finch "doesn't punish you for missing a day" [V2 raw 03].

**Personas**

| Persona | Snapshot | Needs | Pain |
|---|---|---|---|
| **Aiden, 9, ADHD** | Starts strong, loses track, meltdowns at homework | Tiny first step; movement breaks; visible time | Nagging; long lists; losing streaks |
| **Zara, 12, autistic** | Needs predictability; hates surprise changes | Stable routine board; warnings before transitions | Sudden alarms; loud rewards |
| **Lily, 11, anxious perfectionist** | Over-plans, freezes | Realistic time estimates, "good enough" checkpoints | Red overdue badges |
| **Nicole, parent** | Works; homework battles | See what's done without nagging | Joon/Goally setup and admin burden |
| **Mr. Ortiz, guide** | Assigns weekly work | Kids plan their week; he sees status | Kids lose paper planners |

**Needs & wants**

| Need | Evidence | Response |
|---|---|---|
| Start tasks | Goblin Tools "Magic ToDo" popularity [V raw 04] | AI breakdown into first tiny step, child-edited |
| Low parent admin | Goally/Joon admin complaints [V/V2] | 5-min setup; school-assignment import V1; templates |
| No punishment | Finch/Tiimo praise [V2] | Gentle progress; pause days; no loss framing |
| Lasting motivation | Joon novelty decay 4–8 weeks [V2] | Reward fading plan; ownership and mastery, not pets |
| Time awareness | Brili adaptive timer [V] | Visual time bars; estimate vs. actual reflection |

## 3. Competitive feature benchmark

| App | Publisher | Signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Joon** | Joon | Leading ADHD kids' chore game [M] | Free core; $12.99/mo or $89.99/yr [V2] | 4.7 iOS [V2] | Pet ("Doter") motivation; parent-assigned quests | Novelty fades 4–8 wks; trial billing; parent admin [V2] | Game visuals; notifications | ChoosingTherapy; raw 04 |
| **Goally** | Goally | Device + app system [V2] | Tablet $199–369 + $15–20/mo [V2] | n/a | Locked-down device; visual routines; AAC | Setup hours; sync bugs; crashes [V2] | Visual schedules; video modeling | raw 04 |
| **Brili Routines** | Brili | Niche ND routine app [V] | $7.99/mo; $49.99/yr [V] | n/a | Adaptive routine timers | Small team, less content [V] | Visual/audio prompts | Google Play (raw 04) |
| **Tiimo** | Tiimo | 2025 iPhone App of the Year [V raw 04] | $7.99/mo, $79.99/yr; family $119.99/yr (5) [V2] | n/a | Calm visual timeline; AI breakdown; Watch | iOS-centric; 13+ in practice [V2] | ND co-designed; calm | lifestack; raw 04 |
| **Forest** | Seekrtech | 4.8 from 1M+ ratings [V2 raw 03] | Free; Plus $5.99/mo or $32.49–35.99/yr [V2] | 4.8 | Grow a tree while focusing | Tree dies if you leave; bypassable; novelty fades [V2/M] | Loss framing | Apple listing; raw 03 |
| **myHomework** | Instin | Long-standing student planner [M] | Free; ad-free $4.99/yr [V2] | n/a | Simple assignment tracking by class | Plain; ads in free [I] | Text lists | Common Sense; Apple |
| **Habitica** | HabitRPG | Gamified task RPG [M] | Free; ≈£46.49/yr [V2] | n/a | RPG party accountability | Under-13 needs parental permission; party chat [V2] | Text-heavy; damage for missed dailies [M] | Habitica wiki |
| **Greenlight** | Greenlight | Kids' debit card with chores [V2] | $5.99–19.98/mo [V2] | n/a | Chores tied to allowance | Fintech upsell; money for chores framing [I] | Standard | greenlight.com |

OurHome (original) was unpublished from Google Play in Sept 2023 and not updated since 2020 [V2 choresplit] — a reminder that family routine apps churn.

**Feature matrix**

| Feature | Joon | Goally | Brili | Tiimo | Forest | myHomework | Our decision |
|---|---|---|---|---|---|---|---|
| Visual step-by-step routines | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | **Parity** |
| AI task breakdown | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | **Improve** (child-edited, homework-aware) |
| Homework/assignment tracking | ◐ | ✗ | ✗ | ◐ | ✗ | ✓ | **Parity** |
| Focus timer | ◐ | ✓ | ✓ | ✓ | ✓ | ✗ | **Improve** (optional, calm, pausable) |
| Movement breaks | ✗ | ◐ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Virtual pet that suffers | ✓ | ✗ | ✗ | ✗ | ✓ (tree dies) | ✗ | **Reject**: loss framing |
| Parent-assigned rewards/tokens | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | **Reject** token economy; family-agreed celebrations only |
| Child owns the plan | ◐ | ✗ | ◐ | ✓ | ✓ | ✓ | **Differentiate** (for 8–12) |
| Parent view without nagging | ✓ | ✓ | ✓ | ◐ | ✗ | ✗ | **Improve** (no parent pings to child device) |
| Transition warnings | ◐ | ✓ | ✓ | ✓ | ✗ | ✗ | **Parity** |
| Android + web | ✓ | ◐ | ✓ | ◐ | ✓ | ✓ | **Parity** (plus Chromebook) |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| MC-01 | **Mission board** | Today / This week; each assignment a mission card with subject icon, due day, effort size | myHomework parity | Parity | MVP | Must |
| MC-02 | ⭐ **Step Splitter** | AI proposes 3–7 steps with a tiny first step; child edits, reorders (tap), deletes; "make it smaller" button | Goblin Tools pattern [V]; task initiation | Differentiate | MVP | Must |
| MC-03 | **Time estimate & reflect** | Child guesses minutes; after, sees actual vs. guess without judgment; learns own pace | Time blindness; Brili [V] | Improve | MVP | Must |
| MC-04 | ⭐ **Calm focus timer** | Optional visual time bar (not a countdown number by default), pausable, gentle end chime/haptic, no failure if you leave | Forest's loss framing rejected | Improve | MVP | Must |
| MC-05 | ⭐ **Movement & brain breaks** | 1–3 min break cards (stretch, wall push, breathing, water) between steps; child-chosen frequency | ADHD persona; Lumen calm corner | Differentiate | MVP | Must |
| MC-06 | **Family routine board** | Shared after-school/evening routine (snack → homework → free time) with Now/Next/Done | Visual schedules evidence [M raw 04] | Parity | MVP | Must |
| MC-07 | **Transition warnings** | "5 minutes until homework" with visual + haptic; child can snooze once | P3 | Lumen | MVP | Must |
| MC-08 | **Gentle progress** | Weekly goal ring; 2 pause days per week by default; no streak loss | P15 | Lumen | MVP | Must |
| MC-09 | **Parent glance view** | Done/in progress/needs help, in the parent's Guild Hub; no notifications to child's device from parents | Low admin; Goally burden [V2] | Improve | MVP | Must |
| MC-10 | **"I need help" button** | Child flags a mission; routes to Sage (for learning) or to parent card ("Priya wants help with…") | Links to Sage | Differentiate | MVP | Must |
| MC-11 | **Sensory Dial + themes** | Calm default for timers; "Space Ops" and "Minimal" themes | P1, P13 | Lumen | MVP | Must |
| MC-12 | **Reminders the child sets** | Child-chosen reminder times and styles (visual/audio/haptic) | Autonomy | Lumen | MVP | Should |
| MC-13 | Assignment import | Google Classroom/microschool guide assignments pulled in (with school consent) | Admin burden | Improve | V1 | Should |
| MC-14 | Plan-my-week | Sunday planning ritual: spread missions across days by energy | Lily persona | Differentiate | V1 | Should |
| MC-15 | Body-doubling with invited friend | Two invited friends see each other's "focusing" status (no chat, no camera) | ADHD body-doubling practice [M] | Differentiate | V1 | Could |
| MC-16 | Watch/wearable haptics | Gentle wrist nudges | Tiimo parity | Parity | V2 | Could |
| MC-17 | Guide week plans | Microschool guide sets weekly contract; kids plan it | Microschool channel | Parity | V1 | Should |

**MVP (when built) = MC-01 to MC-12 (12).** **Signature features:** MC-02 Step Splitter, MC-04 calm focus timer, MC-05 movement breaks.

## 5. Core experience & key user flows

**Core loop:** after-school transition warning → routine board (Now: homework) → pick mission → Step Splitter → first tiny step → optional focus bar → break card → next step → done → estimate reflection → free-time transition.

**Flow 1: Onboarding (≤5 min).** Parent VPC; picks a routine template (school night, weekend); invites co-parent. Child adds first mission by voice/typing/photo of the planner page; Step Splitter proposes steps; child edits; first step done within 5 minutes.

**Flow 2: Core homework session.**
1. 3:55 p.m. transition card: "Snack ends in 5 minutes. Next: homework." (visual + haptic).
2. Child opens mission "Spelling sentences". Step Splitter shows "1. Get pencil and list (1 min)…".
3. Child starts optional focus bar (15 min). Leaves app? Nothing dies; bar pauses.
4. Break card after step 3 (child-chosen: every 2 steps). 90-second stretch.
5. Done → "You guessed 20 min, it took 28. Maths usually takes you a bit longer. Want to plan more time next week?"

**Flow 3: Parent view.** Glance: 3/4 missions done; one "needs help" (with Sage link suggestion); weekly summary with one encouragement suggestion for the parent to say in person.

**Flow 4: My Needs.** Timer style (bar/number/none), break types, reminder modes, transition warning length, Dial, AAC symbols for steps (V1).

**Flow 5: Billing.** Questwise charter; free tier covers core planner forever.

**IA:** Today (routine + missions), Mission, Week, Breaks, My Needs; adult Guild Hub.

**Session design:** Missions sized 5–30 min; break every 2 steps default; designed ending "Mission complete, homework done for today → free time".

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial:** Calm (default for Mission Control since it's used at stressful moments): no animation; soft haptic cues; muted colours. Balanced: gentle bar fill animation; soft chime. Lively: rocket-launch animation on mission complete (skippable).

**Input modes:** tap; voice for adding missions/steps; typing; photo of a paper planner (optional; OCR with confirm); AAC/symbol step cards (V1); switch (V1).

**Targets:** ≥48 dp; reorder steps with up/down buttons (no drag required).

**Reading:** step text ≤8 words, icon + text + audio; grade 3; BDA typography.

**Time representations:** visual bar (default), analog-style disc, or number; time can be hidden entirely ("tell me when I'm done"). Never red "overdue" badges; overdue shows as "Still to do" in neutral colour.

**Audio/haptic:** separate sliders; every cue has visual and haptic twin; alarms capped and soft-attack.

**Age-respectful:** "Space Ops" (illustrated) and "Minimal" (clean, adult-planner look for 11–12s who find kid apps childish).

**Lumen acceptance criteria**

| P | Criterion |
|---|---|
| P1 | Calm default; Reduce Motion honoured |
| P2 | All reminders multi-modal; no sound-only cues |
| P3 | Routine board fixed; transition warnings always before changes |
| P4 | Reordering by tap |
| P5 | Steps ≤8 words + audio |
| P6 | BDA defaults |
| P7 | Voice + tap + typing to add missions |
| P8 | Leaving a focus session has no penalty |
| P9 | Designed end → free time |
| P10 | Current step always visible |
| P11 | Timers optional, pausable, hideable |
| P12 | Free accommodations |
| P13 | 2 themes |
| P14 | Parent setup ≤5 min; no parent pings on child device |
| P15 | Pause days; no loss framing; reward fading plan |
| P16 | ND panel review; no "fix focus" language |
| P17 | No "treats ADHD" claims (education, not treatment; FDA boundary) |
| P18 | No emotion inference from usage patterns |

**Target Lumen score:** 23/24.

## 7. AI specification & guardrails

- **AI does:** Step Splitter (LLM with a tween-specific template: first step ≤2 min, concrete verbs, ≤7 steps); time estimate priors from the child's own history (simple model); OCR for planner photos.
- **AI does not:** do the homework (routes learning help to Sage's Socratic policy); predict or label "focus problems", ADHD or mood; send nudges on its own schedule; profile attention for anyone.
- **Pedagogy/EF policy:** scaffold then fade: after a child edits 5 AI plans, Step Splitter starts by asking "What's your first step?" before suggesting; weekly reflection on estimates; child-chosen goals.
- **Safety:** tool not friend (no mascot that "misses you"); AI disclosure on breakdowns; distress escalation from self-report (e.g., typed "I hate myself, I can't do anything") → calm script, tell-a-grown-up button, parent alert, human review; no emotion recognition; no usage-based "mood" inference.
- **Evaluation:** breakdown quality rated by ND teachers/OTs (≥4/5); child edit rate (healthy: 30–60%); time-estimate improvement; red-team harmful step suggestions (e.g., unsafe tools).
- **Cost [E]:** ≈$0.002 per breakdown; <$0.10 per learner/month.

## 8. Data, privacy & compliance

Missions and steps, time estimates vs. actuals, routine board, reminders, "needs help" flags. Retention 12 months rolling; export. **Sensitive inference ban:** we do not derive or store attention/ADHD indicators, because such inferences are health-adjacent and would create FDA and privacy risk. COPPA 2025 (VPC; AI training off; separate consent for classroom import); FERPA/SOPIPA for Classroom import (V1); state design codes (no compulsive-use nudges); UK AADC. Kids category and Families policy; notifications to child device only for child-set reminders.

## 9. Monetization & go-to-market

- **Benchmarks:** Joon $89.99/yr; Brili $49.99/yr; Tiimo $79.99/yr (family $119.99/yr); Goally $199–369 device + $180–240/yr; Forest Plus ≈$32–36/yr; myHomework $4.99/yr.
- **Ours:** in Questwise Family ($99/yr for 3 kids); Mission Control-only $4/mo test; free tier generous (planner + 3 missions/day).
- **Channels:** ESA disability-award families (e.g., FL FES-UA [M]); ADHD parent communities (via paid ND co-designers and CHADD-style partner events [I]); microschools (weekly contracts); OTs and ed therapists (V1 clinician share view, education not treatment).
- **ASO:** "homework planner for kids", "ADHD kids routine app", "visual schedule kids", "focus timer for kids no punishment".

## 10. Success metrics

- **North-star:** weekly self-initiated mission completions (target ≥4 per active child).
- **Inputs:** % missions with child-edited steps; break usage; transition warnings acknowledged; parent glance opens (vs. parent nag reports).
- **Guardrails:** parent-reported homework conflict ↓ (target −30% at 6 weeks); Sensory Comfort ≥4/5; no billing complaints; week-8 retention not collapsing (Joon's 4–8 week decay benchmark: target ≥60% of week-2 actives still active at week 8).
- **Outcomes:** EF self-report (child-friendly scale) and parent BRIEF-style informal checklist [M] as exploratory, not claims.
- **Retention:** D30 30%, W8/W2 ≥60% [E].

## 11. Validation plan

**Riskiest assumptions:**
1. Tweens will adopt a planner themselves rather than have a parent run it (vision).
2. Motivation lasts without pets/tokens (vs. Joon decay).
3. AI breakdowns are good enough for ND kids without clinician setup.

| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | 2-week diary study: paper mission board vs. Figma prototype (vision test) | 20 families (≥10 ADHD/autistic) | ≥60% of missions started by child without prompt in week 2 | <35% |
| E2 | Wizard-of-Oz Step Splitter (researcher writes breakdowns from template in real time) | 15 kids | ≥70% keep or lightly edit; first-step start within 2 min | <50% |
| E3 | 8-week extension of E1 with no tokens | 10 families | W8/W2 activity ≥60% | <40% |
| E4 | Parent WTP + ESA disability-award interviews | 12 parents | ≥50% would pay ≥$4/mo or use ESA | <25% |

Mapping: E1, E3 → WP2/WP4; E2 → WP4; E4 → WP5.

## 12. Build handoff

**Epic A: Missions** — **AC-A1:** Given a child says "math worksheet due Thursday", When captured, Then a mission card with subject, due day and an editable title is created and confirmed aloud.

**Epic B: Step Splitter** — **AC-B1:** Given a mission, When the child taps "Split it", Then 3–7 steps appear with a first step estimated ≤2 min, all editable, reorderable by buttons. **AC-B2:** Given the child has edited ≥5 plans, When splitting, Then the app first asks the child for their first step.

**Epic C: Focus & breaks** — **AC-C1:** Given a focus bar is running, When the child leaves the app, Then the bar pauses and no negative message is shown on return. **AC-C2:** Given break frequency "every 2 steps", When step 2 completes, Then a break card appears with a skip option.

**Epic D: Routine board & transitions** — **AC-D1:** Given a routine change at 4:00, When it's 3:55, Then a visual + haptic warning appears with one snooze.

**Epic E: Parent glance** — **AC-E1:** Given a parent views the Hub, When missions update, Then status is visible, and the parent cannot send push notifications to the child device.

**NFRs:** local-first data with sync (routines must work offline); iOS, Android, web/Chromebook; WCAG 2.2 AA; EN/ES; notification reliability ≥99%.

**QA focus:** AT matrix (VoiceOver, TalkBack, Switch, Voice Control for adding missions); sensory A/B (Calm vs. Balanced timers); AI cases (unsafe steps, doing-the-homework requests routed to Sage, distress phrases); COPPA (no inference storage, consent for Classroom import); billing.

**Platform dependencies:** Lumen (Now/Next/Done, calm corner), My Needs, AI orchestration, privacy stack, evidence engine, Guild Hub, Sage handoff API.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Novelty decay like Joon | High | High | Ownership, reflection, fading plan; E3 |
| Parents want control/rewards | Medium | Medium | Family agreements feature (non-token celebrations) |
| Health-claim creep in marketing | Medium | High | Claims register (P17); "education, not treatment" |
| Notification fatigue | Medium | Medium | Child-set reminders only; caps |

**Open questions:** Should Mission Control be the Questwise "home screen" linking all apps? Classroom import scope for microschools without an LMS? Wearable support priority?

## 14. Sources
- [V2] Joon pricing and complaints: https://www.choosingtherapy.com/joon-app-review/ · https://timily.app/guides/joon-app-review/
- [V via raw 04] Goally, Brili, Tiimo, Goblin Tools rows: research/raw/04-neurodivergent-and-inclusive-ux.md
- [V2] Tiimo 2026 pricing: https://lifestack.ai/blog/tiimo-pricing
- [V2] Forest pricing: https://apps.apple.com/us/app/forest-focus-for-productivity/id866450515 · https://calmevo.com/forest-app-review/
- [V2] myHomework: https://www.commonsensemedia.org/app-reviews/myhomework-student-planner · https://apps.apple.com/us/app/myhomework-student-planner/id303490844
- [V2] Habitica children policy: https://habitica.fandom.com/wiki/Children_Using_Habitica
- [V2] Greenlight pricing: https://greenlight.com/chores-and-allowance-app-for-kids · https://vaultleap.com/blog/greenlight-fees-explained-2026
- [V2] OurHome status: https://choresplit.com/compare/ourhome
- [V via raw paper] ADHD prevalence 11.4%: docs/01-research-paper.md §3
- [M] Body-doubling practice; BRIEF-style EF checklists; CHADD partnerships

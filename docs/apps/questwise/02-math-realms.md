# Math Realms: App Strategy & Product Specification

> **Venture:** Questwise · **App #:** 2/7 · **Ages:** 8–12 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/02-questwise-tweens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Questwise index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | An explorable math world where regions unlock through mastery, not money or minutes, with no timers and Sage as the in-world guide. |
| **Primary user / buyer** | User: child 8–12 (grades 3–7). Buyer: parent, ESA-funded family, microschool/co-op, later classroom teacher. |
| **Core job-to-be-done** | "When I practise math, I want it to feel like an adventure where I'm getting stronger, so I can keep going without feeling rushed, judged or out-bought by kids with paid pets." |
| **Category on the stores** | Education (iOS Kids 9–11) · Google Play Education / Families |
| **Top competitors (by downloads / revenue)** | Prodigy Math, IXL, SplashLearn, Khan Academy, DreamBox, Zearn, Beast Academy, DragonBox |
| **Our wedge** | 1) Earned-never-bought: cosmetic rewards from mastery only, zero paid currencies (vs. Prodigy membership gear). 2) Forgiving mastery that never drops your score for one mistake (vs. IXL SmartScore). 3) First-class paths for struggling, dyslexic and ADHD learners (vs. Beast Academy), with screen-reader math. |
| **Business model** | Part of the Questwise family plan (≈$12/mo, $99/yr, 3 kids). Free tier: 1 full region. ESA and microschool licences. |
| **North-star metric** | Weekly mastered skills per active learner (venture north-star). |
| **MVP candidate?** | **Yes**. Year-1 MVP with Sage Tutor. |

## 2. Problem & users

**Problem statement.** Game-based math for tweens either monetises the child or punishes mistakes.
- **Prodigy:** advocacy groups told the FTC the home version shows "up to four times as many advertisements than math questions" and pushes a paid version up to $107/yr [V NBC/EdWeek]. More than 95% of registered users don't pay, per Prodigy [V2 NBC]. Parents describe a "constant battle" [V raw 03]. 2026 tiers run $58.95–$118.95/yr [V2 brighterly].
- **IXL:** "one wrong answer near 100 can erase an hour of progress" [V2 nibble-app]; students call SmartScore drops "rage-inducing" [M raw 03].
- **Beast Academy:** "does not fit kids who have a hard time with math" [V raw 03].
- **Opportunity:** ~70% of 5–13-year-olds want to learn creative subjects in Minecraft/Roblox-style worlds [V2 raw 03], but those worlds have no academic loop.

**Personas**

| Persona | Snapshot | Needs | Pain today |
|---|---|---|---|
| **Aiden, 9, ADHD** | Loves novelty; drops off after a week | Short quests, movement breaks, visible growth | Prodigy battles pull him into shops; long IXL sets |
| **Priya, 11, dyslexic** | Understands concepts; word problems stall | Read-aloud, no timers, voice answers | Timed drills; dense text |
| **Maya, 10, math-anxious** | Cries over fractions | Low-stakes practice, no public scores | IXL score drops; leaderboards |
| **Nicole, 41, parent** | Wants learning, not upsells | Proof of progress; fair price | "My kid wants the paid pet" |
| **Mr. Ortiz, microschool guide** | 14 mixed-age kids | Mastery map across grades, low prep | Six disconnected tools |

**Needs & wants**

| Need | Evidence | How Math Realms addresses it |
|---|---|---|
| Fun without pay-to-win | Prodigy FTC complaint [V] | All rewards cosmetic and earned; no store for kids |
| Mistakes without punishment | IXL SmartScore asymmetry [V2] | Evidence-weighted mastery; a mistake adds a review, never removes progress |
| Support for strugglers | Beast Academy gap [V] | Scaffold tracks, manipulatives, read-aloud, Sage hints |
| Proof parents trust | Badges distrusted [V raw 03] | "What I can do now" skill statements with examples |
| Game worlds | 70% want Roblox/Minecraft-style learning [V2] | Explorable regions, building your own base from mastered skills |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Prodigy Math** | Prodigy Education | US iOS 1.5–2.5M/yr [E raw 02]; >95% free users [V2] | Core $58.95/yr, Plus $88.95, Ultra $118.95 [V2] | 4.8 (≈247K iOS) [V2 raw 02]; Trustpilot 3.8 | RPG battles; adaptive; free at school | Pay-to-win pets/gear; ads for membership; "more game than math" [V] | Read-aloud of questions; VO limited; high sensory [V2 raw 02] | NBC; brighterly; raw 02/03 |
| **IXL** | IXL Learning | Large K-12 footprint [M] | $79–159/yr family; +≈$4/mo per extra child [V2] | n/a | Coverage; diagnostics; parent reports | SmartScore drops; "busywork" [V2/M] | Text-heavy; score anxiety | nibble-app; brighterly |
| **SplashLearn** | StudyPad | 7.5M+ iOS downloads [V2] | ≈$7.49–11.99/mo [V2] | 4.5 (32K iOS); Trustpilot 2.6 [V2] | Bright games K–5 | Billing and subscription complaints [V2] | Busy visuals [I] | Apple listing; Trustpilot |
| **Khan Academy** | Khan Academy | 10M+ Play; ~33M lifetime [V2 raw 01] | Free; Khanmigo $4/mo | 4.1–4.7 [V2] | Free mastery; trusted | Dry for younger kids; grindy [M] | "Fully accessible with VO" [V2] | raw 01/02 |
| **DreamBox Math** | Discovery Education | School-heavy [M] | Family $149.95/yr or $19.95/mo; individual $99.95/yr [V2] | n/a | Intelligent adaptivity; manipulatives | Price; K–8 only | Drag-heavy manipulatives [M] | dreambox.com pricing |
| **Zearn** | Zearn (non-profit) | Used by 1 in 4 US elementary students [V2] | Free for teachers/classrooms | n/a | Free; video + practice aligned to curriculum | Classroom-first; little for home [I] | Captioned videos [M] | zearn.org |
| **Beast Academy Online** | AoPS | Gifted-community favourite [V] | $99.99/yr; siblings $64.99 [V2] | n/a | Rigorous, comic-based, fun | Loses struggling learners [V] | Comic text density | brighterly; Davidson forum |
| **DragonBox** | Kahoot! Group | Premium algebra/geometry series [M] | Paid apps / Kahoot!+ bundle [M] | n/a | Algebra intuition through puzzles | Short; limited scope [M] | Drag-only [M] | [M] |

**Feature matrix**

| Feature | Prodigy | IXL | SplashLearn | Khan | DreamBox | Beast Ac. | Our decision |
|---|---|---|---|---|---|---|---|
| Explorable game world | ✓ | ✗ | ◐ | ✗ | ◐ | ✗ | **Parity** |
| Adaptive placement | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ | **Parity** |
| Mastery gating of progress | ◐ | ✓ | ◐ | ✓ | ✓ | ✓ | **Improve** (evidence-weighted, forgiving) |
| Score drops on errors | ✗ | ✓ | ✗ | ◐ | ✗ | ✗ | **Reject**: P8 |
| Paid gear/pets/currencies | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject**: pay-to-win |
| Timed battles/drills | ◐ | ✗ | ◐ | ✗ | ✗ | ✗ | **Reject**: P11 |
| Virtual manipulatives | ◐ | ◐ | ✓ | ◐ | ✓ | ◐ | **Improve** (tap alternatives to every drag) |
| Built-in tutor | ✗ | ◐ (explanations) | ✗ | ✓ (Khanmigo) | ✗ | ✗ | **Differentiate** (Sage in-world) |
| Open-ended "prove it" tasks | ✗ | ✗ | ✗ | ✗ | ◐ | ✓ | **Differentiate** |
| Public leaderboards | ◐ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject**: social comparison |
| Parent/teacher dashboard | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Parity** (plain language) |
| Screen-reader math | ✗ | ◐ | ✗ | ✓ | ✗ | ✗ | **Differentiate** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| MR-01 | **Placement quest** | 10–15 min story-framed adaptive placement, no timer, can pause | Parity with IXL/DreamBox diagnostics | Parity | MVP | Must |
| MR-02 | ⭐ **Mastery-gated regions** | Fraction Forest, Ratio River, Place-Value Peaks, etc. A region's gate opens when its skill nodes reach mastery | Vision card; mastery learning | Differentiate | MVP | Must |
| MR-03 | ⭐ **Forgiving mastery model** | Bayesian knowledge-tracing-style estimate: errors add a review item and lower confidence softly; visible progress never decreases | IXL asymmetry complaint [V2] | Differentiate | MVP | Must |
| MR-04 | **Knowledge-graph engine** | Skills graph (grades 2–7, CCSS + TEKS) choosing the next problem and spaced reviews | Parity with adaptive leaders | Parity | MVP | Must |
| MR-05 | ⭐ **Earned-never-bought rewards** | Cosmetic items and base-building blocks unlocked only by mastered skills; no currency to buy | Prodigy pay-to-win [V] | Differentiate | MVP | Must |
| MR-06 | **Tap-first manipulatives** | Fraction bars, number lines, area models, base-ten blocks: every drag has tap-select-tap-place | WCAG 2.5.7; P4 | Lumen | MVP | Must |
| MR-07 | **Sage in-world guide** | Hint ladder (from Sage Tutor) available on every problem, with the verified math gate | Khanmigo parity; vision | Differentiate | MVP | Must |
| MR-08 | **Read-aloud word problems** | TTS with highlighting; math spoken correctly; glossary | Priya persona; P5 | Lumen | MVP | Must |
| MR-09 | **"Prove it" mode** | Open tasks: explain or show why (draw, voice, choose-a-reason); teacher/AI rubric | Beast Academy rigor, reasoning focus | Differentiate | MVP | Should |
| MR-10 | **Quest length & designed endings** | Quests of 5–8 problems (≈10 min); end at a camp screen; daily default 25 min | P9; ADHD persona | Lumen | MVP | Must |
| MR-11 | **Parent & guide mastery map** | "What I can do now" statements, skills in progress, time, hints used | Proof parents trust | Parity | MVP | Must |
| MR-12 | **Sensory Dial + two themes** | Calm/Balanced/Lively; "Storybook" and "Blueprint" themes | P1, P13 | Lumen | MVP | Must |
| MR-13 | Guild co-op quests | Invited friends/siblings solve complementary halves of a puzzle; no chat, preset signals | Vision principle 3 | Differentiate | V1 | Should |
| MR-14 | Build-your-base | Base grows with mastered skills (a place-value tower, a fraction garden) | Minecraft appetite [V2] | Differentiate | V1 | Should |
| MR-15 | Movement breaks | Optional 60-s "stretch quests" between quests | ADHD persona; Joon/Goally pattern | Lumen | V1 | Should |
| MR-16 | Educator assignments | Guide assigns a skill; kids see it as a "commission" quest | Microschool need | Parity | V1 | Should |
| MR-17 | Spanish | Full UI and TTS | ESA states [I] | Improve | V1 | Should |
| MR-18 | Algebra readiness realm | Pre-algebra and equations (DragonBox-like intuition) | Grade 6–7 coverage | Parity | V2 | Could |
| MR-19 | Printable offline quests | QR-linked paper quests logged on return | Phone bans; low-device homes | Improve | V2 | Could |

**MVP = MR-01 to MR-12 (12).** **Signature features:** MR-02 mastery-gated regions, MR-03 forgiving mastery, MR-05 earned-never-bought.

## 5. Core experience & key user flows

**Core loop:** open → camp screen (Now/Next/Done) → choose quest in unlocked region → 5–8 problems with manipulatives and optional Sage → mastery update and cosmetic unlock → camp → natural end.

**Flow 1: Onboarding (≤5 min to first value)**
1. Parent creates the family account (VPC) and adds the child; My Needs imports if present.
2. Child picks a theme, avatar (non-human "Ranger" styles, no purchase) and Dial level.
3. First 3 placement problems framed as "map the forest"; the first region lights up by minute 4.
4. Remaining placement is spread over the first 3 quests, not a long test.

**Flow 2: Core quest**
1. Child taps an unlocked region, picks one of 2–3 quests (choice supports autonomy).
2. Each problem: read-aloud available, manipulatives on tap, "Ask Sage" button.
3. Wrong answer → gentle "Let's look again", the mastery bar does not drop, and a review item is scheduled.
4. After 5–8 problems: camp screen with "You can now: compare fractions with unlike denominators", cosmetic reward, and "Stop here, or one more quest?" with the daily limit shown.

**Flow 3: Parent/guide view**
1. Guild Hub → Math Realms tab: mastery map by domain, this week's newly mastered skills with one example each, and suggested offline activity.
2. Guide view (microschool): roster heatmap by skill, assign a commission, export for ESA/portfolio.

**Flow 4: My Needs**
1. Dial, fonts, TTS speed, input modes, hide/show hint button, daily limit, and "no animations in problems".
2. Accommodations are applied per child and never paywalled.

**Flow 5: Billing**
1. Free tier: Place-Value Peaks fully playable forever.
2. Upgrade only in the parent app, behind a parental gate. **Kids never see upgrade prompts.**
3. One-tap cancel; progress kept; region access reverts to free region.

**IA:** Child: Camp (home), Map, Quest, My Base, My Needs. Adult: Guild Hub (Mastery, Settings, Billing).

**Session design:** 10-minute quests, 25-minute default daily cap (parent adjustable 10–45), transition warning "2 problems left", no infinite quest chains.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial**

| Level | Math Realms behaviour |
|---|---|
| Calm | Static map; no ambient music; problem card only; reward = quiet check + one line |
| Balanced (default) | Gentle map transitions; soft effects; short optional reward animation at camp only |
| Lively | Animated creatures on the map; music on the map (never during problems); longer skippable celebration |

**Input modes:** tap (all), keyboard (number entry, arrow navigation on number lines), voice (numeric answers and "prove it" explanations), drawing ("prove it"), switch scanning (V1 via Lumen answer tray), AAC symbols for "prove it" reasons (V1).

**Targets and gestures:** ≥48 dp; manipulative handles ≥56 dp; tap-select-tap-place for every drag; no pinch zoom required (zoom buttons).

**Reading and typography:** word problems default at one grade below the math level; read-aloud; BDA typography; variable names never single italic letters in grades 3–5.

**Screen-reader math:** MathML + speech engine as in Sage (shared component); manipulatives expose state ("Fraction bar: 3 of 8 parts shaded"); number line announces position and tick values; custom actions replace drag.

**Audio:** voice/effects/music sliders; no failure sounds; captions for narration; haptics optional.

**No timers:** none in problems, quests or co-op. Co-op turn-taking waits indefinitely with a gentle "your friend is thinking" state.

**Age-respectful themes:** "Storybook" (illustrated) and "Blueprint" (clean, schematic; appeals to 11–12 and older strugglers).

**Lumen acceptance criteria**

| P | Criterion |
|---|---|
| P1 | Reduce Motion → Calm map, 0 non-essential animation |
| P2 | Every sound has a visual twin; music never plays during problems |
| P3 | Problem card layout fixed across regions |
| P4 | All manipulatives operable by taps only |
| P5 | Every problem has audio; word problems ≤ math grade −1 reading level |
| P6 | BDA defaults; spacing override works |
| P7 | ≥2 input modes per problem type |
| P8 | Visible mastery never decreases; no lives or hearts |
| P9 | Quest ends at camp; daily cap with warning |
| P10 | Picture passcode; problem text persists while using Sage |
| P11 | Zero timers |
| P12 | Accommodations free and portable |
| P13 | 2 themes independent of level |
| P14 | Parent sees weekly one-screen summary; guide setup ≤5 min |
| P15 | Rewards tied to mastery; no streaks; fading plan (rewards shift to base-building and "prove it" badges) |
| P16 | ND review of characters and feedback |
| P17 | No "proven" claims before study |
| P18 | No ads, no third-party trackers, no companion characters |

**Target Lumen score:** 23/24.

## 7. AI specification & guardrails

- **AI does:** knowledge tracing and next-problem selection (recommendation model, not LLM); problem generation from templates with CAS-verified answers; Sage hints (shared policy); rubric-assisted scoring of "prove it" responses with human-reviewed exemplars; TTS/ASR.
- **AI does not:** set prices or offers; run variable-ratio reward schedules; generate unreviewed story content; profile for marketing.
- **Pedagogy:** mastery gating with spaced review; interleaving after mastery; worked-example fading; "prove it" items every 3rd quest; teacher override of mastery.
- **Safety:** no companion persona (creatures are scenery, they don't talk to kids personally); AI disclosure on Sage; distress escalation inherited from Sage; no emotion recognition; all narrative text human-written or human-reviewed.
- **Hallucination control:** templates + CAS for every numeric item; LLM never generates an answer key.
- **Evaluation:** placement accuracy vs. teacher judgement (κ ≥0.6); mastery-prediction AUC ≥0.75 on held-out data; item-quality review by 2 teachers before release; fairness check on mastery predictions by ELL, disability flag (with consent) and gender.
- **Cost/latency [E]:** recommendation on-device or cheap cloud (<$0.02 per learner/month); Sage costs as per Sage doc; p95 next-problem ≤300 ms.

## 8. Data, privacy & compliance

| Data | Why | Retention | Processing |
|---|---|---|---|
| Responses, timing (for analytics only, never shown as speed) | Mastery model | 24 months rolling | Cloud |
| Mastery state | Progress, summaries | Life of account | Cloud; exportable |
| "Prove it" drawings/voice | Assessment | Drawings 12 months; voice not stored (transcript only) | On-device ASR first |
| Co-op pairing | Invited friends only | Life of link | Cloud |

Regimes: COPPA 2025 (VPC, separate AI-training consent off by default, retention policy); FERPA/SOPIPA for school/microschool contracts; state design codes (no nudges, no dark patterns); EU AI Act (mastery placement is potentially Annex III "assessing learning outcomes": plan human oversight by Dec 2027). Apple Kids category and Google Families: no third-party ads/analytics; parental gate on purchases and links.

**Timing data note:** response time is collected only to detect guessing and fatigue, never shown to the child, never used to rank.

## 9. Monetization & go-to-market

- **Benchmarks:** Prodigy $58.95–118.95/yr; IXL $79–159/yr; DreamBox $99.95–149.95/yr; Beast Academy $99.99/yr; SplashLearn ≈$90–144/yr; Khan/Zearn free.
- **Our pricing:** included in Questwise Family ($99/yr for 3 kids) = cheaper per child than every paid competitor. Free tier: one full region, no ads, no child-facing upsells.
- **Channels:** ESA marketplaces (math curriculum is the most common eligible spend [I]); microschools ($100–300/student bundle); homeschool co-op group codes; B2C.
- **ASO:** "math game no ads", "math adventure for kids", "fractions game", "dyslexia math", "math practice without timer". Accessibility Nutrition Label at launch.
- **Launch:** US English; Spanish V1.

## 10. Success metrics

- **North-star:** weekly mastered skills per active learner (target ≥2.5).
- **Inputs:** quests completed/week (≥4); % quests using Sage appropriately (hint then success); review items cleared; parent weekly summary opens.
- **Guardrails:** frustration quits mid-quest ≤10%; Sensory Comfort ≥4/5; 0 child-facing upsell impressions; zero billing complaints; daily cap respected (≤5% overrides by parents).
- **Outcomes:** pre/post on a standardised benchmark (e.g., MAP-like probe) in 3 microschools (Tier 3 target in year 1–2).
- **Retention:** D7 30%, D30 18%, DAU/MAU 25% in school months [E]; benchmark against Prodigy's high school-driven usage as context, not target.

## 11. Validation plan

**Riskiest assumptions**
1. Mastery-gated progress stays fun without variable-ratio rewards (vision).
2. Forgiving mastery keeps rigour (doesn't inflate mastery).
3. Parents will pay for Math Realms when Khan/Zearn are free.
4. Tap-first manipulatives are as usable as drag for typical kids.

| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | Paper-prototype region (Fraction Forest), mastery-gated vs. points-based variant, 3 microschools, 2 weeks | 36 kids | Voluntary persistence in mastery variant equal to or better than points variant (Discovery Plan Q2); kids rate fun ≥4/5 | Mastery variant persistence <75% of points variant |
| E2 | Paper mastery-map test with teachers: does the forgiving model's "mastered" match teacher judgement? | 6 teachers, 60 kid records | Agreement ≥80% | <65% → stricter thresholds |
| E3 | Figma manipulatives (tap vs. drag) usability, incl. motor-impaired kids | 20 kids (6 with motor/ND needs) | Tap completion ≥ drag; SUS-kids ≥75 | Tap slower by >30% |
| E4 | Price test: Questwise Family vs. Math-only $6/mo on landing page | 2,000 visits | ≥5% conversion to waitlist; ≥40% choose family | <2% |
| E5 | Sensory A/B (Calm vs. Balanced) on persistence | 20 kids | Comfort ≥4/5 on both | Comfort <3.5 |

Mapping: E1 = assumption Q2 (§8.2); E1–E3, E5 → WP4; E2 → WP1/WP4; E4 → WP5.

## 12. Build handoff

**Epic A: Placement & knowledge graph**
- **AC-A1:** Given a new learner, When placement quest completes (≤15 items), Then a starting node is set per domain and the first region unlocks.

**Epic B: Forgiving mastery**
- **AC-B1:** Given a learner at 90% displayed progress on a skill, When they answer incorrectly, Then displayed progress does not decrease and a review item is scheduled within the next 2 quests.
- **AC-B2:** Given mastery threshold is reached, When the region gate evaluates, Then all prerequisite nodes must be mastered, including ≥1 correct "prove it" or delayed review.

**Epic C: Manipulatives**
- **AC-C1:** Given Switch Control is on, When the learner partitions a fraction bar, Then it can be completed via focus + select without drag.
- **AC-C2:** Given VoiceOver, When a bar changes, Then the new state is announced ("5 of 8 parts shaded").

**Epic D: Rewards**
- **AC-D1:** Given any screen in the child app, When audited, Then no price, currency purchase or upgrade prompt appears.

**Epic E: Quests and endings**
- **AC-E1:** Given the daily cap is reached, When the quest ends, Then the camp screen shows "Done for today" with an off-screen suggestion and no "one more" button.

**Epic F: Dashboards**
- **AC-F1:** Given a week of activity, When the parent opens the summary, Then newly mastered skills show as plain-language statements with one example problem each.

**NFRs:** 60 fps on 3-year-old Android tablets and Chromebooks; offline quests with sync; iOS/Android/web; WCAG 2.2 AA; EN/ES; no third-party SDKs.

**QA focus:** AT matrix (VoiceOver, TalkBack, Switch Control, keyboard-only web, Dynamic Type max); sensory A/B; AI cases (template CAS verification on 100% of generated items; Sage leakage suite); COPPA (co-op invites only between VPC-verified families; no public profiles); billing (no child-facing upsell; one-tap cancel; ESA invoice).

**Platform dependencies:** Lumen components (answer tray, Dial, Now/Next/Done), My Needs, Sage policy engine + CAS, evidence engine (mastery events), Guild Hub.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Kids find it less exciting than Prodigy's battles | High | High | Exploration, base-building, co-op; E1 thresholds |
| Forgiving mastery inflates results | Medium | High | Delayed reviews and "prove it" required for gates |
| Content breadth (grades 2–7) is expensive | High | Medium | MVP: fractions, place value, multiplication/division; expand by data |
| Free incumbents (Khan, Zearn) | High | Medium | Differentiate on world, accessibility, ESA bundling |
| ESA eligibility rules vary | Medium | Medium | Per-state vendor playbook |

**Open questions:** Should co-op quests be synchronous? Which domains lead MVP? How much narrative is needed to sustain the world for 10–12s?

## 14. Sources
- [V] NBC News, Prodigy FTC complaint: https://www.nbcnews.com/tech/tech-news/child-protection-nonprofit-alleges-manipulative-upselling-math-game-prodigy-n1258294
- [V] EdWeek, Prodigy FTC complaint: https://www.edweek.org/technology/popular-interactive-math-game-prodigy-is-target-of-complaint-to-federal-trade-commission/2021/02
- [V2] Prodigy pricing 2026: https://brighterly.com/blog/prodigy-membership-cost/
- [V2] Fairplay "7 reasons to say no to Prodigy": https://fairplayforkids.org/pf/prodigy/
- [V2] IXL pricing and SmartScore: https://nibble-app.com/blog/ixl-cost · https://nibble-app.com/blog/is-ixl-worth-it · https://brighterly.com/blog/ixl-cost/
- [V2] SplashLearn: https://apps.apple.com/us/app/splashlearn-kids-learning-app/id672658828 · https://www.trustpilot.com/review/splashlearn.com · https://brighterly.com/blog/splashlearn-cost/
- [V2] DreamBox pricing: https://www.dreambox.com/family/pricing
- [V2] Zearn: https://about.zearn.org/
- [V2] Beast Academy: https://beastacademy.com/online/enroll · https://brighterly.com/blog/beast-academy-reviews/
- [V2 via raw 01/02/03] Prodigy rating, Khan accessibility, Beast Academy forum quote, 70% Roblox/Minecraft stat: research/raw/
- [M] DragonBox, IXL school footprint

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (lead) |
| **Ships in** | Questwise app (S2) |
| **Build wave** | 1c |
| **Pre-discovery priority score** | 80/100 [I] |
| **Consumes engines** | EN-03, EN-10 |
| **Studio features used** | SX-17, SX-25, SX-31 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = MR-01, MR-02, MR-03, MR-04, MR-05, MR-06.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| MR-E1 | **Real-world math missions** | Printable family missions (cooking, sport stats) that unlock nothing purchasable (SX-25). |
| MR-E2 | **Calm fluency** | Untimed fact-fluency practice with self-set goals, replacing speed drills. |

### 15.3 New validation question
Mastery-gated vs. points variant: persistence and enjoyment (paper A/B, microschools).

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 4 | 4 | 5 | 4 | 3 | 4 | 4 |

# Study Squad: App Strategy & Product Specification

> **Venture:** Ascendly · **App #:** 5/7 · **Ages:** 13–19 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/03-ascendly-teens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research caveat (important):** The shared session web-search budget ran out before this app's competitor research began, and WebFetch was blocked. Competitor facts here come from the studio's raw research files ([V2]) or from memory ([M]). **All [M] download, price and policy figures must be verified in Discovery WP1** (Sensor Tower/Appfigures export and store-page checks) before they are used in any external document.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Study with your friends — quietly, together — with the phone working for your focus instead of against it. |
| **Primary user / buyer** | Teens 13–19, especially ADHD and easily distracted teens (users). Parents (Plus payer). Schools/libraries (study hall / homework club licence, later). |
| **Core job-to-be-done** | "When I sit down to study and my phone keeps pulling me away, I want to be with friends who are also studying, so I actually start, keep going and stop at a sensible time." |
| **Category on the stores** | Productivity or Education (13+). |
| **Top competitors** | Forest, Opal, Focusmate, Flora, YPT (Yeolpumta), Study Together (Discord), StudyStream, Finch, Flipd, minimalist launchers; plus Tiimo as a design benchmark |
| **Our wedge** | 1. **Friends-only body doubling for minors** — adult platforms (Focusmate, open Discord servers, StudyStream webcams) match strangers; we don't. 2. **Video off, audio off by default:** presence through a quiet shared timer and check-ins, which works for anxious, autistic and Deaf teens. 3. **Focus that doesn't punish:** no dying trees, no rankings, no streak loss; a phone-free "lock-in" that the teen sets and can always exit. 4. **Connects to learning:** sessions start from Exam Ready plans or Study Coach problems and end in the Ascendly Record. |
| **Business model** | Free core (rooms, timers, lock-in). Ascendly Plus ($12/mo, $79/yr) adds unlimited squads, longer history, planning integrations. Later: school/library "virtual study hall" licence. |
| **North-star metric** | Weekly focused study minutes in squads per active teen (self-reported "on task" check-ins). |
| **MVP candidate?** | **Later** (Year 2), but validate now with a Discord-bot pilot (no build). |

## 2. Problem & users

**Problem statement.** Teens frame their phones as the enemy of study, and focus apps are among the most discussed teen study tools: Forest has a 4.8 rating from more than 1M ratings; Opal and one sec add system-level blocks and pauses [V2: raw 03]. The complaints are consistent: focus apps are easy to bypass and their novelty wears off [M: raw 03]. Study is social — teens study with friends on Discord, in "study with me" streams and on StudyTok — while the apps are single-player [M/I: raw 03]. Body doubling (working alongside another person) is widely used by ADHD adults through Focusmate, but those services pair strangers on video and are generally aimed at adults [M]. Phone bans in schools (22 states enacted K-12 cellphone bans in 2025 alone [V: raw 05, Ballotpedia]) push study to after school and home, where there is no structure. ADHD affects about 11.4% of US children, with roughly 1 in 3 untreated [V2: research paper §7]. Punitive mechanics hurt: forums praise Finch because it "doesn't punish you for missing a day" [V2: raw 03].

**Personas**
| Persona | Snapshot | Needs |
|---|---|---|
| **Chloe, 17, ADHD** | Can't start; doomscrolls; Forest "wears off". | Someone "there" when she starts; a lock-in she chose; short sprints; no shame. |
| **Kai, 15, autistic** | Hates video calls and noise; likes routine. | Presence without faces or voices; predictable room structure. |
| **Maya, 16, Deaf** | Discord voice rooms exclude her. | Text/emoji check-ins, visual timers, no audio dependence. |
| **Aaliyah, 16** | Studies alone late at night. | Friends to study with before exams; a "we're done at 10:30" end. |
| **Parent (Ms. Ortiz)** | Worried about strangers online and about screen time. | Friends-only, no DMs with strangers, visible safety model, no surveillance of content. |

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Start and sustain focus | Forest/Opal popularity [V2]; ADHD prevalence [V2] | Shared start, sprint timers, check-ins, lock-in |
| Study socially | Discord/"study with me" [M/I: raw 03] | Friends-only squads, co-presence without video |
| Safety from strangers | FTC 6(b)/teen safety climate [V2]; Discord stranger risk [M] | Invite-only; no stranger discovery; no DMs outside squads |
| No punishment | Finch praise [V2]; streak backlash [V2] | Gentle weekly goals; no dying tree; no leaderboards |
| Sensory comfort | Lumen evidence [V2] | Video/audio off by default; Calm rooms |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Loved | Complaints | A11y / sensory | Source |
|---|---|---|---|---|---|---|---|---|
| **Forest** | Seekrtech | 4.8 from 1M+ ratings [V2]; long-running top productivity app [M] | iOS paid up-front (≈$3.99) [M]; Android free + Pro [M] | 4.8 [V2] | Growing a tree; real-tree planting partnership; "plant together" with friends [M] | Tree dies if you leave (loss framing); easy to bypass; novelty fades [M: raw 03] | Visual timer; loss mechanic stressful for some [I] | raw 03; forestapp.cc [M] |
| **Opal** | Opal | Popular screen-time app with iOS Screen Time API blocking [V2: raw 03]; scale to verify [M] | Freemium; Pro subscription (≈$99/yr) [M] | High [M] | System-level blocks, "deep focus" sessions, schedules | Price; subscription; hard-mode frustration [M] | Clean UI [M] | raw 03 |
| **Focusmate** | Focusmate | Leading body-doubling platform for adults [M] | Free (limited sessions/week); Plus ≈$9.99/mo [M] | High [M] | 25/50/75-min video sessions with a stranger; accountability | Video with strangers; scheduling; **adult-oriented (18+ per ToS [M])** | Video-first; camera required norm [M] | focusmate.com [M] |
| **YPT (Yeolpumta)** | Pallo/YPT [M] | Very popular in Korea and Japan [M] | Free with ads; premium [M] | High [M] | Study-time tracking, study groups with shared timers, phone-down detection [M] | Rankings and hours-comparison pressure; ads [M/I] | Dense UI [I] | [M] |
| **Study Together (Discord) / StudyStream** | Community / StudyStream Ltd | Study Together is one of the largest study Discord servers; StudyStream runs webcam "focus rooms" [M] | Free; StudyStream paid tier [M] | n/a | Always-on rooms, cam/screen share, Pomodoro bots, global community | Strangers; moderation varies; Discord is 13+ but mixed-age [M] | Voice/video heavy; overwhelming for some [I] | [M] |
| **Flora** | AppFinca [M] | Forest-like free alternative [M] | Free; optional real-tree pledges [M] | High [M] | Free group focus with friends; bet-based challenges [M] | Loss mechanic; bet mechanic = pay-to-motivate [I] | Similar to Forest [I] | [M] |
| **Finch** | Finch Care | Popular self-care pet app among teens and ND users [V2] | Freemium [V2: catalog] | High [M] | "doesn't punish you for missing a day" [V2] | Some find it childish [M: raw 03] | Calm; cute aesthetic [V2] | raw 03 |
| **Tiimo** (design benchmark) | Tiimo | 2025 iPhone App of the Year [V2: raw 02/04] | $12/mo or $54/yr (iOS) [V2: raw 04] | High | ND-first visual planner, focus timers, AI task breakdown | iOS-only; price [V2: raw 04] | Calm, co-designed with ND users [V2] | raw 04 |

**Also:** Flipd (focus timer with community features; earlier "full lock" mode) [M]; minimalist launchers (grayscale, text-only home screens) [M]; one sec (friction before opening apps) [V2: raw 03].

**Feature matrix**

| Feature | Forest | Opal | Focusmate | YPT | Discord/StudyStream | Finch | Tiimo | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Focus timer | ✓ | ✓ | ✓ | ✓ | ✓ (bots) | ◐ | ✓ | **Parity** |
| Friends-only groups | ✓ | ✗ | ✗ | ✓ | ◐ (private servers) | ◐ | ✗ | **Parity**, the default and only mode for minors |
| Stranger matching | ✗ | ✗ | ✓ | ✓ (global groups) | ✓ | ✗ | ✗ | **Reject** for under-18s |
| Video co-working | ✗ | ✗ | ✓ | ✗ | ✓ | ✗ | ✗ | **Reject** at MVP; V2 friends-only, opt-in, off by default |
| Text/emoji check-ins | ◐ | ✗ | ◐ (chat) | ◐ | ✓ | ◐ | ✗ | **Improve** (structured, low-effort) |
| App/phone blocking | ◐ (in-app) | ✓ | ✗ | ◐ | ✗ | ✗ | ◐ | **Parity** via OS Screen Time / Digital Wellbeing APIs |
| Loss mechanic (tree dies) | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject** (P8/P15) |
| Leaderboards / hours rankings | ◐ | ✗ | ✗ | ✓ | ◐ | ✗ | ✗ | **Reject** (comparison pressure) |
| Streaks with loss | ◐ | ◐ | ✗ | ◐ | ✗ | ✗ (gentle) | ✗ | **Reject**; weekly goals with pause days |
| Session planning / task breakdown | ✗ | ◐ | ◐ (goal statement) | ✗ | ✗ | ◐ | ✓ | **Improve** (AI plan from Exam Ready/Coach) |
| Real-world reward (tree planting) | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **V2 consider** (collective, not individual loss) |
| Designed session ending | ◐ | ◐ | ✓ | ✗ | ✗ | ◐ | ✓ | **Differentiate** (group wrap-up) |
| Moderation for minors | ✗ | n/a | ◐ | ◐ | ◐ | n/a | n/a | **Differentiate** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| SQ-01 | **Friends-only squads** ★ | Squads of 2–8 created by invite link/QR from a known friend or a school class code; no search or discovery of strangers. | Safety for minors | Differentiate | MVP | Must |
| SQ-02 | **Quiet co-study room** ★ | Shared timer, avatars as initials/tiles, "studying: Chem" status; video and audio off (no voice at MVP). | Body doubling without sensory load | Differentiate | MVP | Must |
| SQ-03 | **Shared sprint timer** | Pomodoro-style (25/5, 50/10, custom); anyone can start; visual countdown hideable; breaks synced. | Forest/Focusmate parity | Parity | MVP | Must |
| SQ-04 | **Structured check-ins** | At start: "I'll finish…" (text/voice-to-text/emoji); at end: "Done / Partly / Stuck". Pre-set emoji reactions only (no free chat during sprints). | Accountability without chat distraction | Improve | MVP | Must |
| SQ-05 | **Phone-free lock-in** ★ | Teen-chosen blocking of distracting apps during sprints via iOS Screen Time/Family Controls and Android Digital Wellbeing/accessibility-safe APIs; always exit-able with a 10-second pause (no penalty). | Opal/one sec parity without punishment | Parity + Lumen | MVP | Must |
| SQ-06 | **Session plan** | Start from an Exam Ready plan, a Coach problem list or a simple 3-task list; AI can split a task into steps (Goblin Tools-style). | Task initiation for ADHD | Improve | MVP | Should |
| SQ-07 | **Designed group wrap-up** | Squad summary: minutes, tasks done, one-line reflections; "Same time tomorrow?" (opt-in reminder). | Lumen P9 | Lumen | MVP | Must |
| SQ-08 | **Gentle weekly goal** | Personal weekly minutes goal; pause days; no streak loss; no leaderboards. | Finch evidence [V2] | Lumen | MVP | Must |
| SQ-09 | **Safety & moderation** | Report/leave/block; squad owner can remove; AI text moderation on check-ins; no DMs outside squads; no images/links at MVP. | Minor safety | Lumen / compliance | MVP | Must |
| SQ-10 | **Solo mode with ambient presence** | Study "with" an anonymous count of Ascendly teens currently studying (no identities, no interaction). | Presence when friends are offline | Differentiate | MVP | Should |
| SQ-11 | **Sensory rooms** | Room themes: Library (silent), Café (optional ambient sound), Night (dark). All sounds off by default. | Sensory choice | Lumen | MVP | Should |
| SQ-12 | Record summary | Weekly focus summary saved to Ascendly Record (teen decides whether to share). | Shared layer | Differentiate | V1 | Should |
| SQ-13 | Voice rooms (friends-only, opt-in) | Push-to-talk voice during breaks only; captions. | Social demand | Parity | V1 | Could |
| SQ-14 | Class/club squads | Teacher or librarian creates a homework-club squad; adults visible as moderators. | School/library channel | Parity | V1 | Should |
| SQ-15 | Collective impact goal | Squad minutes add up to a collective real-world pledge (e.g., trees, library books), no individual loss. | Forest parity, reframed | Improve | V2 | Could |
| SQ-16 | Video co-working (opt-in) | Friends-only, off by default, background blur, no recording. | Focusmate parity | Parity | V2 | Could |
| SQ-17 | Wearable timer | Watch haptic timers and check-ins. | Tiimo parity | Parity | V2 | Could |

★ = signature. **Signature: friends-only quiet co-study rooms with a shared timer and a teen-chosen phone lock-in.** MVP = 11 features.

## 5. Core experience & key user flows

**Core loop:** open → pick squad (or solo) → state goal → start sprint (lock-in optional) → quiet co-presence → break (react) → next sprint → group wrap-up → natural end.

**Flow 1: Onboarding (≤5 min)** — age confirm (13+) → Sensory Dial → "Add a friend": share link/QR or enter class code (no contact-list upload by default) → try a 10-minute solo sprint while waiting.

**Flow 2: Core squad session**
1. Chloe opens "Chem crew" (4 friends; 2 online).
2. Check-in: "Finish stoichiometry set 3" (dictated).
3. Sprint 25 min; lock-in blocks TikTok and Instagram (her choice). Tiles show "studying" dots.
4. Break: emoji reactions; one friend marks "Stuck" → "Open in Study Coach" link.
5. Second sprint. Wrap-up: "Chem crew studied 3 × 50 minutes. You finished 1 of 1 goals." Ends.

**Flow 3: Lock-in exit** — teen taps Exit → 10-second pause with "You chose to lock in until 9:40. Leave anyway?" → exit allowed; no penalty, no notification to friends except status "on break".

**Flow 4: Parent/teacher view** — parent: optional weekly summary of focus minutes (teen consents); never room content. Teacher/librarian (V1): moderates a club squad; sees attendance, not messages.

**Flow 5: My Needs** — Dial, timers visual/haptic, sound off/on per channel, check-in mode (text/emoji/voice-to-text), lock-in presets, reminders.

**Flow 6: Billing** — Plus through fair-billing charter; free core never limits friends-only rooms below 3 squads.

**IA:** Squads · Solo · Plan · Me (weekly goal, My Needs). Four tabs.

**Session design:** default 2 × 25-minute sprints; hard maximum configurable by teen/parent (e.g., "end by 11 p.m."); quiet-hours reminder; wrap-up is mandatory before a new room session starts.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial**
| Level | Study Squad changes |
|---|---|
| Calm (default) | Static tiles, no sound, no confetti, dark or muted palette, timer as a slowly filling bar |
| Balanced | Gentle presence pulses, optional soft break chime |
| Lively | Animated room theme, optional ambient sound, short celebration at wrap-up |

**Input modes:** tap for everything; check-ins by typing, voice-to-text, emoji picker or AAC text; switch access via OS; keyboard shortcuts on web.

**Targets/gestures:** 44 pt/48 dp; no swipe-only actions; timer controls large and labelled.

**Timers (P11):** timers are *tools the teen chose*, not limits; visual + haptic + optional sound; hide numbers option ("fuzzy timer"); transition warnings at 2 minutes before breaks.

**ADHD focus:** one-tap start; task split into steps; "park it" note; ambient presence; lock-in with self-set exits; no infinite feed (the app has no feed at all).

**Autistic/Deaf inclusion:** no voice or video needed; predictable room structure; text/visual only.

**Reading/typography:** grade 5–7 copy; BDA defaults.

**Age-respectful themes:** Library, Night, Minimal; no childish pets.

**Lumen principles**
| # | Acceptance criterion |
|---|---|
| P1 | Calm default; Reduce Motion stops presence animation |
| P2 | All sounds off by default; every cue visual + haptic |
| P3 | Same room layout every time; Now/Next strip (sprint/break/wrap-up) |
| P4 | Single-tap start/stop/react |
| P5 | Copy ≤ grade 7 |
| P6 | BDA defaults |
| P7 | Check-ins via ≥3 modes |
| P8 | No loss mechanic; exiting lock-in never penalised |
| P9 | No feed; wrap-up screen always; end-by time respected |
| P10 | Goal shown throughout the session |
| P11 | All timers adjustable/hideable |
| P12 | All accessibility free |
| P13 | Mature themes |
| P14 | Club squad set up in ≤5 min |
| P15 | Weekly goal, pause days, no rankings |
| P16 | ND panel reviews lock-in language (no "willpower" shaming) |
| P17 | No "improves ADHD" claims; education/productivity only |
| P18 | Friends-only; no stranger contact; no location; DPIA |

**Target Lumen score:** ≥22/24.

## 7. AI specification & guardrails

**AI does:** suggest session plans and task breakdowns from the teen's goal; moderate check-in text (toxicity, bullying, self-harm language, personal-info sharing); summarise the week.

**AI does not:** act as a study "buddy" persona or chat partner; generate social messages on the teen's behalf; rank or compare teens; infer mood from behaviour; recommend strangers.

**Safety:** friends-only graph; invite links expire (24 h) and can be single-use; age-band separation (13–15 and 16–17 cannot join squads with adults unless a verified school adult moderates a club squad); report/block within 2 taps; distress language in check-ins → private crisis resource card to the writer and (for school club squads) the adult moderator per protocol; no images/links at MVP (reduces grooming and harmful content vectors).

**Evaluation:** moderation classifier precision/recall on a teen-slang test set (recall ≥95% for self-harm and sexual-content categories); red-team grooming scenarios (adult impersonation, link sharing, off-platform move requests) blocked 100% in the test set.

**Cost [E]:** minimal; moderation and plan generation ≈$0.001–0.005 per session.

## 8. Data, privacy & compliance

| Data | Why | Retention | Where |
|---|---|---|---|
| Friend connections | Squads | Until removed | Cloud |
| Check-in text | Accountability | 7 days, then aggregated | Cloud |
| Focus minutes | Goals | Account lifetime | Cloud |
| Blocked-app list | Lock-in | On-device only | Device (Screen Time API tokens are opaque) |
| Reports | Safety | 1 year | Cloud |

**Regimes:** COPPA (13+ only); UK AADC (no nudges, geolocation off, high-privacy defaults); state design codes and **KOSA-ready** — Study Squad is the Ascendly app closest to "social media", so we exclude compulsive-use features (no feeds, no infinite scroll, no variable rewards, no public metrics, no push notifications between 10 p.m. and 7 a.m. by default); Australia-style under-16 social-media rules [M: verify whether a friends-only study tool is in scope]; app-store age-assurance laws (Utah/Texas style) [M]; FTC §5. Apple Screen Time API and Android usage-access permissions reviewed for store policy compliance.

**Consent:** teen consent; parent notice with teen visibility for under-16s; no contact-list upload unless explicitly chosen.

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Free | $0 | Up to 3 squads, timers, lock-in, check-ins, weekly goal |
| Plus | $12/mo or $79/yr (Ascendly-wide) | Unlimited squads, plan integrations, history, themes |
| Library/School | $2–5/student/yr or site licence [E] | Club squads, adult moderators, attendance |

Benchmarks: Forest one-time ≈$3.99 [M]; Opal Pro ≈$99/yr [M]; Focusmate Plus ≈$9.99/mo [M]; Tiimo $54/yr [V2]. Study Squad alone would be priced low; value comes through Ascendly Plus.

**Channels:** friend invites (organic, no contact scraping, no rewards for invites); StudyTok/"study with me" creators (organic); school clubs and libraries; exam-season campaigns. **ASO:** "study with friends", "focus app for students", "body doubling", "phone-free study". Accessibility Nutrition Label.

## 10. Success metrics
- **North star:** weekly squad focus minutes per active teen (target ≥120).
- **Inputs:** sessions per week per active teen (≥2 — A3 threshold); % sessions with a stated goal (≥70%); goal completion rate; squad size ≥3.
- **Guardrails:** safety reports per 1,000 sessions (<1; all actioned <24 h); Sensory Comfort ≥4/5; % sessions ending before the teen's end-by time (≥95%); late-night use not increasing; lock-in exits never penalised (audit).
- **Outcomes:** self-reported start latency (minutes to start) and weekly study minutes vs baseline; exam-season study minutes.
- **Retention:** D30 ≥20%; DAU/MAU ≥25% in term time.

## 11. Validation plan (no-code)

**Riskiest assumptions**
1. Teens will use a new social space rather than Discord (A3).
2. Quiet co-presence (no video/voice) is enough body doubling.
3. Teen-chosen lock-in helps more than it annoys.
4. Parents trust the safety model.

**Experiments**
| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | **2-week Discord pilot with a "Squad bot"** (private servers per friend group, timers, check-ins, wrap-up; adult research moderator) | 8 friend groups (~30 teens), ≥30% ADHD/ND | ≥2 sessions/week per active teen (A3); ≥60% say they started faster | <1 session/week |
| E2 | Quiet vs voice rooms A/B (within the pilot) | Same | Quiet ≥ voice for ND teens on comfort and minutes | — |
| E3 | Lock-in concept test with OS Focus modes (teens configure their own) | 20 teens | ≥50% keep it on for 1 week; frustration ≤2/5 | — |
| E4 | Parent safety explainer test | 20 parents | Trust ≥4/5; ≥70% would allow | <50% |
| E5 | Sensory A/B (Calm vs Lively rooms, Figma) | 24 teens | Calm preferred or equal for ND teens | — |

**Mapping:** WP2 (6 study-session observations; diaries), WP4 (E1–E3, E5 via existing-tool pilot), WP5 (E4 + library interest). **WP1 must verify all [M] competitor figures.**

## 12. Build handoff

**Epic A: Squads**
- Given I share an invite link, When a friend opens it within 24 h, Then they join my squad, And the link cannot be found via search.
- Given I'm 14, When an adult account tries to join via link, Then the join is blocked unless the squad is a verified school club.

**Epic B: Room and timer**
- Given a squad sprint starts, Then all members see the same timer within 1 s, And sounds stay off unless enabled.

**Epic C: Lock-in**
- Given I chose to block apps for 25 min, When I exit early, Then I wait 10 s, can leave, and no one is notified except my status changes to "break".

**Epic D: Moderation**
- Given a check-in contains a phone number or self-harm language, Then it's held, the writer sees guidance/resources, and it's not shown to others.

**Epic E: Wrap-up**
- Given a session ends, Then everyone sees the group summary and the app offers no "one more sprint" autoplay.

**NFRs:** real-time sync ≤1 s p95; works on low-end Android; offline solo timer; iOS/Android (web V1); WCAG 2.2 AA; Screen Time API entitlement from Apple.

**QA focus:** AT matrix (VoiceOver announces timer on request, not every second); safety red-team (grooming, off-platform requests); age-band separation; lock-in on iOS/Android variants; notification quiet hours; sensory A/B.

**Platform dependencies:** Lumen; My Needs; moderation service (shared with Life Ready challenges); privacy stack (age assurance); Ascendly Record; plan hooks from Exam Ready/Study Coach.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Discord inertia | High | High | Pilot on Discord first; build only if E1 passes; later Discord integration |
| Safety incident | Low | Very high | Friends-only, no media, moderation, age bands |
| Regulated as social media | Medium | High | No feeds/public profiles; legal review per state |
| Novelty decay (focus apps) | High | Medium | Tie sessions to real deadlines (Exam Ready); social commitment |
| OS blocking APIs change | Medium | Medium | Lock-in optional; degrade to reminders |

**Open questions:** Is voice necessary for retention? Should libraries host public (moderated) study halls for teens without friends on the app? How to handle mixed-age friend groups (e.g., 17 and 19)?

## 14. Sources
- Forest/Opal/one sec/Finch voice of customer — research/raw/03-forum-voice-of-customer.md [V2]
- Tiimo pricing and award — research/raw/04-neurodivergent-and-inclusive-ux.md; research/raw/02-apple-app-store-top30.md (https://www.apple.com/newsroom/2025/12/apple-unveils-the-winners-of-the-2025-app-store-awards/) [V2]
- Phone bans — https://news.ballotpedia.org/2025/08/08/twenty-two-states-enacted-k-12-cellphone-bans-so-far-in-2025/ [V2: raw 05]
- ADHD prevalence — docs/01-research-paper.md §7 [V2]
- KOSA status — https://www.cnbc.com/2026/08/05/kosa-privacy-social-media-senate.html [V2]
- CA SB 243 / FTC 6(b) — https://www.joneswalker.com/en/insights/blogs/ai-law-blog/ai-regulatory-update-californias-sb-243-mandates-companion-ai-safety-and-accoun.html [V2]
- Forest, Opal, Focusmate, YPT, Flora, Flipd, StudyStream, Study Together details — from memory [M]; **verify in WP1** (store pages, Sensor Tower/Appfigures, ToS for age limits)

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Merge → Ascendly skin on EN-05 + EN-11 (Focus & safe rooms) |
| **Ships in** | Ascendly app (S3) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 65/100 [I] |
| **Consumes engines** | EN-05, EN-11 |
| **Studio features used** | SX-19, SX-05 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = SQ-01, SQ-02, SQ-03, SQ-05, SQ-09.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| SQ-E1 | **OS focus integration** | The teen's chosen lock-in uses platform focus and Screen Time APIs (e.g., iOS Family Controls, Android Digital Wellbeing) [M: verify API scope]. |
| SQ-E2 | **Library virtual study hall** | A partner-hosted, moderated study hall for teens without a friend group. |

### 15.3 New validation question
Discord-bot pilot: ≥2 sessions/week per active teen.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 3 | 4 | 2 | 2 | 4 | 3 | 4 |

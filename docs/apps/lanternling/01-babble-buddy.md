# Babble Buddy: App Strategy & Product Specification

> **Venture:** Lanternling · **App #:** 1/7 · **Ages:** 1–3 (parent-held; the child never holds the device) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/01-lanternling-early-years.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given; usually a search-result snippet because store pages were blocked by the proxy) · [V2] secondary or vendor source · [M] from memory, not re-verified · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A pocket talk coach for the grown-up. It turns bath, meals, nappy changes and car rides into back-and-forth conversation with a toddler, without handing the toddler a screen. |
| **Primary user / buyer** | Parents and caregivers of 12–36-month-olds (buyer and user are the same adult). Secondary: grandparents, childminders, Early Head Start home visitors, speech-language pathologists (SLPs) who "prescribe" it between sessions. |
| **Core job-to-be-done** | "When I'm doing the everyday routines with my toddler and my mind is elsewhere, I want one simple, specific thing to say and do, so I can help their language grow without extra screen time or guilt." |
| **Category on the stores** | Apple: Education (adult-facing; **not** the Kids category, because the child is not the user). Google Play: Parenting. |
| **Top competitors (by downloads / revenue)** | Kinedu (11M+ families claimed) · Speech Blubs (6M+ downloads) · Huckleberry (5M+ families claimed) · The Wonder Weeks (5M+ iOS) · BabySparks (2M+) · Vroom (free, foundation-funded) · Lovevery app (bundled with kits) · LENA Start / LENA Grow (programs, not an app store product) |
| **Our wedge** | 1. **The phone stays with the adult.** Competitors either give the toddler a screen (Speech Blubs) or give the parent a video library to watch (Kinedu, Lovevery). We give the parent one sentence to say *now*. 2. **Serve-and-return measured, privately.** LENA-style conversational-turn feedback without a $-hardware recorder, computed on-device, off by default, with a tap-tally alternative for signing and AAC families. 3. **Honest and free at the core.** Free daily prompts forever. Fair-billing charter against a category known for trial traps. |
| **Business model** | Free forever: daily Moment Cards, songs, word tracker. Paid in the Lanternling Family plan (≈$9.99/mo or $69/yr, up to 3 children): personalised prompt plans, Talk Tally trends, SLP/teacher sharing, grandparent seats. B2B2C: Early Head Start, home-visiting, pediatric practices, libraries. |
| **North-star metric** | **Weekly talk moments per family**: Moment Cards the adult marks as done (or Talk Tally sessions), counted per week. |
| **MVP candidate?** | **Yes.** The vision names Babble Buddy as a likely Year-1 MVP app alongside Sound Garden and Story Lantern. |

## 2. Problem & users

**Problem statement.**
- Children's language growth is tied not just to how many words they hear but to **conversational turns**, the back-and-forth "serve and return" with an adult. In Romeo et al. (2018, *Psychological Science*), children aged 4–6 who experienced more adult-child conversational turns showed more activation in Broca's area during story listening, independent of SES and IQ, and turns explained the link between language exposure and verbal skill [V] ([Psych Science](https://journals.sagepub.com/doi/abs/10.1177/0956797617742725)).
- LENA reports that for classrooms starting under 15 turns/hour, its LENA Grow coaching took average turn rates from 9 to 19 per hour [V2] ([LENA Grow outcomes](https://www.lena.org/programs/lena-grow/effectiveness/)). LENA Start (the parent program) reports that lower-talk families gained about 12 percentile points in conversational turns [V2] ([LENA blog](https://www.lena.org/blog-post/page/5/)). **Feedback on talk changes talk.**
- But these programs need a wearable recorder, a facilitator and a group schedule. The app market instead offers either (a) **screens for toddlers** (Speech Blubs video modeling), or (b) **video libraries for parents** (Kinedu's 3,000+ videos [V]), which take the adult's attention away from the child.
- Toddler content is mostly YouTube, and almost nothing in the top 30 is built for 1–3 [V] ([Research paper §4.4](../../01-research-paper.md)). Before ~18–24 months, children learn poorly from 2D screens without a responsive adult (the "video deficit") [M] ([raw 04 §B3](../../../research/raw/04-neurodivergent-and-inclusive-ux.md)).
- The AAP's January 2026 policy statement dropped fixed screen-time limits in favour of co-engagement and family media plans [V] ([raw 04 §B4](../../../research/raw/04-neurodivergent-and-inclusive-ux.md)). Screen-time guilt remains the dominant parent emotion [V] (Research paper §5.2).

**Personas.**

| Persona | Snapshot | What they need from Babble Buddy |
|---|---|---|
| **Maya, 34, parent of Leo (2)** | Hybrid worker. Uses the phone to get through dinner prep and feels guilty. Leo has ~20 words. | A 10-second prompt she can read or hear while cooking; no setup; reassurance that she's doing enough. |
| **Dani, 29, Deaf parent (ASL) of Nia (18 mo, hearing)** | Signs at home; Nia hears English from grandparents and daycare. | Prompts that count **signs** as language. No audio-only cues. Turn tracking that doesn't rely on a microphone. Captions on every song. |
| **Priya, 36, parent of Arjun (30 mo), late talker, on an Early Intervention waitlist** | Anxious. Has read that "apps are no substitute for therapy". Speaks Tamil and English at home. | SLP-aligned strategies (wait time, expansions, choices) in plain words; home-language prompts; progress she can show the SLP; **no diagnosis**, clear "talk to your pediatrician" signposting. |
| **Grandma Rosa, 67** | Minds the grandkids twice a week. Low tech confidence, presbyopia. | Big type, voice-read prompts, one button: "Give me an idea." |
| **Ms. Carter, Early Head Start home visitor** | 12 families, many with low literacy or limited data. | A way to "leave behind" a week of prompts by SMS/print; aggregated, consented progress. |

**Needs & wants.**

| Need | Evidence | How Babble Buddy addresses it |
|---|---|---|
| Language support without handing the toddler a screen | Video deficit [M]; AAP 2026 co-engagement [V]; guilt [V] | Parent-held design; zero child screen time; audio-first prompts |
| Specific, doable ideas tied to daily routines | Vroom organizes 1,000+ free tips around mealtime, bath and bedtime [V] ([vroom.org](https://www.vroom.org/)) | Routine-anchored **Moment Cards** (1 sentence + 1 "wait" cue) |
| Feedback that talk is increasing | LENA turn feedback changes behaviour [V2] | Optional **Talk Tally** (on-device) or tap tally; weekly trend |
| Know what's typical and when to ask for help | Kinedu/BabySparks milestone trackers are core features [V] | Parent-tapped **Word Garden** + milestone guide with careful referral language |
| Honest pricing | Speech Blubs trial/renewal complaints [V] ([Trustpilot](https://www.trustpilot.com/review/speechblubs.com)); category-wide billing anger [V] | Free core; fair-billing charter; one-tap cancel |
| Home-language support | Bilingual families (vision persona Andre; Priya) | Prompts in Spanish at MVP; home-language word logging in any language |
| Works for Deaf, signing, AAC and low-literacy families | Lumen P2, P7 | Sign-inclusive prompts; tap tally; read-aloud prompts; icons |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Kinedu** | Kinedu Inc. (Mexico/US) | "11M+ families" (vendor); ~7.9M Android downloads [V] | Freemium; Premium ≈$7/mo billed $79.99/yr; up to 5 babies [V] | App Store high-4s [M] | 3,000+ short video activities; milestone reports in 4 areas; expert classes; AI assistant; 3 languages [V] | Paywall on most activities; video-heavy [M/I] | Parent watches videos: pulls attention to screen [I]; captions unknown [M] | [App Store](https://apps.apple.com/us/app/kinedu-baby-development/id741277284) · [MIT Solve](https://solve.mit.edu/solutions/7799) |
| **Speech Blubs** | Blub Blub Inc. | 6M+ downloads [V]; ~0.6M US iOS/yr (Sensor Tower, via raw 02) [V2] | 7-day trial; $14.49/mo or $59.98/yr; lifetime $99.99 [V] | 4.6 iOS (11.6K); 4.5 Play (28.2K) [V] | Peer "video modeling" kids love; SLP-created content [V] | **Cancellation and renewal complaints** (charged after cancelling; "70% off" converting to monthly) [V] | Child-facing screen with face filters; high engagement design [I] | [Play](https://play.google.com/store/apps/details?id=org.blubblub.app.speechblubs&hl=en_US) · [Trustpilot](https://www.trustpilot.com/review/speechblubs.com) · [Ed App Store](https://www.educationalappstore.com/app/speech-blubs-language-therapy) |
| **Huckleberry** | Huckleberry Labs | 2.3M downloads (tracker est.); "5M+ families" (vendor) [V] | Free; Plus $58.99/yr; Premium $119.99/yr [V] | 4.9 iOS (74K) [V] | Sleep prediction ("SweetSpot"), routine logging, expert plans [M] | Paywall for sleep plans [M] | Parent-facing, clean; shows parents pay for routine coaching [I] | [App Store](https://apps.apple.com/us/app/huckleberry-baby-tracker/id1169136078) · [Pricing](https://huckleberrycare.com/pricing) |
| **The Wonder Weeks** | Kiddo Kiddo / Hetty van de Rijt | 5M+ on iOS; ~90K/month est. [V] | Free + IAP (≈$4.99/mo); Android paid $6.49 [V] | 4.8 iOS (122K) vs 3.7 Play [V] | Explains fussy "leaps"; reassurance [V] | Scientific basis contested [M]; Android rating gap [V] | Text-heavy [M] | [App Store](https://apps.apple.com/us/app/the-wonder-weeks-baby-leaps/id529815782) · [Sensor Tower](https://app.sensortower.com/overview/529815782?country=US) |
| **BabySparks** | BabySparks Inc. | 2M+ downloads [V] | $3.99/mo, $23.99/yr, lifetime $39.99 [V] | 4.7 [V] | Daily personalised activity program; 1,300+ activities; milestone tracker [V] | Video/article heavy; generic [I] | Parent-facing [V] | [Site](https://babysparks.com/) · [App Store](https://apps.apple.com/us/app/babysparks-development-app/id794574199) |
| **Vroom** | Bezos Family Foundation | Not published; free; widely distributed via states and agencies [V2] | Free, EN/ES [V] | n/a [M] | 1,000+ routine-based tips; "Look, Follow, Chat, Take Turns, Stretch" [V]; Harvard CDC input [V] | Static tips; little personalisation or feedback [I] | Text-first tips; bilingual [V] | [vroom.org](https://www.vroom.org/) · [App Store](https://apps.apple.com/us/app/vroom-early-learning/id885948312) |
| **Lovevery app** | Lovevery | Tied to kit subscribers (not published) [M] | 28-day trial; free with Play Kits or $12/mo app-only [V] | n/a | Weekly stage-based videos; "Play Finder" camera on toys; milestone info [V] | Value depends on buying kits [I] | Video-first [V] | [Lovevery blog](https://blog.lovevery.com/product-recommendations/the-lovevery-app-for-parents/) |
| **LENA Start / Grow** (benchmark, not app) | LENA (non-profit) | Programs in Head Start/EHS and communities [V] | Program-funded [M] | n/a | Measures turns with a wearable; coaching; strong outcome data [V2] | Needs hardware + facilitator [I] | Audio-only measure excludes signing families [I] | [LENA](https://www.lena.org/programs/lena-grow/) |

**Takeaways [I].** Parents pay for routine coaching (Huckleberry) and development plans (Kinedu). Nobody pairs in-the-moment prompts with LENA-style talk feedback at app price. The only speech-focused leader (Speech Blubs) is child-facing and carries billing-trust baggage. Vroom sets the free-content bar, so we must beat it on personalisation, feedback and caregiver sharing.

**Feature matrix.**

| Feature | Kinedu | Speech Blubs | Huckleberry | Wonder Weeks | BabySparks | Vroom | Lovevery | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Parent-held, no child screen | partial | ✗ | ✓ | ✓ | partial | ✓ | partial | **Differentiate**: zero child-facing UI |
| Routine-anchored prompts | partial | ✗ | partial | ✗ | partial | ✓ | partial | **Improve**: one sentence + "wait" cue, audio-first |
| Activity video library | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | **Reject as core**: pulls adult gaze to screen; short demo clips only where a skill must be seen |
| Milestone tracker | ✓ | ✗ | ✓ | partial | ✓ | ✗ | ✓ | **Parity** with careful referral language |
| New-words log | partial | ✗ | ✗ | ✗ | partial | ✗ | ✗ | **Differentiate**: Word Garden, any language, signs count |
| Conversational-turn feedback | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate**: Talk Tally (on-device, opt-in) + tap tally |
| Personalised daily plan | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | **Parity**, from human-written prompt library |
| AI chat assistant for parents | ✓ | ✗ | partial | ✗ | ✗ | ✗ | ✗ | **Defer to V2**: scoped Q&A with citations only; no open chat at MVP |
| Multi-caregiver sharing | ✓ | ✗ | ✓ | ✗ | partial | ✗ | ✗ | **Parity** (Family Hub) |
| Clinician/teacher sharing | partial | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate**: consented SLP/EHS view |
| Spanish / home language | ✓ | partial | partial | ✓ | partial | ✓ | partial | **Parity** (ES at MVP) |
| Songs & rhymes | partial | ✓ | ✗ | ✗ | partial | ✗ | ✗ | **Parity**, audio-only, captioned |
| Face filters / child video selfie | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject**: child-facing, biometric-adjacent data under COPPA 2025 |
| Streaks / push nagging | partial | partial | ✗ | ✗ | partial | ✗ | ✗ | **Reject**: gentle weekly goal, pause days only |
| Trial that auto-converts silently | ✓ [M] | ✓ [V] | ✓ [M] | ✓ [M] | ✓ [M] | n/a | ✓ | **Reject**: price before trial, 3-day reminder, one-tap cancel |

## 4. Recommended feature set

| ID | Feature | Description | Rationale (competitor source / user need) | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| BB-01 | **Moment Cards** ★ | Routine-anchored prompt: one thing to say, one "wait 5 seconds" cue, one expansion example ("If Leo says 'duck', you say 'Yellow duck! Duck swims.'"). Read aloud to the parent on request. | Vroom routine model [V]; LENA serve-and-return [V2]; our need for "one thing now" | Differentiate | MVP | Must |
| BB-02 | **Routine picker** | Six routines at launch: meals, bath, dressing/nappy, car/stroller, play, bedtime. One tap to get a card for "now". | Parents' day is routine-shaped (Vroom, Huckleberry) [V] | Parity | MVP | Must |
| BB-03 | **Word Garden** ★ | Parent taps or says a new word the child used (or a sign / AAC symbol). Grows a calm illustrated garden; shows vocabulary over time, any language. | Milestone tracking is table stakes (Kinedu, BabySparks) [V]; bilingual and signing families under-served [I] | Differentiate | MVP | Must |
| BB-04 | **Talk Tally (opt-in, on-device)** ★ | During a chosen 10–20-minute routine, the phone estimates adult↔child turns using on-device voice-activity and speaker-type detection. **No audio stored or uploaded, no transcription.** Shows "about 14 back-and-forths" with a weekly trend. | LENA shows turn feedback shifts behaviour [V2]; no app offers it [I] | Differentiate | MVP (beta flag) | Should |
| BB-05 | **Tap Tally** | Manual alternative: tap a big button each time the child "serves" (a word, sign, point, babble). Works for signing and AAC families and when the mic is off. | Lumen P7 (never voice-only); Dani persona | Lumen | MVP | Must |
| BB-06 | **Songs & rhymes (audio-only)** | 30 short, hand-recorded rhymes with gestures, played through the phone speaker while the parent sings along; captions and a lyric card. | Speech Blubs/Kinedu include songs [V]; rhymes support phonological awareness [M] | Parity | MVP | Should |
| BB-07 | **Weekly one-screen summary** | "This week: 18 talk moments, 6 new words, most talk at bath time. Try: car-ride cards." | Research paper need #7 (proof parents can see) [V] | Improve | MVP | Must |
| BB-08 | **Milestone guide with careful signposting** | Age-banded communication milestones (based on public CDC "Learn the Signs. Act Early." checklists [M]) with "talk to your pediatrician or Early Intervention" links. **No scores, no diagnosis.** | Kinedu/BabySparks trackers [V]; Priya persona; FDA device boundary | Parity + Lumen | MVP | Must |
| BB-09 | **Family Hub sharing** | Invite co-parents, grandparents, childminders; each gets the same cards; tally merges. | Kinedu account sharing [V]; Huckleberry caregivers [M] | Parity | MVP | Must |
| BB-10 | **Home-language mode** | UI and cards in English and Spanish at MVP; Word Garden accepts any language; "say it in your home language" tip on every card. | Vroom EN/ES [V]; Two Words synergy | Parity | MVP | Must |
| BB-11 | **Gentle reminders (adult-set)** | Optional nudges at routine times the parent chooses ("bath at 6:30"). No streaks, no loss framing, easy mute. | Lumen P9, P15; Huckleberry routine timing [M] | Lumen | MVP | Should |
| BB-12 | **Fair-billing & free core** | Moment Cards, Tap Tally, Word Garden, songs are free forever; Family plan adds personalised plans, trends, sharing with professionals. | Speech Blubs complaints [V]; Research paper need #1 | Lumen | MVP | Must |
| BB-13 | **Personalised prompt plan** | Weekly plan selected from the human-written library by age, interests ("trucks, cats"), new words and routine patterns. AI selects and slot-fills; it does not free-write. | Kinedu/BabySparks personalisation [V] | Improve | V1 | Should |
| BB-14 | **Professional share (SLP / EHS / pediatric)** | Parent-consented, read-only view of Word Garden, tally trends and chosen goals; exportable PDF for appointments. | LENA Grow/Start used by Head Start [V]; Priya persona | Differentiate | V1 | Should |
| BB-15 | **SMS / print "leave-behind" packs** | 7-day card packs by SMS or printable PDF for families with limited data or low tech confidence. | Home-visitor persona; concierge test | Differentiate | V1 | Could |
| BB-16 | **Grandparent seat** | Large-type, voice-first mode with a single "Give me an idea" button. | Rosa persona; Lumen 60+ parameters | Lumen | V1 | Should |
| BB-17 | **More home languages** | Portuguese, Mandarin, Vietnamese, Arabic, Tamil card sets (human-translated and culturally reviewed). | Bilingual demand [I] | Improve | V2 | Could |
| BB-18 | **"Ask a speech question" with citations** | Scoped Q&A over a vetted knowledge base (ASHA/CDC-sourced), with citations, no open chat, escalation to professional resources. | Kinedu AI assistant [V] | Parity (guarded) | V2 | Could |

★ **Signature features:** Moment Cards (BB-01), Word Garden (BB-03), Talk Tally (BB-04). MVP = BB-01 to BB-12 (12 features), which covers the full loop: pick routine → card → talk → tally → word logged → weekly summary.

## 5. Core experience & key user flows

**Core loop.** Routine starts → parent opens app (or hears a scheduled nudge) → one Moment Card → parent talks, waits, expands → optional tally → "Nice. Any new words?" → close. Target: under 20 seconds of screen attention per card [E].

**Flow 1: Onboarding (≤3 min to first card).**
1. Price-and-privacy screen first: "Free forever: cards, songs, word garden. Family plan $69/yr, shown now, no card needed." Privacy in 3 plain lines ("We never record your child. Talk Tally is off. You choose.").
2. Child's first name (or nickname) + birth month. Home language(s). Optional: 3 interests (tap icons).
3. "When do you have the most time together?" (tap routines).
4. Sensory/text: large text? read cards aloud? (defaults follow OS settings).
5. First Moment Card for the current time of day. Done.

**Flow 2: Core session (a Moment Card during bath).**
1. Tap "Bath" (or the card is already waiting).
2. Card: "Name 3 body parts as you wash. Point, say, **pause 5 seconds**. If Leo points or babbles, add one word: 'Toes! Wiggly toes.'" Play button reads it aloud.
3. Optional "Start Talk Tally" (if enabled) or tap-tally button.
4. Parent puts phone down. Tally runs with the screen dimmed (a single soft glow, no animation).
5. End: "About 11 back-and-forths. Any new words?" Big mic or keyboard to log "toes". Garden grows one sprout.
6. Natural end: "That's it. See you at dinner." No "next card" autoplay.

**Flow 3: Caregiver view (grandparent / co-parent).** Invite link by text → grandparent opens in large-type mode → sees today's cards and Leo's newest words ("Leo said 'moon' on Tuesday. Try pointing at the moon tonight!") → logs their own moments; tallies merge into one family week.

**Flow 4: My Needs & settings.** One tap from the header: text size, read-aloud on/off, voice speed, sign/AAC mode (changes wording from "say" to "say or sign" and hides mic features), languages, Talk Tally permission (with plain explanation), reminders, who can view.

**Flow 5: Billing & cancellation.** Settings → Plan → price and renewal date in large type → "Cancel" (one tap, confirmation screen with no guilt copy) → "Pause for up to 3 months" offered as an option, not a barrier. Trial reminder 3 days before charge (email + in-app).

**Information architecture.** Tabs (max 4, text + icon): **Now** (card for this moment) · **Words** (Word Garden) · **Week** (summary) · **Family** (people, settings, plan). The Sensory/My Needs control sits in the header on every screen.

**Session design.** Default is one card per routine, 3–6 cards a day suggested, no minimum. Talk Tally sessions are capped at 20 minutes and end themselves with a soft chime and vibration. No infinite feeds; the card list ends ("That's today's ideas").

## 6. Inclusive, accessible & sensory design spec

Babble Buddy's user is an adult, but it shapes a toddler's environment, so the design protects **both**: an adult UI that's easy under stress, and a phone that never becomes a toy.

**Sensory Dial defaults.** Default **Calm** (the app is used around a toddler; a phone that lights up and sings attracts little hands).

| Level | What changes in Babble Buddy |
|---|---|
| Calm (default) | Static cards; no animation; Word Garden grows with a single cross-fade; sounds off except read-aloud; dimmed screen during Talk Tally |
| Balanced | Gentle garden growth animation; soft chime at card end |
| Lively | Garden sway animation; song previews auto-play (still no flashing, WCAG 2.3.1) |

**Input modes per task.**

| Task | Tap | Voice | Keyboard | Switch | Sign/AAC-aware | Notes |
|---|---|---|---|---|---|---|
| Get a card | ✓ | ✓ ("Give me an idea") | ✓ | ✓ | n/a | |
| Log a word | ✓ (picture chips) | ✓ | ✓ | ✓ | ✓ (log a sign / AAC symbol by name) | |
| Count turns | ✓ Tap Tally | ✓ Talk Tally (opt-in) | ✓ (space bar) | ✓ | ✓ (Tap Tally counts signs, points, AAC) | Never mic-only |

**Targets and gestures.** Adult UI with one-handed use in mind (the other hand holds a toddler): primary buttons ≥56 dp and in the bottom third of the screen; Tap Tally button ≥ 1/3 of the screen; no swipe-only actions; no long-press. Palm rejection on the tally screen.

**Reading and typography.** Card copy at or below US grade 4 reading level [E target] (many parents read little or are reading in a second language); every card has read-aloud; Dynamic Type to the largest size without truncation; sans-serif, 1.5 line height, off-white background; no italics or ALL CAPS for emphasis (Lumen P6).

**Audio.** Channels: read-aloud voice, songs, chimes; each on its own slider. All songs captioned with lyric cards; all chimes have a haptic + visual twin. Peak loudness capped (songs are near a toddler's ears).

**Deaf and signing families.** "Say or sign" wording; ASL/BSL gesture videos for 50 core signs (V1), captioned; Tap Tally as a first-class method; no feature assumes the parent hears.

**Age-respectful themes.** Adult UI themes: "Garden" (illustrated) and "Plain" (minimal, photo-free). Two themes minimum (P13).

**Applicable Lumen principles.**

| P# | App-specific acceptance criterion |
|---|---|
| P1 | With Reduce Motion on, 0 animations; Sensory Dial reachable in 1 tap from every screen |
| P2 | Every chime has a haptic and visual twin; all songs captioned |
| P3 | Four fixed tabs; no layout change between cards |
| P4 | All actions single-tap; primary targets ≥56 dp; Tap Tally ≥ 1/3 screen |
| P5 | Card copy ≤ grade 4 [E]; every card readable aloud |
| P6 | BDA defaults; WCAG 1.4.12 text-spacing override works |
| P7 | Turn counting possible by tap, voice and switch; words loggable by tap, voice, keyboard |
| P8 | No "missed day" states; undo on every logged word |
| P9 | Card list ends each day; no autoplay; Talk Tally self-ends at 20 min |
| P10 | Passkey / magic-link sign-in; no passwords to remember |
| P11 | No timeouts on voice logging; tally wait windows configurable |
| P12 | Sign/AAC mode, text size, languages all free and portable to other Lanternling apps |
| P13 | Two adult themes |
| P14 | First card in ≤3 minutes; weekly summary one screen |
| P15 | Weekly goal chosen by parent; pause days; no streak loss |
| P16 | Late talkers, signing, AAC and bilingual children represented in examples; no "behind/normal" language |
| P17 | Claims register: "based on serve-and-return research", never "boosts IQ" |
| P18 | No child audio stored or sent; Talk Tally off by default; DPIA complete |

**Target Lumen audit score:** ≥22/24 (expected weak point: item 1, screen reader on the garden visual, mitigated by a text list view).

## 7. AI specification & guardrails

**What AI does.**
- **Prompt selection and slot-filling (V1):** a recommender chooses cards from a **human-authored library** (target 600 cards at V1 [E]) using age, routines, interests and logged words, and fills slots ("Leo", "trucks", "moon"). An LLM may paraphrase within a template for variety, but only into pre-approved variants reviewed by our early-language editor (an SLP).
- **Talk Tally (on-device):** voice-activity detection + speaker-type classification (adult vs. child vocalisation) + turn logic (alternation within ~5 s, matching LENA's definition [V2]). Runs fully on-device; no speech-to-text, no audio persisted beyond a rolling in-memory buffer of a few seconds.
- **Word logging by voice:** the *parent's* speech is transcribed (on-device ASR where available) to log the word; the child is never the ASR target.

**What AI does not do.** No chat persona or named "buddy" character that talks to the child or parent as a friend (the app name refers to the parent's tool; there is no avatar). No assessment or diagnosis of the child's speech. No emotion or stress inference from voice. No generation of new developmental advice at runtime.

**Pedagogical policy.** Every card follows one of five evidence-based strategies used by SLPs and in Vroom/LENA-style guidance: *follow the child's lead, wait/pause, expand, offer choices, narrate (self-talk/parallel talk)* [M]. Every card is tagged to a strategy and an age band; editorial review by an SLP is required before a card enters the library.

**Safety.**
- Referral language for milestones is scripted, reviewed by a pediatric advisor, and never computed from Talk Tally (tally counts are too noisy to flag risk, and doing so would move us toward an FDA device claim).
- COPPA: child vocalisations are the child's personal information even if never stored [I]; we treat Talk Tally as child-data processing that needs verifiable parental consent, with a written retention schedule ("none").
- AI disclosure: "Cards are written by our speech team. The app picks which card to show you."

**Evaluation plan.**
- Talk Tally accuracy: compare against human-coded turns on consented, adult-recorded research sessions (n≈40 families, diverse languages and accents, including bilingual homes, a late-talker group and noisy kitchens). Targets: Pearson r ≥0.8 with human counts per session and mean absolute error ≤25% [E targets]; report by language group and noise level; ship only if every group meets the target, otherwise show "ranges" rather than numbers for that group.
- Prompt quality: 100% human review of card library; monthly 5% sample audit of slot-filled cards for errors (wrong name, wrong language).

**Cost and latency [E].** On-device tally: zero marginal cloud cost; battery ≤5% per 20-minute session target. Card selection: server-side lightweight ranking, <$0.001 per card. Optional LLM paraphrase pre-computed in batches, not at runtime.

## 8. Data, privacy & compliance

**Data inventory.**

| Data | Why | Where processed | Retention |
|---|---|---|---|
| Parent account (email/passkey) | Sign-in, billing | Cloud | Life of account + 30 days |
| Child nickname, birth month, languages, interests | Card selection | Cloud (encrypted) | Life of account; deletable anytime |
| Logged words (text) | Word Garden, summary | Cloud (encrypted) | Life of account; exportable |
| Talk Tally counts (numbers only) | Trends | Device → cloud (counts only) | Life of account |
| Child/adult audio | Turn estimation | **On-device only**, in-memory seconds | **Not retained** |
| Usage analytics | Product improvement | First-party only, no third-party SDKs | 13 months, aggregated |

**Applicable regimes.** COPPA 2025 (the service is directed to parents, but collects a child's information and processes child voice on-device; we comply fully: verifiable parental consent, separate consent for any sharing, no training on child data). UK AADC and state design codes (high-privacy defaults, no nudges). EU AI Act: no emotion recognition; Art. 50 disclosure. **FDA device boundary:** we make no diagnostic or screening claim; milestone content is public-health education with referral. FTC §5: claims only at the evidence tier achieved. HIPAA: not a covered entity unless a clinic contracts with us for B2B; if so, sign a BAA and segregate data (V1 decision).

**Consent flows.** (1) Parent account consent. (2) Separate, off-by-default Talk Tally consent explaining on-device processing. (3) Separate consent for each professional share, time-limited. (4) Research consent (separate, opt-in, paid) for any dataset used to evaluate tally accuracy; never pooled into model training without a further separate consent.

**Store policy.** Not in the Kids category (adult-directed), but we still follow Kids-category standards voluntarily: no third-party ads or analytics, parental gate on external links. Google Play: declare in the Families policy form as "not primarily child-directed" while meeting the same data practices.

## 9. Monetization & go-to-market

**Pricing tiers.**

| Tier | Price | Includes |
|---|---|---|
| Free forever | $0 | Moment Cards (daily set), Tap Tally, Word Garden, songs, milestone guide, 1 co-caregiver |
| Lanternling Family | ≈$9.99/mo or $69/yr (all 7 apps, up to 3 children) | Personalised plan, Talk Tally trends, unlimited caregivers, professional share, SMS/print packs |
| B2B2C licence | $12–25 per family per year [E] | EHS/home-visiting dashboards (aggregate, consented), bulk SMS packs |

Benchmark: Huckleberry Plus $58.99/yr, Kinedu $79.99/yr, Speech Blubs $59.98/yr, BabySparks $23.99/yr, Vroom free [V]. A standalone Babble Buddy at $69/yr would be at the top of this range; bundled into the 7-app Family plan, it is priced below Kinedu for more value [I].

**Fair-billing charter** (Lumen §3.7): price before trial; 3-day reminder; one-tap cancel; summer/parental-leave pause; accommodations never paywalled.

**Channels.** Pediatric practices and "Reach Out and Read"-style prescribing [I]; Early Head Start and home-visiting programs (LENA's channel proves budget exists [V]); SLP recommendations for waitlisted families; public libraries (baby story-time handouts with QR); parent creators focused on speech.

**ASO.** Keywords: "toddler talking", "late talker", "speech development toddler", "baby first words tracker", "serve and return". Category: Education (iOS), Parenting (Play). **Accessibility Nutrition Label** at launch: VoiceOver, Voice Control, Larger Text, Sufficient Contrast, Reduced Motion, Captions, all claimed only after the audit passes.

**Launch markets.** US (EN/ES) first; UK and Canada in V1 (UK spellings, BSL signs); Mexico/LatAm via Spanish content (V2).

## 10. Success metrics

- **North-star:** weekly talk moments per active family (target ≥10 at week 4 [E]).
- **Inputs:** % of families using ≥1 card on ≥4 days/week (≥60%, from the discovery threshold); new words logged per week; % families with ≥2 caregivers; Talk Tally opt-in rate (expect 20–35% [E]; low is acceptable).
- **Guardrails:** Sensory Comfort ≥4/5 (parent-rated); zero billing complaints; child-screen-time added = 0 (verified by diary: the child did not hold the phone); average screen-on time per card ≤30 s [E]; uninstall reasons coded for "made me feel guilty".
- **Learning / outcome measures:** parent-reported conversational turns and vocabulary (MacArthur-Bates CDI short form [M]) pre/post in a pilot; evidence tier plan: E4 (logic model) at launch → E3 (pre/post pilot with an EHS partner) → E2 (quasi-experimental with LENA-coded comparison) in Year 2.
- **Retention targets:** D1 55%, D7 35%, D30 20%, DAU/MAU ≥25% [E]. Benchmarks for parenting trackers are high because of daily logging (Huckleberry-type apps) [M]; we expect lower DAU but higher "usefulness" ratings.

## 11. Validation plan (no-code)

**Riskiest assumptions (ranked).**
1. Parents will use a coaching app themselves, rather than hand the device to the child (L2).
2. One-sentence cards change talk behaviour enough for parents to notice value within 2 weeks.
3. Phone-based turn estimation is accurate enough in real homes (noise, multiple children, bilingual speech).
4. Parents will pay for Babble Buddy inside the Family plan (not only use the free core).
5. Professionals (SLPs, EHS) will recommend it.

**Experiments.**

| # | Method | Sample | Success threshold | Kill / rethink |
|---|---|---|---|---|
| E1 | **SMS concierge**: 2 weeks of daily routine prompts by text, human-written and personalised by a coordinator | 30 families (≥6 bilingual, ≥3 late-talker, ≥2 Deaf/signing parents, ≥5 grandparent carers) | ≥60% use prompts on ≥4 days/week; ≥50% report "more talking" | <30% → rethink format (e.g., print cards, audio-only) |
| E2 | **Tap-tally diary**: paper tally cards during 3 routines/week | Same 30 | ≥50% complete ≥4 tallies; parents report tally "useful" ≥4/5 | <25% → drop tally from MVP |
| E3 | **Talk Tally feasibility spike** (research, not product code): off-the-shelf on-device VAD + speaker-type model vs. human coding on consented recordings | 40 sessions across 4 language groups | r ≥0.8, MAE ≤25% in every group | Any group fails → ship tap tally only; reconsider V2 |
| E4 | **Figma prototype usability** (one-handed, while holding a doll) incl. VoiceOver, Dynamic Type XXL, Deaf parent | 12 adults | First card ≤3 min; SUS ≥75; 0 critical a11y failures | SUS <65 → redesign |
| E5 | **Fake-door + price test** on landing page (adults only) | ≥1,500 visitors | ≥8% waitlist; ≥30% pick paid plan | <3% waitlist → reposition |
| E6 | **Professional interviews** | 6 SLPs, 4 EHS/home-visiting leads, 3 pediatricians | ≥50% would recommend; ≥2 programs agree to pilot | <2 interested → deprioritise B2B2C |

**Mapping to Discovery Plan.** E1–E2 → WP4 concierge (L2); E3 → WP4 feasibility spikes; E4 → WP4 accessibility rounds; E5 → WP5 smoke test (L1); E6 → WP2 interviews and WP5 channel validation (L4).

## 12. Build handoff (post-Gate 2)

**Epic BB-E1: Moment Cards.**
- *Story:* As a parent, I want a card for the routine I'm in, so I know what to say right now.
  - **Given** it is 6:30 pm and bath is set as a routine, **when** I open the app, **then** a bath card for my child's age is shown within 1 s, with a play button that reads it aloud.
  - **Given** I have finished a card, **when** I tap "Done", **then** no new card auto-appears and I see "See you at [next routine]".
  - **Given** Sign/AAC mode is on, **when** any card is shown, **then** all "say" instructions read "say or sign".

**Epic BB-E2: Word Garden.**
- **Given** I tap "+ word" and say "moon", **when** on-device ASR returns "moon", **then** I see the word to confirm before it's saved, with an undo for 10 s.
- **Given** my child uses Spanish and English, **when** I log "luna", **then** it is tagged Spanish and counted in total words, never as "extra" or "confusing".
- **Given** VoiceOver is on, **when** I open the garden, **then** a list view reads each word, language and date.

**Epic BB-E3: Tallies.**
- **Given** Talk Tally is off (default), **when** I start a routine, **then** the microphone is never activated and only Tap Tally is offered.
- **Given** I enabled Talk Tally with consent, **when** a session runs, **then** no audio is written to disk or network (verified by network and file-system inspection in QA), and the session ends at 20 min with a haptic + visual cue.
- **Given** I use Tap Tally with a switch, **when** I press the switch, **then** the count increments with a haptic tick and a visible number.

**Epic BB-E4: Weekly summary & milestones.**
- **Given** a week has ended, **when** I open "Week", **then** I see one screen: talk moments, new words, the routine with most talk, and one suggestion.
- **Given** my child is 24 months and I view milestones, **when** I read the section, **then** there are no scores or colours implying "behind", and a "talk to your pediatrician / Early Intervention" link is present.

**Epic BB-E5: Family Hub & billing.**
- **Given** I invite a grandparent, **when** they accept, **then** they see large-type mode by default and their tallies merge into the family week.
- **Given** I am subscribed, **when** I tap Cancel, **then** cancellation completes in one confirmation step, and I receive a confirmation email.
- **Given** a trial ends in 3 days, **then** an email and in-app notice state the exact date and price.

**Non-functional requirements.** Card load <1 s on a 2019 mid-range Android; full offline card library for the week (cached); iOS 16+, Android 10+, web (read-only summary); WCAG 2.2 AA; EN/ES at launch with human translation; encryption at rest and in transit; no third-party SDKs except payment; privacy-preserving crash reporting (first-party).

**QA focus.**
- AT matrix: VoiceOver, TalkBack, Switch Control, Voice Control, Dynamic Type XXL, Reduce Motion, one-handed use, colour-blind modes.
- Sensory A/B: Calm vs. Balanced with parents (does the phone attract the toddler?).
- AI safety: slot-fill injection (a child's name field containing instructions), wrong-language cards, referral copy never triggered by tally data.
- COPPA: mic never on without consent; no audio in files, logs or crash reports; deletion within 30 days of request; separate consent records.
- Billing: price before trial, reminder at T-3 days, one-tap cancel on iOS/Android/web, pause flow, refund policy text.

**Dependencies on the shared platform.** Lumen design system (tokens, Sensory Dial, header control); My Needs profile (sign/AAC mode, text size, languages); Family Hub (accounts, caregivers, billing); privacy stack (consent ledger, on-device audio policy, deletion); evidence engine (pilot instruments, CDI short-form hosting).

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Parents don't open a coaching app mid-routine | M | H | Scheduled nudges at chosen times; printable cards; smart-speaker/audio-only mode in V2 |
| Talk Tally inaccurate for some languages or noisy homes | H | M | Tap Tally first-class; show ranges not numbers where accuracy is lower; per-group WER/agreement gates |
| Perceived surveillance ("the app listens to my child") | M | H | Off by default; on-device only; "mic on" indicator; plain-language privacy; third-party audit |
| Parents misread milestones as diagnosis; anxiety | M | H | Scripted referral language; pediatric advisor review; no scores |
| Free tier cannibalises paid | H | M | Paid value in personalisation, trends, sharing; bundle across 7 apps |
| Vroom (free, foundation-funded) is "good enough" | M | M | Feedback loop (tally, words, summary) and caregiver sharing Vroom lacks |
| B2B partners require HIPAA/FERPA | M | M | Decide BAA scope in V1; aggregate-only dashboards |

**Open questions.** Is "Babble Buddy" read as a child-facing app by parents (naming test)? Can on-device speaker-type models run acceptably on low-end Android? Should Talk Tally ship at all in MVP, or wait for E3 results? Would EHS programs accept an app instead of LENA hardware, or alongside it?

## 14. Sources
- [V] Romeo et al. 2018, *Psychological Science*: https://journals.sagepub.com/doi/abs/10.1177/0956797617742725
- [V2] LENA Grow outcomes: https://www.lena.org/programs/lena-grow/effectiveness/
- [V2] LENA Start virtual results: https://www.lena.org/blog-post/page/5/
- [V2] LENA FAQ (turn definition): https://www.lena.org/frequently-asked-questions/
- [V] Kinedu App Store: https://apps.apple.com/us/app/kinedu-baby-development/id741277284 · MIT Solve: https://solve.mit.edu/solutions/7799
- [V] Speech Blubs Play: https://play.google.com/store/apps/details?id=org.blubblub.app.speechblubs&hl=en_US · Trustpilot: https://www.trustpilot.com/review/speechblubs.com · Educational App Store review: https://www.educationalappstore.com/app/speech-blubs-language-therapy
- [V] Huckleberry App Store: https://apps.apple.com/us/app/huckleberry-baby-tracker/id1169136078 · pricing: https://huckleberrycare.com/pricing
- [V] The Wonder Weeks App Store: https://apps.apple.com/us/app/the-wonder-weeks-baby-leaps/id529815782 · Sensor Tower: https://app.sensortower.com/overview/529815782?country=US
- [V] BabySparks: https://babysparks.com/ · App Store: https://apps.apple.com/us/app/babysparks-development-app/id794574199
- [V] Vroom: https://www.vroom.org/ · App Store: https://apps.apple.com/us/app/vroom-early-learning/id885948312
- [V] Lovevery app: https://blog.lovevery.com/product-recommendations/the-lovevery-app-for-parents/
- [V] AAP 2026 policy statement and video-deficit notes: [raw 04 §B3–B4](../../../research/raw/04-neurodivergent-and-inclusive-ux.md)
- [V2] Speech Blubs US iOS volume (Sensor Tower via raw 02): [raw 02](../../../research/raw/02-apple-app-store-top30.md)
- [M] CDC "Learn the Signs. Act Early." milestone checklists; MacArthur-Bates CDI; SLP strategy taxonomy (to verify in WP1)

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (lead) |
| **Ships in** | Lanternling app (S1) |
| **Build wave** | 1c |
| **Pre-discovery priority score** | 86/100 [I] |
| **Consumes engines** | EN-07, EN-09, EN-10 |
| **Studio features used** | SX-04, SX-06, SX-07, SX-25, SX-26 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = BB-01, BB-02, BB-03, BB-05, BB-06, BB-08.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| BB-E1 | **Hands-free mode** | Moment prompts delivered as audio in the car or kitchen (no screen), via phone audio or smart speaker where platform terms allow for child-directed use. |
| BB-E2 | **Early-intervention signposting** | When the milestone guide flags a possible concern, show local early-intervention services (e.g., IDEA Part C in the US) and 'talk to your pediatrician' guidance. Never a diagnosis. |
| BB-E3 | **Remote co-play invite** | A distant grandparent joins a Moment Card by link, via SX-06. |

### 15.3 New validation question
Does hands-free delivery raise prompt use (≥4 days/week) versus in-app cards? SMS/audio concierge, n=30.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 5 | 4 | 5 | 4 | 3 | 4 | 5 | 4 |

# Tap & Wonder: App Strategy & Product Specification

> **Venture:** Lanternling · **App #:** 2/7 · **Ages:** 1–3 (co-play with an adult) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/01-lanternling-early-years.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given; mostly search snippets, store pages were proxy-blocked) · [V2] secondary or vendor source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A calm first "picture book that answers back": one tap anywhere and a real duck quacks softly and the word "duck" is spoken, then the session winds down to a sleepy ending on its own. |
| **Primary user / buyer** | Toddlers 12–36 months **with** a parent, grandparent or childminder beside them. Buyer: parents (and gift-giving grandparents). |
| **Core job-to-be-done** | "When my toddler wants the phone, I want five minutes of something gentle we can do together, that names real things and ends without a meltdown, so I don't feel guilty or face a fight." |
| **Category on the stores** | Apple: Kids › Ages 5 & Under (Education). Google Play: Teacher Approved / Families, Educational › Ages 5 & Under. |
| **Top competitors** | Bebi: Baby Games (10M+ Play) · Sago Mini World (10M+ Play) · Bimi Boo Baby & Toddler Games (5M+ Play) · Khan Academy Kids (10M+ Play) · Pok Pok (2021 ADA) · Toca Boca Jr / Piknik · Fisher-Price Play & Learn · Hey Duggee (BBC) |
| **Our wedge** | 1. **Built for 12–24 months**, not "2–8": whole-screen single tap, real photos, one concept per screen. 2. **It ends itself** with a designed "sleepy scene" and a parent-set length. Parents report meltdowns at takeaway even with Pok Pok. 3. **Co-play is designed in**: a quiet line for the adult on every scene, and a real-world follow-up. |
| **Business model** | Free forever core (basic scene packs), per the vision. More scene packs, languages and the grandparent voice feature in the Lanternling Family plan (≈$9.99/mo or $69/yr, all 7 apps). |
| **North-star metric** | **Weekly co-play sessions ending by design** (sessions that reach the sleepy scene and show a co-play card). |
| **MVP candidate?** | **Later / conditional.** The vision's likely Year-1 MVP trio is Babble Buddy, Sound Garden, Story Lantern. Tap & Wonder is cheap to build and is the free-tier "front door", so it is a strong Year-1 add if the E1 dyad test passes. |

## 2. Problem & users

**Problem statement.**
- Almost nothing in the top 30 is built for ages 1–3, and toddler screen time is mostly YouTube [V] ([Research paper §4.4](../../01-research-paper.md)).
- The toddler apps that do exist are loud, busy and drag-based. 3-year-olds succeed on basic touch tasks only ~73% of the time vs. >89% for 5+ (Vatavu 2015) [V]. Most "baby games" are tuned for 2–5, not for a 15-month-old's palm swipe.
- Contingent interaction helps: toddlers aged 24–36 months who touched the screen to make an on-screen person label an object learned the word better than those who watched passively; effects depend on age and working memory [V] ([Kirkorian et al. / *Child Development* 2016 and related](https://academic.oup.com/chidev/article/87/2/405/8258405); [PubMed 33716887](https://pubmed.ncbi.nlm.nih.gov/33716887/)). Under ~18–24 months, the live adult matters most (video deficit) [M].
- Parents ask for "calm" apps with natural stopping points, and still report meltdowns at takeaway. One Pok Pok reviewer disagreed with the "non-addictive" claim because her 3-year-old gets upset when the device is taken away [V] ([Common Sense parent reviews](https://www.commonsensemedia.org/app-reviews/pok-pok-playroom/user-reviews/adult)).
- The AAP's 2026 statement puts responsibility on design and co-engagement [V].

**Personas.**

| Persona | Snapshot | Needs |
|---|---|---|
| **Maya, 34, and Leo (2)** | Dinner-prep screen time; guilt; takeaway meltdowns. | 5–10 min, calm, ends itself, gives her a line to say when she sits with him. |
| **Sam, 3, autistic, sensory-sensitive** (with dad) | Loves trains and predictability; overwhelmed by loud rewards. | Same layout every time; no surprises; sound off but visual + haptic feedback; train pack. |
| **Ava, 22 months, cerebral palsy, uses a single switch** (with mum) | Can't do precise taps; switch-toy user at nursery. | Whole screen *is* the button; external switch support; no timing demands. |
| **Grandma Rosa, 67** | Minds grandkids; low tech confidence. | One big "Start" button; no ads; nothing to buy by accident; her own voice naming things. |

**Needs & wants.**

| Need | Evidence | Response |
|---|---|---|
| Calm, non-addictive, natural stopping | Pok Pok demand + complaints [V]; Research paper need #6 | Sensory Dial Calm default; parent-set 3/5/10-min session; sleepy-scene ending |
| Truly toddler-sized interaction | Vatavu 2015 [V] | Whole-screen hit zone; no drag, pinch, double-tap |
| Learning that transfers to the real world | JME/video-deficit evidence [M]; contingency studies [V] | Real photos + spoken words; co-play line + off-screen follow-up ("Find something yellow") |
| No ads, no IAP pressure | Bebi and Pok Pok market "no ads" [V]; Lingokids upsell complaints [V] | No ads ever; purchases only in the parent area behind a gate |
| Price transparency | Pok Pok "no pricing info until after download" complaint [V] | Price shown on store listing text and first screen |
| Accessibility for motor and sensory differences | Lumen P4, P7; Jinja's Garden inclusivity finalist [V] | Switch, external-keyboard and Voice Control start; sound-free mode with haptics |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Bebi: Baby Games for 2-4y** | Bebi Family | **10M+** Play, 243K reviews [V] | Free + subscription; "no ads" [V] | 4.6 Play [V] | 500+ games; offline; parental gate [V] | Most content locked (typical for category) [M] | Bright, cartoon; many drag tasks [M] | [Play](https://play.google.com/store/apps/details?id=com.happytools.learning.kids.games&hl=en_US) · [Bebi](https://bebi.family/en/game/baby-games-1) |
| **Sago Mini World** | Spin Master (Piknik) | **10M+** Play (49K reviews); 0.5–0.9M US iOS/yr [V] | $7.99/mo; Piknik Unlimited $14.99/mo; web $49.99/yr (promo $24.99) [V] | 3.7 Play; 4.3 iOS (~66K) [V] | Open-ended, wordless, gentle; many awards [V] | Bundle confusion; standalone apps removed from sale [V] | Wordless (pre-reader friendly); Jinja's Garden: 2026 ADA Inclusivity finalist, won Games Interaction [V] | [Play](https://play.google.com/store/apps/details?id=com.sagosago.World.googleplay&hl=en_US) · [Help](https://help.sagomini.com/article/418-sago-mini-standalone-apps-removed-from-sale) · [ADA 2026](https://developer.apple.com/design/awards/) |
| **Bimi Boo Baby & toddler games** | Bimi Boo Kids | **5M+** Play (~7.3M lifetime est.) [V] | Subscription or lifetime [V] | 4.6 Play (11.9K) [V] | Simple sorting/puzzle games for 2–5 [V] | Paywall after a few games [M] | Many drag-to-target tasks [M] | [Play](https://play.google.com/store/apps/details?id=com.bimiboo.birthday&hl=en_US) |
| **Khan Academy Kids** | Khan Academy | **10M+** Play; 4.7 (~42K) [V] | 100% free [V] | 4.7–4.8 [V] | Free, calm, narrated, 4,000+ activities [V] | Built for 2–8; toddlers struggle with tasks; "one more" pull [V] | Library text not enlargeable; LOW-MED sensory [V] | [raw 01/02](../../../research/raw/02-apple-app-store-top30.md) |
| **Pok Pok** | Pok Pok (Series A) | Six-figure MRR (2024), subscribers 9× in a year [V2]; 2021 ADA [V] | $6.99/mo, $45.99/yr; lifetime promos $60 (reg. $250) [V] | High 4s [M] | "No levels, winning or losing"; soft hand-recorded sounds [V] | Pricing not shown before download; "not non-addictive" [V] | The calm-tech benchmark; 2–8 target, not toddler-first [V] | [TechCrunch](https://techcrunch.com/2024/06/18/now-a-series-a-startup-kids-app-and-digital-toy-pok-pok-is-coming-to-android/) · [9to5Toys](https://9to5toys.com/2026/08/27/pok-pok-lifetime-subscription-drops-to-60-reg-250/) · [Common Sense](https://www.commonsensemedia.org/app-reviews/pok-pok-playroom/user-reviews/adult) |
| **Toca Boca Jr (Piknik)** | Spin Master | Part of Piknik bundle; not broken out [V] | Piknik $11.99/mo (promo $9.99) [V] | n/a | Toca Kitchen 2 etc. for little kids [V] | "Why does it say in-app purchases?" confusion [V] | Pretend play; moderate sensory [M] | [Piknik](https://playpiknik.com/) · [Help](https://help.sagomini.com/article/328-why-does-it-say-that-toca-boca-jr-has-in-app-purchases) |
| **Fisher-Price Play & Learn** | Mattel (Edujoy) | 100K+ Play; Laugh & Learn Puppy's Player 500K+ [V] | Free/IAP [M] | 4.4 iOS (509); 4.6 Play [V] | Familiar toy brand; baby cause-and-effect [V] | Small catalogue; brand-led [I] | Bright colours, music [M] | [App Store](https://apps.apple.com/us/app/fisher-price-play-learn/id6670388470) |
| **Hey Duggee: The Big Badge App** | BBC Studios | 10K+ Play [V] | $2.99 iOS [V] | 4.3 iOS (43); 3.7 Play [V] | Beloved characters; badges [V] | Tiny catalogue; aimed at 3–6 [V] | Character-led, moderate sensory [I] | [App Store](https://apps.apple.com/us/app/hey-duggee-the-big-badge-app/id1019167420) |

*Bluey apps (Bluey: Let's Play!) are licensed games for older preschoolers and were not verified this session [M].*

**Takeaways [I].** Volume leaders (Bebi, Sago, Bimi Boo) prove huge toddler-parent demand on Android. The design leaders (Pok Pok, Sago's Jinja's Garden) prove calm, wordless design wins awards. **Nobody targets 12–24 months specifically, nobody ends sessions by design, and nobody gives the co-playing adult a role.**

**Feature matrix.**

| Feature | Bebi | Sago World | Bimi Boo | Khan Kids | Pok Pok | Toca Jr | Fisher-Price | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Whole-screen single-tap interactions | partial | partial | ✗ | ✗ | partial | ✗ | ✓ | **Differentiate**: every scene works with one tap anywhere |
| Drag-to-complete tasks | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | partial | **Reject** as a requirement (tap alternatives only) |
| Real photos + spoken word | ✗ | ✗ | ✗ | partial | ✗ | ✗ | ✗ | **Differentiate** (real-world transfer) |
| Wordless / no reading needed | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Parity** |
| No ads | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | partial | **Parity** |
| Calm/low-stim default | ✗ | partial | ✗ | partial | ✓ | ✗ | ✗ | **Parity with Pok Pok**, plus Sensory Dial |
| Designed session ending | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate**: sleepy scene + parent timer |
| Adult co-play prompts | ✗ | ✗ | ✗ | partial | ✗ | ✗ | ✗ | **Differentiate** |
| Switch / external input | ✗ | partial [M] | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Offline | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | partial | **Parity** |
| Rewards/stickers/badges | ✓ | partial | ✓ | ✓ | ✗ | ✗ | partial | **Reject** (no extrinsic rewards for 1–3) |
| Character licence (Duggee/Bluey) | ✗ | own chars | own | own | ✗ | own | ✓ | **Reject** at MVP: cost, and licensed characters raise pull and stimulation |
| Price visible before trial | ✗ [M] | partial | ✗ | n/a | ✗ [V] | partial | n/a | **Improve** (fair billing) |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| TW-01 | **Wonder Scenes** ★ | Full-screen real photo (duck on a pond). One tap anywhere → one gentle response (duck paddles 1 s; soft quack; the word "duck" spoken once). Second tap → next attribute ("yellow duck"). | Contingency studies [V]; real-world transfer [M]; toddler touch data [V] | Differentiate | MVP | Must |
| TW-02 | **Whole-screen hit zone & palm rejection** | Any touch counts as one tap; multi-touch and palm contact ignored; 500 ms debounce so bangs don't skip scenes. | Vatavu 2015 [V]; Lumen P4 | Lumen | MVP | Must |
| TW-03 | **Parent-set session length + Sleepy Scene** ★ | Parent picks 3, 5 or 10 minutes (default 5). Two scenes before the end, the lights dim, a lullaby-tone narrator says "Two more, then the ducks go to sleep"; last scene is a sleeping animal and "All done. Bye-bye, ducks!" App then locks to a calm "Goodnight" screen until the parent unlocks. | Takeaway meltdowns [V]; Lumen P9; vision principle "It stops" | Differentiate | MVP | Must |
| TW-04 | **Co-play whisper line** ★ | A small, adult-only caption at the top of each scene (hidden with a tap): "Ask: where's the duck's beak? Wait. Point together." Off-screen follow-up at the end ("At bath time, look for something yellow"). | JME [M]; AAP 2026 [V]; vision principle "adult is part of the product" | Differentiate | MVP | Must |
| TW-05 | **Scene packs (topics)** | 8 free packs at launch (animals, vehicles, food, body, home, garden, bath, bedtime) of ~12 scenes each; parent picks topics. | Parent topic choice (vision); Sam loves trains | Parity | MVP | Must |
| TW-06 | **Sensory Dial with Calm default** | Calm: narration only, 1-s slow motion, muted palette. Balanced: soft effect sounds. Lively: fuller animation, gentle music (opt-in). | Lumen §3.1; Pok Pok benchmark [V] | Lumen | MVP | Must |
| TW-07 | **Sound-free mode with haptic + visual twin** | Every sound has a haptic pulse and a visual ripple; captions of spoken words for Deaf parents. | Lumen P2 | Lumen | MVP | Must |
| TW-08 | **Switch, keyboard and Voice Control start** | Any switch (iOS Switch Control / Android Switch Access / Bluetooth switch) or any key advances the scene; no scanning required because there is only one action. | Ava persona; Cosmo switch patterns [V] | Differentiate | MVP | Must |
| TW-09 | **Parent area behind an adult gate** | Settings, packs, billing behind a non-reading-based gate that doesn't rely on arithmetic only (e.g., "hold two corners for 3 s" + text option) plus the platform's parental controls. | Apple Kids / Play Families requirement [V] | Parity | MVP | Must |
| TW-10 | **Offline & tiny footprint** | All free packs cached; <150 MB install [E]. | Bebi/Sago offline [V]; low-data families | Parity | MVP | Must |
| TW-11 | **Home-language narration** | English and Spanish narration at MVP; parent can switch per session or play both ("duck… pato"). | Two Words synergy; bilingual persona | Parity | MVP | Should |
| TW-12 | **Grandparent / parent voice recording** | Adult records their own voice for each word in a pack ("That's Grandma's duck!"). Stored in the family account; never used for training. | Rosa persona; Two Words synergy | Differentiate | V1 | Should |
| TW-13 | **"Same again" predictable mode** | Replays the same pack in the same order; no novelty shuffle. | Sam persona; Lumen P3 | Lumen | MVP | Should |
| TW-14 | **Photo-your-world packs** | Parent photographs the child's own cup, cat, shoes; app plays them as scenes with parent-recorded names. Photos stay on device by default. | Real-world transfer [M]; personalisation | Differentiate | V1 | Could |
| TW-15 | **Paid packs & more languages** | Seasonal, farm, city, music-instrument packs; 5 more narration languages. | Family plan value | Parity | V1 | Should |
| TW-16 | **Printable co-play cards** | Printable picture cards matching each pack for screen-free play. | Vision "real-world first" | Differentiate | V2 | Could |

★ **Signature features:** Wonder Scenes (TW-01), Sleepy Scene ending (TW-03), Co-play whisper line (TW-04). **MVP = TW-01 to TW-11 and TW-13 (12 features)**, covering the loop: parent chooses topic + length → child taps through scenes with adult → sleepy scene → off-screen follow-up.

## 5. Core experience & key user flows

**Core loop.** Parent opens → picks length (remembered) → child taps scenes → adult reads the whisper line and talks → transition warning → sleepy scene → "Goodnight" lock screen → real-world follow-up.

**Flow 1: Onboarding (≤3 min).**
1. Store listing and first screen show the price: "Free: 8 packs forever. Family plan $69/yr for everything across Lanternling."
2. Adult sets child age (months), home language, favourite topics (tap icons).
3. Sensory check: "Start calm?" (Calm is pre-selected; OS Reduce Motion respected).
4. Session length: 3 / 5 / 10 minutes (5 pre-selected).
5. "Sit with your child for the first go. Here's what to say." First scene opens.

**Flow 2: Core session.**
1. Scene: real photo of a cat on a rug. Whisper line: "Say: cat! Soft cat. Point to her ears."
2. Child taps anywhere → cat blinks slowly, a soft meow, "cat" is spoken.
3. Tap → "soft cat" (attribute). Tap → next scene after a 1-s cross-fade.
4. At T-60 s: dimming, "Two more, then the animals go to sleep" (visual countdown of two moons).
5. Sleepy scene, then the lock screen with a slow-breathing moon. A tap on the lock screen does nothing (a tiny haptic only), so there's nothing to "win" by tapping.
6. Adult card: "Today: cat, dog, duck. Try: find a cat picture in a book at bedtime."

**Flow 3: Caregiver view.** Parent area → "This week": sessions, words met, whisper lines used (tapped "we did it"). One screen. Shared to Family Hub.

**Flow 4: My Needs.** Sensory Dial, sound channels, haptics, switch input, narration languages, predictable mode, session length, parent recordings.

**Flow 5: Billing.** Same Family Hub flow as all Lanternling apps: price before trial, 3-day reminder, one-tap cancel, pause.

**Information architecture.** Child side: *one screen* (the scene), no menus, no buttons. Parent side (gated): Start · Packs · This week · Settings. Navigation never appears on the child side (avoids accidental exits and "menu surfing").

**Session design.** Default 5 min (vision: "5-minute designed ending"); range 3–10; transition warning at T-60 s; sleepy ending; lock screen until the adult unlocks. No "play again?" button on the child side.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial defaults.** **Calm** for all ages 1–3 (Lumen §3.1).

| Level | Motion | Sound | Colour | Feedback |
|---|---|---|---|---|
| Calm (default) | One slow movement ≤1 s per tap; cross-fades only | Spoken word only, soft attack, capped at 65 dB(A) at 30 cm [E target] | Photo saturation reduced ~15%; muted frames | Ripple + light haptic |
| Balanced | Two-step animation | Word + soft natural sound | Natural photo colour | Ripple + haptic |
| Lively (opt-in) | Up to 3 s animation, no flashing (WCAG 2.3.1) | Adds gentle music in transitions only | Vivid | Longer, still skippable |

**Input modes.** Tap anywhere (default) · external switch · any keyboard key · Voice Control ("Next") · eye-gaze dwell on iPadOS (V1, same single action) [I]. No drag, pinch, long-press, double-tap or multi-finger gestures on the child side.

**Targets and gestures.** The entire screen is the target (far above the ≥2.5 cm floor for 1–3). Debounce 500 ms; ignore touches >3 simultaneous points (palm); ignore edge swipes (with Guided Access / screen pinning recommended in onboarding).

**Reading and typography.** Child side is text-free. Captions (for adults and Deaf parents) in 24 pt+ sans-serif, off by default, on when OS captions are on. Parent area follows BDA defaults and Dynamic Type.

**Audio.** Channels: narration, nature sounds, music (off by default). Every audio cue has a visual ripple and haptic twin. Narration recorded by humans, not TTS, at MVP (warmth; consistent prosody for toddlers) [I].

**Age-respectful themes.** Two visual frames: "Photo" (plain real photographs) and "Picture book" (illustrated frames around the same photos). Content is independent of theme (P13).

**Lumen principles.**

| P# | Acceptance criterion |
|---|---|
| P1 | Calm default; Reduce Motion → cross-fades only; Dial reachable in 1 tap from the parent area and from a 3-s two-corner hold on the child side |
| P2 | 100% of sounds have haptic + visual twins; captions for 100% of words |
| P3 | Scenes always in the same layout; transition warning before every ending |
| P4 | Entire screen is the target; zero drag/pinch/double-tap; palm rejection verified with 12 toddlers |
| P5 | Child side has no text; parent copy ≤ grade 5 [E] |
| P6 | Parent area meets BDA defaults |
| P7 | Tap, switch, key and voice all advance scenes |
| P8 | No wrong answers exist; no fail states |
| P9 | Every session ends at the sleepy scene; no autoplay-next; lock screen |
| P10 | Parent gate doesn't need memorised codes |
| P11 | No timing requirement to respond; scene waits indefinitely (optional gentle "tap!" hint after 20 s in Balanced only) |
| P12 | Settings sync via My Needs profile |
| P13 | Two visual frames |
| P14 | First session ≤3 min from install |
| P15 | No stickers, stars, streaks |
| P16 | Diverse families and children in photos (including children with glasses, hearing aids, wheelchairs) |
| P17 | Claims: "designed for co-play, based on research on toddler learning and touch" only |
| P18 | No accounts for children; no analytics beyond first-party aggregates; no third-party SDKs |

**Target Lumen audit score:** 23/24 (item 8, dyslexia typography, is mostly N/A on the child side; scored on the parent area).

## 7. AI specification & guardrails

**What AI does (minimal by design).** A simple, rules-based **variety scheduler** picks the next scene from the parent's topics, balancing new and familiar items (roughly 1 new per 3 familiar [E]) and never repeating within a session unless predictable mode is on. That's it for MVP.

**What AI does not do.** No engagement optimisation (we never optimise for session length or return frequency; the objective function is "variety within parent-chosen topics"). No generated images (all photos are licensed or commissioned real photographs, reviewed for safety and diversity). No voice interaction with the child. No camera use of the child.

**V1 considerations.** On-device image labelling to suggest names for parent-taken photos (TW-14); the parent always confirms the label. Photos never leave the device unless the parent syncs them to the family account.

**Safety.** Human review of every scene (content, cultural appropriateness, no frightening animals shown aggressively). No companion character. Disclosure in the parent area: "Tap & Wonder does not use AI to talk to your child."

**Evaluation plan.** Scheduler evaluated in dyad tests on (a) child engagement (taps per minute stay stable, not rising), (b) meltdown rate at the ending, (c) parent-rated variety. Any algorithm change that raises average session length beyond the parent's setting is a bug, not a win.

**Cost and latency [E].** No cloud AI; content delivery only. Scene response ≤100 ms from tap (toddlers need tight contingency).

## 8. Data, privacy & compliance

**Data inventory.** Parent account (Family Hub); child age in months, topics, language (on device + synced settings); session counts and scenes seen (aggregate, first-party); parent voice recordings and photos (on device by default; optional encrypted family sync). No child accounts, no child identifiers, no child audio, no camera on the child.

**Regimes.** COPPA 2025 (directed to children: verifiable parental consent before any personal information; minimal collection; written retention schedule; no third-party sharing). Apple Kids category (Guideline 1.3: no third-party ads/analytics; parental gate for links and purchases) [V via raw 02]. Google Play Families policy (Teacher Approved submission; certified SDKs only). UK AADC (high-privacy defaults, no nudges). EU AI Act: no AI features requiring disclosure at MVP.

**Consent flows.** Parent consent at account creation; separate consent if parent recordings/photos are synced; none of this data is used for training.

## 9. Monetization & go-to-market

**Pricing.**

| Tier | Price | Includes |
|---|---|---|
| Free forever | $0 | 8 scene packs (~100 scenes), EN/ES narration, all accessibility features |
| Lanternling Family | ≈$9.99/mo or $69/yr (all 7 apps, 3 children) | 30+ packs, parent voice recording, photo-your-world, more languages |
| B2B2C | $3–6 per child/year [E] for childminders, EHS classrooms, libraries' iPads | Kiosk mode, no accounts |

Benchmarks: Pok Pok $45.99/yr; Sago Mini World $7.99/mo; Piknik $11.99–14.99/mo; Bebi/Bimi Boo subscriptions; Khan Kids free [V]. A standalone Tap & Wonder would need to be ≤$40/yr to compete [I]; its job in the bundle is **acquisition and trust**, not revenue.

**Channels.** App Store/Play featuring (calm-tech and inclusivity stories; Apple rewards this [V]); pediatric waiting rooms and libraries; grandparent gifting; SLP/OT recommendations for switch users (Cosmo-style cause-and-effect gap) [I].

**ASO.** "baby games 1 year old", "toddler first words", "calm app for toddlers", "switch accessible toddler app". Accessibility Nutrition Label: VoiceOver (parent area), Voice Control, Larger Text (parent area), Reduced Motion, Captions, Sufficient Contrast.

**Launch markets.** US and UK (EN), US Hispanic and Mexico (ES) [I]; photo sets reviewed for regional relevance.

## 10. Success metrics
- **North-star:** weekly co-play sessions ending by design (target: ≥3 per active family per week [E]).
- **Inputs:** % sessions reaching the sleepy scene (≥90%); % sessions where the adult marks a whisper line "done" (≥40% [E]); packs chosen per family; % sessions with sound-free or switch mode (tracked for inclusion, not optimised).
- **Guardrails:** meltdown-at-ending rate (parent-reported, pictorial) ≤15% of sessions [E], vs. baseline measured with the family's current app; average session length ≤ parent setting +10%; Sensory Comfort ≥4/5; zero billing complaints; zero accidental purchases.
- **Learning measures:** receptive word recognition of pack words (picture-pointing probe) pre/post in a 4-week pilot; parent-reported naming at home. Evidence plan: E4 → E3 (pilot) → possible academic partnership for a contingency study.
- **Retention:** D7 40%, D30 25% [E]. DAU is *not* a goal; 3–4 sessions/week is ideal.

## 11. Validation plan

**Riskiest assumptions.**
1. Calm, finite play holds a toddler's attention long enough to have value (the vision's riskiest).
2. Parents perceive a free-core, calm app as worth paying for inside the bundle.
3. A designed ending actually reduces takeaway meltdowns.
4. Adults will read and use the whisper line.
5. Real photos are as engaging as cartoons for 12–36-month-olds.

**Experiments.**

| # | Method | Sample | Success | Kill / rethink |
|---|---|---|---|---|
| E1 | **In-home dyad sessions** with a Figma/Keynote tap-through prototype on a tablet (Calm vs. Lively counterbalanced) | 12 dyads (4 aged 12–18 mo, 4 aged 19–27 mo, 4 aged 28–36 mo; ≥3 ND or disabled children incl. 1 switch user) | Child engages ≥3 min in ≥75% of sessions; parent value ≥4/5; Calm comfort ≥ Lively | <50% engage 3 min → add gentle animation to Calm or reconsider age |
| E2 | **Ending A/B**: sleepy scene + lock vs. abrupt stop (prototype) | Same dyads, 2 sessions each | Parent-rated distress at end lower with sleepy scene in ≥8/12 dyads | No difference → simplify |
| E3 | **Whisper line use**: facilitators code adult talk during sessions | Same | Adult uses the line or a variation in ≥60% of scenes | <30% → move line to audio "adult earpiece" or card |
| E4 | **Photo vs. illustration** preference | 12 dyads | Photos ≥ illustrations on engagement | Photos lower → hybrid "picture book" frame default |
| E5 | **Pricing/value**: Van Westendorp in survey + fake-door "Family plan" click | n≈600 survey; landing page | Planned bundle price within acceptable range | Outside range → keep Tap & Wonder fully free as acquisition |

**Mapping.** E1–E4 → WP4 paper/Figma prototypes and sensory A/B; E5 → WP5 (L1); accessibility round with switch user → WP4.

## 12. Build handoff

**Epic TW-E1: Scene engine.**
- **Given** a scene is showing, **when** the child touches anywhere with one finger or a palm, **then** exactly one response plays within 100 ms, and further touches in the next 500 ms are ignored.
- **Given** five simultaneous touches, **then** no action occurs.
- **Given** a Bluetooth switch is connected, **when** it is pressed, **then** the scene advances exactly as a tap would.

**Epic TW-E2: Session length & ending.**
- **Given** session length is 5 min, **when** 4 min have passed, **then** the transition warning appears (visual moons + spoken warning, captioned) and exactly two scenes remain.
- **Given** the sleepy scene has ended, **when** the child taps, **then** only a light haptic fires, and the lock screen persists until the parent-gate gesture.
- **Given** the app is closed mid-session and reopened within 10 min, **then** it resumes the countdown rather than starting a new session.

**Epic TW-E3: Co-play layer.**
- **Given** whisper lines are on, **when** a scene shows, **then** the adult caption appears in the top 15% of the screen and never covers the photo's subject.
- **Given** a session ends, **then** a one-line off-screen follow-up is shown in the parent view.

**Epic TW-E4: Sensory & accessibility.**
- **Given** OS Reduce Motion is on, **when** any scene animates, **then** only cross-fades are used.
- **Given** sound-free mode, **then** every response includes a visual ripple and haptic.
- **Given** captions are on, **then** each spoken word appears as a caption for ≥2 s.

**Epic TW-E5: Parent gate & billing.** Standard Family Hub flows; **Given** a child performs random taps for 5 minutes on the child side, **then** no purchase, link or settings screen is ever reached (fuzz-tested).

**Non-functional.** 60 fps on 2018 iPad and 2019 mid-range Android tablet; tap-to-response ≤100 ms; full offline; iOS/iPadOS 16+, Android 10+ (phones and tablets); no web child experience at MVP; WCAG 2.2 AA for the parent area; EN/ES; zero third-party SDKs.

**QA focus.** AT matrix: Switch Control, Switch Access, Voice Control, external keyboard, Guided Access / screen pinning, VoiceOver/TalkBack for the parent area. Sensory A/B with dyads. Toddler fuzz testing (automated random touch, palm, face contact, drops). COPPA: no identifiers or analytics leaving device beyond approved aggregate events. Billing: gate robustness, no child-side purchase paths.

**Platform dependencies.** Lumen tokens and Sensory Dial; My Needs profile (switch, sound, predictable mode); Family Hub (packs, billing, recordings); privacy stack (on-device media store); content pipeline (licensed photography + human narration).

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Calm scenes too dull for 2.5–3-year-olds | M | M | Balanced default from 30 months (parent-changeable); topic depth; hand off to Pok Pok-style open play in V2 |
| Parents use it as a pacifier without co-play | H | M | Whisper line, session caps, ending lock; co-play moments measured, not minutes |
| "Screen time for under-2s" criticism | M | H | Honest framing: designed for co-play; AAP 2026 language; Babble Buddy as the screen-free partner |
| Photo licensing cost and diversity | M | M | Commission a photo library once; reuse across Two Words and Story Lantern |
| Low willingness to pay | H | L | Positioned as free acquisition for the bundle |
| Lock screen frustrates children | M | M | Test in E2; calm animation; adult can extend session by 1 min once |

**Open questions.** Is 12–18 months a viable screen age at all, or should the minimum be 18 months with Babble Buddy covering younger? Should the lock screen be a short audio lullaby instead? How much does real-photo vs. illustration matter across cultures?

## 14. Sources
- [V] Vatavu et al. 2015 (via raw 04): https://www.sciencedirect.com/science/article/abs/pii/S1071581914001426
- [V] Contingent touchscreen word learning: https://academic.oup.com/chidev/article/87/2/405/8258405 · https://pubmed.ncbi.nlm.nih.gov/33716887/ · https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0240519
- [V] Bebi Play listing: https://play.google.com/store/apps/details?id=com.happytools.learning.kids.games&hl=en_US · https://bebi.family/en/game/baby-games-1
- [V] Sago Mini World Play: https://play.google.com/store/apps/details?id=com.sagosago.World.googleplay&hl=en_US · offer page: https://store.sagomini.com/world-exclusive-offer · help: https://help.sagomini.com/article/418-sago-mini-standalone-apps-removed-from-sale
- [V] Apple Design Awards 2026 (Jinja's Garden): https://developer.apple.com/design/awards/ · https://www.macstories.net/news/2026-apple-design-awards-winners-announced/
- [V] Bimi Boo Play: https://play.google.com/store/apps/details?id=com.bimiboo.birthday&hl=en_US
- [V] Pok Pok: https://techcrunch.com/2024/06/18/now-a-series-a-startup-kids-app-and-digital-toy-pok-pok-is-coming-to-android/ · https://9to5toys.com/2026/08/27/pok-pok-lifetime-subscription-drops-to-60-reg-250/ · https://www.commonsensemedia.org/app-reviews/pok-pok-playroom/user-reviews/adult
- [V] Piknik / Toca Boca Jr: https://playpiknik.com/ · https://help.sagomini.com/article/328-why-does-it-say-that-toca-boca-jr-has-in-app-purchases
- [V] Fisher-Price Play & Learn: https://apps.apple.com/us/app/fisher-price-play-learn/id6670388470
- [V] Hey Duggee Big Badge App: https://apps.apple.com/us/app/hey-duggee-the-big-badge-app/id1019167420
- [V] Khan Academy Kids, Sago iOS volume and ratings: [raw 01](../../../research/raw/01-google-play-top30.md), [raw 02](../../../research/raw/02-apple-app-store-top30.md)
- [M] Bluey licensed apps; eye-gaze dwell on iPadOS; video deficit (via raw 04)

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Merge → 'Wonder' toddler mode inside the Lanternling app |
| **Ships in** | Lanternling app (S1) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 65/100 [I] |
| **Consumes engines** | EN-02, EN-07 |
| **Studio features used** | SX-06, SX-07, SX-12 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = TW-01, TW-02, TW-03, TW-04, TW-13.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| TW-E1 | **Two-touch co-play** | A scene reveals its surprise only when adult and child tap together, making joint media engagement structural. |
| TW-E2 | **Bedtime handoff** | Sleepy Scene can hand over to Story Lantern Lantern Mode, so the day ends screen-off. |

### 15.3 New validation question
Do parents value toddler play more as a mode of Lanternling than as a separate app? Preference test in WP3.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 3 | 3 | 5 | 2 | 2 | 5 | 3 | 3 |

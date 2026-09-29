# Lanternling: App Strategy Index (7 apps)

> **Venture:** Lanternling · calm, voice-first, co-play-first early learning for ages 1–7 · **Status:** Discovery & Validation (specs only, no code) · **Date:** 29 September 2026
> **Parent docs:** [Venture vision](../../vision/01-lanternling-early-years.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Template](../_TEMPLATE.md)
> **Confidence tags:** [V] verified this session · [V2] secondary/vendor · [M] memory · [E] estimate · [I] inference

---

## 1. The seven apps

| # | App | Ages | Signature feature(s) | Top competitors benchmarked | MVP tier |
|---|---|---|---|---|---|
| 1 | [Babble Buddy](01-babble-buddy.md) | 1–3 (parent-held) | **Moment Cards** (one routine-anchored sentence + "wait" cue) · **Word Garden** (any language, signs count) · **Talk Tally** (opt-in, on-device turn estimate, with tap tally alternative) | Kinedu, Speech Blubs, Huckleberry, The Wonder Weeks, BabySparks, Vroom, Lovevery, LENA Start/Grow | **Year-1 MVP** |
| 2 | [Tap & Wonder](02-tap-and-wonder.md) | 1–3 (co-play) | **Wonder Scenes** (whole-screen single tap, real photos, spoken word) · **Sleepy Scene** designed ending with parent-set length · **Co-play whisper line** | Bebi, Sago Mini World, Bimi Boo, Khan Academy Kids, Pok Pok, Toca Boca Jr/Piknik, Fisher-Price, Hey Duggee | Year 1 add-on (free-tier "front door"), conditional on dyad test |
| 3 | [Story Lantern](03-story-lantern.md) | 2–7 | **Pause & Ask** dialogic prompts for the adult · **Lantern Mode** (screen-off, self-ending audio) · **My Story** (human-template, human-reviewed personalised stories) | Epic, Tonies, Yoto, Moshi, Readmio, Vooks, Oscar, Amazon Kids+ | **Year-1 MVP** |
| 4 | [Sound Garden](04-sound-garden.md) | 4–7 | **Read-Along Listener** (on-device, expected-word checking) with **tap parity** on every item · **Garden Path** published scope & sequence · careful **Early Signals** | Duolingo ABC, Reading Eggs, Teach Your Monster to Read, Hooked on Phonics, HOMER, Read Along, Ello, Starfall (+ Amira) | **Year-1 MVP** |
| 5 | [Number Nest](05-number-nest.md) | 3–7 | **The Shelf** (child choice) · **Self-correcting materials** (balance scale, ten-frames, rods) · **Tap-to-place** for every manipulative | Khan Academy Kids, SplashLearn, DragonBox Numbers, Todo Math, Moose Math, Montessori Numbers, Osmo | Year 2 (fast follower) |
| 6 | [Calm Cubs](06-calm-cubs.md) | 3–7 | **Picture Routines + transition warnings** · **Breathing Buddies** (haptic, silent mode) · **Help Now** (≤2 taps, parent-held) | Moshi, Daniel Tiger's Grr-ific Feelings, Breathe Think Do with Sesame, GoNoodle, Headspace/Calm kids, Choiceworks, Brili, Mightier | Year 2 (pull forward if diary study shows in-the-moment use) |
| 7 | [Two Words](07-two-words.md) | 3–7 | **Word Pairs** with the home language as an equal · **Family Voice** (grandparent recordings) · **Two-generation games** | Lingokids, Duolingo, PBS KIDS Games, Gus on the Go, Studycat, Rosetta Stone Kids, Dinolingo, Mondly Kids | Later (after heritage vs. EFL WTP test) |

**Recommended sequence [I].** Year 1: Babble Buddy + Story Lantern + Sound Garden (the vision's trio), with Tap & Wonder as a low-cost free acquisition app if its dyad test passes. Year 2: Number Nest, Calm Cubs, Two Words (market chosen by smoke test). This matches the vision's three-year ambition.

**How the apps cover a child's day and ages [I].**

| Moment | 1–3 | 4–7 |
|---|---|---|
| Routines (meals, bath, car) | Babble Buddy (parent-held) | Calm Cubs (routines) |
| Short play | Tap & Wonder | Number Nest, Sound Garden |
| Bedtime | Story Lantern (Lantern Mode) | Story Lantern |
| Hard moments / transitions | Calm Cubs (Help Now, parent-held) | Calm Cubs |
| Family language | Babble Buddy home-language mode | Two Words |

## 2. Shared features across all apps (the Lanternling Family Hub)

Every app spec depends on these shared platform features. They are designed once and reused.

| Shared feature | What it is | Why (evidence) | Where specced |
|---|---|---|---|
| **Family Hub** | One account, up to 3 children, unlimited caregivers (parents, grandparents, childminders, teachers, SLPs) with role-based, consented views; one weekly one-screen summary across apps. | Research paper need #7 (proof parents can see); multi-caregiver reality (Rosa persona); Kinedu/Huckleberry sharing [V] | Vision §4; each app §5 and §12 |
| **My Needs profile** | Set-once, portable profile: sensory level, sound channels, haptics, motion, reading level/typography, input modes (tap, switch, AAC, voice, sign-aware), pace and wait time, languages, themes, who can view progress. Free, and portable to Questwise and Wavelength. | Lumen P12; §3.2 | [Lumen §3.2](../../02-inclusive-sensory-ux-framework.md) |
| **Sensory Dial** | Calm / Balanced / Lively in one control, 1 tap from every screen. **Calm is the default for ages 1–3**, and for bedtime, regulation and Calm Cubs at all ages; Balanced default for 4–7 learning apps where tested. | Lumen P1; parent demand for calm tech (Pok Pok, Sago) [V] | [Lumen §3.1](../../02-inclusive-sensory-ux-framework.md) |
| **Now / Next / Done strip + designed endings** | Pictorial session plan, transition warnings, and a designed "all done / goodnight" ending with a real-world follow-up in every app. No autoplay-next. | AAP 2026 co-engagement and design responsibility [V]; takeaway meltdowns [V] | Lumen §3.3 |
| **Co-play cards** | One-line adult prompts tied to what the child just did, plus screen-free follow-ups; printable versions. | Joint media engagement [M]; vision principle 1 and 3 | Lumen §3.6 |
| **Multimodal answer tray / tap parity** | Every task works by tap; voice is optional and never the only path; no drag-only actions (tap-then-tap); targets ≥2.5 cm (1–3) and ≥2 cm (4–7). | Vatavu 2015 (3-year-olds 73% touch success) [V]; WCAG 2.5.7; child ASR gap [V] | Lumen §3.5, P4, P7 |
| **Fair-billing charter** | Price shown before any trial; reminder 3 days before charge; one-tap in-app cancel; pause (summer, parental leave); family plan ≈$9.99/mo or $69/yr for all 7 apps and 3 children; accommodations never paywalled; generous free tier in every app; data export. | Billing anger is the #1 unmet need; ABCmouse FTC $10M; Speech Blubs, Moshi, Epic, Lingokids complaints [V] | Lumen §3.7; each app §9 |
| **Privacy & child-safe AI stack** | COPPA 2025 consent ledger (separate consents for mic, photos, recordings, research); on-device child speech; no third-party SDKs; written retention schedule; no training on children's data without separate consent; no companion persona; no emotion recognition; human review of generated content. | COPPA 2025, EU AI Act Art. 5/50, UK AADC [V] | Lumen §5; each app §7–§8 |
| **Evidence engine** | Claims register, pre-registered pilots, shared probes (vocabulary, phonics, number sense, transitions). | Lumen P17; FTC §5 | Discovery plan WP6 |

## 3. Features we reject, and why (combined list)

| Rejected feature | Seen in (examples) | Why we reject it | Apps affected |
|---|---|---|---|
| **Hidden prices, silent trial conversions, hard cancellation** | ABCmouse (FTC $10M), Speech Blubs, Epic, Moshi, Lingokids, Pok Pok (no price before download) [V] | #1 unmet need; trust is the brand; FTC negative-option risk | All |
| **Reward currencies, tokens, stickers and gems** | Reading Eggs "eggs", Oscar coins, SplashLearn, Brili/Mightier rewards [V/M] | Kids game rewards instead of learning; compliance economies conflict with ND-affirming design; Lumen P15 | All, esp. Sound Garden, Number Nest, Calm Cubs |
| **Streaks with loss framing, hearts/energy, lives** | Duolingo Energy backlash [V] | Punishes learning; anxiety; Lumen P8/P15 | All |
| **Timers and speed scoring in learning** | Many math/phonics games [V/M] | Excludes slower processors, dyslexic and motor-impaired children; Lumen P11 | Sound Garden, Number Nest |
| **Drag-only interactions and precision gestures** | Duolingo ABC, Bimi Boo, DragonBox, most toddler apps [V/M] | 3-year-olds ~73% touch success; WCAG 2.5.7 | All child-facing apps |
| **Autoplay-next, infinite feeds, all-night loops** | Video platforms; sleep-sound loops (Moshi) [V/M] | Displaces sleep and talk; Lumen P9; AAP 2026 | Tap & Wonder, Story Lantern, Calm Cubs |
| **Voice-only input and accent/pronunciation scoring** | Read Along, ELSA, Mondly-style scoring [V/M] | Child ASR error gap (~25% vs 3% WER) [V]; excludes speech differences and AAC users | Sound Garden, Two Words, Babble Buddy |
| **Companion personas / AI "friends" for children** | AI companion apps (FTC 6(b) inquiry) [V] | Tutor, not friend; dependency risk; Lumen P18 | All |
| **Emotion recognition from face, voice or biometrics** | Emotion-sensing toys/apps; biometric regulation tools [V] | EU AI Act ban in education; COPPA biometrics; unreliable for ND children | Calm Cubs, Babble Buddy, all |
| **Unreviewed AI-generated story text; AI images of a child's likeness; voice cloning of relatives** | Oscar-style AI stories [V]; AI slop [V] | Parents distrust AI-authored text [V]; deepfake and consent risks | Story Lantern, Two Words |
| **Child-facing face filters and camera-only input** | Speech Blubs filters, Osmo camera tiles [V/M] | Biometric-adjacent data; excludes blind users; camera-only barriers | Babble Buddy, Number Nest |
| **Ads, third-party trackers, in-play upsells to children** | Many free kids apps; Lingokids in-app upgrade prompts [V] | Apple Kids / Google Families rules; COPPA; trust | All |
| **Engagement optimisation (optimising minutes or return rate)** | Industry standard | AAP 2026 design responsibility; we measure good sessions, not minutes | All (Tap & Wonder explicitly) |
| **Diagnostic or screening claims** | Screening products in clinical channels | FDA device boundary; FTC §5; parent anxiety | Babble Buddy, Sound Garden, Calm Cubs |
| **Licensed high-stimulation characters and animated video books as core** | Hey Duggee/Bluey apps, Vooks [V/M] | Stimulation and cost; passive viewing; revisit only if calm and co-play-compatible | Tap & Wonder, Story Lantern |
| **Dedicated hardware (for now)** | Tonies, Yoto, Osmo [V/M] | Retention not yet proven; Osmo cautionary tale; audio mode first | Story Lantern, Number Nest |

## 4. Cross-app validation summary (Discovery WP2–WP5)

| Venture assumption ([Discovery §8.1](../../discovery/discovery-validation-plan.md)) | Apps and experiments |
|---|---|
| L1: Parents pay for calm, co-play-first learning | Smoke tests + Van Westendorp in every app §11; bundle vs. standalone price (Babble Buddy E5, Sound Garden E5, Two Words E1/E4) |
| L2: Toddler-parent pairs co-play when prompted | Babble Buddy SMS concierge (E1); Tap & Wonder dyad whisper-line coding (E3); Story Lantern Pause & Ask diary (E2) |
| L3: Child-speech read-along is accurate enough | Sound Garden ASR spike by speaker group (E1) + Wizard-of-Oz read-along (E2); Babble Buddy Talk Tally spike (E3) |
| L4: Pre-K and libraries will distribute | Babble Buddy E6 (EHS/SLP), Story Lantern library card channel, Number Nest E5 teachers |

**Hard gates for every app (from the Discovery scorecard):** prototype scores ≥22/24 on the Lumen audit; no dependence on emotion recognition, companion personas, training on children's data without consent, or dark-pattern monetisation; ND advisory sign-off.

## 5. Research caveats (read before citing)
- **Search budget and proxy limits.** Web searches for this set were exhausted during App 5 research, and App Store, Google Play, Sensor Tower, Common Sense and most vendor pages were blocked by the network proxy. Figures for Apps 1–4 are mostly **[V] from search-result snippets** (store listings, vendor pages, trackers such as AppBrain and Sensor Tower). Several competitors for Apps 5–7 (Moose Math, Montessori Numbers, Osmo, Daniel Tiger, Breathe Think Do, GoNoodle, Headspace/Calm kids, Gus on the Go, Studycat, Rosetta Stone Kids, Dinolingo, Mondly Kids) are **[M]** and must be verified in Discovery WP1 with a Sensor Tower/Appfigures export.
- **Download figures are mixed**: Play install bands, vendor "families/children reached" claims and tracker estimates are not comparable. Treat them as signals, not rankings.
- **Vendor outcome claims** (e.g., HOMER "74%", Reading Eggs "91% of parents", Pok Pok "90% calmer", Amira ES +0.64) are [V2] and are not endorsements.
- **All prices, retention and cost targets marked [E] are planning assumptions** to validate.

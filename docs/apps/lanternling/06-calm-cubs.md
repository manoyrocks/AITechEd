# Calm Cubs: App Strategy & Product Specification

> **Venture:** Lanternling · **App #:** 6/7 · **Ages:** 3–7 (child + adult; parent-held in hard moments) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/01-lanternling-early-years.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given; mostly search snippets) · [V2] secondary or vendor source · [M] from memory · [E] estimate · [I] inference
> **Research caveat:** the session's web-search budget ran out before this app's research. Store pages were proxy-blocked. Daniel Tiger, Breathe Think Do, Headspace, Calm and GoNoodle figures are [M] and must be verified in Discovery WP1. Moshi, Choiceworks, Brili and Mightier figures come from this session or the repo's verified raw files.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Help for the hardest ten minutes of the day: picture routines with gentle transition warnings, breathing buddies you can feel, feelings words, and calm scripts for the grown-up. No emotion detection, ever. |
| **Primary user / buyer** | Children 3–7 and their adults together; the parent is buyer and often the user in the moment. Secondary: pre-K teachers, childminders, OTs. |
| **Core job-to-be-done** | "When it's time to leave the park, go to bed, or when my child is overwhelmed, I want a predictable routine and a calm thing we can both do, so the transition goes better and my child learns words for feelings." |
| **Category on the stores** | Apple: Kids › Ages 5 & Under / 6–8 (Education or Health & Fitness). Google Play: Families › Educational / Parenting. |
| **Top competitors** | Moshi Kids (4.7★ from ~70K) · Daniel Tiger's Grr-ific Feelings (PBS KIDS) [M] · Breathe, Think, Do with Sesame [M] · GoNoodle [M] · Headspace / Calm kids content [M] · Choiceworks ($39.99) · Brili Routines ($49.99/yr) · Mightier (RCT-supported, hardware) |
| **Our wedge** | 1. **Built for the moment of transition, not only calm moments**: parent-first "Help now" flow in ≤2 taps. 2. **Routines + regulation + feelings in one**, where the market splits them into schedule apps (Choiceworks, Brili), SEL character apps (Daniel Tiger, Sesame) and sleep/meditation apps (Moshi, Headspace). 3. **Neurodiversity-affirming, sensory-safe, no emotion recognition**: works screen-free with printable cards; haptic breathing; nothing that judges a child's face or voice. |
| **Business model** | In the Lanternling Family plan (≈$9.99/mo or $69/yr, 7 apps). Free: 3 routines, 2 breathing buddies, feelings basics, printable cards. B2B2C: pre-K, childminders, OT/SLP clinics (with Wavelength pathway). |
| **North-star metric** | **Weekly supported transitions**: routines completed with the Now/Next/Done strip, plus breathing or co-regulation uses. |
| **MVP candidate?** | **Year 2** in the vision's sequence; strong candidate to pull forward if the E1 diary study shows in-the-moment use. |

## 2. Problem & users

**Problem statement.**
- **Transitions and big feelings cause daily family conflict**, and parents want tools that aren't just distraction (vision). Parents report meltdowns when devices are taken away, even with calm apps [V] ([Common Sense Pok Pok reviews](https://www.commonsensemedia.org/app-reviews/pok-pok-playroom/user-reviews/adult)).
- **Visual supports and schedules are an established evidence-based practice for autism** (NCAEP reviews) [M via raw 04], and parents build them by hand with laminated cards or Choiceworks [M] ([raw 03](../../../research/raw/03-forum-voice-of-customer.md)).
- **Existing tools are split and dated.** Choiceworks is $39.99 one-time, iOS-centric and dated [V]; Brili ($49.99/yr) has dynamic routine timers but "less content" [V]; Goally's setup takes hours with sync bugs [V]; Joon's novelty wears off in weeks [V] ([raw 04 §A](../../../research/raw/04-neurodivergent-and-inclusive-ux.md)).
- **Evidence exists for biofeedback** (Mightier's sham-controlled RCTs on anger and oppositional behaviour) [V], but it needs a wearable and processes sensitive heart-rate data [V].
- **Regulation**: the EU AI Act bans emotion recognition in education (since Feb 2025) [V]; COPPA 2025 expands personal information to biometrics [V]. Emotion-sensing features are off the table.

**Personas.**

| Persona | Snapshot | Needs |
|---|---|---|
| **Maya and Leo (3)** | Leaving the park = tears; bedtime stalls. | Warnings Leo can see; a routine he helps build; a script for Maya. |
| **Sam, 4, autistic, sensory-sensitive** (with dad) | Needs predictability; loud sounds trigger shutdowns. | Visual schedule with his photos; "first/then"; silent, haptic breathing; no surprises. |
| **Ruby, 6, ADHD** | Mornings are chaos; loses track of steps. | Visual timer per step; movement breaks; choices; praise that isn't babyish. |
| **Omar, 5, selective mutism** | Doesn't speak at school; communicates by pointing. | Feelings check-in by tapping pictures; nothing requires speech. |
| **Ms. Patel, pre-K teacher** | Group transitions (tidy-up, line-up). | Classroom routine on a big screen; printable cards; calm-corner ideas. |

**Needs & wants.**

| Need | Evidence | Response |
|---|---|---|
| Predictable transitions | Visual schedules EBP [M]; Lumen P3 | Now/Next/Done routines with visual countdown warnings |
| Something to do in the hard moment | Vision riskiest assumption | "Help now": breathing buddy + parent script in ≤2 taps |
| Feelings vocabulary | Daniel Tiger/Sesame popularity [M] | Feelings words with real faces and illustrated cubs, co-play talk |
| Low setup | Goally setup complaints [V] | Templates in ≤5 min; AI-assisted routine builder |
| Screen-free options | Screen guilt [V] | Printable cards; haptic-only breathing; audio mode |
| No surveillance or emotion AI | EU AI Act [V]; COPPA [V] | Child self-report only; no camera/voice affect inference |
| Affordable | Choiceworks/Brili pricing [V] | Free core; bundle |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Moshi Kids** | Mind Candy | ~70K US iOS ratings; "Moshi Family" bundle [V] | $12.99/mo or $79.99/yr; 7-day trial [V] | 4.7 iOS; Trustpilot 2.8 [V] | 400+ sleep stories, meditations, soundscapes [V] | Billing/renewal complaints [V] | Audio-first, calm [V] | [App Store](https://apps.apple.com/us/app/moshi-kids-sleep-relax-play/id1306719339) · [Trustpilot](https://www.trustpilot.com/review/moshikids.com) |
| **Daniel Tiger's Grr-ific Feelings** | PBS KIDS | Not verified; Daniel Tiger is a top PBS franchise [M] | ≈$2.99 paid [M] | ≈4.4 [M] | Feelings songs ("When you feel so mad…"), photo booth, trusted characters [M] | Small, dated [M] | Character-led; moderate sensory [M] | [M] |
| **Breathe, Think, Do with Sesame** | Sesame Workshop | Not verified [M] | Free, EN/ES [M] | high 4s [M] | Monster-led breathing and problem-solving steps; bilingual [M] | Limited content [M] | Simple; tap-to-breathe [M] | [M] |
| **GoNoodle** | GoNoodle | Widely used in US elementary classrooms (vendor claim) [M] | Free; GoNoodle Plus for schools [M] | n/a [M] | Movement and mindfulness videos [M] | Sponsored content; high energy [M] | Very high stimulation in many videos [M/I] | [M] |
| **Headspace (kids content)** / **Calm (kids content)** | Headspace / Calm | Adult apps with kids sections [M] | ≈$69.99/yr each [M] | 4.8 adult apps [M] | Brand trust; guided breathing for kids [M] | Kids content is secondary [I] | Calm audio [M] | [M] |
| **Choiceworks** | Bee Visual | Clinician-trusted [V] | $39.99 one-time [V] | n/a | Schedule, waiting board, feelings board; simple [V] | iOS-centric; dated [V] | Visual supports EBP [M] | [raw 04](../../../research/raw/04-neurodivergent-and-inclusive-ux.md) |
| **Brili Routines** | Brili | Small team [V] | $7.99/mo; $49.99/yr [V] | n/a | Timers adapt to actual time left [V] | Less content [V] | Visual/audio prompts; rewards [V] | [Play](https://play.google.com/store/apps/details?id=co.brili.routines&hl=en_US&gl=US) (via raw 04) |
| **Mightier** | Mightier (Boston Children's spinout) | RCT-supported (E1/E2) [V] | Subscription incl. hardware [V] | n/a | Heart-rate biofeedback games; kids practise calming [V] | Recurring cost; biometric data [V] | Biometric sensitive data [V] | [raw 04](../../../research/raw/04-neurodivergent-and-inclusive-ux.md) |

**Takeaways [I].** The market is split into (a) **SEL character apps** (cheap, loved, thin), (b) **visual schedule tools** (useful, dated, ND-niche), and (c) **sleep/mindfulness subscriptions** (big, billing complaints). The one strongly evidenced product (Mightier) needs hardware and biometrics. **No one joins routine + regulation + feelings, designed for the moment of difficulty, sensory-safe, with a free core.**

**Feature matrix.**

| Feature | Moshi | Daniel Tiger [M] | Sesame BTD [M] | GoNoodle [M] | Choiceworks | Brili | Mightier | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Picture routines / schedules | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | **Parity + improve** (5-min templates, family photos) |
| Transition warnings / visual timers | ✗ | ✗ | ✗ | ✗ | partial | ✓ | ✗ | **Parity** (Brili-style adaptive) |
| Breathing exercises | ✓ | partial | ✓ | ✓ | ✗ | ✗ | partial | **Improve**: haptic breathing buddy, silent mode |
| Feelings vocabulary | partial | ✓ | ✓ | partial | ✓ (board) | ✗ | partial | **Parity + improve** (real faces + cubs) |
| Adult co-regulation scripts | ✗ | partial | ✗ | ✗ | ✗ | ✗ | partial (parent coaching) | **Differentiate** |
| "Help now" fast path | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Printable cards | ✗ | ✗ | ✗ | partial | partial | ✗ | ✗ | **Differentiate** |
| Movement breaks | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | **Parity (calm version)**; low-energy movement only by default |
| Rewards/token economy | ✗ | partial | ✗ | partial | partial | ✓ | ✓ | **Reject** compliance token economies (Lumen P15, ND-affirming) |
| Biometric sensing | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Reject** at MVP (sensitive data; hardware); revisit only with clinical partner |
| Emotion recognition (face/voice) | ✗ | partial (photo booth faces, not inference) [M] | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject** (EU AI Act ban; Lumen P18) |
| All-night sleep sounds | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject default**; 30-min fade only |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| CC-01 | **Picture Routines with Now/Next/Done** ★ | Routines as picture strips (bedtime, morning, leaving the park, bath, screen-off). Each step: picture (template art or family photo), word, audio. The child taps a step done; the strip slides. | Visual schedule EBP [M]; Choiceworks [V]; Lumen §3.3 | Parity + Improve | MVP | Must |
| CC-02 | **Transition warnings** ★ | "5 more minutes of park, then shoes." Visual countdown (shrinking sun, no numbers needed), gentle chime/haptic at 5/2/0 min; adult can "snooze once". | Lumen P3; Brili adaptive timers [V] | Parity + Lumen | MVP | Must |
| CC-03 | **Breathing Buddies** ★ | A cub whose belly rises and falls; phone vibrates in rhythm (inhale ramp, exhale fade); child can hold the phone on their tummy. 3 patterns (bubble, flower-candle, star). Silent haptic-only mode. 1–2 min, then stops. | Moshi/Sesame breathing [V/M]; haptic for Deaf/HoH & sensory | Improve | MVP | Must |
| CC-04 | **Help Now (parent-held)** ★ | From lock-screen widget or app home: two taps to (a) a breathing buddy and (b) a 3-line co-regulation script for the adult ("Get low. Say less. 'You're safe. I'm here.' Breathe with the cub."). No child tasks. | Vision riskiest assumption | Differentiate | MVP | Must |
| CC-05 | **Feelings Words** | 12 feelings at MVP (happy, sad, mad, scared, worried, excited, tired, frustrated, calm, proud, silly, overwhelmed) with diverse real child faces **and** illustrated cubs; "people show feelings in different ways" framing; co-play talk prompts. | Daniel Tiger/Sesame [M]; ND-affirming (P16) | Parity + Lumen | MVP | Must |
| CC-06 | **Feelings Check-in (self-report)** | Child taps a feeling (or several) and a size (small/medium/big); app suggests a calm tool; adult sees it only if the child is with them. Never inferred from face/voice. | Lumen P18; Omar persona | Lumen | MVP | Must |
| CC-07 | **Routine templates + 5-minute setup** | 10 templates; edit steps, reorder by tap-up/down (no drag required), add photos. | Goally setup burden [V]; Lumen P14 | Improve | MVP | Must |
| CC-08 | **Printable cards** | Every routine and feelings set exports as printable cards / fridge strip (PDF). | Screen-free need; laminated-card workaround [M] | Differentiate | MVP | Must |
| CC-09 | **Calm Corner** | A no-flash space: 3 calm tools (breathing, slow shaker animation, a counting-to-five squeeze), child-chosen. Ends after 3 min with a return to the routine. | Lumen §3.1 calm corner | Lumen | MVP | Should |
| CC-10 | **Co-regulation library (adult)** | 20 short scripts for common moments (leaving, sibling fight, bedtime stalling, public meltdown), written by a child psychologist and ND advisory panel; affirming, non-punitive. | Parent need [I]; no competitor offers it | Differentiate | MVP | Must |
| CC-11 | **Weekly one-screen summary** | "Bedtime routine done 5 of 7 nights; breathing used 4 times; feeling words Leo tapped: tired, mad, proud." | Research paper need #7 | Parity | MVP | Should |
| CC-12 | **Routine Builder (AI-assisted)** | Parent types or says: "bedtime at 7:30, bath then 2 books"; builder assembles from human-reviewed step templates; parent confirms each step. | Vision AI role | Differentiate | V1 | Should |
| CC-13 | **Caregiver sharing** | Grandparents/childminders/teachers get the same routines and scripts (consistency across homes). | Family Hub | Parity | V1 | Should |
| CC-14 | **Classroom routines** | Big-screen tidy-up/line-up routines, group breathing, printable classroom strip. | Ms. Patel persona; GoNoodle classroom use [M] | Parity | V1 | Could |
| CC-15 | **Watch / wearable haptic breathing** | Breathing buddy on Apple Watch / Wear OS (parent's watch in co-regulation). | Haptics accessibility | Differentiate | V2 | Could |
| CC-16 | **Wavelength handoff** | My Needs profile + routines move to Wavelength Day for ND children needing deeper support. | Studio platform | Differentiate | V2 | Could |

★ **Signature features:** Picture Routines + transition warnings (CC-01/02), Breathing Buddies with haptics (CC-03), Help Now (CC-04). **MVP = CC-01 to CC-11 (11 features).**

## 5. Core experience & key user flows

**Core loop (routine).** Adult starts a routine (or it starts at its set time on the family tablet) → warning → Now/Next/Done strip → child taps steps done → calm finish ("Bedtime ready. Goodnight!") → optional feelings check-in → end.

**Core loop (hard moment).** Adult opens Help Now → script + breathing buddy → 1–2 min → "How are you both now?" (adult tap) → optional: log what helped.

**Flow 1: Onboarding (≤5 min).** Price/privacy → child age, languages, sensory needs (Calm default; sound off option) → choose 2 routines from templates → add one photo (optional) → print or use on screen.

**Flow 2: Leaving the park.** Adult taps "Leaving" 5 min before → the phone shows a shrinking sun and "5 more minutes, then shoes"; at 2 min, soft haptic + "2 more slides" → at 0: "Shoes → Car → Snack" strip → child taps each step.

**Flow 3: Help Now in a meltdown.** Lock-screen widget → "Help now" → script card ("Stay close. Few words. Breathe slowly yourself first.") + big "Breathe with cub" button → cub + haptics → stops after 90 s → adult logs outcome (optional).

**Flow 4: Caregiver view.** Summary; routines; scripts favourites; sharing.

**Flow 5: My Needs.** Sensory Dial, haptics, sound, images (photos vs. illustrations), language, AAC symbols for steps, timers visible/hidden.

**Flow 6: Billing.** Family Hub standard.

**Information architecture.** Child: Today's routine strip · Calm Corner · Feelings. Parent (gated): Help Now (also a widget) · Routines · Scripts · Week · Settings.

**Session design.** Routines last as long as real life; the app shows only the strip. Breathing ≤2 min; Calm Corner ≤3 min; each ends with a return to the strip. No free-play content to linger in.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial defaults.** **Calm for all ages** (regulation context).

| Level | Calm Cubs behaviour |
|---|---|
| Calm (default) | Slow cub breathing animation only; haptics on; sound off in Calm Corner; muted palette |
| Balanced | Soft voice guidance; gentle chimes for warnings |
| Lively | Movement-break animations (still slow, no flashing); songs for routines |

**Input modes.** Tap steps; switch (step done = one switch); Voice Control; AAC symbol mode for routine steps and feelings (symbol sets compatible with common AAC vocabularies); parent-held operation throughout. Nothing requires speech.

**Targets.** Steps ≥2.5 cm (3–4), ≥2 cm (5–7); Help Now buttons ≥56 dp in thumb zone; reorder with up/down buttons, drag optional.

**Reading.** Pre-reader: picture + word + audio; captions; parent scripts at ≤ grade 5 [E] with read-aloud.

**Audio.** Warnings have visual + haptic twins; voice, chimes, music separate; peak loudness capped; silent operation fully supported.

**Neurodiversity-affirming content.** Feelings shown with varied expressions (including flat affect, stimming as self-regulation, covering ears); no "calm down" as a demand; scripts avoid compliance/reward framing; no targeting of stimming or eye contact.

**Age-respectful themes.** "Cubs" (illustrated) and "Photo" (real photos; suits older children and ND kids who prefer realism).

**Lumen principles.**

| P# | Acceptance criterion |
|---|---|
| P1 | Calm default; Reduce Motion → breathing shown as a slowly filling bar, no motion |
| P2 | Every warning has chime + haptic + visual |
| P3 | Now/Next/Done in every routine; warnings before every transition |
| P4 | All actions single tap; no drag needed |
| P5 | Pictures + audio for every step |
| P6 | Parent text meets BDA defaults |
| P7 | Tap, switch, AAC symbols, voice control |
| P8 | Unfinished steps simply remain; no "failed" routine |
| P9 | Breathing and Calm Corner self-end |
| P10 | Help Now via widget, no login |
| P11 | Warnings configurable; "snooze once" |
| P12 | Sensory and AAC settings shared with Wavelength |
| P13 | Two themes |
| P14 | First routine ready ≤5 min |
| P15 | No stickers/tokens for compliance; optional child-chosen "cub collection" for routines they *want* to celebrate |
| P16 | ND advisory review of all feelings content and scripts |
| P17 | No claims to reduce tantrums/treat anxiety until measured; "based on visual-support practices" |
| P18 | Zero emotion inference; self-report only |

**Target Lumen audit score:** 23/24.

## 7. AI specification & guardrails

**What AI does.** V1 **Routine Builder**: an LLM parses an adult's description into a routine using only **human-reviewed step templates** (e.g., "bath", "teeth", "2 books"), times and order; the adult confirms every step. Optional V1 ranking of which script to show first based on the adult's past "this helped" taps (on-device).

**What AI does not do.** No chat with the child; no cub that "talks back" as a friend; no emotion recognition from camera, voice or typing; no mental-health advice generation; no diagnosis of anxiety/ADHD/autism.

**Pedagogical/clinical policy.** Scripts and feelings content authored by a licensed child psychologist and reviewed by the ND advisory panel; grounded in co-regulation and visual-support practice [M]; no ABA-style compliance economies.

**Safety.** Adult-side safety: if an adult's free text (Routine Builder) contains crisis indicators (e.g., mentions of harm), the builder stops and shows crisis resources (e.g., 988 in the US [M]) and "talk to your pediatrician" guidance; this is keyword/classifier-based on the **adult's** text, not the child. Child-side: feelings check-ins never trigger automated escalation; the design assumes the adult is present. AI disclosure in the builder.

**Evaluation.** Builder: 300 test descriptions (multilingual, messy) → ≥95% correct step extraction, 0 invented non-template steps; crisis-classifier recall ≥98% on a curated set with human review of false negatives; content review 100% human.

**Cost and latency [E].** Builder call <$0.005; ≤2 s. Everything else on-device.

## 8. Data, privacy & compliance
**Data inventory.** Routines (steps, times, optional family photos); feelings check-ins (child self-report: feeling + size, timestamp); breathing/Help Now usage counts; adult notes (optional). Feelings data is **sensitive**: stored encrypted, parent-only, auto-deleted after 90 days by default (adjustable), never used for profiling or training.
**Regimes.** COPPA 2025 (children's feelings data is PI; verifiable parental consent; retention schedule); UK AADC (profiling off; no nudges); state AADCs; EU AI Act Art. 5 (no emotion recognition: we collect self-report only); HIPAA not applicable unless clinics contract (then BAA); FDA: no treatment claims (not a digital therapeutic); FTC §5 claims discipline.
**Consent.** Parent consent; separate toggle for storing feelings history (default on with 90-day deletion, or off = no history).
**Store policy.** Kids category rules (parental gate; no third-party SDKs); widget shows no child data on the lock screen.

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Free | $0 | 3 routines, 2 breathing buddies, 12 feelings, Help Now, printables |
| Family plan | ≈$9.99/mo or $69/yr (7 apps) | Unlimited routines, all scripts, Routine Builder, caregiver sharing, summaries |
| Classroom / clinic | $100–200/yr per room or clinician [E] | Classroom routines, printables, multi-child |

Benchmarks: Choiceworks $39.99 one-time; Brili $49.99/yr; Moshi $79.99/yr; Headspace/Calm ≈$69.99/yr [M]; Sesame/Daniel Tiger free–$2.99 [M]; Mightier higher with hardware [V].

**Channels.** Pediatricians and OTs; pre-K teachers; autism/ADHD parent communities (with Wavelength); parenting creators on transitions/bedtime.

**ASO.** "visual schedule for kids", "toddler bedtime routine app", "breathing exercises for kids", "feelings app preschool", "transition timer kids". Accessibility Nutrition Label: VoiceOver, Voice Control, Larger Text, Reduced Motion, Captions, Sufficient Contrast.

**Launch.** US (EN/ES), UK, Canada, Australia.

## 10. Success metrics
- **North-star:** weekly supported transitions (target ≥5 per active family [E]).
- **Inputs:** routines completed; warnings used; Help Now uses; scripts marked "helped"; printables downloaded.
- **Guardrails:** Sensory Comfort ≥4/5; parent-reported transition difficulty trend (should fall); zero emotion-inference features; zero billing complaints; Help Now reachable in ≤2 taps (measured).
- **Outcomes:** parent-reported transition difficulty and feelings-vocabulary checklists pre/post (6-week pilot); E4 → E3; any stronger claims only with a clinical partner.
- **Retention:** routine apps are daily-use when they work; D30 35% [E].

## 11. Validation plan

**Riskiest assumptions.**
1. Parents will use the app **in the moment** of a meltdown, not only in calm moments (vision).
2. Printable/screen-free routines are enough for many families (cannibalisation vs. value).
3. Haptic breathing is engaging for 3–7s without animation-heavy design.
4. Scripts feel supportive, not judgmental.

| # | Method | Sample | Success | Kill / rethink |
|---|---|---|---|---|
| E1 | **1-week diary study**: printable routines vs. app prototype (Figma on parent's phone) | 20 families (≥6 ND children) | App prototype used in ≥1 hard moment by ≥50% of families; printables used ≥4 days by ≥60% | <25% in-moment use → reposition as routines + printables (Help Now secondary) |
| E2 | **Haptic breathing test** (prototype on phone) | 16 children 3–7 (incl. 4 autistic, 2 Deaf/HoH) | ≥70% complete 1 minute; Sensory Comfort ≥4/5 | <50% → add optional visual story |
| E3 | **Script review** with parents + ND advisors | 12 parents, 5 advisors | ≥4/5 "supportive"; 0 advisor red flags | Rewrite |
| E4 | **Setup test**: build 2 routines | 10 parents incl. 3 grandparents | ≤5 min median | >8 min → simplify templates |

**Mapping.** E1 → WP2 diary + WP4 paper prototypes; E2 → WP4 sensory A/B and accessibility round; E3 → WP3 co-design; E4 → WP4 usability.

## 12. Build handoff

**Epic CC-E1: Routines & strip.**
- **Given** a routine with 4 steps, **when** the child taps "done" on step 1, **then** the strip advances, step 1 moves to "Done", and "Next" shows step 3.
- **Given** VoiceOver, **when** the strip loads, **then** it reads "Now: bath. Next: teeth. Then: two books."
- **Given** a step is skipped, **then** no failure state appears; the routine can be finished.

**Epic CC-E2: Transition warnings.**
- **Given** a 5-minute warning, **then** a visual countdown starts, with haptic + chime at 2 min and 0 min (chime muted in silent mode).
- **Given** the adult taps "snooze once", **then** 2 extra minutes are added and snooze is disabled for that transition.

**Epic CC-E3: Breathing & Help Now.**
- **Given** Help Now is opened from the widget, **then** the script and "Breathe" button appear within 1 s without login.
- **Given** a breathing session, **then** haptic rhythm plays for the chosen pattern and stops at 2 min maximum.
- **Given** Reduce Motion, **then** breathing is shown as a filling bar with haptics.

**Epic CC-E4: Feelings.**
- **Given** the child taps "mad" + "big", **then** the app suggests 2 calm tools and shows no scoring or judgement.
- **Given** any session, **then** the camera and microphone are never accessed by feelings features (verified).

**Epic CC-E5: Printables & sharing.** **Given** a routine, **when** "Print" is tapped, **then** an A4/Letter PDF with pictures, words and a Now/Next/Done strip is produced.

**Non-functional.** Widget load ≤1 s; offline; iOS/iPadOS, Android, watchOS/Wear OS (V2); WCAG 2.2 AA; EN/ES; encrypted feelings data; zero third-party SDKs.

**QA focus.** AT matrix (VoiceOver, TalkBack, Switch, AAC symbol mode, Voice Control, haptics-only). Sensory A/B. AI safety: builder hallucination tests, crisis-keyword recall, multilingual. COPPA: feelings retention/deletion, no camera/mic. Billing: Help Now always free.

**Platform dependencies.** Lumen (strip, Dial, calm corner); My Needs (sensory, AAC); Family Hub; privacy stack (sensitive-data vault); content review workflow (psychologist + ND panel).

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Not used in hard moments | M | H | Widget; parent-held design; E1 kill criteria |
| Perceived as clinical/therapy | M | M | Plain claims; education framing; clinician referral language |
| Feelings data sensitivity | M | H | 90-day default deletion; parent-only; encryption |
| Overlap with Wavelength | H | L | Clear split: Calm Cubs = everyday 3–7; Wavelength = deeper ND support; shared profile |
| Competitor data gaps [M] | H | L | WP1 verification |

**Open questions.** Should Help Now be free forever (we think yes)? Is a watch app essential for co-regulation? Which feelings vocabulary set aligns with common pre-K SEL curricula?

## 14. Sources
- [V] Moshi: https://apps.apple.com/us/app/moshi-kids-sleep-relax-play/id1306719339 · https://www.trustpilot.com/review/moshikids.com
- [V] Choiceworks, Brili, Goally, Joon, Mightier data: [raw 04](../../../research/raw/04-neurodivergent-and-inclusive-ux.md) · Brili Play: https://play.google.com/store/apps/details?id=co.brili.routines&hl=en_US&gl=US
- [V] Pok Pok takeaway meltdown review: https://www.commonsensemedia.org/app-reviews/pok-pok-playroom/user-reviews/adult
- [V] EU AI Act emotion-recognition ban and COPPA 2025: [Research paper §8](../../01-research-paper.md)
- [M] Daniel Tiger's Grr-ific Feelings (PBS KIDS), Breathe Think Do with Sesame, GoNoodle, Headspace and Calm kids content, 988 crisis line, NCAEP visual supports: to verify in WP1

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Merge → Lanternling skin on EN-05 Routine, Regulation & Focus engine |
| **Ships in** | Lanternling app (S1) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 77/100 [I] |
| **Consumes engines** | EN-05, EN-02 |
| **Studio features used** | SX-12, SX-19, SX-25 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = CC-01, CC-02, CC-03, CC-04, CC-08.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| CC-E1 | **Childcare handoff card** | A one-page routine and 'what calms me' card for daycare or grandparents (Sensory Passport, SX-12). |
| CC-E2 | **Gentle pathway to more support** | If a caregiver asks for more help, offer Wavelength tools. The caregiver chooses; no labelling. |

### 15.3 New validation question
Is a routine built once reused across home, daycare and grandparents? Diary study, n=20.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 4 | 5 | 3 | 3 | 4 | 3 | 5 |

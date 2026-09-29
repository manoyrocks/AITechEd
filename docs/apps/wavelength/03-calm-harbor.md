# Calm Harbor: App Strategy & Product Specification

> **Venture:** Wavelength · **App #:** 3/7 · **Ages:** 4–17 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/05-wavelength-neurodivergent.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary, or carried over from studio raw research · [M] memory · [E] estimate · [I] inference
> **Evidence tiers:** E1 FDA/RCT on product · E2 peer-reviewed product studies · E3 evidence-based method, product untested · E4 testimonials/contested

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A quiet harbor in your pocket: learn what your body and senses are telling you, find what helps *you*, and get to it fast, even mid-overwhelm, without flashing, noise or judgement. |
| **Primary user / buyer** | Users: ND children and teens with sensory processing differences, anxiety or dysregulation. Buyers: parents (B2C/ESA), OTs (clinician licence), schools (calm-corner licence). |
| **Core job-to-be-done** | "When my body feels too loud, I want to get to the thing that helps me in one tap, so I can come back to myself without being told to 'calm down'." Caregiver/OT: "I want to know my child's sensory preferences and have a plan everyone uses." |
| **Category on the stores** | Health & Fitness › Kids / Education. Wellness positioning; no treatment claims. |
| **Top competitors** | Mightier, Zones of Regulation app/curriculum, Breathe Think Do with Sesame, Moshi, Headspace/Calm kids content, Finch, Miracle Modus, sensory toy apps |
| **Our wedge** | 1) **Sensory-safe by construction:** no flashing, sound optional, screen-dim mode and offline, where mainstream calm apps are audio-heavy and some sensory apps flash [V2]. 2) **Personal, not generic:** a sensory profile built with an OT or caregiver drives a "my toolbox" of 3–6 strategies, one tap from anywhere. 3) **Self-report only:** a pictorial "engine" check-in teaches interoception without biometric sensors or emotion AI, avoiding Mightier's hardware cost and sensitive heart-rate data [V]. |
| **Business model** | Wavelength Family plan; Calm Harbor tier ≈$4.99/mo [E]; school calm-corner licence; OT practice licence. |
| **North-star metric** | Weekly self-initiated regulation moments (learner opens the toolbox or check-in themselves) per active learner. |
| **MVP candidate?** | **Yes.** It is part of the Year-1 trio. |

## 2. Problem & users
**Problem statement.**
- Sensory over-responsivity and dysregulation are common in autism, ADHD and sensory processing differences (Lumen P1 rationale, [V2, raw 04]). Parents report that bright, noisy, reward-heavy apps are blamed for meltdowns [M, raw 03].
- Existing tools split into three camps:
  - **Mainstream mindfulness** (Headspace, Calm, Moshi): audio-first and generic. A 2026 parent-facing comparison argues Calm is not suited to autistic children with sensory sensitivities [V2] ([Hush Away](https://www.hushaway.com/blogs/comparing-moshi-calm-headspace-for-neurodivergent-children-kids)).
  - **Curriculum tools** (Zones of Regulation): strong school adoption, but the app is a small companion to a paid curriculum ($144 per user per year for the digital curriculum) [V] ([Zones](https://zonesofregulation.com/subscription-plans-and-pricing/)).
  - **Biofeedback** (Mightier): the best evidence in the category (sham-controlled RCTs [V2, raw 04]), but $28–40/mo with a heart-rate sensor [V] ([Mightier plans](https://www.mightier.com/plans/)). It is game-based and uses biometric data.
- Lived-experience tools such as Miracle Modus (made by an autistic developer) show demand, but include moving or flashing visuals risky for photosensitive users [V2, raw 04].
- **Interoception** (noticing body signals) is an emerging OT focus:
  - An 8-week pilot of the Interoception Curriculum with 8 autistic students aged 6–13 improved an interoception measure [V] ([Hample et al.](https://www.semanticscholar.org/paper/An-Interoception-Based-Intervention-for-Children-A-Hample-Mahler/156f79385620b3876ad40bf7f07aab1da27beec1)).
  - A 25-week school study (n=14, ages 9–19) found significant gains in interoceptive awareness and emotion regulation [V] ([PubMed 35539883](https://pubmed.ncbi.nlm.nih.gov/35539883/)).
  - These are small, uncontrolled studies (E2 for the curriculum, not for any app).

**Personas**
| Persona | Snapshot | What Calm Harbor must do |
|---|---|---|
| **Mia, 9, ADHD + dyslexia** | Homework ends in tears; big feelings fast. | One-tap "I need a break" toolbox; picture-based engine check; movement breaks; no reading needed. |
| **Ethan, 14, autistic, sensory-sensitive** | Overwhelmed in the school cafeteria; hates being told to breathe. | A discreet phone mode (looks like a notes app), dark screen, headphone-friendly brown noise, a "tell my teacher" card, his own sensory profile to share. |
| **Kai, 4, autistic** | Loves water; distressed by sudden noise. | Caregiver-led co-regulation mode: water visual (slow, no flashing), caregiver script prompts. |
| **Priya, OT** | School-based, 45 students. | Build sensory profiles with students, assign a sensory diet, see self-reported check-ins (with consent) without surveillance. |

**Needs & wants**
| Need | Evidence | How Calm Harbor addresses it |
|---|---|---|
| Regulation tools that don't over-stimulate | Raw 03/04; Lumen P1 | Calm-only visuals, no flashing, sound off by default, dim mode |
| Personalized strategies | OT practice [M]; Zones "tools to try" [V] | Sensory profile → toolbox of 3–6 personal tools |
| Body awareness | Interoception studies [V] | Pictorial engine / body-map check-ins (self-report) |
| Speed during overwhelm | Vision riskiest assumption | Toolbox reachable in 1 tap from the lock-screen widget or Day's Break card; no login |
| Adults co-regulating, not controlling | Affirming stance; AAP co-engagement [V2] | Co-regulation scripts for adults ("lower your voice, offer, wait") |
| Privacy of feelings data | COPPA 2025 biometric expansion [V2] | No biometrics; check-ins on device; the learner chooses what to share |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Evidence tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| **Mightier** | Mightier (Boston Children's spinout) | Listed on the ClassWallet ESA marketplace [V]; HSA/FSA eligible [V] | **$40/mo; $34/mo (6-mo); $28/mo (12-mo)**, sensor included; covers every child in the household; 90-day money-back [V] | n/a | Heart-rate biofeedback games; kids practise calming to make games easier [V] | Recurring cost [V2]; children's self-rated anger unchanged in RCT [V2] | Wearable HR = sensitive biometric data; game intensity [I] | **E1/E2** (sham-controlled RCTs) [V2] | [Plans](https://www.mightier.com/plans/), [ClassWallet](https://mightier-classwallet-shop.myshopify.com/), [PMC RCT](https://pmc.ncbi.nlm.nih.gov/articles/PMC8440816/) |
| **The Zones of Regulation app + Digital Curriculum** | Zones of Regulation / Social Thinking | Widely used school framework [M] | App **$5.99**; bundle $14.49; Digital Curriculum **$144/user** [V] | n/a | Common language (4 zones), "tools to try" cards [V] | App is a small companion; curriculum cost [I]; some ND critics say the zones can become behavior compliance ("be in green") [M] | Simple visuals | E3 (framework) [M] | [App Store](https://apps.apple.com/us/app/the-zones-of-regulation/id610272864), [Pricing](https://zonesofregulation.com/subscription-plans-and-pricing/) |
| **Breathe, Think, Do with Sesame** | Sesame Workshop | Play 1,740+ reviews; Amazon 1,287 ratings [V] | **Free** [V] | 3.8★ US App Store (149); 3.4★ Play [V] | Bilingual EN/ES; problem-solving steps; belly breathing [V] | Short; young-only [I] | Gentle; character-led | E3 | [App Store](https://apps.apple.com/us/app/breathe-think-do-with-sesame/id721853597) |
| **Moshi Kids** | Moshi | **70K ratings** on iOS [V] | $9.99/mo or $49.99/yr (7-day trial) [V] | **4.7★ iOS**; 3.1★ Play (7,097); Trustpilot 2.8 [V] | 300+ sleep stories, sounds, meditations [V] | Billing/support (Trustpilot 2.8) [V] | Audio-first; not visual-first | E4 | [App Store](https://apps.apple.com/us/app/moshi-kids-sleep-relax-play/id1306719339), [Trustpilot](https://www.trustpilot.com/review/moshikids.com) |
| **Headspace (kids content)** | Headspace | Mass-market adult app [M] | Subscription [M] | n/a | Kids themes (Calm, Focus, Kindness, Sleep, Wake Up) by age band [V2] | Less visual support for younger kids who need visual cues [V2] | Audio-led | E3 (mindfulness broadly) | [Understood](https://www.understood.org/en/articles/8-meditation-apps-for-kids) |
| **Finch** | Finch Care | **12.5M+ downloads**; ≈400k downloads and ≈$2M revenue in a recent month (estimate) [V2] | Freemium [V2] | **4.9★** (≈752K iOS ratings) [V2] | Self-care pet; no streak anxiety [V2] | "Childish" to some [V2]; pet-attachment mechanic [I] | Gentle design; pet ≈ companion framing | E4 | [mwm.ai](https://mwm.ai/apps/finch-self-care-pet/1528595748), raw 03 |
| **Miracle Modus** | Independent autistic developer | Niche [I] | Free/low [M] | n/a | Hypnotic visuals + soft bells; lived-experience design [V2] | **Flashing/moving visuals: photosensitive risk** (WCAG 2.3.1) [V2] | Motion-heavy | E4 | raw 04 |

Also scanned: fluid/"sensory toy" apps (Fluid, Sensory Baby) [M]. They are popular for visual stimming, but vary widely in flash risk and ad load. Our "Stim Space" (V1) offers a safe, ad-free version.

**Feature matrix**
| Feature | Mightier | Zones | Sesame BTD | Moshi | Headspace | Finch | Our decision |
|---|---|---|---|---|---|---|---|
| Personal sensory profile | ✗ | ◐ (tools to try) | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Self-report check-in (pictorial) | ◐ | ✓ | ◐ | ✗ | ◐ | ✓ | **Improve**: interoception body-map |
| Physiological sensor | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject for MVP** (cost, biometric data). Optional V2 manual heart check, device-local |
| Breathing guide with haptics | ◐ | ◐ | ✓ | ◐ | ✓ | ✓ | **Parity+**: haptic-only option |
| Calm visual (no flashing) | ✗ (games) | ◐ | ◐ | ◐ | ◐ | ✓ | **Differentiate**: guaranteed and flash-tested |
| Sounds library / brown noise | ✗ | ✗ | ✗ | ✓ | ✓ | ◐ | **Parity** |
| Co-regulation scripts for adults | ✓ (conversation cards) [V] | ✓ (curriculum) | ◐ | ✗ | ✗ | ✗ | **Parity** |
| Sensory diet planner (OT) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Offline | ◐ | ✓ | ✓ | ◐ | ◐ | ◐ | **Parity** |
| Discreet teen mode | ✗ | ✗ | ✗ | ✗ | ✓ (adult app) | ✓ | **Improve** |
| Games that get harder when upset | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject**: we don't make regulation a performance |
| Pet/companion that "needs you" | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Reject**: companion/obligation mechanic (P18) |
| Emotion detection from face/voice | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject** (EU AI Act Art. 5; ethics) |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| C1 | **My Sensory Profile** ★ | Built together (learner + caregiver/OT) with picture cards: "I like / I don't like / I'm not sure" across 8 senses (incl. interoception and vestibular); exportable profile card | OT practice [M]; no competitor | Differentiate | MVP | Must |
| C2 | **My Toolbox, one tap** ★ | 3–6 personal tools, drawn from the profile, reachable from the app icon long-press / widget / Day Break card; no sign-in needed | Speed during overwhelm | Differentiate | MVP | Must |
| C3 | **Engine / body check-in** | Pictorial "engine" (slow / just right / fast) + optional body map ("where do you feel it?") + "what I need" choices; self-report only | Interoception evidence [V]; Zones [V] | Improve | MVP | Must |
| C4 | **Calm corner visuals** | 6 slow visuals (water, clouds, sand, lava lamp, stars, dark) at ≤0.5 Hz motion, flash-tested; a "screen dim" mode | Miracle Modus lesson [V2] | Differentiate | MVP | Must |
| C5 | **Breathing & body tools with haptics** | Shape breathing (square, balloon, hum) with haptic-only mode; pressure/"push the wall" movement cards; humming | Sesame/Headspace parity | Parity | MVP | Must |
| C6 | **Sound shelf** | Brown/pink/white noise, rain, favorite-song link; volume cap; fade-in only | Moshi parity; auditory sensitivity | Parity | MVP | Should |
| C7 | **Co-regulation scripts** | For adults: short, literal scripts ("Say less. Offer 2 choices. Wait.") linked to the child's profile | Mightier conversation cards [V]; affirming stance | Parity | MVP | Must |
| C8 | **"Tell someone" cards** | Show-screen cards: "I need a break", "Too loud", "Please don't touch", "I'm OK, just need quiet"; optional text to a trusted adult (teen) | Self-advocacy; AAC link | Differentiate | MVP | Must |
| C9 | **Discreet mode** | Neutral icon/theme, dark UI, headphones-first for teens | Ethan; stigma | Improve | MVP | Should |
| C10 | **What helped? reflection** | After a tool: "Did it help?" 3 faces (optional). Builds the learner's own evidence about what works | Learner agency | Improve | MVP | Must |
| C11 | **Sensory diet planner** | OT/caregiver schedules sensory activities into Wavelength Day (movement before homework, etc.) | OT workflow | Differentiate | MVP | Should |
| C12 | **My Needs + Sensory Dial (Calm locked as default)** | Shared hub | Lumen | Lumen | MVP | Must |
| C13 | **Offline + no-login quick access** | All tools work offline; toolbox opens without auth (settings need the adult gate) | Crisis use | Lumen | MVP | Must |
| C14 | Stim Space | Safe, ad-free, non-flashing visual/tactile stim toys (drag optional, tap alternatives) | Sensory apps demand [M]; affirming stims | Differentiate | V1 | Should |
| C15 | Strategy suggestions (AI) | Suggest tools from the profile and "what helped" history | Vision AI role | Differentiate | V1 | Could |
| C16 | Classroom calm-corner kiosk | Shared-tablet mode for a school calm corner, no personal data by default | School channel | Improve | V1 | Should |
| C17 | Interoception lessons | 12 short, OT-authored body-signal explorations (co-designed with autistic adults) | Interoception evidence [V] | Improve | V1 | Should |
| C18 | Wearable haptic breathing | Watch haptic breathing, no HR capture by default | Discreet use | Improve | V2 | Could |

★ Signature features: **My Sensory Profile (C1)** and **one-tap Toolbox (C2)**. The MVP has 13 features.

## 5. Core experience & key user flows
**Core loop:** notice (check-in or feeling) → open Toolbox in 1 tap → use a tool for 1–5 min → "did it help?" (optional) → back to life. The designed ending is "Ready to go back?", with a choice of "Yes" or "A bit more". There is **no pressure to be "green"**.

**Flow 1: Onboarding (≤5 min)**
1. The Calm Sensory Dial is preset. The screen shows one visual with sound off.
2. The adult (or teen) answers: age band, who sets it up, look (playful / neutral / discreet).
3. Quick profile: 12 picture cards (loud noise, bright light, hugs, spinning, humming…) sorted into like / don't like / not sure.
4. The Toolbox is auto-built with 4 tools, which the learner can swap.
5. "Try one now": the balloon breathing with haptics.

**Flow 2: Mid-overwhelm use (Mia)**
1. Mia long-presses the app icon and chooses "Toolbox" (or taps the Break card in Day).
2. Four big picture tiles appear: Push the wall, Water, Brown noise, Hum.
3. She picks Water. The screen dims to 40% and a slow water visual plays with no sound.
4. After 3 minutes, a gentle visual prompt asks "Ready to go back?" with no sound. She taps "A bit more".
5. Afterwards she can answer "Did it help?" or skip it.

**Flow 3: OT / caregiver view**
1. Priya builds a profile with the student in a session.
2. She assigns a sensory diet (C11) that appears in Day.
3. With the student's consent (teen) or the parent's consent (child), she sees a weekly count of self-initiated tool uses and the tools rated helpful. **There are no timestamps of "meltdowns" and no incident logs.**

**Flow 4: My Needs:** Dial, sound channels, haptics, dim level, visual speed, discreet mode, who sees check-ins.

**Flow 5: Billing:** Fair-billing charter. The Toolbox and "Tell someone" cards stay free forever as accommodations.

**Information architecture:** Toolbox (home) · Check-in · Calm corner · Tell someone · My profile. Adult area: Scripts, Sensory diet, Summary, Settings.

**Session design:** Tools run for 1–5 min with a user-set default. There are no streaks, and no notifications to the child's device except user-set reminders.

## 6. Inclusive, accessible & sensory design spec
**Sensory Dial in Calm Harbor.** Calm is the default and is recommended; Lively is limited.
| Level | Motion | Sound | Color | Feedback |
|---|---|---|---|---|
| **Calm (default)** | ≤0.5 Hz slow drifts; no sudden starts; 1 s fades | Off; sounds only when chosen, fade-in over 2 s, peak capped [E: ≤70 dB(A) at typical headphone volume] | Low saturation, dark mode default at night | Haptic only |
| **Balanced** | Gentle | User-chosen sounds | Moderate | Soft chime + haptic |
| **Lively (opt-in)** | Still ≤3 flashes/s, no red flashes, no high-contrast strobing | Music allowed | Vivid | Chime |

**Photosensitivity:** Every visual passes an automated flash and red-flash analysis (WCAG 2.3.1 general and red flash thresholds) and a pattern check (no high-contrast stripes). The same test runs in CI on the design assets.

**Input modes:** All tools work by tap, switch (scan 4 tiles), eye gaze (dwell) or voice ("water"), and **never** need drag or precise gestures. Stim Space offers drag *and* tap-to-ripple.

**Targets:** Toolbox tiles ≥2.5 cm (child) and ≥2 cm (teen); maximum 6 tiles.

**Reading:** No reading required. Every tile has a picture and an audio label (audio label plays only if audio is on). Adult scripts use plain language at grade 6.

**Audio:** Separate channels for narration, sound shelf and effects. Every audio cue has a visual or haptic twin. Captions for any narration.

**Age-respectful themes:** Playful, neutral and discreet (teen). Discreet mode uses an unremarkable icon and a dark theme.

**Lumen principles: acceptance criteria**
| P | Criterion |
|---|---|
| P1 | Calm by default; Reduce Motion freezes all visuals into slow cross-fades |
| P2 | Sound off by default; 100% visual/haptic twins |
| P3 | Toolbox layout fixed; same tile positions every time |
| P4 | Single-tap everything; tiles ≥2 cm |
| P5 | Picture + audio labels; literal adult scripts |
| P6 | BDA text in the adult area |
| P7 | Tap, switch, gaze and voice for all tools |
| P8 | No "wrong" choices; skip any question |
| P9 | "Ready to go back?" ending; no autoplay chains |
| P10 | No login needed for the Toolbox |
| P11 | No required timers; tool length is the user's |
| P12 | Profile in My Needs; accommodations free |
| P13 | Discreet mode for teens |
| P14 | ≤5 min setup; co-regulation scripts |
| P15 | No points for "calming down"; no compliance zones |
| P16 | Stims framed as valid regulation; ND board reviews all content |
| P17 | "Wellness and self-regulation tools"; never "reduces meltdowns" or "treats anxiety" |
| P18 | No biometrics, no emotion AI; check-ins on device |

**Target Lumen score:** 24/24.

## 7. AI specification & guardrails
- **What AI does (V1):** A simple, explainable recommender ranks tools from the profile and "what helped" ratings. The rules are readable: "You said Water helped 4 of 5 times." An LLM is used only in the adult area, to draft co-regulation scripts from ND-board-approved templates, and every draft is reviewed by the adult.
- **What AI does not do:** No face, voice or physiological emotion inference (EU AI Act Art. 5 prohibits emotion recognition in education [V2, raw 04]). No chat with the child and no companion persona. No prediction or logging of "meltdown risk". No diagnosis.
- **Distress escalation (self-report based):** If a teen selects "I'm not safe" or "I want to hurt myself" (a check-in option co-designed with clinicians), the app shows crisis resources (988 in the US, Shout 85258 / Childline in the UK [M]) and offers to message a pre-set trusted adult. It never auto-contacts anyone without consent, except as required by the school safeguarding policy in school mode, which is disclosed to the learner.
- **Evaluation:** A recommender offline replay on WoZ diary data; ND board review of script templates; red-team tests of the self-harm pathway with clinicians.
- **Cost [E]:** Negligible. The recommender runs on device, and script drafts cost ≈$0.002 each.

## 8. Data, privacy & compliance
| Data | Why | Retention | Where |
|---|---|---|---|
| Sensory profile | Toolbox | Account life | Device + opt-in cloud |
| Check-ins, "what helped" | Learner's own insight; OT summary with consent | 12 months rolling [E]; learner can delete | Device by default |
| Tool usage counts | Summary | 12 months | Cloud aggregate, with consent |
| Crisis-path events | Safety | Not stored beyond the session unless the trusted-adult message is sent | Device |

- **COPPA 2025:** Feelings check-ins are sensitive. Default is on device, with separate consent for sharing. We collect no biometrics, which avoids the expanded biometric-identifier scope [V2].
- **HIPAA:** applies under the OT clinician licence (BAA).
- **FERPA:** school calm-corner mode stores no personal data by default.
- **FDA:** general-wellness positioning; no claims to treat anxiety, ADHD or autism. FDA general wellness guidance allows stress/relaxation claims not tied to disease [M].
- **FTC:** no efficacy claims beyond the evidence tier.
- **EU AI Act:** no emotion recognition. **UK AADC:** profiling off by default; the recommender is on device and explainable.

## 9. Monetization & go-to-market
| Tier | Price [E] | Benchmark |
|---|---|---|
| Free | Toolbox (4 tools), Tell-someone cards, 1 calm visual | Sesame free [V] |
| Calm Harbor | $4.99/mo or $39/yr | Moshi $49.99/yr [V]; Zones app $5.99 [V] |
| Family plan | ≈$19/mo, all apps | Mightier $28–40/mo [V] |
| School calm corner | $300/school/yr [E] | Zones digital curriculum $144/user [V] |
| OT practice | $15/mo per practitioner | — |

- **Channels:** OTs (sensory-profile workflows), school counselors and SENCOs, ESA marketplaces (Mightier's ClassWallet listing proves the path [V]), HSA/FSA eligibility review [M], and autistic-led sensory communities.
- **ASO:** sensory app, calm down app kids, autism calm, sensory overload, calm corner, breathing kids.
- **Launch:** US and UK.

## 10. Success metrics
- **North star:** Weekly self-initiated regulation moments per active learner.
- **Input metrics:** Toolbox opens without an adult prompt (%); profiles completed; "helped" rating ≥ "a bit" (%); sensory diet adherence.
- **Guardrails:**
  - Sensory Comfort ≥4.5/5
  - 0 photosensitivity-test failures
  - 0 billing complaints
  - Crisis-path QA 100%
  - Toolbox open time ≤2 s
- **Outcomes:** Caregiver- and learner-rated regulation (a validated measure chosen with the OT panel [M]), interoceptive awareness (a self-report scale for older children [M]). **Evidence:** E3 → E2 (pre-registered OT clinic pilot).
- **Retention [E]:** Use is episodic. Target 30-day active ≥40% and ≥2 self-initiated uses per week among actives.

## 11. Validation plan
| # | Assumption | Experiment | Sample | Success | Kill |
|---|---|---|---|---|---|
| 1 | Children will use it **during** dysregulation, not only when calm | OT-led in-clinic sessions with a paper + Figma calm corner; 2-week caregiver diary with a printed toolbox + Figma | 15 learners (in clinic); 15 families (diary) | ≥50% of logged hard moments include a toolbox attempt; learner-rated "helped" ≥3/5 | <25% → reposition as a co-regulation tool for adults |
| 2 | Sensory profile is quick and useful | Card-sort with OTs and families | 10 OTs, 15 families | ≤10 min; OT usefulness ≥4/5 | — |
| 3 | Teens accept discreet mode | Figma test | 12 ND teens | ≥70% "would use at school" | — |
| 4 | Calm vs. Lively (W4) | Lumen sensory A/B | 20 | Comfort +1 for ND participants | — |
| 5 | Schools buy calm-corner kiosks | 8 counselor/SENCO interviews + LOIs | 8 | ≥3 pilot LOIs | — |

**Mapping:** WP2 diaries (meltdowns), WP4 sensory A/B, WP5 channels.

## 12. Build handoff
**Epic A: Toolbox quick access**
- *Given* the app is closed, *when* the learner long-presses the icon and chooses Toolbox, *then* the Toolbox appears in ≤2 s with no login and no sound.
- *Given* switch mode, *when* scanning, *then* only the ≤6 tool tiles and "back" are in the scan order.

**Epic B: Calm visuals**
- *Given* any visual asset, *when* CI runs the flash analyzer, *then* it fails the build if the general or red flash thresholds are exceeded.
- *Given* Reduce Motion on, *then* visuals render as slow cross-fades ≤0.2 Hz.

**Epic C: Profile & check-in**
- *Given* the profile card sort, *when* completed, *then* ≥3 tools are suggested and the learner can replace any of them.
- *Given* a check-in, *then* it is stored on device only unless sharing consent exists.

**Epic D: Crisis path**
- *Given* a teen selects "I'm not safe", *then* local crisis resources display within 1 tap and the optional trusted-adult message requires one confirm.

**Non-functional requirements:** Fully offline; ≤1 s cold start to Toolbox [E]; WCAG 2.2 AA; iOS/Android; localization EN/ES; widget support.

**QA focus**
- **AT matrix:** VoiceOver, TalkBack, Switch Control/Access, Eye Tracking, Voice Control, Dynamic Type XXL, Reduce Motion, Guided Access (kiosk).
- **Sensory A/B;** photosensitivity analyzer on all assets.
- **AI safety:** script templates, crisis pathway.
- **COPPA:** check-in data locality.
- **Billing:** free-tool guarantee.

**Platform dependencies:** Lumen (Dial, calm corner component), Circle (profile sharing), Day (Break card, sensory diet), privacy stack.

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Kids don't reach for a phone mid-meltdown | High | High | Adult co-regulation mode; printable toolbox; widget; validate early (#1) |
| Screens as regulation conflict with some OT advice | Med | Med | Include screen-free tools (push the wall, hum); "put the phone down" endings |
| Crisis content liability | Low | High | Clinician-reviewed pathway; resources only; safeguarding policy |
| Weak outcome evidence vs. Mightier | Med | Med | Position on access and personalization; pre-register an OT pilot |
| Zones-style "be green" compliance creep | Med | High | No zone scoring; ND board veto |

**Open questions:** Should we partner with a validated sensory profile instrument (licensing) or keep our own non-diagnostic card sort? Which V2 wearable, if any, can support haptics without collecting biometrics?

## 14. Sources
- [V] Mightier plans: https://www.mightier.com/plans/ ; ClassWallet store: https://mightier-classwallet-shop.myshopify.com/ ; [V2] RCTs: https://pmc.ncbi.nlm.nih.gov/articles/PMC8440816/ , https://link.springer.com/article/10.1007/s10802-025-01387-x
- [V] Zones of Regulation app and pricing: https://apps.apple.com/us/app/the-zones-of-regulation/id610272864 ; https://zonesofregulation.com/subscription-plans-and-pricing/
- [V] Breathe, Think, Do with Sesame: https://apps.apple.com/us/app/breathe-think-do-with-sesame/id721853597 ; https://play.google.com/store/apps/details?id=air.com.sesameworkshop.ResilienceThinkBreathDo&hl=en_US
- [V] Moshi Kids: https://apps.apple.com/us/app/moshi-kids-sleep-relax-play/id1306719339 ; https://www.trustpilot.com/review/moshikids.com
- [V2] Headspace kids content: https://www.understood.org/en/articles/8-meditation-apps-for-kids ; neurodivergent comparison: https://www.hushaway.com/blogs/comparing-moshi-calm-headspace-for-neurodivergent-children-kids
- [V2] Finch: https://mwm.ai/apps/finch-self-care-pet/1528595748
- [V] Interoception studies: https://www.semanticscholar.org/paper/An-Interoception-Based-Intervention-for-Children-A-Hample-Mahler/156f79385620b3876ad40bf7f07aab1da27beec1 ; https://pubmed.ncbi.nlm.nih.gov/35539883/ ; https://pubmed.ncbi.nlm.nih.gov/38375672/
- [V2] Miracle Modus, EU AI Act, COPPA: studio raw file 04
- [M] Crisis line numbers, FDA general-wellness guidance, Zones compliance critique, sensory toy apps: verify in WP1.

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (lead; shares EN-05 with Calm Cubs) |
| **Ships in** | Wavelength app (S7) |
| **Build wave** | 1b |
| **Pre-discovery priority score** | 83/100 [I] |
| **Consumes engines** | EN-05, EN-02 |
| **Studio features used** | SX-12, SX-19 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = C1, C2, C3, C5, C8, C13.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| CH-E1 | **Sensory passport for school** | A one-page sensory profile the learner approves and shares with teachers (SX-12). |
| CH-E2 | **Classroom calm-corner kiosk (V1 → MVP)** | A school edition on a shared device that anchors district sales. |

### 15.3 New validation question
OT-led sessions (n=15): use during dysregulation, not only at calm times; comfort ≥4/5.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 5 | 4 | 5 | 3 | 3 | 4 | 4 | 5 |

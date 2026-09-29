# Wavelength Voice: App Strategy & Product Specification

> **Venture:** Wavelength · **App #:** 2/7 · **Ages:** 2+ (AAC users of any age; child and teen focus) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/05-wavelength-neurodivergent.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source, or carried over from studio raw research without re-checking · [M] from memory · [E] estimate · [I] inference
> **Evidence tiers:** E1 FDA/RCT on product · E2 peer-reviewed product studies · E3 evidence-based method, product untested · E4 testimonials/contested

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Robust, affordable AAC where words never move, the voice sounds like a kid or teen, the whole team can edit the vocabulary, and AI suggestions never speak without the user's say-so. |
| **Primary user / buyer** | User: minimally speaking or non-speaking children and teens (autism, CP, Down syndrome, apraxia, DLD) and adults who need AAC. Buyers: families (B2C/ESA), schools (IEP AT), SLPs recommending; funding via IEP, ESA, EHCP. |
| **Core job-to-be-done** | "When I have something to say, I want to say it fast and in my own words, anywhere, so people hear *me*." Caregiver: "I want a robust system we won't have to abandon in a year, at a price we can afford, that our SLP trusts." |
| **Category on the stores** | Education › Special needs / Medical (AAC). iPad-first; iPhone, Android tablet, Chromebook/web. |
| **Top competitors** | Proloquo2Go, TouchChat/WordPower, LAMP Words for Life, TD Snap, Speak for Yourself, Grid for iPad, CoughDrop, Avaz, Cboard, Apple Live Speech |
| **Our wedge** | 1) **Price and platform:** robust core vocabulary at ≈$9.99/mo or a one-time price well below $249.99–$299.99 incumbents, on iOS **and** Android/web. 2) **No lock-in:** Open Board Format import/export, and users own their vocabulary. 3) **Authorship-first AI:** phrase expansion that shows exactly what it added and needs a confirming action before speaking. |
| **Business model** | Voice standalone subscription or one-time licence; included in the Wavelength Family plan; free supporter/communication-partner accounts; school and SLP licences. |
| **North-star metric** | Weekly self-initiated utterances (user-selected, not prompted) per active communicator. |
| **MVP candidate?** | **Yes.** It is part of the Year-1 trio. |

## 2. Problem & users
**Problem statement.**
- Robust AAC apps cost $149.99–$299.99 up front: Proloquo2Go $249.99 [V], LAMP WFL $299.99 [V], TouchChat $149.99 and WordPower $299.99 [V2]. Several are iOS-only (Proloquo2Go [V2]).
- Tablet AAC apps generally do not qualify for Medicaid/Medicare DME funding, unlike dedicated speech-generating devices [V2, raw 04].
- Families face SLP-run trials of 2–4 weeks and are overwhelmed by choosing a vocabulary system, fearing relearning if they switch [V2, raw 03].
- The field is divided between core-word and motor-planning approaches [V2, raw 03]. Some SLPs still hear the myth that AAC stops speech. The research consensus is that AAC does not hinder speech and may support it [V2, raw 04; M for underlying studies].
- LLM-based prediction can raise communication rates; one line of work reports entry rates up to 30.4 WPM [V] ([arXiv 2501.10582](https://arxiv.org/pdf/2501.10582)). But AAC users and the AAC community treat **authorship** as critical. An autoethnographic study of personalized LLM suggestions found users willing to trade *some* authorship for speed in time-pressured situations [V] ([arXiv 2509.13671](https://arxiv.org/html/2509.13671v1)). That trade must be the user's choice, never the default.

**Personas**
| Persona | Snapshot | What Voice must do |
|---|---|---|
| **Kai, 4, autistic, minimally speaking** | Uses some signs, loves letters and water. Family on Android. | A small-grid core board that grows without moving words; a child voice; letters available (hyperlexia); caregiver modeling mode. |
| **Zara, 7, CP + intellectual disability** | Head switch user (see Spark Switch). | 2-switch scanning of the same vocabulary; auditory scan cues in a separate earbud channel; a partner-assisted scanning mode. |
| **Jordan, 16, autistic, part-time AAC user** | Speaks sometimes; shuts down under stress. | Type-to-speak plus core board on a phone; teen voice; quick phrases; no childish symbols; private history. |
| **Dr. Nguyen, SLP** | 60-student caseload. | Evaluate quickly; edit remotely; export and import OBF; usage data for IEP; trust that motor plans stay stable. |

**Needs & wants**
| Need | Evidence | How Voice addresses it |
|---|---|---|
| Affordable robust AAC | Prices $149.99–$299.99 [V/V2]; Medicaid rarely funds apps [V2] | ≈$9.99/mo or ≈$129 one-time [E]; free supporter accounts; ESA/IEP-fundable |
| Stable motor plans | LAMP and Speak for Yourself built on consistent motor planning [V] | **Motor-plan lock:** a word's position never changes as grids grow; edits that would move words are blocked or warned |
| No lock-in | CoughDrop/Cboard open formats [V2/V] | OBF import/export; vocabulary is the user's property |
| Cross-platform | Proloquo2Go iOS-only [V2] | iOS, iPadOS, Android, Chromebook/web |
| Natural child/teen voices, multilingual | Proloquo2Go child voices [V2]; Avaz Indian languages [V2]; Cboard 33 languages [V] | Child and teen neural voices; EN, ES at launch; code-switching boards |
| Team modeling | Goally remote AAC modeling [V]; CoughDrop supporters [V2] | Partner devices mirror the board for aided language modeling |
| Speed without losing authorship | LLM rate gains [V]; authorship concerns [V] | Opt-in AI expansion with a diff view and confirm-to-speak |
| Access by switch and eye gaze | TD Snap eye-gaze path [V2]; Grid [V] | Built-in scanning, dwell, keyguard layouts |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Evidence tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| **Proloquo2Go** | AssistiveWare | Market leader with SLPs [V2]; 12K ratings on the US App Store [V] | **$249.99** one-time (Aug 2026); Gateway vocab IAP $149.99 [V] | **4.8★** (12K) [V] | Crescendo core vocab, grids that grow, natural child voices, multilingual [V2] | Price; iOS/macOS only [V] | Switch Control, scanning; polished | E3 (AAC as practice strongly supported) | [littlewords](https://littlewords.ai/blog/proloquo2go-aac-device), [App Store](https://apps.apple.com/us/app/proloquo2go-aac/id308368164) |
| **TD Snap** | Tobii Dynavox | Major clinical brand; runs on funded devices [V2] | **Free download; $9.99/mo "Speaking Upgrade"** after a 1-month trial [V] | n/a | Core First, PODD page sets, eye-gaze path [V] | Subscription to speak [V] | Strong eye-gaze and scanning heritage | E3 | [mwm.ai](https://mwm.ai/apps/td-snap/1072799231), [BridgingApps](https://search.bridgingapps.org/apps/td-snap-lite) |
| **LAMP Words for Life** | PRC-Saltillo + Center for AAC & Autism | Strong autism-SLP following [V2] | **$299.99** (US); free Discover app with 30-day trial [V] | **3.8★** (93) [V] | Consistent 1–3-hit motor plans; automaticity [V2] | Expensive; needs trained implementers [V2] | Motor-planning model | E3–E2 [M] | [BridgingApps](https://search.bridgingapps.org/apps/lamp-words-for-life), [App Store](https://apps.apple.com/us/app/lamp-words-for-life/id551215116) |
| **Speak for Yourself** | SFY LLC | Niche, SLP-founded [I] | $299.99 per one review; $149.99 plus IAP per another [V] (conflicting, re-check) | n/a | A word never moves even as vocab grows to ≈14,000 buttons [V] | Price; iOS-only [M] | Motor planning; babble lock [M] | E3 | [SFY features](https://speakforyourself.org/features/), [speechymusings](https://speechymusings.com/speak-for-yourself-app-review/) |
| **Grid for iPad** | Smartbox | UK/EU clinical staple [V2] | **$299.99 one-off or $10.99/mo**; 30-day trial; £250 UK [V] | n/a | Many built-in vocabularies, symbol and text AAC, many languages [V] | Price; complexity [I] | Strong switch access heritage | E3 | [App Store](https://apps.apple.com/us/app/grid-for-ipad-aac/id1064332378), [assistivetech](https://www.assistivetech.com.au/products/grid-for-ipad-aac-app-for-ipad) |
| **CoughDrop** | CoughDrop | Small vendor [V2] | **$9/mo or $295 lifetime per communicator**; free supporters [V2] | n/a | Cross-platform, OBF, team accounts [V2] | UI polish [V2] | Web/Android/iOS | E3 | [CoughDrop help](https://coughdrop.zendesk.com/hc/en-us/articles/115002655512) |
| **Avaz AAC** | Avaz Inc. | Multilingual, India + global [V2] | $9.99/mo, $99.99/yr, $199.99–299.99 lifetime (varies) [V2] | n/a | Indian languages; picture + keyboard [V2] | — | — | E3 | [App Store](https://apps.apple.com/us/app/avaz-aac/id909574843) |
| **Cboard** | Cboard (UNICEF-funded, open source) | **100K+ Play downloads (≈140K)** [V] | **Free** [V] | **3.9★** (≈230) [V] | Free, browser-based, 33 languages, Mulberry symbols [V] | Less robust vocabulary [V2] | Web access; basic scanning [M] | E3 | [Play](https://play.google.com/store/apps/details?id=com.unicef.cboard&hl=en_US), [cboard.io](https://www.cboard.io/en/) |

Also in scope: **TouchChat HD/WordPower** ($149.99 / $299.99 bundle; runs on funded Saltillo devices [V2]); **Proloquo4Text** (text-based AAC for literate users [M]); **Apple Live Speech and Personal Voice** (free type-to-speak and voice banking built into iOS [M]). These set the *floor*: typing to speak is free, so our value is in symbol-based robust vocabulary, access and team features.

**Feature matrix**
| Feature | Proloquo2Go | TD Snap | LAMP WFL | SFY | Grid | CoughDrop | Cboard | Our decision |
|---|---|---|---|---|---|---|---|---|
| Robust core vocabulary | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ | **Parity** |
| Consistent motor planning guaranteed | ◐ (Crescendo) [M] | ◐ | ✓ | ✓ | ◐ | ◐ | ✗ | **Parity+**: motor-plan lock enforced in the editor |
| Grid grows without moving words | ✓ | ◐ | ✓ | ✓ | ◐ | ◐ | ✗ | **Parity** |
| Android / web | ✗ | ◐ [M] | ◐ [M] | ✗ | ✗ | ✓ | ✓ | **Improve** |
| Switch scanning | ✓ | ✓ | ✓ | ◐ | ✓ | ✓ | ◐ | **Parity** |
| Eye gaze / dwell | ◐ (OS) | ✓ | ◐ | ◐ | ✓ | ◐ | ✗ | **Parity** |
| Open Board Format import/export | ✗ [M] | ✗ [M] | ✗ | ✗ | ◐ [M] | ✓ | ✓ | **Differentiate** among robust apps |
| Team editing and remote modeling | ◐ | ◐ | ◐ | ◐ | ◐ | ✓ | ◐ | **Improve** |
| Child and teen natural voices | ✓ | ✓ | ◐ | ◐ | ✓ | ◐ | OS voices | **Parity** |
| AI phrase expansion with diff and confirm | ✗ | ✗ | ✗ | ✗ | ◐ (prediction) [M] | ✗ | ✗ | **Differentiate** |
| Usage data for SLP (with consent) | ✓ | ✓ | ✓ (LAM) [M] | ◐ | ✓ | ✓ | ✗ | **Parity**, with user-visible logging |
| Pay to speak (speech locked behind subscription) | ✗ | ✓ [V] | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject**: speech output is never paywalled; lapsed subscriptions keep speaking |
| AI auto-speak / auto-complete that speaks | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject**: never speaks without user action |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| V1 | **Core vocabulary system** | Research-informed core words (≈400 in the starter set, ≈3,000 at full) plus fringe folders; developed with SLP advisors; symbols + text | Parity with all robust AAC | Parity | MVP | Must |
| V2 | **Motor-plan lock** ★ | Each word has a permanent position across grid sizes (e.g., 4×4 → 6×6 → 9×12). Hidden words keep their slot. The editor warns and blocks moves unless an SLP-role user confirms | LAMP/SFY principle [V]; trust | Differentiate | MVP | Must |
| V3 | **Progressive grids (reveal, don't move)** | Start with few visible words; reveal more in place | Proloquo2Go/SFY [V2/V] | Parity | MVP | Must |
| V4 | **Natural child and teen voices** | 4+ child/teen neural voices (EN, ES); pitch and rate; OS Personal Voice support where available [M] | Identity; P13 | Parity | MVP | Must |
| V5 | **Message bar + speak on user action** | Words collect in a bar; speaking happens on tapping Speak, or per-word speech if the user sets it | AAC convention | Parity | MVP | Must |
| V6 | **Keyboard with word prediction** | Letters page and type-to-speak; on-device n-gram prediction learned from the user's own history | Literate users; Proloquo4Text floor | Parity | MVP | Must |
| V7 | **Switch scanning + eye gaze + keyguard layout** | 1–2 switch row/column and linear scan; auditory preview cues to a separate audio route; dwell 0.5–3 s; keyguard-compatible fixed grid spacing | Access for Zara; Grid/TD parity | Parity | MVP | Must |
| V8 | **Team sharing & remote editing** | Parent, SLP and teacher edit a shared vocab set with version history and undo; changes queue for the communicator's approval (or the SLP's, for young users) | CoughDrop [V2]; SLP need | Improve | MVP | Must |
| V9 | **Partner modeling mode** | A communication partner's phone mirrors the board (read-only); modeling taps highlight on both devices without speaking on the user's device | Aided language modeling [M]; Goally remote modeling [V] | Improve | MVP | Should |
| V10 | **OBF import/export** ★ | Open Board Format `.obf/.obz` in and out; export any time, including after cancellation | No lock-in [V2] | Differentiate | MVP | Must |
| V11 | **Guided setup with SLP** | 10-minute setup: pick starting grid, voice and access method; an "SLP evaluation kit" link for trial periods | Choice overwhelm [V2, raw 03] | Differentiate | MVP | Must |
| V12 | **AI phrase expansion (opt-in)** ★ | "water + cold + please" → a suggestion "Can I have cold water, please?" with **added words highlighted**; the user can accept, edit, pick an alternative, or speak the original; nothing is spoken until the user selects | Rate gains [V]; authorship [V] | Differentiate | MVP (off by default) | Should |
| V13 | **Quick phrases & teen mode** | User-owned quick phrases; teen symbol set; phone layout; private history | Jordan; P13 | Improve | MVP | Must |
| V14 | **Never mute on lapse** | If a subscription lapses, the board keeps speaking and exporting; only team/AI/cloud features pause | Ethics; TD Snap contrast [V] | Lumen | MVP | Must |
| V15 | Context word suggestions | Suggest next words from the user's own history and optional context ("at school"), never from other users' data | LLM prediction [V] | Differentiate | V1 | Could |
| V16 | Usage insights for SLP (consented, user-visible) | Word counts by category, new words, modeling sessions; IEP export | SLP need | Parity | V1 | Should |
| V17 | Multilingual boards and code-switching | Same motor plan across languages where grammar allows | Avaz/Cboard [V] | Improve | V1 | Should |
| V18 | Dedicated-device mode | Locked single-app mode guide (Guided Access / Android pinning) and support for a funded-SGD partner | Medicaid SGD path [V2] | Improve | V2 | Could |
| V19 | Watch / quick-talk | Top 12 quick phrases on a watch | Teen use | Improve | V2 | Could |

★ Signature features: **Motor-plan lock (V2)**, **authorship-first AI expansion (V12)** and **OBF no-lock-in (V10)**. The MVP has 14 features (V1–V14). V12 is included in the MVP but off by default, pending the authorship validation (§11).

## 5. Core experience & key user flows
**Core loop:** open, with the board always on its home page → select words (tap, switch or gaze) → message bar → speak (user action) → partner responds → continue. There is no "ending": AAC is a voice, always available. **Voice never has session limits, timers or engagement prompts.**

**Flow 1: Onboarding (≤10 min to first spoken message; ≤5 min with the "Quick start" preset)**
1. The adult or the user chooses: "I'm setting this up for someone" / "for myself" / "I'm an SLP".
2. Access: touch, switch, eye gaze or keyguard, with a live test.
3. Starting grid: a recommendation from 3 questions (fine motor, vision, current symbol use), which can always be changed later without moving words.
4. Voice: child, teen or adult, with a preview; the user picks where possible.
5. The home board opens, and a 3-card co-play tip shows how to model.

**Flow 2: Core communication with AI expansion (opt-in)**
1. Kai selects "want", "water" and "cold".
2. He taps Speak. That speaks exactly "want water cold". **Or**, if expansion is on, a suggestion chip appears *above* the bar: "I want cold water, please". Added words are underlined with a "+" marker, and 2 alternatives are offered.
3. The user selects the chip to speak it, edits it, or ignores it. **Ignoring it has no penalty and never auto-speaks.**
4. History shows what was spoken and whether the AI suggested it, visible to the user and the team.

**Flow 3: SLP / team view**
1. The SLP opens the shared vocab, adds a "swimming" fringe folder, and sends the change.
2. The communicator's device shows "New words from Dr. Nguyen: accept?" (auto-accept is possible for users under 8 if the parent allows).
3. Usage insights (V1) show new words used this week. Export to PDF for the IEP.

**Flow 4: My Needs:** access method, scan speed, dwell, voice, symbol set, button size and spacing, high contrast, feedback (audio click, visual highlight or haptic) and the Sensory Dial.

**Flow 5: Billing:** Fair-billing charter. Speech never stops. One-tap cancel and export any time.

**Information architecture:** Board (home) · Keyboard · Quick phrases · History · Settings (locked behind an adult gate *or* user-controlled for self-managing users). The page layout is fixed, with Home, Back, Clear and Speak in permanent positions.

## 6. Inclusive, accessible & sensory design spec
**Sensory Dial in Voice**
| Level | Visual | Audio | Feedback |
|---|---|---|---|
| **Calm (default)** | No animation; button press = 150 ms border highlight; muted palette with Fitzgerald-style category colors at reduced saturation [M] | Speech only; no click sounds | Optional light haptic |
| **Balanced** | Button press scale 95% | Soft click on selection | Haptic |
| **Lively (opt-in)** | Color-rich symbols | Click + speech | Haptic |

No flashing anywhere (WCAG 2.3.1). Speech output volume is separate from the device volume and has a "whisper" preset.

**Access specification**
| Mode | Spec |
|---|---|
| **Touch** | Button sizes from 2.5 cm (early grids) to 0.9 cm (9×12 on large iPad) [E]; accept-on-release or accept-on-touch; hold-duration filter 0–1 s; repeat-ignore 0–2 s (for tremor or repeated hits) |
| **Keyguard** | Fixed-spacing grid presets matching common keyguard templates; no layout shifts ever |
| **Switch (1)** | Auto-scan row → column or linear; scan speed 0.5–5 s; "scan loops before pause" 1–5 |
| **Switch (2)** | Step scan (move / select); partner-assisted auditory scanning with preview cues in an earbud and final speech on the speaker |
| **Eye gaze** | Dwell 0.4–3 s with a visible ring fill (no flashing); gaze-blink option off by default; "rest area" that never selects; supports Apple Eye Tracking and external gaze bars where the OS exposes them [M] |
| **Head tracking** | Via OS pointer control (Apple Head Tracking [V2, raw 04]; Android Camera Switches [M]) |
| **Keyboard** | Full keyboard navigation; type-to-speak |

**Motor-plan consistency rules**
1. Each word has a permanent coordinate on the largest grid. Smaller grids are *views* that reveal a subset in the same relative positions.
2. Hiding a word leaves an empty, inert slot in the same place, never collapsing the layout.
3. Navigation to a fringe word always follows the same path (≤3 hits for the top 400 words).
4. Editor: moving a word shows "This will change [Kai]'s motor plan for 'go'. Only do this with your SLP." It requires SLP-role confirmation and is logged.
5. Language switch: same position for translated core words where possible.

**Reading and typography:** Symbol + text on every button. Text position (above or below) is fixed. Font is sans-serif and scalable, with BDA spacing in the message bar.

**Age-respectful themes:** Child symbols, teen symbols (line icons, photos) and a text-first layout, all using the same motor plan. There are no cartoon mascots.

**Lumen principles: Voice acceptance criteria**
| P | Criterion |
|---|---|
| P1 | Calm default; Reduce Motion is honored with 0 animations |
| P2 | Selection feedback is visual and optionally haptic; audio clicks off by default |
| P3 | Home, Back, Clear and Speak never move; motor-plan lock tests pass 100% |
| P4 | All actions work by single tap, switch or dwell; no gestures on the board |
| P5 | Settings in plain language; symbol + text labels |
| P6 | Message bar text is adjustable |
| P7 | Touch, 1–2 switch, eye gaze, keyboard and head pointer all verified |
| P8 | Undo on every word; clear-bar undo |
| P9 | No engagement mechanics at all |
| P10 | No password to open the board; the adult gate uses a non-memory option (hold 3 s + a picture) |
| P11 | No timeouts on input; the message bar persists |
| P12 | Access settings stored in My Needs and portable |
| P13 | Teen and adult symbol sets |
| P14 | Guided setup; team editing |
| P15 | Not applicable; no rewards in AAC |
| P16 | ND board and **adult AAC-user advisors** sign off defaults and AI policy |
| P17 | "AAC is an evidence-based practice"; no claim that the app improves speech |
| P18 | Message history stays on device by default; cloud sync is opt-in |

**Target Lumen score:** ≥23/24.

## 7. AI specification & guardrails
**What AI does (all optional, off by default for new users)**
- **Phrase expansion (V12):** A small LLM (on-device where feasible, [E] 1–3B-parameter class; cloud fallback under a zero-retention contract) proposes a grammatical sentence from the selected words. The output shows **added words visibly marked**, keeps every user word, and never adds content words the user did not select, except function words and politeness markers that the user has allowed ("please" can be turned off).
- **Next-word suggestions (V15):** Ranking from the user's own history.

**Hard rules (the AAC authorship charter)**
1. **AI never speaks without user action.** No auto-speak, no timer-based speak, no "speak best guess".
2. **Show the diff.** Every added or changed word is marked. One tap reverts to the original words.
3. **The original is always one tap away** ("say my words").
4. **No content invention.** Do not add opinions, feelings, names or negations that were not selected. The eval rejects outputs that change polarity ("don't want" → "want").
5. **Log provenance:** History records "AI-suggested, user-accepted". Communication partners can see a small indicator if the user chooses (default: on for users 13+, their choice).
6. **Adults can't force it on.** For users who self-manage, only the user can enable or disable AI. For young children, the parent and SLP decide together, and a board "stop" symbol ("not what I meant") is always present.
7. **No emotion inference, no companion persona,** no conversation-partner simulation.

**Evaluation plan**
- A test corpus of 2,000 symbol sequences co-created with adult AAC users and SLPs.
- **Metrics:** meaning preservation (human-rated ≥95%), polarity errors = 0 on the test set, added-content-word rate ≤1%.
- AAC-user panel acceptability ≥4/5 on authorship.
- Latency p95 <600 ms on device [E].
- Red-teaming: manipulative expansions, sexual or violent content, swearing (the user's own swear words are allowed, never added).
- Bias review across dialects (AAVE, Spanish-English code-switching).

**Cost [E]:** On device ≈$0 marginal; cloud fallback ≈$0.0005 per suggestion.

## 8. Data, privacy & compliance
| Data | Why | Retention | Where |
|---|---|---|---|
| Vocabulary set, layout | Core | Owned by the user; exportable | Device + opt-in cloud |
| Message history | Prediction, SLP insight | On device by default; cloud only with consent; user can delete any item | Device |
| Usage aggregates (word counts) | SLP/IEP insights | 24 months [E] | Cloud, with consent |
| Voice banking (Personal Voice) | Identity | Stays in OS | Device (OS-managed) |

- **Regimes:** COPPA 2025. Message history is sensitive personal information: separate consent for cloud sync and for sharing with the SLP. Never used for training without separate opt-in, and never for under-13s.
- **HIPAA:** applies when used under an SLP practice licence (BAA).
- **FERPA / IDEA:** school accounts. AAC is assistive technology under IDEA, and IEP teams can specify it.
- **FDA:** AAC software is generally not marketed as a regulated device when sold as communication software, but dedicated SGDs are DME for funding [M]. Keep claims to communication access.
- **FTC:** no claims that the app "teaches speech" or improves outcomes without evidence.
- **Adult users:** They own their data. Guardianship-aware supported decision-making.
- **Stores:** Education category. No ads, no third-party analytics SDKs on the board surface.

## 9. Monetization & go-to-market
| Tier | Price [E] | Benchmark |
|---|---|---|
| **Voice monthly** | $9.99/mo (speech never stops on lapse) | TD Snap $9.99/mo [V]; CoughDrop $9/mo [V2]; Grid $10.99/mo [V] |
| **Voice one-time** | ≈$129 one-time + optional $29/yr cloud/team | Proloquo2Go $249.99 [V]; LAMP $299.99 [V]; CoughDrop $295 lifetime [V2] |
| **Family plan** | Included in ≈$19/mo | — |
| **Supporter accounts** | Free, unlimited | CoughDrop [V2] |
| **SLP evaluation kit** | Free 60-day trial licences for SLPs to use in evaluations | LAMP 30-day [V]; CoughDrop 2-month [V2] |
| **School** | $40–60 per communicator per year [E] | IEP AT budgets |

- **Channels:** SLP advisory panel and evaluation kits, AAC communities led by AAC users, ESA vendor lists, IEP AT procurement, UK EHCP and communication aid services [M].
- **ASO:** AAC, speech app, communication app, nonverbal, autism communication, core vocabulary, Android AAC.
- **Launch markets:** US (EN/ES), UK. India later (EN/HI) via a partner.

## 10. Success metrics
- **North star:** Weekly self-initiated utterances per active communicator.
- **Input metrics:** % of communicators with ≥1 modeling session per week; new words used per month; % of active teams (≥2 members); OBF exports (as a trust signal, not churn).
- **Guardrails:**
  - Motor-plan-change incidents without SLP confirm = 0
  - AI polarity errors in production (user-reported "not what I meant") <0.5% of accepted suggestions
  - Sensory Comfort ≥4/5
  - 0 billing complaints
  - Speech never interrupted by billing = 0 incidents
- **Outcome measures:** Communication-partner-rated functional communication (a standardized measure chosen with the SLP panel [M]); number of communicative functions used; user-reported satisfaction. **Evidence:** E3 → E2 via a pre-registered clinic pilot.
- **Retention:** AAC is daily-use. Target 6-month active ≥70% of communicators who pass week 4 [E].

## 11. Validation plan (no-code)
| # | Assumption | Experiment | Sample | Success | Kill |
|---|---|---|---|---|---|
| W2a | SLPs will trust and recommend a new system | SLP advisory review of the vocabulary structure, motor-plan spec and Figma | 10 SLPs | ≥70% would trial; ≥7/10 rate the motor-plan lock "adequate" | <40% → partner with an existing open vocabulary (e.g., licensed core set) |
| W2b | AI expansion keeps authorship | Wizard-of-Oz expansion on a Figma board; adult AAC users first, then supervised teen users | 8 adult AAC users, 6 teens | Authorship satisfaction ≥4/5; ≥60% would keep it on for some contexts | <3/5 → ship without AI; revisit in V2 |
| 3 | Families choose a subscription over one-time | Van Westendorp + choice test | 150 caregivers | Planned price within the acceptable range | — |
| 4 | Switch/gaze users can navigate the core board | Paper/Figma with an operator simulating scanning; real switch hardware | 4 switch users, 2 gaze users | Task success ≥80% | — |
| 5 | Android families are underserved | Survey | 300 caregivers | ≥30% on Android-only or mixed devices | — |

**Mapping:** WP4 (AAC phrase-expansion Wizard-of-Oz is named in the plan), WP5 (SLP interest ≥10 recommend, ≥3 practices pilot).

## 12. Build handoff
**Epic A: Board & motor-plan lock**
- *Given* a user on a 4×4 grid, *when* the grid grows to 6×6, *then* every previously visible word keeps the same relative position, verified by an automated layout diff.
- *Given* a non-SLP editor drags a word to a new slot, *when* they save, *then* the change is blocked with a motor-plan warning.

**Epic B: Speaking & authorship**
- *Given* expansion is on, *when* a suggestion appears, *then* nothing is spoken until the user selects the suggestion or Speak, and added words are visually marked and announced by VoiceOver as "added".
- *Given* the user selects "say my words", *then* the original sequence is spoken verbatim.

**Epic C: Access**
- *Given* 2-switch step scanning, *when* the user presses Move, *then* focus advances exactly one group and the auditory preview plays only on the preview audio route.
- *Given* eye gaze with 1.2 s dwell, *when* gaze rests on the rest area, *then* nothing is selected.

**Epic D: Team & OBF**
- *Given* an SLP edit, *when* the communicator's device syncs, *then* the change awaits approval per the policy and can be undone.
- *Given* any account state (including lapsed), *when* the user taps Export, *then* a valid `.obz` is produced.

**Epic E: Lapse safety.** *Given* a lapsed subscription, *then* the board, speech and export still work.

**Non-functional requirements**
- **Performance:** Speech starts ≤150 ms after Speak; the board works 100% offline.
- **Platforms:** iPadOS/iOS, Android, ChromeOS/web.
- **Accessibility:** WCAG 2.2 AA.
- **Battery:** ≤8%/hr on a mid-range tablet [E].
- **Security:** Encrypted history; adult gate.

**QA focus**
- **AT matrix:** Switch Control/Switch Access (1 and 2 switches, all scan modes), Apple Eye Tracking + 1 external gaze device [M], Head Tracking, VoiceOver/TalkBack (for blind AAC users with auditory scanning), keyguard fit tests on 3 tablet sizes, Guided Access.
- **Sensory:** Selection-feedback A/B.
- **AI:** Polarity, content-invention and dialect tests.
- **COPPA:** History consent, deletion.
- **Billing:** Lapse-still-speaks test.

**Platform dependencies:** Lumen, Circle hub (roles, approvals), on-device model runtime, TTS voice licensing, privacy stack.

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| SLP gatekeepers don't adopt a new system | High | High | SLP panel, evaluation kits, published vocabulary rationale, OBF interoperability |
| AI expansion perceived as "putting words in mouths" | Med | High | Off by default, diff view, adult AAC-user board, provenance log |
| Vocabulary development cost and quality | Med | High | License or co-develop an open core set; SLP authorship |
| Voice licensing (child voices) | Med | Med | Contract ethical, consented child-voice actors |
| Medicaid SGD funding bypasses us | Med | Med | Partner route for dedicated devices (V2) |

**Open questions:** Build our own core vocabulary or license one? Can on-device LLMs hit latency on low-end Android? Should expansion ever be available for under-8s?

## 14. Sources
- [V] Proloquo2Go price and rating: https://littlewords.ai/blog/proloquo2go-aac-device ; https://apps.apple.com/us/app/proloquo2go-aac/id308368164 ; iOS-only: https://www.assistiveware.com/products/proloquo2go
- [V] TD Snap subscription: https://mwm.ai/apps/td-snap/1072799231 ; https://search.bridgingapps.org/apps/td-snap-lite
- [V] LAMP WFL: https://search.bridgingapps.org/apps/lamp-words-for-life ; https://apps.apple.com/us/app/lamp-words-for-life/id551215116
- [V] Speak for Yourself: https://speakforyourself.org/features/ ; https://speechymusings.com/speak-for-yourself-app-review/
- [V] Grid for iPad: https://apps.apple.com/us/app/grid-for-ipad-aac/id1064332378 ; https://www.assistivetech.com.au/products/grid-for-ipad-aac-app-for-ipad
- [V] Cboard: https://play.google.com/store/apps/details?id=com.unicef.cboard&hl=en_US ; https://www.cboard.io/en/
- [V] LLM-based AAC: https://arxiv.org/pdf/2501.10582 ; authorship autoethnography: https://arxiv.org/html/2509.13671v1
- [V2] CoughDrop pricing: https://coughdrop.zendesk.com/hc/en-us/articles/115002655512 ; Avaz: https://apps.apple.com/us/app/avaz-aac/id909574843 ; TouchChat: https://littlewords.ai/blog/proloquo2go-versus-touchchat-which-is-better-for-toddlers
- [V2] Studio raw research 03/04 (AAC funding, family pain points)
- [M] Apple Live Speech/Personal Voice, Proloquo4Text, Fitzgerald key, OBF support in incumbents, dedicated-SGD DME rules: verify in WP1.

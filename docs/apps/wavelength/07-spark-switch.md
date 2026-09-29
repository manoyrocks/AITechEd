# Spark Switch: App Strategy & Product Specification

> **Venture:** Wavelength · **App #:** 7/7 · **Ages:** 2–17 (higher support needs; usable by adults) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/05-wavelength-neurodivergent.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary, or carried over from studio raw research · [M] memory · [E] estimate · [I] inference
> **Evidence tiers:** E1 FDA/RCT on product · E2 peer-reviewed product studies · E3 evidence-based method, product untested · E4 testimonials/contested
> **Research note:** The session's web-search quota ran out before this app's competitor pass, and vendor pages were blocked by the network proxy. Facts about Inclusive Technology, Sensory Guru, Sensory App House and Tobii Dynavox Look to Learn are **[M]** and must be re-verified (prices, platforms, current availability) in WP1.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Press, look, or move, and the world answers: switch- and eye-gaze-first play that grows from cause-and-effect to real choices, with light, music and vibration the adult can tune to the child. |
| **Primary user / buyer** | Users: children and young people with higher support needs: profound and multiple learning disabilities (PMLD), cerebral palsy, intellectual disability, Rett syndrome, cortical visual impairment (CVI), some autistic children with high support needs. Buyers: special schools, OTs/SLTs, AT services, families (ESA/EHCP/IEP). |
| **Core job-to-be-done** | Learner: "When I move, I want something good to happen, so I learn that I can make things happen, and choose." Teacher: "I want motivating, switch- and gaze-accessible activities that progress in small steps and let me evidence engagement." |
| **Category on the stores** | Education (iPad-first), Android tablet, Windows (for eye-gaze hardware). |
| **Top competitors** | Cosmo (Filisia), Inclusive Technology apps and SwitchIt!-style tools, Tobii Dynavox Look to Learn and TD Snap, Sensory Guru (Eyegaze Learning Curve), Sensory App House apps, Leka robot, Apple Switch Control / Eye Tracking (platform) |
| **Our wedge** | 1) **One progression, every input:** the same activities work with 1–2 switches, eye gaze, head tracking, touch-anywhere and tangible switches (Cosmo-style), on consumer tablets. 2) **Sensory control belongs to the adult who knows the child:** intensity, contrast (CVI palettes), sound and haptics per child, with photosensitivity safety built in. 3) **Engagement evidence without testing the child:** observation logging mapped to engagement frameworks (e.g., the UK Engagement Model [M]) and IEP/EHCP outcomes. |
| **Business model** | School/site licence; family plan; AT-service licence. |
| **North-star metric** | Weekly *intentional* actions per learner (observer-confirmed purposeful switch/gaze activations, including choices) across sessions. |
| **MVP candidate?** | **Later** (Year 3 per vision), but a no-code school validation (WoZ with existing switches) runs in discovery now. |

## 2. Problem & users
**Problem statement.**
- Children with higher support needs are barely served by mainstream or even special-needs apps, most of which assume touch dexterity (vision doc; [V2, raw 04]).
- Tangible multisensory switches such as **Cosmo** (light-up "Dots" + iPad app; sold as Switch (1), Explore (3) or Excel (6) packs; case-study-level evidence) show the value of **tangible, low-cognitive-load, multisensory input** [V2, raw 04] ([Inclusive](https://inclusive.com/products/cosmo-explore), [LGfL case study](https://curriculumblog.lgfl.net/cosmo-switch-case-study)).
- Eye-gaze learning software exists from Tobii Dynavox and Sensory Guru, often Windows- and hardware-bound [M]. Robots such as Leka are expensive (≈€2,490 later listing) with limited peer-reviewed evidence [V2, raw 04].
- Platforms have added strong building blocks (Apple Switch Control, Eye Tracking, Head Tracking [V2, raw 04; M]). Apps rarely design for them *first*.
- Classic switch-skills progressions (cause and effect → timing → choice making → scanning) are widely taught by AT specialists [M: e.g., Burkhart; Bean's switch progression roadmap]. Few apps implement the full progression with consistent activities across inputs.
- Many learners in this group have **epilepsy** and **CVI**, so flashing, clutter and low contrast are safety and access issues, not preferences [M].

**Personas**
| Persona | Snapshot | What Spark Switch must do |
|---|---|---|
| **Zara, 7, CP + intellectual disability** | Head switch; loves music; tires quickly. | Big musical responses to 1 switch; timing games; choice between 2 songs via 2-step scanning; short sessions with rest. |
| **Tom, 12, PMLD, CVI, epilepsy** | Responds to bright yellow on black, slow movement, vibration. | CVI palette (single bright target on black), no flashing, haptic pad or vibration, very slow pacing, long wait times. |
| **Leila, 4, autistic, high support needs** | Touches the screen anywhere; overwhelmed by noise. | Touch-anywhere cause and effect, soft sounds, a predictable "all done". |
| **Mrs. Okafor, special-school teacher** | Class of 8 PMLD pupils; 1 iPad, 2 switches, a gaze bar. | Quick per-pupil profiles, easy switch pairing, observation logging for EHCP reviews, shared devices. |

**Needs & wants**
| Need | Evidence | How Spark Switch addresses it |
|---|---|---|
| Cause-and-effect with any movement | Switch progressions [M]; Cosmo [V2] | Touch-anywhere, 1-switch, gaze-anywhere modes |
| Progress toward choice-making | AT practice [M]; vision | Levels: effect → timing → choice of 2 → scanning of 4+ |
| Safe sensory output | Epilepsy/CVI prevalence [M]; WCAG 2.3.1 | Flash-free engine; CVI palettes; caregiver intensity limits |
| Works with the school's hardware | Vision riskiest assumption | Standard switch interfaces (keyboard-key emulation), OS Switch Control, gaze via OS/partner SDKs, Cosmo-style BLE switches [I] |
| Evidence of progress without tests | Engagement frameworks [M] | Observer logging with quick tags; latency and response data |
| Turn-taking and social play | Vision | Caregiver-and-child turn games; 2 switches, 2 players |

## 3. Competitive feature benchmark
| App / product | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Evidence tier | Source |
|---|---|---|---|---|---|---|---|---|---|
| **Cosmo** | Filisia (distributed by Inclusive Technology) | School/therapy market; case studies (LGfL) [V2] | School pricing, packs of 1/3/6 switches [V2] | n/a | Light-up tangible switches + iPad app; cause-and-effect, turn-taking, motor games [V2] | Hardware cost; iPad-only [M] | Multisensory, low cognitive load [V2] | E2/E3 [V2] | [SchoolHealth](https://www.schoolhealth.com/blog/cosmo-by-filisia-interactive-and-multisensory-accessibility-switches/), [Inclusive](https://inclusive.com/products/cosmo-explore) |
| **Inclusive Technology apps** (switch-skills and cause-and-effect series; SwitchIt!-style tools) | Inclusive Technology (UK) | Long-standing UK special-school supplier [M] | Low one-time iPad apps; some subscriptions [M] | n/a | Switch-accessible progressions; UK curriculum fit [M] | Dated visuals; many separate apps [M] | Switch-first design [M] | E3 [M] | [M] |
| **Look to Learn** | Tobii Dynavox | Widely used eye-gaze starter software in schools [M] | Windows software licence [M] | n/a | Eye-gaze activities from cause-and-effect to choice [M] | Windows + gaze hardware required; cost [M] | Gaze-first [M] | E3 [M] | [M] |
| **TD Snap** | Tobii Dynavox | Major AAC brand [V2] | Free download; $9.99/mo speaking upgrade [V] | n/a | AAC with eye-gaze path [V] | Subscription to speak [V] | Eye gaze, scanning | E3 | [mwm.ai](https://mwm.ai/apps/td-snap/1072799231) |
| **Sensory Guru** (Eyegaze Learning Curve, Sensory Eye FX) | Sensory Guru (UK) | Special-school eye-gaze staple [M] | Licences; Windows [M] | n/a | Structured eye-gaze learning progression with assessment [M] | Windows/hardware-bound; cost [M] | Gaze-first; high-contrast options [M] | E3 [M] | [M] |
| **Sensory App House apps** | Sensory App House | Many low-cost iOS sensory cause-and-effect apps [M] | Low one-time [M] | n/a | Simple, bright cause-and-effect [M] | Some very bright or fast visuals [I]; separate apps | Touch-first; limited switch settings [M] | E4 [M] | [M] |
| **Leka** | Leka (France) | Niche; crowdfunded [V2] | Crowdfund $390–490; later ≈€2,490 [V2] | n/a | Spherical robot with light, sound, vibration; tablet-driven games [V2] | Price; limited evidence [V2] | Multisensory, non-threatening form [V2] | E3/E4 [V2] | [The Robot Report](https://www.therobotreport.com/leka-robot-for-special-needs-kids-launches-on-indiegogo/) (via raw 04) |
| **Apple Switch Control / Eye Tracking / Head Tracking** (platform) | Apple | Built into iOS/iPadOS [V2/M] | Free | n/a | System-wide access [M] | Setup complexity for teachers [I]; apps not designed for it [I] | Our foundation, not a competitor | n/a | [Apple Newsroom](https://www.apple.com/newsroom/2025/05/apple-unveils-powerful-accessibility-features-coming-later-this-year/) (via raw 04) |

**Feature matrix**
| Feature | Cosmo | Incl. Tech apps | Look to Learn | Sensory Guru | Sensory App House | Leka | Our decision |
|---|---|---|---|---|---|---|---|
| 1-switch cause and effect | ✓ | ✓ | ◐ | ◐ | ◐ | ✓ | **Parity** |
| 2-switch / scanning choices | ◐ | ✓ | ✗ | ✗ | ✗ | ◐ | **Parity** |
| Eye-gaze activities | ✗ | ◐ | ✓ | ✓ | ✗ | ✗ | **Parity** |
| Same activity across switch, gaze and touch | ✗ | ◐ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Consumer tablet (iPad + Android) | ◐ (iPad) | ◐ (iPad) | ✗ (Windows) | ✗ (Windows) | ◐ (iOS) | ◐ | **Differentiate** |
| Tangible light-up switches | ✓ | ◐ | ✗ | ✗ | ✗ | ✓ (robot) | **Partner** (support Cosmo-style BLE switches; no own hardware in MVP) |
| CVI palettes / contrast profiles | ◐ [M] | ◐ [M] | ◐ | ✓ [M] | ✗ | ✗ | **Improve** |
| Caregiver-set sensory intensity | ◐ | ◐ | ◐ | ◐ | ✗ | ◐ | **Improve** |
| Structured progression | ◐ | ✓ | ✓ | ✓ | ✗ | ◐ | **Parity** |
| Observation logging / engagement evidence | ◐ [M] | ◐ [M] | ◐ [M] | ✓ [M] | ✗ | ◐ | **Improve** |
| Turn-taking with a partner | ✓ | ◐ | ✗ | ✗ | ✗ | ✓ | **Parity** |
| Flashing/strobe effects | ◐ [I] | ◐ [I] | ✗ | ◐ [I] | ◐ [I] | ◐ | **Reject** (WCAG 2.3.1; epilepsy) |
| Timed "fail" states | ✗ | ◐ | ✗ | ✗ | ✗ | ✗ | **Reject** (timing games reward attempts) |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| P1 | **Universal input layer** ★ | One settings screen maps: touch-anywhere, 1–2 switches (via switch interfaces sending Space/Enter or other keys, BLE switches, OS Switch Control), eye gaze (OS Eye Tracking; partner gaze SDKs V1), head tracking (OS), keyboard, big-button, mouse | Vision; hardware compatibility risk | Differentiate | MVP | Must |
| P2 | **Cause-and-effect library** | 24 activities: music, lights, bubbles, fireworks-style *without flashing*, animals, vehicles, favourite photos/videos (caregiver-added) | Cosmo/Sensory App House parity | Parity | MVP | Must |
| P3 | **Switch progression path** ★ | Stages: (1) any press = effect; (2) press-and-hold sustains effect; (3) timing (press when the thing appears; generous windows, no failure state); (4) choice of 2 (two switches or 2-item scanning); (5) scanning 3–6 items; (6) choice-making linked to real outcomes (AAC/Day) | Switch progressions [M] | Parity+ | MVP | Must |
| P4 | **Eye-gaze progression** | Look anywhere → look at a target → look at one of 2 → dwell select from 4; dwell 0.3–3 s; visible soft dwell ring; "rest zones" | Look to Learn/Sensory Guru parity [M] | Parity | MVP | Must |
| P5 | **Per-learner sensory profile (adult-controlled)** ★ | Intensity (brightness, motion speed, volume, haptic strength), contrast profile (standard, high-contrast, CVI: single salient color on black, reduced clutter, movement to attract), preferred colors/sounds, "avoid" list | Tom persona; CVI [M] | Differentiate | MVP | Must |
| P6 | **Flash-free effects engine** | All effects generated within safe luminance-change limits; automated checks; no red flashes; no patterns | WCAG 2.3.1; epilepsy | Lumen | MVP | Must |
| P7 | **Adjustable scan & wait** | Scan speed 0.5–10 s; auditory scan cues (partner-assisted style); unlimited wait; response windows 1–20 s | AT practice | Parity | MVP | Must |
| P8 | **Choice-making games with real outcomes** | "Music or bubbles?"; caregiver-added real choices (snack photos, activities) that the adult honours | Vision; agency | Differentiate | MVP | Must |
| P9 | **Turn-taking mode** | Two players (learner + adult/peer), two switches or split screen; "my turn / your turn" cues | Cosmo parity; social play | Parity | MVP | Should |
| P10 | **Observation logger** ★ | During/after a session the adult taps quick tags (noticed, anticipated, initiated, persisted, explored, chose) plus optional note; the app records response latency and activations; export for IEP/EHCP | Engagement Model areas [M]; teacher need | Differentiate | MVP | Must |
| P11 | **Shared-device class mode** | Picture-based pupil picker; profiles switch in 1 tap; no pupil login; per-pupil hardware presets | Special-school reality | Improve | MVP | Must |
| P12 | **Session pacing & rest** | Default 5–10 min, adult-set; automatic "rest" screen after N minutes; designed "all done" song/visual | Fatigue; Lumen P9 | Lumen | MVP | Must |
| P13 | **Fine-motor touch games** (for learners who can touch) | Large-target tap, tap-and-hold, optional drag with tap alternative | Vision | Parity | V1 | Should |
| P14 | **Adaptive timing suggestions (AI-light)** | Suggests scan speed/dwell/response-window changes from response latency trends; adult approves | Vision AI role | Differentiate | V1 | Should |
| P15 | **Voice & Day bridge** | Choices made in Spark Switch can send a symbol to Voice or select a Day activity | Cross-app | Differentiate | V1 | Should |
| P16 | **Partner BLE switches / gaze SDKs** | Certified compatibility with Cosmo-style tangible switches and ≥2 gaze devices | Hardware risk | Improve | V1 | Should |
| P17 | Music creation mode | Switch-driven instrument play and simple composition | Zara loves music | Differentiate | V2 | Could |
| P18 | External devices (smart lights, adapted toys via switch-adapted relays) | Cause-and-effect beyond the screen | Real-world effect | Differentiate | V2 | Could |

★ Signature features: **Universal input layer (P1)**, **switch progression path (P3)**, **adult-controlled sensory profile with CVI palettes (P5)** and the **observation logger (P10)**. The MVP has 12 features.

## 5. Core experience & key user flows
**Core loop:** the adult picks the learner → the activity (or "continue path") starts with the learner's saved input and sensory settings → the learner acts → multisensory response → repeat with wait time → rest or all done → the adult logs observations (≤30 s).

**Flow 1: Setup (≤5 min per learner with hardware ready)**
1. The adult chooses "Add a learner" with a photo and name, and no diagnosis field.
2. Input test: "Press your switch / look at the star / touch anywhere". The app detects the input and maps it automatically.
3. Sensory profile: brightness, contrast (standard / high / CVI), sounds on or off, haptics, speed. Presets are available (e.g., "Very calm", "CVI yellow-on-black").
4. Start stage: suggested from 3 questions (e.g., "Does X already make things happen with a switch?"). The adult can override.
5. The first activity runs.

**Flow 2: Core session (Zara, 2 switches)**
1. Music activity at stage 4 (choice of 2): left switch = drums, right = piano, each with a distinct color and side.
2. Zara presses right, and piano music plays for 8 s with a slow color bloom and no flashing.
3. Wait time is 15 s. If there is no response, the app waits with a soft visual pulse (≤1 Hz) and never shows a failure.
4. After 7 minutes, "Rest time" shows a still image and silence.
5. "All done" song; the adult logs "chose (consistently right)" and "anticipated".

**Flow 3: Teacher view**
1. Class mode shows the pupils' pictures.
2. After sessions: a timeline per pupil (activations, latency trend, observation tags).
3. Export an EHCP/IEP evidence pack (PDF with tags, notes, optional photos or video only if consented).

**Flow 4: Settings:** input mappings, scan/dwell, sensory profile, session length, rest interval, who can view.

**Flow 5: Billing:** School licences via purchase order and invoice. Family plan under the Fair-billing charter. Accessibility features are never paywalled.

**Information architecture:** Learners → Activities (by stage) → Session. Adult: Profiles · Observations · Export · Hardware.

**Session design:** 5–10 min default with rest screens; the learner can end via a dedicated "stop" switch mapping if they have one. Every session ends on "All done".

## 6. Inclusive, accessible & sensory design spec
**Sensory Dial:** For this app the adult-controlled **sensory profile (P5)** replaces the generic Dial, with Calm as the baseline.
| Level | Visual | Motion | Sound | Haptic |
|---|---|---|---|---|
| **Calm (default)** | Low clutter, 1 target, soft colors | ≤0.5 Hz; slow blooms | Soft, fade-in, capped | Light |
| **Balanced** | 1–2 targets | Moderate | Music and effects | Medium |
| **Lively (adult opt-in)** | Up to 4 targets | Faster motion, still no flashing >3/s and no red flashes | Full | Strong |
| **CVI profile** | Black background, single saturated target (e.g., yellow/red per learner), no competing detail | Slow movement to attract attention | Optional | Optional |

**Switch scanning spec**
- **Modes:** auto-scan (1 switch), step-scan (2 switches: move/select), inverse scan (hold to move, release to select), timed single-press "anywhere".
- **Settings:** scan speed 0.5–10 s; loops before pausing 1–∞; first-item delay; highlight style (thick border, enlarge, color fill: choose to suit vision); auditory preview of each item on a separate route or earbud.
- **Debounce:** accept delay 0–2 s (ignore brief presses) and post-activation lockout 0–5 s (ignore repeated hits, for tremor or spasticity).

**Eye gaze spec**
- **Dwell:** 0.3–3 s with a soft ring fill; no flashing.
- **Layout:** targets ≥3 cm with ≥1.5 cm gaps at early stages; calibration-free "look anywhere" at stage 1.
- **Rest zones:** off-target regions never select.
- **Blink-select:** off by default.

**Touch:** Touch-anywhere; palm rejection; targets ≥3 cm; no multi-touch; no drag required.

**Audio:** Separate music, effects and voice channels. Every sound has a visual and/or haptic twin for Deaf and hard-of-hearing learners, and vice versa for blind learners (audio-rich mode with minimal visuals).

**Age-respectful themes:** Activities are available as "young" (animals, bubbles) and "mature" (concert, space, sports, real photos and music chosen by the teen). A 16-year-old with PMLD gets age-appropriate music and imagery by default.

**Lumen principles: acceptance criteria**
| P | Criterion |
|---|---|
| P1 | Calm baseline; no flashing ever (automated flash analysis on all effects) |
| P2 | Every effect is available as visual-only, audio-only or haptic-only |
| P3 | Same start, rest and end structure every session |
| P4 | Single action for everything; targets ≥3 cm; no drag |
| P5 | Adult UI in plain language; learner UI needs no reading |
| P6 | BDA typography in the adult UI |
| P7 | Touch, 1–2 switches, gaze, head, keyboard all verified per activity |
| P8 | No failure states; no timed penalties |
| P9 | Rest screens and "All done" |
| P10 | Pupil picker by photo; no logins |
| P11 | Wait times adjustable to unlimited |
| P12 | Profile portable (Circle), including hardware presets |
| P13 | Mature activity themes |
| P14 | ≤5-min setup; class mode; quick logging |
| P15 | No points; the effect *is* the reward |
| P16 | No "low-functioning" language; ND board plus disabled adults and families of PMLD learners review |
| P17 | "Access and play tools"; no claims of developmental improvement |
| P18 | Video/photo logging off by default; on-device storage |

**Target Lumen score:** 24/24.

## 7. AI specification & guardrails
- **What AI does (V1, minimal):**
  - **Timing suggestions:** A rule-based plus simple statistical model looks at response-latency distributions and activation patterns. It suggests changes such as "Zara responds in ~4 s; try a 6 s response window" or "consider moving to stage 4". The adult approves every change, within adult-set bounds.
  - **Activity suggestions:** Recommends next activities from the learner's preference history (effects that produced more activations).
- **What AI does not do:** No face or emotion analysis (no camera-based engagement detection, even though some engagement-assessment tools use observation video; ours relies on the human observer). No automatic stage progression without adult approval. No chat or voice persona.
- **Why so little AI:** In this population, human observation and relationship are the core. Automated "engagement scores" risk misreading atypical responses [I].
- **Evaluation:** Replay studies on pilot data. Teachers rate suggestion usefulness ≥4/5, with 0 unsafe suggestions (e.g., faster/brighter beyond profile bounds).
- **Cost:** Negligible (on device).

## 8. Data, privacy & compliance
| Data | Why | Retention | Where |
|---|---|---|---|
| Learner photo, name, profile | Picker, settings | Account life | Device + school cloud |
| Activations, latency | Progress, suggestions | 24 months [E] | Device + cloud |
| Observation tags, notes | IEP/EHCP evidence | Per school policy (DPA) | Cloud |
| Photos/video of sessions | Evidence | **Off by default**; consent required; 12 months | Device first |

- **Sensitive population:** Many learners cannot consent themselves. Parental consent is needed plus a **best-interests** review under UK AADC and GDPR [V2]. Video of disabled children is highly sensitive.
- **COPPA 2025; FERPA** (school official); **UK GDPR / DUAA 2025** (children's higher protection [V2]); **HIPAA** only for clinical AT services (BAA).
- **FDA/FTC:** no therapeutic claims.
- **Procurement:** VPAT/ACR, DPA templates (US state DPAs; UK DPIA).

## 9. Monetization & go-to-market
| Tier | Price [E] | Notes |
|---|---|---|
| **Special-school site licence** | £600–1,500 / $750–1,800 per school per year, unlimited devices [E] | Benchmark: Windows eye-gaze suites and switch hardware budgets [M] |
| **AT service / OT practice** | $300/yr per clinician | Loan-library friendly |
| **Family** | Included in Family plan; Spark-only $4.99/mo | ESA/EHCP-fundable |
| **Hardware bundles (V1)** | Partner resale of switches/interfaces | No own hardware in MVP |

- **Channels:** special schools (UK first, via local-authority networks and AT exhibitions), US special-education programs (IDEA AT), AT services and loan libraries, OT/SLT networks, disability charities (partners), hardware distributors (Inclusive-Technology-type resellers).
- **ASO:** switch accessible games, eye gaze games, cause and effect app, PMLD, sensory app switch.
- **Launch:** UK + US, with iPadOS first and Android tablet next. Windows (eye-gaze PCs) is explored in V1 via a web/PWA build [I].

## 10. Success metrics
- **North star:** Weekly intentional actions per learner (observer-confirmed).
- **Input metrics:** Sessions per learner per week (≥3); % of learners with a saved sensory profile; stage progressions approved; observations logged per session (≥1).
- **Guardrails:**
  - 0 flash-test failures
  - Sensory Comfort (observer-rated) ≥4/5
  - Setup ≤5 min
  - Teacher value ≥4/5
  - 0 billing complaints
- **Outcomes:** Observer-rated engagement across exploration, realisation, anticipation, persistence and initiation [M: Engagement Model areas]; switch/gaze skill stage; choice consistency. **Evidence:** E3 → E2 single-case designs with 2 special schools and a university partner.
- **Retention [E]:** School weekly active classes ≥70%; licence renewal ≥85%.

## 11. Validation plan
| # | Assumption | Experiment | Sample | Success | Kill |
|---|---|---|---|---|---|
| 1 | Special schools and OTs will buy (hardware compatibility, procurement) | Sessions at 2 special schools using *existing* switches and gaze bars with Figma/Keynote prototypes driven Wizard-of-Oz (a researcher triggers effects in response to real switch presses via a keyboard-emulating interface) | 2 schools, ≥12 learners, ≥6 staff | Teacher value ≥4/5; ≥80% of existing school hardware usable; ≥1 school LOI | <50% hardware usable → focus on the OS-level Switch Control path only |
| 2 | The CVI/sensory profile matters | Within-learner comparison of standard vs. personalized profiles (observer-rated attention) | 8 learners | Personalized preferred for ≥6/8 | — |
| 3 | Observation logging fits the teacher's day | Paper logging sheets for 2 weeks | 6 staff | ≤30 s per log; ≥80% sessions logged | >60 s → simplify tags |
| 4 | Families use it at home | Home diary with a loaned switch + WoZ prototype | 6 families | ≥3 sessions per week | — |
| 5 | Procurement path | Interviews with 5 school business managers/AT leads | 5 | Clear budget line identified | — |

**Mapping:** WP4 existing-tool pilots ("Spark Switch using existing school switch hardware"), WP5 channels.

## 12. Build handoff
**Epic A: Input layer**
- *Given* a switch interface sending Space, *when* the adult runs the input test, *then* the app maps it to Switch 1 within 1 press and shows a confirmation.
- *Given* a post-activation lockout of 2 s, *when* the learner presses 3 times in 1 s, *then* one activation is registered.
- *Given* OS Switch Control is on, *then* the app's in-app scanning defers to OS scanning (no double scanning), with a notice to the adult.

**Epic B: Effects engine**
- *Given* any effect, *then* luminance change never exceeds the WCAG 2.3.1 general/red flash thresholds (automated test in CI).
- *Given* a CVI profile, *then* backgrounds render pure black with one target in the chosen color and no secondary decoration.

**Epic C: Progression**
- *Given* stage 3 timing, *when* the learner presses outside the window, *then* a gentle effect still plays (no failure), and the attempt is logged as "early/late", not "wrong".
- *Given* the model suggests a stage change, *then* the change is applied only after an adult taps Approve.

**Epic D: Observation & export.** *Given* a finished session, *then* a 1-screen tag panel appears (≤6 tags), and the export PDF includes tags, dates and optional notes, with no video unless consented.

**Non-functional requirements:** Input-to-effect latency ≤100 ms [E]; fully offline; shared-device profiles; iPadOS + Android tablet; WCAG 2.2 AA for the adult UI.

**QA focus**
- **AT/hardware matrix:** Apple Switch Control (auto, step, single-switch "tap"), Android Switch Access, ≥3 common USB/BLE switch interfaces [M: e.g., keyboard-emulating interfaces], Apple Eye Tracking, ≥1 external gaze device via OS pointer [M], Head Tracking / Android Camera Switches, touch with palm rejection, VoiceOver for blind adult staff.
- **Sensory:** flash analysis on 100% of effects; CVI profile checks with a CVI specialist.
- **Data:** COPPA consent for video; school DPA flows.
- **Billing:** PO/invoice path; family cancel.

**Platform dependencies:** Lumen (effects tokens, safe-motion library), Circle (profiles, hardware presets), Voice/Day bridges, evidence engine (observation schema).

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Hardware fragmentation | High | High | Keyboard-emulation standard + OS Switch Control; compatibility list; partner program |
| Windows-dominant eye-gaze estate in schools | Med | High | Web/PWA build (V1); partnerships with gaze vendors |
| Small market; long procurement | Med | Med | Site licences, UK-first, charity partners, grant funding |
| Photosensitive seizure risk | Low (with engine) | Very high | Engine-level limits, automated tests, clinical review |
| Observation data misused as "compliance" tracking | Low | Med | Tags describe engagement, not behavior; ND board review |

**Open questions:** Build our own tangible switch in V2 or partner (Cosmo/Filisia)? How do we support Rett syndrome gaze users (a large eye-gaze AAC group)? Should Spark Switch share the codebase with the Voice scanning engine? (Recommended: yes.)

## 14. Sources
- [V2] Cosmo (via raw 04): https://www.schoolhealth.com/blog/cosmo-by-filisia-interactive-and-multisensory-accessibility-switches/ ; https://inclusive.com/products/cosmo-explore ; https://curriculumblog.lgfl.net/cosmo-switch-case-study
- [V2] Leka (via raw 04): https://www.therobotreport.com/leka-robot-for-special-needs-kids-launches-on-indiegogo/ ; https://en.leobotics.com/comparateur-robot/robot-leka-apf-france-handicap-outil-ludo-educatif-compagnon-enfant-autisme-assistance-a-la-personne
- [V] TD Snap subscription: https://mwm.ai/apps/td-snap/1072799231
- [V2] Apple accessibility features (Eye Tracking, Head Tracking) via raw 04: https://www.apple.com/newsroom/2025/05/apple-unveils-powerful-accessibility-features-coming-later-this-year/
- [V2] WCAG 2.2 and 2.3.1 (via raw 04): https://dequeuniversity.com/resources/wcag-2.2/
- [M] Inclusive Technology app range, Look to Learn, Sensory Guru Eyegaze Learning Curve, Sensory App House, UK Engagement Model areas, switch progression authors, epilepsy/CVI prevalence in PMLD: **re-verify in WP1** (search quota exhausted this session).

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (Wave 3; partner hardware) |
| **Ships in** | Wavelength app (S7) |
| **Build wave** | 3 |
| **Pre-discovery priority score** | 73/100 [I] |
| **Consumes engines** | EN-02, EN-09 |
| **Studio features used** | SX-16 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = P2, P3, P4, P6, P7, P10.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| SS-E1 | **Remote therapist mode** | During a telehealth session, an OT or teacher adjusts scan speed and dwell remotely. |
| SS-E2 | **Family music-making (V2 → V1)** | Switch-driven music the family plays together (P17 promoted). |

### 15.3 New validation question
2 special schools with existing switches (Wizard-of-Oz); teacher value ≥4/5.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 3 | 5 | 3 | 3 | 3 | 5 | 2 |

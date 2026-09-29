# Wavelength: App Strategy Index

> **v1.1 update:** every app below now has **§15 Reevaluation & enhancements** (verdict, surface, wave, trimmed MVP, new features). See the [Project Reevaluation](../../03-project-reevaluation.md) and [Studio Platform Features](../../04-studio-platform-features.md).

> **Venture:** Wavelength (neurodivergent children and teens, ≈2–17) · **Status:** Discovery & Validation (specs only, no code) · **Date:** 2026-09-29
> **Parent docs:** [Venture vision](../../vision/05-wavelength-neurodivergent.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [App template](../_TEMPLATE.md)
> **Confidence tags:** [V] verified this session · [V2] secondary / studio raw research · [M] memory · [E] estimate · [I] inference
> **Evidence tiers (raw file 04):** E1 FDA authorization and/or RCT on the product · E2 peer-reviewed product studies (non-RCT/small) · E3 built on an evidence-based method, product untested · E4 testimonials only / contested

Every Wavelength app is **neurodiversity-affirming, calm by default and multi-input**:
- The goals are the ones the learner and family choose (communication, regulation, self-advocacy, independence, learning, joy).
- We never target stimming, eye contact or "looking normal".
- All content passes a **named ND advisory board review** (autistic, ADHD and dyslexic adults and teens, plus AAC users), and the board has veto power.

---

## 1. The seven apps

| # | App | Ages | Signature feature(s) | Top competitors benchmarked | Our evidence tier at launch → target | Competitor evidence ceiling | MVP tier |
|---|---|---|---|---|---|---|---|
| 1 | [**Wavelength Day**](01-wavelength-day.md) | 2–17 | Change card for unexpected changes; AI schedule draft from one sentence; AI-drafted social narratives with a **mandatory caregiver review gate** | Choiceworks, First Then / Visual Schedule Planner, Goally, Tiimo, Brili, Otsimo, Social Story Creator, Birdhouse | E3 (visual supports and social narratives are NCAEP 2020 EBPs [V]) → E2 single-case study | E3 | **MVP (Year 1)** |
| 2 | [**Wavelength Voice**](02-wavelength-voice.md) | 2+ | Motor-plan lock (words never move); authorship-first AI phrase expansion (diff view, confirm to speak); Open Board Format no-lock-in; speech never stops on lapse | Proloquo2Go, TD Snap, LAMP WFL, Speak for Yourself, Grid for iPad, CoughDrop, Avaz, Cboard (+ TouchChat, Proloquo4Text, Apple Live Speech) | E3 (AAC is an evidence-based practice) → E2 clinic pilot | E3 (E2 for LAMP approach [M]) | **MVP (Year 1)** |
| 3 | [**Calm Harbor**](03-calm-harbor.md) | 4–17 | My Sensory Profile → one-tap personal Toolbox; flash-tested calm visuals; self-report interoception check-ins (no biometrics) | Mightier, Zones of Regulation, Breathe Think Do (Sesame), Moshi, Headspace kids, Finch, Miracle Modus | E3 → E2 OT clinic pilot | **E1/E2** (Mightier RCTs) | **MVP (Year 1)** |
| 4 | [**ReadWave**](04-readwave.md) | 5–14 | Speech-tolerant read-along with a guaranteed tap fallback; age-respectful (teen) decodables; tutor scope alignment | Nessy, Lexia Core5, Amira, Microsoft Reading Coach, Learning Ally, Speechify, Teach Your Monster, HOMER | E3 (structured literacy) → E2 reading-clinic pilot | **E1** (Lexia Core5 ESSA "Strong" [V]) | Year 2 |
| 5 | [**Focus Crew**](05-focus-crew.md) | 7–17 | Co-signed **reward-fading plan** + independence meter; caregiver co-work and a non-companion focus buddy (safe body doubling) | Joon, Tiimo, Goally, Brili, Goblin Tools, Forest, EndeavorRx, Focusmate | E3 → E2 ADHD clinic pilot | **E1** (EndeavorRx, FDA De Novo [V2]) | Year 2 |
| 6 | [**Social Compass**](06-social-compass.md) | 8–17 | Two-sided (double-empathy) scenarios; self-advocacy script builder; learner-written "My Profile" card | Social Thinking, Everyday Speech, Model Me Kids, Floreo, QTrobot, Otsimo, social-story apps, Zones | E3 (social narratives EBP) → E2 mixed methods with autistic researchers | E2 (QTrobot/Floreo pilots [V2/M]) | Year 3 |
| 7 | [**Spark Switch**](07-spark-switch.md) | 2–17 (higher support needs) | Universal input layer (switch, gaze, head, touch-anywhere); switch progression to choice-making; CVI/sensory profiles; observation logger for IEP/EHCP | Cosmo (Filisia), Inclusive Technology apps, Tobii Dynavox Look to Learn / TD Snap, Sensory Guru, Sensory App House, Leka, Apple Switch Control/Eye Tracking | E3 → E2 single-case designs in special schools | E2/E3 (Cosmo case studies [V2]) | Year 3 (no-code school pilot now) |

**Sequencing:** This follows the vision doc. Year 1: Day + Voice + Calm Harbor on the shared Circle hub. Year 2: ReadWave + Focus Crew. Year 3: Social Compass + Spark Switch. Spark Switch's **no-code** validation (Wizard-of-Oz with existing school switches) runs during this discovery phase, because hardware compatibility is its gating risk. Voice and Spark Switch should **share one scanning/dwell engine**.

---

## 2. Shared features: the Wavelength Circle hub

All seven apps sit on one account and one learner profile. Accommodations are **always free**.

| Shared feature | What it does | Apps that use it | Lumen |
|---|---|---|---|
| **My Needs profile** (learner-owned, portable) | Sensory Dial (Calm default), sound channels, haptics, motion, tint; reading level and typography; input modes (tap / voice / keyboard / AAC / 1–2 switch / eye gaze / head) with scan speed and dwell; pace (timers, wait time, transition warnings); identity-language choice; visual theme (playful / neutral / mature-photo / discreet), independent of level. The learner can see all of it, and teens can edit it. Exportable to a new school or device. | All | P1, P12, P13 |
| **Five-minute templates** | Starter packs per situation (morning routine, first AAC board, calm toolbox, homework plan, class switch session) plus caregiver-reviewed AI drafting | Day, Voice, Calm Harbor, Focus Crew, Spark Switch | P14 |
| **Multi-caregiver and professional sharing** | Roles for parent, grandparent, teacher, SLP, OT, coach, each with a view/edit scope. Change approvals (e.g., AAC vocabulary edits, reward-plan stages). Learners see who can see what, and teens approve sharing. Offline-first sync with per-item merges (the lesson from Goally's sync complaints [V]). | All | P14, P18 |
| **IEP / EHCP / 504 export** | An affirming goal bank written with the ND board and SLP/OT advisors (e.g., "will request a break using a chosen method"). Progress evidence exported as PDF/CSV: transitions rated OK, self-initiated utterances, self-advocacy actions, decoding accuracy, engagement observations. **No behavior-reduction or compliance metrics.** | All (school and clinician licences) | P14, P16 |
| **Weekly one-screen summary** | One screen per learner; notifications meant for parents never go to the child's device | All | P14 |
| **Data-control center** | Per-app data inventory in plain language; on-device-by-default toggles; separate consents for cloud sync, professional sharing, voice recordings and (never default) research/training; export everything (including AAC vocabulary as OBF); delete per item or per account; retention schedule shown | All | P18 |
| **Fair-billing charter** | Price before trial; reminder 3 days before conversion; one-tap in-app cancel; monthly and annual plans; family plan (up to 5 learners); summer pause; AAC keeps speaking on lapse; ESA/IEP invoicing | All | §3.7 |
| **Claims register** | Every marketing claim is mapped to an evidence tier; pre-registered pilots | All | P17 |
| **ND advisory board review step** | A publishing gate in the content system: no scenario, narrative template, script, AI policy or marketing copy ships without the recorded approval of ≥2 ND reviewers (plus an adult AAC user for Voice, and dyslexic reviewers for ReadWave). The board has veto power. | All | P16 |

**Pricing architecture [E]:**
- Wavelength Family plan ≈$19/mo or $149/yr, covering all apps and up to 5 learners.
- Standalone tiers: Day $5.99/mo; Voice $9.99/mo or ≈$129 one-time; Calm Harbor $4.99/mo; ReadWave $9.99/mo; Focus Crew $6.99/mo; Social Compass $5.99/mo; Spark Switch $4.99/mo (family) or a site licence (schools).
- School, clinician and AT-service licences per app doc.

---

## 3. Features we reject, and why (combined list)

| Rejected feature / pattern | Seen in (examples) | Why we reject it | Our alternative |
|---|---|---|---|
| **Compliance token economies** ("sit still = points", rewards for "expected behavior") | Common in ABA-framed and reward-chart apps [V2] | Trains compliance over agency. Criticized by autistic self-advocates [V2]. Violates Lumen P15. | Learner-chosen goals; Focus Crew's co-signed **reward-fading plan**; the effect *is* the reward (Spark Switch) |
| **Targeting stimming, "quiet hands", eye contact, "looking normal"** | Some social-skills and video-modeling content [M] | Masking is associated with harm [V2/M]. Against the vision's stance. | Stims framed as valid regulation (Calm Harbor); double-empathy scenarios (Social Compass) |
| **Emotion recognition** from face, voice or physiology to infer a child's feelings | Some social-robot and engagement-analytics tools [M] | EU AI Act Art. 5 bans emotion recognition in education [V2]. Unreliable for ND expression. Invasive. | **Self-report only** (pictorial check-ins); human observation in Spark Switch |
| **Posed-face "name the emotion" drills with one right answer** | Social-skills apps [M] | Assumes one neurotypical reading of expression | "Many ways people show feelings", with asking over guessing |
| **Puzzle-piece imagery, "cure/fix/recover" language, functioning labels** | Legacy autism branding [M] | Disliked by many autistic adults [M]. P16. | User-chosen identity language; ND-board-reviewed brand |
| **Cure, treatment or "clinically proven" claims** without product evidence | Brain Balance, historic brain-training cases [V2] | FTC §5 risk (Lumosity, LearningRx) [V2]. FDA device boundary. | Claims register; education and access claims only; pre-registered pilots |
| **Billing traps** (charged after trial cancel, annual-only, no in-app cancel) | Speech Blubs, Joon, Speechify complaints [V2] | Harms exhausted families. Regulatory risk. | Fair-billing charter; one-tap cancel; monthly option; summer pause |
| **Paywalled speech or accommodations** ("pay to speak") | TD Snap speaking upgrade model [V] | Communication is a right. P12. | Voice keeps speaking and exporting on lapse; accommodations always free |
| **AI speaking or acting without user action** (auto-speak, auto-send, auto-assign) | LLM-AAC prototypes raise authorship concerns [V] | AAC authorship; the user's voice must be the user's | Diff view + confirm-to-speak; caregiver review gate for AI narratives; adult approval for Spark Switch timing changes |
| **AI companions / "friend" personas / pets that need you** | Companion chatbots; self-care pets [V2/M] | FTC and state scrutiny of AI companions for minors [M]. Dependency risk. P18. | Labeled practice characters (no memory); a non-talking focus buddy that is clearly a tool |
| **Loss framing and streak punishment** (tree dies, pet sad, damage for missed dailies) | Forest, Habitica-style mechanics [V2/M] | Anxiety and shame, especially for ADHD. KOSA/AADC "compulsive use" direction [V2]. | Gentle weekly goals, pause days, independence meter |
| **Flashing or strobing effects; loud "wrong" buzzers; default background music** | Some sensory and "autism" apps (e.g., Miracle Modus flash risk) [V2] | Photosensitive epilepsy (WCAG 2.3.1); sensory overload | Flash-analyzed effects engine; sound off by default; visual + haptic twins |
| **Timed tasks and fluency pressure in learning loops** | Many reading and brain-training apps [M] | Processing-speed differences; anxiety. P11. | Timers only by choice; optional private fluency probes |
| **Voice-only or camera-only input** | Many AI tutors [V2] | Child and atypical speech ASR errors [V]. Excludes non-speakers. | Multimodal answer tray; tap fallback always visible |
| **ABC "behavior incident" tracking as a default** | Birdhouse-style journals [V] | Turns caregivers into compliance monitors; sensitive data | "What helped?" reflections; engagement observations; learner-visible data |
| **Mandatory proprietary locked hardware** | Goally tablet model [V] | Cost; lock-in | OS Guided Access / Screen Time guidance; runs on existing devices |
| **Vocabulary lock-in** | Proprietary AAC formats [M] | Families fear relearning; users own their words | Open Board Format import/export at any time |
| **Ads, third-party trackers or training on children's data by default** | Common in free kids' apps [V2] | COPPA 2025; AADC; trust | No ads; minimal SDKs; separate opt-in consent for any research use; never for under-13s by default |
| **Infantilizing design for older learners** | Cartoon-only special-needs apps [V2] | Stigma; P13 | Mature photo / teen / discreet themes, independent of level |

---

## 4. Cross-app accessibility and QA baseline

These are the minimum requirements for every app before Gate 2. Details are in each doc, §6 and §12.
- **Lumen audit:** ≥22/24 on the audit rubric. Calm Harbor and Spark Switch target 24/24.
- **Standards:** WCAG 2.2 AA; Apple Accessibility Nutrition Label filled in at launch.
- **AT test matrix** (in every usability round, not a separate pass):
  - VoiceOver
  - TalkBack
  - Apple Switch Control (1 and 2 switches; auto and step scan)
  - Android Switch Access
  - Apple Eye Tracking plus ≥1 external gaze device
  - Head Tracking / Camera Switches
  - Voice Control
  - Full Keyboard Access
  - Dynamic Type XXL / Android 200% font
  - Reduce Motion
  - Guided Access
- **Access rules:**
  - Dwell is adjustable 0.3–3 s with a non-flashing ring.
  - Scan speed is adjustable 0.5–10 s, with debounce and lockout.
  - No drag is ever required (WCAG 2.5.7).
  - No uncontrollable time limits (WCAG 2.2.1).
- **Photosensitivity:** Automated flash and red-flash analysis on every animated asset, run in CI.
- **Sensory A/B:** Calm vs. Lively (counterbalanced), measuring the pictorial Sensory Comfort Rating, persistence, distress signals and preference. Results are split by ND vs. non-ND participants and by age.
- **AI safety suites:** affirming-stance red-teaming (masking or compliance requests), AAC authorship (polarity and content-invention tests), companion-drift and jailbreak tests, and self-report distress pathways.

## 5. Research caveats for this document set

- **Verification limits:** Competitor facts for Day, Voice, Calm Harbor and ReadWave were verified this session (tagged [V] with URLs). The session's shared web-search quota ran out before the Focus Crew, Social Compass and Spark Switch passes, and the network proxy blocked direct fetches of app stores and several vendor sites. Those three docs therefore rely on the studio raw files ([V2]) and memory ([M]), clearly flagged for **WP1 re-verification**.
- **No sales-panel data:** Download and revenue signals are store counts or third-party estimates, not Sensor Tower/AppMagic panel data. WP1 plans to buy that data.
- **Snapshot prices:** All prices are US snapshots (Aug–Sep 2026 where dated) and vary by region.
- **No invented figures:** No quotes from self-advocates, vendors or reviewers are reproduced. Complaints are paraphrased from the cited sources.

# Inclusive & Sensory UX Framework ("Lumen")

**Studio-wide design framework for all five ventures, v1.0 (Discovery Phase)**
**Date:** 29 September 2026
**Evidence base:** [Research paper §6–§8](01-research-paper.md) and [raw file 04, Parts B–C](../research/raw/04-neurodivergent-and-inclusive-ux.md)

> **Design stance.** Accessibility and sensory comfort are **the product**, not a settings page. Every app in the studio starts calm, works with any input mode, respects system settings, and never uses shame, fear of loss or manipulation to hold attention. We design *with* disabled and neurodivergent people, and we pay them for it.

---

## 1. Why this is our moat

- **Incumbents fail here.** No top-30 learning app pairs dependable screen-reader support with dyslexia-friendly type and a true low-sensory mode. Timers, drag-only tasks, camera-only and voice-only input, and loud reward loops are standard.
- **Users punish those failures.** Common complaints are billing traps, streak "dread", pay-to-win, and "AI slop".
- **Regulators increasingly require what we'd build anyway:**
  - AAP 2026: responsibility sits with design
  - UK Children's Code: no nudge techniques
  - state design codes and KOSA: limits on compulsive-use features
  - COPPA 2025
  - EU AI Act: ban on emotion recognition in education
- **Platforms reward it.** Apple's Accessibility Nutrition Labels make accessibility searchable. Apple Design Awards for Inclusivity and Delight went to Pok Pok, Speechify, Guitar Wiz and Tiimo.
- **Neurodivergent people are a large share of every segment**, not a niche. What works for them (predictability, calm, clarity) improves the experience for everyone. This is the "curb-cut effect".

---

## 2. The 18 Lumen principles

These are condensed from the evidence in raw file 04, Part C. Each principle has a **testable acceptance criterion**, which we use to audit competitors in discovery and our own prototypes later.

| # | Principle | Do | Don't | Acceptance criterion (prototype/test) |
|---|---|---|---|---|
| P1 | **Default to calm; respect system settings** | Honor Reduce Motion, Increase Contrast and OS text size automatically. Show the Sensory Dial on the first screen | Autoplay confetti, shaking or strobing; override the system font size | With Reduce Motion on, 0 non-essential animations. The Sensory Dial is reachable in 1 tap from every screen |
| P2 | **Granular sound; never sound alone** | Separate sliders for voice, music and effects. Soft-attack sounds. Visual and haptic twin for every cue. Captions | Default background music during tasks; "wrong!" buzzers | Every audio cue has a visual equivalent. Peak loudness is capped. Captions are available for all narration |
| P3 | **Predictable structure** | "Now / Next / Done" strip. Fixed navigation and help. Transition warnings. Outcome-labeled buttons | Layout changes between levels; surprise pop-ups; mystery icons | No layout shifts within a session. 100% of buttons have text or audio labels |
| P4 | **Big, forgiving, tap-first targets** | Targets ≥2 cm for under-7s and ≥48–56 dp for seniors. Every drag can also be done as tap-then-tap. Palm rejection | Pinch, long-press, double-tap or multi-finger gestures for core actions | Every core task can be completed with single taps only (WCAG 2.5.7). Target sizes match the age profile |
| P5 | **Plain, literal language; reading-level dial** | Short sentences. Literal wording. Read-aloud with highlighting. Caregiver-set reading level | Idioms, sarcasm, walls of text, text-only instructions for pre-readers | Default copy reads at or below the profile level. Every instruction is available as audio |
| P6 | **Dyslexia-friendly typography** | Sans-serif, ≥16–19 px, 1.5 line-height, extra letter spacing, off-white background, 60–70 characters per line. User can change font, size, spacing and tint | Justified text, italics or ALL CAPS for emphasis, patterned backgrounds; claiming a special font "treats" dyslexia | Meets BDA 2023 defaults. WCAG 1.4.12 text-spacing override works |
| P7 | **Multimodal in, multimodal out (UDL)** | Answer by tap, voice, AAC symbol, drawing, switch or keyboard. Picture + word + audio | Voice as the only input (child speech recognition is unreliable); penalizing non-speaking learners | Each task accepts at least 2 input modes. Switch and eye-gaze path verified for core flows |
| P8 | **Errorless, low-penalty learning** | Informative, gentle feedback. Faded scaffolds. Undo. Auto-save. "Skip for now" | Lives, hearts, time pressure or loud failure in the learning loop; resetting progress | Zero punitive mechanics in the learning loop. Undo is always available |
| P9 | **Help focus; don't exploit attention** | One primary action per screen. Optional focus timers. Natural stopping points and session summaries | Infinite scroll, autoplay-next, loot boxes, variable-ratio rewards, "Are you sure you want to leave?" | Every session has a designed ending. Anti-dark-pattern checklist passes at 100% |
| P10 | **Don't rely on memory** | Picture passwords, parent approval, passkeys. Show prior answers. Carry information between steps | Passwords for kids; codes to copy from another screen; one-time instructions | Sign-in meets WCAG 3.3.8. No step needs information from a previous screen that is no longer shown |
| P11 | **Timing belongs to the user** | Remove or allow adjustment of all limits. Long voice wait times. Timers shown only when chosen | Auto-advancing slides; quick timeouts on voice or AAC input | No uncontrollable time limits (WCAG 2.2.1) |
| P12 | **"My Needs" profile, set once, portable** | Sensory, reading, input, pace, voice and language preferences. Caregiver-configurable and learner-visible. Exportable | Requiring a diagnosis to unlock accommodations; premium-only accommodations | All accommodations are free. The profile moves between devices and ventures |
| P13 | **Age-respectful aesthetics** | Content difficulty separate from visual theme. Mature themes at early-reader levels. Peer-aged voices | Only cartoon animals and baby voices for a 16-year-old learning to read | Each app ships at least 2 visual themes, independent of level |
| P14 | **Caregiver in the loop; low admin** | Co-play prompts. Templates ready in 5 minutes. One-screen weekly summary. Multi-caregiver sharing | An hour of setup; parent notifications on the child's device | Median time to first successful session ≤5 minutes in testing |
| P15 | **Motivation without manipulation; plan the fade** | Mastery visuals, learner-chosen goals, collections tied to learning, reward fading. Calm, optional celebrations | Compliance token economies; paid currencies; streak punishment | "Gentle streaks" only (weekly goals, pause days, no loss framing) |
| P16 | **Neurodiversity-affirming content and language** | User-chosen identity language. Diverse characters, including AAC users and characters who stim. Paid ND co-designers | "Cure / fix / normal", puzzle-piece imagery, functioning labels | Content review by the ND advisory panel before release |
| P17 | **Honest evidence claims** | State the evidence tier. Publish outcomes. Pre-register pilots. Separate education from treatment | "Clinically proven" or "treats ADHD" without an RCT or FDA authorization | Every marketing claim is mapped to an evidence tier in a claims register |
| P18 | **Privacy by default; safe AI for minors** | Data minimization. Profiling and geolocation off. No third-party ads. Separate consent for sharing. On-device voice where feasible. AI disclosure. Human oversight. Distress escalation | Emotion inference from face or voice; training on children's data without consent; AI "friends" | DPIA completed. COPPA 2025 / AADC checklist passed. No companion persona for under-18s |

---

## 3. Signature patterns (shared components across the ventures)

### 3.1 The Sensory Dial
A single control, visible on the first screen and one tap away everywhere. It sets motion, sound, color saturation, reward intensity and on-screen density together.

| Setting | Motion | Sound | Color | Rewards | Density | Default for |
|---|---|---|---|---|---|---|
| **Calm** | Essential only, slow easing | Narration only, soft | Muted, low saturation | A quiet check and a short phrase | 1 focus element | Wavelength, 1–3, anyone with OS Reduce Motion on |
| **Balanced** | Gentle transitions | Voice and soft effects | Moderate | Short, optional celebration | 1–3 elements | Lanternling 4–7, Questwise, Evergrow 60+ |
| **Lively** | Full, no flashing (WCAG 2.3.1) | Music allowed, but off by default in tasks | Vivid | Longer celebration, still skippable | Up to 5 elements | Opt-in only |

Plus **fine-tune** sliders, separate sound channels, a haptics toggle, a background tint, and a **"calm corner"** (a regulation tool with no flashing).

### 3.2 "My Needs" profile, portable across all five ventures
```
Sensory:   dial level · sound channels · haptics · motion · tint
Reading:   pre-reader (icons+audio) · early · fluent · reading-level dial · font/size/spacing
Input:     tap · voice · keyboard · AAC symbols · switch (1–2) · eye gaze · drawing
Pace:      timers off/on · wait-time for voice · session length default · transition warnings
Language:  UI language(s) · home language · identity language (identity-first/person-first)
Look:      visual theme (playful / neutral / mature photo) — independent of level
People:    who can view progress (parent, grandparent, teacher, SLP/OT) — learner-visible
```
- The learner **can see** what is set. Older learners **can change it** within age-appropriate limits.
- It is exportable, so a child's profile follows them from Lanternling to Questwise, or from Wavelength to a new school.

### 3.3 Now / Next / Done strip
- A persistent, pictorial session plan.
- Transition warnings ("2 more turns, then we stop") come with a calm visual countdown.
- Every session ends on a designed **"goodnight / all done" screen** with a real-world suggestion.

### 3.4 Gentle progress (instead of punitive streaks)
- Weekly goals, **pause days**, streak "freezes" that are free by default, and a mastery garden or map.
- There are no loss-framed notifications, and notifications meant for parents never go to the child's device.

### 3.5 Multimodal answer tray
- Every question can be answered by tap, voice, typed text, AAC symbols, a drawing or a switch scan.
- Voice recognition failures get "I didn't catch that, want to tap instead?" and never blame the learner.

### 3.6 Co-play cards (caregiver in the loop)
- One-line prompts for the adult ("Ask: what else is red in your room?").
- Each is tied to what the child just did, and each offers a screen-free follow-on activity.

### 3.7 Fair-billing charter (a UX pattern, not only a policy)
- Price shown before any trial.
- Reminder 3 days before a trial converts.
- **One-tap in-app cancellation.**
- Monthly and annual plans, plus family plans covering up to 3–5 learners.
- Accommodations are never behind the paywall.
- Pause a subscription for summer.
- Data export on request.

---

## 4. Per-segment UX parameters

| Segment | Interaction | Targets | Default session | Reading | Sensory default | Caregiver role | Watch-outs |
|---|---|---|---|---|---|---|---|
| **1–3** | Single tap; cause and effect; voice with a live adult; tangibles | ≥2.5 cm; whole-screen hit zones; no drag, pinch or double-tap | 5–10 min, adult-led; designed ending | Pre-literate: real photos, spoken words, songs | **Calm** | Essential: joint media engagement | Video deficit under ~2 years; displacing talk and play |
| **4–7** | Tap, optional drag, swipe, voice with fallback | ≥2 cm; forgiving hit areas | 10–20 min with transition warnings | Icon + audio; read-aloud with highlighting; decodable text | Calm/Balanced | Co-player; weekly summary | Child ASR errors; over-rewarding; IAP traps |
| **8–12** | Tap, drag, typing starts, voice | ≥1.5 cm / 48 dp+; keyboard | 15–30 min; optional focus timers | Moderately skilled; glossary; TTS always available | Balanced | Coach and monitor; child starts to own settings | Social comparison; pay-to-win |
| **13–19** | Full touch, keyboard, voice, chat UIs | Platform standard (44 pt / 48 dp) | User-chosen; break nudges, not hard limits | Grade 6–8 default with a dial; age-respectful | Learner-set | Autonomy with a safety net; parental controls with child notice | Surveillance fears; companion-AI risk; stigma |
| **20–34** | Mobile-first, voice, calendar | Platform + large text | Task-based | Plain-language option | System settings | Self-directed | Streak burnout; trust in AI content |
| **35–59** | Mobile + desktop, often as a caregiver | Platform; presbyopia from ~40 | Short, interruptible | Scannable summaries | System settings | Is the caregiver | Setup burden; billing trust |
| **60+** | Large-target tap, voice, linear flows, video calls | ≥48–56 dp; no precision gestures | Self-paced; no timeouts | ≥16–18 px body; icon + text labels | Balanced, high contrast | Trusted helper for setup (adult child, librarian) | Scams, dark patterns, accessible sign-in |
| **ND overlay** | All modes, chosen per task | Per motor profile | Learner/caregiver-set; visual timers | Level independent of age and theme | **Calm on first screen** | Team (learner, family, SLP/OT, teacher); learner agency first | ABA/compliance framing; over-stimulation; novelty decay; sensitive data |

---

## 5. Safe and inclusive AI guidelines

1. **Tutor, not friend.** No companion personas, romance or dependency mechanics for minors. Remind learners regularly that they are talking to AI. Escalate to a human when distress is detected, based on what the learner says, **never** on emotion inference from face or voice.
2. **Socratic by default** for tutoring (hint-first, retrieval practice, mastery gating). Answers are available only in modes a teacher or parent unlocks. This follows the evidence that unguarded AI lowers exam performance (Bastani 2025).
3. **Human-reviewed content.** Curriculum and generated stories go through human editorial review. We publish our "human-crafted + AI-assisted" policy, a direct response to the Duolingo "AI slop" backlash.
4. **Speech inclusivity.** Voice features must tolerate child speech, accents, stuttering, dysarthria and AAC-generated speech. Tap and typing are always available as alternatives. We measure word error rate by speaker group before launch.
5. **AAC authorship.** AI phrase expansion shows exactly what it added, the user confirms it, and it never speaks without user action.
6. **Transparency to learners.** Explain in child-readable language what the AI is, what it remembers, and who can see what. Teens can see what their parents or teachers see.
7. **Data.** No training on children's data without separate verifiable parental consent. On-device processing where feasible. Written retention schedule. Minimal SDKs, with vendor review (the Apitor lesson).

---

## 6. Inclusive research practice (how we validate the framework itself)

- **Paid co-design panels** in every venture: autistic, ADHD, dyslexic, blind and low-vision, Deaf and hard-of-hearing, and motor-impaired participants, plus seniors. An **ND advisory board** is named publicly (see the Wavelength vision).
- **Accessible research materials:** easy-read consent, visual schedules for sessions, breaks on request, sensory-friendly rooms or at-home sessions, and AAC-friendly interviews.
- **Children:** parental consent **and** child assent, a trusted adult present, the right to stop at any time, and short sessions matched to the age table above.
- **Assistive-technology testing:** VoiceOver, TalkBack, Switch Control, Voice Control, Dynamic Type at the largest size, and Reduce Motion, included in **every** usability round (not a separate "a11y pass").
- **Sensory measures:** a self- or caregiver-reported Sensory Comfort Rating (1–5 pictorial scale), persistence (time on task before a voluntary stop), and distress signals observed by trained facilitators.

---

## 7. Competitive Accessibility & Sensory Audit rubric (used in discovery)

Score each app 0–2 on each item (max 24):

| # | Criterion |
|---|---|
| 1 | Screen reader completes a core learning task |
| 2 | Larger text / Dynamic Type without truncation |
| 3 | Honors Reduce Motion |
| 4 | Separate sound controls; no sound-only cues |
| 5 | Core tasks possible without drag or precision gestures |
| 6 | No timers in the learning loop (or adjustable) |
| 7 | Alternative to voice-only and camera-only input |
| 8 | Dyslexia-friendly typography / spacing controls |
| 9 | Predictable layout; clear, labeled navigation |
| 10 | Low-sensory mode or calm-by-default design |
| 11 | No punitive mechanics (hearts, energy, streak loss) or pay-to-win |
| 12 | Fair billing (price before trial, in-app cancellation, reminders) |

**Target:** every studio prototype scores **≥22/24** before it leaves the validation phase. **Benchmark:** audit the unified top 30 plus the ND leaders in Discovery WP1.

# Sage Tutor: App Strategy & Product Specification

> **Venture:** Questwise · **App #:** 1/7 · **Ages:** 8–12 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/02-questwise-tweens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Questwise index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A patient, COPPA-safe Socratic homework coach for 8–12s that helps kids get unstuck by thinking, never by copying. |
| **Primary user / buyer** | User: child 8–12 (grades 3–7). Buyer: parent (B2C), ESA-funded family, microschool guide or co-op lead. |
| **Core job-to-be-done** | "When I'm stuck on homework at 8 p.m. and nobody at home can explain the 'new math', I want someone patient to help me figure out the next step myself, so I can finish and actually understand it tomorrow." |
| **Category on the stores** | Education (iOS Kids category, Ages 9–11 band) · Google Play Education, Teacher Approved / Families programme |
| **Top competitors (by downloads / revenue)** | Gauth (51M downloads 2025), Photomath (19M 2025), Brainly (100M+ Play), Question.AI (10M+), Google Lens (absorbed Socratic), Khanmigo ($4/mo), Gemini Guided Learning (under-13 via Family Link), ChatGPT Study Mode, Synthesis Tutor |
| **Our wedge** | 1) Built *for* under-13s: the snap-and-solve leaders are 13+ or not child-directed, and Khanmigo is web-first. 2) Verified-math Socratic ladder that never hands over the final answer, with a "try one like it" mastery check. 3) Screen-reader-readable math, voice/typing/drawing input and no timers, which no solver offers. |
| **Business model** | Included in the Questwise family plan (≈$12/mo or $99/yr, up to 3 kids). Free tier: 3 Sage sessions a week. ESA and microschool seat licences. |
| **North-star metric** | Weekly "unstuck-and-understood" problems per active learner (a problem solved by the child *and* followed by a correct independent "try one like it"). |
| **MVP candidate?** | **Yes**. Year-1 MVP with Math Realms (vision §9). |

## 2. Problem & users

**Problem statement.** Homework help for 8–12s is split between answer engines that teach copying and generic AI tutors that are not designed or permitted for this age.
- The fastest-growing education apps are snap-and-solve engines: Gauth, 51M downloads in 2025, #3 education app worldwide [V2 raw 01]; Photomath, 19M [V2 raw 01].
- Answer apps are linked to "higher immediate grades but … reduced knowledge retention" [V2 raw 03]. Unguarded GPT raised practice scores by 48% but cut unassisted exam scores by 17%; a guardrailed tutor largely removed the harm (Bastani et al., *PNAS* 2025) [V raw 05].
- Guardrailed tutoring works when kids use it: +0.31 SD in the World Bank Nigeria RCT, more than 2× gains in the Harvard RCT [V raw 05].
- The engagement problem is real. A two-year cluster RCT of Khanmigo in 18 Tennessee middle schools found that 96% of students tried it, but the median student messaged it in only 17% of exercise sessions where they made a mistake. Messages were "mostly bare answers or clicks on suggested prompts", and gains matched Khan Academy practice without AI [V Chalkbeat/NBER w35620]. **Access is not the constraint. Engagement is.**
- Gauth says it is not directed to children under 13 [V2 therundown.ai]. Gemini is the only major assistant that officially admits under-13s, through Family Link [V2 kidgeni/Qustodio]. Frontier study modes are 13+ [M].

**Personas**

| Persona | Snapshot | Needs | Pain today |
|---|---|---|---|
| **Jayden, 10** | Grade 5, loves Minecraft, stuck on fraction division at 8 p.m. | A fast way to get unstuck without feeling dumb | Parent can't explain the method; an older cousin's Gauth gives the answer, and the next day's quiz goes badly |
| **Priya, 11, dyslexic** | Strong reasoner, slow decoder; word problems stall her | Read-aloud, voice answers, no timers, extra wait time | Walls of text; camera-first solvers; typing long answers |
| **Sam, 12, blind (VoiceOver user)** | Grade 7, uses braille display at school | Math spoken correctly and navigable term by term | Solver output is images or unlabelled text that screen readers cannot parse [V2 raw 01/02] |
| **Nicole, 41, parent of 2** | Works full time; worries about AI cheating and stranger contact | Evidence the child did the thinking; fair price; no chat with strangers | AI that "just hands over answers"; subscription traps |
| **Mr. Ortiz, microschool guide** | 14 mixed-age students on ESA funding | Low-prep homework support he can trust; weekly mastery view | Juggling six tools; can't vet generic chatbots for under-13s |

**Needs & wants**

| Need | Evidence | How Sage Tutor addresses it |
|---|---|---|
| Help that doesn't do the work for you | Teacher and parent VoC; Bastani −17% [V raw 05] | Hint ladder; final answers are never shown; "try one like it" check |
| Accurate math | Khanmigo accepted "272 − 172 = 430" [V2 raw 03]; LLMs make more errors with larger numbers [V2 Chalkbeat] | Every step checked by a symbolic verifier before it is shown |
| Patience at any hour | ChatGPT Study Mode praised as "a tutor who doesn't get tired of my questions" [V raw 03] | Available 24/7 within parent-set hours |
| Not surveillance | "Everything you type in it, it sends it to your teacher… scary" [V2 raw 03] | Parent sees a summary, not a transcript, and the child can see exactly what the parent sees |
| Access for disabled learners | Camera-first flows exclude blind users; math output poorly read by screen readers [V2 raw 01] | Five input modes; MathML + MathCAT-style speech; no timers |
| Engagement without manipulation | Khanmigo thin engagement [V Chalkbeat] | Sage starts inside the problem (not a blank chat), offers one-tap "next nudge" chips, and celebrates reasoning |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Gauth** | ByteDance | 100M+ Play; 51M downloads 2025; #1 US Education downloads 6 days in Q3 2025 [V2] | Freemium; Plus ≈$11.99/mo or ≈$89.99/yr [E] | 4.8 (~2M Play) [V2] | Instant snap-to-answer, all subjects, live-tutor fallback | Copying; wrong answers on complex problems; billing loop (Trustpilot 2.1) [V2]; not directed to under-13s [V2] | Camera-first; text walls; no dyslexia options [E] | raw 01/02; therundown.ai |
| **Photomath** | Google | 100M+ Play; 19M downloads 2025 [V2] | Plus ≈$9.99/mo, ≈$69.99/yr [E] | ≈4.2–4.8 [V2] | Best-in-class handwriting OCR; animated steps | Steps paywalled; OCR misreads; "does homework for you" [V2] | Math output poorly read by screen readers [E] | raw 01/02 |
| **Brainly** | Brainly | 100M+ Play [V2] | Plus ≈$24–36/yr [E]; ads in free tier | 4.5 (~4.5M) [V2] | Huge Q&A archive plus AI | Ads; answer quality; used for copying [E] | Heavy ads harm readability [E] | raw 01 |
| **Question.AI** | Zuoyebang-linked | 10M+ Play [V2] | Weekly/annual subs [E] | 4.1–4.7 [V2] | Snap-and-solve, multi-model | Wrong answers; paywall; ownership opacity [V2] | Camera-first; likely minimal a11y [E] | raw 01/02 |
| **Khanmigo** | Khan Academy | 770k US students in 795 districts (2024–25) [V2 raw 05] | $4/mo learners/parents, up to 10 kids; free for teachers; districts ≈$35/student/yr [V2] | Khan app 4.1–4.7 [V2] | Socratic, won't give answers; tied to mastery content | Math errors [V2]; thin engagement in RCT (17% of mistake sessions) [V]; web-first | Khan app "fully accessible with VO" (AppleVis) [V2] | khanmigo.ai/pricing; Chalkbeat; NBER |
| **Gemini Guided Learning** | Google | Built into Gemini; under-13s via Family Link [V2] | Free | n/a | Step-by-step help, quizzes, videos rather than just an answer [V2] | General assistant; parent must enable; not curriculum-bound [V2] | Google a11y baseline [M] | kidgeni.com; Qustodio |
| **Synthesis Tutor** | Synthesis | Premium niche; strong Reddit sentiment [V2] | $45/mo or $300/yr individual; family $29/mo or $119/yr [V2] | n/a | Voice-guided, adapts to how the child thinks (ages 5–11) | Content runs out fast for strong students; price clarity [V2] | Voice-led; Lumen audit pending | synthesis.com; brighterly |
| **Google Lens (ex-Socratic)** | Google | Socratic removed from stores Oct 2024; merged into Lens [V2] | Free | n/a | Photo → explanation + videos | Answer-first; no child mode [I] | Camera-first [I] | Wikipedia (Socratic) |

**Feature matrix** (✓ yes · ✗ no · ◐ partial)

| Feature | Gauth | Photomath | Brainly | Khanmigo | Gemini GL | Synthesis | Our decision |
|---|---|---|---|---|---|---|---|
| Photo input of problem | ✓ | ✓ | ✓ | ◐ | ✓ | ✗ | **Parity** (one of 5 input modes, never the only one) |
| Voice input | ◐ | ✗ | ✗ | ◐ | ✓ | ✓ | **Improve** (child-speech tolerant, tap fallback) |
| Final answer shown | ✓ | ✓ | ✓ | ✗ | ◐ | ✗ | **Reject**: violates "think, don't copy" |
| Graduated hints | ◐ | ◐ (steps) | ✗ | ✓ | ✓ | ✓ | **Improve** (5-rung ladder + worked parallel example) |
| Verified math per step | ◐ | ✓ (solver) | ✗ | ✗ | ✗ | ✓ (scripted) | **Differentiate** (symbolic verifier gate on every step) |
| "Try one like it" mastery check | ✗ | ✗ | ✗ | ◐ | ✓ (quizzes) | ✓ | **Differentiate** |
| Screen-reader math (MathML/speech) | ✗ | ✗ | ✗ | ◐ | ◐ | ✗ | **Differentiate** |
| Parent summary (not transcript) | ✗ | ✗ | ✗ | ◐ (parent sees chats) | ◐ | ◐ | **Differentiate** |
| Live human tutor upsell | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | **Reject for MVP**: cost, and stranger contact with children |
| Ads | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | **Reject**: Kids category, P18 |
| Companion persona / chit-chat | ✗ | ✗ | ✗ | ◐ (characters) | ◐ | ✗ | **Reject**: FTC 6(b), P18; Sage is a tool, not a friend |
| Timers / speed | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Parity (none)** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| ST-01 | **Multimodal problem capture** | Snap a photo, type, speak or draw the problem. OCR shown back as editable text and as spoken math before help begins | Camera-only excludes blind users [V2 raw 01]; P7 | Parity/Lumen | MVP | Must |
| ST-02 | ⭐ **Socratic Hint Ladder** | 5 rungs: (1) "What do you notice?" (2) Point to the relevant idea (3) Break into a sub-step (4) Worked *parallel* example with different numbers (5) Fill-the-gap step. Never the final answer | Bastani guardrails [V raw 05]; Khanmigo policy | Differentiate | MVP | Must |
| ST-03 | ⭐ **Verified Math Gate** | Every number, step and check passes a symbolic engine (CAS) before display. Disagreement → Sage says "Let me double-check" and falls back to a scripted hint | Khanmigo "272 − 172 = 430" [V2]; LLM math errors [V2] | Differentiate | MVP | Must |
| ST-04 | **Show-your-thinking canvas** | Child writes working by stylus, finger, keyboard or voice; Sage comments on the child's step, not on a hidden solution | Engagement was thin when kids only pasted answers [V Chalkbeat] | Improve | MVP | Must |
| ST-05 | ⭐ **"Try one like it" check** | After finishing, one isomorphic problem solved with no hints; counts toward the north-star | Mastery evidence; Synthesis/Gemini quiz parity | Differentiate | MVP | Must |
| ST-06 | **Nudge chips** | One-tap prompts ("I don't know where to start", "Check my step", "Explain the word") so kids don't face a blank chat | Khanmigo messages were "bare answers or clicks on suggested prompts" [V]: we design for that behaviour | Improve | MVP | Must |
| ST-07 | **Accessible math output** | All math rendered as MathML with speech and braille (MathCAT-class engine), explorable term by term; large-print zoom | MathCAT offers speech, braille and navigation [V daisy.github.io]; no solver does this | Differentiate/Lumen | MVP | Must |
| ST-08 | **Read-aloud + dyslexia layer** | TTS with word highlighting, BDA typography, tint, reading-level dial for Sage's language (default grade 3–4) | P5/P6; Priya persona | Lumen | MVP | Must |
| ST-09 | **Parent session summary** | Plain-language card: topic, hints used, "try one like it" result, one co-play question. No transcript by default | Surveillance fear [V2]; P14 | Differentiate | MVP | Must |
| ST-10 | **Topic & safety guard** | Homework-only scope (math first, then reading/science); off-topic gently redirected; distress phrases trigger the escalation flow (§7) | FTC 6(b); P18 | Lumen | MVP | Must |
| ST-11 | **Curriculum alignment tags** | Problem classified to CCSS/TEKS standard; matched to Math Realms skill node | Parents want proof of learning [V raw 03] | Improve | MVP | Should |
| ST-12 | **Sensory Dial + calm ending** | Calm/Balanced/Lively; session closes with "what I figured out" card and a stop suggestion | P1, P9 | Lumen | MVP | Must |
| ST-13 | Word-problem unpacker | Sage reads a word problem aloud, then helps the child highlight "what we know / what we need" | Priya persona; Lumen P5 | Improve | V1 | Should |
| ST-14 | Reading and science homework | Extend the ladder to comprehension ("find the evidence") and science explanations | Gauth multi-subject parity | Parity | V1 | Should |
| ST-15 | Teacher/guide unlocks | Educator can set per-assignment policy (e.g., "hints to rung 3 only", "worked example allowed") | Lumen §5.2 (answers only in modes adults unlock) | Improve | V1 | Should |
| ST-16 | Home-language help | Explanations in Spanish first, child can toggle mid-session | ESA states (TX, FL, AZ) demographics [I] | Improve | V1 | Should |
| ST-17 | Mistake museum | Child's own past mistakes turned into short retrieval puzzles | Retrieval practice evidence [M] | Differentiate | V2 | Could |
| ST-18 | Co-op "study table" | Two invited friends work the same problem type in parallel, no free chat, emoji-only reactions | Vision principle 3 | Differentiate | V2 | Could |
| ST-19 | AAC and switch answering | Answer tray with symbol sets and 1–2 switch scanning | P7; Wavelength shared component | Lumen | V1 | Should |
| — | Final-answer mode, live stranger tutors, ads, companion persona, coins for help | — | See Reject list | Reject | — | Won't |

**MVP = ST-01 to ST-12 (12 features).** Core loop covered end to end: capture → think → hint → verify → try one like it → summary. **Signature features:** ST-02 Socratic Hint Ladder, ST-03 Verified Math Gate, ST-05 "Try one like it".

## 5. Core experience & key user flows

**Core loop:** open → capture problem → "what do you notice?" → child's step → Sage checks → (hint rung if needed) → child finishes → try one like it → "what I figured out" card → natural end.

**Flow 1: Onboarding (≤5 min to first value)**
1. Parent downloads and passes a parental gate. Creates a family account with verifiable parental consent (VPC) by card check, ID or knowledge-based method (§8).
2. Parent picks grade, state standards and hours Sage is available (default 3–9 p.m.). AI-training consent shown separately and **off**.
3. Child picks a picture passcode, theme (playful or neutral) and a Sensory Dial level. The My Needs profile imports from Lanternling if one exists.
4. Sage explains itself in 3 plain lines, read aloud: "I'm a computer helper, not a person. I help you think. I won't give you the answer."
5. Child tries a warm-up problem with the ladder. First "aha" in under 5 minutes.

**Flow 2: Core session**
1. Child taps "I'm stuck" and captures the problem (photo, type, voice or draw). Sage shows its reading of the problem in text + speech: "Is this right?"
2. Sage asks the rung-1 question. The child answers on the canvas or by voice.
3. Each child step is checked by the verifier. Right → specific praise for the reasoning ("You found the common denominator first. Smart move."). Wrong → rung up, with no "wrong!" sound.
4. The child reaches the answer. Sage does **not** confirm by revealing it; it asks the child to check (e.g., substitute back). Verifier confirms.
5. "Try one like it" (no hints). Result stored as mastery evidence.
6. "What I figured out" card and a transition: "That's one done. Take a stretch, or do the next one?"

**Flow 3: Parent view**
1. Parent opens the Guild Hub (separate adult app or web). No notifications on the child's device.
2. Weekly card: problems unstuck, skills, hints needed, independent "try one like it" rate, one co-play question.
3. Parent can open a session summary. The transcript is available only if the parent enables "full transcript" in settings, which the child is told about in the app.

**Flow 4: My Needs / settings**
1. The child reaches the Sensory Dial in one tap from every screen.
2. My Needs covers input modes, TTS speed, wait time for voice, font/spacing/tint, math verbosity (e.g., "three fourths" vs. "3 over 4"), and a braille display toggle.
3. Parent-locked settings: availability hours, subjects, hint ceiling.

**Flow 5: Billing and cancellation**
1. Price shown before trial. Trial reminder 3 days before conversion (email to parent).
2. One-tap in-app cancel, with no retention maze. Pause for summer. ESA purchase via marketplace invoice (§9).

**Information architecture:** Child app has 4 screens: Home ("I'm stuck" + recent), Session, My Stuff (figured-out cards), My Needs. Fixed bottom nav with text labels. Adult Guild Hub: Summaries, Settings, Billing, Privacy.

**Session design:** One problem = one mini-session (≈5–12 min). Default cap of 30 minutes a day, parent-adjustable. After 3 problems, a gentle break card. Every session ends on the "what I figured out" screen. No autoplay into another problem.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial defaults:** **Balanced** (Questwise default); **Calm** if OS Reduce Motion is on.

| Level | Sage Tutor behaviour |
|---|---|
| Calm | Static UI; narration only; a quiet check mark for correct steps; one element on screen (the current step) |
| Balanced | Gentle step transitions; soft chime (volume-capped) for a completed problem; "Now / Next / Done" strip visible |
| Lively | Short optional sparkle animation on the figured-out card (no flashing, WCAG 2.3.1); themed backgrounds |

**Input modes per task**

| Task | Tap | Voice | Keyboard | Drawing/stylus | AAC/switch | Camera |
|---|---|---|---|---|---|---|
| Capture problem | ✓ (math keypad) | ✓ | ✓ | ✓ | V1 | ✓ |
| Answer a hint question | ✓ (chips) | ✓ | ✓ | ✓ | V1 | — |
| Show working | ✓ (step builder) | ✓ (dictated steps) | ✓ (linear math input, e.g., `3/4`) | ✓ | V1 | ✓ (photo of paper working) |

**Targets and gestures:** ≥48 dp targets (≥1.5 cm); math keypad keys ≥56 dp. No drag in core flow; the step builder uses tap-to-place. No pinch, long-press or multi-finger gestures (WCAG 2.5.7).

**Reading and typography:** Sage's prompts default to grade 3–4 reading level, capped at 2 sentences per turn. Always-on read-aloud button with word highlighting. BDA defaults: sans-serif ≥18 px, 1.5 line spacing, off-white background, left-aligned, no italics. User can change font, size, spacing and tint (WCAG 1.4.12). Glossary tap on any math word.

**Screen-reader math output (spec):**
- All math is stored as Content-annotated MathML (with `intent` attributes where ambiguous), never as images.
- Speech via a MathCAT-class engine in "ClearSpeak"-style verbosity for grades 3–7; navigation by term, sub-expression and fraction parts.
- VoiceOver/TalkBack custom rotor: "Steps", "Current hint", "My answer".
- Braille output (Nemeth and UEB Technical) to connected displays [V MathCAT].
- OCR results are always confirmed aloud before help begins, so a misread cannot silently derail a blind student.

**Audio:** Separate sliders for voice, effects, music (music off in tasks). No sound-only cues. Captions for all Sage speech. Haptic tick for a verified step (optional).

**Timing:** No timers anywhere. Voice wait time default 8 s, adjustable to "until I tap done". Sage never auto-advances.

**Age-respectful themes:** "Explorer" (illustrated) and "Studio" (clean, neutral, suits 11–12s and older strugglers), independent of grade level.

**Lumen principles and acceptance criteria**

| P | App-specific acceptance criterion |
|---|---|
| P1 | With Reduce Motion on, 0 non-essential animations; Dial reachable in 1 tap |
| P2 | Every chime has a visual twin; peak loudness capped; Sage speech captioned |
| P3 | Session screen layout identical for every problem; Now/Next/Done strip |
| P4 | Full session completable with single taps; targets ≥48 dp |
| P5 | 95% of Sage turns score ≤ grade 4 on a readability check; every turn has audio |
| P6 | BDA defaults on; text-spacing override passes |
| P7 | Every task accepts ≥3 input modes; switch path verified by V1 |
| P8 | No "wrong" buzzers; errors trigger a rung, not a penalty; undo on canvas |
| P9 | Designed ending on every session; no autoplay to next problem |
| P10 | Picture passcode; OCR text stays visible throughout the session |
| P11 | Zero time limits; configurable voice wait |
| P12 | All accommodations free; My Needs imported/exported |
| P13 | 2 themes independent of level |
| P14 | Parent setup ≤5 min; weekly one-screen summary |
| P15 | No streaks; celebration of reasoning, not speed |
| P16 | ND advisory review of Sage's feedback language |
| P17 | Marketing claims mapped to evidence tier (none above "designed from research" at launch) |
| P18 | No companion persona; AI disclosure every session; DPIA done |

**Target Lumen audit score:** 23/24 at prototype (expected shortfall: item 7 until AAC answering ships in V1).

## 7. AI specification & guardrails

**What AI does:**
- Vision/OCR for printed and handwritten math (on-device first pass, cloud fallback).
- LLM (policy-constrained) generates Socratic questions and hint text *from a structured solution plan* produced by the CAS, not from free reasoning.
- CAS/symbolic verifier checks every number and step; problem generator creates isomorphic "try one like it" items.
- ASR tuned for child speech (on-device where feasible); TTS with math speech rules.
- Classifier for topic scope and distress phrases (text-based, not voice tone).

**What AI does not do:** give the final answer; write essays; chat socially; remember personal details outside learning data; infer emotion from voice or face; roleplay as a person or friend.

**Pedagogical policy**
- **Hint ladder** (5 rungs, §4). Rungs advance only on child request or after two unproductive attempts. Rung 4 always uses *different numbers*.
- **No-answer rule:** output filter blocks any string equal to the verified final answer (and trivial transforms) unless the child produced it first.
- **Mastery gating:** a problem counts as "understood" only after an independent "try one like it".
- **Escape valve:** "Show me a similar example" (rung 4) is always available so kids don't quit (vision §8 mitigation).
- **Educator unlocks** (V1): worked-solution mode only for adult-enabled contexts (Lumen §5.2).

**Safety**
- **No companion persona.** Sage is a named tool with a simple glyph, not a character with feelings. It never says "I missed you" or asks personal questions.
- **Disclosure:** "I'm a computer helper" at every session start; tap-able "What is Sage?" explainer.
- **Distress escalation (self-report only):** If the child types or says phrases indicating self-harm, abuse or danger, Sage stops tutoring, shows a calm script ("That sounds really hard. You deserve help from a grown-up you trust."), displays a one-tap "tell my grown-up" button and region-appropriate helpline (988 in the US), and sends a parent alert to the Guild Hub (not the content verbatim, a category + time). Human safety reviewer queue within 24 h. **No emotion recognition**, no sentiment scoring of voice.
- **Content filters:** input and output moderation tuned for under-13s; images of problems are processed transiently and not stored beyond 30 days unless the parent saves them.
- **Hallucination controls:** CAS gate; retrieval from curated explanation bank; refusal when the verifier can't parse ("I'm not sure I read that right. Can you type it?").

**Evaluation plan**
- Offline: 5,000-item gold set of grade 3–7 problems (CCSS + TEKS), measuring answer leakage rate (target 0%), step-verification accuracy (≥99.5%), and hint quality (rubric by teachers, ≥4/5).
- Red-teaming: 500 adversarial prompts written by kids in paid, consented sessions and by staff ("just tell me", "my teacher said you can", jailbreak role-play), target leakage ≤0.5% before beta, 0 in the regression suite after fixes.
- ASR word error rate by speaker group (age 8–9 vs 10–12, accent groups, stutter, dysarthria, AAC-synthesised speech); ship voice only where WER gap ≤5 pts versus the best group, with tap fallback always.
- Human review sampling: 2% of sessions (de-identified, consented) reviewed weekly by credentialed teachers.

**Cost and latency [E]:** ≈15 LLM turns per problem at small-model rates plus CAS ≈ $0.004–0.01 per problem; a heavy user (40 problems/month) ≈ $0.40/month. Target p95 latency ≤2.0 s per Sage turn; OCR ≤1.5 s.

## 8. Data, privacy & compliance

| Data | Why | Retention | Processing |
|---|---|---|---|
| Parent account (name, email, payment token) | Billing, VPC | Life of account + 30 days | Cloud (US) |
| Child profile (first name or nickname, grade, My Needs) | Personalisation | Life of account; deleted on request | Cloud; exportable |
| Problem images | Capture | 30 days default; parent can save | On-device OCR first; cloud fallback |
| Voice audio | Input | Not stored; transcripts only | On-device ASR where feasible; cloud audio deleted after transcription |
| Session logs (steps, hints, results) | Learning model, summaries | 12 months rolling | Cloud |
| Safety events | Escalation | 24 months | Cloud, restricted access |

**Regimes:** COPPA (2025 amendments, full compliance since 22 Apr 2026): all users under 13; VPC; separate consent for any third-party disclosure and for AI training (default **off**); written retention and security programme; voice treated as personal information [V raw 05]. FERPA/SOPIPA and state student-privacy laws for school/microschool contracts (DPA templates). UK AADC and state design codes (high-privacy defaults, no nudges). EU AI Act: no emotion recognition; Art. 50 AI disclosure; placement or assessment functions reviewed for Annex III by Dec 2027. FTC §5 for claims. No FDA boundary (education only).

**Consent flows:** VPC at account creation; separate toggles for AI-training use of de-identified data, for research participation and for full-transcript visibility; child assent screen in plain language with read-aloud.

**Store requirements:** Apple Kids category (no third-party ads or analytics, parental gate before links/purchases); Google Families policy (certified SDKs only, no advertising ID). Accessibility Nutrition Label completed at launch.

## 9. Monetization & go-to-market

**Pricing (benchmarks: Gauth ≈$90/yr, Photomath ≈$70/yr, Khanmigo $48/yr, Synthesis $119–300/yr):**
- **Free:** 3 Sage problems/week, all accessibility features.
- **Questwise Family:** ≈$12/mo or $99/yr, up to 3 kids, all 7 apps (vision §6).
- **Sage-only** (V1 test): $5/mo, to compete head-on with Khanmigo's $4.
- **Microschool/co-op:** $100–300 per student/yr bundle; Sage included.
- **Fair-billing charter:** price before trial, 3-day reminder, one-tap cancel, pause for summer, accommodations never paywalled.

**Channels:** (1) ESA marketplaces (AZ, FL, TN, TX 2026–27, IA) through ClassWallet/Odyssey vendor approval; (2) homeschool co-ops and microschool networks; (3) B2C App Store / Play; (4) free teacher tier on Chromebook web later.

**ASO:** Keywords "homework help for kids", "math tutor for kids", "safe AI tutor", "no answers homework helper", "dyslexia math help". Category: Education, Kids 9–11. Accessibility Nutrition Label with VoiceOver, Voice Control, Larger Text, Sufficient Contrast, Reduced Motion, Captions claimed only when verified.

**Launch markets:** US (English + Spanish V1). UK/Australia after AADC review in V2.

## 10. Success metrics

- **North-star:** weekly unstuck-and-understood problems per active learner (target ≥4 at month 3).
- **Inputs:** sessions started per week; % sessions reaching "try one like it" (≥60%); independent success rate on try-one-like-it (≥70%); hint rungs used per problem (median ≤2); parent summary open rate (≥50%).
- **Guardrails:** answer leakage 0 in audits; frustration events (child quits within 2 turns after a hint) ≤10% of sessions; Sensory Comfort ≥4/5; parent trust score ≥8/10; zero billing complaints; distress escalations reviewed within 24 h (100%).
- **Learning outcomes and evidence tiers:** Tier 4 logic model at launch → pre-registered quasi-experimental study with 3 microschools in year 1 (Tier 3) → RCT with a university partner in year 3 (Tier 2).
- **Retention:** D1 45%, D7 25%, D30 15% (homework is weekly and seasonal); DAU/MAU 20–25% during the school year [E]. Benchmark: Duolingo DAU/MAU 41.7% as a ceiling, not a target [V raw 05].

## 11. Validation plan (no-code, discovery phase)

**Riskiest assumptions (ranked)**
1. Kids 8–12 keep engaging when Sage won't give the answer (the Khanmigo engagement gap).
2. Parents prefer summaries to transcripts and trust them.
3. A verified-math pipeline can keep leakage and errors near zero at acceptable latency.
4. Blind and dyslexic learners can complete a session end to end.
5. Parents or ESAs will pay ≈$99/yr when Gemini Guided Learning is free.

**Experiments**

| # | Method | Sample | Success threshold | Kill / pivot threshold |
|---|---|---|---|---|
| E1 | **Wizard-of-Oz tutor** (trained human follows Sage policy in a Figma chat shell) for 2 weeks | 20 families, ≥6 ND/disabled kids | ≥70% of sessions completed through try-one-like-it and child rating ≥4/5 (Discovery Plan Q1); ≥60% of kids use Sage ≥3 times in week 2; frustration ≤15% | <40% reach try-one-like-it or week-2 use <30% → redesign ladder or add worked-example-first mode |
| E2 | Parent summary vs. transcript preference test (card sort + interview) | 30 parents | ≥65% prefer summary and rate trust ≥7/10 | <40% → transcript-by-default option |
| E3 | Accessibility task test on Figma + screen-reader-readable HTML math prototype | 6 blind/low-vision, 8 dyslexic, 6 ADHD kids | ≥85% task completion; Sensory Comfort ≥4/5 | <70% → rework math speech |
| E4 | Offline verifier spike (paper spec + existing CAS/LLM tools, no product code) on 500 problems | — | ≥99% step verification; 0 answer leakage with filter | <97% → narrow MVP to arithmetic/fractions |
| E5 | Smoke test: landing page with $99/yr family plan and "Sage-only $5/mo" | 2,000 targeted parent visits | ≥6% waitlist; ≥30% of those choose annual | <2% → reposition as ESA/microschool-first |

**Mapping to Discovery Plan:** E1 = assumption Q1 (§8.2); E1, E3 → WP4; E2 → WP2/WP4; E4 → WP1 (evidence verification) and WP4; E5 → WP5.

## 12. Build handoff (for the agent team, post-Gate 2)

**Epic A: Problem capture**
- *Story:* As a child, I can enter a problem by photo, typing, voice or drawing.
- **AC-A1:** Given a photo of a printed fraction problem, When OCR completes, Then the parsed problem is shown as text and spoken math, and the child must confirm or edit before any hint appears.
- **AC-A2:** Given VoiceOver is on, When the child uses the math keypad, Then every key has a spoken label and entered math is announced via the math speech engine.

**Epic B: Hint ladder and no-answer policy**
- **AC-B1:** Given a verified solution exists, When any Sage output is generated, Then it contains no token sequence equal to the final answer unless the child has already entered it.
- **AC-B2:** Given the child taps "I'm still stuck" twice, When the ladder advances, Then rung 4 shows a worked example with different numbers.
- **AC-B3:** Given the child types "just tell me the answer", When Sage responds, Then it declines kindly and offers the next rung.

**Epic C: Verified math gate**
- **AC-C1:** Given the LLM proposes a hint containing a number, When the CAS disagrees, Then the hint is suppressed and a scripted fallback is shown within 2 s.

**Epic D: Try one like it and mastery evidence**
- **AC-D1:** Given a problem is completed, When "try one like it" is generated, Then it matches the same skill node and difficulty band and offers no hints.

**Epic E: Parent summary**
- **AC-E1:** Given a session ended, When the parent opens the Guild Hub, Then they see topic, hints used and try-one-like-it result, and no transcript unless transcript mode is enabled.
- **AC-E2:** Given transcript mode is enabled, When the child opens Sage, Then a child-readable notice states that a grown-up can read their chats.

**Epic F: Safety escalation**
- **AC-F1:** Given the child writes a self-harm phrase, When the classifier flags it, Then tutoring pauses, the calm script and helpline appear, a parent alert is queued, and a human-review ticket is created.

**Epic G: My Needs and Sensory Dial**
- **AC-G1:** Given OS Reduce Motion is on, When the app launches, Then the Dial defaults to Calm and no non-essential animation plays.

**Non-functional requirements:** p95 Sage turn ≤2 s; offline mode shows cached "try one like it" practice and queues problems; iOS, Android, web (Chromebook); WCAG 2.2 AA; English + Spanish strings externalised; encryption in transit/at rest, SOC 2 roadmap, no third-party SDKs that transmit identifiers.

**QA focus**
- *AT matrix:* VoiceOver + braille display (iPad), TalkBack (Android), ChromeVox + NVDA (web), Switch Control, Voice Control, Dynamic Type XXXL, Reduce Motion, Increase Contrast.
- *Sensory A/B:* Calm vs. Balanced on persistence and comfort.
- *AI safety cases:* answer-leak suite (2,000 prompts), jailbreaks, off-topic, distress phrases (EN/ES), OCR misread handling.
- *COPPA cases:* no data before VPC; AI-training toggle off by default; deletion within 30 days of request; no third-party identifiers in network traces.
- *Billing cases:* price shown pre-trial, reminder sent, one-tap cancel, ESA invoice matches marketplace record.

**Platform dependencies:** Lumen design system, My Needs profile, AI orchestration (policy engine, CAS service, moderation), privacy stack (VPC, consent ledger, retention jobs), evidence engine (mastery events, study export).

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Kids find Socratic friction annoying and quit (Khanmigo pattern) | High | High | Start inside the problem, nudge chips, worked parallel example escape; E1 thresholds |
| Free Gemini Guided Learning for under-13s erodes willingness to pay | Medium | High | Win on verified math, accessibility, curriculum/Math Realms link and ESA reimbursement |
| OCR misreads handwriting and misleads | Medium | Medium | Confirm-before-help step; edit option |
| Verifier coverage gaps (word problems, geometry diagrams) | Medium | Medium | MVP scope: arithmetic → fractions → ratios → pre-algebra; explicit "I can't check this yet" |
| Distress false negatives | Low | Very high | Conservative classifier, human review, parent-configurable trusted adult |
| Teachers view any AI homework help as cheating | Medium | Medium | Educator unlocks, transparency cards, "try one like it" evidence |

**Open questions:** Should Sage ever confirm a correct final answer explicitly, or only through the child's own check? What is the right hint ceiling default for grades 3–4 vs. 6–7? Can on-device ASR reach the WER target for 8-year-olds? Which ESA states accept AI tutoring as an eligible expense?

## 14. Sources
- [V] Chalkbeat, Khanmigo two-year Tennessee study (Aug 2026): https://www.chalkbeat.org/2026/08/25/ai-tutoring-students-khanmigo-khan-academy-engagement-study/
- [V] NBER w35620, "One Click Away: AI Tutoring with Khanmigo": https://www.nber.org/papers/w35620
- [V] Khanmigo pricing: https://www.khanmigo.ai/pricing
- [V2] Khanmigo district pricing and review: https://www.myengineeringbuddy.com/blog/khanmigo-reviews-alternatives-pricing-offerings/
- [V2] Gauth review (not directed to under-13s): https://www.therundown.ai/tools/gauth
- [V2] Socratic by Google history: https://en.wikipedia.org/wiki/Socratic_(Google)
- [V2] Gemini for under-13s via Family Link: https://kidgeni.com/learn/is-gemini-safe-for-kids · https://www.qustodio.com/en/blog/is-google-gemini-safe/
- [V2] Synthesis Tutor pricing and reviews: https://www.synthesis.com/tutor · https://brighterly.com/blog/synthesis-tutor-cost/
- [V] MathCAT: https://daisy.github.io/MathCAT/
- [V2] Harvard accessible math guide (Aug 2026): https://accessibility.huit.harvard.edu/news/2026/08/practical-guide-accessible-math
- [V2 via raw 01/02] Gauth, Photomath, Brainly, Question.AI store signals: research/raw/01-google-play-top30.md, research/raw/02-apple-app-store-top30.md
- [V via raw 05] Bastani et al. PNAS 2025: https://www.pnas.org/doi/10.1073/pnas.2422633122 · World Bank Nigeria: https://voxdev.org/topic/education/how-ai-tutors-improved-learning-nigeria · Harvard RCT: https://www.nature.com/articles/s41598-025-97652-6
- [V via raw 05] COPPA 2025 final rule: https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule
- [V2 via raw 03] Khanmigo "272 − 172 = 430" and surveillance quote: research/raw/03-forum-voice-of-customer.md
- [M] Frontier study-mode age minimums (13+); CCSS/TEKS alignment approach

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Re-scope → Embedded Tutor (EN-03) in every Questwise experience + a homework mode |
| **Ships in** | Questwise app (S2) |
| **Build wave** | 1c |
| **Pre-discovery priority score** | 85/100 [I] |
| **Consumes engines** | EN-03, EN-09, EN-12 |
| **Studio features used** | SX-08, SX-09, SX-17 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = ST-02, ST-03, ST-04, ST-05, ST-07, ST-10.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| ST-E1 | **At-error invitations** | After two misses in any Questwise experience, Sage offers help in context. The target is ≥40% uptake, against the 17% Khanmigo baseline [V2]. |
| ST-E2 | **Guide & parent CoPilot** | Suggests how the adult can help without giving the answer (the Tutor CoPilot pattern). |
| ST-E3 | **Worksheet-aware capture** | Recognizes the method on the class worksheet so hints match what the teacher taught. |

### 15.3 New validation question
Wizard-of-Oz A/B: embedded at-error invitation vs. a separate tutor entry point. Measure uptake and completion, n=20 families.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 5 | 4 | 4 | 5 | 4 | 3 | 4 | 5 |

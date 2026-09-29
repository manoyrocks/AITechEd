# Study Coach: App Strategy & Product Specification

> **Venture:** Ascendly · **App #:** 1/7 · **Ages:** 13–19 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/03-ascendly-teens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research note:** WebFetch was blocked by the egress proxy this session. Facts marked [V] were confirmed in search-result text from the primary source's own domain. Pages were not opened in full. Facts marked [V2] come from secondary sites or from the studio's raw research files.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A Socratic study coach that helps you get unstuck at 11 p.m. without doing the work for you, and lets you prove you understood it. |
| **Primary user / buyer** | Teens 13–19 (user). Parents (B2C payer for Plus). Schools (B2B payer for the proof-of-learning layer shared with Explain It Back). |
| **Core job-to-be-done** | "When I'm stuck on homework late at night and tempted to just get the answer, I want help that gets me moving and makes me understand it, so I can do the next one alone and walk into the test ready." |
| **Category on the stores** | Education (13+ / Teen rating). Not the Kids category. |
| **Top competitors (by downloads / revenue)** | Gauth (ByteDance), Photomath (Google), Brainly, Question.AI, ChatGPT (Study Mode / ChatGPT for Teens), Gemini Guided Learning, Khanmigo, Studdy |
| **Our wedge** | 1. **Learning mode is the only path by default**, not a toggle. Answers unlock only after the teen has done the thinking (attempt → hint ladder → faded worked example → teach-it-back). 2. **Verified math and science steps plus citations**, read aloud properly (MathML), so a blind teen gets the full product. 3. **The effort counts:** a "verified understanding moment" goes into the teen-owned Ascendly Record, which answer apps and generic chatbots don't produce. |
| **Business model** | Free core (daily coaching allowance with no hard stop mid-problem). Ascendly Plus ≈$12/mo or $79/yr (unlimited coaching, all subjects, exam integration). School licence $5–15 per student per year (bundled with Explain It Back). |
| **North-star metric** | Weekly verified understanding moments per active teen (teach-it-back passes plus independent re-attempts solved without hints). |
| **MVP candidate?** | **Yes.** Year 1 in the vision doc. |

## 2. Problem & users

**Problem statement.** Teens already use AI for schoolwork at scale. Pew (Feb 2026) found just over half of US teens have used chatbots for schoolwork, and about one in ten say they do all or most of their schoolwork with chatbot help [V2: Pew via search]. Answer-first AI raises practice scores and then lowers performance on unassisted tests: in the Bastani et al. *PNAS* 2025 RCT, unguarded GPT-4 raised practice performance by 48% but cut unassisted exam performance by 17%, while a guardrailed tutor mostly removed the harm [V2: raw 05]. The UC Irvine study of 3.2M ALEKS problems found the odds of a correct answer fell about 25% after ChatGPT arrived [V2: vision doc]. Every frontier lab now has a Socratic mode, and OpenAI launched **ChatGPT for Teens** on 18 Aug 2026 with Study Mode and "homework reminders" that appear when a teen seems to be trying to cheat [V2: TechCrunch, Business Today]. The modes are still **opt-in or easy to leave**. Critics call Study Mode "a new conversation filter", and engagement reportedly fell ~60% after three weeks of unfacilitated use [V2: raw 03]. Camera-first answer apps (Gauth, Photomath, Question.AI) are hard or impossible for blind students to use [V2: raw 01/02].

**Personas**
| Persona | Snapshot | What they need from Study Coach |
|---|---|---|
| **Aaliyah, 16, AP Calc and Chem** | Anxious and busy. Uses ChatGPT at night "just to check". Scores lower on tests than on homework. | A fast way to get unstuck that still leaves her able to do the problem on the test. A plan when she's out of time. |
| **Marcus, 15, blind (VoiceOver + braille display)** | Strong in history. Math graphs and camera-first apps shut him out. | Typed or spoken problem entry. Math spoken and navigable by structure (MathML). Graphs described in text and as data tables. No timers. |
| **Chloe, 17, ADHD** | Can't start. Loses the thread in long chat replies. | One step per screen, short turns, a visible "now / next" strip, and a way to park a thought without losing her place. |
| **Ms. Ortiz, parent** | Pays for tools. Worried about cheating and about AI "friends". | Proof that the tool teaches and doesn't give answers. No companion persona. No access to her teen's chats, but a weekly effort summary if the teen agrees. |
| **Mr. Chen, chemistry teacher** | 150 students. Has scaled back homework. | Evidence that thinking happened (process summaries, not transcripts), and class-level misconception patterns. |

**Needs & wants**
| Need | Evidence | How Study Coach addresses it |
|---|---|---|
| Help that doesn't undermine learning | Bastani 2025 (−17%); UCI ALEKS (−25% odds) [V2] | Hint ladder by default. Answer reveal only after an attempt. Independent re-attempt ("your turn") before closing |
| Patient, always-on "office hours" | "a tutor who doesn't get tired of my questions" (Study Mode users) [V2: raw 03] | 24/7, no judgement, short turns, voice or text |
| Accuracy | Khanmigo accepted "272 − 172 = 430" [V2: raw 03]; Gauth/Question.AI "wrong answers" [V2] | Computer-algebra and unit-checking verifier for every math/science step. Citations for factual claims. "I'm not sure" allowed |
| Not surveillance | "Everything you type… it sends it to your teacher… scary" [V2: raw 03] | Teachers and parents never see transcripts. Teen chooses to share process summaries only |
| Accessible math | Math output poorly read by screen readers; camera-first flows [V2: raw 01/02] | MathML output, typed/voice/LaTeX/keyboard input, text descriptions of every diagram |
| Honest billing | Gauth: user billed $11.99/mo for 27 months after a broken cancel flow; Trustpilot 2.1 vs App Store 4.9 [V2: myengineeringbuddy] | Fair-billing charter: price before trial, reminder, one-tap cancel, no weekly plans |
| Deadline pressure | Teens reach for answers when time is short [I; A1 in discovery plan] | "Deadline mode": a triage plan and a partial-credit strategy, not an answer dump |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Gauth** | Gauthtech (ByteDance) | 100M+ Play; 51M downloads in 2025 [V2]; Sensor Tower US iOS last-month estimate ~900K downloads and ~$1M revenue [V2] | Free + Plus ≈$11.99/mo; trial converts at $11.99–$49.99 depending on plan/region [V2] | 4.9 App Store (1.67M); Trustpilot 2.1 [V2] | Snap-to-answer, fast, multi-subject, step explanations, live tutors | Cheating use; billing loops and refused refunds; wrong answers on hard problems; data concerns | Camera-first; text walls; no dyslexia settings [V2: raw 01/02] | sensortower.com; myengineeringbuddy.com |
| **Photomath** | Google | 100M+ Play; 19M downloads in 2025 [V2] | Free; Plus $9.99/mo or $69.99/yr [V2] | ≈4.8 iOS; 4.2–4.3 Play [V2: raw] | Best handwriting OCR; animated steps; textbook solutions | Detailed steps paywalled; OCR misreads; "does homework for you" | Camera-first; math output weak for screen readers [V2: raw 01] | nibble-app.com; myengineeringbuddy.com |
| **Brainly** | Brainly | 100M+ Play; >15M daily users and 350M+ registered claimed; 2025 revenue est. $75M [V2/E: getlatka] | Free with ads; Plus ≈$24–$90/yr [E: raw 02] | 4.5 Play [V2: raw 01] | Huge answer archive; AI "Learning Companion" relaunch in 2025 | Answer quality; ads; used for copying | Heavy ads harm readability [V2: raw 01] | getlatka.com; fast.io |
| **Question.AI** | D3 Dimension Technology (Zuoyebang-linked [V2: raw]) | 10M+ Play, ~230K ratings; last updated Jun 2026 [V2] | Freemium, weekly and annual plans [E] | 4.6 Play [V2] | Snap-and-solve; chatbot; math focus | Wrong answers; paywall; ownership opacity | Camera-first [V2: raw 02] | play.google.com |
| **ChatGPT (Study Mode / ChatGPT for Teens)** | OpenAI | Top-3 overall US App Store for most of 2025–26 [E: raw 02] | Free; Plus $20/mo | n/a (general app) | Patient, 24/7; teen experience with Study Mode, homework reminders, quiet hours; parents can't read chats [V2] | Easy to switch to answer mode; child-safety experts skeptical of the teen launch [V2: Engadget headline] | Strong VoiceOver and Dynamic Type; voice mode [V2: raw 02] | techcrunch.com (18 Aug 2026); businesstoday.in |
| **Gemini (Guided Learning)** | Google | 1B+ incl. preinstalls [E: raw 01]; Gemini in Classroom for students of all ages from 10 Aug 2026 [V] | Free; AI Pro ≈$19.99/mo | n/a | Step-by-step questioning; quizzes; Classroom distribution | Opt-in; engagement fades [V2: raw 03] | Google a11y baseline; under-18 stricter policies [V2] | workspaceupdates.googleblog.com |
| **Khanmigo** | Khan Academy | 2M users globally, 770K US students in 2024–25 [V2: raw 05] | $4/mo or $44/yr learners; districts from $10/student/yr [V2] | ≈4.7 iOS (Khan app) [E] | Socratic; free for teachers; Khan content | Math errors; "sends it to your teacher" fear; web-first | Khan app "fully accessible with VO" (AppleVis) [V2: raw 02] | khanmigo.ai; edisonos.com |
| **Studdy** | Studdy (YC) | 500K+ students claimed; $500K YC funding (Apr 2025) [V2] | 5 free scans/day; Plus from $6.99/week [V2] | n/a | Step-by-step tutor chat across subjects | Weekly pricing [I] | Camera-first [I] | ycombinator.com; apps.apple.com |

**Market signal:** Chegg's Q2 2026 revenue was $51.8M, down 51% year on year, with academic subscription revenue down about 57% [V: sec.gov 10-Q/8-K via search]. Paid answer engines are collapsing while free AI and ByteDance-scale solvers grow. We should not compete on answers.

**Feature matrix** (✓ yes · ✗ no · ◐ partial)

| Feature | Gauth | Photomath | Brainly | Question.AI | ChatGPT Teens | Gemini GL | Khanmigo | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Photo/camera problem capture | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ◐ | **Parity**, never the only input |
| Typed / voice / LaTeX / math-keyboard input | ◐ | ◐ | ✓ | ◐ | ✓ | ✓ | ✓ | **Improve** (accessible math keyboard, voice math) |
| Instant final answer | ✓ | ✓ | ✓ | ✓ | ◐ | ◐ | ✗ | **Reject** as default. Answer shown only after attempt + ladder |
| Socratic hint ladder | ✗ | ✗ | ◐ | ✗ | ✓ | ✓ | ✓ | **Parity+**: fixed 4-rung ladder, visible to the teen |
| Learning mode cannot be switched off by the teen | ✗ | ✗ | ✗ | ✗ | ◐ | ✗ | ✓ | **Differentiate** (default and non-bypassable; parent/teacher can relax per class) |
| Worked-example fading | ✗ | ◐ | ✗ | ✗ | ✗ | ◐ | ✗ | **Differentiate** |
| Independent re-attempt ("your turn") | ✗ | ✗ | ✗ | ✗ | ◐ | ◐ | ◐ | **Differentiate** |
| Teach-it-back check | ✗ | ✗ | ✗ | ✗ | ◐ | ◐ | ◐ | **Differentiate**, feeds Ascendly Record |
| Verified solver / CAS check of steps | ◐ | ✓ | ✗ | ◐ | ✗ | ✗ | ◐ | **Improve**: every step checked, plus unit checks |
| Citations for factual claims | ✗ | n/a | ◐ | ✗ | ◐ | ◐ | ✗ | **Improve** (curated sources only) |
| Deadline / study-plan mode | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Screen-reader-navigable math (MathML) | ✗ | ◐ | ✗ | ✗ | ◐ | ◐ | ✓ | **Differentiate** (full parity for blind teens) |
| Live human tutor upsell | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | **Later (V2)**: school-provided tutors only, no coin packs |
| Coins / credits / weekly plans | ✓ | ✗ | ◐ | ✓ | ✗ | ✗ | ✗ | **Reject**: dark-pattern pricing |
| Ads in free tier | ◐ | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | **Reject**: no ads for minors |
| Named companion persona / "AI friend" | ✗ | ✗ | ◐ | ✗ | ✗ | ✗ | ◐ (named tutor) | **Reject** (FTC 6(b), CA SB 243). Neutral "Coach" tool voice only |
| Parent can read chats | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ◐ (teacher can) | **Reject**. Teen-shared summaries only |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| SC-01 | **Multimodal problem capture** | Type, dictate, math keyboard, LaTeX, photo (OCR with a "read back to confirm" step), paste. | Camera-first excludes blind teens [V2]; parity with Gauth/Photomath | Parity + Lumen P7 | MVP | Must |
| SC-02 | **Attempt-first prompt** | "What have you tried?" Accepts a partial attempt, a guess, or "no idea" (which is fine and starts at rung 1). | Bastani guardrail design [V2]; generation effect [I] | Differentiate | MVP | Must |
| SC-03 | **4-rung hint ladder** ★ | Rung 1 nudge (concept), 2 strategy, 3 first step shown, 4 faded worked example. The ladder is visible so the teen knows where they are. | Khanmigo/Study Mode parity, made predictable (P3) | Parity+ | MVP | Must |
| SC-04 | **Worked-example fading + "your turn"** ★ | After help, the coach generates a verified sibling problem. The teen solves it with fewer supports. Success closes the loop. | Worked-example effect; no competitor closes the loop [I] | Differentiate | MVP | Must |
| SC-05 | **Teach-it-back** ★ | 30–90 second explanation by voice, text, drawing or AAC. Checked against a short rubric. Pass = a "verified understanding moment". | North star; bridges to Explain It Back | Differentiate | MVP | Must |
| SC-06 | **Verified steps** | Every math/physics/chemistry step is checked by a computer-algebra system, unit checker and stoichiometry balancer before display. Unverifiable steps are labelled. | Khanmigo "272 − 172 = 430"; answer-app errors [V2] | Improve | MVP | Must |
| SC-07 | **Cited facts (humanities/science)** | Factual claims link to a curated source set (open textbooks, primary sources). No source, no claim: the coach says it isn't sure. | Hallucination control | Improve | MVP | Must |
| SC-08 | **Accessible math output** | MathML plus a plain-speech string, step-by-step navigation, braille-ready output, text + data-table descriptions for every graph. | Marcus persona; MathML support gaps on mobile [V2: mtm.se, Harvard] | Differentiate / Lumen | MVP | Must |
| SC-09 | **Deadline mode** | If the teen says "due in 20 minutes", the coach offers a triage plan (which parts to attempt, what to ask the teacher, partial-credit strategy). It still does not produce the answer. | Riskiest assumption A1; pressure drives cheating [I] | Differentiate | MVP | Must |
| SC-10 | **Session strip and designed ending** | Now / Next / Done strip. Ends with a 2-line summary, "what to review tomorrow", and a natural stop. | Lumen P3, P9 | Lumen | MVP | Must |
| SC-11 | **My Needs + Sensory Dial** | Shared profile: reading level, TTS, dyslexia typography, input modes, extended wait times, motion and sound. | Lumen P12 | Lumen | MVP | Must |
| SC-12 | **Ascendly Record entry (teen-owned)** | Each verified moment is saved privately. The teen chooses whether to share a process summary with a teacher or parent. | Surveillance fear [V2]; vision principle 3 | Differentiate | MVP | Must |
| SC-13 | **Safety layer** | AI disclosure, break reminder, distress escalation based on what the teen says, age-appropriate content filters, no persona. | SB 243, FTC 6(b) [V2] | Lumen / compliance | MVP | Must |
| SC-14 | Class context (teacher-set) | Teacher links a class: curriculum, notation conventions, and whether rung-4 examples are allowed. | Khanmigo district parity | Parity | V1 | Should |
| SC-15 | Misconception memory | Coach remembers the teen's recurring errors (on-device summary, teen can view/delete) and targets them. | Personalisation without profiling [I] | Improve | V1 | Should |
| SC-16 | Handoff to Exam Ready | "Add this to my review deck" creates spaced-retrieval cards. | Cross-app loop | Differentiate | V1 | Should |
| SC-17 | Diagram coach | Teen draws or describes a diagram. Coach gives feedback. Accessible alternative via structured description. | Science and geometry needs | Improve | V1 | Could |
| SC-18 | Study-group mode | Two to four friends work one problem with the coach, turn by turn (links to Study Squad). | Social study [V2: raw 03] | Differentiate | V2 | Could |
| SC-19 | School-provided human tutor escalation | District-funded tutoring hours routed from the coach when stuck repeatedly. | Gauth/Brainly tutor parity, without coin packs | Parity | V2 | Could |
| SC-20 | Offline practice pack | Downloaded sibling problems with verified solutions for no-connection study. | Equity [I] | Improve | V2 | Could |

★ = signature features. **Signature loop: attempt → hint ladder → faded example → "your turn" → teach-it-back.** The MVP has 13 features and covers that full loop.

## 5. Core experience & key user flows

**Core loop:** open → state the problem (any mode) → "what have you tried?" → ladder (as few rungs as needed) → "your turn" sibling problem → teach-it-back (optional but encouraged) → summary and natural end.

**Flow 1: Onboarding (≤5 min to first value)**
1. Store page shows price and the "no answers by default" promise before install.
2. Age screen (neutral date entry, per Apple Declared Age Range / Play age signals where available). Under 13 → redirected, no data kept.
3. First screen: Sensory Dial (Calm / Balanced / Lively) and "How do you like to work?" (type, talk, draw, screen reader detected automatically).
4. One sentence on how the coach works: "I'll help you get unstuck. I won't do it for you. You can see every step I check."
5. Straight into a real problem. Account creation is deferred until the teen wants to save progress (passkey or school SSO).

**Flow 2: Core session**
1. Teen photographs a stoichiometry problem. OCR reads it back ("Is this right?").
2. Coach: "What have you tried?" Teen: "I found moles of O₂." Coach checks that work (verified).
3. Rung 2 hint: "What does the balanced equation tell you about the ratio?" Teen answers. Correct.
4. Teen finishes. Coach: "Your turn": a sibling problem with different numbers. Teen solves it with no hints.
5. Teach-it-back: "In one or two sentences, why do we use the mole ratio?" Teen records 20 seconds of voice. Rubric passes.
6. Summary: "You did this one mostly alone. Tomorrow: 2 limiting-reagent questions." Saved to Record. Session ends.

**Flow 3: Deadline mode**
1. Teen: "It's due in 15 min, just give me the answer."
2. Coach acknowledges without judging, then offers: (a) a 10-minute plan to finish the two parts they can do, (b) the exact question to ask the teacher, (c) a reminder that honest partial work usually earns partial credit.
3. If a teacher has enabled "answer check" for this class, the teen can submit their own answer to be checked right/wrong. Never generated for them.

**Flow 4: Teacher/parent view**
1. Teen taps "Share" on a Record entry and chooses who sees it (teacher, parent, both, nobody).
2. Recipient sees a process summary: topic, rungs used, independent re-attempt result, teach-it-back excerpt (if the teen includes it). **Never the chat transcript.**
3. Teacher console (B2B) shows class-level misconception clusters from shared summaries only.

**Flow 5: My Needs profile** — reachable in one tap from every screen. Settings: reading level (grade 5–12 dial), TTS voice and speed, font/spacing/tint, input defaults, voice wait time (up to 30 s or "until I tap done"), motion, sound channels, break reminders. Changes apply immediately. Profile syncs across all Ascendly apps.

**Flow 6: Billing / cancellation** — price shown before trial; reminder 3 days before conversion; one-tap in-app cancel (and store-level cancel instructions); summer pause; accommodations and teach-it-back are free forever. Refund request in two taps.

**Information architecture:** Home (Ask · Continue · Today's review) · Session · Record · My Needs · Account/Billing · Help. Bottom tab bar with 4 labelled tabs. No infinite feed.

**Session design:** no default length; teen-chosen goal (1 problem / 25 min / "until I'm done"). Break nudge at 45 min (dismissible). SB 243-style AI and break reminder at least every 3 hours for known minors [V2]. A "2 more steps then we wrap up" transition warning when a teen-set time is reached.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial defaults.** First launch defaults to **Balanced**, or **Calm** if the OS has Reduce Motion or Increase Contrast turned on.
| Level | Study Coach changes |
|---|---|
| Calm | No animation apart from focus indication; no sound effects; muted palette; success shown as a quiet check and a short phrase; one element per screen (chat collapses to the current turn) |
| Balanced | Gentle transitions; soft confirmation tone (off by default); up to 3 elements (problem, current step, input) |
| Lively | Animated step reveals (Photomath-style) without flashing (WCAG 2.3.1); optional celebration after "your turn", always skippable |

**Input modes per task**
| Task | Tap | Keyboard | Voice | Math keyboard / LaTeX | Drawing | AAC | Switch | Camera |
|---|---|---|---|---|---|---|---|---|
| Enter problem | ✓ | ✓ | ✓ | ✓ | ✓ (handwriting) | ✓ (text) | ✓ | ✓ (never required) |
| Answer a hint | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Teach-it-back | ✓ (choose from sentence starters) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |

**Targets and gestures:** 44 pt / 48 dp minimum; no core gesture beyond single tap; no drag anywhere; step navigation also by Next/Previous buttons and hardware keyboard shortcuts.

**Reading and typography:** default copy at grade 6–8 with a reading-level dial (grade 5–12) that changes hint wording without changing the maths. Read-aloud with word highlighting on every message. BDA-aligned defaults (sans-serif, ≥16 px, 1.5 line height, left-aligned, 60–70 characters per line, off-white or dark background). WCAG 1.4.12 text-spacing override. Full Dynamic Type / font scale to the largest accessibility sizes without truncation.

**Math accessibility (concrete):**
- Every expression rendered with MathML and an aria-label speech string generated by a MathCAT-class engine (ClearSpeak style). VoiceOver reads MathML in WebKit; touch exploration into equations is unreliable on mobile [V2: mtm.se], so each step also has an **"explore this expression"** view that steps through terms with Next/Previous.
- Chrome on Android has supported MathML since version 109 [V2: caniuse via search], but TalkBack math speech is weaker, so the Android build ships the speech string as the primary label and tests with TalkBack each release.
- Nemeth and UEB braille output for refreshable braille displays [I; confirm in WP1].
- Graphs: auto-generated text summary plus a data table and optional sonification (off by default).

**Extended time and accommodations (504/IEP):** there are no timers in Study Coach. The profile stores accommodations once ("extended time 1.5×", "read-aloud", "scribe/speech-to-text") and passes them to Exam Ready and Explain It Back. Accommodations never require proof of diagnosis and are never behind the paywall.

**ADHD focus:** one question per turn; hint answers capped at ~60 words (expand on request); "park it" button to save a stray question for later; visible progress through the ladder; optional 25-minute focus timer (off by default); body-doubling handoff to Study Squad.

**Audio:** separate sliders for TTS voice and effects (music never plays). Every sound has a visual equivalent. Captions/transcripts for any voice output. Haptics optional.

**Age-respectful themes:** two themes (Minimal Light, Night Study Dark) plus high-contrast. No mascots and no childish rewards. Illustrations are optional.

**Lumen principles: app-specific acceptance criteria**
| # | Principle | Study Coach acceptance criterion |
|---|---|---|
| P1 | Default to calm | With Reduce Motion on, 0 non-essential animations; Dial reachable in 1 tap from Session and Home |
| P2 | Granular sound | No sound-only cue; effects default off; TTS and effects on separate sliders |
| P3 | Predictable structure | Ladder position always visible; no layout shift between rungs |
| P4 | Forgiving targets | Entire session completable with single taps / keyboard only (WCAG 2.5.7 pass) |
| P5 | Plain language | Hints at or below profile reading level in ≥95% of sampled turns (automated readability check + human review) |
| P6 | Dyslexia typography | BDA defaults on; text-spacing override does not break math rendering |
| P7 | Multimodal | Each task accepts ≥3 input modes; camera never required |
| P8 | Errorless, low-penalty | No scores, lives or penalties; wrong attempts get informative feedback; undo on every input |
| P9 | Focus, not exploitation | Every session ends on a summary screen; no autoplay-next problem |
| P10 | Don't rely on memory | Problem stays pinned on screen through the ladder; passkeys/SSO sign-in |
| P11 | Timing belongs to user | No time limits; voice input waits until "done" when set |
| P12 | My Needs profile | All accommodations free; profile shared across Ascendly apps |
| P13 | Age-respectful | ≥2 mature themes independent of reading level |
| P14 | Caregiver/teacher low admin | Teacher class link set up in ≤5 min; parent summary is one screen |
| P15 | Motivation without manipulation | No streak loss; weekly goal with pause days; no loss-framed notifications |
| P16 | ND-affirming | ND panel reviews coach tone and examples before release |
| P17 | Honest evidence claims | No "raises grades" claim until the pilot result is published; claims register maintained |
| P18 | Privacy and safe AI | DPIA done; no transcript sharing; no training on teen data without separate consent; no persona |

**Target Lumen audit score:** ≥22/24 (expected 23: item 12 "fair billing" depends on store-level cancellation behaviour we don't fully control).

## 7. AI specification & guardrails

**What AI does:** interprets the problem (OCR + LLM), diagnoses the attempt, selects the ladder rung, writes hints at the profile reading level, generates sibling problems (verified before display), evaluates teach-it-back against a rubric, and summarises the session.

**What AI does not do:** produce final answers by default; write essays or paragraphs (redirects to Draft Mentor); claim to be a person or a friend; infer emotion from voice, face or typing; grade for a teacher; remember anything the teen hasn't been shown and can delete.

**Capabilities needed:** frontier LLM with tutoring system policy (hosted, zero-retention contract); computer-algebra system and unit checker (deterministic); chemistry balancer; math OCR (handwriting); ASR tolerant of teen and accented speech (on-device where feasible); TTS; retrieval over a curated source index; safety classifier (self-harm, sexual content, violence) tuned for teens.

**Pedagogical policy**
- Attempt first. Rung escalation only on request or after two unproductive turns.
- Maximum one new idea per turn. Always end a hint with a question the teen can answer.
- Rung 4 worked examples use a *parallel* problem, never the teen's exact problem, unless a teacher has enabled it for the class.
- "Your turn" must be completed (or explicitly skipped) before a session is recorded as verified.
- Answer reveal after the full ladder plus an attempt, showing the verified solution with the teen's own mistakes highlighted. Teachers can turn answer reveal off for a class.

**Safety**
- **No companion persona.** The coach has no name, avatar, backstory or feelings, and does not express affection or loneliness. It declines relationship role-play and redirects to study. This avoids the "companion chatbot" pattern targeted by the FTC 6(b) inquiry (Sept 2025) and CA SB 243, which since 1 Jan 2026 requires AI disclosure and break reminders at least every 3 hours for known minors [V2: Jones Walker, CA leginfo].
- **Disclosure:** "You're working with an AI" on first run, in the session header, and in reminders.
- **Distress escalation:** triggered only by what the teen says (keywords + classifier). Response: calm acknowledgement, 988 Suicide & Crisis Lifeline (US) or local equivalent, option to pause, and — for school accounts — the district's designated contact only if the district's protocol requires it and the teen has been told so at onboarding. No emotion recognition (banned in EU education since Feb 2025 [V2: raw 05]).
- **Academic integrity:** detects "take-home test" wording and reminds the teen of their teacher's AI policy; does not refuse to teach the concept.
- **Content filters:** teen-appropriate policy; no sexual content; health questions get general information plus "talk to a trusted adult or clinician".

**Hallucination controls:** CAS verification of every quantitative step (unverifiable → "I can't check this step; here's how you could"); retrieval-only factual claims with citations; refusal to invent sources; sibling problems generated then solved by the CAS before display.

**Evaluation plan**
| Eval | Method | Threshold to ship |
|---|---|---|
| Step correctness | 2,000-problem benchmark across Algebra I → AP Calc, Chem, Physics | ≥99.5% displayed steps correct; 100% of unverifiable steps labelled |
| Answer leakage | Red-team set of 500 "just give me the answer" jailbreaks | ≤1% leakage outside the policy |
| Hint quality | Teacher raters (n=6) score 300 sessions on a 5-point rubric | Mean ≥4.0 |
| Teach-it-back agreement | AI vs two teacher raters | Cohen's κ ≥0.6 (AI never used for grades) |
| ASR word error rate by speaker group | Consented teen voice samples: accents, stuttering, dysarthria, AAC speech | WER gap ≤5 points between groups, or tap/type fallback prompted automatically |
| Safety | Self-harm, sexual, persona-seeking prompts | 100% correct routing in the gold set |
| Screen reader | Blind testers complete 5 flows | 5/5 completion without sighted help |

**Cost and latency [E]:** ~6–10 LLM turns per problem at ~1.5K tokens each; ~$0.01–0.03 per problem with a mid-tier model and caching; CAS negligible. First hint ≤2.5 s p50, ≤5 s p95. A free tier of ~10 problems/day costs ≈$0.20–0.60 per active teen per month [E].

## 8. Data, privacy & compliance

**Data inventory**
| Data | Why | Retention | Where |
|---|---|---|---|
| Problem text/images | Tutoring | Images deleted after OCR (≤24 h); text 90 days unless saved to Record | Cloud (zero-retention LLM contract) |
| Chat transcripts | Session continuity | 30 days rolling; teen can delete anytime; never shared | Cloud, encrypted |
| Voice (teach-it-back, dictation) | ASR | Audio discarded after transcription unless the teen saves it to Record | On-device ASR where feasible; else cloud, no retention |
| Misconception summary | Personalisation | Until deleted; visible and editable | On-device first |
| Record entries | Portfolio | Teen-owned; export any time | Cloud |
| My Needs profile | Accessibility | Until deleted | Synced |
| Birth year (not date) | Age assurance | Account lifetime | Cloud |

**Applicable regimes:** COPPA 2025 (under-13 blocked; no knowing collection); FERPA/SOPIPA and state student-privacy laws for school accounts (school-official exception, signed DPAs, SDPC NDPA); UK AADC and US state design codes (high-privacy defaults, no nudges, DPIA); **KOSA-ready** (Senate Commerce advanced KOSA unanimously on 5 Aug 2026; the House passed a version without the duty of care; not law [V2: CNBC, CT Mirror]); CA SB 243; EU AI Act Art. 50 transparency (in force Aug 2026) and Art. 5 emotion-recognition ban; teach-it-back evaluation is designed to Annex III high-risk standards ahead of the Digital Omnibus date of **2 Dec 2027** [V2: Gibson Dunn, CSA]; FTC §5 for claims. Not a medical device.

**Consent flows:** teen (13+) consents in plain language; for 13–15 in regions requiring it (e.g., parts of EU under GDPR Art. 8), verifiable parental consent; separate opt-in for using de-identified sessions to improve models (default **off**); school accounts governed by district DPA with teen-facing notice of exactly what the school can see.

**Store policies:** Teen rating (12+/13+). Not in Apple Kids category or Google "Designed for Families" (under-13 excluded), but we follow Families-style SDK restrictions anyway: no ad SDKs, analytics limited to first-party, no third-party data sharing.

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Free | $0 | ~10 coached problems/day (never cut off mid-problem), all subjects, teach-it-back, all accessibility features, Record, export |
| Plus | $12/mo or $79/yr (benchmarks: Gauth ≈$11.99/mo; Photomath $69.99/yr; Khanmigo $44/yr [V2]) | Unlimited coaching, misconception memory, Exam Ready integration, family plan up to 3 teens ($119/yr) |
| School | $5–15 per student per year (Khanmigo districts from $10 [V2]) | Class context, teacher console, proof-of-learning with Explain It Back, SSO, DPA |

**Fair-billing charter:** no weekly plans, no coins; price before trial; 3-day reminder; one-tap cancel; summer pause; refunds for forgotten renewals within 14 days.

**Channels:** teen-native short-form content (organic; "watch me get unstuck without cheating"); teacher communities (free teacher console seeds B2B); state AI-literacy initiatives; libraries. **No paid ads targeted at under-18s.**

**ASO:** keywords "homework help without cheating", "AI tutor", "math help step by step", "study help", "accessible math". Category Education. Accessibility Nutrition Label: declare VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Color, Sufficient Contrast, Reduced Motion, Captions — only after WP4 audit confirms each.

**Launch markets:** US first (English, Spanish UI in V1); UK (GCSE/A-level notation) in V1; India and Southeast Asia deliberately not first (price and solver competition) [I].

## 10. Success metrics

- **North star:** weekly verified understanding moments per weekly active teen (target ≥3 by month 3 of pilot).
- **Inputs:** % sessions with an attempt before rung 2 (≥60%); "your turn" completion rate (≥50%); teach-it-back attempt rate (≥35%); % sessions ended on the summary screen (≥80%); deadline-mode sessions that end without cheating complaints (teacher-reported).
- **Guardrails:** Sensory Comfort ≥4/5; answer-leakage ≤1%; displayed-step error ≤0.5%; zero billing complaints escalated to stores; frustration events (rage-quit within 60 s of a hint) ≤10% of sessions; teen privacy-comfort score ≥4/5.
- **Learning outcomes:** pre/post unassisted quiz gains in the WoZ pilot (target ≥0.2 SD vs. control); later a pre-registered RCT with an unassisted exam outcome (ESSA Tier 2 → Tier 1 path).
- **Retention:** D1 ≥40%, D7 ≥20%, D30 ≥12%; DAU/MAU ≥25% in term time (studio "habit formed" benchmark for teen learning apps [E: raw 05]). Seasonality expected.

## 11. Validation plan (no-code, discovery phase)

**Riskiest assumptions (ranked)**
1. Teens choose Socratic help over free answer engines when deadlines loom (A1).
2. Verified steps and MathML output make a blind teen's experience equal (feasibility).
3. Teens accept teach-it-back as worth 60 seconds.
4. Parents pay $79/yr when ChatGPT for Teens is free.
5. Teachers value process summaries enough to link classes.

**Experiments**
| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | Diary study + **Wizard-of-Oz coach** (trained tutors follow the written ladder policy via a chat front end), 3 weeks, 2 schools | 40 teens, ≥30% ND/disabled | ≥50% return weekly in week 3; pre/post quiz gain ≥0.2 SD vs. own baseline | <30% weekly return in week 3 |
| E2 | Deadline-mode role-play in Figma with a timer countdown scenario | 20 teens | ≥60% choose the plan over "leave for ChatGPT" | <35% |
| E3 | Screen-reader math spike: 20 expressions in accessible HTML mockups | 6 blind/low-vision teens | ≥90% of expressions understood; SUS ≥75 | <70% understood |
| E4 | Teach-it-back comfort: voice vs text vs drawing | 30 teens | ≥70% complete at least one; comfort ≥3.5/5 | <40% |
| E5 | Fake-door pricing ($79/yr vs $49/yr vs free) on parent landing page | ~2,000 adult visitors | ≥8% waitlist; ≥30% pick paid | <3% waitlist |
| E6 | Sensory A/B (Calm vs Lively) | 24 teens incl. 8 ND | Calm ≥ Lively on comfort for ND teens, no task-success loss | — |

**Mapping to Discovery Plan:** WP1 (competitor audit of Gauth/Photomath/Question.AI/ChatGPT Teens with the Lumen rubric); WP2 (teen interviews, 15 study-session diaries); WP4 (E1–E4, E6); WP5 (E5).

## 12. Build handoff (for the agent team, post-Gate 2)

**Epic A: Problem capture**
- *Story:* As a blind teen, I want to type or dictate a math problem so I don't need the camera.
  - Given VoiceOver is on, When I open Ask, Then focus lands on a labelled text field with a math keyboard toggle, And the camera button is labelled and optional.
  - Given I photograph a problem, When OCR completes, Then the problem is read back as text and MathML speech, And I must confirm or edit it before coaching starts.

**Epic B: Hint ladder**
- *Story:* As a teen, I want the smallest hint that gets me moving.
  - Given I've submitted an attempt, When I tap "Hint", Then I receive rung 1 only, And the ladder indicator shows 1 of 4.
  - Given I ask "just tell me the answer" before any attempt, When the policy engine evaluates the turn, Then no final answer is shown, And I'm offered rung 1 or deadline mode.

**Epic C: Verification**
- Given a hint contains a quantitative step, When the step cannot be verified by the CAS, Then it is displayed with an "unchecked" label and a way to check it by hand, And the event is logged for review.

**Epic D: "Your turn" and teach-it-back**
- Given I finished the original problem, When I start "your turn", Then the sibling problem has different values and a CAS-verified solution, And completing it without hints records a verified moment.
- Given I choose AAC or text for teach-it-back, When I submit, Then the rubric is applied identically to voice submissions.

**Epic E: Record and sharing**
- Given I have a Record entry, When I share with my teacher, Then the teacher sees only the process summary fields I previewed, And never the transcript.

**Epic F: Safety**
- Given I write a message expressing intent to self-harm, When the classifier flags it, Then the coach pauses tutoring, shows crisis resources, And no emotion is inferred from voice or face.
- Given a continuous session for a known minor reaches 3 hours, Then an AI-disclosure and break reminder is shown.

**Non-functional requirements**
- Performance: first hint p95 ≤5 s; app cold start ≤2 s on a 4-year-old mid-range Android.
- Offline: Record, My Needs and saved problems readable offline; coaching needs a connection (V2 offline packs).
- Platforms: iOS, Android, web (Chromebook priority for schools).
- Accessibility: WCAG 2.2 AA; Lumen ≥22/24; MathML + speech strings on all platforms.
- Localization: English (US/UK notation) at MVP; Spanish V1; RTL-ready layout.
- Security: SOC 2 Type II path; encryption at rest and in transit; zero-retention LLM contracts; annual pen test.

**QA focus**
- AT matrix: VoiceOver (iOS), TalkBack (Android), ChromeVox (Chromebook), Switch Control, Voice Control, Dynamic Type XXXL, braille display (Nemeth/UEB), Reduce Motion.
- Sensory A/B: Calm vs Lively comfort and task success.
- AI safety cases: answer-leakage jailbreaks, persona-seeking prompts ("be my girlfriend"), self-harm disclosures, take-home-test detection, wrong-step injection.
- Age/COPPA: under-13 entry, age re-entry attempts, parent-consent path for regions that require it.
- Billing: trial reminder timing, one-tap cancel, summer pause, refunds, family plan.

**Platform dependencies:** Lumen design system (Dial, answer tray, typography tokens); My Needs profile; AI orchestration (tutor policy engine, CAS service, citation retrieval, safety classifier); privacy stack (consent, age assurance, retention); evidence engine (pre-registered pilot tooling); shared Ascendly Record service.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Free ChatGPT for Teens / Gemini in Classroom commoditise Socratic tutoring | High | High | Own the verified loop, Record, accessibility and teacher trust; integrate rather than compete on raw chat |
| Teens leave for answer apps under pressure | High | High | Deadline mode; honest partial-credit strategy; speed of first hint |
| Verified-solver coverage gaps (proofs, word problems) | Medium | High | Label unchecked steps; restrict MVP subjects to where verification works |
| Teach-it-back feels like surveillance | Medium | Medium | Private by default; teen chooses to share; no transcripts |
| MathML support uneven on Android/TalkBack | Medium | Medium | Speech strings as primary label; explore-expression view; test each release |
| Regulatory drift (KOSA duty of care, state codes) | Medium | Medium | Design to the strictest version now |

**Open questions:** Which 2–3 subjects give the best verification coverage for MVP (Algebra I–II, Chemistry, Physics)? Should teachers be able to allow rung-4 on the exact problem? What is the right free daily allowance given LLM costs? Does "no persona" reduce engagement compared with named tutors like Khanmigo?

## 14. Sources
- Sensor Tower, Gauth US overview — https://app.sensortower.com/overview/1542571008?country=US [V2]
- Gauth review, billing loop and ratings — https://www.myengineeringbuddy.com/blog/gauth-reviews-alternatives-pricing-offerings-in-2026/ [V2]
- Brainly revenue estimate — https://getlatka.com/companies/brainly [V2/E]; Brainly AI review — https://fast.io/resources/brainly-ai-review-2026/ [V2]
- Photomath pricing — https://nibble-app.com/blog/photomath-app ; https://www.myengineeringbuddy.com/blog/photomath-reviews-alternatives-pricing-offerings/ [V2]
- Question.AI Play listing — https://play.google.com/store/apps/details?id=com.qianfan.aihomework&hl=en_US [V2]
- Studdy — https://www.ycombinator.com/launches/JDE-studdy-an-ai-tutor-for-every-student ; https://apps.apple.com/us/app/studdy-ai-tutor-math-solver/id6450114499 [V2]
- ChatGPT for Teens — https://techcrunch.com/2026/08/18/openai-launches-a-safer-chatgpt-for-teens-years-after-teens-started-using-it/ ; https://www.businesstoday.in/technology/news/story/openai-launches-chatgpt-for-teens-parental-controls-study-mode-and-more-features-explained-549969-2026-08-19 [V2]
- Pew, How Teens Use and View AI (24 Feb 2026) — https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/ [V2: search summary]
- ChatGPT meta-analysis — https://www.nature.com/articles/s41599-026-07019-z [V2]
- Gemini in Classroom for all ages — https://workspaceupdates.googleblog.com/2026/08/gemini-in-google-classroom-is-expanding-to-users-of-all-ages-with-contextualized-Gemini-starter-prompts-for-students.html [V]
- Khanmigo pricing — https://www.edisonos.com/alternatives/khan-academy-pricing ; https://www.khanmigo.ai/pricing [V2]
- Chegg Q2 2026 — https://www.sec.gov/Archives/edgar/data/0001364954/000136495426000085/a9901-financialresultsq220.htm [V]; https://www.tradingview.com/news/tradingview:b586680b848f9:0-chegg-inc-2026-revenue-51-85m-eps-0-03-10-q-summary/ [V2]
- CA SB 243 — https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB243 [V]; https://www.joneswalker.com/en/insights/blogs/ai-law-blog/ai-regulatory-update-californias-sb-243-mandates-companion-ai-safety-and-accoun.html [V2]
- KOSA status — https://www.cnbc.com/2026/08/05/kosa-privacy-social-media-senate.html ; https://ctmirror.org/2026/08/05/senate-panel-approves-kosa/ [V2]
- EU AI Act Digital Omnibus — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ ; https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-high-risk-deadline-omnibus-20260/ [V2]
- Math accessibility — https://www.mtm.se/en/recommendations-for-stem-users/ ; https://accessibility.huit.harvard.edu/news/2026/08/practical-guide-accessible-math ; https://caniuse.com/mathml [V2]
- Bastani et al., PNAS 2025 — https://www.pnas.org/doi/10.1073/pnas.2422633122 [V2: raw 05]
- Studio raw research: research/raw/01–05, research/app-catalog.csv [V2]

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Re-scope → Embedded Tutor (EN-03) in Exam Ready / Explain It Back + a stand-alone mode |
| **Ships in** | Ascendly app (S3) |
| **Build wave** | 1d |
| **Pre-discovery priority score** | 77/100 [I] |
| **Consumes engines** | EN-03, EN-12 |
| **Studio features used** | SX-08, SX-09, SX-17 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = SC-02, SC-03, SC-04, SC-05, SC-06, SC-08.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| SC-E1 | **Bring your AI chat** | The teen imports a chat they had with a general assistant. The coach turns it into retrieval questions and a teach-it-back check, meeting teens where they already study. |
| SC-E2 | **At-error invitations** | Offered inside Exam Ready practice after two misses (SX-17). |

### 15.3 New validation question
Under deadline pressure, do teens choose the coach? Diary + Wizard-of-Oz study, n=40; ≥50% return weekly.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 5 | 3 | 4 | 5 | 3 | 3 | 3 | 5 |

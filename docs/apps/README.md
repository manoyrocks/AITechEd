# App Strategy Library: 35 apps across 5 ventures

**Status:** Discovery & Validation (specifications only, no code) · **Date:** 29 September 2026

Every app has an individual **strategy and product specification**. All specs follow the same [14-section template](_TEMPLATE.md):
1. Summary
2. Problem & users
3. Competitive feature benchmark against the top-selling / top-downloaded apps in the same store category
4. Recommended feature set (MVP / V1 / V2, MoSCoW, Parity / Improve / Differentiate / Lumen)
5. Core experience & flows
6. Inclusive, accessible & sensory design spec
7. AI specification & guardrails
8. Data, privacy & compliance
9. Monetization & go-to-market
10. Success metrics
11. No-code validation plan
12. Build handoff: epics, Given/When/Then acceptance criteria, QA focus
13. Risks & open questions
14. Sources

To hand an app to an AI or human build team, use the **[Unified Agent-Team Prompt](../agent-team/unified-agent-team-prompt.md)** with the app's doc path.

## Venture indexes
Each venture folder has a README with:
- an app table
- shared venture features
- a combined **"features we reject and why"** list

| Venture | Ages | Index |
|---|---|---|
| 🏮 Lanternling | 1–3, 4–7 | [lanternling/README.md](lanternling/README.md) |
| 🧭 Questwise | 8–12 | [questwise/README.md](questwise/README.md) |
| 🧗 Ascendly | 13–19 | [ascendly/README.md](ascendly/README.md) |
| 🌲 Evergrow | 20–34, 35–59, 60+ | [evergrow/README.md](evergrow/README.md) |
| 🌊 Wavelength | Neurodivergent ≈2–17 | [wavelength/README.md](wavelength/README.md) |

## All 35 app specs

| Venture | App | Ages | Signature features (from the spec) | Benchmarked against (examples) |
|---|---|---|---|---|
| Lanternling | [Babble Buddy](lanternling/01-babble-buddy.md) | 1–3 (parent-held) | Moment Cards for routines. Word Garden (any language; signs count). Opt-in on-device Talk Tally | LENA, Speech Blubs, Kinedu, BabySparks, Vroom |
| Lanternling | [Tap & Wonder](lanternling/02-tap-and-wonder.md) | 1–3 | Single-tap real-photo scenes. Parent-set "Sleepy Scene" ending. Co-play line per scene | Pok Pok, Sago Mini, Bimi Boo, Khan Kids |
| Lanternling | [Story Lantern](lanternling/03-story-lantern.md) | 2–7 | Pause & Ask dialogic prompts. Screen-off Lantern Mode. Human-template, editor-checked personalized stories | Epic!, Vooks, Readmio, Moshi, Yoto |
| Lanternling | [Sound Garden](lanternling/04-sound-garden.md) | 4–7 | On-device expected-word read-along. Tap version of every task. Published phonics scope. Careful early-risk guidance | HOMER, Reading Eggs, Teach Your Monster, Ello, Read Along |
| Lanternling | [Number Nest](lanternling/05-number-nest.md) | 3–7 | Montessori choice shelf. Self-correcting materials. Tap-to-place instead of dragging | Khan Kids, DragonBox, Todo Math, SplashLearn |
| Lanternling | [Calm Cubs](lanternling/06-calm-cubs.md) | 3–7 | Picture routines with transition warnings. Haptic breathing buddies. Two-tap parent "Help Now" | Daniel Tiger, Breathe Think Do, Moshi, Choiceworks |
| Lanternling | [Two Words](lanternling/07-two-words.md) | 3–7 | Home language treated as an equal. Grandparent voice recordings. Two-generation games | Lingokids, Gus on the Go, Studycat, Dinolingo |
| Questwise | [Sage Tutor](questwise/01-sage-tutor.md) | 8–12 | 5-rung Socratic hint ladder with no final answers. Verified-solver gate. "Try one like it". Screen-reader math | Khanmigo, Gauth, Photomath, Brainly, ChatGPT Study Mode |
| Questwise | [Math Realms](questwise/02-math-realms.md) | 8–12 | Mastery-gated regions. One error never lowers progress. Earned-only rewards | Prodigy, IXL, SplashLearn, DreamBox, Zearn, Beast Academy |
| Questwise | [Read Rangers](questwise/03-read-rangers.md) | 8–12 | Passion-matched leveled texts. Dyslexia settings. "Find the evidence" quests. Optional on-device fluency | Epic!, Reading Eggspress, Raz-Kids, Newsela, Amira |
| Questwise | [Builder's Lab](questwise/04-builders-lab.md) | 9–12 | Question-only AI pair-programmer. Blocks ↔ Python. Build-log portfolio | Scratch, Tynker, Code.org, CodeSpark, Swift Playgrounds |
| Questwise | [AI Detectives](questwise/05-ai-detectives.md) | 9–12 | Weekly case mysteries. Sandboxed "catch the AI mistake" model. Real-or-fake media lab | Interland, Day of AI, Code.org AI, BrainPOP |
| Questwise | [Wonder Lab](questwise/06-wonder-lab.md) | 8–12 | Off-screen experiments. Phone sensors as instruments. ESA-exportable science journal | Tinybop, KiwiCo, Mystery Science, Seek |
| Questwise | [Mission Control](questwise/07-mission-control.md) | 8–12 | AI task breakdown the child edits. No-loss focus timers. Movement breaks | Joon, Brili, Goally, Tiimo, Forest |
| Ascendly | [Study Coach](ascendly/01-study-coach.md) | 13–19 | Attempt → 4-rung hints → faded example → teach-it-back. Solver-checked steps. MathML | ChatGPT Study Mode, Gemini, Claude, Khanmigo, Gauth |
| Ascendly | [Exam Ready](ascendly/02-exam-ready.md) | 14–19 | Readiness score as a range. Free exportable spaced flashcards. 1.5×/2× extended-time practice | Khan + Bluebook, Quizlet, Knowt, UWorld, Save My Exams |
| Ascendly | [Explain It Back](ascendly/03-explain-it-back.md) | 13–19 | Any-modality explanations (incl. AAC and sign video). Adaptive "why?" follow-up. Teacher-confirmed feedback. Misconception heat map | Edpuzzle, Nearpod, Formative, Seesaw, MagicSchool |
| Ascendly | [Draft Mentor](ascendly/04-draft-mentor.md) | 13–19 | Question-only mentor. Teen-owned authorship timeline. Dictation and AAC count as own writing | Grammarly Authorship, QuillBot, NoRedInk, Turnitin Clarity |
| Ascendly | [Study Squad](ascendly/05-study-squad.md) | 13–19 | Friends-only quiet rooms. Shared timers. Self-chosen phone lock-in. No penalty for leaving early | Forest, Focusmate, YPT, StudyStream, Opal |
| Ascendly | [Pathfinder](ascendly/06-pathfinder.md) | 15–19 | Accessible 20-minute job simulations. Skills portfolio | Naviance, Xello, Forage, BigFuture, Roadtrip Nation |
| Ascendly | [Life Ready](ascendly/07-life-ready.md) | 13–19 | Scenario challenges. Scam sandbox. "Is this real?" AI and media lab | Greenlight, Zogo, NGPF, Checkology, iCivics |
| Evergrow | [AI Fluency Lab](evergrow/01-ai-fluency-lab.md) | 20–59 | Real-workflow sandboxes. Rubric grading with human review. Skills Passport | Coursera, LinkedIn Learning, DataCamp, Section, Google AI Essentials |
| Evergrow | [Career Sprint](evergrow/02-career-sprint.md) | 20–34 | Employer-briefed projects with an AI-use log. Practice-only interview coach (no emotion scoring) | Forage, Springboard, Yoodli, Big Interview |
| Evergrow | [Speak Freely](evergrow/03-speak-freely.md) | 20+ | 15-minute human tutor check-in steering AI practice. Type-instead-of-speak counts equally | Duolingo Max, Speak, Praktika, Babbel, italki, Preply |
| Evergrow | [Lead with AI](evergrow/04-lead-with-ai.md) | 35–59 | Branching AI-rollout simulations. Individual transcripts never shown to the employer | LinkedIn Learning, Harvard ManageMentor, Mursion, BetterUp |
| Evergrow | [Parent Coach](evergrow/05-parent-coach.md) | 25–59 | Tonight's script from the child's in-app activity. AI-talk guides. Teens see what parents see | Common Sense, Understood.org, Kinedu, Khan parent tools |
| Evergrow | [Silver Circuit](evergrow/06-silver-circuit.md) | 60+ | Safe in-app scam simulations. Family help only with consent. Live peer-guide classes | GetSetUp, Senior Planet, AARP Fraud Watch, TechBoomers |
| Evergrow | [Curiosity Circle](evergrow/07-curiosity-circle.md) | 55+ | Host-led cohorts of 8–12. Captions. AI study buddy between sessions. No dementia claims | GetSetUp, Wondrium, MasterClass, BrainHQ, OLLI |
| Wavelength | [Wavelength Day](wavelength/01-wavelength-day.md) | 2–17 | Change Card for surprises. One-sentence AI schedule drafts. Page-by-page caregiver review of social narratives | Choiceworks, First Then, Goally, Tiimo, Birdhouse |
| Wavelength | [Wavelength Voice](wavelength/02-wavelength-voice.md) | 2+ | Motor-plan-stable grid growth. AI expansion shows what it added and never speaks by itself. OBF export. Speech keeps working if the subscription lapses | Proloquo2Go, TouchChat, LAMP WFL, TD Snap, CoughDrop, Avaz |
| Wavelength | [Calm Harbor](wavelength/03-calm-harbor.md) | 4–17 | Sensory profile → one-tap toolbox. Flash-tested calm visuals. Self-report check-ins, no biometrics | Mightier, Zones of Regulation, Breathe Think Do, Miracle Modus |
| Wavelength | [ReadWave](wavelength/04-readwave.md) | 5–14 | Speech-difference-tolerant read-along with tap equivalence. Age-respectful decodables | Nessy, Lexia Core5, Amira, Learning Ally, Speechify |
| Wavelength | [Focus Crew](wavelength/05-focus-crew.md) | 7–17 | Co-signed reward plan that fades. Minor-safe body doubling (parent co-work, silent focus buddy) | Joon, Brili, Goally, Tiimo, Goblin Tools |
| Wavelength | [Social Compass](wavelength/06-social-compass.md) | 8–17 | Double-empathy scenarios. Self-advocacy scripts. Learner-authored "My Profile" card | Social Thinking, Model Me Kids, Everyday Speech, Floreo |
| Wavelength | [Spark Switch](wavelength/07-spark-switch.md) | 2–17 (higher support) | One activity set for switch, gaze, head and touch. Choice-making progression. CVI palettes. IEP/EHCP log | Cosmo, Switch Skills, Look to Learn, Sensory Guru, Leka |

## Cross-cutting patterns across the 35 specs
- **What the top sellers do well, and we match:**
  - short sessions and a clear core loop
  - visible mastery progress
  - voice and read-aloud
  - personalization
  - parent and teacher dashboards
  - offline modes
  - polished character and design craft
- **Where we deliberately differ:** the combined reject lists in each venture README cover:
  - hearts and energy limits
  - streak punishment
  - pay-to-win and loot boxes
  - ads to children
  - answer-giving AI
  - companion personas
  - emotion recognition
  - timed learning loops
  - drag-only interaction
  - billing traps
  - diagnosis and efficacy over-claims
- **Our signature differentiators everywhere:**
  - the Sensory Dial (Calm default where specified)
  - a tap equivalent for every voice or drag task
  - human-reviewed AI content
  - learner-owned, portable "My Needs" profiles
  - fair billing
  - the evidence-tier claims register

## Research caveats (read before external use)
- The five spec agents shared a **200-search web budget, and it ran out**. Direct page fetches (app stores, Sensor Tower, vendor sites) were blocked by the environment's proxy.
- The competitor tables for these apps rely more on the studio's earlier raw research ([V2]) and on memory ([M]):
  - Lanternling: Number Nest onward
  - Questwise: some rows
  - Ascendly: Study Squad, Pathfinder, Life Ready
  - Evergrow: Silver Circuit, Curiosity Circle
  - Wavelength: Focus Crew, Social Compass, Spark Switch
- Every figure is tagged [V] / [V2] / [M] / [E] / [I], and no quotes or numbers were invented.
- **Discovery WP1** (a Sensor Tower/Appfigures export and a hands-on competitor audit) must verify these figures before any investor or public use.
- **New findings the agents surfaced that affect the plan:**
  - An NBER/Chalkbeat study of Khanmigo in Tennessee (2026) found students used the tutor in only **17%** of the practice sessions where they made an error. Tutor engagement design is the crux.
  - The EU AI Act's Art. 4 AI-literacy duty was reportedly softened to an "obligation of effort" (June 2026). Lead B2B messaging with productivity, not compliance.
  - Coursera's enterprise net retention was reported at ~91%, a sign of tight L&D budgets. Mid-market positioning and proof of ROI matter.
  - Babbel reportedly closed its consumer live classes in July 2025. This is a warning for the economics of hybrid human-plus-AI tutoring (Speak Freely).

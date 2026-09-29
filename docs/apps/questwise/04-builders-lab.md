# Builder's Lab: App Strategy & Product Specification

> **Venture:** Questwise · **App #:** 4/7 · **Ages:** 9–12 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/02-questwise-tweens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Questwise index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A project-based path from blocks to Python where kids build their own games, animations and robots, with an AI pair-programmer that explains and asks but never writes the code for them. |
| **Primary user / buyer** | User: makers 9–12. Buyer: parent, ESA family, microschool/co-op, after-school club. |
| **Core job-to-be-done** | "When I have an idea for a game, I want to build it myself and get unstuck when it breaks, so I can show people something I made and feel like a real coder." |
| **Category on the stores** | Education (iOS Kids 9–11) · Google Play Education; strong web/Chromebook use |
| **Top competitors (by downloads / revenue)** | Scratch (135M+ registered users), ScratchJr (70M+ downloads), Code.org, Minecraft Education (23M downloads 2025), Tynker, codeSpark, Kodable, Hopscotch, Swift Playgrounds, Roblox Studio |
| **Our wedge** | 1) Past "tutorial hell": projects of your own design, with a scaffolded bridge from blocks to text (Scratch/Code.org stall point). 2) A pair-programmer that explains errors Socratically (vs. AI that writes code, or no help at all). 3) Keyboard- and screen-reader-accessible editor with voice commands, and no open community chat. |
| **Business model** | In Questwise Family ($99/yr). "Project Club" add-on or microschool licence. Free tier: 2 active projects. |
| **North-star metric** | Weekly "ship moments" per active maker (a project change that runs and was built by the child, measured by child-authored blocks/lines). |
| **MVP candidate?** | **Later** (V1/V2 per vision; validate WTP now). |

## 2. Problem & users

**Problem statement.** Free block coding is excellent for starting, but kids stall after tutorials, and the new AI tools can write the code for them.
- Scratch has over 130M registered users [V2 jetlearn/brightchamps]; ScratchJr has 70M+ downloads [V2 scratchjr.org]. Forum VoC: "Kids stall without projects to work toward"; the Scratch community needs moderation for older kids [M raw 03].
- Paid players (Tynker ≈$180/yr, Kodable $119.99/yr, codeSpark $90/yr) are mostly puzzle-first [V2].
- Scratch itself is preparing an opt-in "Creative Learning Assistant" that "offers help only when asked… prioritizing their agency" [V2 Scratch forum], signalling where the category is going.
- Code.org turned Hour of Code into Hour of AI (Dec 2025) with 50+ partners [V THE Journal/PR Newswire], raising AI-creation expectations.
- Roblox Studio is popular but platform safety is under pressure: 2026 facial age checks to chat and new Roblox Kids (5–8)/Select (9–15) accounts [V Roblox newsroom].

**Personas**

| Persona | Snapshot | Needs | Pain |
|---|---|---|---|
| **Jayden, 10** | Minecraft fan, finished Hour of Code | Build his own game | Tutorials feel like copying; stuck on bugs |
| **Zara, 12, autistic** | Deep interest in trains; prefers keyboard | Predictable editor; precise feedback | Noisy community, surprise pop-ups |
| **Eli, 11, low vision / screen reader** | Wants to code like his brother | Accessible editor | Drag-and-drop blocks are unusable with screen readers [I] |
| **Nicole, parent** | Scratch is free; why pay? | Visible progress beyond Scratch; safety | Unmoderated comments; AI doing the work |
| **Mr. Ortiz, guide** | Runs a Friday maker block | Ready projects, progress view | Prep time; mixed ages |

**Needs & wants**

| Need | Evidence | Response |
|---|---|---|
| Projects, not puzzles | Stall after tutorials [M raw 03] | Idea → plan → build → share-with-invited loop |
| Help without AI doing it | Vision; Scratch CLA direction [V2] | Pair-programmer: explain, question, point; no code writing |
| Path to "real" code | Tynker/Code.org have text tracks [M] | Blocks ↔ Python dual view |
| Safe sharing | Scratch moderation concerns [M]; Roblox chat safety [V] | Share only with invited family/class; preset reactions |
| Accessibility | Block editors are drag-first [I] | Keyboard block editor, screen-reader announcements, voice commands |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Scratch** | MIT / Scratch Foundation | 135M registered users; 164M projects shared (2024) [V2] | Free | n/a | Creative freedom; huge remix community | Stalls without projects; community moderation for older kids [M] | Drag-first blocks; limited SR support [I] | jetlearn; scratch.mit.edu/statistics |
| **ScratchJr** | MIT/Tufts/Playful Invention | 70M+ downloads, 400M+ projects [V2] | Free | n/a | Great 5–7 entry | Outgrown by 8 [I] | Icon-based, drag | scratchjr.org |
| **Code.org** | Code.org | Hour of AI 2025, 50+ partners [V] | Free | n/a | Structured courses; Hour of AI | Classroom-centric; puzzle feel [M] | Block editor + some keyboard [M] | THE Journal; code.org |
| **Minecraft Education** | Microsoft | 23M downloads 2025 [V2 raw 01] | School licence ≈$5.04/user/yr [E raw] | ≈4.2 [V2] | Kids love Minecraft; code builder | School login; curriculum fit; motion sickness [V2/E] | Immersive Reader; high sensory load [E] | raw 01/02 |
| **Tynker** | Tynker | Established paid leader [M] | ≈$180/yr individual; ≈$225 family; lifetime ≈$360 [V2] | n/a | Blocks → Python/JS; Minecraft mods | Price [V2] | Standard | myelearningworld |
| **codeSpark** | codeSpark | Popular 5–9 [M] | $15/mo or ≈$90/yr [V2] | n/a | Wordless puzzles for pre-readers | Younger skew | Wordless helps pre-readers | Apple listing |
| **Kodable** | Kodable | School + home [M] | $119.99/yr; $24.99/mo; lifetime $199.99 [V2] | n/a | K–5 path to JS | Monthly price high | — | teachyourkidscode / brighterly |
| **Hopscotch** | Hopscotch | Popular iPad maker app [M] | $79.9/yr unlimited; $1.99/mo play pass [V2] | n/a | Make and publish games on iPad | Community exposure [M] | Touch-first | coding app roundups |

Also benchmarked [M]: Swift Playgrounds (free, Apple, strong VoiceOver, older skew); Roblox Studio (Luau; 2026 age checks for collaboration [V]); micro:bit (hardware, free MakeCode editor).

**Feature matrix**

| Feature | Scratch | Code.org | Tynker | Hopscotch | Minecraft Ed | Swift PG | Our decision |
|---|---|---|---|---|---|---|---|
| Open-ended projects | ✓ | ◐ | ◐ | ✓ | ✓ | ◐ | **Parity** |
| Guided project path | ✗ | ✓ | ✓ | ◐ | ✓ | ✓ | **Improve** (idea-first scaffolds) |
| Blocks ↔ text bridge | ✗ | ◐ | ✓ | ✗ | ✓ (MakeCode/Python) | ✗ (text) | **Parity** |
| AI helper | ◐ (CLA planned) | ◐ | ◐ [M] | ✗ | ◐ | ✗ | **Differentiate** (Socratic, no code writing) |
| AI writes code for you | ✗ | ✗ | ◐ [M] | ✗ | ◐ | ✗ | **Reject** |
| Public community/comments | ✓ | ✗ | ◐ | ✓ | ✗ | ✗ | **Reject** (invited-only sharing) |
| Keyboard/SR-accessible editor | ◐ | ◐ | ✗ | ✗ | ◐ | ✓ | **Differentiate** |
| Hardware/robots | ✓ (ext.) | ✓ | ✓ | ✗ | ✗ | ✓ | **V2** (micro:bit) |
| Portfolio/build log | ◐ | ◐ | ◐ | ◐ | ✗ | ✗ | **Differentiate** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| BL-01 | **Idea starter** | Pick a genre (maze, pet sim, story, platformer) and personalise via questions; produces a plan card, not code | Stall without projects [M] | Differentiate | MVP | Must |
| BL-02 | **Accessible block editor** | Blocks placed by tap-to-insert or keyboard; every block has a spoken description; no drag required | P4; Eli persona | Lumen | MVP | Must |
| BL-03 | ⭐ **Pair-Programmer (Socratic)** | Explains errors, asks "What did you expect to happen?", points to the block/line; may show a *different* example; never inserts code | Vision; Scratch CLA direction [V2] | Differentiate | MVP | Must |
| BL-04 | ⭐ **Blocks ↔ Python dual view** | Toggle shows the same program as Python; from level 3, kids edit in Python with block peek | Tynker/MakeCode parity | Parity | MVP | Must |
| BL-05 | **Mission path** | 6 starter missions per genre teaching concepts (events, loops, variables, conditionals) inside the child's project | Code.org parity with less copying | Improve | MVP | Must |
| BL-06 | ⭐ **Build log portfolio** | Auto-captured milestones with the child's own notes/voice memo; exportable for ESA portfolios | Microschool/ESA need | Differentiate | MVP | Must |
| BL-07 | **Invited-only sharing** | Share a playable link with family/class; preset reactions ("Cool level!", "I found a bug"); no free text | Roblox/Scratch safety concerns [V/M] | Lumen | MVP | Must |
| BL-08 | **Asset library (human-made)** | Sprites, sounds, backgrounds with diverse, age-respectful styles; kid drawing tool | P13 | Parity | MVP | Must |
| BL-09 | **Debugger for kids** | Step-through with highlighted block/line, variable watch in plain words | Pair-programmer support | Improve | MVP | Should |
| BL-10 | **Sensory Dial + editor themes** | Calm editor (no sound on run by default), high-contrast theme | P1, P2 | Lumen | MVP | Must |
| BL-11 | **Parent/guide progress** | Concepts used (from the child's code), projects shipped, build log highlights | Proof of learning | Parity | MVP | Must |
| BL-12 | Voice coding commands | "Add a when-clicked block", "move to line 4" | Motor/SR access | Lumen | V1 | Should |
| BL-13 | micro:bit / robot kits | MakeCode-compatible hardware projects | Maker demand [M] | Parity | V2 | Could |
| BL-14 | Co-build | Two invited friends edit different sprites of one project | Vision co-op | Differentiate | V1 | Should |
| BL-15 | "Make an AI" projects | Kid trains a tiny classifier (images/sounds) with on-device data; links to AI Detectives | Hour of AI trend [V] | Differentiate | V1 | Should |
| BL-16 | Club kit for guides | Weekly session plans, rubrics | Microschool channel | Improve | V1 | Should |

**MVP (when built) = BL-01 to BL-11 (11).** **Signature features:** BL-03 Socratic pair-programmer, BL-04 dual view, BL-06 build log.

## 5. Core experience & key user flows

**Core loop:** idea → plan card → build a small step → run → (bug → pair-programmer questions) → ship moment → build log note → share with invited people → next step.

**Flow 1: Onboarding (≤5 min)**
1. Parent VPC; sharing permissions (family only by default).
2. Child picks genre + theme; answers 3 idea questions ("Who's your hero? What do they collect?").
3. First mission: make the hero move with arrow keys; runs by minute 4.

**Flow 2: Core build session**
1. Now/Next/Done strip shows the plan step ("Next: make coins disappear when touched").
2. Child adds blocks by tap/keyboard; runs the game.
3. Something breaks → taps "Help me think": pair-programmer asks "What did you expect?", highlights the relevant block, suggests a test ("Try making the coin say something when touched").
4. Fix → ship moment, build log prompt ("What did you figure out?" voice or text).
5. Session ends with "Your game now has: scoring!" and a stop point.

**Flow 3: Parent/guide:** concepts heatmap (events, loops, conditionals, variables, functions), playable latest version, build log highlights.

**Flow 4: My Needs:** input mode (tap, keyboard, voice V1), code font size, colour-blind-safe block palette, reduced motion in game previews, sound on run off.

**Flow 5: Billing:** Questwise charter; free tier keeps all projects readable forever (no hostage projects).

**IA:** Child: My Projects, Editor, Missions, Build Log, My Needs. Adult: Guild Hub.

**Session design:** Default 30 minutes with a 5-minute warning; saving is automatic; ends at a working state when possible ("Let's stop after this runs").

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial:** Calm: no editor animation; game preview motion reduced (sprites move but no screen shake/particles); sounds muted on run. Balanced (default): gentle snaps; preview sounds at 50%. Lively: effects on, still no flashing >3/s (and the editor warns kids when *their* game would flash: "Flashing can hurt some players' eyes").

**Input modes:** tap-to-insert blocks; full keyboard (Tab through palette, Enter to insert, arrows to move in script); screen-reader navigation of scripts as nested lists; voice commands (V1); switch access via Lumen scanning (V1); drawing for sprites.

**Targets:** blocks ≥48 dp tall; no drag required (drag available as an option).

**Reading:** block labels at grade 3 reading level with icons; read-aloud on any block; Python view with dyslexia-friendly monospace option, adjustable spacing.

**Screen-reader code:** each block announces type, parameters and nesting ("repeat 10 times, contains 2 blocks"); Python view uses standard text semantics; errors announced politely, never as alert sounds.

**No timers** in missions; kids' own games can use timers, but the mission path teaches "accessible game design" (offer a no-timer mode in your game).

**Age-respectful:** "Workshop" (illustrated) and "Terminal" (dark, pro-style) themes.

**Lumen acceptance criteria**

| P | Criterion |
|---|---|
| P1 | Reduce Motion → no editor animation, reduced preview |
| P2 | Error states never sound-only; sound on run off by default in Calm |
| P3 | Editor layout fixed; palette never reorders |
| P4 | Every block operation possible without drag |
| P5 | Block labels ≤ grade 3; read-aloud |
| P6 | Code fonts adjustable; spacing override |
| P7 | Tap + keyboard at MVP; voice V1 |
| P8 | Undo/redo unlimited; autosave; no "fail" |
| P9 | Session ends at designed point |
| P10 | Plan card always visible |
| P11 | No mission timers |
| P12 | Accessibility free |
| P13 | 2 themes |
| P14 | Parent sees one-screen summary |
| P15 | No streaks; ship moments celebrate the child's authorship |
| P16 | Asset library includes disabled/ND characters |
| P17 | No "become a programmer in X weeks" claims |
| P18 | No public profiles; AI never writes code |

**Target Lumen score:** 22–23/24 (screen-reader block editing is the hardest item; validate early).

## 7. AI specification & guardrails

- **AI does:** static analysis of the child's program to locate likely bugs (deterministic first); LLM generates Socratic questions and explanations grounded in the analysis; suggests a *different* mini-example illustrating the concept; build-log prompts; concept detection for dashboards.
- **AI does not:** insert or rewrite blocks/lines in the child's project; generate whole projects; generate images of real people; chat off-topic.
- **Pedagogy:** PRIMM-style (Predict, Run, Investigate, Modify, Make) [M]; hint ladder (question → point to area → concept reminder → parallel example → pseudo-step in words); authorship metric counts only child-authored code.
- **Safety:** tool not friend (pair-programmer is a "Lab Assistant" panel, no avatar persona); disclosure; distress escalation via shared classifier on typed text; no emotion recognition; asset uploads scanned; no external links.
- **Code-copy guard:** paste of >20 lines into Python view triggers a gentle authorship check ("Did you write this? Tell your build log where it came from"); guide-visible flag, not punishment.
- **Evaluation:** 1,000 buggy kid-programs benchmark; target ≥85% correct bug localisation, 0% code insertion in responses; teacher-rated helpfulness ≥4/5; SR usability sessions each sprint.
- **Cost [E]:** ≈$0.10–0.25 per active maker/month.

## 8. Data, privacy & compliance

Projects (code, child-made assets), build log (text, optional voice memo stored only with parental consent), sharing links (invited recipients only), concept analytics. Retention: projects life of account; exportable (.sb3-compatible and .py where possible). COPPA 2025 (child drawings/voice are personal information when identifiable; separate consent for voice memo; AI training off); FERPA/SOPIPA for clubs/schools; state design codes (no public profiles, no nudges); EU AI Act transparency. Kids category: no external links without a parental gate; no UGC exposure to strangers (avoids Apple/Google UGC moderation obligations for public content).

## 9. Monetization & go-to-market

- **Benchmarks:** Scratch/Code.org free; Tynker ≈$180/yr; Kodable $119.99/yr; codeSpark ≈$90/yr; Hopscotch $79.9/yr.
- **Ours:** in Questwise Family ($99/yr for 3 kids); "Project Club" (guide-led monthly challenge + review) test at $8/mo; microschool licence.
- **Channels:** ESA (coding courses eligible in many states [I]); microschool Friday-maker blocks; after-school programmes; B2C.
- **ASO:** "coding for kids 9-12", "learn Python kids", "make games kids", "safe coding app no chat".
- **Positioning vs. free:** "Scratch is where you start; Builder's Lab is where you finish your own game."

## 10. Success metrics

- **North-star:** weekly ship moments per active maker (≥3).
- **Inputs:** projects with ≥5 sessions; % help requests resolved by child after pair-programmer questions (≥60%); Python-view adoption at level 3 (≥40%).
- **Guardrails:** AI code insertion incidents = 0; Sensory Comfort ≥4/5; SR-user task completion ≥80%; zero billing complaints.
- **Outcomes:** concept assessment (e.g., short CS-concepts probe) pre/post over 8 weeks.
- **Retention:** D30 20%, project return rate 50% [E].

## 11. Validation plan

**Riskiest assumptions:**
1. Parents will pay for coding when Scratch and Code.org are free (vision).
2. Kids accept an AI that won't write code.
3. A screen-reader-usable block editor is achievable.

| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | Smoke test "Project Club" offer | 1,500 visits; 10 parent interviews | ≥4% waitlist; ≥5/10 say they'd pay ≥$8/mo | <1.5% → bundle-only |
| E2 | Wizard-of-Oz pair-programmer (human helper in a Scratch session using the policy) | 12 kids, 3 sessions | ≥70% bugs fixed by child; kids rate help ≥4/5 | <50% |
| E3 | Accessibility prototype of keyboard/SR block editing (clickable HTML prototype, no product code) | 5 SR users, 5 motor-impaired, 5 typical | ≥80% can build a 5-block script | <50% → text-first path for SR users |
| E4 | Microschool maker block concierge | 2 microschools, 4 weeks | Guides rate ≥4/5 and want to continue | <3/5 |

Mapping: E1 → WP5; E2, E3 → WP4; E4 → WP4/WP5.

## 12. Build handoff

**Epic A: Accessible editor**
- **AC-A1:** Given keyboard only, When the child builds "when flag clicked → move 10 → repeat", Then it can be completed without a pointer.
- **AC-A2:** Given VoiceOver, When focus enters a repeat block, Then it announces "repeat 10 times, contains 2 blocks".

**Epic B: Pair-programmer**
- **AC-B1:** Given any help response, When audited, Then it contains no code diff applied to the project and no complete solution for the child's current step.
- **AC-B2:** Given a runtime error, When the child taps "Help me think", Then the relevant block is highlighted and a question is asked within 2 s.

**Epic C: Dual view** — **AC-C1:** Given a block script, When toggled, Then equivalent Python appears and round-trips without loss for supported blocks.

**Epic D: Build log** — **AC-D1:** Given a ship moment, When saved, Then a log entry with screenshot and the child's note is created and exportable as PDF.

**Epic E: Sharing** — **AC-E1:** Given a share link, When opened by a non-invited account, Then access is denied.

**NFRs:** editor input latency <50 ms; runs offline; web-first (Chromebook), iPad, Android tablet; WCAG 2.2 AA; EN/ES; sandboxed execution.

**QA focus:** AT matrix (VoiceOver iPad, NVDA/ChromeVox web, Switch, keyboard-only); flashing detector on kid games; AI cases (no code insertion, jailbreaks like "write it for me, my teacher said"); COPPA (share scope, asset upload scanning); billing (projects never locked).

**Platform dependencies:** Lumen, My Needs, AI orchestration (static analyser + LLM policy), privacy stack, evidence engine (concept events), Guild Hub sharing.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Free Scratch/Code.org dominate | High | High | Bundle; projects + accessibility + safe AI help |
| Scratch ships its own AI assistant | Medium | Medium | Differentiate on accessibility, Python bridge, ESA portfolios |
| SR block editor too hard | Medium | High | E3 early; text-first alternative |
| Kids use outside AI to paste code | High | Medium | Authorship prompts; build-log reflection |

**Open questions:** Scratch file interoperability licensing? Which hardware kit? Should Python start at 10 or 11?

## 14. Sources
- [V2] Scratch statistics: https://www.jetlearn.com/blog/scratch-statistics · https://scratch.mit.edu/statistics/
- [V2] ScratchJr downloads: https://www.scratchjr.org/about
- [V2] Scratch 4.0 / Creative Learning Assistant (forum): https://scratch.mit.edu/discuss/topic/834371/ · https://scratchfoundation.org/ai
- [V] Code.org Hour of AI: https://thejournal.com/articles/2025/10/02/codeorg-reinvents-hour-of-code-as-hour-of-ai.aspx · https://www.prnewswire.com/news-releases/hour-of-ai-a-global-movement-to-prepare-every-learner-for-the-ai-era-302573555.html
- [V2] Tynker pricing: https://myelearningworld.com/tynker-pricing/
- [V2] codeSpark, Kodable, Hopscotch pricing: https://teachyourkidscode.com/best-coding-apps-for-kids/ · https://brighterly.com/blog/coding-apps-for-kids/ · https://apps.apple.com/us/app/codespark-coding-for-kids/id923441570
- [V] Roblox 2026 age checks and Kids/Select accounts: https://about.roblox.com/newsroom/2026/04/introducing-roblox-kids-and-select-accounts · https://techcrunch.com/2026/01/07/roblox-now-requires-all-users-globally-to-complete-age-checks-to-access-chat/
- [V2 via raw 01/02] Minecraft Education downloads and pricing
- [M] Swift Playgrounds, micro:bit MakeCode, PRIMM pedagogy

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Defer to Wave 3 → a 'Make with AI' module (free Scratch/Code.org dominate) |
| **Ships in** | Questwise app (S2) |
| **Build wave** | 3 |
| **Pre-discovery priority score** | 55/100 [I] |
| **Consumes engines** | EN-03 |
| **Studio features used** | SX-14, SX-17 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = BL-02, BL-03, BL-04, BL-06.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| BL-E1 | **Accessible coding as the wedge** | A screen-reader- and switch-operable block/Python editor, which few kids' coding tools offer [I]. |
| BL-E2 | **Make an AI responsibly** | Projects paired with AI Detectives cases (SX-18). |

### 15.3 New validation question
Parent willingness to pay against free tools. Interviews, n=10; proceed only if ≥40% would pay.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 2 | 3 | 4 | 3 | 2 | 3 | 3 | 2 |

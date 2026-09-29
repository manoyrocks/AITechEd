# AI Detectives: App Strategy & Product Specification

> **Venture:** Questwise · **App #:** 5/7 · **Ages:** 9–12 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/02-questwise-tweens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Questwise index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Weekly case-based mysteries where kids investigate how AI works, catch it making mistakes, spot fakes and scams, and practise staying safe online. |
| **Primary user / buyer** | User: 9–12. Buyer: teachers and microschool guides (primary), homeschool parents, ESA families. |
| **Core job-to-be-done** | "When I see a weird video, chatbot answer or message online, I want to know how to check if it's real and safe, so I can make smart choices and explain it to my family." |
| **Category on the stores** | Education (iOS Kids 9–11); web-first for classrooms |
| **Top competitors (by reach)** | Google Be Internet Awesome/Interland, Common Sense digital citizenship (used in 70% of US schools), Code.org Hour of AI, Day of AI (MIT RAISE), BrainPOP, Nearpod, Experience AI, AI4K12 resources |
| **Our wedge** | 1) Hands-on sandbox where kids *test* a real (safe, bounded) model and see it fail, rather than watching slides about AI. 2) A continuing mystery season with a home loop (family case night), not a one-off lesson. 3) Fully accessible (captions, narration, no timers) and built for 9–12 reading levels, while many AI literacy lessons target grades 6–12. |
| **Business model** | Free classroom tier (brand builder); in Questwise Family; microschool/co-op licence; later district. |
| **North-star metric** | Weekly cases solved with a correct "evidence + explanation" per active learner. |
| **MVP candidate?** | **Later** (Year 2 per vision), but the cheapest to validate now (paper cases). |

## 2. Problem & users

**Problem statement.** Kids 9–12 use AI and see synthetic media daily, but most AI-literacy content is either one-hour events or teacher slide decks, and the leading online-safety game predates generative AI.
- **Policy pull:** Executive Order 14277 (23 Apr 2025) sets US policy to promote AI literacy through "early exposure to AI concepts", a task force and a Presidential AI Challenge [V UCSB/Wikisource].
- **Supply is free but fragmented:** Common Sense's digital citizenship curriculum is used by 70% of US schools, with 165+ lessons; its AI lessons are "geared towards students in grades 6 through 12" and take ≤20 min [V2 commonsense.org/Wyoming library]. Be Internet Awesome added an AI Literacy Guide for grades 2–8 in June 2025 [V2 Google]. Day of AI offers a free PreK–12 AI literacy curriculum [V2 dayofai.org]. Hour of AI ran in Dec 2025 with 50+ partners [V].
- **Gap [I]:** there is no continuing, game-quality, accessible AI-literacy experience for 9–12s that works at home and school, with hands-on model testing.
- Under-13s now meet AI directly: Gemini is available to under-13s through Family Link [V2].

**Personas**

| Persona | Snapshot | Needs | Pain |
|---|---|---|---|
| **Ms. Patel, grade 5 teacher** | Must cover digital citizenship + new AI standards | 20–30 min ready lessons, assessment | Slides are dry; kids already know more than the slides |
| **Mr. Ortiz, microschool guide** | Wants AI literacy for mixed ages | Case sets for groups | No time to vet AI tools |
| **Jayden, 10** | Watches gaming videos; saw an AI "leak" | Fun, detective-style challenge | Lectures |
| **Deaf learner, Nia, 11** | Uses captions and ASL | Captioned, visual cases | Video-heavy lessons without good captions |
| **Nicole, parent** | Worried about scams and deepfakes | Talk starters | Doesn't know what to say |

**Needs & wants**

| Need | Evidence | Response |
|---|---|---|
| AI literacy that meets new expectations | EO 14277 [V]; AI4K12, Day of AI [V2] | Cases mapped to AI4K12 "Five Big Ideas" [M] and state standards |
| Short, ready classroom units | Common Sense ≤20 min lessons [V2] | 20-min case + 10-min discussion |
| Hands-on, not slides | Hour of AI hands-on format [V] | Sandbox experiments with bounded models |
| Family conversation | Parent persona | Family case night cards |
| Accessibility | Nia persona | Captions, transcripts, ASL for flagship cases (V1) |

## 3. Competitive feature benchmark

| App / programme | Publisher | Reach signal | Price | Rating | Features users love | Top complaints / gaps | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Be Internet Awesome / Interland** | Google + iKeepSafe | Large classroom use [M]; AI Literacy Guide (grades 2–8) June 2025 [V2] | Free | n/a | Game worlds (Interland), 5 safety pillars | Interland is a browser game from 2017 [M]; AI content is teacher-guide supplementary [V2] | Some timed mini-games [M] | beinternetawesome.withgoogle.com; Google AI literacy guide |
| **Common Sense Education** | Common Sense | Used by 70% of US schools; 165+ lessons [V2] | Free | n/a | Trusted, short lessons, K–12 | AI lessons target grades 6–12 [V2]; slide-based [I] | Lesson materials; variable | commonsense.org |
| **Code.org Hour of AI** | Code.org + CSforALL | Global event, 50+ partners, 100+ activities [V] | Free | n/a | Creative hands-on AI (dance, music) | One-off event [I] | Web-based | THE Journal; PR Newswire |
| **Day of AI** | Day of AI (MIT RAISE) | Free PreK–12 curriculum; national Responsible AI for America's Youth campaign 2025–26 [V2] | Free | n/a | Research-backed, grade-by-grade | Teacher-led, not a kid app [I] | Varies | dayofai.org |
| **BrainPOP** | BrainPOP | Classroom staple [M] | Family ≈$129/yr; homeschool $350/yr (3–8) [V2] | n/a | Animated videos + quizzes incl. digital citizenship/AI topics [M] | Price for homes; passive video [I] | Captions; quiz timers none [M] | homeschoolbuyersclub; learnspark |
| **Nearpod** | Renaissance | Classroom platform [M] | School licence; some free lessons [V2] | n/a | Media literacy "Evaluating Media" bundles (8 lessons) [V2] | Teacher-driven only | Standard | nearpod.com blog |
| **Experience AI** | Raspberry Pi Foundation + Google DeepMind | 2M+ students [V2] | Free | n/a | Lesson units on ML | Ages 11–14 skew [M] | Teacher-led | Google AI literacy PDF |

**Feature matrix**

| Feature | Interland | Common Sense | Hour of AI | Day of AI | BrainPOP | Our decision |
|---|---|---|---|---|---|---|
| Kid-playable game | ✓ | ✗ | ✓ | ◐ | ◐ | **Parity** |
| Hands-on model testing | ✗ | ✗ | ✓ | ✓ | ✗ | **Improve** (bounded sandbox, repeatable) |
| Deepfake / synthetic media spotting | ✗ [M] | ◐ | ◐ | ◐ | ◐ | **Differentiate** |
| Scam/phishing practice | ✓ | ✓ | ✗ | ✗ | ◐ | **Parity** |
| Continuing season/narrative | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Family/home loop | ◐ (family guide) | ✓ (family tips) | ✗ | ✗ | ✗ | **Improve** |
| Teacher dashboard/assessment | ◐ | ✗ | ✗ | ✗ | ✓ | **Parity** |
| Grade 3–5 reading level for AI topics | ◐ | ✗ | ✓ | ✓ | ✓ | **Parity** |
| Timed challenges | ◐ [M] | ✗ | ✗ | ✗ | ✗ | **Reject** |
| Real deepfakes of real people | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject**: consent/defamation; use synthetic personas made for the case |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| AD-01 | ⭐ **Case files** | Weekly mysteries (20 min): clues, evidence board, a verdict with reasoning | Continuity gap [I] | Differentiate | MVP | Must |
| AD-02 | ⭐ **Model sandbox** | Kids test a bounded chatbot and image classifier: find where it fails, see bias from skewed training data | Hands-on trend [V] | Differentiate | MVP | Must |
| AD-03 | **Real or synthetic? lab** | Spot-the-generated image/audio/video with lateral-reading moves (source, reverse search, context), not just "look for six fingers" | Synthetic media need [I] | Differentiate | MVP | Must |
| AD-04 | **Scam & safe-sharing drills** | Simulated messages (fake prize, "friend" asking for photo, password request); child chooses and explains | Interland parity | Parity | MVP | Must |
| AD-05 | **Safe prompting practice** | What's OK to share with AI (no names, addresses, photos of self); prompt clinic | COPPA spirit; Gemini under-13 access [V2] | Differentiate | MVP | Must |
| AD-06 | **Evidence board & explain-it** | Kids justify verdicts by voice, text, drawing or choosing reasons; Sage-style Socratic nudges | Reasoning focus | Improve | MVP | Must |
| AD-07 | **Teacher case pack** | Lesson plan, slides, printable clue cards, standards map (AI4K12, CSTA, state), exit ticket | Classroom channel | Parity | MVP | Must |
| AD-08 | **Family case night** | Printable/co-play card for home, one talk question | Parent persona | Improve | MVP | Must |
| AD-09 | **Detective's notebook** | Glossary of AI terms with pictures and audio, earned as cases are solved | Vocabulary | Improve | MVP | Should |
| AD-10 | **Accessible media** | Captions, transcripts, audio descriptions for all case media; ASL for flagship cases (V1) | Nia persona; P2 | Lumen | MVP | Must |
| AD-11 | **Teacher/parent progress** | Cases solved, reasoning quality, concepts covered | Assessment | Parity | MVP | Should |
| AD-12 | Class co-op cases | Teams split clues; team verdict; no chat, preset clue-sharing | Vision co-op | Differentiate | V1 | Should |
| AD-13 | Make-a-fake-safely studio | Generate a synthetic image of a made-up creature, watermark it, and explain the label | Creation builds understanding | Differentiate | V2 | Could |
| AD-14 | News literacy season | Headlines, ads vs. news, algorithm feeds (partner content) | Nearpod/Newsela parity | Parity | V1 | Should |

**MVP (when built) = AD-01 to AD-11 (11).** **Signature features:** AD-01 case files, AD-02 model sandbox, AD-03 real-or-synthetic lab.

## 5. Core experience & key user flows

**Core loop:** new case → briefing (narrated) → investigate 3–5 clues (sandbox, media lab, message drill) → evidence board → verdict + explanation → debrief ("what AI can and can't do") → family card → case closed.

**Flow 1: Onboarding.** Teacher creates class (roster by code; school acts under FERPA/COPPA school-authorisation for educational use only) or parent creates family account (VPC). Child picks detective badge (non-human icon), theme, Dial. Case 0 "The Confident Robot" runs in 5 min.

**Flow 2: Core case (example: "The Homework Bot That Lied").**
1. Briefing: "A bot told a student that spiders have 6 legs. Why?"
2. Sandbox: kids ask the bounded bot 5 questions; one clue shows it answering confidently and wrongly.
3. Clue 2: training-data cards show the bot learned from a mislabeled set.
4. Evidence board: pick 2 clues that explain the error; explain by voice/typing/choice.
5. Debrief: "AI predicts likely words. It can sound sure and be wrong." Family card: "Ask a grown-up to check one AI answer together this week."

**Flow 3: Teacher view.** Assign case; live board of class progress (no names shown to peers); exit ticket results; standards covered.

**Flow 4: My Needs.** Captions default on; narration speed; text size; Calm media (no jump scares, no dramatic stingers); answer modes.

**Flow 5: Billing.** Free for classrooms; family plan via Questwise charter.

**IA:** Case Board (season map), Case, Notebook, My Needs; Teacher console.

**Session design:** 20-minute cases; 5 min debrief; one case per week recommended; no binge unlocking (next case opens on schedule or when a teacher assigns).

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial:** Calm: no suspense music or sudden reveals; static clue cards. Balanced (default): light mystery music on the map only; soft reveal animations. Lively: dramatic music allowed on briefings, never during reasoning; no jump scares at any level.

**Input modes:** tap, voice, typing, drawing (circle evidence on an image), AAC symbol reasons (V1), switch scanning (V1).

**Targets:** ≥48 dp; evidence board uses tap-to-pin (no drag).

**Reading:** case text at grade 3–4, key terms glossed; full narration; BDA typography.

**Audio/visual:** every media clue has captions + transcript; images have descriptive alt text *that does not give away the answer* (and an "audio description detective" mode where describers point to the clues for blind learners, validated with blind testers); audio clues have visual waveforms and transcripts for Deaf learners.

**Deepfake exercises for blind/low-vision kids:** audio-based and text-based synthetic media cases are equivalent paths, so no child is excluded from the concept.

**No timers.** Scam drills never use countdowns ("act now!" is shown as a *clue* in the message, not a timer on the child).

**Age-respectful:** "Noir" (stylised, mature) and "Comic" themes.

**Lumen acceptance criteria**

| P | Criterion |
|---|---|
| P1 | Reduce Motion → static reveals |
| P2 | 100% media captioned + transcribed |
| P3 | Case structure identical every week |
| P4 | Evidence pinning by tap |
| P5 | Grade 3–4 text; narration everywhere |
| P6 | BDA defaults |
| P7 | ≥3 answer modes; equivalent non-visual case paths |
| P8 | Wrong verdicts lead to "re-examine clue" with no penalty |
| P9 | Weekly cadence; case-closed ending |
| P10 | Clues remain visible on evidence board |
| P11 | No timers |
| P12 | Free accessibility |
| P13 | 2 themes |
| P14 | Family card per case; teacher setup ≤5 min |
| P15 | Notebook collection tied to learning; no streaks |
| P16 | Diverse detectives incl. disabled characters |
| P17 | No "makes kids safe online" claims |
| P18 | Sandbox bot has no persona; no personal data typed into sandbox (filtered) |

**Target Lumen score:** 23/24.

## 7. AI specification & guardrails

- **AI does:** a **bounded sandbox model** (small model with a fixed knowledge set and deliberately designed failure modes) so kids can experiment safely; a toy image classifier trained on curated sets to show bias; Socratic nudges on explanations; generation of synthetic case media *by staff* offline (never live generation of people).
- **AI does not:** let kids chat with an open frontier model; generate images of real people; store kids' sandbox prompts beyond the session; act as a character or friend.
- **Pedagogy:** inquiry cases aligned to AI4K12 Five Big Ideas (perception, representation & reasoning, learning, natural interaction, societal impact) [M]; lateral reading for media; explain-your-evidence assessment; spaced "case recall" mini-quizzes.
- **Safety:** sandbox input filter blocks personal information (names, addresses, school, photos) and teaches why ("Detectives never give clues about themselves!"); distress escalation for self-report (e.g., if a scam drill triggers a real disclosure: "Someone did this to me") → calm script, tell-a-grown-up button, teacher/parent alert, human review; no emotion recognition; synthetic media labelled with C2PA-style provenance metadata and visible "Case Material" watermarks.
- **Evaluation:** sandbox behaviour tests (designed failures reproducible 100%, no out-of-scope answers); red-team prompts from kids (with consent) and staff; teacher panel review of each case; comprehension pre/post on AI concepts.
- **Cost [E]:** sandbox small-model inference <$0.05 per learner/month; media production is the main cost (≈$3–6k per case) [E].

## 8. Data, privacy & compliance

Class roster (first name/initial), case progress, explanations (text; voice transcribed and discarded), teacher notes. Retention: school year + 60 days for school accounts; account life for family. COPPA 2025 (school authorisation limited to educational use; no commercial use; VPC for family accounts; AI training off); FERPA/SOPIPA DPAs; state student-privacy laws; EU AI Act Art. 50 (synthetic content labelling; disclose AI interactions). Kids category and Families policy. Content: synthetic "persons" in cases are fully fictional; no likeness of real people, voices or brands.

## 9. Monetization & go-to-market

- **Benchmarks:** Common Sense, Be Internet Awesome, Day of AI, Hour of AI free; BrainPOP ≈$129–350/yr for homes.
- **Ours:** free classroom tier (first season); Questwise Family includes all seasons + family nights; microschool licence; district pricing after efficacy evidence.
- **Channels:** classroom teachers (Digital Citizenship Week in October, Hour of AI in December), microschools, homeschool co-ops, ESAs (as part of the bundle), libraries.
- **ASO/SEO:** "AI for kids", "deepfake game for kids", "online safety game", "AI literacy lessons grade 5".
- **Partnership angle:** align case packs to state AI-literacy guidance and EO 14277's Presidential AI Challenge [V].

## 10. Success metrics

- **North-star:** weekly cases solved with correct evidence + explanation (≥1 per active learner).
- **Inputs:** teacher-assigned cases/week; family card completion (self-report ≥30%); sandbox experiments per case.
- **Guardrails:** 0 personal data leaks in sandbox logs; Sensory Comfort ≥4/5; case clarity rating ≥4/5 from teachers.
- **Outcomes:** AI concept assessment gain; transfer task (evaluate a new AI answer or image) at 4 weeks.
- **Retention:** season completion ≥50% of starting classes [E].

## 11. Validation plan

**Riskiest assumptions:**
1. Schools and ESA families prioritise AI literacy enough to adopt a new tool (vision).
2. Kids 9–12 can do meaningful model testing in a bounded sandbox.
3. Deepfake lessons don't increase anxiety.

| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | Classroom paper-case pilot (printed clues, teacher-run "sandbox" via scripted cards) | 3 teachers, ~75 kids | ≥2 of 3 teachers want next 4 cases; adoption intent ≥4/5 | <2/5 intent |
| E2 | Wizard-of-Oz sandbox (staff play the bounded bot) | 12 kids | ≥75% find the designed failure and explain it | <50% |
| E3 | Anxiety check (pictorial worry scale pre/post deepfake case) | 30 kids | No increase in worry; confidence ↑ | Worry ↑ >0.5 pt |
| E4 | Parent survey on family case night | 40 parents | ≥60% would use monthly | <30% |

Mapping: E1 → WP4/WP5; E2, E3 → WP4; E4 → WP2.

## 12. Build handoff

**Epic A: Case engine** — **AC-A1:** Given a case, When a learner pins 2 clues and gives a reason, Then the verdict is evaluated against the rubric and feedback points to the clue to re-examine if incorrect.

**Epic B: Sandbox** — **AC-B1:** Given the sandbox bot, When a learner types their full name or address, Then the input is blocked with a teaching message and not logged. **AC-B2:** Given a designed failure prompt, When asked, Then the bot reproduces the failure consistently.

**Epic C: Media lab** — **AC-C1:** Given a synthetic image, When displayed, Then it carries a visible "Case Material" mark and provenance metadata.

**Epic D: Accessibility** — **AC-D1:** Given any media clue, When VoiceOver is on, Then an equivalent non-visual clue path is available.

**Epic E: Teacher console** — **AC-E1:** Given a class code, When a teacher assigns a case, Then students see it on their board with no peer names visible.

**NFRs:** web-first (Chromebook), iPad, Android; works on school networks (allowlisted domains); WCAG 2.2 AA; EN/ES; sandbox latency <1.5 s.

**QA focus:** AT matrix incl. captions/transcripts; sensory A/B (suspense audio); AI cases (sandbox scope, PII filter, jailbreak attempts, no real-person generation); COPPA/FERPA (school-authorised data scope, deletion at year end); billing (classroom tier never shows parent upsells to kids).

**Platform dependencies:** Lumen, My Needs, AI orchestration (bounded model hosting, PII filter), privacy stack, evidence engine, Guild Hub educator console.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Free incumbents (Common Sense, Google) own the classroom | High | Medium | Complement them (map to their pillars); win on hands-on + continuity |
| Media production cost per case | High | Medium | Reusable case templates; seasonal cadence |
| Content dates fast as AI changes | High | Medium | Quarterly review; principles over product specifics |
| Deepfake material misused | Low | High | Watermarks; no export of synthetic media |

**Open questions:** Should AI Detectives be free forever as the brand funnel? Which state standards to map first? ASL budget?

## 14. Sources
- [V] EO 14277 text: https://www.presidency.ucsb.edu/documents/executive-order-14277-advancing-artificial-intelligence-education-for-american-youth · https://en.wikisource.org/wiki/Executive_Order_14277
- [V2] Be Internet Awesome AI Literacy Guide (June 2025): https://services.google.com/fh/files/misc/be_internet_awesome_ai_literacy_guide.pdf · https://beinternetawesome.withgoogle.com/en_us
- [V2] Google AI literacy reach (AI4K12 13M, Experience AI 2M): https://services.google.com/fh/files/misc/google_ai_literacy_skills_training_for_education.pdf
- [V2] Common Sense digital citizenship (70% of schools, 165+ lessons, AI lessons grades 6–12): https://www.commonsense.org/education/digital-citizenship · https://library.wyo.gov/common-sense-education-offers-free-ai-literacy-and-digital-citizenship-lessons-and-resources/
- [V] Code.org Hour of AI: https://thejournal.com/articles/2025/10/02/codeorg-reinvents-hour-of-code-as-hour-of-ai.aspx · https://www.prnewswire.com/news-releases/hour-of-ai-unveils-100-free-activities-to-help-demystify-ai-for-educators-families-and-kids-302612434.html
- [V2] Day of AI: https://dayofai.org/curriculum-resources · https://www.edtechinnovationhub.com/news/day-of-ai-and-mit-raise-launch-national-ai-literacy-push-for-us-schools
- [V2] BrainPOP pricing: https://homeschoolbuyersclub.com/products/brainpop-family-access-2 · https://learnspark.io/blog/homeschooling-curriculum-brainpop-price-review-2026/
- [V2] Nearpod media literacy: https://nearpod.com/blog/media-literacy-fake-news/
- [V2] Gemini under-13 access: https://www.qustodio.com/en/blog/is-google-gemini-safe/
- [M] AI4K12 Five Big Ideas; Interland release year; BrainPOP AI topics

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Merge → age 9–12 edition of EN-06 Safety, Scam, AI & Media Literacy engine |
| **Ships in** | Questwise app (S2) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 73/100 [I] |
| **Consumes engines** | EN-06 |
| **Studio features used** | SX-18, SX-32 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = AD-01, AD-02, AD-03, AD-04.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| AD-E1 | **Teach-your-grandparent missions** | Kids walk a grandparent through a scam case that pairs with Silver Circuit's Scam Gym (SX-18). |
| AD-E2 | **Free classroom edition** | A brand-building distribution channel for Questwise. |

### 15.3 New validation question
Intergenerational mission completion with ≥10 families; teacher adoption intent ≥4/5.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 3 | 4 | 3 | 3 | 4 | 4 | 5 |

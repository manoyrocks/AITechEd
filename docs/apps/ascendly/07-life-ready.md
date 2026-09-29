# Life Ready: App Strategy & Product Specification

> **Venture:** Ascendly · **App #:** 7/7 · **Ages:** 13–19 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/03-ascendly-teens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research caveat (important):** The shared session web-search budget ran out before this app's competitor research, and WebFetch was blocked. Duolingo figures come from the studio's raw files ([V2]); other competitor facts are from memory ([M]) and **must be verified in Discovery WP1**. No competitor numbers have been invented; unknown figures are marked "verify".

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Short, real-life challenges — your first paycheck, a scam text, a viral AI claim, a local election — that build the money, AI, media and civic skills school often skips. |
| **Primary user / buyer** | Teens 13–19 (users). Teachers of personal finance, civics, digital citizenship and advisory (assign). Schools/districts (licence, where personal-finance graduation requirements exist). Credit unions/community partners (sponsors, later). |
| **Core job-to-be-done** | "When real-life stuff shows up — a paycheck with deductions, a too-good offer, a video that might be AI — I want to know what to do, so I don't get scammed, fooled or stuck." |
| **Category on the stores** | Education (13+). |
| **Top competitors** | Greenlight, Step, Zogo, Next Gen Personal Finance (NGPF), Ramsey (Foundations), Khan Academy financial literacy, Common Sense Education (digital citizenship / AI literacy), News Literacy Project Checkology, iCivics; Duolingo as UX benchmark |
| **Our wedge** | 1. **Scenario practice, not lectures or a bank card:** decisions with consequences in a safe sandbox, across four literacies (money, AI, media, civic) in one place. 2. **AI literacy by doing:** teens test AI claims, spot synthetic media and practise verifying — a gap in finance-only apps and in older curricula [I]. 3. **Duolingo-grade polish without Duolingo's punishments:** short, delightful, calm by default; no hearts, energy or streak loss. 4. **Accessible and plain-language** for teens with disabilities, English learners and those reading below grade level. |
| **Business model** | Free for teens. School licence $3–8/student/yr [E] (teacher dashboard, standards alignment, reporting). Ascendly Plus includes extras (friend challenges, real-world task tracker). Sponsor-funded modules from mission-aligned nonprofits/credit unions later (no product promotion). |
| **North-star metric** | Weekly "real-world moves": verified-by-self actions taken after a challenge (e.g., set up a budget, checked a claim with lateral reading, registered to vote at 18, turned on 2FA), per active teen. |
| **MVP candidate?** | **Later** — the riskiest assumption is engagement without a school requirement; test organic pull first. |

## 2. Problem & users

**Problem statement.** Teens face adult decisions early — first jobs, digital payments, targeted scams, AI-generated media, first elections — often without instruction. Many US states have adopted personal-finance graduation requirements in recent years, creating school demand for curricula [M: NGPF tracks this; verify count in WP1]. AI adds a new literacy: about 72% of US teens have tried AI companions (Common Sense Media, 2025) [M: raw 05], and just over half have used chatbots for schoolwork [V2: Pew Feb 2026]. Existing products split the space: teen banking apps (Greenlight, Step) teach by giving a card; nonprofit curricula (NGPF, Checkology, iCivics, Common Sense) are excellent but classroom-bound and rarely mobile-first [M]; gamified apps (Zogo) pay rewards for quizzes [M]. Duolingo shows how to build a daily-learning habit (178M downloads in 2025; 58.7M DAU in Q2 2026 [V2: research paper]) and also how punishment backfires (the Energy system: "So now we're punished for using the app?") [V2: raw 03].

**Personas**
| Persona | Snapshot | Needs |
|---|---|---|
| **Jaylen, 16, first job** | Confused by his first paycheck; gets "you won a prize" texts. | Short, practical scenarios; plain numbers. |
| **Sofia, 14, heavy TikTok user** | Shares viral clips; can't tell AI images from real. | Fast verification skills that feel smart, not preachy. |
| **Ben, 17, intellectual disability, reads at grade 3** | Wants independence; school materials are too dense. | Plain language, audio, pictures, age-respectful tone. |
| **Mr. Alvarez, personal-finance teacher** | Must deliver a required semester course. | Standards-aligned, ready-to-assign modules with reporting. |
| **Parent** | Wants their teen scam-safe and money-smart without another bank app. | No ads, no financial product selling, visible learning. |

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Practical money skills | State requirements [M]; teen banking app popularity [M] | Paycheck, budget, credit, borrowing, investing basics scenarios |
| Scam resistance | Scams target young people online [M: FTC Consumer Sentinel — verify figures] | Realistic simulated scam messages in a sandbox, safe-fail |
| AI and media literacy | Teen AI use [V2/M]; synthetic media spread [I] | "Is this real?" labs; lateral reading; AI claim checks |
| Civic skills | iCivics/Checkology demand [M] | Local-government and voting scenarios (non-partisan) |
| Engagement without manipulation | Duolingo Energy backlash [V2] | Short challenges, gentle weekly goals, friend challenges without leaderboards |
| Accessibility | Lumen; Ben persona | Reading-level dial, audio, pictures, captions |

## 3. Competitive feature benchmark

| App | Publisher | Scale / grossing signal | Price | Rating | Loved | Complaints | A11y / sensory | Source |
|---|---|---|---|---|---|---|---|---|
| **Greenlight** | Greenlight Financial Technology | Large US family debit-card app [M]; scale: verify | Family plans monthly (roughly $5–15+/mo tiers) [M: verify] | High on stores [M] | Parent-controlled card, chores/allowance, savings, investing for kids [M] | Monthly fees; support issues [M] | Standard fintech UI [M] | [M] |
| **Step** | Step | Teen banking + secured credit-building card [M]; scale: verify | Free core [M] | High [M] | Build credit as a teen, no fee [M] | Fintech-partner changes; support [M] | Standard [M] | [M] |
| **Zogo** | Zogo | Financial-literacy app distributed via banks/credit unions [M] | Free (B2B2C) [M] | High [M] | Short modules, rewards/gift cards [M] | Reward-driven "farm the quiz" behaviour [I] | Standard [M] | [M] |
| **NGPF** | Next Gen Personal Finance (nonprofit) | Widely used free personal-finance curriculum for US high schools [M] | Free | n/a | High-quality lessons, arcade games, teacher PD [M] | Web/classroom-bound [I] | Web [M] | [M] |
| **Ramsey (Foundations in Personal Finance)** | Ramsey Solutions | Established HS curriculum [M] | School pricing [M] | n/a | Structured, video-led [M] | Debt-avoidance ideology; one viewpoint [M/I] | Video captions [M] | [M] |
| **Checkology** | News Literacy Project (nonprofit) | Free news-literacy platform for educators [M] | Free | n/a | Real examples, misinformation lessons [M] | Classroom-bound; web [I] | Web [M] | [M] |
| **iCivics** | iCivics (nonprofit, founded by Sandra Day O'Connor) [M] | Widely used civics games in US schools [M] | Free | n/a | Games like "Win the White House" [M] | Younger-feeling for older teens [I] | Web [M] | [M] |
| **Duolingo (UX benchmark)** | Duolingo | 500M+ Play; 178M downloads 2025; 58.7M DAU Q2 2026 [V2] | Free + Super/Max | 4.7 [V2] | 3–5 minute lessons, polish, habit loop [V2] | Energy system, streak burnout, "AI slop" backlash [V2] | VoiceOver inconsistent; high sensory celebrations [V2: catalog] | research paper; raw 03 |

**Also:** Khan Academy financial literacy course (free, high-quality, video + exercises) [M]; Common Sense Education digital citizenship and AI literacy lessons (free) [M].

**Feature matrix**

| Feature | Greenlight | Step | Zogo | NGPF | Checkology | iCivics | Duolingo | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Real money account/card | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject** (we teach; we don't sell financial products) |
| Scenario/simulation practice | ◐ | ✗ | ◐ | ✓ | ✓ | ✓ | ◐ | **Differentiate** (mobile-first, four literacies) |
| Short daily lessons (≤5 min) | ✗ | ✗ | ✓ | ◐ | ✗ | ◐ | ✓ | **Parity** |
| AI literacy (claims, synthetic media) | ✗ | ✗ | ✗ | ◐ | ◐ | ✗ | ✗ | **Differentiate** |
| Scam sandbox | ◐ | ◐ | ◐ | ◐ | ◐ | ✗ | ✗ | **Differentiate** |
| Cash/gift-card rewards for completing | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | **Reject** (extrinsic farming, sponsor influence) |
| Hearts/energy limits | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Reject** |
| Streak with loss / leagues | ✗ | ✗ | ◐ | ✗ | ✗ | ✗ | ✓ | **Reject**; gentle weekly goals, no leagues |
| Friend challenges | ✗ | ✗ | ◐ | ✗ | ✗ | ◐ | ✓ | **Improve**: cooperative "team solves" and invite-a-friend challenges, no rankings |
| Teacher dashboard & standards alignment | ✗ | ✗ | ◐ | ✓ | ✓ | ✓ | ✗ (Duolingo for Schools ◐) | **Parity** |
| Real-world task tracker | ◐ (chores) | ✗ | ✗ | ◐ | ✗ | ✗ | ✗ | **Differentiate** |
| Non-partisan civic content review | n/a | n/a | n/a | n/a | ✓ | ✓ | n/a | **Parity** (bipartisan review panel) |
| Reading-level dial + audio | ✗ | ✗ | ✗ | ◐ | ◐ | ◐ | ◐ | **Differentiate** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| LR-01 | **Scenario challenges (3–7 min)** ★ | Branching real-life scenarios with consequences and feedback: "Your first paycheck", "Rent vs roommate", "BNPL at checkout", "Your first credit card offer". | Vision; NGPF/iCivics parity mobile-first | Differentiate | MVP | Must |
| LR-02 | **Scam sandbox** ★ | Simulated texts, DMs, emails and calls (text transcript) in a safe fake inbox; teen decides; feedback shows the red flags. Includes AI voice-clone and deepfake scams. | Scam need | Differentiate | MVP | Must |
| LR-03 | **"Is this real?" AI & media lab** ★ | Examine images, clips, AI claims and headlines; practise lateral reading, reverse search reasoning and source checks; learn how generative AI works and fails. | AI literacy gap | Differentiate | MVP | Must |
| LR-04 | **Civic scenarios** | Non-partisan local-government, voting-process, jury, and community-action scenarios; reviewed by a bipartisan panel. | iCivics parity | Parity | MVP | Should |
| LR-05 | **Money tools (practice only)** | Budget builder, paycheck decoder, compound-interest and loan calculators — sandbox, no account linking. | Practical | Improve | MVP | Must |
| LR-06 | **Real-world moves tracker** | After a challenge, optional action ("turn on 2FA", "check your pay stub"); teen self-reports; no data verification. | North star | Differentiate | MVP | Must |
| LR-07 | **Gentle weekly goal** | Choose 1–5 challenges per week; pause weeks; no streak loss. | Duolingo lesson learned | Lumen | MVP | Must |
| LR-08 | **Friend challenges (cooperative)** | Send a scenario to a friend; compare choices privately afterward; "team solve" mode. No leaderboards. | Vision; social pull | Improve | MVP | Should |
| LR-09 | **Plain-language & audio mode** | Reading-level dial (grade 3–10), full narration, icon support, glossary. | Ben persona | Lumen | MVP | Must |
| LR-10 | **Teacher assign + standards map** | Map to state personal-finance standards and national frameworks (e.g., Jump$tart, C3) [M]; assign modules; completion + mastery view. | School channel | Parity | MVP | Should |
| LR-11 | Record badges with evidence | Skills evidence (e.g., "Spotted 10/10 scam patterns") saved to Ascendly Record; teen chooses sharing. | Shared layer | Differentiate | V1 | Should |
| LR-12 | Seasonal "live" scenarios | Timely modules (tax season, election season, back-to-school scams), human-reviewed. | Relevance | Improve | V1 | Should |
| LR-13 | Short-form creator kit | Teens make 30-second explainer clips from scenarios (privacy-safe templates) to share. | Organic distribution test | Differentiate | V1 | Could |
| LR-14 | Family mode | Parent–teen conversation cards after money scenarios (co-play). | Lumen P14 | Lumen | V2 | Could |
| LR-15 | Localisation (UK/other) | Local tax, benefits and civic systems. | Expansion | Parity | V2 | Could |

★ = signature. **Signature: scenario challenges with a scam sandbox and an "Is this real?" AI & media lab.** MVP = 10 features.

## 5. Core experience & key user flows

**Core loop:** open → pick a challenge (or friend's) → scenario decisions → consequences + why → optional real-world move → weekly goal progress → natural end.

**Flow 1: Onboarding (≤5 min)** — age check (13+) → Dial and reading level → choose interests (Money · AI & Media · Scams · Civic) → first 3-minute challenge ("Is this text from your bank?").

**Flow 2: Core challenge — "Your first paycheck"**
1. Scenario: $480 gross; stub shows deductions. Teen answers "Why is it $402?" with choices or typed.
2. Feedback explains taxes/FICA in plain language with a visual.
3. Decision: spend/save split; consequence shown one month later.
4. Real-world move: "Want a checklist for reading your own pay stub?" Save.
5. End: "Challenge done. 2 of 3 this week."

**Flow 3: Scam sandbox** — fake inbox with 5 messages; teen flags, replies or ignores; a "trap" reply shows what would happen, with no shame; red-flag recap; tip card for real life.

**Flow 4: Teacher** — assign "Scams unit"; class view of completion and common misses; printable/offline versions.

**Flow 5: My Needs** — reading level, narration, Dial, input modes, content notes for sensitive topics.

**Flow 6: Billing** — free for teens; Plus extras through the fair-billing charter; schools licence.

**IA:** Today · Explore (4 literacies) · Friends · My Moves · My Needs.

**Session design:** 3–7 minutes per challenge; weekly (not daily) goals; "That's a good place to stop" after 3 challenges.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial:** Calm — static illustrations, no sound, consequences shown as text + simple charts; Balanced (default) — gentle transitions, optional soft sounds; Lively — animated consequences, optional celebration (skippable), never flashing.

**Input modes:** tap choices, typed answers, voice, keyboard, switch scanning, AAC text; no drag (sorting tasks use buttons); no timers.

**Reading and typography:** reading-level dial grade 3–10 changes wording, not concepts, with age-respectful tone; narration of everything; glossary; BDA defaults; numbers shown with visual aids and read aloud clearly (currency, percentages).

**Media accessibility:** "Is this real?" items include audio descriptions and non-visual verification tasks (source/metadata/context reasoning) so blind teens get an equivalent challenge; video clips captioned; no seizure-risk media.

**Cognitive accessibility:** one decision per screen; consequences explained concretely; "undo my choice" to explore alternatives; money amounts kept small and realistic.

**Age-respectful themes:** Street (photo), Minimal, High Contrast; no cartoon mascots.

**Lumen principles**
| # | Acceptance criterion |
|---|---|
| P1 | Calm respects Reduce Motion (0 non-essential animation) |
| P2 | Scam "call" scenarios provided as transcript + optional audio; no sound-only cues |
| P3 | Every challenge: Setup → Decide → Consequence → Why → Move |
| P4 | No drag; single-tap completion |
| P5 | Copy at profile reading level; literal language (idioms explained) |
| P6 | BDA defaults |
| P7 | ≥2 input modes per decision |
| P8 | Wrong choices are explored, not punished; undo available |
| P9 | Weekly goal; natural stop after 3 challenges |
| P10 | Scenario facts visible while deciding |
| P11 | No timers |
| P12 | Accessibility free |
| P13 | Mature themes at every reading level |
| P14 | Teacher assigns a unit in ≤5 min |
| P15 | No streak loss, no leagues, no cash rewards |
| P16 | Content reviewed by ND/disability panel and a bipartisan civics panel |
| P17 | No "prevents scams" claims; evidence tier stated |
| P18 | No real account linking; no ads; no financial product promotion |

**Target Lumen score:** ≥22/24.

## 7. AI specification & guardrails

**AI does:** generate scenario *variations* inside human-authored templates (names, amounts, platforms); give feedback on open answers against a rubric; create synthetic scam and media examples for training in the sandbox (clearly watermarked "training example"); answer "why" questions with cited sources.

**AI does not:** give personalised financial, legal or tax advice; recommend financial products; take political positions or generate persuasive political content; produce deepfakes of real people (all synthetic media uses fictional people); act as a companion.

**Content governance:** all modules human-authored and reviewed (finance educator + accessibility reviewer; civics adds a bipartisan reviewer pair); AI variants spot-checked (≥5%) and constrained to template facts; election content locked (no AI generation) and reviewed each cycle.

**Safety:** scam sandbox never uses real brands' logos in a way that could be lifted as a phishing kit [I]; no links out of sandbox messages; AI disclosure; distress routing if a teen discloses real scam victimisation or financial abuse (resources: FTC ReportFraud, trusted adult) [M]; no emotion inference.

**Evaluation:** factual accuracy 100% on a fixed item set reviewed by experts; political-neutrality audit (bipartisan raters find no slant); synthetic-media examples never resemble real individuals (review); feedback rubric agreement with teachers ≥80%.

**Cost [E]:** low (~$0.005–0.02 per challenge); authoring ~$1–3K per challenge including review [E].

## 8. Data, privacy & compliance

| Data | Why | Retention | Where |
|---|---|---|---|
| Challenge choices | Feedback, progress | Account lifetime; deletable | Cloud |
| Real-world moves (self-report) | North star | Teen-owned | Cloud |
| Friend links | Challenges | Until removed | Cloud |
| No financial account data | — | — | Not collected |

**Regimes:** COPPA (13+); FERPA/SOPIPA for schools; UK AADC; state design codes; KOSA-ready; FTC §5 and endorsement rules (no undisclosed sponsor content); state election-law sensitivities (non-partisan, no voter targeting); GLBA not applicable because no financial accounts [I]; EU AI Act Art. 50 labelling for synthetic media used in training examples.

**Consent:** teen consent; sponsor modules labelled; no data shared with sponsors beyond aggregates.

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Teen | Free | All core challenges, sandbox, lab, tools |
| Plus | Ascendly Plus ($12/mo or $79/yr) | Friend team-solves, seasonal packs early, Record export extras |
| School | $3–8/student/yr [E] | Assign, standards map, reporting, offline packs |
| Sponsored modules | Grant/sponsor funded [E] | Mission-aligned nonprofits/credit unions fund modules; no product promotion |

Benchmarks: NGPF, Checkology, iCivics, Khan Academy free [M]; Greenlight/Step monetise via accounts [M]; Zogo via financial institutions [M]. Free for teens is table stakes.

**Channels:** short-form content test (scam "spot the red flag" clips); personal-finance and civics teacher communities; state requirement implementation offices; libraries; credit unions' youth programs. **ASO:** "scam test", "money skills for teens", "is this AI", "first paycheck". Accessibility Nutrition Label.

**Markets:** US first; UK/Canada V2 (localised systems).

## 10. Success metrics
- **North star:** weekly real-world moves per active teen (target ≥1).
- **Inputs:** challenges per week (≥3); friend challenges sent per active teen (≥0.5/week); scam-sandbox completion (≥70%).
- **Guardrails:** Sensory Comfort ≥4/5; political-neutrality audit pass; zero financial-product promotion; no increase in anxiety about money (pulse check).
- **Outcomes:** pre/post scam-detection accuracy on a held-out set; lateral-reading task success; financial-knowledge scale (e.g., adapted from national surveys) — ESSA Tier 3 → 2.
- **Retention:** D7 ≥20% (organic), DAU/MAU ≥15% organic; ≥25% when school-assigned.

## 11. Validation plan (no-code)

**Riskiest assumptions**
1. Teens will engage without a school requirement (vision).
2. Scenario format beats video/quiz for real-world transfer.
3. Schools prefer a mobile-first multi-literacy tool over free nonprofit curricula.

**Experiments**
| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | **TikTok/Shorts content test** — 12 "spot the scam / is this AI?" clips posted organically from a studio account (adult-run, no targeting of minors), linking to a waitlist | ~4 weeks | ≥2% profile-visit → waitlist; saves/shares above account median | <0.5% |
| E2 | Paper/Figma scenario test vs a short explainer video | 30 teens | Transfer task success +15 points for scenarios | No difference |
| E3 | School elective interest survey | 20 PF/civics teachers | ≥8 would assign; ≥3 would pay | <3 would assign |
| E4 | Plain-language accessibility round | 8 teens incl. intellectual disability, dyslexia, ELL | Task success ≥85%; comfort ≥4/5 | — |
| E5 | Scam-sandbox safety review | Security + child-safety reviewers | No reusable phishing assets; content notes adequate | — |

**Mapping:** WP1 (verify all [M] competitor facts; state requirements count), WP2 (teen interviews on money/AI/scams), WP4 (E2, E4, E5), WP5 (E1 CAC/organic probe, E3).

## 12. Build handoff

**Epic A: Scenarios**
- Given a branching scenario, When the teen chooses, Then the consequence and a plain explanation appear, And "undo" lets them explore another choice without penalty.

**Epic B: Scam sandbox**
- Given the sandbox inbox, When the teen taps a link in a message, Then no network request occurs and a training explanation appears.

**Epic C: AI & media lab**
- Given a blind teen, When an image item appears, Then an equivalent non-visual verification task is offered.

**Epic D: Weekly goal**
- Given a missed week, Then the goal resets quietly with no loss message.

**Epic E: Teacher**
- Given a class, When assigning a unit, Then standards alignment is shown and completion reports are exportable.

**NFRs:** fully offline challenge packs; iOS/Android/web; WCAG 2.2 AA; content versioning with review sign-off; English + Spanish V1.

**QA focus:** AT matrix; reading-level dial correctness; political-neutrality review; sandbox isolation (no outbound links); sensory A/B; friend-challenge abuse (spam, harassment) and moderation.

**Platform dependencies:** Lumen; My Needs; AI orchestration (template variation, rubric feedback); moderation (shared with Study Squad); Ascendly Record; teacher console.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Low organic engagement | High | High | E1 gate; school channel; friend challenges |
| Free nonprofit curricula "good enough" | High | Medium | Partner rather than compete (link NGPF/Checkology lessons) |
| Political controversy | Medium | High | Bipartisan review; process-focused civic content |
| Scam content misused | Low | Medium | Sandbox isolation; fictional brands |
| Content staleness (tax rules, platforms) | Medium | Medium | Annual review cycle; seasonal packs |

**Open questions:** Partner with NGPF/News Literacy Project or build original content? Should Life Ready merge into Study Coach/Pathfinder as modules rather than a stand-alone app? What counts as a "real-world move" without surveillance?

## 14. Sources
- Duolingo downloads/DAU and Energy backlash — docs/01-research-paper.md; research/raw/03-forum-voice-of-customer.md [V2]
- Pew teen AI use (Feb 2026) — https://www.pewresearch.org/internet/2026/02/24/how-teens-use-and-view-ai/ [V2]
- Common Sense AI companions stat — research/raw/05-market-and-trends.md [M]
- EU AI Act Art. 50 — docs/01-research-paper.md §8 [V2]
- Greenlight, Step, Zogo, NGPF, Ramsey, Checkology, iCivics, Khan Academy financial literacy, Common Sense Education — from memory [M]; **verify in WP1** (vendor sites, store pages, NGPF state-requirement tracker, FTC Consumer Sentinel data)

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Merge → teen edition of EN-06 Safety, Scam, AI & Media Literacy engine |
| **Ships in** | Ascendly app (S3) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 60/100 [I] |
| **Consumes engines** | EN-06 |
| **Studio features used** | SX-18 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = LR-01, LR-02, LR-03.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| LR-E1 | **Teach-a-grandparent missions** | Teens coach a grandparent through Silver Circuit Scam Gym cases (SX-18). |
| LR-E2 | **Live scam season** | Timely scenarios based on current scam patterns, reviewed by humans before release (LR-12 promoted). |

### 15.3 New validation question
Organic pull: short-form content test plus school elective interest.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 3 | 2 | 4 | 3 | 2 | 4 | 3 | 4 |

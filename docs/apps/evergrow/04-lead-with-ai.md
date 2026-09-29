# Lead with AI: App Strategy & Product Specification

> **Venture:** Evergrow · **App #:** 4/7 · **Ages:** 35–59 (people managers, team leads, HR business partners) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/04-evergrow-adults.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Evergrow index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research note:** Searched 29 Sep 2026. Page fetches were blocked by the egress proxy, so [V] means the fact appeared in search results attributed to the primary source.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Rehearse the hard moments of leading an AI rollout (the sceptical team, the data-leak incident, the reskilling decision) in branching simulations with a debrief coach and a peer cohort, then take a ready playbook back to your team. |
| **Primary user / buyer** | User: first-line and middle managers (35–59) whose teams are adopting AI. Buyer: L&D or HR leadership, often the same buyer as AI Fluency Lab; the CIO/transformation office as co-sponsor. |
| **Core job-to-be-done** | "When leadership tells me to 'drive AI adoption' and my team is anxious, I want to practise the conversations and decisions before I face them for real, so I can lead the change without losing trust or making an unsafe call." |
| **Category on the stores** | Business › Leadership development (web-first; mobile for micro-practice) |
| **Top competitors (by downloads / revenue)** | LinkedIn Learning, Harvard ManageMentor (Harvard Business Publishing), BetterUp, Coursera for Business, Section, Mursion, Skillsoft Percipio (CAISY), Yoodli; Headway / Blinkist / Imprint as consumer micro-learning benchmarks |
| **Our wedge** | 1) **AI-change-specific simulations** (not generic "difficult conversations"). 2) **Built on the team's real skills data** from AI Fluency Lab, aggregate only, never individual surveillance. 3) Priced for mid-market managers at a fraction of human coaching. |
| **Business model** | B2B add-on to AI Fluency Lab ($120–180 per manager per year) or stand-alone ($250–350). Cohort programmes $600–900 per manager. |
| **North-star metric** | Team AI actions launched per active manager per quarter (e.g., a team AI charter adopted, a workflow piloted), with the team's verified skills rising |
| **MVP candidate?** | **Later (Year 2);** Pricing interviews run in discovery. Could ship as the "Managers" track inside AI Fluency Lab first. |

## 2. Problem & users
**Problem statement**
- Managers are the adoption bottleneck. Gallup's 2026 research finds manager-led adoption is one of the top two drivers of frequent AI use [V].
  - Only 36% of employees in AI-integrating organisations strongly agree their manager supports the team's AI use (May 2026) [V].
  - Employees who do strongly agree are 8.7× as likely to say AI has transformed how work gets done [V].
- Managers get generic content. LinkedIn Learning, Coursera and Skillsoft have large catalogues, but leadership-for-AI scenarios are thin. Workers report no time to learn: 56% in Workera's 2026 study [V].
- **Practice-based simulation is growing, but it is expensive or generic:**
  - Skillsoft's AI simulator CAISY grew learners 146% year on year while total Skillsoft revenue fell 2.3% in Q4 FY2026 [V].
  - Mursion has delivered 800K+ simulations and says it targets 2M a year [V2].
  - Yoodli raised $40M for AI roleplays [V].
  - Human coaching (BetterUp) is estimated at ~$3,000–5,000 per user per year [V2], so it is out of reach for most mid-level managers.
- L&D budgets are tight. Coursera's enterprise NRR fell to 91% because of budget pressure [V]. **A stand-alone manager product must prove value or ride along with a bundle** [I].

**Personas**
1. **Rahul, 45, engineering manager** (vision). He must roll out a coding assistant to 12 engineers, two of whom fear job loss, and he needs to decide on usage policy. He wants realistic practice, a policy template and peers facing the same thing.
2. **Denise, 52, nursing unit manager who is Deaf and uses captions and text.** She has no time and a 24/7 unit. Voice-only roleplays and live video workshops exclude her. She needs text-mode simulations, captioned cohorts and asynchronous participation.
3. **Omar, 39, HR business partner (buyer/facilitator).** He runs manager development for 300 managers. He needs cohorts he can run with light facilitation, aggregate insight and **assurance that the tool is not a manager-surveillance device** (works councils in the EU).

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Practise high-stakes AI change conversations | Gallup [V]; CAISY growth [V] | Branching simulations with AI role-play characters |
| Decision practice (policy, ethics, workforce) | Vision: ethics incident and reskilling | Decision simulations with consequences and a debrief |
| Peers facing the same change | Cohort completion benefits [M] (repo) | 6-week peer cohorts |
| Playbooks, not theory | Headway/Imprint micro-formats [V2] | Playbook templates (AI charter, pilot plan, comms) |
| Time-efficient | Workera 56% no time [V] | 10–15 min sims; asynchronous cohorts |
| Accessible practice | Lumen P7 | Text or voice; captions; no timed responses |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **LinkedIn Learning** | Microsoft | 20,000+ courses [V2] | $239.88/yr individual; Teams $379.88/seat/yr [V2] | n/a | Broad catalogue incl. GenAI leadership courses; profile integration | Passive video; certificate value doubts [V2] (repo) | Captions | [trainingcost.com](https://trainingcost.com/linkedin-learning-pricing) |
| **Harvard ManageMentor** | Harvard Business Publishing | Long-standing enterprise manager-curriculum brand [M] | Enterprise quote [M] | n/a | HBR authority; management topics | Text-heavy; little practice [M] | Web; standard [M] | [M] |
| **BetterUp** | BetterUp | Large enterprise coaching platform [M] | Est. ~$3,000–5,000 per user per year; not published [V2] | G2 4.5 (competitor-cited) [V2] | Human coaches; AI coach add-on [M] | Cost; access limited to senior staff [V2] | Video/phone sessions; depends on coach | [risely pricing guide](https://risely.me/compare/pricing-guide/) |
| **Skillsoft Percipio + CAISY** | Skillsoft | Q4 FY2026 revenue $130.7M (−2.3%); CAISY learners +146% YoY [V] | Enterprise [M] | n/a | AI conversation simulator for coaching, change management, feedback [V]; in Microsoft Viva Learning [V] | Legacy catalogue; revenue decline [V] | Voice and text [M] | [Skillsoft 8-K](https://www.sec.gov/Archives/edgar/data/1774675/000143774926011599/ex_898416.htm), [MS Learn](https://learn.microsoft.com/en-us/viva/learning/learning-agent-roleplay-skillsoft) |
| **Mursion** | Mursion | 800K+ simulations; $40.6M raised [V2] | Enterprise [M] | n/a | Realistic avatar sims with human "simulation specialists" + AI [V] | Cost; scheduling [I] | Avatar/voice-centric [I] | [mursion.com](https://www.mursion.com/) |
| **Section** | Section | Mid-market AI proficiency [V] | $750 per seat (small teams) [V] | n/a | Practical AI strategy for leaders | Price; live timing | Live video | [sectionai.com/pricing](https://www.sectionai.com/pricing) |
| **Coursera for Business** | Coursera | 12,107 enterprise customers; NRR 91% [V] | Enterprise | 4.3–4.7 (repo) | University brands; GenAI for leaders courses | Passive; completion | Captions | [Coursera IR](https://investor.coursera.com/news/news-details/2026/Coursera-Reports-Second-Quarter-2026-Financial-Results/default.aspx) |
| **Headway / Blinkist / Imprint** (consumer micro-learning) | Headway; Blinkist; Polywise | Headway 50M+ lifetime, #1 US Education Jan 2025 (repo); Imprint 5M+ downloads [V2] | Headway $89.99/yr (repo); Blinkist Premium $99.99/yr, Pro $174.99/yr with Blinkist AI [V2]; Imprint $124.99/yr [V2] | 4.6–4.7 (repo) | 10-min formats; visual summaries; audio | Trial-to-annual surprises (repo); shallow | Audio versions help (repo) | [Blinkist pricing](https://www.shortform.com/blog/hub/product/blinkist-pricing/), [Imprint](https://mwm.ai/apps/imprint-visual-micro-learning/1482780647) |

### Feature matrix
| Feature | LinkedIn L. | HMM | BetterUp | Skillsoft CAISY | Mursion | Section | Blinkist/Imprint | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| AI-change-specific scenarios | partial | ✗ | partial | partial | partial | ✓ | ✗ | **Differentiate** |
| Branching decision simulations with consequences | ✗ | ✗ | ✗ | partial | ✓ | ✗ | ✗ | **Differentiate** |
| AI role-play conversation practice | partial | ✗ | partial | ✓ | ✓ | ✗ | ✗ | **Parity** |
| Text-mode equivalent for role-plays | ✗ | n/a | partial | partial | ✗ | n/a | n/a | **Differentiate (Lumen)** |
| Human coaching | ✗ | ✗ | ✓ | ✗ | ✓ (specialists) | ✓ (live) | ✗ | **Improve:** cohort facilitators, not 1:1 |
| Peer cohorts | ✗ | ✗ | partial | ✗ | ✗ | ✓ | ✗ | **Parity** |
| Playbook templates | partial | partial | ✗ | ✗ | ✗ | ✓ | ✗ | **Parity+** |
| Micro-format (10 min) | ✓ | partial | ✗ | ✓ | ✗ | ✗ | ✓ | **Parity** |
| Voice/face "emotion" or sentiment scoring | ✗ | ✗ | ✗ | partial [M] | partial [M] | ✗ | ✗ | **Reject:** EU AI Act Art. 5 bans emotion recognition in the workplace |
| Individual employee monitoring for managers | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject** (and contractually prohibited) |
| Trial-to-annual auto-conversion without reminder | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | partial (repo) | **Reject** |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| F1 | **Change Room simulations** ★ signature | 12 branching scenarios at launch, e.g. "The sceptical senior engineer", "Someone pasted patient data into a chatbot", "Budget says cut 2 roles, or reskill?", "Your team's AI output was wrong and a client noticed". Characters are AI role-play (labelled); decisions branch into consequences over 3–5 "weeks". | Mursion/CAISY show demand [V]; AI-specific gap | Differentiate | MVP | Must |
| F2 | **Debrief coach** | After each sim, a structured debrief: what happened, which principle applied, what you might try, links to the playbook. Rubric is transparent. | Practice + reflection | Parity+ | MVP | Must |
| F3 | **Speak-or-type role-play** | Every conversation can be voice or text; the learner can switch mid-sim; captions on all AI speech | Denise persona | Lumen | MVP | Must |
| F4 | **Playbook library** | Editable templates: team AI charter, pilot plan, risk checklist (privacy, bias, verification), comms scripts, reskilling conversation guide. Human-authored, reviewed by legal/HR advisers. | Section parity [V] | Parity | MVP | Must |
| F5 | **Peer cohorts** | 6-week cohorts of 8–12 managers: asynchronous threads, two optional 45-min captioned live sessions, facilitator | Cohort completion (repo) | Parity | MVP | Must |
| F6 | **Team Readiness view (aggregate)** ★ | If the org uses AI Fluency Lab: team-level skills coverage (k≥5), never individual; suggestions like "3 of your team's roles have no verification skill yet" | Integration drives adoption [V] | Differentiate | MVP | Should |
| F7 | **10-minute "moments"** | Micro-practice for a single conversation opener (for example "announce the pilot") on mobile | Micro-learning parity [V2] | Parity | MVP | Must |
| F8 | **Responsible AI decisions pack** | Sims on the EU AI Act Art. 4 duty, data protection, bias incidents and transparency to staff | Compliance-adjacent value [V2] | Differentiate | MVP | Must |
| F9 | **My Needs + accessibility** | Text-first option, captions, screen-reader-navigable branching (a list view of choices), no timers | Lumen | Lumen | MVP | Must |
| F10 | **Commitments & follow-up** | Manager chooses 1 action for their real team; 14-day private check-in ("Did it happen? What did you learn?") | North-star | Differentiate | MVP | Must |
| F11 | Facilitator kit | For HR BPs: session plans, discussion prompts, aggregate cohort insight | Omar persona | Improve | V1 | Should |
| F12 | Custom scenario builder | L&D describes a local situation; draft sim generated; HR plus our editors approve | Local relevance | Improve | V1 | Should |
| F13 | Executive edition | Workforce planning sims with financial trade-offs | Upsell | Differentiate | V2 | Could |
| F14 | Works-council pack | Documentation of data flows, DPIA template, EU-language UI (DE/FR/NL) | EU sales | Differentiate | V1 | Should |
| F15 | Audio "commute" episodes | 10-min narrated case stories (human-voiced) | Headway/Blinkist audio [V2] | Parity | V2 | Could |

MVP = F1–F10. **Core loop:** pick a moment → simulate → debrief → playbook → commit an action → follow-up → next sim or cohort session.

## 5. Core experience & key user flows
**Core loop.** Weekly: Monday "this week's scenario" (from the cohort plan) → a 15-min sim → debrief → pick a playbook → commit 1 action → Thursday cohort thread → end-of-week summary.

**Flow 1: Onboarding (≤5 min)**
1. SSO sign-in.
2. My Needs card: text or voice, captions, text size.
3. "What's your AI situation?" with 6 options (for example "rolling out a tool", "incident happened", "team anxious").
4. A 5-minute starter sim ("Tell your team about the pilot"). First value.

**Flow 2: Change Room simulation**
1. A scenario card sets context (team roster of fictional people, stakes and goal). It stays visible throughout.
2. Conversation turns with AI characters, in voice or text. Unlimited thinking time and a "pause and look at the playbook" button.
3. Decision points: 2–4 options plus "write your own".
4. The consequence timeline shows "Two weeks later…".
5. Debrief: principle, alternative path, playbook link. Replay a branch if wanted.

**Flow 3: Cohort**
- Join the cohort, which has a fixed weekly structure.
- Asynchronous thread with prompts; live sessions optional (captioned; recording and transcript posted).
- Facilitator summary each week.

**Flow 4: HR/L&D console**
- Assign cohorts and see aggregate participation and commitments completed (counts only).
- Export the programme report.
- **Cannot** see transcripts of any manager's simulation.

**Flow 5: My Needs.** One tap from any screen. The branching view can switch to a list with headings so screen readers get a predictable structure.

**Flow 6: Billing.** B2B invoice; seat transfer self-serve. Individual (V1) follows the fair-billing charter.

**IA.** This week · Change Room (scenario library) · Playbooks · Cohort · Team readiness · My Needs.

**Session design.** Sims last 10–20 min with save and resume. The debrief is always the designed end: "One thing to try this week".

## 6. Inclusive, accessible & sensory design spec
- **Sensory Dial.** Default **Balanced** (Calm if the OS says so). Sim tension is conveyed through narrative, not sound effects or countdowns. There is no alarm audio in the incident sims. Lively adds optional ambient office audio (off by default).
- **Input modes.** Voice, text, keyboard-only decisions, switch access to decision lists, AAC speech accepted.
- **Targets.** ≥48 dp (≥56 dp in the 60+ preset); no drag.
- **Typography.** 18 px body; scenario cards ≤120 words with a "more detail" expander; plain-language toggle; dyslexia settings.
- **Audio.** AI character voices have captions, speaker labels and adjustable rate; separate sliders; mono option; hearing-aid streaming via the OS.
- **Speech-disability text path.** Full text parity; the rubric never scores fluency or tone of voice.
- **Presbyopia (35–59).** Respect OS text size to 200%; no light-grey text; contrast ≥4.5:1 (7:1 in high contrast).
- **Themes.** "Boardroom" (neutral) and high contrast. Illustrated, non-photoreal characters to avoid uncanny valley and stereotype risk.

| # | Principle | Acceptance criterion in Lead with AI |
|---|---|---|
| P1 | Calm | No countdowns or alarms in incident sims; Reduce Motion honoured |
| P2 | Sound | Captions on 100% of character speech; ambient audio off by default |
| P3 | Predictable | Every sim: Context → Conversation → Decision → Consequence → Debrief |
| P4 | Targets | 48/56 dp; decisions as large list buttons |
| P5 | Plain language | Plain toggle ≤ grade 8 |
| P6 | Typography | WCAG 1.4.12 passes |
| P7 | Multimodal | All sims completable in text; switch-accessible decisions |
| P8 | Low penalty | Replay any branch; "there's no single right answer" framing where true |
| P9 | Focus | One sim per session suggested; designed end |
| P10 | Memory | Scenario context and roster pinned on screen |
| P11 | Timing | No timed decisions |
| P12 | My Needs | Free accommodations; profile shared with AI Fluency Lab |
| P13 | Age-respectful | Professional, diverse characters (age, disability, ethnicity), reviewed |
| P14 | Low admin | HR sets up a 12-person cohort in ≤15 min |
| P15 | Motivation | No manager leaderboards |
| P16 | Affirming | Scenarios include disabled and neurodivergent employees portrayed with dignity (panel review) |
| P17 | Honest claims | No "proven to increase adoption" until a study exists |
| P18 | Privacy | Sim transcripts private to the manager; employer sees counts only |

**Lumen audit target:** ≥22/24.

## 7. AI specification & guardrails
**Does**
- LLM role-play of fictional characters, with persona sheets written by humans (motivations, concerns, boundaries).
- Branch management by a deterministic scenario graph; the LLM varies dialogue within a node but does not invent outcomes.
- Debrief feedback against a published rubric (clarity, empathy statements *as words used*, fairness, risk handling, next steps).
- Optional ASR/TTS.

**Does not**
- Score emotion, sentiment of voice or face (EU AI Act Art. 5 [V] (repo)).
- Rate real employees.
- Give legal advice (it points to the playbook and HR/legal).
- Present characters as real people or companions.

**Scenario integrity.** Characters are diverse and non-stereotyped. A bias review panel checks each persona (for example, the "resistant" older worker trope is avoided or explicitly challenged).

**Grader bias testing.** Matched transcripts vary name, dialect and text vs. voice mode. Maximum rubric difference 0.25 points; quarterly re-test.

**Safety.** If a manager discloses real misconduct or crisis ("someone on my team said they want to hurt themselves"), the sim pauses and offers resources plus a recommendation to contact HR/EAP. This is self-report based.

**Evaluation.**
- Scenario playtests with 20 managers per sim.
- Red-team: attempts to get the AI to endorse unlawful actions (e.g., "use AI to monitor who's unproductive"). The system responds within the sim by explaining the legal and ethical risks.

**Cost [E].** A text sim costs ~$0.05–0.15 and a voice sim ~$0.30–0.60. Facilitator cost per 12-person cohort is ~$1,200 (about 16 hours).

## 8. Data, privacy & compliance
| Data | Purpose | Retention | Where |
|---|---|---|---|
| Sim transcripts & decisions | Debrief, personal history | 12 months; manager-deletable | Cloud; **never visible to employer** |
| Commitments | Follow-up | Manager-controlled | Cloud |
| Team readiness (from AI Fluency Lab) | Aggregate insight | Live view | k≥5 aggregation |
| Cohort threads | Discussion | Cohort + 6 months | Cloud; members only |

**Regimes.**
- GDPR (Art. 88 employment context; works councils in DE/NL/FR).
- EU AI Act Art. 4 support, Art. 50 transparency, Art. 5 (no emotion recognition), and Annex III avoided (no evaluation of employees for HR decisions).
- US state privacy laws.
- FTC §5.

**Consent.** Managers see what HR can and cannot see before first use. Participation in cohorts is voluntary where required by local rules.

## 9. Monetization & go-to-market
| Offer | Price | Benchmark |
|---|---|---|
| Add-on to AI Fluency Lab | $150 per manager per year | Section $750/seat [V]; LinkedIn Teams $379.88 [V2] |
| Stand-alone | $300 per manager per year | Same |
| Cohort programme | $750 per manager (6 weeks, facilitated) | BetterUp ~$3,000+ [V2] |
| Individual (V1) | $15/mo | Blinkist Pro $174.99/yr [V2] |

- **Channels:** cross-sell to AI Fluency Lab buyers; HR consultancies and change-management partners; LXP marketplaces; EU partners with the works-council pack.
- **ASO / web SEO:** "leading AI change", "AI adoption for managers", "manager AI training". Business category. Accessibility Nutrition Label.
- **Markets:** US, UK, DACH (DE localisation in V1).

## 10. Success metrics
- **North star:** team AI actions launched per active manager per quarter (target ≥2).
- **Inputs:** sims completed per manager per month (≥3); cohort completion (≥65%); commitments made (≥80% of sims) and reported done (≥50%).
- **Outcomes:**
  - team verified skills growth (AI Fluency Lab aggregate) vs. teams of non-participating managers
  - employee "my manager supports AI use" pulse item (Gallup-style wording, aggregate)
  - Evidence plan: matched-team comparison in design-partner orgs (Tier 2).
- **Guardrails:** Sensory Comfort ≥4/5; zero employer access to transcripts; grader subgroup gaps within thresholds; manager-reported "felt judged" ≤10%.
- **Retention:** 30-day activation ≥70% of seats; quarterly active ≥60%; NRR ≥115% (bundle).

## 11. Validation plan
**Riskiest assumptions**
1. L&D buyers fund manager sims separately from AI Fluency Lab (vision).
2. Managers find AI role-play credible and useful, not gimmicky.
3. Sims lead to real team actions.
4. Text-mode sims are as effective as voice.

| # | Experiment | Sample | Success | Kill |
|---|---|---|---|---|
| X1 | **Bundle vs. stand-alone pricing interviews** (vision test), with a Van Westendorp card sort | 12 L&D leaders | ≥6 would buy as add-on at ≥$120; ≥3 stand-alone at ≥$250 | <3 at any price |
| X2 | Paper/Figma branching sim with Wizard-of-Oz characters (a facilitator types character lines from persona sheets) | 16 managers (incl. 3 disabled/Deaf) | Usefulness ≥4/5; ≥70% commit an action | <3.5 usefulness |
| X3 | 14-day commitment follow-up | Same 16 | ≥50% report action done | <25% |
| X4 | Text vs. voice mode A/B | Same | No usefulness gap >0.3 | Gap >0.7 |
| X5 | Works-council/privacy review | 2 EU HR leaders, 1 DPO | "Approvable" with the data model | Blocking concerns |

**Mapping.** WP2 (12 managers/L&D buyers), WP4 (X2–X4), WP5 (X1, X5).

## 12. Build handoff
**Epic A: Scenario engine**
- Given a scenario graph, when the LLM generates a character line, then it stays within the node's allowed intents (validated by a classifier), or falls back to the authored line.
- Given text mode, when a sim completes, then the debrief is identical in structure to voice mode.

**Epic B: Debrief & rubric**
- Given a completed sim, then the debrief shows the rubric, 1 strength, 1 suggestion, and a playbook link, and contains no emotion or tone score.

**Epic C: Privacy boundary**
- Given an HR admin, when calling any endpoint, then no transcript, decision or commitment text is returned. The only permitted outputs are counts where k≥5.

**Epic D: Cohorts**
- Given a live session, then captions are live and the transcript is posted within 24 h. Asynchronous-only participants can complete the cohort.

**Epic E: Accessibility**
- Given a screen-reader user, when a decision point appears, then focus moves to a heading "Decision: {question}", and options are a list of buttons.

**Non-functional requirements**
- Sim turn latency <2 s p95.
- Web plus iOS/Android.
- WCAG 2.2 AA.
- EN, then DE.
- SOC 2 path; EU data residency option.

**QA focus**
- AT matrix: VoiceOver, NVDA, JAWS, TalkBack, Voice Control.
- Sensory: no alarms in incident sims.
- AI safety: unlawful-surveillance requests, discriminatory decisions, crisis disclosure.
- Billing: seat transfer.
- COPPA: N/A.

**Dependencies.** Lumen DS, My Needs, AI orchestration (scenario graph runtime shared with Career Sprint's interview coach), AI Fluency Lab skills data API (aggregate), consent ledger.

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Buyers won't fund separately | High | Med | Ship as add-on/track first |
| Sims feel generic | Med | High | Co-author with practising managers; custom builder |
| Perceived as surveillance | Med | High | Hard privacy boundary; works-council pack |
| Big vendors add AI-change sims (Skillsoft, LinkedIn) | High | Med | Integration with verified team skills; accessibility; price |
| Stereotyped characters | Med | Med | Panel review; diverse personas |

**Open questions.** Is the best buyer L&D or the AI transformation office? Do managers prefer cohorts or solo sims? What is the right number of scenarios for launch (12 vs. 20)?

## 14. Sources
- [V] Gallup manager support and AI adoption: https://www.gallup.com/workplace/694682/manager-support-drives-employee-adoption.aspx · https://www.gallup.com/workplace/712736/organizational-adoption-jumps-six-points.aspx · https://www.gallup.com/workplace/712433/employee-engagement-remains-flat-adoption-accelerates.aspx
- [V] Workera: https://www.prnewswire.com/news-releases/ai-training-more-than-doubled-this-year-but-56-of-employees-report-no-time-at-work-to-build-the-skills-workera-research-finds-302887120.html
- [V] Skillsoft Q4 FY2026 and CAISY: https://www.sec.gov/Archives/edgar/data/1774675/000143774926011599/ex_898416.htm · https://www.stocktitan.net/news/SKIL/skillsoft-reports-financial-results-for-the-fourth-quarter-and-full-lkqfsnq2u8lv.html · https://learn.microsoft.com/en-us/viva/learning/learning-agent-roleplay-skillsoft
- [V2] Mursion: https://www.mursion.com/ · https://tracxn.com/d/companies/mursion/__T3ch6LjbWBdD8xTiViD5FpjoZsU-VPw6SmUIghWM--A
- [V] Yoodli: https://www.geekwire.com/2025/ai-roleplay-startup-yoodli-raises-40m-reports-900-revenue-growth/
- [V2] BetterUp pricing estimates: https://risely.me/compare/pricing-guide/ · https://www.heycompono.com/blog/betterup-pricing-guide-2026
- [V] Section pricing: https://www.sectionai.com/pricing
- [V2] LinkedIn Learning pricing: https://trainingcost.com/linkedin-learning-pricing
- [V] Coursera Q2 2026: https://investor.coursera.com/news/news-details/2026/Coursera-Reports-Second-Quarter-2026-Financial-Results/default.aspx
- [V2] Blinkist pricing: https://www.shortform.com/blog/hub/product/blinkist-pricing/ · [V2] Imprint: https://mwm.ai/apps/imprint-visual-micro-learning/1482780647
- [M] Harvard ManageMentor product and pricing (not verified this session)
- Repo: research/raw/02 (Headway), raw/04 (EU AI Act Art. 5), raw/05 (L&D channel economics)

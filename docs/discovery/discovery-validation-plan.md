# Discovery & Validation Plan: AI EdTech Startup Studio (5 ventures, 35 app concepts)

**Version:** 1.0 · **Date:** 29 September 2026 · **Duration:** 16 weeks · **Scope:** Planning and validation only. **No production code.**
**Inputs:**
- [Research paper](../01-research-paper.md)
- [Inclusive & Sensory UX Framework](../02-inclusive-sensory-ux-framework.md)
- Vision documents: [Lanternling](../vision/01-lanternling-early-years.md) · [Questwise](../vision/02-questwise-tweens.md) · [Ascendly](../vision/03-ascendly-teens.md) · [Evergrow](../vision/04-evergrow-adults.md) · [Wavelength](../vision/05-wavelength-neurodivergent.md)

---

## 1. Objectives
1. **Verify the research base.** Close the evidence gaps flagged [M], [E] or [V2] in the raw research, and replace estimates with primary data.
2. **Validate problems** for each venture. Confirm that the top user needs are real, frequent and intense for the target segment, including neurodivergent and disabled users.
3. **Prioritize the 35 app concepts.** Select **2–3 MVP apps per venture** using evidence on desirability, feasibility, viability and inclusivity.
4. **Validate solutions without code.** Use paper prototypes, clickable Figma, concierge and Wizard-of-Oz tests, especially for AI behavior, sensory design and multimodal input.
5. **Validate business models and channels.** Test willingness to pay, the payer (parent, ESA, school, employer, health plan, library) and the cost to reach users.
6. **Hold to inclusive-UX targets.** Every surviving concept must meet the Lumen acceptance criteria and score ≥22/24 on the accessibility and sensory rubric.
7. **Decide the sequence.** Hold a studio investment gate at week 16: which ventures and apps go to MVP build, in what order, and with what budget.

## 2. Guiding principles for the research itself
- **Nothing about us without us.** Paid co-design panels with neurodivergent and disabled people start in week 1, not after concepts are fixed.
- **Test the riskiest assumption first.** Every experiment names the assumption it could disprove, and sets its success and kill thresholds in advance.
- **Ethics before speed.** Research with children follows a formal protocol (see §7), including consent, assent, safeguarding and COPPA-grade data handling.
- **Accessible research.** Participants with assistive technology take part in every round. Accessibility is never a separate pass at the end.
- **No deception of children.** Wizard-of-Oz tests with children are always supervised by a caregiver, and the method is disclosed to caregivers in advance. Adults are debriefed afterwards.

## 3. Team and governance

| Role | FTE (16 wks) | Notes |
|---|---|---|
| Studio lead / research director | 1.0 | Owns gates and synthesis |
| Venture leads (×5) | 5 × 0.5–1.0 | One per venture; may be entrepreneurs-in-residence |
| UX researchers | 3.0 | Including 1 specialist in accessibility research and 1 in child research |
| Product designers (inclusive design) | 2.0 | Build the Lumen design system prototype and Figma concepts |
| Learning scientist | 0.5 | Logic models and evidence design |
| AI/ML advisor (feasibility) | 0.5 | ASR benchmarks, guardrail feasibility, cost models |
| Privacy and compliance counsel | 0.25 | COPPA 2025, AADC, FERPA, EU AI Act, research protocol |
| Market analyst | 0.5 | Data purchases, sizing, pricing tests |
| **Advisory boards (paid)** | — | **ND advisory board** (autistic, ADHD, dyslexic adults and teens, AAC users) · clinical panel (SLP, OT, BCBA, developmental pediatrician) · educator panel (pre-K, 3–12, special education, homeschool/microschool) · 60+ panel |

**Cadence:** weekly venture stand-ups · a synthesis review every 2 weeks · gates at week 8 (problem) and week 16 (solution and investment).

## 4. Timeline (16 weeks)

```
Week:   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16
WP0  ███                                                             Setup, ethics, panels, recruitment
WP1  ███████████                                                     Evidence verification & competitive audit
WP2      ███████████████████                                         Problem discovery (interviews, diaries, surveys)
WP3                      ███████████                                 Opportunity mapping & concept prioritization
                                 ◆ GATE 1: Problem validation (wk 8)
WP4                              ███████████████████████             Solution validation (no-code prototypes, WoZ)
WP5                                  ███████████████████             Business model & channel validation
WP6                                              ███████████████     Synthesis, MVP definition, investment memo
                                                                 ◆ GATE 2: Build / Pivot / Kill (wk 16)
```

## 5. Work packages

### WP0: Setup (weeks 1–2)
- Ethics protocol reviewed by an independent IRB (commercial IRB) for child and vulnerable-adult research.
- Easy-read consent and assent materials, visual session schedules, AAC-friendly interview kits.
- Recruit advisory boards and participant panels. **Target ≥30% of all participants neurodivergent or disabled.**
- Research data handling: minimal PII, encrypted storage, retention schedule, no recordings of children without explicit consent.
- Trademark screening of the five working names.

### WP1: Evidence verification and competitive audit (weeks 1–5)
| Task | Output | Closes gap from |
|---|---|---|
| Buy a Sensor Tower / Appfigures / AppMagic export (Education + Kids, US and global, 2025–26) | Verified top-30 lists, downloads, revenue, retention proxies | Raw 01, 02, 05 |
| Direct Reddit pull (API) and manual reading of the top 20 threads per subreddit, plus Mumsnet, Common Sense, AppleVis and Product Hunt | Verbatim quotes, upvote-weighted pain points | Raw 03 |
| **Hands-on accessibility and sensory audit** of the unified top 30 plus 10 ND leaders, using the Lumen 24-point rubric with VoiceOver, TalkBack, Switch Control, Dynamic Type XXL and Reduce Motion | Scored audit matrix and a video library | Raw 01, 02, 04 |
| Fill specific data gaps: RevenueCat/AppsFlyer education benchmarks (D30, trial→paid), the Common Sense 2025 census, Pew teen AI use, UK EHCP 2026, KFF on Medicaid/OBBBA, state app-store age-verification laws | Updated benchmark sheet | Raw 04 appendix, Raw 05 §9 |
| Legal memo covering COPPA 2025, AADCs, KOSA status, EU AI Act (Art. 5, Annex III, Art. 50), FERPA/SOPIPA, FDA/FTC claims | Compliance requirements for each venture | Raw 04 B7, Raw 05 §5 |
| Pricing teardown (trial mechanics, cancellation flows) for 30 apps | Dark-pattern benchmark | Research paper §5 |

### WP2: Problem discovery (weeks 2–8)

**Methods and samples (minimums):**

| Method | Lanternling | Questwise | Ascendly | Evergrow | Wavelength | Notes |
|---|---|---|---|---|---|---|
| In-depth interviews (JTBD) | 25 parents (incl. 5 grandparents), 6 pre-K educators, 4 SLPs/pediatric staff | 20 parents, 15 kids (8–12) with parents present, 8 homeschool/microschool educators | 25 teens (13–19), 10 teachers, 5 counselors, 8 parents | 15 workers (20–34), 12 managers/L&D buyers, 15 older adults (60+), 8 adult children of seniors, 5 library/aging-agency staff | 25 parents/caregivers, 12 ND teens and adults (incl. 4 AAC users), 10 SLP/OT/BCBA, 8 special-ed teachers/SENCOs | ≥30% ND/disabled across ventures |
| Contextual inquiry / in-home or in-class observation | 10 homes (dinner, bedtime, car) | 4 microschools/classrooms, 6 homework sessions | 3 classrooms, 6 study sessions | 3 workplaces, 2 senior centers/libraries | 8 homes, 2 clinics, 2 special-ed classrooms (incl. 1 special school) | Sensory environment notes |
| Diary study (1–2 weeks) | 15 families (screen-time moments) | 12 families (homework moments) | 15 teens (study sessions) | 10 workers (AI at work), 10 seniors (tech moments) | 15 families (transitions, meltdowns, communication) | Pictorial diaries for kids and ND participants |
| Quantitative survey | n≈600 parents of 1–7s | n≈500 parents of 8–12s + 300 homeschool/ESA families | n≈600 teens (13–19, parental consent for under-18s) + 200 teachers | n≈800 adults across 20–34 / 35–59 / 60+ + 100 L&D buyers | n≈500 caregivers of ND children + 150 professionals | Includes Kano, willingness to pay (Van Westendorp), and segment sizing |

**Discussion-guide themes (all ventures):**
- current tools
- moments of struggle
- workarounds
- screen-time and AI attitudes
- **sensory and accessibility needs**
- trust and privacy
- billing experiences
- who decides and who pays

**Outputs:**
- personas (validated)
- journey maps with sensory and emotional overlays
- JTBD statements
- ranked pain-point list for each venture, compared with the research paper's top 15

### WP3: Opportunity mapping and concept prioritization (weeks 5–8)
- Build an opportunity-solution tree for each venture from the WP2 evidence.
- Score all **35 app concepts** with the scorecard in §6.
- Run co-design workshops (ND advisory board, clinicians, educators) to refine the top concepts.
- **Gate 1 (week 8):** confirm or adjust each venture's problem focus. Shortlist **3–4 concepts per venture** for solution validation. Kill or merge the rest.

### WP4: Solution validation without code (weeks 8–15)

**Prototype types:**
| Type | Used for |
|---|---|
| Paper prototypes and printable cards | Toddler and pre-K concepts; routines (Calm Cubs, Wavelength Day); Math Realms regions |
| Clickable Figma (Lumen design tokens, Sensory Dial, multimodal answer tray) | All app flows; accessibility testing with VoiceOver and Switch Control, using Figma prototypes plus accessible HTML mockups only where needed for AT testing |
| **Wizard-of-Oz AI** (a trained human plays the AI under a written policy) | Sage Tutor, Study Coach, Explain It Back, Speak Freely, Story Lantern personalization, AAC phrase expansion, Focus Crew task breakdown |
| Concierge (a human delivers the service manually) | Babble Buddy by SMS, AI Fluency Lab cohorts, Career Sprint, Curiosity Circle cohorts, Silver Circuit classes |
| Existing-tool pilots | Study Squad via a Discord bot; Spark Switch using existing school switch hardware |
| Feasibility spikes (research, not product code) | Child-speech ASR word error rate by speaker group on consented samples; guardrail policy red-teaming on public models; cost-per-session models |

**The sensory A/B protocol (every venture):**
- Participants try the same flow in **Calm** vs. **Lively** (counterbalanced).
- Measures:
  - pictorial Sensory Comfort Rating (1–5)
  - persistence (time on task before a voluntary stop)
  - task success
  - distress signals observed by trained facilitators
  - stated preference
- Report results split by ND vs. non-ND and by age.

**Accessibility usability rounds:** each round includes at least these participants:
- 2 screen-reader users
- 1 switch or eye-gaze user
- 1 Dynamic Type XXL / low-vision user
- 1 Deaf/HoH user
- 2 dyslexic participants
- 2 autistic participants
- 2 ADHD participants
- For Evergrow, 3 participants aged 60+

### WP5: Business model and channel validation (weeks 9–15)
| Test | Venture(s) | Success threshold (pre-registered) |
|---|---|---|
| Landing-page smoke tests with price variants (targeting adults only; no ads aimed at children) | All B2C | Waitlist conversion ≥8% of visitors; ≥30% choose the paid tier over the free tier in a fake-door price test |
| Van Westendorp + Gabor-Granger in the survey | All | Acceptable price range includes the planned price |
| ESA vendor-approval discovery (AZ, FL, TN, TX, IA) | Questwise, Wavelength | Clear path to approval in ≥3 states within 6 months |
| Microschool/co-op letters of intent | Questwise | ≥5 LOIs |
| Employer design partners and paid pilots | Evergrow | ≥2 design partners; ≥3 LOIs at ≥$150 per seat per year |
| Library / aging-agency / MA plan discovery | Evergrow (60+) | ≥2 library pilots agreed; ≥1 MA plan in active conversation |
| School proof-of-learning pilot interest | Ascendly | ≥8 teachers commit to a pilot; ≥2 school leaders show purchase intent |
| Pre-K / Head Start / library distribution | Lanternling | ≥2 program partners agree to pilot |
| SLP/OT practice interest | Wavelength | ≥10 clinicians would recommend; ≥3 practices would pilot |
| Special-ed director interviews | Wavelength | ≥3 districts would pilot with IDEA funds |
| CAC probes (small paid social tests to parents and adults) | B2C | Cost per waitlist signup within the model's assumptions |

### WP6: Synthesis and investment memo (weeks 13–16)
- A validated vision update for each venture, with the MVP scope (2–3 apps plus the shared hub) and the evidence behind it.
- Lumen design system v0.1: tokens, Sensory Dial, "My Needs" profile spec, multimodal answer tray, co-play cards, fair-billing flows.
- Shared platform requirements, drafted in prose, not code:
  - AI orchestration and guardrail policies
  - privacy architecture
  - evidence engine: logic models and pilot designs
- An evidence plan for each MVP: logic model, outcome measures, pre-registration draft, university or clinic partner.
- Financial model: CAC, LTV and payback by channel, with a sensitivity analysis.
- **Gate 2 (week 16):** build / pivot / kill for each venture, and the sequencing decision.

## 6. Concept prioritization scorecard (for the 35 apps)

Each criterion is scored 1–5 and multiplied by its weight (maximum 100).

| Criterion | Weight | Evidence source |
|---|---|---|
| **Problem severity and frequency** (the need is real, frequent and intense) | 20 | WP2 interviews, diaries, survey |
| **Desirability** (target users want this solution) | 15 | WP4 prototype tests, Kano |
| **Inclusivity potential** (Lumen fit, ND/disabled users served well, sensory comfort) | 15 | WP4 sensory A/B, accessibility rounds |
| **Learning or outcome potential** (evidence base, measurable outcome) | 10 | Learning-scientist review |
| **Viability** (willingness to pay, payer identified, channel cost) | 15 | WP5 |
| **Feasibility** (AI accuracy, e.g., child ASR; content cost; compliance load) | 10 | Feasibility spikes, legal memo |
| **Differentiation vs. free AI and incumbents** | 10 | WP1 audit |
| **Platform leverage** (reuse across ventures) | 5 | Architecture review |

**Hard gates, regardless of score:**
- The concept must be able to meet the Lumen acceptance criteria. The prototype must score **≥22/24** on the accessibility and sensory rubric.
- The concept must not depend on emotion recognition, a companion persona for minors, training on children's data without consent, or dark-pattern monetization.
- The ND advisory board must sign off (Wavelength, and any concept aimed at children).

## 7. Research ethics and safeguarding protocol (summary)
- **Review:** An independent IRB reviews the protocol. Counsel reviews COPPA and GDPR handling.
- **Consent:**
  - Verifiable parental consent plus the child's own assent, in pictorial or easy-read form, with the right to stop at any time.
  - Teens (13–17) give their own assent plus parental consent.
  - Adults with intellectual disability use supported decision-making.
- **Session design:** short sessions matched to the age table, breaks on request, a sensory-friendly setting (home or a quiet room), a trusted adult present for under-13s, and AAC available.
- **Data:** minimum PII, no recording of children without explicit opt-in, encrypted storage, a deletion schedule, and no use of research data for model training.
- **Compensation:** fair payment for every participant, including children (in an age-appropriate form) and ND co-designers at professional rates.
- **Safeguarding:** trained facilitators, a distress protocol, and escalation paths. Wizard-of-Oz operators follow written policies and never role-play as friends or companions.

## 8. Riskiest assumptions and first experiments (by venture)

### 8.1 Lanternling (1–7)
| # | Assumption | Experiment | Success / kill threshold |
|---|---|---|---|
| L1 | Parents will pay for calm, co-play-first learning | Smoke test + survey WTP | ≥8% waitlist; planned price inside the acceptable range / kill if <3% |
| L2 | Toddler-parent pairs actually co-play when prompted | Babble Buddy SMS concierge (30 families, 2 weeks) | ≥60% use prompts ≥4 days/week / <30% → rethink |
| L3 | Child-speech read-along accuracy is good enough | ASR WER benchmark + Wizard-of-Oz read-along | Group WER within target; frustration events ≤1 per session |
| L4 | Pre-K and libraries will distribute | Partner discovery | ≥2 pilot agreements |

### 8.2 Questwise (8–12)
| # | Assumption | Experiment | Threshold |
|---|---|---|---|
| Q1 | Kids stay engaged with a Socratic tutor that never gives answers | Wizard-of-Oz Sage Tutor (20 families, 2 weeks) | ≥70% of sessions completed; child rating ≥4/5 |
| Q2 | Mastery-gated worlds are fun without variable rewards | Paper Math Realms A/B vs. points variant | Persistence equal or better |
| Q3 | ESA and microschool channels will buy | ESA discovery + LOIs | ≥3 states on a clear path; ≥5 LOIs |
| Q4 | Parents value "no pay-to-win" enough to switch | Survey + interviews | ≥50% rank it a top-3 purchase driver |

### 8.3 Ascendly (13–19)
| # | Assumption | Experiment | Threshold |
|---|---|---|---|
| A1 | Teens choose learning mode under deadline pressure | Diary + Wizard-of-Oz Study Coach (40 teens) | ≥50% return weekly; measurable quiz gains |
| A2 | Teachers adopt proof-of-learning; teens don't feel surveilled | Explain It Back paper pilot (4 classes) | Teacher value ≥4/5; teen comfort ≥3.5/5 |
| A3 | Study Squad beats Discord for focus | Discord bot pilot | ≥2 sessions/week per active teen |
| A4 | Sponsors will pay for pathways | Employer and college LOIs | ≥2 sponsor LOIs |

### 8.4 Evergrow (20+)
| # | Assumption | Experiment | Threshold |
|---|---|---|---|
| E1 | Mid-market employers pay for role-specific AI fluency | Concierge cohorts with design partners | Pre/post task-performance gain; ≥3 paid LOIs ≥$150 per seat per year |
| E2 | Hybrid AI + human language practice is viable at $20–30/mo | Price test + concierge | Conversion inside the model; tutor cost ≤35% of revenue |
| E3 | The 60+ payer exists (library / MA / family gift) | Library pilots + gift smoke test + MA calls | ≥2 library pilots; ≥5% gift-page conversion |
| E4 | 60+ learners are comfortable with voice-first AI | Silver Circuit usability with 15 seniors | Task success ≥80%; confidence gain ≥1 point (5-point scale) |

### 8.5 Wavelength (ND children)
| # | Assumption | Experiment | Threshold |
|---|---|---|---|
| W1 | Caregivers adopt an integrated hub if setup takes ≤5 minutes | Timed setup tests vs. incumbents | Median ≤5 minutes; SUS ≥75 |
| W2 | SLPs and AAC users accept AI phrase expansion that keeps authorship | SLP panel + AAC user co-design + Wizard-of-Oz | Authorship satisfaction ≥4/5; ≥70% of SLPs would trial it |
| W3 | Affirming framing matches what parents will pay for | Message test (affirming vs. deficit framing) + WTP | Affirming framing converts equal or better |
| W4 | Calm-by-default improves comfort and persistence | Sensory A/B | Comfort +1 point for ND participants; persistence up |
| W5 | ESA, IDEA and clinician channels will fund it | Channel discovery | ≥3 districts; ≥3 practices; ESA path in FL + 2 states |

## 9. Measures and instruments
- **Usability:** task success, time on task, System Usability Scale (SUS; target ≥75), Single Ease Question.
- **Accessibility:** Lumen 24-point rubric; WCAG 2.2 AA checklist (on accessible mockups); AT user task success.
- **Sensory:** pictorial Sensory Comfort Rating (1–5), persistence, observed distress signals, preference.
- **Desirability:** Kano, "very disappointed" Sean Ellis test (≥40% target on concept tests), NPS on concierge services.
- **Learning (pilot proxies):** pre/post probes (vocabulary, phonics, math items, explanation rubrics, AI task performance).
- **Trust and privacy:** caregiver trust scale, teen privacy comfort, AI-content trust ("human-crafted" perception).
- **Economics:** willingness to pay (Van Westendorp), smoke-test conversion, CAC probes, LOIs.

## 10. Deliverables at week 16
1. **Research paper v2**, with verified data replacing flagged estimates.
2. **Five validated vision documents v2**, each with an MVP scope, a sequence and a kill list.
3. **Lumen Inclusive & Sensory Design System v0.1** (Figma), plus the "My Needs" profile specification.
4. **Competitive accessibility and sensory audit** (40 apps, scored and with video).
5. **Persona and journey library**, including ND and disabled personas and sensory overlays.
6. **Evidence plans** (logic models and pre-registration drafts) for each MVP.
7. **Compliance requirements** for each venture (COPPA 2025, AADC, FERPA, EU AI Act, FTC/FDA claims).
8. **Financial model and investment memo**, with a studio sequencing recommendation.

## 11. Indicative budget (16 weeks, USD, to refine)
| Line | Estimate |
|---|---|
| Core team (≈14 FTE-equivalents × 16 weeks, blended) | $700k–950k |
| Participant incentives (≈600 interview/test participants + ≈4,000 survey completes) | $120k–180k |
| Advisory boards (ND, clinical, educator, 60+), paid | $60k–90k |
| Data purchases (Sensor Tower/Appfigures, benchmark reports) | $40k–80k |
| IRB, legal and privacy counsel | $50k–80k |
| Smoke tests and CAC probes (paid social to adults) | $30k–50k |
| Prototyping tools, AT devices (switches, eye-gaze loaner), research ops | $20k–40k |
| **Total** | **≈ $1.0M–1.5M** |

## 12. Risk register (discovery phase)
| Risk | Impact | Mitigation |
|---|---|---|
| Hard to recruit ND, disabled and 60+ participants | Biased findings | Partner with advocacy organizations, special schools and libraries. Pay fairly. Offer flexible formats |
| Children's research ethics or COPPA misstep | Reputational and legal harm | IRB, counsel review, minimal data, trained facilitators |
| Wizard-of-Oz overstates AI capability | False-positive validation | Feasibility spikes run in parallel. Operators follow realistic-capability scripts |
| Confirmation bias toward 35 attractive concepts | Wasted build | Pre-registered thresholds. Kill criteria. External reviewers at the gates |
| Market data remains uncertain | Poor sizing | Buy primary data (WP1). Use bottom-up TAM |
| Scope sprawl across 5 ventures | Shallow learning | Shared panels and instruments. Staggered depth: Evergrow and Wavelength first if resources are tight |

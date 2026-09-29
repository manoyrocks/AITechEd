# Pathfinder: App Strategy & Product Specification

> **Venture:** Ascendly · **App #:** 6/7 · **Ages:** 15–19 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/03-ascendly-teens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research caveat (important):** The shared session web-search budget ran out before this app's competitor research, and WebFetch was blocked. Competitor facts are from memory ([M]) or the studio's raw files ([V2]). **All [M] figures (user counts, prices, ownership) must be verified in Discovery WP1** before external use. No competitor numbers have been invented; where a figure is not known, the table says "verify".

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Try a real job for 20 minutes, see which skills you already have, and find the next concrete step — college, trade, dual enrollment or work. |
| **Primary user / buyer** | Teens 15–19 (users). School counselors and CTE coordinators (buyers/champions). Employers, community colleges and apprenticeship programs (sponsors). |
| **Core job-to-be-done** | "When I don't know what to do after high school and generic quizzes tell me nothing, I want to try real work and see what fits, so I can pick a next step I actually believe in." |
| **Category on the stores** | Education (13+); web-first for school use. |
| **Top competitors** | Naviance (PowerSchool), Xello, Scoir, MajorClarity, BigFuture (College Board), Roadtrip Nation, CareerVillage, Handshake, Forage, Coursera career paths |
| **Our wedge** | 1. **Do, don't just quiz:** accessible 20-minute AI-run job simulations (clearly simulations) instead of interest inventories. 2. **Skills evidence, not personality labels:** simulations, Explain It Back and Draft Mentor feed a teen-owned skills portfolio in the Ascendly Record. 3. **Every path is equal:** trades, CTE, dual enrollment, apprenticeships and college shown side by side, with local, funded next steps. 4. **Accessible by design:** every simulation has motor, sensory and communication alternatives. |
| **Business model** | Free for teens (core simulations, portfolio). School/district licence $5–15/student/yr (counselor dashboard, local pathway data). Sponsored pathways (employers/community colleges fund simulations for their fields; clearly labelled, no data sale). |
| **North-star metric** | Monthly "next steps taken" per active teen (e.g., applied to dual enrollment, booked a CTE visit, requested a job-shadow, saved a scholarship deadline) after completing ≥1 simulation. |
| **MVP candidate?** | **Later** (Year 3 sponsors per vision); discovery now because the sponsor model is a top assumption (A4). |

## 2. Problem & users

**Problem statement.** Career guidance in US high schools is thin and generic. Counselors carry large caseloads [M: ASCA reports ratios well above its recommended 250:1 — verify], and the most common digital tools are interest inventories and college-search databases [M]. Meanwhile, the job market is shifting quickly: the WEF *Future of Jobs 2025* expects 39% of workers' core skills to change by 2030 [V2: raw 05], and forums show anxiety that AI is eroding entry-level jobs [M: raw 03]. Investors favour "AI-enabled, career-aligned" learning [V2: raw 05, HolonIQ]. Teens like Diego (first-generation) rarely get real exposure to careers before choosing. Teen student data is also a trust issue: the PowerSchool breach (disclosed Dec 2024/Jan 2025) exposed tens of millions of student records [M: raw 03], and PowerSchool owns Naviance [M].

**Personas**
| Persona | Snapshot | Needs |
|---|---|---|
| **Diego, 18, first-generation** | Unsure about college vs trade vs job; works part-time. | Real exposure, costs and pay in plain numbers, a local next step. |
| **Marcus, 15, blind** | Interested in law and tech; simulations are often visual. | Fully screen-reader-accessible simulations; role models who are blind [I]. |
| **Aisha, 16, wheelchair user** | Told "hands-on" trades aren't for her. | Honest information on accommodations and adaptive tools in each field; simulations without fine-motor demands. |
| **Mrs. Johnson, school counselor** | 400+ students; must document career-readiness activities for the state. | A dashboard of who has explored what, exportable evidence, low admin. |
| **Community college CTE dean** | Wants more dual-enrollment students in HVAC and nursing. | Qualified, informed interest; a way to fund exposure. |

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Real exposure, not quizzes | Vision: "generic career quizzes" pain | 20-minute simulations |
| AI-era skills clarity | WEF 39% skills change [V2] | Skills map with "AI-resilient" and "AI-augmented" tags (explained, not predictions) |
| Equal status for non-college paths | Diego persona; CTE/dual enrollment channels [V2: raw 05] | Paths shown side by side with cost, pay and time |
| Accessibility | Lumen; Marcus/Aisha | Multimodal simulations; disability-in-work info |
| Trustworthy data handling | PowerSchool breach [M] | Minimal data, teen-owned portfolio, no data sale to sponsors |
| Counselor time | Caseloads [M] | Dashboard + state-reporting export |

## 3. Competitive feature benchmark

| App | Publisher | Scale / grossing signal | Price | Rating | Loved | Complaints | A11y / sensory | Source |
|---|---|---|---|---|---|---|---|---|
| **Naviance** | PowerSchool [M] | Long-time market leader in US high-school college & career readiness [M]; scale: verify | District licence [M]; price: verify | n/a (school tool) | College application workflow, transcripts, counselor tools [M] | Dated UX; feels like paperwork; data-trust concerns post-breach [M/I] | Web; varies [M] | [M] |
| **Xello** | Xello | Widely used in US/Canada K-12 career programs [M]; scale: verify | District licence [M] | n/a | Engaging career exploration, lessons, matchmaker quiz [M] | Quiz-based; teachers assign it as compliance [I] | Reports WCAG work [M]; verify | [M] |
| **Scoir** | Scoir | College search + application platform [M]; scale: verify | Free for students/families; school licence [M] | Good [M] | Clean college search, "following" colleges, counselor docs [M] | College-centric [I] | Web/app [M] | [M] |
| **MajorClarity** | Paper (acquired) [M: verify] | Career & CTE exploration with "Career Test Drives" [M] | District licence [M] | n/a | Short career tasks, pathway alignment [M] | Content depth varies [I] | Verify | [M] |
| **BigFuture** | College Board | Free national college & career planning site with scholarships [M] | Free | n/a | Scholarship programs, college search, career search [M] | College-centric; tied to College Board ecosystem [I] | Web a11y [M] | [M] |
| **Roadtrip Nation** | Roadtrip Nation (nonprofit) | Large interview archive + PBS series [M] | Free / school curriculum [M] | n/a | Authentic stories from diverse professionals [M] | Passive video; no doing [I] | Captions [M] | [M] |
| **CareerVillage** | CareerVillage.org (nonprofit) | Crowdsourced career Q&A with volunteer professionals; AI career coach [M] | Free | n/a | Real professionals answer questions [M] | Response delays; quality varies [I] | Web [M] | [M] |
| **Forage** | Forage | Free employer-designed virtual job simulations for students [M] | Free (employer-funded) [M] | Good [M] | Real company tasks; résumé line [M] | Aimed at university students; mostly corporate roles [I] | Web; varies [M] | [M] |

**Also:** Handshake — early-career job network for college students (not built for under-18s) [M]; Coursera career paths and certificates, now merged with Udemy (closed 11 May 2026; ~290M learners) [V2: raw 05].

**Feature matrix**

| Feature | Naviance | Xello | Scoir | MajorClarity | BigFuture | Roadtrip | Forage | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Interest/personality quiz | ✓ | ✓ | ◐ | ✓ | ✓ | ◐ | ✗ | **Parity-lite**: optional 3-minute "what do you enjoy doing" starter, never labels |
| Career video/story library | ◐ | ✓ | ✗ | ✓ | ◐ | ✓ | ◐ | **Integrate** (link partners, e.g., Roadtrip) |
| Hands-on job simulations | ✗ | ◐ | ✗ | ✓ (test drives) | ✗ | ✗ | ✓ | **Differentiate**: AI-run, accessible, 20 min, all levels including trades |
| Skills portfolio with evidence | ◐ | ◐ | ✗ | ◐ | ✗ | ✗ | ◐ (certificate) | **Differentiate** (Ascendly Record) |
| College search/apply workflow | ✓ | ◐ | ✓ | ✗ | ✓ | ✗ | ✗ | **Reject at MVP** (integrate with Scoir/Common App later) |
| CTE, apprenticeships, dual enrollment finder | ◐ | ◐ | ✗ | ✓ | ◐ | ✗ | ✗ | **Improve**: local, with cost/pay/time |
| Scholarship discovery | ◐ | ◐ | ◐ | ✗ | ✓ | ✗ | ✗ | **Parity** (curated; no "scholarship spam" data harvesting) |
| Counselor dashboard/reporting | ✓ | ✓ | ✓ | ✓ | ✗ | ◐ | ✗ | **Parity** |
| Talk to real professionals | ✗ | ◐ | ✗ | ◐ | ✗ | ✗ | ✗ | **V1**: moderated, asynchronous, via partners (e.g., CareerVillage-style) |
| AI role-play with "a professional persona" | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject persona**; AI is the *simulation engine* with scenario roles, clearly labelled, no ongoing relationship |
| Sponsor-funded content | ✗ | ✗ | ✗ | ◐ | ✗ | ◐ | ✓ | **Parity with guardrails**: labelled, no data sale, no recruiting contact under 18 without consent |
| Disability-in-work information | ✗ | ✗ | ✗ | ✗ | ✗ | ◐ | ✗ | **Differentiate** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| PF-01 | **Job simulations (20 min)** ★ | Scenario-based tasks (nurse triage, electrician troubleshooting, UX brief, paralegal research, HVAC diagnosis, data analyst, early-childhood educator). AI plays scenario roles (patient, client, supervisor) inside a scripted, human-reviewed scenario. | Vision; Forage/MajorClarity parity, broader and accessible | Differentiate | MVP | Must |
| PF-02 | **Accessible simulation design** ★ | Every simulation completable by screen reader, keyboard, switch, voice or AAC; motor tasks have decision-based equivalents; audio has captions/transcripts. | Marcus/Aisha | Lumen / Differentiate | MVP | Must |
| PF-03 | **Reflection + skills map** | After each simulation: what you enjoyed, found hard, skills shown (evidence-based, from the task log). | Evidence over labels | Differentiate | MVP | Must |
| PF-04 | **Skills portfolio (Ascendly Record)** ★ | Skills with evidence links (simulations, Explain It Back, Draft Mentor, Exam Ready mastery). Teen chooses what to share. | Shared layer | Differentiate | MVP | Must |
| PF-05 | **Path comparison** | For a career: side-by-side paths (apprenticeship, CTE certificate, dual enrollment, associate, bachelor's) with time, typical cost, typical pay range and sources (BLS/O*NET). | Equal status for paths | Improve | MVP | Must |
| PF-06 | **Local next steps** | Dual enrollment, CTE programs, apprenticeships and job-shadow options near the teen (by ZIP, not GPS), with deadlines. | Diego persona | Improve | MVP | Must |
| PF-07 | **AI-era skills lens** | Each career shows which tasks are changing with AI and which human skills grow in value, with sources; framed as uncertainty, not prediction. | WEF [V2] | Differentiate | MVP | Should |
| PF-08 | **Disability-in-work notes** | Accommodations, assistive technology and role models per field, co-written with disabled professionals. | Aisha persona | Differentiate / Lumen | MVP | Should |
| PF-09 | **Counselor dashboard** | Class/caseload view of exploration activity (not reflections), exports for state career-readiness reporting. | Counselor buyer | Parity | MVP | Must |
| PF-10 | **Starter interest check** | 3-minute activity-based starter ("which of these would you rather do this Saturday?") to suggest first simulations; no personality types. | Onboarding | Parity-lite | MVP | Should |
| PF-11 | Scholarship & funding finder | Curated scholarships, FAFSA/state aid reminders, CTE grants; no lead-gen partners. | BigFuture parity | Parity | V1 | Should |
| PF-12 | Ask a professional | Moderated asynchronous Q&A with verified professionals (partner network). | CareerVillage parity | Parity | V1 | Should |
| PF-13 | Sponsored pathways | Employers/colleges fund simulations and local opportunities; labelled; teen opts in to be contacted (18+ only for direct recruiting). | Revenue; A4 | Parity | V1 | Should |
| PF-14 | Job-shadow and work-based learning tracker | Log shadows, internships, part-time work; reflections become portfolio evidence. | CTE programs | Improve | V2 | Could |
| PF-15 | College list integration | Export portfolio to Common App/Scoir activities section. | College path | Parity | V2 | Could |

★ = signature. **Signature: accessible 20-minute job simulations feeding an evidence-based, teen-owned skills portfolio.** MVP = 10 features.

## 5. Core experience & key user flows

**Core loop:** open → pick a simulation (suggested or browsed) → 20-minute scenario → reflection → skills map updates → compare paths → save a local next step → natural end.

**Flow 1: Onboarding (≤5 min)** — school SSO or personal sign-up (13+; Pathfinder content aimed at 15+) → Dial and input preferences → 3-minute starter check → first simulation suggested ("Try: Electrician troubleshooting, 20 min").

**Flow 2: Core simulation (Electrician troubleshooting)**
1. Brief: "A client's kitchen outlets stopped working. You're an apprentice on your first call." Label: "Simulation. The client is played by AI."
2. Teen asks the client questions (voice/text/choices). AI plays the client within the script.
3. Teen chooses diagnostic steps (decision-based, no fine motor); safety rules enforced ("Did you shut off the breaker?").
4. Supervisor feedback (scripted rubric): safety, reasoning, communication.
5. Reflection: 3 quick questions. Skills map: "Systematic troubleshooting ✓ (evidence: step log)".
6. Path compare: apprenticeship vs CTE certificate vs associate degree; local program deadline saved.

**Flow 3: Counselor** — assigns "Explore 3 simulations by Dec" → dashboard shows completion counts and saved next steps (not reflections unless shared) → exports report.

**Flow 4: My Needs** — Dial, input modes, captions, reading level, extended time (simulations untimed), "skip audio-heavy scenes".

**Flow 5: Sponsor opt-in (V1)** — teen sees "Sponsored by [Hospital]" label → can choose "Tell me about programs" → for under-18s, information only; no recruiter contact.

**IA:** Explore · Simulations · My Skills (portfolio) · Next Steps · My Needs.

**Session design:** simulations 15–25 min, pausable, resume anywhere; natural end with a single "next step" suggestion.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial:** Calm — text/illustration scenes, no ambient sound; Balanced (default) — narrated scenes with optional ambient audio (e.g., hospital sounds) off by default; Lively — richer visuals, still no flashing, ambient sound opt-in.

**Input modes:** choices (tap/switch), typed or voice questions to scenario characters, AAC text, keyboard; no drag or precision tasks; any "hands-on" step is a decision with an optional (never required) illustrative mini-task.

**Accessibility specifics:** every visual clue (a wiring diagram, a patient chart) has a structured text alternative; charts as data tables; captions for all speech; simulations untimed, with an optional "realistic pace" mode that only *describes* time pressure.

**Reading:** grade 6–8 default with dial; job jargon glossary inline.

**Age-respectful and identity-affirming:** diverse professionals including disabled people; no gendered defaults; mature photography/illustration themes.

**Lumen principles**
| # | Acceptance criterion |
|---|---|
| P1 | No ambient sound or motion by default in Calm/Balanced |
| P2 | All scenario audio captioned; no sound-only clue |
| P3 | Simulation layout fixed: Brief → Task → Feedback → Reflect |
| P4 | No drag/precision tasks; decisions by tap/keyboard |
| P5 | Glossary for every jargon term |
| P6 | BDA defaults |
| P7 | ≥3 input modes for character dialogue |
| P8 | Safe mistakes; feedback explains; retry any step |
| P9 | One simulation at a time; no autoplay-next |
| P10 | Scenario facts pinned in a "case notes" panel |
| P11 | Untimed by default |
| P12 | Accommodations free |
| P13 | Mature themes |
| P14 | Counselor assignment in ≤5 min |
| P15 | No badges for volume; portfolio shows evidence quality |
| P16 | Disabled professionals co-write disability-in-work content |
| P17 | Pay/cost data sourced and dated; no "you'll earn X" promises |
| P18 | No data sold to sponsors; no recruiting contact for under-18s |

**Target Lumen score:** ≥22/24.

## 7. AI specification & guardrails

**AI does:** play scenario roles within human-authored scripts and guardrails (client, patient, supervisor); evaluate task logs against scenario rubrics (draft, explainable); map evidence to a skills taxonomy (O*NET-aligned); summarise reflections for the teen; generate scenario *variants* from reviewed templates.

**AI does not:** act as an ongoing mentor/companion or remember the teen socially across sessions; claim to be a real professional; recommend a single "best career"; infer personality or emotion; use protected characteristics in matching; steer by sponsor interest.

**Human oversight / EU AI Act:** simulation feedback is formative; nothing is used for admission or placement decisions. If a school uses portfolios for placement (e.g., CTE program entry), that falls within Annex III "access/admission" high-risk use (from 2 Dec 2027 [V2: Gibson Dunn]) — we would require counselor review, logging and a FRIA before enabling it.

**Safety:** scenario roles are clearly labelled simulations; role-play boundaries (no romance, no personal relationship, exits on off-topic); sensitive scenarios (nurse triage) avoid graphic content and offer content notes; distress routing as per shared policy; no emotion recognition.

**Accuracy:** pay/cost/outlook data from BLS/O*NET and state sources with dates; AI-era lens uses cited sources; scenario content reviewed by two practising professionals per field.

**Evaluation:** professional reviewers rate realism ≥4/5; teen reviewers rate engagement ≥4/5; rubric agreement AI vs professional κ ≥0.6; bias audit — skills evidence and suggestions not significantly different by gender, race or disability for equivalent task logs.

**Cost [E]:** ~$0.05–0.15 per 20-minute simulation (multi-turn role-play); scenario authoring ~$3–8K per simulation (professional review + accessibility) [E].

## 8. Data, privacy & compliance

| Data | Why | Retention | Where |
|---|---|---|---|
| Simulation logs | Feedback, skills evidence | Teen-owned; deletable | Cloud |
| Reflections | Self-understanding | Private by default | Cloud |
| ZIP code | Local opportunities | Until changed | Cloud (no GPS) |
| Saved next steps | Planning | Teen-owned | Cloud |
| Counselor aggregates | Reporting | School year + 1 | Cloud (FERPA) |

**Regimes:** FERPA/SOPIPA; state student-privacy laws (many prohibit using student data for targeted advertising or selling it — sponsor model must comply) [M]; COPPA (13+); UK AADC; KOSA-ready; EU AI Act Annex III (admission/placement) if used that way; FTC §5 for outcome claims and endorsement guides for sponsored content; no employment-decision use (avoids AI hiring laws such as NYC Local Law 144 [M]).

**Consent:** teen consent; separate explicit opt-in to be contacted by sponsors (18+ only); sponsors receive aggregate, de-identified reach data only.

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Teen | Free | All simulations in the library, portfolio, path compare, local next steps |
| School/District | $5–15/student/yr [E, vision range] | Counselor dashboard, assignment, state-report export, local data curation |
| Sponsor | Per simulation/region [E: $10–50K/yr per sponsored pathway, to validate] | Fund a simulation for their field; labelled; aggregate impact reports |

Benchmarks: district career platforms are sold per student or per school [M: verify Naviance/Xello pricing in WP1]; Forage is free to students and employer-funded [M].

**Channels:** school counselors (ASCA community), CTE directors (ACTE), dual-enrollment offices at community colleges, workforce boards, state career-readiness initiatives; teen organic content ("I tried being a nurse for 20 minutes"). **ASO:** "career quiz alternative", "try a job", "trade school vs college", "career exploration". Accessibility Nutrition Label.

**Markets:** US first (O*NET/BLS data); UK V2 (apprenticeships).

## 10. Success metrics
- **North star:** monthly next steps taken per active teen (target ≥1 after first simulation).
- **Inputs:** simulations completed per teen (≥3 per term); reflection completion (≥70%); path-compare views; portfolio items added.
- **Guardrails:** simulation realism ≥4/5 (professional-rated); Sensory Comfort ≥4/5; bias-audit pass; zero sponsor contacts to under-18s; teen "felt pushed" score ≤2/5.
- **Outcomes:** career-decision self-efficacy (validated scale, pre/post); dual-enrollment/CTE enrolment among pilot schools vs comparison (longer-term).
- **Retention:** episodic by design; target ≥50% of teens return within a term; school renewal ≥85%.

## 11. Validation plan (no-code)

**Riskiest assumptions**
1. Schools, colleges or employers will pay (A4).
2. Teens find 20-minute simulations more useful than quizzes/videos.
3. Simulations can be both realistic and fully accessible at affordable authoring cost.
4. Counselors will assign it (time, reporting fit).

**Experiments**
| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | Counselor interviews | 15 counselors | ≥10 name a funded budget line or reporting need it fits | <5 |
| E2 | **Sponsor LOI test** | 5 employers/community colleges | ≥2 sponsor LOIs (A4) | 0 LOIs |
| E3 | Wizard-of-Oz simulation (facilitator plays client/supervisor from a script; paper or chat) | 30 teens incl. 6 disabled | Usefulness ≥4/5; ≥50% save a next step; accessible completion 100% | Usefulness <3 |
| E4 | Quiz vs simulation comparison | Same teens (counterbalanced) | Simulation preferred by ≥65% | <50% |
| E5 | Authoring cost spike (2 simulations with professional + accessibility review) | 2 scenarios | ≤$8K each; realism ≥4/5 | >$15K each |

**Mapping:** WP1 (verify all [M] competitor facts; buy data), WP2 (5 counselors in interviews as planned), WP4 (E3–E5), WP5 (E2 employer/college LOIs, E1).

## 12. Build handoff

**Epic A: Simulation engine**
- Given a scenario script, When the AI plays a role, Then it stays within the script's allowed facts and ends the role at the scenario's end, And every screen shows "Simulation".
- Given a teen goes off-topic toward personal/relationship talk, Then the role politely returns to the task or ends the scene.

**Epic B: Accessibility**
- Given VoiceOver, When a scenario shows a diagram, Then a structured text alternative is available and all decisions are reachable.
- Given switch access, When a step would normally require precise manipulation, Then an equivalent decision-based step is offered.

**Epic C: Portfolio**
- Given a completed simulation, Then skills are added with evidence links, And the teen can hide or delete any item.

**Epic D: Path compare / next steps**
- Given a ZIP code, When viewing a career, Then local programs with dated sources appear, And no GPS is requested.

**Epic E: Counselor**
- Given a caseload, When exporting, Then the report lists completions and next steps without reflections unless teens shared them.

**NFRs:** web + iOS/Android; Chromebook-first; WCAG 2.2 AA; dated data sources; SOC 2 path; sponsor content isolation.

**QA focus:** AT matrix for every simulation; role-play safety (romance, self-harm, graphic content); bias audit; sponsor-label and contact-rule tests; data freshness checks.

**Platform dependencies:** Lumen; My Needs; AI orchestration (scenario role-play engine with script constraints); Ascendly Record; teacher/counselor console; evidence engine.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Sponsors don't pay | Medium | High | School licence first; E2 gate; grant funding (workforce boards) |
| Authoring cost | Medium | High | Template-based scenarios; start with 8 high-demand fields |
| Role-play drifts into companion-like chat | Low | High | Script constraints; session-bound roles; red-team |
| Incumbent bundling (Naviance/Xello) | High | Medium | Integrate via export; differentiate on doing + accessibility |
| Outdated labour data | Medium | Medium | Dated sources; annual refresh |

**Open questions:** Which 8 fields to launch (local demand × accessibility × sponsor interest)? Can simulations earn micro-credentials recognised by CTE programs? How to serve 13–14s (lighter exploration) without diluting the 15–19 focus?

## 14. Sources
- WEF Future of Jobs 2025 — https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf [V2: raw 05]
- HolonIQ funding climate — https://www.holoniq.com/notes/512m-in-q1-signals-a-slow-start-to-2026-with-capital-continuing-to-favor-ai-enabled-career-aligned-platforms [V2: raw 05]
- Coursera–Udemy merger — research/raw/05-market-and-trends.md [V2]
- PowerSchool breach — research/raw/03-forum-voice-of-customer.md [M]
- EU AI Act Omnibus — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ [V2]
- Naviance, Xello, Scoir, MajorClarity, BigFuture, Roadtrip Nation, CareerVillage, Handshake, Forage — from memory [M]; **verify in WP1** (vendor sites, district procurement records, store pages)
- O*NET / BLS Occupational Outlook Handbook as planned data sources — https://www.onetonline.org/ ; https://www.bls.gov/ooh/ [M]

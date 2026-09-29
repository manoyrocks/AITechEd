# Parent Coach: App Strategy & Product Specification

> **Venture:** Evergrow · **App #:** 5/7 · **Ages:** 25–59 (parents, grandparents and other caregivers of children 1–19) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/04-evergrow-adults.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Evergrow index](README.md)
> **Cross-venture links:** [Lanternling (1–7)](../../vision/01-lanternling-early-years.md) · [Questwise (8–12)](../../vision/02-questwise-tweens.md) · [Ascendly (13–19)](../../vision/03-ascendly-teens.md) · [Wavelength (ND)](../../vision/05-wavelength-neurodivergent.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research note:** Searched 29 Sep 2026. The session's web-search budget ran out before Understood.org, Lovevery and Khan Academy parent tools could be re-checked, so those rows are [M] or taken from repo research. Page fetches were blocked by the egress proxy.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Five-minute lessons and ready-to-use scripts that help you support your child's learning and talk about AI at home, linked (with your child's knowledge) to what they're actually doing in our kids' apps. |
| **Primary user / buyer** | Parents and caregivers aged 25–59 (plus grandparent carers). Buyer: the parent (included free with a paid child plan in Lanternling, Questwise or Ascendly); schools and districts as family-engagement add-ons; employers as a family benefit (V2). |
| **Core job-to-be-done** | "When my child is stuck on homework or starts using AI chatbots, I want a quick, trustworthy way to know what to say and do tonight, so I can help without doing it for them or panicking." |
| **Category on the stores** | Education › Parenting (Lifestyle secondary) |
| **Top competitors (by downloads / revenue)** | Khan Academy (Khanmigo parent tools), Common Sense Media, ClassDojo, ParentSquare, Brightwheel, Lovevery, Kinedu, Huckleberry, Peanut, Bark, Qustodio, Understood.org |
| **Our wedge** | 1) **"Tonight's Script":** coaching tied to the child's *actual* learning moment in our apps, not generic articles. 2) **AI-at-home curriculum** for parents: conversations, not covert monitoring. 3) **Transparency with the child:** teens see what parents see (Lumen P18), unlike surveillance apps. |
| **Business model** | Mainly a **retention and cross-sell engine** (vision). Free with any child plan; stand-alone $4.99/mo or $39/yr; district/school licence as family engagement; employer family benefit (V2). |
| **North-star metric** | Coached moments per active family per week (a script or lesson used and marked "tried it"), and its effect on child-app retention |
| **MVP candidate?** | **Later.** Validate via the Lanternling and Questwise pilots (child-app retention lift). A minimal "Tonight's Script" can ship inside child apps' parent areas first. |

## 2. Problem & users
**Problem statement**
- Kids use AI more than parents realise:
  - Pew (survey fielded Sep–Oct 2025) found 64% of US teens use AI chatbots, but only 51% of parents think their teen does [V].
  - Homework help is a top use (54%) [V].
  - About four in ten parents have not talked to their teen about chatbots [V].
- AI companions are the parental blind spot:
  - Common Sense Media found nearly 3 in 4 teens have used AI companions [V].
  - 23% of parents think kids use AI mainly for companionship, versus 8% who actually do [V].
  - 44% of kids say no parent has talked to them about using AI safely [V].
  - Parents misjudge both how much children use AI and why [I].
- The parent-tool market is fragmented:
  - School communication apps (ClassDojo, ParentSquare, Brightwheel) push notifications.
  - Baby apps (Kinedu, Huckleberry) stop at toddlerhood.
  - Monitoring apps (Bark $99/yr; Qustodio's ChatGPT alerts) scan children's messages [V].
  - The research paper notes that parent-facing content is "scattered" (vision).
- Parents want to help without giving answers. The studio's pedagogy (Socratic hints, Bastani 2025 evidence that unguarded AI hurts learning [V] (repo)) needs parents on board, or kids will route around it with general chatbots [I].

**Personas**
1. **Dana, 38, parent of a 9-year-old** (vision). Wants to help with fractions homework and handle the "can I use ChatGPT?" question. Has 10 minutes after dinner.
2. **Marisol, 34, Spanish-dominant parent with limited literacy, mother of an autistic 6-year-old (Wavelength/Lanternling user).** Needs audio-first, Spanish, plain-language guidance with no jargon, and advice that respects her son's sensory needs.
3. **George, 63, grandfather raising his 14-year-old grandson (caregiver persona).** Low confidence with AI, larger text needed, and wants to "not be the old guy who bans everything". Needs the 60+ preset, simple explanations and conversation starters that work with teens.

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Know what the child is doing | Pew perception gap [V] | Linked child summary (learning, not surveillance) |
| Talk about AI and companions | Common Sense [V] | "AI Talk Kit": age-banded scripts |
| Help with homework without answering | Bastani 2025 (repo) | "Help, don't solve" coaching ladder |
| Time-poor | Vision (audio-first for busy parents) | 5-min audio lessons; one weekly summary |
| Multilingual, low literacy | ClassDojo translation is valued (repo) | Spanish at MVP; audio-first; plain language |
| Trustworthy, vetted | Common Sense brand trust [M] | Vetted knowledge base with sources; expert review |
| Respect for the child's privacy | Lumen P18; UK AADC | Child-visible sharing; no message scanning |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **ClassDojo** | ClassDojo | Millions of users in 180 countries [V2]; top school app (repo) | Free; Plus for parents (repo) | Play listed [V] | Class stories; translation to 35+ languages (repo); **Parent AI tools** incl. a homework helper that reads a worksheet photo and suggests how to help; Dojo Tutor highlights [V] | Notification overload; privacy (repo) | Translation helps multilingual families | [ClassDojo AI transparency](https://help.classdojo.com/hc/en-us/articles/34969247491341-Parent-AI-Transparency-Note) |
| **Khan Academy / Khanmigo** | Khan Academy | Khanmigo 2M users globally (2024–25) [V2] (repo) | Khanmigo ~$4/mo for parents/learners (repo) | High (repo) | Trusted nonprofit; parent dashboard [M]; Socratic AI | Khanmigo errors (repo); mobile has fewer features | Fully accessible with VoiceOver (repo) | repo raw/05 |
| **Common Sense Media** | Common Sense (nonprofit) | Leading US family media-ratings brand [M]; AI research reports [V] | Free; donation/membership [M] | n/a | Age ratings; AI risk assessments; research | Web-first; articles rather than coaching [I] | Web standard | [Common Sense AI research](https://www.commonsensemedia.org/research/a-comprehensive-report-on-teens-tweens-and-ai) |
| **Bark** | Bark Technologies | Major US monitoring app [M] | Premium $14/mo or $99/yr; Jr $5/mo or $49/yr [V] | Trustpilot listed [V] | AI flags risky content so parents needn't read everything [V] | Teen privacy; bypassable [M] | Parent-only view | [bark.us/pricing](https://www.bark.us/pricing/) |
| **Qustodio** | Qustodio | Major monitoring app [M] | Subscription [M] | App Store listed [V] | AI message alerts; **ChatGPT conversation alerts** with summaries [V] | Surveillance concerns; teen trust [I] | Parent-only | [Qustodio ChatGPT alerts](https://www.qustodio.com/en/blog/introducing-chatgpt-alerts/) |
| **Kinedu** | Kinedu | 5M+ Play downloads (~7.1M) [V2] | ~$7/mo after a 7-day trial [V2] | High [M] | Daily developmental activities 0–4 | Paywall; ends at toddlerhood | Video activities | [kinedu.com](https://www.kinedu.com/) |
| **Huckleberry** | Huckleberry Labs | Leading baby-sleep app [M] | Plus $11.99/mo or $68.88/yr; Premium $14.99/mo or $119.88/yr [V] | App Store high [M] | Sleep predictions; expert plans | Premium upsell; free tier thin [V2] | Night-mode friendly [M] | [huckleberrycare.com/pricing](https://huckleberrycare.com/pricing) |
| **Understood.org** | Understood (nonprofit) | Leading learning-differences resource [M] | Free [M] | n/a | Expert, affirming ADHD/dyslexia content; podcasts [M] | Not personalised [I] | Good accessibility reputation [M] | [M] |

Also noted: **Brightwheel** (childcare check-ins, daily reports, billing [V]); **ParentSquare** (district communications [M]); **Lovevery** (play kits with stage-based app guidance [M]); **Peanut** (parent social network [M]).

### Feature matrix
| Feature | ClassDojo | Khan/Khanmigo | Common Sense | Bark/Qustodio | Kinedu/Huckleberry | Understood | **Our decision** |
|---|---|---|---|---|---|---|---|
| Short parent lessons (≤5 min) | ✗ | partial | partial | ✗ | ✓ | partial | **Parity** |
| Scripts for tonight's situation | ✗ | ✗ | partial | ✗ | partial | ✓ | **Improve:** tied to the child's actual activity |
| Linked to child's learning data | ✓ (class) | ✓ | ✗ | ✗ | ✓ (baby log) | ✗ | **Differentiate:** across 3 age ventures, child-visible |
| Homework coaching (help without answers) | ✓ (worksheet helper) [V] | ✓ | ✗ | ✗ | ✗ | partial | **Parity+** with the Socratic ladder |
| AI-safety conversation curriculum | ✗ | partial | ✓ (research/tips) | partial (alerts) | ✗ | ✗ | **Differentiate** |
| Covert scanning of child messages / AI chats | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | **Reject:** surveillance erodes trust; not our role |
| Multilingual + audio-first | ✓ (translation) | partial | partial | ✗ | partial | partial | **Improve:** Spanish audio at MVP |
| Learning differences guidance | ✗ | ✗ | partial | ✗ | ✗ | ✓ | **Parity** via Wavelength and expert partners |
| Notification-heavy engagement | ✓ | ✗ | ✗ | ✓ | partial | ✗ | **Reject:** one weekly summary, opt-in nudges only |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| F1 | **Tonight's Script** ★ signature | When the child finishes a session in a studio app, the parent gets (opt-in, once a day max) a 3-line script: what they worked on, one question to ask, one screen-free follow-on. It uses Lumen co-play cards. | Vision; ClassDojo homework helper [V] | Differentiate | MVP | Must |
| F2 | **5-minute lessons** | Human-written, audio-first lessons: "How to help without giving the answer", "Productive struggle", "Reading at bedtime", "Math anxiety". Age-banded 1–3, 4–7, 8–12, 13–19. | Vision | Parity | MVP | Must |
| F3 | **AI Talk Kit** ★ | Conversation guides on chatbots, AI companions, deepfakes, AI and homework honesty, and privacy, with age-specific scripts and a family AI agreement template | Pew/Common Sense gaps [V] | Differentiate | MVP | Must |
| F4 | **Ask Parent Coach** | Q&A answered from a vetted knowledge base with citations; says "I don't know" and refers out (paediatrician, school) when outside scope | Vision AI role | Improve | MVP | Must |
| F5 | **Linked child summary** | Weekly one-screen summary from Lanternling/Questwise/Ascendly: skills practised, what went well, what to encourage. **Teens (13+) see exactly what the parent sees** and can add a note. | Lumen P14/P18 | Differentiate | MVP | Must |
| F6 | **Homework coach ladder** | Parent photographs a worksheet (optional); the coach suggests a hint ladder for the *parent* to use and never the final answer | Socratic policy (repo) | Improve | MVP | Should |
| F7 | **Multi-caregiver sharing** | Invite a co-parent, grandparent or nanny with role-based views | Lumen P14 | Parity | MVP | Must |
| F8 | **My Needs (parent) + 60+ preset** | Audio-first, Spanish, plain language, large type | Marisol/George personas | Lumen | MVP | Must |
| F9 | **Learning-differences lens** | Tips adjusted to the child's My Needs profile (e.g., sensory-friendly homework set-up) without labels or diagnosis requirements | Wavelength bridge | Differentiate | MVP | Should |
| F10 | **Calm notifications** | One weekly summary by default; Tonight's Script opt-in; never sent to the child's device | Lumen 3.4 | Lumen | MVP | Must |
| F11 | Expert live Q&A | Monthly captioned sessions with educators, SLPs and paediatric experts | Trust | Improve | V1 | Should |
| F12 | School/district edition | Family-engagement licence; translated; aligned with the school's AI policy | B2B | Differentiate | V1 | Should |
| F13 | More languages | Mandarin, Arabic, Vietnamese, Haitian Creole | Equity | Parity | V1 | Should |
| F14 | Employer family benefit | Bundle with Evergrow employer plans | B2B2C | Differentiate | V2 | Could |

MVP = F1–F10.

## 5. Core experience & key user flows
**Core loop.** Child finishes a session → parent gets Tonight's Script (opt-in) → 2-minute conversation at dinner → parent taps "tried it" (optional) → weekly summary → a 5-minute lesson suggested for the weekend → end.

**Flow 1: Onboarding (≤5 min)**
1. Sign in with the same account as the child plan (passkey or Apple/Google).
2. My Needs: language (EN/ES), audio-first, text size.
3. Add children (age band only is enough; linking to a child app profile is optional).
4. Pick 1 worry ("homework battles", "AI chatbots", "screen time", "reading").
5. A first 3-minute audio lesson plays, with its transcript. First value.

**Flow 2: Tonight's Script**
1. Notification: "Maya practised equivalent fractions today. Tap for tonight's idea." Opt-in; quiet hours respected.
2. Card: what she did (1 line), one question ("Can you show me how 1/2 and 2/4 are the same with pizza?"), one screen-free activity.
3. Optional "tried it" or "not tonight". No guilt, no streak.

**Flow 3: AI Talk Kit**
1. Choose the child's age band and topic ("AI friends and companions").
2. Read or listen to a 4-min primer.
3. Script with 3 openers, likely responses and follow-ups.
4. Optional family AI agreement template, which can be printed or shared, and co-signed in Ascendly by teens.

**Flow 4: Caregiver/teacher view.** Invite a grandparent (large-type view) or nanny (limited view). School edition: a teacher can send a "family tip" that appears as a script.

**Flow 5: My Needs.** One tap from any screen. Also sets the notification schedule.

**Flow 6: Billing.** Included with child plans (clearly stated). Stand-alone plan: price before trial, reminder, one-tap cancel, pause over summer.

**IA.** Today · Lessons · AI Talk Kit · Ask · My kids (summaries) · My Needs.

**Session design.** 2–5 minutes; audio-first with a transcript; an end card with "That's it for today".

## 6. Inclusive, accessible & sensory design spec
- **Sensory Dial.** Default **Calm** (parents are often multitasking or near a sleeping child): no sounds, dark-mode friendly, no animation. Balanced adds soft transitions.
- **Input modes.** Tap, voice questions in Ask, keyboard, screen reader, and a photo of a worksheet (optional, with a typed alternative).
- **Targets.** ≥48 dp; **≥56 dp in the 60+ preset** (George).
- **Typography.** 18 px body; plain language at ≤ grade 6 by default (Marisol), with a reading-level dial; dyslexia settings.
- **Audio.** All lessons human-narrated in EN and ES with captions and transcripts; speed 0.75–1.5×; separate voice volume; hearing-aid streaming via the OS.
- **Text path.** Ask accepts typing; every audio item has a transcript.
- **Themes.** "Home" (warm) and "Plain" (neutral). No cartoon-baby aesthetic for parents of teens.

| # | Principle | Acceptance criterion in Parent Coach |
|---|---|---|
| P1 | Calm | Calm default; 0 animations with Reduce Motion |
| P2 | Sound | No sounds by default; captions on all audio |
| P3 | Predictable | Script card format fixed (Did / Ask / Try) |
| P4 | Targets | 48/56 dp |
| P5 | Plain language | Default ≤ grade 6; audio for every instruction |
| P6 | Typography | WCAG 1.4.12 passes |
| P7 | Multimodal | Audio, text, voice question, typed question |
| P8 | Low penalty | No streaks; "not tonight" is a valid choice |
| P9 | Focus | Max 1 Tonight's Script per day; weekly summary; designed end |
| P10 | Memory | Passkeys; shared family account without password sharing |
| P11 | Timing | Nothing timed |
| P12 | My Needs | Parent and child profiles linked, each owner-controlled |
| P13 | Age-respectful | Teen-appropriate language in 13–19 scripts |
| P14 | Low admin | Linked summary set up in ≤5 min; multi-caregiver invites |
| P15 | Motivation | No loss framing, no parent leaderboards |
| P16 | Affirming | Learning-differences content reviewed by the ND advisory panel; identity-first/person-first choice |
| P17 | Honest claims | No "raise your child's grades" claims without evidence |
| P18 | Privacy | Child data shared under the child venture's consent; teens see parent view; no message scanning |

**Lumen audit target:** 24/24.

## 7. AI specification & guardrails
**Does**
- Retrieval-augmented Q&A over a vetted knowledge base (studio-authored lessons plus licensed expert sources), with citations.
- Personalising scripts to the child's age, activity and My Needs.
- Worksheet understanding (vision model) to suggest *parent* hints.
- Translation reviewed by native-speaking editors for published lessons.

**Does not**
- Diagnose (ADHD, autism, dyslexia, mental health) or give medical advice. It refers out.
- Read the child's chats or AI conversations.
- Provide homework answers.
- Act as a parent's companion or therapist.

**Safety**
- If a parent reports a child in danger (self-harm, abuse, sextortion), show crisis resources immediately (e.g., 988 in the US) and relevant reporting routes, with human-reviewed copy.
- Hallucination control: answers must cite a KB passage or say "I'm not sure".
- Weekly human review of 3% of Q&A.

**Evaluation**
- 400-question gold set (EN/ES) rated by educators and a paediatric adviser: accuracy ≥95%, harmful-advice rate 0 in the red-team set.
- Readability checks.
- Bias check on family structures (single parents, same-sex parents, grandparent carers) and income assumptions (no "buy X" advice).

**Cost [E].** ~$0.10–0.30 per active parent per month (RAG + TTS caching; lessons are pre-recorded).

## 8. Data, privacy & compliance
| Data | Purpose | Retention | Processing |
|---|---|---|---|
| Parent account, language, My Needs | Service | Until deletion | Cloud |
| Child summary (derived from child apps) | Linked coaching | 12 months rolling | Cloud; minimal fields (skills, not raw answers) |
| Worksheet photos | Hint generation | Deleted after processing | Cloud, zero retention |
| Ask questions | Answers, QA | 90 days | Cloud |

**Regimes.**
- **COPPA 2025** for children under 13: the linked summary relies on verifiable parental consent collected by the child app. A **separate consent** covers sharing the child's data with other caregivers; there is no ad or AI-training use of child data.
- FERPA/SOPIPA when the school edition uses school data.
- UK AADC and state design codes: no nudges on the child side.
- GDPR/GDPR-K.
- FTC §5.
- EU AI Act Art. 50.

**Teen transparency.** 13–17s in Ascendly see the parent view and receive notice when a new caregiver is added, consistent with Lumen P18.

**Store.** The parent app is not in the Kids category (adult audience), but it follows Families-policy data practices for any child-derived data.

## 9. Monetization & go-to-market
| Offer | Price | Benchmark |
|---|---|---|
| Included with any child plan | $0 | ClassDojo free core [V2] |
| Stand-alone | $4.99/mo or $39/yr | Khanmigo ~$4/mo (repo); Kinedu ~$7/mo [V2] |
| School/district family engagement | $2–4 per student per year | [E] |
| Employer family benefit (V2) | $2–3 per employee per month | [E] |

- **Channels:** built into child apps (primary); schools adopting Questwise/Ascendly; paediatric and library partners; employer ERGs (parents' networks).
- **ASO:** "help child with homework", "talk to kids about AI", "parenting tips AI safety", "consejos para padres tareas".
- **Markets:** US (EN/ES) first; UK V1.

## 10. Success metrics
- **North star:** coached moments per active family per week (target ≥1.5).
- **Inputs:** Tonight's Script opt-in (≥50% of linked parents); "tried it" rate (≥35%); lessons completed per month (≥3); AI Talk Kit usage (≥40% of parents of 8+).
- **Outcomes:**
  - child-app 30-day retention for families with an active parent vs. without (target +5 points)
  - parent self-efficacy (short scale)
  - "we talked about AI" reported by child and parent
  - Evidence plan: A/B in the Lanternling and Questwise pilots (Tier 2).
- **Guardrails:** Sensory Comfort ≥4/5; notification opt-out <15%; teen "feel watched" item ≤ baseline; zero child-data incidents.
- **Retention:** parent MAU / linked families ≥45%; D30 ≥30% (engine, not stand-alone).

## 11. Validation plan
**Riskiest assumptions**
1. The app works as a retention and cross-sell engine (vision).
2. Parents act on scripts.
3. Linking child data is acceptable to parents and teens.
4. Spanish/audio-first reaches lower-literacy families.

| # | Experiment | Sample | Success | Kill |
|---|---|---|---|---|
| X1 | **Retention A/B in the Lanternling & Questwise pilots:** concierge Tonight's Scripts sent by SMS/email written by an educator | 60 families (30/30) | +5 pts child-app D30 in the script arm | No difference |
| X2 | Script usability diary | 15 parents (incl. 5 ES-dominant, 3 grandparent carers) | ≥60% "tried it" at least twice a week | <30% |
| X3 | Teen transparency concept test | 12 teen–parent pairs (consent + assent) | ≥70% of teens say the shared view is fair | <50% |
| X4 | AI Talk Kit value test (landing page, parents) | Paid social to adults | ≥8% signup | <3% |
| X5 | School family-engagement interest | 8 schools already piloting Questwise/Ascendly | ≥3 will co-fund | 0 |

**Mapping.** WP2 (parent interviews in the Lanternling/Questwise samples), WP4 (X1–X3), WP5 (X4–X5).

## 12. Build handoff
**Epic A: Tonight's Script**
- Given a linked child finishes a session and the parent opted in, when quiet hours are not active, then at most one script notification is sent per day, and never to the child's device.
- Given the parent taps "not tonight", then no follow-up nudge is sent that day.

**Epic B: Ask Parent Coach**
- Given a question outside the KB, then the answer states uncertainty and gives a referral, with no uncited claims.
- Given a crisis phrase, then crisis resources appear at the top within the first response.

**Epic C: Linked summary & consent**
- Given a teen (13+) profile, when a parent opens the summary, then the teen's app shows the identical summary and a "seen by" note.
- Given a caregiver is removed, then their access ends within 1 minute.

**Epic D: Accessibility & language**
- Given Spanish selected, then 100% of lessons have Spanish audio and transcripts reviewed by a native editor.

**Non-functional requirements**
- Offline download of lessons.
- iOS, Android and web.
- WCAG 2.2 AA.
- EN/ES.
- Child-data segregation; the privacy stack is shared with the child ventures.

**QA focus**
- AT matrix: VoiceOver, TalkBack, and large-text 200% for the 60+ preset.
- COPPA test cases: consent inheritance, deletion propagation, no child data to third parties.
- AI safety: medical/diagnosis prompts, homework-answer extraction, crisis prompts.
- Billing: "included with child plan" clarity; stand-alone cancel.

**Dependencies.** Child ventures' event API (skill-level only), shared consent ledger, Lumen co-play cards, My Needs, RAG service.

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Parents ignore it (notification fatigue) | High | Med | One per day max; high relevance; test in pilots |
| Pressure to add monitoring features | Med | High | Clear positioning; refer to OS parental controls for filtering |
| Child-data leakage across ventures | Low | High | Minimal fields; consent ledger; audits |
| Advice errors (medical/developmental) | Med | High | KB-only answers; expert review; referrals |
| Stand-alone revenue small | High | Low | Treat as engine; measure retention lift |

**Open questions.** Should Parent Coach live inside each child app rather than as a separate app? What do teens accept being shared? Can schools fund it from family-engagement budgets?

## 14. Sources
- [V] Pew Research, teens and AI chatbots (Dec 2025 / Feb 2026): https://www.pewresearch.org/internet/2026/02/24/what-parents-say-about-their-teens-ai-use/ · https://www.pewresearch.org/wp-content/uploads/sites/20/2025/12/PI_2025.12.09_Teens-Social-Media-AI_REPORT.pdf
- [V] Common Sense Media, AI companions and 2026 census: https://www.commonsensemedia.org/press-releases/nearly-3-in-4-teens-have-used-ai-companions-new-national-survey-finds · https://www.commonsensemedia.org/sites/default/files/research/report/2026-ai-use-by-tweens-and-teens-1.pdf
- [V] ClassDojo Parent AI tools: https://help.classdojo.com/hc/en-us/articles/34969247491341-Parent-AI-Transparency-Note
- [V] Bark pricing: https://www.bark.us/pricing/ · [V] Qustodio ChatGPT alerts: https://www.qustodio.com/en/blog/introducing-chatgpt-alerts/
- [V] Huckleberry pricing: https://huckleberrycare.com/pricing · [V2] Kinedu: https://www.kinedu.com/ · https://www.appbrain.com/app/kinedu-baby-development/com.kinedu.appkinedu
- [V] Brightwheel: https://mybrightwheel.com/childcare-app/
- [M] Understood.org, Lovevery, Peanut, ParentSquare, Common Sense membership model (not re-verified; search budget exhausted)
- Repo: research/raw/05 (Khanmigo metrics and pricing, Bastani 2025, COPPA 2025), raw/01 (ClassDojo), docs/02 (co-play cards, gentle progress)

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Re-scope → Studio Family Hub (cross-venture caregiver app) |
| **Ships in** | Studio Family Hub (S9) |
| **Build wave** | 1b |
| **Pre-discovery priority score** | 79/100 [I] |
| **Consumes engines** | EN-01, EN-10, EN-12 |
| **Studio features used** | SX-01, SX-04, SX-08, SX-27, SX-28, SX-29 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = F1, F2, F3, F5, F7.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| PC-E1 | **IEP/EHCP Prep Coach** | Plain-language report explainer, meeting question builder and progress-evidence pack (SX-27). |
| PC-E2 | **Caregiver wellbeing & peer support** | Moderated groups, respite finder and a self-report burnout check (SX-28). |
| PC-E3 | **Family Digest home** | The single weekly summary across all children (SX-04). |

### 15.3 New validation question
IEP Prep Coach concierge with ND parents, n=15: ≥70% feel 'more prepared'.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 4 | 5 | 3 | 3 | 4 | 4 | 5 |

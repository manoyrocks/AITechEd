# AITechEd: AI EdTech Startup Studio (Discovery & Validation Phase)

> **Status:** Research and planning only. **No code** is written in this phase.
> **Date:** 29 September 2026

This repository holds the research, the vision documents and the validation plan for a studio of **five AI-powered EdTech startups** with **seven apps each (35 app concepts)**. Four of the startups together cover every life stage from toddler to older adult. The fifth is dedicated to **neurodivergent children**: autistic, ADHD/ADD, dyslexic and others.

The whole initiative puts **intuitive, accessible UX and sensory-inclusive design** at its core.

---

## How the research was done
Five AI research agents ran in parallel, one per research stream:

| # | Stream | Raw output |
|---|---|---|
| 1 | Top 30 learning apps on **Google Play** | [research/raw/01-google-play-top30.md](research/raw/01-google-play-top30.md) |
| 2 | Top 30 learning apps on the **Apple App Store** | [research/raw/02-apple-app-store-top30.md](research/raw/02-apple-app-store-top30.md) |
| 3 | Learning apps most discussed in **forums and communities**, with voice of customer | [research/raw/03-forum-voice-of-customer.md](research/raw/03-forum-voice-of-customer.md) |
| 4 | **Neurodivergent/special-needs** landscape, plus **inclusive and sensory UX** evidence | [research/raw/04-neurodivergent-and-inclusive-ux.md](research/raw/04-neurodivergent-and-inclusive-ux.md) |
| 5 | **Market, trends, regulation and funding** | [research/raw/05-market-and-trends.md](research/raw/05-market-and-trends.md) |

The five outputs were combined into one research paper and a categorized catalog of 83 apps. Age segments are **1–3, 4–7, 8–12, 13–19, 20–34, 35–59, 60+**, plus a neurodivergent overlay.

**Confidence tags** used throughout:

| Tag | Meaning |
|---|---|
| **[V]** | Verified this session |
| **[V2]** | Secondary source |
| **[M]** | From memory, not re-verified |
| **[E]** | Estimate |
| **[I]** | Inference |

Network limits in the research environment blocked direct page fetches, including Reddit, the app store pages and Sensor Tower. So several figures are marked for verification in Discovery work package 1.

## Documents

| Document | What it is |
|---|---|
| **[docs/01-research-paper.md](docs/01-research-paper.md)** | The research paper: methods, unified top-30, forum favorites, categorization by age, voice of customer (top 15 unmet needs), accessibility and sensory audit, neurodivergent landscape, regulation, opportunities, and the studio proposal |
| **[docs/02-inclusive-sensory-ux-framework.md](docs/02-inclusive-sensory-ux-framework.md)** | **"Lumen"**, the studio-wide inclusive and sensory UX framework: 18 principles with acceptance criteria, the Sensory Dial, the "My Needs" profile, per-age UX parameters, safe-AI rules, and the accessibility audit rubric |
| **[docs/vision/](docs/vision/)** | Five startup vision documents, each with personas, needs mapping, **seven app concepts**, business model, ethics, risks and validation focus |
| **[docs/discovery/discovery-validation-plan.md](docs/discovery/discovery-validation-plan.md)** | The 16-week discovery and validation plan: work packages, sample sizes, no-code prototyping (paper, Figma, Wizard-of-Oz, concierge), the sensory A/B protocol, prioritization scorecard, ethics, pre-registered thresholds, budget and gates |
| **[research/app-catalog.csv](research/app-catalog.csv)** | Categorized catalog of 83 apps: segment, subject, model, accessibility and sensory notes, top complaint, confidence |

## The five ventures (working names, pending trademark screening)

| Venture | Segment | Thesis | Seven apps |
|---|---|---|---|
| 🏮 **[Lanternling](docs/vision/01-lanternling-early-years.md)** | 1–3 & 4–7 | Calm, voice-first, co-play-first early learning that stops by itself | Babble Buddy · Tap & Wonder · Story Lantern · Sound Garden · Number Nest · Calm Cubs · Two Words |
| 🧭 **[Questwise](docs/vision/02-questwise-tweens.md)** | 8–12 | A COPPA-safe Socratic tutor and mastery worlds, with no pay-to-win | Sage Tutor · Math Realms · Read Rangers · Builder's Lab · AI Detectives · Wonder Lab · Mission Control |
| 🧗 **[Ascendly](docs/vision/03-ascendly-teens.md)** | 13–19 | AI-native learning, not cheating: proof-of-learning and future pathways | Study Coach · Exam Ready · Explain It Back · Draft Mentor · Study Squad · Pathfinder · Life Ready |
| 🌲 **[Evergrow](docs/vision/04-evergrow-adults.md)** | 20–34, 35–59, 60+ | Hands-on AI fluency and lifelong learning, with humans in the loop | AI Fluency Lab · Career Sprint · Speak Freely · Lead with AI · Parent Coach · Silver Circuit · Curiosity Circle |
| 🌊 **[Wavelength](docs/vision/05-wavelength-neurodivergent.md)** | Neurodivergent children (≈2–17) | A neurodiversity-affirming, sensory-friendly suite for communication, regulation, learning and independence | Wavelength Day · Wavelength Voice · Calm Harbor · ReadWave · Focus Crew · Social Compass · Spark Switch |

**Shared studio platform** (specified during discovery):
- the Lumen inclusive design system and Sensory Dial
- a portable "My Needs" profile
- guardrailed AI (tutor, not friend; Socratic by default; human-reviewed content)
- a privacy and child-safety stack (COPPA 2025, AADC, FERPA, EU AI Act)
- an evidence engine
- a fair-billing charter

## Key findings at a glance
1. **The market leaders are habit machines and answer engines.** Examples: Duolingo (178M downloads in 2025) and Gauth (51M). **Paywall and billing anger** is the number-one complaint almost everywhere.
2. **Coverage by age is uneven.**
   - **Under-served:** ages 1–3, 8–12 and 60+.
   - **Teens:** plenty of answer apps, too little that builds real learning.
   - **Neurodivergent learners:** a fragmented market with little evidence behind it.
3. **Frontier labs now give Socratic tutoring away for 13+/18+.** Startups have to win on the learners the labs avoid, on teaching method, on trust and on proven outcomes.
4. **No top-30 app combines three things:** screen-reader-ready learning exercises, dyslexia-friendly type and a real low-sensory mode. **Inclusive, calm design is the moat.**
5. **Regulation is tightening,** and it favors this studio's design stance:
   - COPPA 2025 applies in full.
   - The EU AI Act bans emotion recognition in education.
   - The FTC is scrutinizing AI companion apps.
   - The AAP's 2026 guidance puts the responsibility on product design.

## Next step
Run the **[16-week Discovery & Validation Plan](docs/discovery/discovery-validation-plan.md)**:
- Gate 1 (problem validation) at week 8.
- Gate 2 (build / pivot / kill and venture sequencing) at week 16.

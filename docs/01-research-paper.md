# Learning Apps Across the Lifespan: Market, User and Inclusive-Design Research for an AI EdTech Startup Studio

**Research paper, Discovery & Validation Phase, v1.0**
**Date:** 29 September 2026
**Status:** Planning only. No code is written in this phase.
**Companion documents:**
- [Inclusive & Sensory UX Framework](02-inclusive-sensory-ux-framework.md)
- [Five vision documents](vision/)
- [Discovery & Validation Plan](discovery/discovery-validation-plan.md)
- [App catalog (CSV)](../research/app-catalog.csv)
- [Raw research files](../research/raw/)

---

## Abstract

We ran five parallel research streams, each handled by one AI research agent:
1. Google Play top-30 learning apps
2. Apple App Store top-30 learning apps
3. The ~30 learning apps most discussed in online communities, plus voice-of-customer evidence
4. The neurodivergent and special-needs EdTech landscape, plus evidence-based inclusive and sensory UX
5. Market size, trends, regulation and funding

We merged 83 distinct apps into one catalog. Each app is tagged with an age segment: **1–3, 4–7, 8–12, 13–19, 20–34, 35–59, 60+**, plus a **neurodivergent overlay**.

The market is led by "habit machines" (Duolingo: 178M downloads in 2025, 58.7M DAU in Q2 2026) and fast-growing **AI answer engines** (Gauth: 51M downloads in 2025).

The same leaders show the category's biggest weaknesses:
- **paywall and billing anger**, the top complaint in almost every leading app
- **gamification that punishes users** (Duolingo's 2025 Energy backlash)
- **AI answer-getting that weakens learning** (Bastani et al., *PNAS* 2025: −17% on unassisted exams)
- **poor accessibility and sensory design**: no top-30 app offers a real low-sensory mode, dyslexia-friendly typography by default, or dependable screen-reader support in learning exercises

Coverage is uneven by age:
- **Ages 1–3, 8–12 and 60+ are clearly under-served.**
- Teens are **over-served with answers and under-served with learning**.
- Neurodivergent learners, including 1 in 31 US 8-year-olds diagnosed autistic and 11.4% of US 3–17-year-olds diagnosed with ADHD, get a fragmented market with little evidence behind most products.

Frontier AI labs now give Socratic tutoring away free to people aged 13+/18+. A startup therefore cannot win on generic tutoring. It can win on:
1. learners the labs avoid (under-13s, neurodivergent children, seniors)
2. depth of teaching method
3. trusted distribution
4. published evidence that learners improve
5. **inclusive, calm design** as a core product value, not a setting

On these findings we propose a studio of **five ventures with seven apps each (35 apps)**: four covering ages 1 to 60+, and one for neurodivergent children. All five share an inclusive design system, a privacy-by-default child-safety stack and an evidence engine. This paper documents the evidence. The vision documents describe the ventures. The discovery plan sets out how we will test the ideas before any code is written.

---

## 1. Introduction and research questions

**Studio thesis.** Learning apps are among the most downloaded software in the world. Yet many are built to maximize engagement and conversion rather than learning, and most exclude learners with disabilities or sensory sensitivities. Generative AI changes both what is possible (voice-first tutoring for pre-readers, adaptive scaffolds, AAC phrase support) and what is risky (answer-getting, companion chatbots, children's data).

**Research questions**
| # | Question | Where answered |
|---|---|---|
| RQ1 | Which learning apps lead downloads on Google Play and the Apple App Store, and which are most discussed and recommended in communities? | §4 |
| RQ2 | Which age segment does each app serve, and where are segments over- or under-served? | §4.4, §9 |
| RQ3 | What do users (learners, parents, teachers, clinicians) need and want, and what frustrates them? | §5 |
| RQ4 | How accessible and sensory-inclusive are today's leaders? | §6 |
| RQ5 | What does the special-needs and neurodivergent landscape look like, and how should a new entrant position itself? | §7 |
| RQ6 | What market, regulatory and funding conditions shape viable ventures? | §3, §8 |
| RQ7 | Which ventures and apps should the studio take into discovery and validation? | §10 |

---

## 2. Methodology

### 2.1 Multi-agent research design
Five AI research agents ran in parallel. Each had one mandate and wrote a raw report:

| Stream | Mandate | Raw file |
|---|---|---|
| S1 | Top-30 learning apps on Google Play (global, US notes) | [`01-google-play-top30.md`](../research/raw/01-google-play-top30.md) |
| S2 | Top-30 learning apps on the Apple App Store (US-primary) | [`02-apple-app-store-top30.md`](../research/raw/02-apple-app-store-top30.md) |
| S3 | Forum-favored apps and voice of customer: Reddit via secondary sources, HN, Common Sense, Trustpilot, teacher and parent blogs | [`03-forum-voice-of-customer.md`](../research/raw/03-forum-voice-of-customer.md) |
| S4 | Neurodivergent and special-needs apps, and the evidence base for inclusive and sensory UX | [`04-neurodivergent-and-inclusive-ux.md`](../research/raw/04-neurodivergent-and-inclusive-ux.md) |
| S5 | Market size, business-model benchmarks, trends, cautionary tales, regulation, funding | [`05-market-and-trends.md`](../research/raw/05-market-and-trends.md) |

The studio lead then synthesized the five reports:
- de-duplicated apps across lists
- assigned one primary age segment to each app (plus secondaries)
- triangulated needs across the three evidence types (store data, reviews, forums)
- mapped each gap to a venture

### 2.2 Age segmentation
- **Primary segments:** 1–3 (toddlers), 4–7 (preschool and early primary), 8–12 (middle childhood / tweens), 13–19 (teens), 20–34 (young adults), 35–59 (mid-life), 60+ (older adults).
- **Neurodivergent (ND) overlay** across all ages: autism, ADHD/ADD, dyslexia, dyspraxia/DCD, sensory processing differences, speech and language delay, intellectual disability.
- When an app is used mostly by a caregiver or teacher on behalf of a child (for example, ClassDojo), it is filed under **the child's segment**, and the adult user is noted.

### 2.3 Evidence confidence tags
All raw files use explicit tags, and this paper keeps them where it matters:
- **[V]**: verified this session through a search result or snippet with a URL
- **[V2]**: secondary or vendor source
- **[M]**: analyst memory, not re-verified
- **[E]**: estimate or derived figure
- **[I]**: inference

### 2.4 Limitations (read before citing externally)
1. **Direct page fetches were blocked** by the network egress proxy for most domains: Play and App Store listings, Sensor Tower, Appfigures, Reddit, NN/g, FTC, Wikipedia. Figures come from search-result snippets of those sources, company filings, or analyst knowledge.
2. **Reddit could not be read directly.** Forum sentiment is second-hand, through articles and review sites that quote threads. No quotes were invented.
3. **Download rankings are composite estimates.** Play install bands are lifetime thresholds, and App Store figures are ranges.
4. Market-size figures for kids' learning apps, assistive tech and ABA services are **low-confidence [M]**.
5. **Discovery work package 1** in the [Discovery Plan](discovery/discovery-validation-plan.md) lists these verification tasks. The main ones are a direct Reddit pull, a Sensor Tower/Appfigures export, and a hands-on accessibility audit of the top apps.

---

## 3. Market context (headline numbers)

| Indicator | Figure | Tag |
|---|---|---|
| Education-app downloads, 2025 | >1B downloads; ~800M users | [V2] Business of Apps |
| Consumer education-app IAP revenue, 2025 | ~$6.4B (+6.7% YoY); North America 42% of spend. Duolingo ≈ $1B of it | [V2] |
| Language-learning apps | 327M downloads, $1.54B IAP (2025) | [V2] |
| Global EdTech | $163.5B (2024) → $348B (2030), 13.3% CAGR | [V] Grand View |
| AI in education | $5.9B (2024) → $32.3B (2030), 31% CAGR | [V] Grand View |
| Corporate training | ~$427B (2025) | [V] Grand View |
| Duolingo Q2 2026 | 58.7M DAU, 140.6M MAU (DAU/MAU 41.7%), 12.7M paid subs (9% of MAU), $298.5M revenue | [V] SEC filing |
| EdTech VC | $16.7B (2021 peak) → $2.4–2.6B (2025) → ~$1.0B H1 2026 (−26% YoY) | [V] HolonIQ |
| Europe "learning & work" VC | €1.6B (2025); €1.4B H1 2026 | [V] Brighteye |
| Autism prevalence (US, age 8) | 1 in 31 (CDC 2025, 2022 data) | [V] |
| ADHD prevalence (US, 3–17) | 11.4% ever diagnosed; ~1 in 3 untreated | [V] |
| Dyslexia | 5–20% depending on definition | [V2] |

**How to read these numbers [E].** Top-down "EdTech" totals mix enterprise LMS, hardware and services. The pools this studio can actually reach are:
- ~$6–7B in consumer app IAP
- K-12 supplemental and ESA/homeschool budgets
- the part of the $400B+ corporate-training pool being moved to AI upskilling
- funded special-needs provision (IDEA, Medicaid, EHCP, ESA disability awards)

---

## 4. Findings: the top learning apps

### 4.1 Unified top 30 (composite of both stores)
**Method.** Rank by 2025 all-platform downloads where published (Appfigures via Business of Apps). Then use Play install band and US App Store TTM download estimates. Then review volume. General-purpose AI assistants (ChatGPT, Gemini, Claude, Copilot) are excluded from the ranking and discussed in §4.3.

| # | App | Publisher | Signal | Subject | Primary age (secondary) | Model |
|---|---|---|---|---|---|---|
| 1 | Duolingo | Duolingo | 500M+ Play; 178M dl 2025; 4.7★ | Languages, math, music, chess | 20–34 (13–19, 35–59) | Freemium, Energy limit; Super/Max subs |
| 2 | Seekho | Seekho (India) | 100M+; 92M dl 2025 | Micro-learning video (careers, money) | 20–34 (13–19, 35–59) | Low-price subscription |
| 3 | Gauth | ByteDance | 100M+; 51M dl 2025; #1 US Education days | AI homework solver | 13–19 (8–12, 20–34) | Freemium, Plus ~$12/mo |
| 4 | Learna | Codeway | 50M+; 32M dl 2025; #2 US Education 2026 | AI English tutor | 20–34 (35–59) | Hard paywall, weekly plans |
| 5 | Google Classroom | Google | 100M+; 30M dl 2025 | LMS | 13–19 (8–12) | Free / Workspace |
| 6 | Quizlet | Quizlet | 50M+; 26M dl 2025 | Flashcards, AI study | 13–19 (20–34) | Freemium, Plus $35.99/yr |
| 7 | Minecraft Education | Microsoft | 50M+; 23M dl 2025 | STEM, coding | 8–12 (13–19) | School license |
| 8 | Impulse | Headway/Gen.tech | 22M dl 2025 | Brain training | 35–59 (20–34, 60+) | Weekly/annual subs |
| 9 | Photomath | Google | 100M+; 19M dl 2025 | Math solver | 13–19 (8–12) | Freemium, Plus ~$70/yr |
| 10 | Toca Boca World | Spin Master | 100M+; #1 grossing kids game 2025 | Open-ended pretend play | 4–7 (8–12) | Free + IAP packs |
| 11 | Brainly | Brainly | 100M+ | Homework Q&A + AI | 13–19 (8–12) | Freemium, ads |
| 12 | Kahoot! | Kahoot! | 100M+ | Quiz games | 8–12 (13–19, teachers) | Freemium, B2B |
| 13 | Cake | Cake Corp | 100M+ | English/Korean via clips | 20–34 (13–19) | Freemium, ads |
| 14 | Lingokids | Monkimun | 50M+ Play; 2.5–3.5M US iOS/yr | Early learning, ESL | 4–7 (1–3) | Subscription ~$80–100/yr |
| 15 | ClassDojo | ClassDojo | 50M+ | Class community (parents) | 4–12 (parents 35–59) | Free; Plus for parents |
| 16 | Headway | Headway | 50M+ lifetime; #1 US Education Jan 2025 | Book summaries | 20–34 (35–59) | Subscription $89.99/yr |
| 17 | ABCmouse | Age of Learning | 2–3M US iOS/yr | Pre-K–2 curriculum | 4–7 (1–3) | Subscription |
| 18 | PBS KIDS Games | PBS KIDS | 10M+ Play; 2–3M US iOS | Character-based early learning | 4–7 (1–3) | Free, no ads |
| 19 | Khan Academy Kids | Khan Academy | 10M+ | Early literacy, math, SEL | 4–7 (1–3) | 100% free |
| 20 | Khan Academy (+ Khanmigo) | Khan Academy | 10M+ | K-12 math, science, test prep | 13–19 (8–12) | Free; Khanmigo $4/mo |
| 21 | Babbel | Babbel | 50M+ | Languages (structured) | 35–59 (20–34, 60+) | Subscription, lifetime |
| 22 | Memrise | Memrise | 50M+ | Languages | 20–34 (35–59) | Freemium |
| 23 | Prodigy Math | Prodigy | 1.5–2.5M US iOS | Math RPG | 8–12 (4–7) | Freemium membership |
| 24 | Question.AI | Zuoyebang-linked | 10M+ | AI homework solver | 13–19 | Freemium |
| 25 | Praktika | Praktika.ai | 10M+; ~$20M ARR | AI avatar language tutor | 20–34 (35–59) | Subscription |
| 26 | Speak | Speak ($1B valuation) | 10M+ | AI speaking tutor | 20–34 (35–59) | ~$20/mo |
| 27 | Elevate | Elevate Labs | 10M+ | Brain training (verbal, math) | 35–59 (20–34, 60+) | Subscription, lifetime |
| 28 | Speechify | Speechify | 55M users claimed; 2025 ADA Inclusivity | Text-to-speech, reading access | 20–34 (13–19; ND) | Premium ~$139/yr |
| 29 | Read Along by Google | Google | 10M+ | AI read-aloud early literacy | 4–7 (8–12) | Free, offline |
| 30 | Coursera / Udemy (merged May 2026) | Coursera | 10M+ each | Professional courses | 20–34 (35–59) | Subscription, per course, B2B |

**Near misses (10M+ or high US iOS volume):**
- Epic!, Kiddopia, Simply Piano, Brilliant, Sololearn, Mimo
- ELSA, Loora, Stimuler, Busuu, Mathway, PW (Physics Wallah)
- Sago Mini World, HOMER, Duolingo ABC, Lumosity

**Store differences.**
- Android has the volume. The India-centric apps Seekho, Guru and PW barely register on the US App Store.
- iOS has the spending. US iOS users pay $45–$170/yr, and premium kids subscriptions and hard-paywall AI tutors do well there.
- Apple's Kids-category rules (no third-party ads or tracking, parental gates) and the 2025 age-range API leave two workable kids' models on iOS: **subscription** or **mission-funded free**.

### 4.2 Forum-favored apps (community top ~30)
These are the apps communities recommend, which often differ from what charts show:

| Segment | Forum favorites | Why recommended | Why criticized |
|---|---|---|---|
| 1–3 | Pok Pok, Sago Mini / Toca (Piknik), PBS KIDS, Khan Kids | Calm, open-ended, "no dopamine hits", free/no-ads | Subscription price; "not truly non-addictive" |
| 4–7 | Khan Academy Kids, Teach Your Monster to Read, HOMER / Hooked on Phonics, Reading Eggs, Starfall, Duolingo ABC, Epic!, ScratchJr | Learning to read; free and safe | Paywalls after the child is hooked; ABCmouse's cancellation trap ($10M FTC settlement); scary content |
| 8–12 | Prodigy, IXL, Beast Academy, Khan Academy, Minecraft Education, Kahoot!/Blooket/Gimkit, Scratch/Code.org | Game worlds; adaptive practice; rigorous advanced math | Prodigy "pay-to-win" (FTC complaint); IXL SmartScore "rage-inducing"; nothing for kids who struggle |
| 13–19 | Khan + Bluebook, Quizlet → **Knowt** migration, Photomath/Gauth/Brainly, Forest/Opal, ChatGPT Study Mode, Gemini Guided Learning, Claude learning mode, Khanmigo | Free test prep, a patient AI "office hours", focus tools | AI cheating; Quizlet "cashgrab"; Khanmigo errors; "it sends everything to my teacher" |
| 20–34 / 35–59 | Duolingo, Anki, Pimsleur, Babbel/Busuu, italki/LingQ, Odin Project / freeCodeCamp / CS50, Brilliant, Coursera/Udemy/LinkedIn Learning | Habit forming; serious learner tools; free coding curricula | **Duolingo backlash**: the AI-first memo ("AI slop"), the Energy system ("punished for using the app?", ~3k upvotes), streak burnout; auto-renew surprises |
| 60+ | BrainHQ, Lumosity, Elevate, GetSetUp | Cognitive health; peer-taught live tech classes | Gains don't transfer outside the app; confusing subscriptions; seniors barely heard in forums |
| ND | Proloquo2Go / TouchChat / LAMP (AAC), Speech Blubs, Otsimo, Goblin Tools, Tiimo, Finch, Nessy, Learning Ally, Speechify | Visual schedules, AAC, task breakdown, "no streak anxiety" | $250–300 AAC; billing traps; setup burden; novelty wears off in weeks |

### 4.3 The frontier-lab factor
Between April and August 2025 every major AI lab shipped a Socratic learning mode, free or nearly free to students:
- Claude for Education and learning mode (Apr 2025; all users Aug 2025)
- ChatGPT Study Mode (29 Jul 2025)
- Gemini Guided Learning (Aug 2025; free AI Pro for US college students)
- Microsoft Copilot Study agent

ChatGPT for Teachers is free to verified US K-12 educators until June 2028. **Generic AI tutoring is commoditized for 13+/18+.** Children under 13 remain structurally under-served because of COPPA and safety risk, and seniors and neurodivergent learners are not the focus of design.

### 4.4 Categorization by age segment
The full list of 83 apps is in [`research/app-catalog.csv`](../research/app-catalog.csv).

| Segment | Leaders (downloads) | Forum / design benchmarks | Coverage verdict |
|---|---|---|---|
| **1–3** | Sago Mini World, Lingokids (down-age), Khan Kids (down-age), PBS KIDS | Pok Pok (2021 ADA), Endless Alphabet, Sago Mini Jinja's Garden (2026 ADA Inclusivity finalist) | **Under-served.** Almost nothing is built for the age. Toddler content is mostly YouTube. No product centres on parent co-play or talk. |
| **4–7** | Toca Boca World, Lingokids, ABCmouse, PBS KIDS, Khan Kids, Read Along, Kiddopia | Teach Your Monster, HOMER, Endless Reader, Tinybop | **Well served but split** between high-stimulation subscriptions and free non-profits. Little science-of-reading AI. Few dyslexia-aware or low-sensory options. |
| **8–12** | Minecraft Education, Kahoot!, Prodigy, Epic!, Google Classroom | Beast Academy, Scratch, IXL (resented) | **Under-served.** Too old for preschool apps, too young for Gauth and ChatGPT (ToS 13+). No COPPA-safe Socratic tutor leads. Pay-to-win pressure. |
| **13–19** | Gauth, Quizlet, Photomath, Brainly, Question.AI, Google Classroom, Khan Academy | Knowt, Forest, AI study modes | **Over-served with answers, under-served with learning.** Integrity, proof-of-learning and focus are open. |
| **20–34** | Duolingo, Seekho, Learna, Cake, Headway, Speak, Praktika, Memrise, Coursera/Udemy | Anki, Odin/freeCodeCamp, Tiimo | **Crowded** in languages and summaries. Hands-on, role-specific AI fluency is open. So is a "no streak guilt" experience. |
| **35–59** | Babbel, Elevate, Impulse, Simply Piano, Coursera | LinkedIn Learning, Brilliant, Pimsleur | **Moderate.** Mid-career AI reskilling and "parent as learning coach" are open. |
| **60+** | (No app targets them.) Babbel, Elevate, Impulse draw many older users | GetSetUp, BrainHQ | **Clearly under-served.** Timed games and small type dominate. AI confidence and scam safety are unmet needs. |
| **ND overlay** | Speechify (accessibility), Tiimo (2025 iPhone App of the Year) | AAC trio, Otsimo, Choiceworks, Goally, Joon, Nessy, Mightier, EndeavorRx | **Fragmented, thin evidence.** Billing traps, setup burden, over-stimulation, and the ABA vs. affirming tension. |

---

## 5. Voice of the customer: needs, wants and pain points

### 5.1 Top 15 unmet needs, ranked by frequency × intensity
| Rank | Unmet need | Segments | Representative evidence |
|---|---|---|---|
| 1 | **Honest, trap-free pricing**: no cancellation traps, silent renewals or paywalls mid-play | All | ABCmouse FTC $10M; Gauth 27-month billing loop; Brilliant "no heads-up before the charge"; Trustpilot 1.4–3.8 vs App Store 4.3–4.9 |
| 2 | **Learning that AI answer-getting does not undermine** | Teens, college, teachers | Teachers "abandoning homework"; UCI ALEKS study: odds of correct answers −25% after ChatGPT; Bastani: −17% on unassisted exams |
| 3 | **Motivation without manipulation or punishment** | Adults, teens, ND | Duolingo Energy: "So now we're punished for using the app?"; streak "dread" |
| 4 | **No ads, upsells or pay-to-win in kids' play** | 1–12 | Prodigy: "up to four times as many advertisements than math questions" (CCFC/FTC complaint) |
| 5 | **Trust in human-crafted or human-reviewed content** | Adults, parents | Duolingo "AI slop" backlash |
| 6 | **Calm, non-addictive screen time with natural stopping points** | 1–7, ND | Pok Pok's "no levels, winning or losing"; parents' meltdown-at-takeaway stories |
| 7 | **Proof of real learning parents can see** | Parents 4–12 | Badges and SmartScores distrusted |
| 8 | **Focus and phone-distraction management** | Teens, adults, ADHD | Forest 1M+ ratings; Opal, one sec |
| 9 | **Free core tools with data portability** | Teens | Quizlet "removed the option to export"; migration to Knowt |
| 10 | **An AI tutor that is accurate, patient and not surveillance** | Teens, parents | Khanmigo "272 − 172 = 430"; "sends it to your teacher… scary" |
| 11 | **Affordable, guided AAC and speech support** | ND parents | $249.99–$299.99 apps; SLP trials required |
| 12 | **Predictable, shame-free executive-function tools** | ND teens and adults | Finch "doesn't punish you for missing a day"; Tiimo "first planner that stuck" |
| 13 | **A path past beginner level to real speaking** | Adult language learners | Babbel "tops out at B2" |
| 14 | **Support for struggling (not only gifted) learners** | 8–12, dyslexia | Beast Academy "does not fit kids who have a hard time with math" |
| 15 | **Senior-friendly learning that builds tech confidence and cognitive health** | 60+, adult children | GetSetUp peer guides; brain-training transfer doubts |

### 5.2 Segment voices (condensed)
- **Toddler parents (1–3).**
  - Screen-time guilt shapes every decision, and the industry knows it. Lingokids ran a "parent guilt on trial" campaign.
  - The AAP's January 2026 statement dropped fixed time limits in favour of design quality and co-engagement. That gives "built for co-play" and "stops itself" new credibility.
- **Parents of 4–7s.** The job is *learning to read*. They want a science-of-reading scope and sequence, progress they can check in 30 seconds, and one plan for siblings.
- **Tweens (8–12).**
  - Kids want game worlds; parents want learning without pay-to-win.
  - About 70% of 5–13-year-olds want to learn creative subjects inside Roblox/Minecraft-style worlds [V2].
  - Parents of struggling learners feel ignored.
- **Teens (13–19).**
  - AI cheating dominates the conversation.
  - Free test-prep stack: Khan + Bluebook.
  - Phones are framed as the enemy of study.
  - Study is social (Discord, "study with me"), but the apps are single-player.
  - Teens fear AI-tutor surveillance.
- **Adults (20–59).**
  - Adults forgive gamification. They do not forgive manipulation or human craft being removed.
  - "Real learners" graduate to Anki, italki and Pimsleur.
  - They are sceptical of certificates and anxious about AI eroding entry-level jobs.
- **Seniors (60+).**
  - They are heard mostly through adult children ("how do I get Mom to use the iPad / avoid scams / stay sharp").
  - What works: peer instructors, live classes, no-download access, large type.
- **Neurodivergent learners and parents.** They ask for:
  - no overstimulation
  - predictability and visual schedules
  - affordable AAC with guided selection
  - shame-free executive-function tools
  - structured literacy for dyslexia
  - low caregiver admin

---

## 6. Accessibility and sensory audit of the market

The research found that **no top-30 app combines strong screen-reader support, dyslexia-friendly type and a real low-sensory mode.**

| Barrier | Where observed | Who is excluded |
|---|---|---|
| Timers and speed scoring | Kahoot!, Impulse, Quizlet Match, Elevate | Slower readers, dyslexic learners, motor-impaired users, seniors, screen-reader users |
| Drag-and-drop only | Duolingo tiles, many kids' apps | Toddlers (3-year-olds succeed only ~73% of the time on basic touch tasks), motor-impaired users, switch users |
| Camera-first input | Gauth, Photomath, Question.AI | Blind and low-vision students |
| Voice-only scoring | ELSA, Praktika, Learna, Read Along | Speech-impaired users, AAC users, children with atypical speech |
| High-stimulation rewards | Duolingo, ABCmouse, Kiddopia, Lingokids, Prodigy, Toca | Autistic users, sensory-sensitive users, ADHD users, many toddlers |
| No Dynamic Type / larger text | Most kids and game-like apps; Khan Kids library text reportedly fixed | Low-vision users, seniors |
| Unreadable math output | Most solvers | Screen-reader users |
| VoiceOver "an afterthought" | Duolingo (AppleVis reports) | Blind learners |

**Positive benchmarks:**
- Khan Academy ("fully accessible with VO" per AppleVis)
- Khan Kids (narration, calm, no timers)
- Pok Pok (calm tech)
- Speechify (2025 ADA Inclusivity)
- Guitar Wiz (2026 ADA Inclusivity)
- Tiimo (2025 App of the Year)
- Sago Mini Jinja's Garden (2026 ADA Inclusivity finalist)
- PBS KIDS (spoken instructions, large controls)

**Market signal.** Apple's **Accessibility Nutrition Labels** (2025) make accessibility visible and searchable on product pages. Early, honest adopters in education will gain discovery and trust.

**Evidence base for design.** Part B of raw file 04 covers:
- WCAG 2.2, including 24 px targets, dragging alternatives and accessible authentication
- W3C COGA's 8 objectives
- UDL 3.0, with its focus on learner agency, joy and play
- the BDA 2023 Dyslexia Style Guide
- Vatavu 2015 on toddler touch
- NN/g children's guidelines
- the AAP 2026 policy statement
- the 2025 Montessori national RCT (positive results)
- the Orton-Gillingham meta-analysis (multisensory component not significant)

These are distilled into the studio's **[Inclusive & Sensory UX Framework](02-inclusive-sensory-ux-framework.md)**.

---

## 7. The neurodivergent and special-needs landscape

- **Demand.** Autism 1 in 31; ADHD 11.4% with ~1 in 3 untreated; dyslexia 5–20%; ~7.5M US students served under IDEA [M]; England ~638.7k EHC plans (+~11%/yr) [M].
- **Market structure.** Fragmented, with no winner outside AAC. The categories are:
  - AAC (Proloquo2Go, TouchChat, LAMP WFL, TD Snap, CoughDrop, Avaz)
  - visual schedules and executive function (Choiceworks, First Then, Goally, Tiimo, Brili, Joon, Goblin Tools)
  - speech (Speech Blubs, Articulation Station)
  - dyslexia (Nessy, Ghotit)
  - regulated digital therapeutics (EndeavorRx, Mightier, Cognoa Canvas Dx)
  - tangibles and robots (Cosmo, Leka, QTrobot)
- **Evidence.** Only EndeavorRx, Mightier and Cognoa have strong product-level evidence. Even FDA clearance did not create a business: Akili sold for ~$34M, and Pear went bankrupt. Brain Balance (~$12k, contested) and FTC actions (Lumosity $2M, LearningRx) are cautionary tales about efficacy claims.
- **Repeated complaints:**
  - billing dark patterns (Speech Blubs, Joon)
  - setup burden and sync bugs (Goally)
  - novelty that wears off in weeks (Joon)
  - $250–$300 AAC prices, with tablet apps rarely covered by Medicaid
  - infantilizing visuals for older learners
  - over-stimulation even in "autism apps"
- **Positioning.** Autistic self-advocates strongly criticize compliance-oriented ABA (#ABAisAbuse). The studio should be **neurodiversity-affirming**:
  - goals the learner and family choose (communication, self-advocacy, regulation, independence)
  - never target stimming or eye contact
  - paid neurodivergent co-designers
  - IEP/EHCP-compatible data
  - no cure or treatment claims
- **Channels:**
  - ESA disability awards (for example, FL FES-UA)
  - IDEA-funded district special education, relatively protected from the ESSER cliff
  - UK EHCP and DSA
  - clinician partners as between-session tools

---

## 8. Regulatory, ethical and funding conditions

| Area | Status (Sept 2026) | Design consequence |
|---|---|---|
| **COPPA (amended)** | Full compliance required since 22 Apr 2026. Personal information now includes biometric identifiers. AI training and ads need **separate** parental consent | No child-data model training by default. On-device voice where feasible. Retention schedule |
| **KOSA / KIDS Act** | Passed the House in June 2026; cleared Senate Commerce in August 2026. **Not law** | Design as if duty of care and compulsive-use limits already apply |
| **US state Age-Appropriate Design Codes** | California (partly enjoined), Maryland, Nebraska (in force 2026), Vermont (2027); app-store age-verification laws | High-privacy defaults; no nudges; DPIAs |
| **UK Children's Code** | 15 standards, in force; strengthened by the Data (Use and Access) Act 2025 | Profiling and geolocation off; no nudge techniques |
| **EU AI Act** | Emotion recognition in education **banned** since Feb 2025. Education high-risk obligations moved to **2 Dec 2027**. Art. 50 transparency in force Aug 2026 | No affect inference from face or voice. Human oversight of AI that assesses or places learners |
| **FTC 6(b) on AI companions** | Inquiry since Sept 2025; CA SB 243 | **Tutor, not friend.** No companion personas for minors |
| **FTC §5 / FDA** | Efficacy claims need competent evidence. Diagnosis or treatment claims make a product a device | Claim only the evidence tier achieved. Education, not treatment |
| **Accessibility law** | WCAG 2.2 AA baseline; ADA Title II web rule from Apr 2026 for large public entities [M] | WCAG 2.2 AA plus a filled-in Accessibility Nutrition Label at launch |

**Funding climate:**
- Capital favours **AI-native, career- and outcome-aligned, capital-efficient** companies with **learning-outcome evidence**.
- K-12 district sales are harder after ESSER, and investors are wary of consumer kids' apps.
- ESA, homeschool and microschool channels are growing (TX $1B ESA from 2026–27; ~75k microschools; ~3M homeschooled), which helps tweens and neurodivergent products.
- Pitching as "learning & work / human capability" widens the investor pool.

---

## 9. Where the opportunity is (synthesis)

1. **Calm, co-play-first early years (1–7).** No calm, speech- and science-of-reading-led companion exists that parents trust and that ends sessions by itself. Frontier labs don't serve under-13s.
2. **A COPPA-safe Socratic tutor plus mastery worlds for 8–12,** without pay-to-win, sold through the ESA and homeschool channel.
3. **"Learning, not cheating" for teens.** Proof-of-learning, exam depth, social co-study and career paths that free generic study modes don't provide.
4. **Hands-on, role-specific AI fluency for adults,** plus a clearly under-served **60+** market for AI confidence, scam safety and lifelong curiosity.
5. **A neurodiversity-affirming, sensory-friendly suite** covering visual schedules, affordable AAC, regulation, structured literacy, ADHD executive function and affirming social communication. It would come with low-admin caregiver and IEP tooling.
6. **The cross-cutting moat: inclusive and sensory design plus honesty.** That means:
   - a calm mode on the first screen
   - multimodal input
   - WCAG 2.2 AA
   - fair billing with in-app cancellation
   - no streak punishment
   - human-reviewed AI content
   - published outcomes

   Competitors' reviews show that users punish the lack of these, and regulators increasingly require them.

---

## 10. Studio proposal: five ventures, 35 apps

> **v1.1 update:** the [Project Reevaluation](03-project-reevaluation.md) keeps all 35 as experiences but builds them on 12 shared engines and ships them in 10 surfaces instead of 35 store apps. See also [Studio Platform Features](04-studio-platform-features.md).

Working names are subject to trademark screening in discovery.

| Venture | Segment | One-line thesis | Seven apps | Vision doc |
|---|---|---|---|---|
| **Lanternling** | 1–3 and 4–7 | Calm, voice-first, co-play-first early learning that parents trust | Babble Buddy · Tap & Wonder · Story Lantern · Sound Garden · Number Nest · Calm Cubs · Two Words | [vision/01-lanternling-early-years.md](vision/01-lanternling-early-years.md) |
| **Questwise** | 8–12 | A COPPA-safe Socratic tutor and mastery worlds; curiosity without pay-to-win | Sage Tutor · Math Realms · Read Rangers · Builder's Lab · AI Detectives · Wonder Lab · Mission Control | [vision/02-questwise-tweens.md](vision/02-questwise-tweens.md) |
| **Ascendly** | 13–19 | AI-native learning, not cheating; proof-of-learning and future pathways | Study Coach · Exam Ready · Explain It Back · Draft Mentor · Study Squad · Pathfinder · Life Ready | [vision/03-ascendly-teens.md](vision/03-ascendly-teens.md) |
| **Evergrow** | 20–34, 35–59, 60+ | Hands-on AI fluency and lifelong learning for every adult stage | AI Fluency Lab · Career Sprint · Speak Freely · Lead with AI · Parent Coach · Silver Circuit · Curiosity Circle | [vision/04-evergrow-adults.md](vision/04-evergrow-adults.md) |
| **Wavelength** | Neurodivergent children (≈2–17) | A neurodiversity-affirming, sensory-friendly suite for communication, regulation, learning and independence | Wavelength Day · Wavelength Voice · Calm Harbor · ReadWave · Focus Crew · Social Compass · Spark Switch | [vision/05-wavelength-neurodivergent.md](vision/05-wavelength-neurodivergent.md) |

**Shared studio platform, to be designed in discovery:**
1. **Lumen inclusive design system**: calm-by-default tokens, a Sensory Dial, motor profiles by age, typography
2. **"My Needs" profile**: portable, learner-owned, caregiver-configurable
3. **Guardrailed AI orchestration**: Socratic tutor policies, human-reviewed content, no companion personas, on-device voice where feasible
4. **Privacy and child-safety stack**: COPPA 2025, AADC, FERPA, EU AI Act
5. **Evidence engine**: logic models, pre-registered pilots, ESSA-tier roadmap
6. **Fair-billing charter**: trial reminders, in-app cancellation, family plans, ESA and school licensing

**Suggested sequencing (from S5, to be confirmed at the discovery gate):**
1. Evergrow AI Fluency Lab first, for the fastest revenue and fundability. It also builds the shared tutoring and assessment core.
2. Then Wavelength or Questwise, which share the ESA channel and the child-safe stack.
3. Then Lanternling and Ascendly on the proven child-safe voice and tutoring infrastructure.

Discovery is run **for all five in parallel** so the sequencing decision rests on evidence.

---

## 11. Open questions for discovery
1. Will parents pay for "calm" and co-play, and will kids come back to it? (Lanternling)
2. Can a Socratic tutor for under-13s stay engaging when it never gives the answer? (Questwise, Ascendly)
3. Will teachers adopt proof-of-learning, and will teens accept it without feeling watched? (Ascendly)
4. Which mid-market employers buy role-specific AI fluency, and at what price per seat? (Evergrow)
5. Who pays for 60+: the senior, adult children, Medicare Advantage plans or libraries? (Evergrow)
6. Can affordable AAC with AI phrase support preserve user authorship and win SLP trust? (Wavelength)
7. Does a calm mode on the first screen measurably change comfort, persistence and learning for sensory-sensitive users? (all)

The [Discovery & Validation Plan](discovery/discovery-validation-plan.md) turns these into testable hypotheses, methods, sample sizes and decision gates.

---

## References
The full source lists with URLs are in the raw files. Key sources:
- Business of Apps / Appfigures, Education App Market 2025–26; Sensor Tower State of Mobile 2026 and education blogs
- Duolingo Q2 2026 shareholder letter / 10-Q (SEC)
- CDC MMWR SS 74(2), autism prevalence 1 in 31 (2025); CDC ADHD data
- Kestin et al., *Scientific Reports* 2025 (Harvard AI tutor RCT); World Bank Nigeria AI tutor RCT; Wang et al. 2024 (Tutor CoPilot); Bastani et al., *PNAS* 2025
- W3C WCAG 2.2; W3C COGA "Making Content Usable"; CAST UDL Guidelines 3.0 (2024); BDA Dyslexia Style Guide 2023; Vatavu et al., *IJHCS* 2015; NN/g UX for Children
- AAP "Digital Ecosystems, Children, and Adolescents", *Pediatrics* 157(2), Jan 2026
- Lillard et al., *PNAS* 2025 (Montessori RCT); Stevens et al. 2021 (Orton-Gillingham meta-analysis)
- FTC: COPPA Rule amendments (Federal Register, 22 Apr 2025); ABCmouse, Edmodo, Epic Games, Lumosity, LearningRx actions; AI companion 6(b) (Sept 2025)
- EU AI Act and Digital Omnibus (Reg. (EU) 2026/1744); UK ICO Age Appropriate Design Code
- HolonIQ funding notes 2025–H1 2026; Brighteye European Learning & Work reports; WEF Future of Jobs 2025
- Apple Design Awards 2021/2025/2026; App Store Awards 2025; Apple Accessibility Nutrition Labels

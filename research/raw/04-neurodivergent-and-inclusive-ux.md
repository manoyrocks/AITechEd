# 04 — Neurodivergent & Special-Needs EdTech Landscape + Inclusive & Sensory UX Framework

**Prepared:** 2026-09-29 · **Author role:** Research lead, inclusive design & special-needs EdTech
**Scope:** (A) App/market landscape for children with special needs; (B) evidence-based inclusive, accessible and sensory UX principles across all ages (toddler → 60+), including child-safety/privacy regulation.

---

## 0. How to read this document (verification legend)

| Tag | Meaning |
|---|---|
| **[V]** | Verified via web search during this session (2026-09-29); source link given. Most facts were confirmed from search snippets or secondary sources, not by reading the full primary document. |
| **[V-2nd]** | Verified only via a secondary or vendor/affiliate blog (for example, a competitor's comparison post). Treat as directional and re-check before quoting. |
| **[M]** | **From memory / model knowledge (cutoff ~mid-2026). NOT re-verified in this session.** Confirm before external use. |

> **Research limitations:** The session's web-search quota ran out partway through, and direct page fetches were blocked by the network proxy for several domains (wikipedia.org, nngroup.com, ftc.gov). As a result, some items are marked [M]: EndeavorRx trial statistics, NN/g senior-usability numbers, the FTC AI-chatbot 6(b) inquiry, California SB 243, IDEA enrollment counts, platform target sizes, and EU AI Act Annex III/Art. 5 details. App Store prices change often and differ by region. Treat all prices as snapshots.

---

## Executive summary (key takeaways for a startup studio)

1. **Demand is large and growing because of diagnosis trends.** CDC's 2025 ADDM report puts autism at **1 in 31** 8-year-olds (2022 data), up from 1 in 36 **[V]**. ADHD: **11.4% of US children aged 3–17 (7.1M)** have ever been diagnosed, and about 1 in 3 received no ADHD-specific treatment in 2022 **[V]**. Dyslexia estimates range from **5–20%**, depending on the definition **[V]**.
2. **The market is fragmented and has no clear winner outside AAC.** The strongest categories are (a) AAC (Proloquo2Go, TouchChat, LAMP WFL, TD Snap), which is professional-led, costs $150–$300 one-time, and gets school/IEP or device funding; (b) visual schedules and routines (Choiceworks, First Then, Goally, Tiimo, Brili, Joon); (c) speech/articulation (Speech Blubs, Articulation Station); (d) dyslexia (Nessy, Ghotit); and (e) regulated digital therapeutics (EndeavorRx, Mightier, Cognoa Canvas Dx).
3. **Evidence is thin across most of the category.** Only a handful of products have RCTs or FDA authorization (EndeavorRx, Mightier's sham-controlled RCTs, Cognoa Canvas Dx). Most "evidence-based" claims mean "built on ABA/OG principles," not "product was tested." FTC enforcement history (Lumosity $2M, LearningRx) shows that efficacy claims without proof are a real legal risk **[V]**.
4. **The same parent complaints come up again and again.** They are billing and cancellation dark patterns (Speech Blubs, Joon) **[V]**, setup complexity and sync bugs (Goally) **[V]**, novelty wearing off quickly (Joon) **[V]**, and high one-time AAC prices.
5. **Positioning risk: ABA vs. neurodiversity-affirming.** Autistic self-advocates strongly criticize compliance-oriented ABA (#ABAisAbuse), and ABA training programs are now adding neurodiversity-affirming content **[V]**. Products that frame themselves as "ABA-based" (for example, Otsimo) sell well to some parents and BCBAs but alienate autistic adults and many SLPs/OTs. A studio should position as **neurodiversity-affirming and goal-directed by the learner and family**, while staying compatible with IEP goals.
6. **Regulation tightened in 2025–26.**
   - The amended **COPPA Rule** has been fully in force since **22 Apr 2026** **[V]**.
   - The **EU AI Act** high-risk (Annex III, incl. education) deadline moved to **2 Dec 2027** by the Digital Omnibus (Reg. (EU) 2026/1744) **[V]**.
   - The US House passed the **KIDS Act (incl. KOSA)** on **29 Jun 2026**. The Senate Commerce Committee advanced S.1748 on 5 Aug 2026, and no floor vote was reported at time of writing **[V]**.
   - Nebraska's and Vermont's AADCs join California's and Maryland's **[V]**.
   - The UK Data (Use and Access) Act 2025 strengthens the Children's Code under UK GDPR **[V-2nd]**.
7. **UX standards also moved.**
   - WCAG 2.2 (Oct 2023) is the enforceable baseline. It adds **Target Size 24×24 CSS px (AA)**, **Dragging Movements**, and **Accessible Authentication** **[V]**.
   - The **WCAG 3.0** Working Draft was updated **10 Sep 2026**. A Candidate Recommendation is expected around Q4 2027, and it is not normative yet **[V]**.
   - **UDL 3.0** (July 2024) shifts from "expert learners" to **learner agency**, identity, joy and play **[V]**.
   - The **AAP's Jan 2026** "Digital Ecosystems" policy statement **dropped fixed screen-time limits** in favor of design, caregiver-relationship and system factors **[V]**.
   - **Apple Accessibility Nutrition Labels** on the App Store (2025) make accessibility a visible, searchable selling point **[V]**.

---

# PART A — LANDSCAPE

## A1. Prevalence & population context

| Condition / population | Figure | Source / status |
|---|---|---|
| Autism (8-year-olds, US) | **1 in 31 (≈3.2%)** in 2022 surveillance year; published 15 Apr 2025; up from 1 in 36 (2020). Range across 16 sites: 1 in 103 (Laredo, TX) to 1 in 19 (California). Boys:girls 3.4:1. 4-year-olds: 1 in 34. API, Black, Hispanic and multiracial children had higher identified prevalence than White children. | [V] [CDC MMWR SS 74(2)](https://www.cdc.gov/mmwr/volumes/74/ss/ss7402a1.htm); [Autism Speaks](https://www.autismspeaks.org/news/autism-prevalence-rises-1-31-children-us); [autismcenter.org](https://autismcenter.org/autismprevalence/) |
| Autism — political framing | HHS press release titled "'Autism Epidemic Runs Rampant'". Note that federal messaging has become politicized, while advocacy groups attribute much of the rise to better identification. | [V] [HHS](https://www.hhs.gov/press-room/autism-epidemic-runs-rampant-new-data-shows-grants.html); [Autism Society](https://autismsociety.org/autism-society-of-america-responds-to-new-cdc-report-on-updated-autism-prevalence-rates/) |
| ADHD (US, 3–17) | **11.4% (7.1M)** ever diagnosed (2022 NSCH), up from 9.9% in 2016. ~78% have ≥1 co-occurring condition (behavior/conduct 44.1%, anxiety 39.1%). ~1 in 3 received no ADHD-specific treatment. | [V] [CDC ADHD data](https://www.cdc.gov/adhd/data/index.html); [Danielson et al. 2024, JCCAP](https://www.tandfonline.com/doi/full/10.1080/15374416.2024.2335625); [APSARD](https://apsard.org/cdc-releases-new-adhd-prevalence-paper/) |
| Dyslexia | Estimates range from **5–10%** (strict diagnostic definitions) to **15–20%** (IDA: "some symptoms of dyslexia"; Yale Center: ~1 in 5). Most common specific learning disability. | [V-2nd] [Dyslexia Action](https://dyslexiaaction.org.uk/2023/10/the-prevalence-of-dyslexia/); [Yale EliScholar](https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article=1058&context=yurj). The IDA and Yale primary pages were not fetched. |
| Students served under IDEA (US, 3–21) | ~**7.5M students, ~15% of public-school enrollment** (2022–23). Specific learning disability is the largest category, followed by speech/language impairment and autism. | **[M]** NCES Condition of Education. Not re-verified. |
| Dyspraxia / DCD | ~5–6% of school-age children | **[M]** DSM-5 estimate. Not re-verified. |
| Speech/language | Developmental language disorder ~7% of kindergarteners | **[M]** Tomblin et al. 1997; Norbury et al. 2016. Not re-verified. |

## A2. Market size (treat with caution: estimates vary widely)

| Segment | Estimate | Source |
|---|---|---|
| Assistive technology (global) | $28.35B (2024) → $31.16B (2025), 9.9% CAGR (TBRC/R&M). Another firm: $36.65B (2025) → $96.99B (2035). | [V] [Research & Markets](https://www.researchandmarkets.com/reports/6174414/assistive-technology-market-report); [MRFR](https://www.marketresearchfuture.com/reports/assistive-technology-market-29777) |
| Special-education software (global) | **$23.0B (2025) → $51.0B (2032)**, 12.1% CAGR | [V] [Research & Markets](https://www.researchandmarkets.com/report/special-education-software) |
| AT market growth | +$6.3B, 2025–2029 (Technavio) | [V] [PR Newswire](https://www.prnewswire.com/news-releases/assistive-technology-at-market-to-grow-by-usd-6-3-billion-from-2025-2029--driven-by-rising-orthopedic--neurological-disorders-with-ai-impact---technavio-302371177.html) |

**Analyst note:** Syndicated "special education software" numbers probably include SIS/IEP-management platforms (e.g., Frontline, PowerSchool SpEd), not just learner-facing apps. The consumer-facing special-needs app segment is likely much smaller, in the low single-digit billions **[M — inference, not sourced]**. For fundraising, build a bottom-up TAM: diagnosed children × payer mix × realistic ARPU.

## A3. Stakeholder ecosystem

| Stakeholder | Role / buying power | What they need from a product |
|---|---|---|
| **Parents / caregivers** | Primary consumer purchaser (subscriptions, one-time apps). Often exhausted and on tight budgets. Heavy users of Facebook groups, Reddit and TikTok for recommendations. | Fast setup, visible progress, no billing traps, works offline, and the child actually likes it. |
| **SLPs** (speech-language pathologists) | Gatekeepers for AAC and articulation. Run AAC evaluations that justify device funding. | Robust vocabulary (core-word, motor planning), data export, customization, and no "baby-ish" design for older users. |
| **OTs** (occupational therapists) | Sensory processing, fine motor, handwriting, self-regulation | Graded sensory challenge, fine-motor tasks, and zones/regulation tools |
| **BCBAs** (behavior analysts) | Run ABA programs (insurance-funded). Collect data on target behaviors. | Data collection, reinforcement schedules, token economies. This is where the neurodiversity tension sits (see A6). |
| **Special-ed teachers / SENCOs (UK)** | Classroom implementation; IEP goal tracking | Multi-student dashboards, IEP-goal alignment, minimal prep, and district privacy compliance |
| **District procurement / IT** | Buys site licenses. Requires DPAs and student-privacy pledges (FERPA/COPPA/state laws). | SOC 2, a signed DPA, rostering (Clever/ClassLink), and accessibility conformance (VPAT/ACR) |
| **IEP / 504 process** | IEPs (IDEA) can specify **assistive technology** as a service. Districts must provide AT if the team determines it is needed. 504 plans provide accommodations. | Products whose outputs map to measurable IEP goals are easier to "write in." |
| **Insurance / Medicaid** | Dedicated **speech-generating devices (SGDs)** can be covered as DME by Medicaid/Medicare/private insurance. **Tablet AAC apps generally are not** [V-2nd]. Medicaid EPSDT covers medically necessary services for under-21s, incl. ABA **[M]**. FDA-cleared devices seek payer coverage (Cognoa Canvas Dx: Wyoming Medicaid first state, Highmark first commercial payer) [V]. | Clinical evidence, CPT/HCPCS pathway, and FDA status where claims are medical |
| **ESSER end** | Federal pandemic relief (ESSER III) funded a wave of district EdTech purchases. The obligation deadline has passed, and the ED **cancelled extensions** in 2025 and then allowed late liquidation for pre-approved states. The final liquidation deadline was around **28–30 Mar 2026** [V]. | Expect **budget cliffs** and license non-renewals in 2025–27. Districts are shifting to Title I, IDEA Part B and state funds. Tools need hard ROI evidence. |

Sources: [K-12 Dive on ESSER late liquidation](https://www.k12dive.com/news/schools-esser-ARP-late-liquidation-McMahon-letter/751908/); [K-12 Dive on cancelled extensions](https://www.k12dive.com/news/education-department-cancels-esser-spending-extensions/744020/); [CRS IF12978](https://www.congress.gov/crs-product/IF12978); [ED FAQ Sept 2025](https://www.ed.gov/media/document/esf-liquidation-extension-faqs-updated-september-30-2025-110426.pdf); [Cognoa Wyoming Medicaid](https://www.prnewswire.com/il/news-releases/wyoming-medicaid-becomes-first-state-to-cover-cognoas-canvas-dx-expanding-access-to-early-autism-diagnosis-302259679.html); [Fierce Healthcare on Highmark](https://www.fiercehealthcare.com/payers/cognoas-autism-diagnostic-tool-now-network-highmark-members).

## A4. App catalog (~26 products)

Legend for evidence tier:
- **E1** = FDA authorization and/or RCT on the product itself
- **E2** = peer-reviewed studies on the product (non-RCT/small)
- **E3** = built on an evidence-based method (AAC, OG, ABA, visual supports) but the product itself is untested
- **E4** = testimonials only, or contested

### A4.1 AAC (augmentative & alternative communication)

| App | Target / age | What it does | Evidence | Pricing (snapshot) | Strengths | Complaints / risks | Sources |
|---|---|---|---|---|---|---|---|
| **Proloquo2Go** (AssistiveWare) | Non-speaking / minimally speaking people of any age; autism, CP, Down syndrome, apraxia | Symbol-based AAC with Crescendo core vocabulary, grid sizes that grow with the user, natural voices incl. child voices, multilingual | E3. AAC as a practice is strongly evidence-based (AAC does not hinder speech; it may support it). Product-level trials are limited. | **$249.99** US App Store (Aug 2026). Optional "Gateway" vocab $149.99 IAP. | Polished, widely known, strong SLP community, iOS only | Price. iOS-only. Some SLPs prefer motor-planning (LAMP) approaches. Medicaid generally won't fund an app on a consumer iPad. | [V-2nd] [littlewords.ai](https://littlewords.ai/blog/proloquo2go-aac-device); [SLP guide](https://www.speechpathologygraduateprograms.org/blog/top-10-aac-augmentative-and-alternative-communication-devices/) |
| **TouchChat HD** (PRC-Saltillo) | Same | Page/symbol sets incl. WordPower. Available on dedicated Saltillo devices, which are fundable. | E3 | **$149.99**. WordPower bundle $299.99. | Runs on funded dedicated devices; broad vocab options | Navigation can be deep. Older UI. | [V-2nd] [littlewords.ai](https://littlewords.ai/blog/proloquo2go-versus-touchchat-which-is-better-for-toddlers) |
| **LAMP Words for Life** (PRC-Saltillo + Center for AAC & Autism) | Autism focus | Motor-planning AAC. Each word has a consistent, unique motor pattern (1–3 hits), based on the LAMP therapy approach. | E3–E2 (small LAMP studies) **[M]** | **$299.99** after a 30-day free trial | Automaticity; strong autism-SLP following | Expensive. Needs trained implementers. Less intuitive for new communication partners. | [V-2nd] [talaaac.com](https://talaaac.com/lamp-words-for-life-vs-proloquo2go) |
| **TD Snap** (Tobii Dynavox) | Wide | Core First vocab, eye-gaze compatible | E3 | ~$49.99 (iPad app) **[M]** | Cheapest of the major robust AAC apps; eye-gaze path | — | [V-2nd] [spectrumunlocked](https://www.spectrumunlocked.com/blog/best-aac-apps-and-devices); price is [M] |
| **CoughDrop** | Wide | Cloud-based, cross-platform AAC. Open Board Format (open-licensed content). Team/supporter accounts. | E3 | **$9/month or $295 lifetime per communicator**. 2-month trial. Free supporter accounts. | Cross-platform (web, Android, iOS). Open standards. Collaboration. | Smaller vendor; UI polish | [V] [CoughDrop help](https://coughdrop.zendesk.com/hc/en-us/articles/115002655512-What-pricing-options-and-funding-opportunities-are-available-to-purchase-CoughDrop); [intuitionlabs](https://intuitionlabs.ai/software/speech-language-pathology/aac-augmentativealternative-communication/coughdrop) |
| **Avaz AAC** (Avaz Inc., India) | Autism focus; multilingual incl. Indian languages | Picture + keyboard AAC | E3 | ~$129.99 one-time, **or $9.99/month, $99.99/year, $199.99–$299.99 lifetime** (varies by platform). 14-day trial. | Multilingual; subscription lowers the entry cost | — | [V] [App Store](https://apps.apple.com/us/app/avaz-aac/id909574843); [AAC Plus](https://blog.aac-plus.com/how-much-is-an-aac-app/) |
| **Cboard** | Wide | Free, open-source, browser-based AAC | E3 | Free (freemium) | Zero cost; web | Less robust vocab | [V-2nd] (same search) |

**AAC funding insight [V-2nd]:** Tablet AAC apps "typically do not qualify for Medicare or Medicaid coverage", while dedicated SGDs can, and schools can fund AAC through the IEP ([littlewords.ai](https://littlewords.ai/blog/best-aac-apps-toddlers)). This is why PRC-Saltillo and Tobii Dynavox sell "locked" dedicated devices.

### A4.2 Early learning / special education games

| App | Target / age | What it does | Evidence | Pricing | Strengths | Complaints / risks | Sources |
|---|---|---|---|---|---|---|---|
| **Otsimo Special Education** | Autism, Down syndrome, ADHD, learning disabilities; ~2–10 | 80+ games and 1,000+ materials: vocabulary, matching, social stories, fine-motor tracing. AAC and speech companion apps. | E3. Developer claims the activities follow an **ABA framework**. Product-level peer-reviewed RCT not found. | **$9.99/month, $119.99/year, or $229.99 lifetime**. 7-day trial. | Breadth; affordable lifetime option | "ABA" positioning is polarizing (A6). Subscription friction. | [V] [educationalappstore](https://www.educationalappstore.com/app/otsimo-special-education-aba); [Common Sense](https://www.commonsensemedia.org/app-reviews/otsimo-special-education-aac) |
| **Endless Reader** (Originator) | Early literacy, ~2–6. Popular with autistic kids for its predictable, animated letter-monsters. | Sight words, letter sounds, sentences | E3/E4 | Free download. Word packs $5.99 each. All 12 packs $29.99. | Delightful and predictable. Low text load. | Animation may over-stimulate some kids. IAP upsell. | [V] [App Store](https://apps.apple.com/us/app/endless-reader/id722910739); [Common Sense](https://www.commonsensemedia.org/app-reviews/endless-reader) |
| **Autism iHelp** series | Autism, expressive vocabulary; ~2–6 | Real-photo vocabulary with sounds. Deliberately only 24 photos in 3 groups to limit over-stimulation. Built by parents + an SLP. | E3/E4 | Low one-time (varies) **[M]** | Minimalism as a design choice; parental controls | Dated; limited content | [V] [App Store](https://apps.apple.com/us/app/autism-ihelp-play/id521485216) |
| **Miracle Modus** | Sensory overload / self-regulation, any age | Hypnotic rainbow visuals + soft bells. **Made by an autistic developer** "to mitigate sensory overload." Predictable motion patterns. | E4 (anecdotal) | Free / low **[M]** | Authentic lived-experience design; calm-down tool | Includes flashing/moving visuals, which is **risky for photosensitive users** (WCAG 2.3.1) | [V] [App Store](https://apps.apple.com/us/app/miracle-modus/id555904748) |

### A4.3 Visual schedules, routines & executive function

| App | Target / age | What it does | Evidence | Pricing | Strengths | Complaints / risks | Sources |
|---|---|---|---|---|---|---|---|
| **Choiceworks** (Bee Visual) | Autism, ADHD, anxiety; ~3–12 | Visual schedules, waiting board, feelings board; audio prompts | E3. **Visual supports and visual schedules are an established evidence-based practice for autism** (NCAEP/NPDC reviews) **[M]**. | **$39.99** one-time (US). Optional add-ons. | Simple, clinician-trusted, one-time price | iOS-centric; dated look | [V] [App Store](https://apps.apple.com/us/app/choiceworks/id486210964) |
| **First Then Visual Schedule** (Good Karma Applications) | Same | "First–then" boards and schedules with photos/audio | E3 | **$9.99** (iPhone); HD ~$14.99 | Cheap; simple | Minimal updates | [V] [App Store](https://apps.apple.com/us/app/first-then-visual-schedule/id355527801) |
| **Goally** | ADHD, autism; ~3–12 | Dedicated kid tablet (no YouTube or browser) + parent app: visual routines, video modeling, rewards, AAC, emotional-regulation games | E3 | Tablet ~**$199–$369** + subscription ~**$15–$20/month**. Also "Daily Skills System" $295. Figures vary by source. | Locked-down device solves the "tablet = YouTube" problem; all-in-one | **Setup takes hours. App crashes. Routines vanish between the parent and child devices.** Refund requests reported. | [V-2nd] [getgoally pricing](https://getgoally.com/pricing/); [justuseapp reviews](https://justuseapp.com/en/app/1262461227/goally/reviews); [BridgingApps](https://bridgingapps.org/bridgingapps-reviewed-app-goally-home-therapy-suite/) |
| **Tiimo** | ADHD, autism, neurodivergent teens and adults (13+ in practice) | Visual timeline planner, AI task breakdown, focus timers, Apple Watch. **2025 Apple iPhone App of the Year.** | E3 (co-designed with neurodivergent users) | iOS in-app: **$12/month or $54/year**; web $10/month or $42/year. Free tier. | Beautiful, calm, neurodiversity-affirming brand; mainstream validation | iOS/Apple ecosystem only; subscription | [V] [Daring Fireball](https://daringfireball.net/2025/12/2025_app_store_award_winners); [How-To Geek](https://www.howtogeek.com/productivity-app-is-a-iphone-app-of-the-year-heres-why-i-love-it/); [Tiimo](https://www.tiimoapp.com/) |
| **Brili Routines** | ADHD, autism; kids + separate adult app | Dynamic routine timers, visual/audio prompts, rewards | E3 | **$7.99/month, $34.99/6 months, $49.99/year** | Timer adapts to the actual time left | Small team; less content | [V] [Google Play](https://play.google.com/store/apps/details?id=co.brili.routines&hl=en_US&gl=US) |
| **Joon** | ADHD, ~6–12 | Chores/routines turned into a virtual-pet game ("Doters"); parent assigns quests | E3 (studies in progress per vendor **[M]**) | Free core. **Premium $12.99/month or $89.99/year**. 7-day trial. | Strong intrinsic motivation for ADHD; "dopamine hit" | **Charged after cancelling the trial.** "Overpriced." **Kids get bored within weeks.** Heavy parent admin. | [V] [ChoosingTherapy](https://www.choosingtherapy.com/joon-app-review/); [Common Sense](https://www.commonsensemedia.org/app-reviews/joon-kids-chore-list-chart); [App Store](https://apps.apple.com/us/app/joon-kids-adhd-chore-tracker/id1482225056) |
| **Goblin Tools** (Bram De Buyser) | Neurodivergent teens and adults | Free AI micro-tools: **Magic ToDo** (recursive task breakdown), Formalizer, Judge (tone reading), Estimator, Compiler, Chef | E4. Popular because it is simple, free and practical. | Free web; small one-time mobile fee **[M]** | Example of "AI as executive-function prosthetic"; went viral 2023–24 | LLM output quality varies; not child-directed | [V] [goblin.tools](https://goblin.tools/About); [QUB](https://blogs.qub.ac.uk/studentatguide/2025/02/19/introducing-goblin-tools-ai-powered-support-for-neurodivergent-thinkers/) |

### A4.4 Speech & language

| App | Target / age | What it does | Evidence | Pricing | Strengths | Complaints / risks | Sources |
|---|---|---|---|---|---|---|---|
| **Speech Blubs** | Speech/language delay, late talkers; ~1–8 | Video modeling: kids imitate peer "speech heroes." Face filters. | E3 (video modeling is supported; product-level evidence is limited) | Subscription ~**$59.99/year** **[M]**. Reviews cite $29.99/6 months and $59/year charges. | Kid-peer modeling is engaging | **Many billing complaints:** charged after trial cancellation, cannot cancel in-app, slow support, no phone support. ComplaintsBoard 3.2★. | [V] [ComplaintsBoard](https://www.complaintsboard.com/speech-blubs-b149129); [App Store reviews](https://apps.apple.com/us/app/speech-blubs-language-therapy/id1239522573?see-all=reviews&platform=iphone) |
| **Articulation Station** (Little Bee Speech) | Speech-sound disorders; ~3–10; SLP and parent tiers | Target sounds at word, phrase, sentence and story level; data tracking | E3. Classic SLP drill design. | **Hive parent $9.99/month or $83.99/year. Pro (with Test Center) $14.99/month or $119.99/year.** 14-day trial. | SLP-trusted; clear photos; data | Moved from one-time to subscription (SLP grumbling) | [V] [littlewords.ai](https://littlewords.ai/blog/articulation-station-review); [Little Bee Speech](https://www.littlebeespeech.com/blog/what-is-the-little-bee-hive-membership) |

### A4.5 Dyslexia & literacy

| App | Target / age | What it does | Evidence | Pricing | Strengths | Complaints / risks | Sources |
|---|---|---|---|---|---|---|---|
| **Nessy Reading & Spelling** | Dyslexia / struggling readers; ~5–12 | Structured-literacy, OG-inspired game curriculum | E3. **British Dyslexia Association Quality Mark**; Educational Resources Awards. | From **$15.50/month**; 3-month $47.75; Dyslexia Home Education Pack from $195.50/year | Structured, cumulative, fun | Cartoonish for older kids; subscription | [V] [Nessy](https://www.nessy.com/en-us/product/nessy-reading-and-spelling-home); [Literacy Hive](https://literacyhive.org/nessy-reading-spelling-program/) |
| **Dyslexia Quest** (Nessy) | Screening, ~5–12 | Game-based screener: RAN, working memory, phonemic/phonological awareness | E3 (screener, not diagnostic) | From **$25.50/year** | Cheap, non-threatening screening | Screener only; risk of false reassurance | [V] [Nessy](https://nessy.com/en-us/shop/home-products/dyslexia-quest/); [Common Sense](https://www.commonsensemedia.org/app-reviews/dyslexia-quest) |
| **Ghotit Real Writer & Reader** | Dyslexia, dysgraphia; teens and adults | Context-aware spelling/grammar for phonetic misspellings, word prediction, TTS | E3 | ~**$199 desktop**; iOS $50–$70; some $9.99/month options | Built specifically for dyslexic error patterns | Competes with free built-in tools (Microsoft Immersive Reader/Editor, Apple Accessibility Reader, Grammarly) | [V-2nd] [Undivided](https://undivided.io/resources/top-tech-apps-and-more-for-specific-learning-disabilities-2965) |

### A4.6 Regulated digital therapeutics / diagnostics & biofeedback

| Product | Target / age | What it does | Evidence | Pricing / access | Strengths | Complaints / risks | Sources |
|---|---|---|---|---|---|---|---|
| **EndeavorRx** (Akili → Virtual Therapeutics) | ADHD, inattentive/combined type. **FDA De Novo June 2020 for ages 8–12; label expanded to 13–17.** **EndeavorOTC** cleared for adults (OTC). | Action video game (Selective Stimulus Management Engine) that trains attentional control | **E1.** First FDA-authorized game-based therapeutic. STARS-ADHD RCT (n≈348, ages 8–12; Kollins et al., *Lancet Digital Health* 2020) improved the objective attention metric (TOVA API) vs. control. **Parent-rated ADHD symptoms did not differ significantly from control.** **[M — trial stats not re-verified]** | Rx; roughly $99/month cash price historically **[M]**. Poor payer coverage. | Regulatory first; strong brand halo | **Commercial failure:** Akili cut 46% of staff (Apr 2024) and sold to Virtual Therapeutics for ~$34M. Critics note weak real-world functional outcomes. | [V] [BioPharma Dive](https://www.biopharmadive.com/news/akili-sell-34m-virtual-therapeutics-digital/717576/); [Managed Healthcare Exec](https://www.managedhealthcareexecutive.com/view/fda-expands-akili-s-endeavorrx-game-based-digital-therapy-for-adhd-eligibility-to-ages-8-17); [BioSpace](https://www.biospace.com/akili-announces-fda-authorization-of-endeavorotc-the-first-fda-clearance-of-a-digital-treatment-for-adults-with-adhd-through-a-video-game); [PMC review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12495783/) |
| **Mightier** (Boston Children's Hospital spinout) | Emotional dysregulation, ADHD, autism, anxiety; ~6–14 | Heart-rate biofeedback games. Wearable HR strap; the game gets harder as HR rises, so kids practise calming down. | **E1/E2.** Sham-controlled RCTs (RAGE-Control): lower aggression and oppositional behavior, lower clinician-rated anger. Children's own anger ratings did not differ; the effect was on anger *expression*. **Community RCT (n=72, ages 7–12):** better adaptive emotion regulation after 6 weeks. Lower parenting stress. | Subscription ~$40/month incl. hardware **[M]**. Some payer/health-system partnerships **[M]**. | Strongest evidence among consumer emotional-regulation tools; clever biofeedback loop | Recurring cost. Mixed results on self-report. Using HR sensors on children makes this **sensitive biometric data** (COPPA 2025 PI expansion). | [V] [PMC proof-of-concept RCT](https://pmc.ncbi.nlm.nih.gov/articles/PMC8440816/); [Springer 2025](https://link.springer.com/article/10.1007/s10802-025-01387-x); [EurekAlert](https://www.eurekalert.org/news-releases/930620); [Mightier science](https://www.mightier.com/science/) |
| **Cognoa Canvas Dx** | Autism **diagnosis aid**, 18 months–6 years | ML combines a parent questionnaire, parent-uploaded home videos and a clinician questionnaire. Outputs positive, negative or indeterminate. | **E1.** FDA De Novo 2021. | Rx/clinical. **Wyoming Medicaid first state (Sept 2024); Highmark first commercial payer.** NY Medicaid evidence review Nov 2024. | Shortens diagnostic waits (months → days) | Indeterminate-output rate; equity of video-based AI; limited payer coverage | [V] [HCPLive](https://www.hcplive.com/view/fda-grants-de-novo-clearance-to-ai-based-autism-diagnosis-aid); [NY DOH](https://www.health.ny.gov/health_care/medicaid/ebbrac/meetings/2024/docs/2024-11-21_canvas_rpt.pdf); [HIT Consultant](https://hitconsultant.net/2024/09/26/cognoa-launches-first-state-medicaid-program-to-cover-ai-powered-autism-diagnostic/) |

### A4.7 Robots, tangibles & centers

| Product | Target | What it does | Evidence | Pricing | Notes | Sources |
|---|---|---|---|---|---|---|
| **Cosmo** (Filisia; distributed by Inclusive Technology) | Moderate–severe autism, PMLD, CP, brain injury; schools/therapy | Multisensory light-up **accessibility switches** ("Dots") + iPad Cosmo Learning app: cause-and-effect, turn-taking, motor games. Sold as Switch (1), Explore (3) or Excel (6). | E2/E3 (case studies, e.g., LGfL) | School pricing (not captured) | Strong model for **tangible, low-cognitive-load, multisensory** input | [V] [SchoolHealth](https://www.schoolhealth.com/blog/cosmo-by-filisia-interactive-and-multisensory-accessibility-switches/); [Inclusive](https://inclusive.com/products/cosmo-explore); [LGfL case study](https://curriculumblog.lgfl.net/cosmo-switch-case-study) |
| **Leka** (France) | Autism, Down syndrome, multiple disabilities | Spherical robot with an expressive face, light, sound and vibration; tablet-driven games; co-designed with therapists | E3/E4. No recent peer-reviewed efficacy found. | Crowdfund $390–$490. Later listing ~**€2,490**. | Multisensory, non-threatening form factor | [V] [The Robot Report](https://www.therobotreport.com/leka-robot-for-special-needs-kids-launches-on-indiegogo/); [Leobotics](https://en.leobotics.com/comparateur-robot/robot-leka-apf-france-handicap-outil-ludo-educatif-compagnon-enfant-autisme-assistance-a-la-personne) |
| **QTrobot** (LuxAI, Luxembourg) | Autism; home and school | Humanoid social robot with an emotion/social-skills curriculum | E2. **69-family longitudinal home study with LIH + Univ. of Birmingham launched Dec 2025, due to end ~late 2026.** | **Home: $1,980 device + $140/month (1-yr) or $1,540/year. Pro: $4,000 + $3,900/year.** | Most research-engaged social-robot vendor | [V] [LuxAI shop](https://luxai.com/shop/); [LIH](https://www.lih.lu/en/article/luxai-luxembourg-institute-of-health-and-university-of-birmingham-launch-the-first-large-scale-study-of-at-home-robot-led-early-development-support-for-autistic-children-with-qtrobot/) |
| **Brain Balance** (centers) | ADHD, autism, dyslexia, anxiety | Center-based "hemispheric integration" sensory-motor + academic program + dietary changes | **E4 / contested.** Only two low-quality studies. Experts call it pseudoscientific. **Wisconsin DHS found insufficient evidence.** | ~**$12,000 for 6 months**; not insured | **Cautionary tale:** high price, weak evidence, reputational risk. Note FTC precedents against similar "brain training" (LearningRx, Lumosity $2M). | [V] [NBC News](https://www.nbcnews.com/news/amp/ncna1100681); [KQED](https://www.kqed.org/futureofyou/442896/little-evidence-for-brain-balances-alternative-autism-treatment); [ASAT](https://asatonline.org/for-parents/becoming-a-savvy-consumer/is-there-science-behind-that-brain-balance/); [Frontiers 2024](https://www.frontiersin.org/journals/child-and-adolescent-psychiatry/articles/10.3389/frcha.2024.1450695/full); [FTC Lumosity](https://www.ftc.gov/news-events/news/press-releases/2016/01/lumosity-pay-2-million-settle-ftc-deceptive-advertising-charges-its-brain-training-program) |

### A4.8 Platform-level and AI-era inclusive tools (2024–2026)

| Tool | What's new | Why it matters | Status |
|---|---|---|---|
| **Apple Accessibility Nutrition Labels** | App Store product pages show supported features (VoiceOver, Voice Control, Larger Text, Sufficient Contrast, Reduced Motion, captions…). Searchable from Sept 2025. Apple signalled they will become required on submission. | Accessibility becomes a **discoverable feature**. Parents of disabled kids will filter on it. | [V] [Apple Newsroom](https://www.apple.com/newsroom/2025/05/apple-unveils-powerful-accessibility-features-coming-later-this-year/); [Apple Support](https://support.apple.com/en-us/123073) |
| **Apple Accessibility Reader, Head Tracking, Braille Access** (2025 OS releases) | System-wide reading mode for dyslexia/low vision; head-movement control | Raises the baseline, so apps must not break system settings | [V] [9to5Mac](https://9to5mac.com/2025/05/13/apple-unveils-ios-19-accessibility-features/) |
| Apple Eye Tracking, Music Haptics, Vocal Shortcuts, Vehicle Motion Cues (2024); Personal Voice / Live Speech (2023) | Built-in AAC-adjacent and motor features | Personal Voice lets at-risk speakers bank their voice; Live Speech is type-to-speak | **[M]** |
| Microsoft Immersive Reader / Reading Coach; Google Project Relate; Voiceitt | Free literacy supports; recognition of atypical speech | Free built-in tools compete with paid dyslexia apps | **[M]** |
| **Cognoa, Goblin Tools, Tiimo AI** | AI diagnosis aid; AI task breakdown; AI planning | See above | [V] |
| LLM-powered AAC prediction (various startups, 2025–26) | Context-aware phrase prediction, "expand my 3 symbols into a sentence" | Promising but raises questions about **authorship and "putting words in the user's mouth"**, which the AAC community considers critical | **[M]** — no verified product-specific source captured |

## A5. Cross-cutting complaint patterns (synthesized)

1. **Billing and cancellation dark patterns.** Trial-to-annual traps and in-app cancellation that does not work (Speech Blubs, Joon) [V]. These also run into the COPPA/AADC "no nudge" rules and FTC negative-option enforcement **[M: FTC "click-to-cancel" rule was vacated by the 8th Circuit in July 2025]**.
2. **Setup burden on caregivers.** Hours of configuration, and cross-device sync bugs (Goally) [V]. Caregiver time is the scarcest resource.
3. **Novelty decay.** Gamified reward loops lose power within weeks (Joon) [V]. The product needs **progression, variety and a path to fade the reward**.
4. **Price vs. uncertainty.** $250–$300 AAC apps and $12k programs, with little product-level evidence.
5. **Age-inappropriate aesthetics.** Cartoonish UI for teens and adults with intellectual disability is seen as infantilizing **[M: common SLP/self-advocate critique]**.
6. **Over-stimulation.** Loud rewards, confetti and flashing, even in apps marketed for autism **[M: common OT/parent critique]**.
7. **Platform lock-in.** iOS-only (Proloquo2Go, Tiimo) leaves out Android- and Chromebook-heavy families and districts.
8. **Data trust.** Behavior logs, voice, video (Cognoa) and heart rate (Mightier) are highly sensitive. The 2025 COPPA amendments expanded "personal information," including biometric identifiers [V].

## A6. Positioning: neurodiversity-affirming vs. ABA

- **The tension [V]:**
  - Autistic self-advocates criticize traditional ABA for aiming to make autistic people appear "normal." That means suppressing stimming, forcing eye contact, and focusing on compliance. They link it to later mental-health harms, and the **#ABAisAbuse** movement grew out of this.
  - BCBA training programs now often include neurodiversity-affirming content.
  - Critics warn of tokenistic "**neurodiversity-lite**" practice.
  - Sources: [Child Mind Institute](https://childmind.org/article/controversy-around-applied-behavior-analysis/); [PMC — Affirming Neurodiversity within ABA](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11219658/); [MDPI 2025](https://www.mdpi.com/2075-4698/15/3/72); [Disability & Society 2025](https://www.tandfonline.com/doi/full/10.1080/09687599.2025.2478049); [Temple ICLJ 2025](https://sites.temple.edu/ticlj/files/2025/05/Leone-The-Neurodiversity-Critique-of-Applied-Behavior-Analysis-Therapy-for-Autistic-Children-in-the-Context-of-International-Human-Rights-Treaties.pdf).
- **The commercial reality:** ABA is the dominant insurance-funded autism intervention in the US, and BCBAs are a real buyer channel **[M]**. Many parents search for "ABA app."
- **Recommended positioning for the studio:**
  - Use **identity-first or person-first language as the user chooses**. Many autistic adults prefer "autistic person" **[M]**.
  - Frame goals as **skills the learner and family choose**: communication, self-advocacy, regulation, independence. Never "reduce autistic behaviors."
  - **Never target stimming, eye contact or "looking normal."** Support regulation instead: offer calm-down tools, and don't punish meltdowns.
  - Use **visual supports, AAC and predictability**. These are supported across both camps.
  - **Include autistic and ADHD co-designers**, paid, with credit in the product. Tiimo and Miracle Modus show that lived-experience design builds trust.
  - Provide data for IEP and clinical teams without building "compliance trackers."
  - **Never make cure/recovery claims.** Keep efficacy claims to what product-level evidence supports (FTC risk).

---

# PART B — INCLUSIVE & SENSORY UX: EVIDENCE BASE

## B1. Standards & guidelines

### WCAG 2.2 (W3C Recommendation, 5 Oct 2023) [V]
- Adds **9 new success criteria** and removes 4.1.1 Parsing.
- The criteria that matter most for children, neurodivergent users and seniors:
  - **2.5.8 Target Size (Minimum), AA:** pointer targets ≥ **24×24 CSS px** (or have enough spacing).
  - **2.5.7 Dragging Movements, AA:** anything done by dragging must also work with a single pointer and no drag. This is **critical for toddlers and motor-impaired users**.
  - **2.4.11 Focus Not Obscured (Minimum), AA.**
  - **3.3.8 Accessible Authentication (Minimum), AA:** no cognitive-function tests (remembering passwords, puzzles) unless an alternative or assistance exists. This fits kids, cognitive disabilities and seniors.
  - Also new in 2.2 **[M]**: 3.2.6 Consistent Help (A) and 3.3.7 Redundant Entry (A).
- Long-standing criteria that matter for sensory design **[M]**:
  - 1.4.3 Contrast 4.5:1 (AA)
  - 1.4.12 Text Spacing (AA)
  - 2.2.2 Pause, Stop, Hide (A)
  - 2.3.1 Three Flashes (A)
  - 2.3.3 Animation from Interactions (AAA)
  - 1.4.2 Audio Control (A)
  - 3.1.5 Reading Level (AAA: lower-secondary level or supplement)
- Sources: [Deque WCAG 2.2](https://dequeuniversity.com/resources/wcag-2.2/); [Vispero](https://vispero.com/resources/new-success-criteria-in-wcag22/).

### WCAG 3.0 status [V]
- A new Working Draft was published **10 Sep 2026**. Several former AAA-only requirements moved into the core tier.
- The March 2026 draft renamed "outcomes" to **"requirements" (174)**.
- **Not normative.** Candidate Recommendation is anticipated around **Q4 2027**; final Recommendation not before **2028**.
- **Implication:** build to WCAG 2.2 AA now, and track WCAG 3's cognitive and sensory requirements as a roadmap.
- Sources: [W3C WAI news](https://www.w3.org/WAI/news/2026-09-10/wcag3/); [WCAG 3.0 WD](https://www.w3.org/TR/2026/WD-wcag-3.0-20260910/); [AbilityNet](https://abilitynet.org.uk/resources/digital-accessibility/what-expect-wcag-30-web-content-accessibility-guidelines).

### W3C COGA — "Making Content Usable for People with Cognitive and Learning Disabilities" (W3C WG Note, 2021) [V]
- This is informative guidance that goes beyond WCAG.
- It has **8 objectives**:
  1. Help users understand what things are and how to use them
  2. Help users find what they need
  3. Use clear and understandable content
  4. Help users avoid mistakes and know how to correct them
  5. Help users focus
  6. Ensure processes do not rely on memory
  7. Provide help and support
  8. Support adaptation and personalization
- It also includes personas, user needs, and guidance on involving users.
- Companion research modules cover **online safety** and **voice systems** for cognitive accessibility.
- Sources: [COGA Content Usable](https://w3c.github.io/coga/content-usable/); [W3C news](https://www.w3.org/news/2021/working-group-note-making-content-usable-for-people-with-cognitive-and-learning-disabilities/); [COGA voice](https://www.w3.org/TR/coga-voice/); [COGA safety](https://www.w3.org/TR/coga-safety/).

### Universal Design for Learning — UDL Guidelines 3.0 (CAST, 30 Jul 2024) [V]
- The three principles are unchanged: **Engagement, Representation, Action & Expression**.
- The goal shifts from "expert learners" to **learner agency** (purposeful and reflective, resourceful and authentic, strategic and action-oriented).
- "Provide" language was removed so the guidelines read as co-creation with learners, not an adult checklist.
- New emphasis areas:
  - **identity as part of variability**
  - **joy and play**
  - belonging
  - multilingual/multicultural perspectives
  - confronting bias
  - barriers at the individual, institutional and systemic levels
- Sources: [CAST UDL 3.0](https://udlguidelines.cast.org/more/about-guidelines-3-0/); [Novak Education](https://www.novakeducation.com/blog/what-to-know-about-the-udl-guidelines-3.0-update).

### UK Home Office / GOV.UK "Designing for accessibility" posters [V]
- The set covers autism, screen readers, low vision, physical/motor, deaf/hard of hearing and dyslexia.
- The **autism poster** says:
  - **Do:** use simple colours, write in plain English, use simple sentences and bullets, make buttons descriptive, build simple and consistent layouts.
  - **Don't:** use bright contrasting colours, figures of speech/idioms, walls of text, vague buttons, or cluttered layouts.
- Sources: [Home Office autism poster](https://ukhomeoffice.github.io/accessibility-posters/autism); [GOV.UK blog](https://accessibility.blog.gov.uk/2016/09/02/dos-and-donts-on-designing-for-accessibility/).
- *BBC GEL / BBC accessibility guidance for neurodiverse audiences exists but was not verified in this session* **[M]**.

### Dyslexia-friendly typography — BDA Dyslexia Style Guide 2023 [V]
- Font size **12–14 pt (≈16–19 px)**; some readers want larger.
- Letter spacing ≈ **35% of average letter width**; word spacing ≥ **3.5× letter spacing**; line spacing **1.5**.
- Single-colour backgrounds with no patterns; **dark text on a light, not pure white, background**; avoid green and red/pink.
- Also **[M]**: use sans-serif fonts (Arial, Verdana, Century Gothic…); avoid italics, underline and ALL CAPS; left-align and don't justify; keep lines to 60–70 characters.
- **Special "dyslexia fonts" (OpenDyslexic, Dyslexie) have not been shown to beat standard sans-serif fonts** in controlled studies **[M — e.g., Wery & Diliberto 2017; Kuster et al. 2018]**.
- Source: [BDA Style Guide 2023 PDF](https://cdn.bdadyslexia.org.uk/uploads/documents/Advice/style-guide/BDA-Style-Guide-2023.pdf?v=1680514568).

### Platform guidelines **[M]**
- **Apple HIG:** minimum hit target **44×44 pt**; support Dynamic Type, Reduce Motion, Reduce Transparency, Increase Contrast, VoiceOver, Switch Control, Guided Access (single-app mode, useful for kids and autism).
- **Google Material / Android:** minimum touch target **48×48 dp**; support font scaling, TalkBack, Switch Access, "Remove animations."
- **Both:** respect system accessibility settings. Never override user text size or motion preferences.

## B2. Multi-sensory learning — what the evidence actually says

| Approach | Evidence status | Design takeaway |
|---|---|---|
| **Orton-Gillingham** (structured, explicit, multisensory phonics) | **Stevens et al. 2021 meta-analysis (16 studies):** foundational-skills ES = 0.22, **not statistically significant** (p=.40); comprehension/vocab ES = 0.14 (p=.57). Positive direction, wide variance, small samples. EdWeek 2025 notes the "multisensory" component in particular is unproven. [V] | The *structured, explicit, cumulative phonics* part is well supported (National Reading Panel). Don't market "multisensory" as the active ingredient. Use multisensory channels for **engagement and access**, and build the curriculum on structured literacy. Sources: [Stevens et al. PDF](https://mimtsstac.org/sites/default/files/session-documents/Resource%204_2021_Stevens%20et%20al.%20OG%20meta-analysis.pdf); [EdWeek 2025](https://www.edweek.org/teaching-learning/popular-reading-programs-feature-multisensory-instruction-does-it-help/2025/06); [Reading League](https://www.thereadingleague.org/wp-content/uploads/2025/06/trl-journal-sneakpeek-orton-gillingham-interventions-solari.pdf) |
| **Montessori** (self-directed, hands-on, concrete-to-abstract materials) | **National lottery-based RCT (Lillard et al., PNAS Oct 2025; n=588, 24 public programs):** by end of kindergarten, Montessori students scored higher in **reading, executive function, short-term memory and social understanding**. Math was positive in most models. **~$13,127 lower cost per child** over 3 years. [V] | Strong support for **learner choice, concrete manipulation, self-correcting materials, and uninterrupted work cycles**. Translate this into self-correcting digital activities with low extrinsic reward. Sources: [PNAS](https://www.pnas.org/doi/10.1073/pnas.2506130122); [UVA](https://as.virginia.edu/news/nationwide-uva-led-study-finds-montessori-preschool-boosts-learning-lower-cost) |
| **Tangible / switch-based multisensory** (Cosmo) | Case-study level [V] | Good for PMLD and early cause-and-effect; pair light, sound and haptics with one simple action |
| **Biofeedback** (Mightier) | RCT-supported for expression of anger and emotion regulation [V] | Physiological signals can drive adaptive difficulty. Handle them as sensitive data. |

## B3. Children's touch interaction & developmental UX

- **Vatavu, Cramariuc & Schipor (IJHCS 2015)** [V] — [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1071581914001426):
  - 89 children aged 3–6 produced 2,912 touch records across tap, double-tap, single- and multi-touch drag-and-drop.
  - Success rates: **3-year-olds 73%** vs. **>5-year-olds 89%**.
  - Adults were still **30% more accurate on taps** and **10% more accurate on drag** than the best children.
  - Drag accuracy correlates with visuospatial processing and finger dexterity.
  - **Implication:** under-5s need **very large targets, tolerant hit areas, and single-tap primary actions**. Drag should be optional and forgiving (this lines up with WCAG 2.5.7).
- **NN/g "UX Design for Children (Ages 3–12)" 4th ed.** (156 guidelines) [V] — [NN/g report](https://www.nngroup.com/reports/children-on-the-web/); [NN/g physical development](https://www.nngroup.com/articles/children-ux-physical-development/):
  - Segment design into **3–5 (pre-readers), 6–8 (beginning readers), 9–12 (moderately skilled readers)**.
  - Touch targets **≥ 2 cm × 2 cm for young children** (about 4× the ~1 cm adult guideline).
  - Kids under 9 should get **swipe, tap and simple drag**, which use large arm and hand movements. Avoid gestures that need fine motor control (pinch, precise long-press, multi-finger).
- **NN/g teenagers report (13–17)** [V — exists; findings not re-verified] — [NN/g](https://www.nngroup.com/reports/teenagers-on-the-web/). Teens dislike childish design, have less patience than adults assume, and are not "digital natives" at complex tasks **[M]**.
- **Toddlers (1–3) [M]:**
  - Before ~18–24 months, children learn poorly from 2D screens without a live, responsive adult (the "video deficit").
  - Live video chat is the notable exception because it is responsive.
  - **Joint media engagement (JME)** means an adult co-using the media and connecting it to the real world. It improves learning transfer (Takeuchi & Stevens, Joan Ganz Cooney Center 2011).

## B4. AAP screen-time guidance & joint media engagement

- **Jan 20, 2026 — AAP policy statement "Digital Ecosystems, Children, and Adolescents"** (*Pediatrics* 157(2)) [V]:
  - Replaces the 2016 statements and **drops set screen-time limits**.
  - Reframes the issue around the "digital ecosystem": engagement-based designs that are immersive, pervasive and commodified. Also looks at caregiver relationships, platform design, commercial incentives and systems.
  - Recommends **family media plans**, **co-engagement**, media literacy and system-level/industry change.
  - Sources: [Pediatrics](https://publications.aap.org/pediatrics/article/157/2/e2025075320/206129/Digital-Ecosystems-Children-and-Adolescents-Policy); [AAP explainer](https://www.aap.org/en/patient-care/media-and-children/center-of-excellence-on-social-media-and-youth-mental-health/understanding-the-new-AAP-digital-media-guidelines/); [EdSurge](https://www.edsurge.com/news/2026-02-05-new-aap-screen-time-recommendations-focus-less-on-screens-more-on-family-time).
- **Legacy 2016 guidance (still widely quoted by parents) [M]:**
  - Under 18–24 months: avoid screens except video chat.
  - Ages 2–5: ≤1 hour/day of high-quality programming, co-viewed.
  - 6+: consistent limits.
- **Design implication:** The AAP now puts responsibility on **product design**, meaning no engagement-maximizing mechanics. This matches the UK AADC, the state codes and KOSA's "compulsive use" features. "Built for co-play" and "stops itself" are now credible differentiators.

## B5. Seniors UX (60+) [mostly M — NN/g pages blocked]

- **Vision:**
  - Presbyopia, reduced contrast sensitivity, yellowing lens (blue/green discrimination), glare sensitivity.
  - Use **larger default text (≥16–18 px body)**, high contrast, and avoid light-grey text.
- **Motor:**
  - Tremor, arthritis, and slower, less precise pointing.
  - Use **larger targets (≥ 44–48 pt/dp, ideally larger)**, generous spacing, no time-limited or precision gestures, no hover-only reveals, and alternatives to drag (WCAG 2.5.7).
- **Cognitive:**
  - Slower processing and reduced working memory; crystallized knowledge stays strong.
  - Keep **step-by-step flows, explicit labels (icons + text), consistent navigation, clear error recovery, and no reliance on memory** (COGA Objective 6; WCAG 3.3.8).
- **Hearing:** high-frequency loss. Provide captions, adjustable volume, and don't rely on sound alone for alerts.
- **Research:**
  - NN/g's senior-usability research (2002, updated ~2019) found older users markedly slower and less successful than younger adults.
  - Seniors are **not a monolith**: tech-confident "young-old" users coexist with frail "old-old" users.
  - **[M — numbers not re-verified]**
- **Role:** increasingly **grandparent-as-caregiver/co-player**. This is an under-served intergenerational JME use case.

## B6. AI voice & conversational UX for kids [mostly M]

- **Speech recognition of children's speech is markedly less accurate** than for adults. Error rates are higher still for young, accented, disordered (apraxia, dysarthria) or AAC-generated speech. Design fallbacks are needed: tap-to-answer, choice chips, and "I didn't catch that" without blame.
- **COGA voice-systems module** [V — exists]: give extra time to respond, avoid long menus, allow repetition and reformulation, and don't time out quickly — [COGA voice](https://www.w3.org/TR/coga-voice/).
- **Anthropomorphism and parasocial risk:**
  - Children attribute mind and feelings to voice agents.
  - AI "companions" for minors are under regulatory scrutiny **[M]**:
    - the **FTC 6(b) inquiry into AI companion chatbots (Sept 2025)**, with orders to Alphabet, Character.AI, Meta/Instagram, OpenAI, Snap and xAI
    - **California SB 243 (2025)**, on companion-chatbot disclosures and protections for minors
  - Design stance: the agent is **clearly a tool, not a friend**. No simulated romance or emotional dependency. Regular disclosure that it is AI. Escalate to a human for distress.
- **EU AI Act Art. 5 [M]:** since Feb 2025 it **prohibits emotion-recognition AI in education institutions** (with medical/safety exceptions). Do not infer learners' emotions from face or voice in a school product sold in the EU. Self-report is fine.
- **Voice/audio recordings of children are "personal information" under COPPA.** The 2025 amendments further expanded PI (biometric identifiers) [V/M].
- **AAC authorship:** AI "sentence expansion" must keep the **user in control**, show what the AI added, and support editing.

## B7. Child-safety & privacy regulation (status as of 2026-09-29)

| Regime | Status | Key design obligations | Source |
|---|---|---|---|
| **COPPA Rule (US, <13)**, 2025 amendments | Published 22 Apr 2025; effective 23 Jun 2025; **full compliance required since 22 Apr 2026** [V] | Expanded "personal information" (incl. biometric identifiers [M detail]). **Separate verifiable parental consent for third-party disclosures** (e.g., targeted ads). New conditions on the "support for internal operations" exception. **Written information-security program.** Written data-retention policy / no indefinite retention [M detail]. The FTC has signalled COPPA enforcement as a priority. | [Federal Register](https://www.federalregister.gov/documents/2025/04/22/2025-05904/childrens-online-privacy-protection-rule); [Hunton](https://www.hunton.com/privacy-and-information-security-law/ftc-publishes-final-coppa-rule-amendments); [Davis Polk](https://www.davispolk.com/insights/client-update/ftc-prioritizes-coppa-enforcement-new-compliance-obligations-take-effect); [Finnegan](https://www.finnegan.com/en/insights/articles/coppas-amended-rule-is-now-in-full-effect-what-operators-need-to-know.html) |
| **KOSA / KIDS Act (US federal)** | **House passed H.R. 7757 KIDS Act 267–117 on 29 Jun 2026** (KOSA is its centerpiece; **no "duty of care"**). **Senate Commerce advanced amended S.1748 on 5 Aug 2026** (includes duty of care). No full Senate vote reported as of late Sept 2026. **Not law.** [V] | Strongest privacy/safety defaults for minors, parental tools, limits on compulsive-use design features | [Congress.gov S.1748](https://www.congress.gov/bill/119th-congress/senate-bill/1748); [CRS LSB11465](https://www.congress.gov/crs-product/LSB11465); [Washington Times](https://www.washingtontimes.com/news/2026/jun/29/house-passes-kids-online-safety-package-setting-battle-senate/) |
| **US state Age-Appropriate Design Codes** | **California** (2022): district court preliminary injunction (Mar 2025). The Ninth Circuit let parts proceed (coverage, age estimation, data use) but kept the injunction on dark-pattern provisions. **Maryland** (2024): challenged; no injunction. **Nebraska** (signed 30 May 2025): effective 1 Jan 2026, penalties from 1 Jul 2026. **Vermont** (signed 12 Jun 2025): effective 2027. [V] Plus a wave of **app-store age-verification laws** (Utah, Texas, Louisiana…) [M]. | DPIAs, high-privacy defaults, limits on profiling, no manipulative design, age estimation | [NatLawReview](https://natlawreview.com/article/us-state-law-status-age-appropriate-design-code-laws); [FPF](https://fpf.org/blog/vermont-and-nebraska-diverging-experiments-in-state-age-appropriate-design-codes/); [Loeb 2026](https://www.loeb.com/en/insights/publications/2026/06/childrens-online-privacy-2026-state-app-store-design-code-and-social-media-laws) |
| **UK Age Appropriate Design Code (Children's Code, ICO)** | In force since 2021. **15 standards:** best interests, DPIA, age-appropriate application, transparency, detrimental use, policies, **default settings (high privacy)**, data minimisation, data sharing, **geolocation off**, parental controls (with child notice), **profiling off by default**, **no nudge techniques**, connected toys/devices, online tools. **Data (Use and Access) Act 2025** (Royal Assent 19 Jun 2025) makes children's "higher protection" part of UK GDPR Art. 25 [V-2nd; commencement timing to confirm]. UK **Online Safety Act** children's safety codes enforceable from Jul 2025 [M]. | As listed | [ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/childrens-information/childrens-code-guidance-and-resources/age-appropriate-design-a-code-of-practice-for-online-services/executive-summary/); [Wikipedia summary via search](https://en.wikipedia.org/wiki/Children%27s_Code); [gdprlocal](https://gdprlocal.com/age-appropriate-design/) |
| **GDPR-K (EU GDPR Art. 8)** | Digital age of consent 16 by default; member states may lower it to 13 (patchwork: 13, 14, 15, 16) [M] | Parental consent below the national age; child-friendly privacy notices (Art. 12); DPIA for large-scale processing of children's data | [M] |
| **EU AI Act** | Prohibitions (Art. 5) apply from **2 Feb 2025** [M], incl. **emotion recognition in education** and exploiting vulnerabilities due to age or disability. **High-risk Annex III** includes education/vocational training (AI deciding access/admission, evaluating learning outcomes, steering learning, assessing the appropriate education level, proctoring) [M on the exact list]. **Digital Omnibus (Reg. (EU) 2026/1744, in force 27 Jul 2026) moved the Annex III high-risk deadline from 2 Aug 2026 to 2 Dec 2027.** [V] Transparency obligations (Art. 50) and AI-literacy duties still apply sooner. [V/M] | For EU edtech AI that grades, places or adapts: risk-management system, data governance, human oversight, logging, accuracy/robustness, conformity assessment by Dec 2027 | [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-omnibus-vii-deadline-delay-20260/); [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/); [Jones Walker](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon) |
| **FERPA / state student-privacy laws (US)** | In force [M] | School-official exception, DPAs, no sale or ad-targeting of student data (e.g., CA SOPIPA) | [M] |
| **FDA (digital health claims)** | In force | Claiming to diagnose or treat ADHD/autism makes the product a medical device (EndeavorRx, Canvas Dx). "General wellness" and education claims avoid this. | [V examples above] |
| **FTC Act §5 (efficacy claims)** | In force | Claims like "clinically proven to improve ADHD/autism" need competent and reliable scientific evidence (LearningRx $4M judgment, suspended to $200k; Lumosity $2M) | [V] [FTC 2016 LearningRx](https://www.ftc.gov/news-events/news/press-releases/2016/05/marketers-one-one-brain-training-programs-settle-ftc-charges-claims-about-ability-treat-severe) |

---

# PART C — INCLUSIVE & SENSORY UX FRAMEWORK

**18 principles.** Each lists the rationale, sources, and concrete Do / Don't.

### P1. Respect the user's sensory settings, and default to calm
- **Rationale:**
  - Sensory over-responsivity is common in autism, ADHD and sensory processing differences.
  - The GOV.UK autism poster says to avoid bright contrasting colours.
  - Vestibular disorders make motion harmful.
  - Apple and Google expose OS-level settings (Reduce Motion, Increase Contrast).
  - Sources: GOV.UK poster [V]; WCAG 2.3.3/2.2.2 [M]; Apple Accessibility Nutrition Labels list "Reduced Motion" [V].
- **Do:**
  - Read `prefers-reduced-motion`, `prefers-contrast` and the OS text size, and honor them automatically.
  - Offer an in-app **"Calm mode"** preset: muted palette, no parallax, soft or no sound, fewer simultaneous elements.
  - Put the sensory toggle **on the first screen** and in a persistent corner.
- **Don't:**
  - Autoplay full-screen confetti, shaking screens, or strobing reward animations.
  - Override the system font size.
  - Hide motion settings three menus deep.

### P2. Separate and granular sound control; never rely on sound alone
- **Rationale:**
  - Auditory hypersensitivity is common in autism.
  - Sound-only cues exclude deaf and hard-of-hearing users, and seniors with high-frequency loss.
  - Sources: WCAG 1.4.2 Audio Control [M]; COGA [V]; GOV.UK posters [V].
- **Do:**
  - Provide **separate sliders**: voice/narration, music, sound effects.
  - Use soft-attack sounds and cap loudness.
  - Pair every audio cue with a visual cue and optional **haptic** cue.
  - Provide captions for narration.
- **Don't:**
  - Play background music by default in learning tasks.
  - Use sudden loud "wrong!" buzzers.
  - Tie the sound level to reward intensity.

### P3. Predictable structure: same place, same behavior, preview what's next
- **Rationale:**
  - Uncertainty drives anxiety for autistic users.
  - The GOV.UK poster calls for consistent layouts and descriptive buttons.
  - COGA Objectives 1–2; WCAG 3.2.3/3.2.4 [M] and 3.2.6 Consistent Help [M].
  - Visual schedules are an evidence-based autism practice [M].
- **Do:**
  - Show a **visual "now / next / done" strip** for every session.
  - Keep navigation and help in fixed positions.
  - Give **transition warnings** ("2 more turns, then snack") with a visual timer.
  - Label buttons with outcomes ("Save and go to map").
- **Don't:**
  - Change the layout between levels.
  - Surprise the user with pop-ups or unannounced mode switches.
  - Use icon-only mystery buttons.

### P4. Big, forgiving, tap-first targets that scale by age
- **Rationale:**
  - 3-year-olds succeed only ~73% of the time on touch tasks, and adults are 30% more accurate on taps (Vatavu 2015) [V].
  - NN/g recommends ≥2×2 cm targets for young children [V].
  - WCAG 2.2 sets 24×24 px as the minimum and 2.5.7 requires dragging alternatives [V].
  - Apple asks for 44 pt and Android for 48 dp [M].
- **Do:**
  - Toddlers/preschool: targets **≥ 2 cm (~75–100 px)** with padded hit areas beyond the visible shape.
  - Seniors: ≥ 48–56 dp.
  - Make every drag also possible as **tap-source, then tap-destination**.
  - Ignore accidental palm touches.
- **Don't:**
  - Require pinch, long-press, double-tap or multi-finger gestures for core actions for under-7s, motor-impaired users or seniors.
  - Put targets at screen edges next to OS gestures.

### P5. Plain, literal language with a reading-level dial
- **Rationale:**
  - Autistic users may interpret idioms literally (GOV.UK) [V].
  - COGA Objective 3 [V]; WCAG 3.1.5 [M].
  - The BDA style guide [V].
- **Do:**
  - Use short sentences, one idea per sentence, and bullets.
  - Use literal words ("Tap the red circle").
  - Provide **read-aloud with word highlighting**.
  - Let caregivers set the reading level (pre-reader icons+audio → early reader → fluent).
  - Keep a glossary for new words.
- **Don't:**
  - Say "You nailed it!", "Break a leg" or use sarcasm.
  - Show walls of text or rely on text-only instructions for pre-readers.

### P6. Dyslexia-friendly typography by default, adjustable by user
- **Rationale:** BDA 2023 [V]; WCAG 1.4.12 Text Spacing [M]; "dyslexia fonts" are not superior [M].
- **Do:**
  - Use a clean sans-serif at **≥16–19 px** body text.
  - Set line-height **1.5**, slightly increased letter spacing, and left-aligned text.
  - Use off-white or cream backgrounds and dark-grey text.
  - Offer user controls for font, size, spacing and background tint.
  - Aim for 60–70 characters per line.
- **Don't:**
  - Justify text, use italics or ALL CAPS for emphasis, use patterned backgrounds, or rely on red/green contrasts.
  - Claim a special font "treats" dyslexia.

### P7. Multi-modal in, multi-modal out (UDL)
- **Rationale:**
  - UDL 3.0's multiple means of representation, action & expression [V].
  - AAC evidence [M].
  - Multisensory channels help access and engagement, even though the multisensory component of OG is unproven as the active ingredient [V].
- **Do:**
  - Let learners answer by **tap, voice, AAC symbol, drawing, or switch**.
  - Present content as picture + word + audio.
  - Support **switch access and eye gaze** (Cosmo, TD Snap patterns).
  - Integrate with the OS AAC and voice features.
- **Don't:**
  - Make voice the only input: child speech recognition is unreliable [M].
  - Penalize a non-speaking child for "not answering."

### P8. Errorless / low-penalty learning and easy recovery
- **Rationale:**
  - COGA Objective 4 (avoid mistakes, know how to correct them) [V].
  - Montessori's self-correcting materials [V].
  - Frustration intolerance is common in ADHD and anxiety.
- **Do:**
  - Use **gentle, informative feedback** ("Try the one that starts with /m/").
  - Fade scaffolds progressively.
  - Provide undo everywhere.
  - Auto-save.
  - Allow "skip for now."
- **Don't:**
  - Use lives, hearts, time pressure or loud failure states in learning cores.
  - Reset progress on error.

### P9. Help focus: one primary task per screen; manage attention, don't exploit it
- **Rationale:**
  - COGA Objective 5 [V].
  - ADHD attention differences.
  - The AAP 2026 statement criticizes engagement-maximizing design [V].
  - The UK AADC bans nudge techniques [V].
  - KOSA and the state codes target compulsive-use features [V].
- **Do:**
  - Keep one clear call-to-action per screen.
  - Hide non-essential chrome during tasks.
  - Offer optional **focus timers** (Tiimo/Brili style).
  - Build **natural stopping points** and session summaries.
- **Don't:**
  - Use infinite scroll, autoplay-next, streak-loss guilt, loot boxes, variable-ratio reward schedules, or "Are you sure you want to leave?" guilt-trips.

### P10. Don't rely on memory
- **Rationale:** COGA Objective 6 [V]; WCAG 3.3.8 Accessible Authentication and 3.3.7 Redundant Entry [V/M]. This matters for intellectual disability, ADHD working memory, young children and seniors alike.
- **Do:**
  - Use **picture passwords**, parent-device approval, magic links or passkeys for sign-in.
  - Show progress and previous answers on screen.
  - Carry information across steps.
- **Don't:**
  - Require remembering a password, a code from another screen, or multi-step instructions given only once.

### P11. Timing belongs to the user
- **Rationale:** WCAG 2.2.1 Timing Adjustable [M]; COGA voice guidance (extra time) [V]. Processing-speed differences occur in many conditions and in aging.
- **Do:**
  - Remove or make adjustable all time limits.
  - Give voice agents long, adjustable wait times.
  - Show timers as **visual, calm countdowns** only when the user chose them.
- **Don't:**
  - Auto-advance slides or time out AAC or voice input quickly.

### P12. Personalization profiles, set once and portable
- **Rationale:**
  - COGA Objective 8 [V].
  - UDL 3.0 emphasizes learner identity and variability [V].
  - Apple's labels make these features discoverable [V].
- **Do:**
  - Provide a **"My Needs" profile**: sensory, reading level, input mode, pace, avatar/voice, and preferred language/pronouns.
  - Let a caregiver or therapist configure it, while the **learner can view and change what's age-appropriate**.
  - Allow export for a new device or school.
- **Don't:**
  - Force a diagnosis label to unlock accommodations.
  - Make accommodations premium-only.

### P13. Age-respectful aesthetics: skill level ≠ age
- **Rationale:**
  - Teens and adults with intellectual disability are often given toddler-themed apps. Self-advocates and SLPs criticize this as infantilizing [M].
  - NN/g's teen research shows teens reject childish design [V exists / M detail].
- **Do:**
  - Decouple **content difficulty** from **visual theme**: offer mature themes (real photos, neutral palettes) at early-reader levels.
  - Use peer-aged voices and models.
- **Don't:**
  - Use cartoon animals and baby voices as the only option for a 16-year-old learning to read.

### P14. Caregiver-in-the-loop: co-play first, low admin
- **Rationale:**
  - The AAP 2026 statement emphasizes caregiver relationships and co-engagement [V].
  - Joint media engagement evidence [M].
  - Goally and Joon complaints are about setup and admin burden [V].
- **Do:**
  - Build **co-play prompts** ("Ask your child: what else is red in your room?").
  - Provide **templates that are ready in 5 minutes**.
  - Send a weekly 1-screen summary.
  - Make multi-caregiver sharing easy (parent, grandparent, SLP, teacher).
- **Don't:**
  - Require an hour of configuration before first use.
  - Bury co-play in settings.
  - Send notifications to the child's device that are meant for parents.

### P15. Motivation without manipulation (and plan the fade)
- **Rationale:**
  - Novelty decay (Joon) [V].
  - UDL 3.0's joy, play and agency [V].
  - Montessori's intrinsic motivation [V].
  - The neurodiversity critique of compliance-driven reinforcement [V].
  - AADC and KOSA limits on nudges [V].
- **Do:**
  - Use **mastery and progress visualizations**, learner-chosen goals, collections tied to learning, and **reward fading** schedules.
  - Celebrate calmly: a short, optional, sensory-light celebration.
- **Don't:**
  - Use token economies aimed at compliance ("sit still = points").
  - Use paid currencies, streak punishments, or rewards for suppressing stims or forcing eye contact.

### P16. Neurodiversity-affirming content & language
- **Rationale:** Autistic self-advocate critiques; neurodiversity-affirming practice guidance [V]; UDL 3.0's identity and bias focus [V].
- **Do:**
  - Let users choose identity-first or person-first language.
  - Frame goals around communication, autonomy and well-being.
  - Include diverse characters: disabled, AAC users, stimming characters, and varied ethnicities and families.
  - **Pay neurodivergent co-designers.**
- **Don't:**
  - Use "cure," "recover," "fix," "normal behavior," puzzle-piece iconography (disliked by many autistic adults [M]), or "low/high functioning" labels.

### P17. Honest evidence & efficacy claims
- **Rationale:**
  - Only a few products have RCTs [V].
  - FTC actions against brain-training claims [V].
  - FDA device rules for treatment and diagnosis claims [V examples].
  - The Brain Balance reputational example [V].
- **Do:**
  - State the evidence tier clearly ("built on structured literacy principles; product study underway with X University").
  - Publish outcomes.
  - Pre-register pilots.
  - Distinguish **education** from **treatment**.
- **Don't:**
  - Say "clinically proven," "treats ADHD," or "reduces autism symptoms" without an RCT or FDA authorization.
  - Cherry-pick parent testimonials as evidence.

### P18. Privacy-by-default and safe AI for minors and vulnerable users
- **Rationale:**
  - Amended COPPA [V]; UK AADC's 15 standards [V]; state AADCs [V].
  - EU AI Act high-risk (education) and Art. 5 prohibitions [V/M].
  - COGA online-safety module [V].
  - FTC and state scrutiny of AI companions [M].
- **Do:**
  - Practise data minimization, **profiling off by default**, **geolocation off**, and no third-party ads.
  - Get separate parental consent for any third-party sharing.
  - Keep **on-device processing for voice** where feasible.
  - Set clear retention limits.
  - Disclose the AI in child-readable language.
  - Give humans oversight of any AI that assesses or places learners.
  - Build **distress escalation** to caregivers.
- **Don't:**
  - Infer emotions from faces or voices in EU education products.
  - Train models on children's voice or video without explicit consent.
  - Design AI "friends" that simulate emotional dependency.
  - Use dark-pattern subscriptions or cancellation flows (Speech Blubs/Joon complaints) [V].

## C2. Per-age-segment UX table

Legend:
- Session length figures are **design targets synthesized** from AAP 2016/2026, NN/g and developmental norms **[M synthesis, not a single cited standard]**. Always let caregivers adjust them.
- Target sizes: see P4.

| Segment | Primary interaction modes | Target / motor | Session length (default) | Reading level & content | Sensory settings (defaults) | Caregiver role | Key risks / notes |
|---|---|---|---|---|---|---|---|
| **1–3 (toddlers)** | Single tap anywhere-ish; cause-and-effect; voice/video chat with a real person; tangible or switch toys (Cosmo-style) | Huge targets (≥2.5 cm), whole-screen hit zones; **no drag, pinch or double-tap** (3-year-olds are ~73% accurate on basic touch [V]) | **5–10 min**, adult-led; natural end screen | **Pre-literate:** real photos, spoken words, songs; one concept per screen | Calm by default; soft sounds; no flashing; no ads; no autoplay chains | **Essential: joint media engagement.** Adult sits with the child, prompts talk, connects to the real world (AAP 2026 [V]; JME [M]) | Video deficit under ~2 years [M]; displacing talk and play; COPPA (<13) [V] |
| **4–7 (preschool / early primary)** | Tap, simple drag (with tap alternative), swipe, voice with fallback, AAC | ≥2 cm targets (NN/g [V]); forgiving hit areas; drag optional | **10–20 min** blocks with transition warnings | **Pre-reader → beginning reader:** icon + audio instructions; read-aloud with highlighting; decodable text | Calm mode available; separate volume sliders; brief optional celebrations | **Co-player and setup:** adult configures and co-plays; weekly summary; SLP/OT templates | Voice-recognition failures on child speech [M]; over-rewarding; IAP traps |
| **8–12 (middle childhood)** | Tap, drag, typing starts, voice, game controllers; some multi-step navigation | ≥ 1.5 cm / 48 dp+; keyboard support | **15–30 min** focused blocks; optional focus timers | **Moderately skilled readers** (NN/g 9–12 [V]); plain language; glossary; TTS always available | User-controllable sensory panel; reduced-motion honored; no strobing (WCAG 2.3.1) | **Coach and monitor:** parent approves social/sharing; teacher/SLP dashboards; child starts to own their settings | Social comparison; streak pressure; EndeavorRx age band (8–17) shows the regulatory path [V] |
| **13–19 (teens)** | Full touch, keyboard, voice, messaging-style UIs; AI assistants; Watch/phone reminders (Tiimo-style) | Standard platform targets (44 pt/48 dp) | User-chosen; offer break nudges, not hard limits | **Age-respectful** content even at lower reading levels (P13); plain language; ~Grade 6–8 default with a dial | Full self-control of sensory settings; dark mode; notification controls | **Autonomy with a safety net:** teen controls profile; privacy from parents appropriate to age (AADC "parental controls with child notice" [V]); IEP transition planning | KOSA/state codes (compulsive-use design) [V]; AI companion risks [M]; stigma, so avoid "special-needs" branding |
| **20–34 (young adults)** | Mobile-first, voice, AI task breakdown (Goblin Tools), calendar integration | Platform standard + large-text support | Task-based, self-directed | Plain-language option; COGA patterns for complex flows (forms, money, health) | System settings honored; focus modes | **Self-directed;** optional trusted-supporter sharing (job coach, partner) | Late-diagnosed ADHD/autism adults are a big, underserved segment (Tiimo's success [V]); workplace accommodations |
| **35–59 (mid-life)** | Mobile + desktop; voice; often **as caregiver** of a neurodivergent child *and* sometimes as a neurodivergent adult | Platform standard; presbyopia begins (~40+), so easy text scaling | Short, interruptible sessions (caregiver time-poor) | Plain language; **5-minute setup**; scannable summaries | Respect OS contrast and text size | **Is the caregiver:** needs co-play scripts, progress reports, IEP-ready exports, multi-caregiver sharing | Setup burden (Goally complaints [V]); billing trust (Speech Blubs/Joon [V]) |
| **60+ (seniors)** | Tap with large targets, voice, simple linear flows; phone/video calls with grandchildren | **≥48–56 dp**, spacing, **no precision gestures**; drag alternatives (WCAG 2.5.7) | Self-paced; no timeouts (WCAG 2.2.1 [M]) | **≥16–18 px** body text, high contrast, icon + text labels, step-by-step | Captions; adjustable volume; avoid blue-on-blue; reduce glare and transparency | Often **grandparent-caregiver or co-player** (intergenerational JME); may need a trusted helper for setup | Accessible authentication (no memory tests, WCAG 3.3.8 [V]); scam and dark-pattern vulnerability; cognitive decline is variable [M] |
| **Neurodivergent (any age) overlay** | **All input modes:** AAC, switch, eye gaze, tap, voice, keyboard; choice of mode per task | Per profile (motor differences common in autism and DCD) | Learner- or caregiver-set; visual timers; **transition warnings**; natural stopping points | Reading level independent of age and theme (P13); literal language; social-story/visual-schedule scaffolds | **Calm mode on first screen**; granular sound; motion off option; predictable layouts; optional haptics; stim-friendly "calm corner" tool (no flashing — cf. Miracle Modus risk) | **Team:** learner, family, SLP/OT/BCBA/teacher. Learner agency first (UDL 3.0 [V]); data exportable to IEP; **neurodiversity-affirming goals** | ABA/compliance framing backlash [V]; over-stimulation; novelty decay; privacy of sensitive behavioral/biometric data [V] |

## C3. Build checklist for a studio MVP (derived)

1. WCAG 2.2 AA conformance + an Apple Accessibility Nutrition Label filled in **at launch**.
2. "My Needs" profile (P12) with a Calm-mode preset (P1) shown in onboarding.
3. Tap alternative for every drag (P4). Target sizes by age profile.
4. Read-aloud + highlight, and a reading-level dial (P5–P6).
5. Separate audio sliders + visual/haptic redundancy (P2).
6. Now/Next/Done strip + transition warnings (P3).
7. Co-play prompts + 5-minute templates + weekly caregiver summary (P14).
8. No streak punishment, loot boxes, autoplay or guilt prompts. Natural end screens (P9, P15).
9. COPPA-2025 / AADC privacy defaults. Separate third-party consent. Retention policy. On-device voice where possible (P18).
10. Evidence plan: logic model → pilot with a university or clinic → pre-registered study. Marketing claims limited to the tier achieved (P17).
11. Neurodivergent co-design panel (paid) + an autistic/ADHD advisory board named publicly (P16).
12. Fair billing: in-app cancellation, reminder before the trial converts, monthly option, family/school licensing.

---

## Appendix: Items flagged [M] that should be verified next

- EndeavorRx STARS-ADHD trial statistics, current pricing, and whether it is still on the market under Virtual Therapeutics in 2026.
- Mightier current pricing and payer partnerships.
- Speech Blubs and TD Snap current prices; Goblin Tools app price; Autism iHelp and Miracle Modus prices.
- NN/g senior usability figures (2019 report).
- FTC 6(b) AI companion inquiry (Sept 2025) details; California SB 243 provisions and effective date.
- EU AI Act Art. 5 emotion-recognition prohibition wording and Annex III(3) education list; whether the Omnibus changed Art. 50 timing.
- UK DUAA 2025 commencement of the children's higher-protection duty; Online Safety Act children's code dates.
- IDEA enrollment (NCES 2022–23/2023–24), DCD and DLD prevalence.
- Children's ASR error-rate literature (e.g., recent Interspeech studies).
- WCAG 2.2 3.2.6 / 3.3.7 and legacy criteria numbering (stable, but confirm for spec documents).
- Apple HIG 44 pt / Material 48 dp (stable, but confirm current HIG wording).

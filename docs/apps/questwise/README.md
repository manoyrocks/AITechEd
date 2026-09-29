# Questwise: App Specs Index (ages 8–12)

> **v1.1 update:** every app below now has **§15 Reevaluation & enhancements** (verdict, surface, wave, trimmed MVP, new features). See the [Project Reevaluation](../../03-project-reevaluation.md) and [Studio Platform Features](../../04-studio-platform-features.md).

> **Venture 2 of 5** · A COPPA-safe Socratic tutor and mastery worlds for ages 8–12, with no pay-to-win.
> **Status:** Discovery & Validation (specs only, no code) · **Date:** 29 September 2026
> **Parent docs:** [Venture vision](../../vision/02-questwise-tweens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [App template](../_TEMPLATE.md)
> **Confidence tags:** [V] verified · [V2] secondary · [M] memory · [E] estimate · [I] inference

---

## 1. The seven apps

| # | App | Ages | Signature feature(s) | Top competitors benchmarked | MVP tier |
|---|---|---|---|---|---|
| 1 | [Sage Tutor](01-sage-tutor.md) | 8–12 | Socratic Hint Ladder that never gives the final answer · Verified Math Gate (CAS checks every step) · "Try one like it" mastery check · screen-reader math | Gauth, Photomath, Brainly, Question.AI, Khanmigo, Gemini Guided Learning, Synthesis Tutor, Google Lens | **Year-1 MVP** (12 features) |
| 2 | [Math Realms](02-math-realms.md) | 8–12 | Mastery-gated regions · forgiving mastery (visible progress never drops) · earned-never-bought rewards | Prodigy, IXL, SplashLearn, Khan Academy, DreamBox, Zearn, Beast Academy | **Year-1 MVP** (12 features) |
| 3 | [Read Rangers](03-read-rangers.md) | 8–12 | Leveled passion library (human-curated, AI-leveled) · dyslexia reading layer · evidence quests | Epic!, Reading Eggspress, Raz-Kids, Amira, ReadTheory, Nessy, Learning Ally | Year 2 (11 features) |
| 4 | [Builder's Lab](04-builders-lab.md) | 9–12 | Socratic pair-programmer that never writes code · blocks ↔ Python dual view · build-log portfolio | Scratch, ScratchJr, Code.org, Minecraft Education, Tynker, codeSpark, Kodable, Hopscotch | Year 2–3 (11 features) |
| 5 | [AI Detectives](05-ai-detectives.md) | 9–12 | Weekly case files · bounded model sandbox · real-or-synthetic media lab | Be Internet Awesome/Interland, Common Sense, Hour of AI, Day of AI, BrainPOP, Nearpod, Experience AI | Year 2 (11 features); free classroom tier |
| 6 | [Wonder Lab](06-wonder-lab.md) | 8–12 | Guided off-screen investigations · phone sensor toolkit · science journal (ESA portfolio export) | Mystery Science, Generation Genius, KiwiCo, Tinybop, Seek, PictureThis, Sky Guide | Year 2–3 (10 features) |
| 7 | [Mission Control](07-mission-control.md) | 8–12 | Step Splitter (child-edited AI breakdown) · calm focus timer (nothing dies) · movement breaks | Joon, Goally, Brili, Tiimo, Forest, myHomework, Habitica, Greenlight | Year 2 (12 features) |

**Sequencing (from vision §9):** Year 1 = Sage Tutor + Math Realms MVP and ESA approval in 3 states. Year 2 = Read Rangers, Mission Control, AI Detectives. Year 3 = Builder's Lab and Wonder Lab at scale, ESSA Tier 2 study. All seven run no-code validation experiments now (see §11 of each spec).

## 2. Shared features (the Questwise Guild Hub layer)

| Shared feature | What it is | Used by | Spec notes |
|---|---|---|---|
| **Guild Hub** | One adult app/web portal for all 7 apps: plain-language weekly summary ("what I can do now"), settings, billing, privacy | All | Summaries, not transcripts; no parent notifications on the child's device; child can see what adults see |
| **Parent dashboard** | Weekly one-screen summary; per-app drill-down; co-play questions | All | Setup ≤5 min (Lumen P14) |
| **Educator dashboard** | Rosters, mastery heatmaps, assignments ("commissions"), exports | All; key for microschools/co-ops/classrooms | FERPA/SOPIPA DPA; class codes; no peer-visible names |
| **ESA invoicing** | Marketplace-ready invoices and vendor records (ClassWallet, Odyssey and state portals), curriculum descriptions, portfolio exports | All (bundled) | Per-state eligibility playbook; ESA purchase flows follow the fair-billing charter |
| **My Needs profile** | Portable Lumen profile (sensory, reading, input, pace, language, look, people), imported from Lanternling and exportable to Ascendly | All | All accommodations free (P12); learner-visible |
| **Sensory Dial** | Calm/Balanced/Lively, one tap from every screen; Balanced default, Calm when OS Reduce Motion is on | All | Mission Control and reading screens default Calm |
| **Sage policy engine** | Shared Socratic hint ladder, no-answer filter, CAS verifier, distress classifier | Sage, Math Realms, Read Rangers, Builder's Lab, AI Detectives, Mission Control (handoff) | One safety and evaluation suite for all AI surfaces |
| **Co-op play with invited friends only** | Friends/siblings/classmates linked by parent- or guide-approved invite codes; preset reactions and structured collaboration, no free-text chat, no public profiles, no stranger discovery | Math Realms co-op quests, Read Rangers book circles, Builder's Lab co-build, AI Detectives team cases, Wonder Lab science fair, Mission Control body-doubling, Sage study table | Both families' VPC required; revocable by either parent |
| **Multimodal answer tray** | Tap, voice, typing, drawing, AAC symbols, switch | All | Voice never the only mode; ASR WER measured by speaker group |
| **Accessible math renderer** | MathML + speech/braille (MathCAT-class) | Sage, Math Realms, Wonder Lab data | Built once, reused |
| **Evidence engine** | Mastery events, pre-registered studies, claims register | All | Evidence tier stated on every claim (P17) |
| **Fair-billing charter** | One family plan (≈$12/mo or $99/yr for up to 3 kids, all 7 apps), price before trial, 3-day reminder, one-tap cancel, summer pause, kids never see upsells | All | Free tier per app with full accessibility |

## 3. Features we reject, and why (venture-wide)

| Rejected feature | Seen in | Why we reject it |
|---|---|---|
| **Pay-to-win** (paid gear, pets, boosts) | Prodigy membership items; FTC complaint alleging "up to four times as many advertisements than math questions" [V NBC/EdWeek] | Vision principle 2 ("earned, never bought"); P15; creates the parent–child "constant battle" [V raw 03] |
| **Loot boxes and variable-ratio rewards** | Many kids' games [M] | Gambling-like; P9 bans variable-ratio rewards; state design codes and UK AADC anti-nudge standards |
| **Paid or premium currencies** | Gauth coin packs [V2 raw 02]; games | Children can't evaluate them; P15 |
| **Open chat, public profiles, stranger discovery** | Roblox (now requiring facial age checks to chat [V]); Scratch comments [M]; Habitica party chat [V2] | Vision principle 3; Epic Games' $275M COPPA penalty included default-on chat for kids [V raw 05] |
| **Ads of any kind (including ads for our own upgrades shown to kids)** | Brainly free tier; Prodigy in-game membership promotion | Apple Kids category and Google Families rules; COPPA 2025 separate consent for ads; P18 |
| **Answer-giving AI** (final answers, code written for the child, essays) | Gauth, Photomath, Question.AI, Brainly | Bastani et al.: −17% on unassisted exams without guardrails [V raw 05]; vision principle 1 ("think, don't copy"); answers only in adult-unlocked modes (Lumen §5.2) |
| **Companion personas / AI "friends"** | Character chatbots [M] | FTC 6(b) inquiry, CA SB 243; P18; "tutor, not friend" |
| **Emotion recognition** (face or voice affect inference) | Some edtech proctoring and "engagement" tools [M] | EU AI Act Art. 5 ban in education; P18; distress escalation uses self-report only |
| **Timers and speed scoring in learning** | Kahoot!, timed drills [V raw paper §6] | Excludes dyslexic, motor-impaired and screen-reader users; P11 |
| **Hearts, lives, energy, score drops** | Duolingo Energy; IXL SmartScore drops [V2] | P8; "rage-inducing" score anxiety |
| **Streak punishment and loss framing** (dying trees, sad pets) | Forest, Joon, Duolingo | P15 gentle progress with pause days |
| **Public leaderboards** | Prodigy, Kahoot! | Social comparison harms 8–12s (Lumen segment watch-out) |
| **Paywalls on children mid-play / daily limits** | Epic! "1 book a day"; PictureThis 1–2 free IDs [V2] | Upgrades only in the adult app; free tier never limits accessibility |
| **Voice-only or camera-only input** | Amira (accents, speech impediments [V2]); solver apps | P7; excludes blind, speech-impaired and AAC users |
| **Training AI on children's data by default** | Industry norm [M] | COPPA 2025 requires separate consent; default off; Edmodo algorithm-disgorgement precedent [V raw 05] |
| **Precise geolocation** | Nature and social apps | COPPA PI; UK AADC geolocation standard; Wonder Lab uses coarse, on-device only |
| **Health or efficacy claims beyond evidence** ("treats ADHD", "proven") | Brain-training cautionary tales (Lumosity $2M FTC) [V raw paper] | P17; FTC §5; FDA device boundary |
| **Surveillance transcripts by default** | Khanmigo surveillance fear [V2 raw 03] | Summaries, not transcripts; transcript mode is opt-in and disclosed to the child |

## 4. Venture-level metrics and gates

- **North-star (venture):** weekly mastered skills per active learner; each app's north-star feeds it (see §10 of each spec).
- **Shared guardrails:** frustration events per session; Sensory Comfort ≥4/5; parent trust score ≥8/10; zero billing complaints; zero answer leakage in audits; Lumen audit ≥22/24 for every prototype (target 23).
- **Inputs to Gate 2 (week 16, build / pivot / kill):** the Discovery Plan's Questwise assumptions (§8.2) map to these specs: **Q1** Socratic engagement → Sage E1 (≥70% of sessions completed, child rating ≥4/5); **Q2** mastery-gated fun → Math Realms E1 (persistence equal or better than points variant); **Q3** ESA/microschool buying → ≥3 states on a clear vendor path and ≥5 LOIs; **Q4** "no pay-to-win" as a purchase driver → ≥50% of surveyed parents rank it top-3.
- **Hard gates (Discovery Plan §6):** Lumen ≥22/24; no dependence on emotion recognition, companion personas, non-consented child-data training or dark-pattern monetization; ND advisory board sign-off for every Questwise app.

## 5. Research caveats

- The shared web-search budget ran out part-way through this research round (the session limit was reached). Several competitor details (Newsela, Beanstack, Raz-Kids, DragonBox, Swift Playgrounds, Interland specifics) rely on the existing raw research files or analyst memory and are tagged [M]. Verify them in Discovery WP1.
- Store-page fetches are blocked, as noted in the research paper §2.4. Download and rating figures come from search snippets, vendor pages and raw research files. Treat them as signals, not audited data.
- Several 2026 prices come from third-party price roundups (e.g., brighterly, nibble-app) [V2], so confirm them with vendor pages before external use.
- No quotes were invented. Quoted phrases come from sources listed in each spec or from the raw research files.

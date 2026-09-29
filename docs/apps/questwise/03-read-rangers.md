# Read Rangers: App Strategy & Product Specification

> **Venture:** Questwise · **App #:** 3/7 · **Ages:** 8–12 · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/02-questwise-tweens.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Questwise index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Passion-matched, leveled reading with read-aloud highlighting and Socratic "find the evidence" quests, built so dyslexic and reluctant readers are first-class Rangers. |
| **Primary user / buyer** | User: readers 8–12, including dyslexic, ADHD and ELL readers. Buyer: parent, ESA family, microschool, later library and classroom. |
| **Core job-to-be-done** | "When I have to read, I want texts about things I care about that I can actually get through, with help that doesn't make me feel slow, so I can understand, talk about it and want to read more." |
| **Category on the stores** | Education / Books (iOS Kids 9–11) · Google Play Education, Families |
| **Top competitors (by downloads / revenue)** | Epic! (12.5M+ iOS, 10M+ Play), Reading Eggspress, Raz-Kids, Amira, ReadTheory, Newsela, Nessy, Learning Ally, Beanstack |
| **Our wedge** | 1) Comprehension *and* access in one place: Epic has breadth, Nessy has structured literacy, Learning Ally has audio, but none combines leveled, passion-matched texts with Socratic discussion. 2) Voice is optional: fluency checks are opt-in, never the gate (vs. Amira complaints about kids with accents or speech differences). 3) Dignity: age-respectful themes and no "1 book a day" paywall on children. |
| **Business model** | In Questwise Family ($99/yr for 3 kids). Free tier: 3 texts/week with full accessibility. ESA, microschool and library licences. |
| **North-star metric** | Weekly "understood reads" per active learner (a text finished with ≥1 evidence-backed answer). |
| **MVP candidate?** | **Later** (Year 2 per vision §9); validation runs now. |

## 2. Problem & users

**Problem statement.** Comprehension and stamina drop at 8–12 as texts shift from "learning to read" to "reading to learn", and dyslexic and reluctant readers fall further behind.
- Epic!'s free tier is "1 book a day", and it is "notoriously difficult to cancel"; young kids can reach "terrifying" nonfiction [V raw 03].
- AI reading tutors are spreading, with friction. Amira reports 5M students in 4,000 districts [V2 tools-competition.org]. In San Francisco (Sept 2026) "kids say Amira can't understand them", with problems for students with accents or speech impediments, voice recording concerns and a 1,000+ signature petition [V2 SF Standard/NBC Bay Area].
- Dyslexia affects 5–20% depending on definition [V2 raw paper §3]. Families piece together Nessy (structured literacy, BDA Quality Mark), Learning Ally (human-narrated audiobooks, $135/yr, eligibility required) and Speechify [V2 raw 04; Learning Ally].
- Reading Eggspress (7–13) is reward-heavy and "kids game the rewards" [M raw 03].

**Personas**

| Persona | Snapshot | Needs | Pain today |
|---|---|---|---|
| **Priya, 11, dyslexic** | Grade 5 ideas, grade 3 decoding | Audio + text, time, voice or typed answers, grown-up topics | Babyish leveled books; timed quizzes |
| **Leo, 9, reluctant reader** | Loves soccer and sharks | Short, high-interest texts; visible stamina growth | Library shelves don't match interests |
| **Camila, 10, ELL** | Spanish at home | Bilingual glossary, read-aloud | English-only supports |
| **Nicole, parent** | Wants her kid reading, not scrolling | Honest progress, safe content | Epic content surprises; cancel friction |
| **Ms. Grant, co-op lead** | 20 kids, mixed levels | Discussion-ready texts, simple tracking | Hours of leveling and question writing |

**Needs & wants**

| Need | Evidence | Response |
|---|---|---|
| Access without stigma | Nessy "cartoonish for older kids" [V raw 04] | Age-respectful themes; level hidden from peers |
| Voice that works for all kids | Amira ASR complaints [V2] | Fluency reading is optional; tap/typed answers always count |
| Interesting texts | Leo persona; vision | Passion picker; human-curated texts in 30+ interest strands |
| Understanding, not just minutes | Parents distrust badges [V raw 03] | Evidence quests; "what I understood" card |
| Safe content | Epic "terrifying" nonfiction [V] | Human-reviewed, age-rated library; parent topic filters |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Epic!** | Epic Creations | 12.5M+ iOS; 10M+ Play [V2] | $11.99/mo or $79/yr; 4 profiles; free for educators [V2] | 4.7 iOS (500K+); 3.9 Play (92K) [V2] | 40,000+ books; Read-to-Me | 1 book/day free tier; hard to cancel; unsuitable content [V raw 03] | Read-to-Me highlighting; fixed layouts in picture books [M] | Apple/Play listings; raw 03 |
| **Reading Eggspress** | Blake eLearning | Homeschool favourite [V2 raw 03] | $9.99/mo or $69.99/yr; with math $99.99/yr [V2] | n/a | Structured comprehension 7–13; 30-day trial | Reward gaming [M] | Busy visuals [I] | readingeggspress.com |
| **Raz-Kids** | Learning A-Z | School staple [M] | ≈$132/yr per classroom (36 students) [V2] | n/a | Leveled e-books + quizzes | Classroom-only; dated [M] | Record-yourself; narration | spellingjoy; raz-kids.com |
| **Amira** | Amira Learning | 5M students, 4,000 districts [V2] | District-sold | n/a | Listens to oral reading; interventions (EN/ES) | Struggles with accents/speech differences; voice recording concerns; unproven efficacy claims per critics [V2] | Voice-first excludes some kids [I] | SF Standard; tools-competition.org |
| **ReadTheory** | ReadTheory | 14M+ teachers and students claimed [V2] | Free; premium tiers [M] | n/a | Free adaptive comprehension K–12 | Dry passages [M] | Basic | readtheory.org |
| **Nessy Reading & Spelling** | Nessy | BDA Quality Mark [V raw 04] | From $15.50/mo; home ed from $195.50/yr [V raw 04] | n/a | Structured literacy for dyslexia | Cartoonish for older kids [V raw 04] | Dyslexia-designed | raw 04 |
| **Learning Ally** | Learning Ally | 80k human-narrated books [V2 raw 03] | $135/yr (promo $99); eligibility required [V2] | n/a | Human narration, highlighting | School/eligibility dependent [V2] | Built for print disabilities | learningally.org |
| **Newsela** | Newsela | Large school footprint [M] | School-licensed [M] | n/a | Same article at 5 levels | Classroom-only [M] | Text-level toggle [M] | [M] |

**Feature matrix**

| Feature | Epic | Eggspress | Raz-Kids | Amira | Nessy | Learning Ally | Our decision |
|---|---|---|---|---|---|---|---|
| Large library | ✓ | ◐ | ✓ | ◐ | ✗ | ✓ | **Improve** (smaller, curated, passion-matched) |
| Leveled texts | ◐ | ✓ | ✓ | ✓ | ✓ | ✗ | **Parity** |
| Read-aloud with highlighting | ✓ | ◐ | ✓ | ◐ | ✓ | ✓ | **Parity** (human + TTS) |
| Comprehension questions | ◐ | ✓ | ✓ | ◐ | ◐ | ✗ | **Improve** (Socratic, evidence-based) |
| Oral reading fluency by ASR | ✗ | ✗ | ◐ (record) | ✓ | ✗ | ✗ | **Improve** (opt-in, never gating, on-device) |
| Structured literacy/phonics | ✗ | ◐ | ◐ | ◐ | ✓ | ✗ | **Partner/refer** in MVP; decoding bridge V2 |
| Dyslexia typography controls | ✗ | ✗ | ✗ | ✗ | ◐ | ◐ | **Differentiate** |
| Discussion with peers/family | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** (co-play cards, book circles with invited friends) |
| Reward-heavy economy | ◐ | ✓ | ◐ | ✗ | ✓ | ✗ | **Reject** variable-ratio; mastery badges only |
| Daily paywall on child | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | **Reject** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| RR-01 | **Passion picker** | Child picks 3–5 interests via icons + audio; refresh anytime | Leo persona; vision | Differentiate | MVP | Must |
| RR-02 | ⭐ **Leveled passion library** | 600 human-curated texts at launch (fiction + nonfiction, 30 strands), each available at 3 levels (AI-drafted, human-edited) | Newsela-style multilevel; vision "human-curated, AI-leveled" | Differentiate | MVP | Must |
| RR-03 | **Read-aloud with highlighting** | Word and sentence highlighting; speed 0.6–1.5×; human narration for flagship texts | Epic/Learning Ally parity; P5 | Parity | MVP | Must |
| RR-04 | ⭐ **Dyslexia reading layer** | BDA fonts, size, spacing, tint, line focus ruler, one-line mode, syllable dots toggle | BDA 2023; P6 | Lumen | MVP | Must |
| RR-05 | ⭐ **Evidence quests** | Socratic questions ("What would you do?", "Find the sentence that proves it"); child taps/highlights evidence, speaks or types reasoning | Comprehension focus; Sage policy | Differentiate | MVP | Must |
| RR-06 | **Tap-a-word glossary** | Kid-friendly definition, picture, audio; Spanish gloss | Camila persona | Improve | MVP | Must |
| RR-07 | **Adaptive level placement** | Short passage-based placement (no timer); moves levels on comprehension, not speed | ReadTheory parity | Parity | MVP | Must |
| RR-08 | **Stamina trail** | Minutes and pages build a visible trail; weekly goals; pause days; no streak loss | Gentle progress P15 | Lumen | MVP | Must |
| RR-09 | **Parent "what I understood" summary** | Texts read, evidence answers, one co-play question per text | Proof of learning | Parity | MVP | Must |
| RR-10 | **Content safety & topic filters** | Every text human-reviewed; parent can hide topics (e.g., predators, war) | Epic content complaint [V] | Improve | MVP | Must |
| RR-11 | **Sensory Dial + themes** | Calm default for reading; "Field Guide" and "Magazine" themes | P1, P13 | Lumen | MVP | Must |
| RR-12 | Opt-in fluency check | Child can record a 1-min read; on-device ASR gives words-correct estimate to parent; never gates | Amira parity minus its failure mode [V2] | Improve | V1 | Should |
| RR-13 | Book circles | Invited friends read the same text; post preset reactions and one evidence card; no free chat | Vision co-op | Differentiate | V1 | Should |
| RR-14 | Library card link | Holds/borrowing via Libby-style partner links; Beanstack-style challenge export | Library channel [I] | Improve | V2 | Could |
| RR-15 | Writing response | Short "write back" with Sage feedback on reasoning, not grammar policing | Reading-writing link | Improve | V1 | Should |
| RR-16 | Decoding bridge | Structured-literacy mini-lessons for gaps detected (or partner with Nessy) | Dyslexia need | Improve | V2 | Could |
| RR-17 | Guide assignments | Assign a text to a group with discussion prompts | Co-op lead persona | Parity | V1 | Should |

**MVP (when built) = RR-01 to RR-11 (11).** **Signature features:** RR-02 leveled passion library, RR-04 dyslexia reading layer, RR-05 evidence quests.

## 5. Core experience & key user flows

**Core loop:** open → today's pick (3 choices from passions) → read (listen/read/both) → 2–4 evidence quests → "what I understood" → natural end with co-play question.

**Flow 1: Onboarding**
1. Parent: VPC, child profile, topic filters (defaults on for sensitive topics), My Needs import.
2. Child: passion picker (icons + audio), theme, Dial, reading setup preview ("Which looks easiest to read?" shows 3 font/spacing samples).
3. 2 short placement passages with 3 questions each; first full read within 5 minutes.

**Flow 2: Core read**
1. Choose one of 3 texts. Length shown as minutes at your speed ("about 6 minutes").
2. Read mode: text, audio + highlight, or audio only (text still available).
3. Evidence quest: "Why did Mara go back to the reef? Tap the sentence that shows it." Wrong tap → "Hmm, that tells us *where*. Look for *why*." No score loss.
4. "What I understood" card; stamina trail grows; "Done, or one more?" with daily goal shown.

**Flow 3: Parent/guide**
1. Weekly summary: texts, minutes, evidence-answer rate, strands, and co-play questions to ask at dinner.
2. Guide: assign text, see class evidence answers (anonymised to peers).

**Flow 4: My Needs**
1. Reading layer (font, size, spacing, tint, ruler), TTS voice and speed, audio-first mode, answer modes, daily goal.

**Flow 5: Billing** as in the Questwise charter: parent-only, price first, one-tap cancel, free tier never limits accessibility tools.

**IA:** Child: Today, Library (by passion), My Trail, My Needs. Adult: Guild Hub.

**Session design:** Texts of 3–12 minutes; default 20-minute daily goal; transition warning before the last question; no autoplay of the next text.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial:** Calm (default for reading screens): no animation in text; soft page transitions. Balanced: small illustration motion on the Today screen only. Lively: animated trail and celebration, never inside reading.

**Input modes:** evidence answers by tap-highlight, voice, typing, drawing (for "draw what happened"), AAC/symbol choice (V1), switch scanning through sentences (V1).

**Targets:** sentences are tap targets with ≥48 dp line height in answer mode; no press-and-drag highlighting (tap start, tap end).

**Reading and typography (BDA 2023 defaults):** sans-serif (e.g., Lexend/Atkinson-style), 19 px default, 1.5 line height, 0.12 em letter spacing, off-white/cream background, 60–70 characters per line, no justified text, no italics for emphasis. **We do not claim any font "treats" dyslexia** (P6, P17).

**Screen readers:** texts are live HTML with semantic headings; highlight-sync works with VoiceOver speaking; evidence quests expose sentences as selectable list items; images have human-written alt text.

**Audio:** narration, effects and music separate; no music during reading; captions for all audio-only content (the text itself).

**No timers:** reading speed is never displayed to the child or ranked; fluency (V1) is parent-visible only and opt-in.

**Age-respectful:** texts at low levels with mature topics and photography ("Field Guide" theme), so a grade-6 reader at a grade-3 level doesn't see baby content.

**Lumen acceptance criteria**

| P | Criterion |
|---|---|
| P1 | Reading screens have 0 animations at any Dial level |
| P2 | Every audio cue has visual twin; captions = synced text |
| P3 | Reader layout identical across texts |
| P4 | Evidence selection by tap only |
| P5 | All instructions audio; reading-level dial per child |
| P6 | BDA defaults; WCAG 1.4.12 passes |
| P7 | ≥3 answer modes per quest |
| P8 | No score loss; "look again" hints |
| P9 | Designed end; no autoplay |
| P10 | Text stays visible while answering |
| P11 | No timers; fluency optional |
| P12 | Free, portable reading layer |
| P13 | Level independent of theme and topic maturity |
| P14 | Parent co-play questions per text |
| P15 | Gentle trail, pause days |
| P16 | Diverse authors/characters incl. disabled and ND characters; ND panel review |
| P17 | No "improves reading level by X" claims pre-study |
| P18 | No voice stored; fluency on-device |

**Target Lumen score:** 23/24.

## 7. AI specification & guardrails

- **AI does:** drafts leveled versions of human-selected source texts (human editor approves every version); drafts question sets (human-approved); Socratic follow-ups within a text-bounded scope (answers must cite the text); recommendation of next texts; TTS; optional on-device ASR for fluency.
- **AI does not:** generate unreviewed stories for children; answer questions outside the text; grade a child's pronunciation as a gate; store voice.
- **Pedagogy:** evidence-based comprehension (claim + evidence); vocabulary in context; gradual release (modelled → guided → independent quests); Socratic ladder shared with Sage (point to paragraph → point to sentence → model a similar question).
- **Safety:** no companion persona; AI disclosure in quests ("Questions made with help from a computer and checked by our editors"); distress escalation for self-report in typed/voice answers (shared classifier); no emotion recognition.
- **Hallucination controls:** retrieval restricted to the text; answer validation checks the child's highlighted sentence against editor-tagged evidence spans; editor sign-off log.
- **Evaluation:** leveling accuracy (editor rating ≥4/5, readability within target band 95%); question quality (teacher panel ≥4/5); ASR WER by group (8–9 vs 10–12, ELL accents, speech differences), with fluency feature withheld for any group whose WER gap >5 pts.
- **Cost [E]:** leveling and question drafting ≈$0.50 per text version plus ≈$25 editor time per text; per-learner runtime <$0.10/month.

## 8. Data, privacy & compliance

| Data | Why | Retention | Processing |
|---|---|---|---|
| Passions, level, reading layer | Personalisation | Life of account | Cloud |
| Reading events, answers | Summaries, level moves | 24 months | Cloud |
| Voice (fluency) | Opt-in estimate | Not stored; on-device | On-device |
| Typed "write back" | Feedback | 12 months | Cloud |

COPPA 2025 (voice is personal information; separate consent for fluency feature and for any AI training, both off by default); FERPA/SOPIPA for school/library contracts; state design codes; EU AI Act transparency. Apple Kids and Google Families. Content licensing: publisher/author rights tracked per text; accessible-format obligations noted.

## 9. Monetization & go-to-market

- **Benchmarks:** Epic $79/yr; Reading Eggspress $69.99/yr; Nessy from $186/yr; Learning Ally $135/yr; ReadTheory free.
- **Ours:** in the $99/yr Questwise Family; Read Rangers-only $6/mo test; free tier 3 texts/week, all access tools free forever.
- **Channels:** ESA (reading curriculum eligible [I]); FL FES-UA disability awards for dyslexic learners [M raw 05]; microschools; library partnerships (V2); dyslexia communities (paid ND co-designers, not affiliates).
- **ASO:** "reading app for dyslexia", "reading comprehension kids", "books for reluctant readers", "read aloud app kids". Accessibility Nutrition Label.
- **Content partnerships:** public-domain and licensed nonfiction; children's magazine publishers [I].

## 10. Success metrics

- **North-star:** weekly understood reads per active learner (target ≥3).
- **Inputs:** minutes read/week (≥60); evidence-answer success (≥65%); % texts chosen from passions; parent co-play question use.
- **Guardrails:** Sensory Comfort ≥4/5; dyslexic readers' completion rate within 10% of typical readers; zero unreviewed AI texts shipped; zero billing complaints.
- **Outcomes:** comprehension probes pre/post (3-week concierge), then a semester study with co-ops (Tier 3).
- **Retention:** D7 30%, D30 18% [E].

## 11. Validation plan

**Riskiest assumptions:**
1. Interest-matched texts improve stamina more than a curated library (vision).
2. Dyslexic readers prefer audio + text with our layer over audiobooks alone.
3. Human-edited AI leveling is fast and cheap enough at 600+ texts.
4. Parents pay when Epic and ReadTheory exist.

| # | Method | Sample | Success | Kill |
|---|---|---|---|---|
| E1 | 3-week A/B concierge with printed texts (passion-matched vs. curated) | n=30 | +20% minutes read; comprehension probe non-inferior | <5% difference → drop passion engine, keep curation |
| E2 | Figma reading-layer test with dyslexic kids (font/spacing/ruler) | 12 dyslexic + 8 typical readers | Preferred-setting comprehension ≥ default; Comfort ≥4/5 | No preference signal → simplify |
| E3 | Leveling cost spike (editor + AI drafts for 30 texts; manual tools only) | 2 editors | ≤45 min editor time per text for 3 levels; quality ≥4/5 | >90 min → fewer levels |
| E4 | Parent WTP interviews + landing page | 15 interviews; 1,500 visits | ≥5% waitlist | <2% |

Mapping: E1, E2 → WP4; E3 → WP4/WP5; E4 → WP2/WP5.

## 12. Build handoff

**Epic A: Library & leveling pipeline**
- **AC-A1:** Given a source text, When AI drafts 3 levels, Then none is publishable until an editor approves it and the readability score is in band.

**Epic B: Reader**
- **AC-B1:** Given read-aloud is on, When audio plays, Then word highlighting stays synced within 150 ms and respects the chosen font/spacing.
- **AC-B2:** Given VoiceOver is on, When the child reads, Then text is navigable by sentence and heading.

**Epic C: Evidence quests**
- **AC-C1:** Given a question with editor-tagged evidence, When the child taps a non-evidence sentence, Then a hint explains what that sentence tells us, and no progress is lost.

**Epic D: Placement and levels**
- **AC-D1:** Given 3 consecutive texts with ≥80% evidence success, When the next pick loads, Then one of the 3 choices is at the next level.

**Epic E: Safety & filters**
- **AC-E1:** Given a parent hides a topic, When the library loads, Then no text tagged with that topic appears in any list or search.

**NFRs:** text render <500 ms; offline download of 10 texts; iOS/Android/web; WCAG 2.2 AA; EN/ES glossary; licensing metadata enforced.

**QA focus:** AT matrix (VoiceOver + highlight sync, TalkBack, NVDA web, Switch sentence scanning); dyslexia settings matrix; AI cases (question answer keys vs evidence spans; no out-of-text answers); COPPA (voice never leaves device; consent off by default); billing (free tier limits never block accessibility).

**Platform dependencies:** Lumen reader component, My Needs, AI orchestration (leveling pipeline, editor console), privacy stack, evidence engine.

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Library too small vs. Epic's 40k | High | Medium | Position as "right text, not most texts"; library links V2 |
| Content licensing cost | Medium | High | Public domain + commissioned nonfiction; publisher rev-share |
| AI leveling errors (meaning drift) | Medium | High | Editor sign-off; fact check on nonfiction |
| Voice features alienate (Amira backlash) | Medium | Medium | Opt-in, on-device, never gating |
| Overlap with Wavelength ReadWave | Medium | Low | Shared reader; ReadWave for structured literacy, Read Rangers for comprehension |

**Open questions:** Should MVP include decoding support or refer out? Which publisher partners? Is human narration worth the cost beyond flagship texts?

## 14. Sources
- [V2] Epic! listings and pricing: https://apps.apple.com/us/app/epic-kids-books-reading/id719219382 · https://play.google.com/store/apps/details?id=com.getepic.Epic&hl=en_US · https://mwm.ai/apps/epic-kids-books-reading/719219382
- [V2] Reading Eggspress pricing: https://readingeggspress.com/pricing/
- [V2] Raz-Kids price: https://spellingjoy.com/best-apps/app/raz-kids
- [V2] Amira scale: https://tools-competition.org/winner/amira/ · https://amiralearning.com/amira-tutor
- [V2] Amira backlash (Sept 2026): https://sfstandard.com/pacific-standard-time/2026/09/25/pst-sf-amira-ai-in-schools/ · https://www.nbcbayarea.com/news/local/sfusd-ai-classroom-policy-parents-concerns/4146401/
- [V2] ReadTheory: https://readtheory.org/homepage/
- [V2] Learning Ally pricing and eligibility: https://learningally.org/solutions-for-home/home-school-resources-join
- [V via raw 04] Nessy pricing and BDA mark: research/raw/04-neurodivergent-and-inclusive-ux.md
- [V via raw 03] Epic complaints, Reading Eggs reward gaming: research/raw/03-forum-voice-of-customer.md
- [M] Newsela, Beanstack, Raz-Kids details not re-verified (search budget exhausted)

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep |
| **Ships in** | Questwise app (S2) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 73/100 [I] |
| **Consumes engines** | EN-04, EN-03 |
| **Studio features used** | SX-20, SX-14 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = RR-02, RR-03, RR-04, RR-05, RR-07.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| RR-E1 | **Reading continuum** | Uses one skill model with Sound Garden and ReadWave, so dyslexic readers keep their supports (SX-20). |
| RR-E2 | **Synced audiobook + text shelf** | An access route to grade-level content, alongside decoding practice rather than instead of it. |

### 15.3 New validation question
Interest-matched texts vs. a curated library: minutes read and comprehension probes, 3-week concierge.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 3 | 5 | 4 | 3 | 3 | 3 | 4 |

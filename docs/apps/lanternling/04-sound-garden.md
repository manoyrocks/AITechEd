# Sound Garden: App Strategy & Product Specification

> **Venture:** Lanternling · **App #:** 4/7 · **Ages:** 4–7 (pre-K to Grade 1; independent play with a weekly adult check-in) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/01-lanternling-early-years.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given; mostly search snippets) · [V2] secondary or vendor source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Learn to read the science-of-reading way: a garden that grows as your child masters sounds, blending and decodable books, with a patient AI read-along that listens, helps, and always lets them tap instead. |
| **Primary user / buyer** | Children 4–7 (user); parents (buyer; 30-second weekly check); pre-K/K teachers and reading specialists (B2B2C). |
| **Core job-to-be-done** | "When my child is ready to read, I want a trustworthy, step-by-step phonics path that listens to them read and shows me real progress, so they're reading before first grade without me guessing what to do." |
| **Category on the stores** | Apple: Kids › Ages 6–8 / 5 & Under (Education). Google Play: Families › Educational (Teacher Approved target). |
| **Top competitors** | Duolingo ABC (10M+ Play) · Reading Eggs (20M+ children claimed, 5M+ Play) · Teach Your Monster to Read (30M+ players) · Hooked on Phonics (4.5★, 18K) · HOMER (4.4★, 25K) · Read Along by Google (10M+) · Ello (AI read-along, $14.99/mo) · Starfall ($35/yr) |
| **Our wedge** | 1. **Structured literacy done right, stated plainly**: explicit scope and sequence, decodable books matched to taught patterns, no "guessing from pictures". 2. **Speech-inclusive read-along**: constrained, on-device checking of expected words (not open transcription), tap fallback on every item, tuned for child speech and measured by speaker group. 3. **Calm and honest**: no reward economies to game, calm celebrations, fair billing, and careful early-difficulty signals for parents (no diagnosis). |
| **Business model** | In the Lanternling Family plan (≈$9.99/mo or $69/yr, all 7 apps, 3 children). Free: first 3 garden beds (letter sounds for s-a-t-p-i-n, or equivalent) and 5 decodable books. B2B2C: pre-K/K classroom licences, libraries, ESA-eligible (post-validation). |
| **North-star metric** | **Weekly mastered skills per active child** (skills passing a mastery check), with a guardrail on frustration events. |
| **MVP candidate?** | **Yes**, one of the likely Year-1 trio; Year-3 ambition is an ESSA Tier 2 study. |

## 2. Problem & users

**Problem statement.**
- **Learning to read is the job to be done for parents of 4–7s** [V] ([Research paper §5.2](../../01-research-paper.md)). They want a science-of-reading scope and sequence and progress they can check in 30 seconds.
- **Quality is hard to judge.** Parents report kids "gaming" reward loops (Reading Eggs "eggs") instead of reading [M] ([raw 03](../../../research/raw/03-forum-voice-of-customer.md)); Duolingo ABC "stops at early reading" [M]; HOMER/Hooked on Phonics "science of reading alignment varies by product" [M].
- **Structured, explicit, cumulative phonics is well supported** (National Reading Panel). But the "multisensory" ingredient of Orton-Gillingham is **not** shown to add effect (Stevens et al. 2021, foundational ES 0.22, n.s.) [V] ([raw 04 §B2](../../../research/raw/04-neurodivergent-and-inclusive-ux.md)). We build on structured literacy and use multisensory channels for access, and we don't market them as the active ingredient.
- **AI read-along exists, but child ASR is hard.** Whisper reaches ~3% WER on adult read speech but ~25% on child voices in similar conditions [V] ([The Learning Agency](https://the-learning-agency.com/the-cutting-ed/article/how-speech-recognition-systems-struggle-with-childrens-voices/)); fine-tuning on child speech cut Whisper-small WER from 13.9% to 9.1% on MyST, a Grades 3–5 corpus, so 4–7-year-olds are harder still [V] ([Kid-Whisper, arXiv 2309.07927](https://arxiv.org/abs/2309.07927)). Read Along users report frustration when the app doesn't detect their speech, especially with accents [V] ([Learning Agency](https://the-learning-agency.com/the-cutting-ed/article/teaching-kids-to-read-with-speech-recognition-technology/)).
- **Dyslexia affects 5–20% of children** [V2]; early risk signals matter, but a consumer app must not diagnose (FDA/FTC boundary).

**Personas.**

| Persona | Snapshot | Needs |
|---|---|---|
| **Andre, 38, and Zoe (5), bilingual ES/EN** | Wants Zoe reading before first grade; distrusts reward-gaming. | Clear sequence; 30-second weekly check; Spanish-speaking accent handled well. |
| **Kai, 6, dyslexia risk (family history), with mum** | Avoids print; loves stories. | Slow pace; more practice at each step; no timers; dyslexia-friendly text; early-signal guidance for mum. |
| **Mateo, 5, speech sound disorder (lisp and /r/ gliding), seeing an SLP** | Reads fine in his head; ASR rejects him. | Tap alternative everywhere; the app never "marks him wrong" for articulation. |
| **Noor, 7, autistic, minimally speaking, uses AAC** | Decodes but doesn't read aloud. | Answer by tapping words/pictures or AAC; no voice-only tasks. |
| **Ms. Patel, pre-K lead** | 18 children, several dual-language learners. | Class view, printable decodables, family onboarding with a code. |

**Needs & wants.**

| Need | Evidence | Response |
|---|---|---|
| Trustworthy phonics sequence | Parent VoC [V]; NRP [M] | Published scope & sequence; mastery gating; decodables aligned |
| Real reading, not reward-gaming | Reading Eggs rewards gamed [M] | No currencies; garden grows from mastery only |
| Voice that works for all kids | Child WER gap [V]; Read Along frustration [V] | Expected-word verification; per-group WER gates; tap fallback |
| Support for struggling readers | Dyslexia prevalence [V2] | Slower paths, cumulative review, early-signal guidance |
| 30-second progress check | Research paper §5.2 [V] | One-screen weekly summary in plain language |
| Honest price | Category billing anger [V] | Fair billing; free starter beds |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Duolingo ABC** | Duolingo | 10M+ Play; 5M+ iOS [V] | Free, no ads/IAP [V] | 3.9 Play; 4.2 iOS [V] | 700+ bite-sized lessons; free; phonics + sight words [V] | Stops at early reading; gamified pressure [M] | Tracing and **drag-and-drop** tasks [V]; short lessons | [App Store](https://apps.apple.com/us/app/learn-to-read-duolingo-abc/id1440502568) · [Common Sense](https://www.commonsensemedia.org/app-reviews/duolingo-abc-learn-to-read) |
| **Reading Eggs** | Blake eLearning / 3P Learning | "20M+ children"; 5M+ Play; 12,000 schools [V2] | $9.99/mo or $69.99/yr (up to 4 kids); +math $99.99/yr; 30-day trial [V] | 4.7 iOS (7.3K); 4.2 Play [V] | Most-recommended paid option in homeschool roundups [V2] | Reward-heavy; kids game the eggs [M] | Busy, reward-rich [M] | [pricing](https://readingeggs.com/pricing/) · [App Store](https://apps.apple.com/us/app/reading-eggs-learn-to-read/id726696040) |
| **Teach Your Monster to Read** | Usborne Foundation | "30M+ players" [V] | App $8.99 one-time; web free; moving to subscription in 2026 [V] | n/a | Funny monsters; covers first 2 years of reading [V] | App paid vs. free web; later levels repetitive [M]; pricing-model change [V] | Playful, moderate sensory [M] | [pricing help](https://help.teachyourmonster.org/en/articles/10260379-app-pricing) · [update](https://www.teachyourmonster.org/monster-news/important-update-changes-to-teach-your-monster-to-read/) |
| **Hooked on Phonics** | HOP | Not published; 18.1K iOS ratings [V] | $12.99/mo; $79.99/yr web; $1 30-day trial promos [V] | 4.5 iOS [V] | Brand trust; songs; books + app bundles [V] | Price; SoR alignment varies [M] | Colourful, song-heavy [M] | [App Store](https://apps.apple.com/us/app/hooked-on-phonics-learning/id588868907) · [pricing](https://brighterly.com/blog/hooked-on-phonics-price/) |
| **HOMER** | Begin | Not published; 25K iOS ratings [V] | ≈$12.99/mo or $59.99–79.99/yr [V] | 4.4 iOS [V] | Personalised pathway; "74% increase in early reading scores" (vendor) [V2] | Subscription cost [V2] | Editors' Choice design [V2] | [App Store](https://apps.apple.com/us/app/homer-fun-learning-for-kids/id601437586) · [Begin](https://www.beginlearning.com/homer/pdp) |
| **Read Along by Google** | Google | 10M+ Play (~22M lifetime) [V] | Free, offline, no ads [V] | ~4.4–4.6 [E] | Reading buddy listens and helps in real time; many languages [V] | Speech recognition errors for young voices/accents [V] | Voice-first; offline; low bandwidth [V] | [raw 01](../../../research/raw/01-google-play-top30.md) · [Learning Agency](https://the-learning-agency.com/the-cutting-ed/article/teaching-kids-to-read-with-speech-recognition-technology/) |
| **Ello** | Ello Technology | Fortune "Change the World" #5; $15M Series A [V] | $14.99/mo or $139/yr; $0.99/mo low-income; paperback plan $39.99/mo [V] | n/a [M] | AI coach listens to reading; 800+ decodable books, K–3 SoR sequence [V] | Price [I] | Voice-dependent [I] | [Ello](https://www.ello.com/digital-product-page) · [Yahoo](https://finance.yahoo.com/news/ello-launches-storytime-version-ai-150500669.html) |
| **Starfall** | Starfall Education | Long-running free/low-cost site [V2] | $35/yr home membership [V] | n/a | Classic phonics sequence; cheap [V2] | Dated; most content behind membership [M] | Simple, low sensory [M] | [membership](https://help.starfall.com/help/help-me-choose-a-membership) |

*Also relevant:* **Amira** (school-sold AI tutor with ORF assessment and dyslexia screening; ESSA Level II study reports ES +0.64 on WRMT [V2]) ([Amira research](https://amiralearning.com/research)); **Endless Reader** (no fail states, word packs $5.99, animation may over-stimulate) [V via raw 04]; **Lingokids** (broad, not SoR-focused; high-stimulation) [V].

**Takeaways [I].** Free options (Duolingo ABC, Read Along, Khan Kids) set a high bar for price. Paid leaders (Reading Eggs, HOP, HOMER) sell trust and breadth, not listening. Ello and Amira prove **listening to the child read** is the premium feature, but both are voice-dependent. **No one pairs SoR rigour, speech-inclusive listening with full tap parity, and a calm, reward-free design.**

**Feature matrix.**

| Feature | Duo ABC | Reading Eggs | TYMTR | HOP | HOMER | Read Along | Ello | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Explicit phonics scope & sequence | ✓ | ✓ | ✓ | ✓ | partial | partial | ✓ | **Parity**, published openly |
| Decodable books matched to lessons | partial | partial | ✗ | ✓ | partial | ✗ | ✓ | **Parity** |
| Child reads aloud; AI listens | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | **Improve**: expected-word checking, on-device, group-level WER gates |
| Tap alternative to every speaking task | n/a | n/a | n/a | n/a | n/a | ✗ | ✗ [I] | **Differentiate** |
| Phonemic awareness (oral) activities | partial | ✓ | partial | ✓ | ✓ | ✗ | partial | **Parity** |
| Mastery gating + cumulative review | partial | ✓ | partial | ✓ | ✓ | ✗ | ✓ | **Parity** |
| Reward currency (eggs, coins, gems) | ✓ (stars) | ✓ | ✓ | partial | partial | ✓ (stars) | partial | **Reject** (gaming; Lumen P15) |
| Drag-only tasks | ✓ | ✓ | ✓ | partial | ✓ | ✗ | ✗ | **Reject**: tap-then-tap alternative |
| Timers / speed scoring | ✗ | partial | partial | ✗ | ✗ | ✗ | ✗ | **Reject** in the learning loop (fluency is measured untimed at MVP) |
| Parent progress report | ✓ | ✓ | partial | ✓ | ✓ | partial | ✓ | **Improve**: 30-second plain-language summary |
| Early difficulty signals | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | partial | **Differentiate** (careful, no diagnosis) |
| Dyslexia-friendly type & spacing | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ [M] | **Differentiate** |
| Offline | partial | partial | ✓ | partial | partial | ✓ | partial | **Parity** |
| Spanish-accent robustness | ? | n/a | n/a | n/a | n/a | partial | ? | **Differentiate** (measured) |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| SG-01 | **Garden Path (scope & sequence)** ★ | ~120 skills in 9 "beds": phonological awareness → letter-sound (by frequency and confusability) → CVC blending → digraphs → blends → long vowels (V1) → sight/"heart" words taught as decodable-plus-irregular. Published to parents. | NRP / SoR [M]; parent trust need [V] | Parity (done openly) | MVP (beds 1–5) | Must |
| SG-02 | **Explicit lesson micro-loop** | I do (model) → We do (guided) → You do (practice) → Check; 5–8 min per skill. | Explicit instruction evidence [M] | Parity | MVP | Must |
| SG-03 | **Read-Along Listener** ★ | Child reads a word/sentence aloud; on-device model checks it against the **expected text** (keyword-spotting/forced alignment, not open transcription); gentle help ladder: wait → point to the tricky letter → model the sound → "Let's sound it out together: /m/ /a/ /p/" → offer tap. | Ello/Read Along demand [V]; child WER gap [V] | Improve | MVP | Must |
| SG-04 | **Tap parity on every item** ★ | Every speaking task has a tap/AAC version (e.g., choose which picture matches the word; tap sounds in order; tap-to-read-word shows the child pointing). Mastery can be reached fully by tap. | Lumen P7; Mateo/Noor personas | Differentiate | MVP | Must |
| SG-05 | **Decodable Books** | 60 books at MVP [E] matched to beds 1–5 (≥95% decodable given taught patterns); read-to-me for non-target words; child-read mode with Listener. | Ello's 800 decodables [V]; HOP [V] | Parity | MVP | Must |
| SG-06 | **Mastery gating + spaced review** | Advance at ≥85% accuracy across two separate days [E]; review due items resurfaced; never reset progress. | Mastery learning [M]; Lumen P8 | Parity | MVP | Must |
| SG-07 | **Garden (mastery visual)** | Each mastered skill plants/grows a flower; nothing wilts; no currency. | Lumen P15; reward-gaming complaints [M] | Lumen | MVP | Must |
| SG-08 | **Weekly 30-second summary** | "Zoe learned /sh/ and /ch/, read 4 books, is practising blending 4-letter words. Try: find 'sh' on signs this week." | Research paper §5.2 [V] | Improve | MVP | Must |
| SG-09 | **Phonemic awareness by ear** | Oral games: rhyme, first sound, blend and segment with picture choices, no print. | Phonological awareness predicts decoding [M] | Parity | MVP | Must |
| SG-10 | **Reading-level dial & dyslexia settings** | Adult sets pace (standard / gentle: more practice per skill), letter spacing, font, tint, line spacing. | BDA; Kai persona | Differentiate | MVP | Must |
| SG-11 | **Early Signals (parent-only)** | If a child shows persistent difficulty on phonemic-awareness and letter-sound items across ≥3 weeks despite gentle pacing, parent sees: "Some children need more time or a different kind of help with sounds. It may be worth talking with Zoe's teacher or pediatrician. Here's what to ask." No labels, no risk scores. | Dyslexia prevalence [V2]; Amira screening shows demand [V2]; FDA boundary | Differentiate | MVP (copy + rules) | Should |
| SG-12 | **Letter formation (tap-trace)** | Letter formation by tapping sequential dots (no free-drag required); optional finger/stylus trace. | Handwriting-reading link [M]; Lumen P4 | Improve | V1 | Should |
| SG-13 | **Teacher / class view** | Class code, skill heatmap, printable decodables, family invitations; FERPA-ready. | Ms. Patel persona; Reading Eggs 12K schools [V2] | Parity | V1 | Should |
| SG-14 | **Spanish-speaking-child support** | Contrastive tips for EN sounds absent in ES (/v/ vs /b/, short vowels); ASR model evaluated on ES-accented child English. | Andre persona; bilingual segment | Differentiate | MVP (eval) / V1 (tips) | Should |
| SG-15 | **Beds 6–9 & fluency** | Long vowels, r-controlled, multisyllable; untimed fluency measure (words read correctly per passage; no stopwatch shown). | Complete K–1 path | Parity | V1 | Must (V1) |
| SG-16 | **Spanish literacy path** | Separate SoR sequence for Spanish (syllable-based). | Two Words synergy | Differentiate | V2 | Could |
| SG-17 | **SLP/teacher share** | Consented progress export for IEP/RTI meetings. | Wavelength synergy | Differentiate | V2 | Could |

★ **Signature features:** Read-Along Listener (SG-03) with Tap parity (SG-04), Garden Path (SG-01). **MVP = SG-01 to SG-11 (11 features) + SG-14 evaluation.**

## 5. Core experience & key user flows

**Core loop.** Open → Now/Next/Done strip ("Sound → Blend → Book → Done") → one lesson (5–8 min) → one decodable book (3–5 min) → garden grows if mastered → natural end with a real-world "sound hunt" → closed.

**Flow 1: Onboarding (≤5 min).**
1. Parent: price & privacy; child's age, languages, known letters (tap letters they know, or "not sure").
2. Microphone choice: "Sound Garden can listen as [child] reads, on this device only. Or use tap only." (Tap-only is equally complete.)
3. 3-minute friendly placement game for the child (by ear and by tap; no failure screens).
4. Parent sees the starting bed and the published path.
5. Child starts their first lesson.

**Flow 2: Core session.**
1. Strip shows 3 steps. Lesson: "This is /sh/. Like a finger on your lips: shhh." (model)
2. We do: "Let's read 'ship' together." Child taps each sound or says it.
3. You do: 5 items (mix of read-aloud and tap). Listener hears "sip" for "ship" → waits 3 s → highlights "sh" → "This pair says /sh/. Try again?" → second miss → models it → offers tap. Never "wrong!".
4. Book: *Shep the Fish* (decodable). Child reads; non-target words read-to-me.
5. Garden: a new flower if skill mastered, otherwise "More practice tomorrow."
6. End: "All done! Hunt for 'sh' in the bath tonight." App shows a calm goodbye; no next lesson autoplay.

**Flow 3: Parent view.** Weekly summary card (30 s). Drill-down: skills mastered, current bed, books read, a tip; Early Signals only if rules trigger, never pushed to the child's device.

**Flow 4: My Needs.** Sensory Dial; input (voice / tap / AAC / switch); pace (standard/gentle); typography; wait time for voice (3–10 s); session length (10/15/20 min); captions.

**Flow 5: Billing.** Family Hub standard; free beds 1–3 fully usable, including Listener.

**Flow 6: Teacher (V1).** Class code → family invites → class skill heatmap → printable decodables.

**Information architecture.** Child: Garden (home) → Today's path (strip) → Lesson / Book / Done. Parent (gated): Week · Path · Settings · Family. Fixed "Help" (replay instruction) and "Tap instead" buttons on every task.

**Session design.** Default 15 min (range 10–20) with transition warning at T-2 min ("One more book, then we're done"); max 1 new skill per session; designed ending with real-world activity.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial defaults.** **Calm** for 4–5; **Balanced** for 6–7 (Lumen segment default), both parent-changeable.

| Level | Sound Garden behaviour |
|---|---|
| Calm | Static garden; single soft chime + checkmark for correct; narration only; no background music |
| Balanced | Flower grows with a 1-s animation; gentle effects; music off in tasks |
| Lively | Longer bloom animation (skippable), light music between activities only, no flashing |

**Input modes per task.**

| Task | Tap | Voice | AAC/symbols | Switch | Keyboard |
|---|---|---|---|---|---|
| Sound ID / phonemic awareness | ✓ picture choice | ✓ | ✓ | ✓ (scan 2–4 choices) | ✓ |
| Word reading | ✓ (select picture; tap each sound then "read" button that plays the child's selection) | ✓ Listener | ✓ (word bank) | ✓ | ✓ |
| Book reading | ✓ (tap word to hear; comprehension picture choices) | ✓ Listener | ✓ | ✓ | ✓ |
| Letter formation (V1) | ✓ tap dots | n/a | n/a | ✓ step mode | ✓ |

**Targets & gestures.** ≥2 cm targets, ≥0.5 cm spacing; letter tiles ≥2.2 cm; every drag (e.g., building words from tiles) has tap-tile → tap-slot; no timers; no double-tap.

**Reading & typography.** Default: sans-serif with single-storey 'a' and distinct b/d/p/q shapes, 24–32 pt for target words, letter spacing +12%, line height 1.5, off-white background; tint options; no justified text; no italics. We **do not** claim a dyslexia font "treats" dyslexia (evidence does not support it) [M].

**Audio.** Narration, sound models, effects on separate sliders; all sounds modelled by human voice actors (clear phoneme articulation) with captions showing the grapheme; visual + haptic twin for feedback.

**Speech inclusion.** Voice wait-time default 6 s, adjustable; "I didn't catch that. Want to tap instead?" after two misses (never blame); articulation differences (e.g., /r/ gliding, lisp) must not cause failure on decoding items; per-speaker adaptation stays on device.

**Age-respectful themes.** Two looks: "Garden" (illustrated) and "Notebook" (plain, for 6–7s and older struggling readers who find gardens babyish). Content independent of theme.

**Lumen principles.**

| P# | Acceptance criterion |
|---|---|
| P1 | Reduce Motion → no bloom animation; Dial 1 tap from header |
| P2 | Every sound shown as a grapheme caption; feedback has visual + haptic twin |
| P3 | Same lesson structure (I do / We do / You do / Check) every time; strip always visible |
| P4 | All tasks completable by single taps; targets ≥2 cm |
| P5 | Instructions spoken; ≤8 words on screen for instructions |
| P6 | Typography defaults above; spacing override works |
| P7 | Every task ≥2 input modes; Listener never the only path |
| P8 | No "wrong" sounds or red Xs; undo; "skip for now" |
| P9 | Session ends by design; no next-lesson autoplay |
| P10 | Picture login for child; parent gate |
| P11 | No timers; voice wait adjustable to 10 s |
| P12 | Pace, input, typography from My Needs; free |
| P13 | Two themes |
| P14 | First lesson ≤5 min |
| P15 | Garden = mastery; no currency, streak loss or leaderboards |
| P16 | Characters include AAC users, glasses, hearing aids; no "fix" language |
| P17 | "Built on structured literacy" (not "proven to…") until our own study |
| P18 | Child audio processed on-device; not stored by default |

**Target Lumen audit score:** 23/24.

## 7. AI specification & guardrails

**What AI does.**
- **Listener (ASR):** on-device, child-tuned acoustic model used in **constrained mode**: it scores whether the expected word/sentence was read (and where it diverged) rather than transcribing freely. This is a much easier task than open ASR and reduces privacy exposure [I]. Word-level confidence thresholds are set **per speaker group** so that false "try again" prompts stay under target.
- **Adaptive sequencing:** Bayesian knowledge tracing (or similar) per skill; chooses review items and pace; human-authored item bank only.
- **TTS:** not used for phoneme models (human recordings); may be used for non-target words in books with a consistent, child-friendly voice.

**What AI does not do.** No generative text for books at MVP (decodables are human-written and checked by a decodability tool). No chatbot or tutor persona; the "voice" is a narrator, not a friend. No emotion detection from voice. No diagnosis; Early Signals are rule-based, reviewed by a reading specialist, and conservative.

**Pedagogical policy.** Explicit, systematic phonics; decodable-first reading; "sound it out" hint ladder (never "look at the picture and guess"); mastery gating; cumulative review; untimed.

**Safety & fairness.**
- **WER/accuracy gates by speaker group before launch:** age (4–5, 6–7), sex, regional US accents, Spanish-accented English, AAVE speakers, children with speech sound disorders. Target: false-reject rate (child read correctly, app said try again) ≤8% per group and within 3 points of the best group [E]; false-accept ≤10% [E]. A group failing the gate gets tap-first defaults and a notice to parents.
- Frustration guardrail: ≤1 frustration event per session (two consecutive false rejects, or a child-initiated quit mid-task) [from Discovery L3].
- Early Signals wording reviewed by a reading specialist and an ND advisory member; no push to child devices; "talk to your teacher or pediatrician" plus resource links.

**Evaluation plan.** Offline: consented child-speech benchmark (research-only data, n≈150 children across groups [E]); per-group false-reject/accept. Wizard-of-Oz: human "listener" vs. model decisions compared. Red-team: background TV, siblings, whispered reading, AAC speech output (should route to AAC mode, not be scored). Human review sampling: 1% of anonymised on-device decision logs (counts only) weekly.

**Cost and latency [E].** On-device inference: zero marginal cloud cost; decision latency ≤400 ms after end of utterance; model size ≤80 MB. Cloud only for sync of mastery data.

## 8. Data, privacy & compliance

**Data inventory.**

| Data | Purpose | Processing | Retention |
|---|---|---|---|
| Child profile (first name/nickname, age, languages) | Personalisation | Cloud, encrypted | Life of account |
| Skill mastery, item responses (correct/incorrect, input mode) | Sequencing, summary | Cloud | Life of account; export |
| Child voice audio | Listener decisions | **On-device, transient** | Not stored by default |
| Optional research voice samples | Model improvement | Cloud, separate store | Only with separate verifiable parental consent; 24 months max; deletable |
| Early Signals flags | Parent guidance | Cloud, parent-only | Cleared when resolved or on request |

**Regimes.** COPPA 2025 (child voice = PI; biometric expansion; separate consent for any model training; retention schedule) [V via raw 04]. FERPA/SOPIPA and state student-privacy laws for the classroom tier (DPA, no ads, no profiling beyond education). UK AADC; state AADCs. EU AI Act: education AI that evaluates learning outcomes may be high-risk (Annex III) from 2 Dec 2027; we design for human oversight, logging and accuracy documentation now. FDA: no screening/diagnosis claim; Early Signals is general guidance. FTC §5: evidence-tier claims only.

**Consent.** Parent consent; separate mic consent (default tap-only is fine); separate research-data consent (off by default, paid participation only in studies).

**Store policy.** Apple Kids category (no third-party analytics; parental gate); Google Families + Teacher Approved submission.

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Free | $0 | Beds 1–3, 5 decodables, Listener, all accessibility |
| Family plan | ≈$9.99/mo or $69/yr (7 apps, 3 kids) | Full path, all decodables, Early Signals guidance, summaries |
| Classroom | $3–5 per student/yr [E] or $150–250 per classroom [E] | Teacher view, printables, rostering (V1) |

Benchmarks: Reading Eggs $69.99/yr (4 kids), HOMER $59.99–79.99/yr, HOP $79.99/yr, Ello $139/yr, Starfall $35/yr, Duolingo ABC/Read Along free [V]. Our bundle matches Reading Eggs on price while including 6 other apps; standalone Sound Garden value is positioned between HOMER and Ello.

**Channels.** Science-of-reading creators and teachers; pre-K/K classrooms (home-school link); libraries; ESA marketplaces after validation; dyslexia parent communities (with careful claims).

**ASO.** "learn to read phonics app", "science of reading app", "decodable books app", "reading app that listens", "dyslexia friendly reading app kids". Accessibility Nutrition Label: VoiceOver, Voice Control, Larger Text, Reduced Motion, Captions, Sufficient Contrast, Differentiate Without Color.

**Launch.** US first (EN, with Spanish-accent support); UK V1 (phonics sequence adapted to UK "Letters and Sounds"-style expectations) [I].

## 10. Success metrics
- **North-star:** weekly mastered skills per active child (target 2–3 [E]).
- **Inputs:** sessions/week (3–5 target); % tasks answered via tap vs. voice (monitored, not optimised); books read per week; review completion.
- **Guardrails:** frustration events ≤1/session; false-reject rate per group ≤8%; Sensory Comfort ≥4/5; zero billing complaints; parents' "I understand my child's progress" ≥4.5/5.
- **Learning outcomes:** pre/post letter-sound fluency, phonemic awareness (e.g., segmenting) and decoding probes in a 10-week pilot; evidence tier E4 → E3 (pilot, Year 1) → E2 (quasi-experimental, Year 2) → ESSA Tier 2 (Year 3).
- **Retention:** D30 35%, M3 25%; school-year seasonality expected (summer pause option) [E].

## 11. Validation plan

**Riskiest assumptions.**
1. Child ASR is accurate enough (or failure handling kind enough) that children don't get frustrated (L3).
2. Parents trust and pay for a calm, reward-free phonics app vs. free Duolingo ABC/Read Along.
3. Children 4–7 stay motivated by mastery visuals without currencies.
4. Early Signals help rather than alarm parents.

| # | Method | Sample | Success | Kill / rethink |
|---|---|---|---|---|
| E1 | **ASR feasibility spike**: constrained expected-word checking on consented child read-speech | ~150 children, 6+ speaker groups, research consent | False-reject ≤8% per group and ≤3-pt spread | Any group >12% → tap-first for that group; >2 groups → Listener as V1, not MVP |
| E2 | **Wizard-of-Oz read-along**: human listener behind a Figma prototype applying the hint ladder | 24 children (incl. ≥4 speech sound disorder, ≥2 AAC, ≥6 bilingual) | ≤1 frustration event per session; Sensory Comfort ≥4/5 | >2 events avg → redesign ladder |
| E3 | **Paper decodables + garden** motivation test in pre-K/K class | 2 classrooms, 3 weeks | Voluntary return to "garden" activity ≥ comparable sticker chart | Clear loss → add child-chosen garden decorations (still no currency) |
| E4 | **Early Signals copy test** | n≈200 parents | "Helpful" ≥4/5; "alarming" ≤10% | Else rewrite / remove from MVP |
| E5 | **Price test** (Family plan vs. standalone $59/yr) | Landing page + survey | ≥30% choose paid; planned price in range | <15% → larger free tier, B2B focus |

**Mapping.** E1 → WP4 feasibility spike (L3); E2 → WP4 Wizard-of-Oz + sensory A/B + accessibility round; E3 → WP4 paper prototypes; E4 → WP2 survey; E5 → WP5 (L1).

## 12. Build handoff

**Epic SG-E1: Lesson engine.**
- **Given** a skill is new, **when** the lesson starts, **then** the sequence is Model → Guided → Practice → Check, and the strip shows the current step.
- **Given** a child answers 2 practice items incorrectly in a row, **then** the next item is a guided item, and no negative sound or red colour appears.

**Epic SG-E2: Listener.**
- **Given** mic consent is off, **then** no microphone permission is requested and every item renders in tap mode.
- **Given** the child reads "sip" for "ship", **when** the model detects divergence at "sh", **then** the app waits 3 s, highlights "sh", and offers the hint; after the second miss it offers "Tap instead?".
- **Given** any session, **then** no audio is written to disk or network unless research consent is on (verified by instrumentation).
- **Given** an AAC device speaks the word, **then** the app offers switching to AAC mode rather than scoring the synthetic voice.

**Epic SG-E3: Decodables.**
- **Given** a book is assigned, **then** ≥95% of words are decodable from mastered skills + taught heart words (validated by the decodability checker at content build time).

**Epic SG-E4: Mastery & garden.**
- **Given** ≥85% accuracy across two separate days, **then** the skill is marked mastered and one flower grows (animation per Sensory Dial).
- **Given** any inactivity, **then** nothing in the garden wilts or disappears.

**Epic SG-E5: Parent summary & Early Signals.**
- **Given** a week ends, **then** the summary is one screen, ≤60 words, with one real-world tip.
- **Given** Early Signals rules trigger, **then** the parent (only) sees the approved copy with resources; the child device shows nothing.

**Non-functional.** On-device ASR on iPhone 11+/mid-range Android 2020+; Listener latency ≤400 ms; full offline for downloaded beds; iOS/iPadOS, Android, web (parent/teacher views); WCAG 2.2 AA; EN (US) at MVP; encrypted sync; zero third-party SDKs.

**QA focus.** AT matrix (VoiceOver/TalkBack on parent + child tasks, Switch scanning of choices, Voice Control, Dynamic Type XXL in parent views, AAC path). Sensory A/B (Calm vs. Lively). AI safety: per-group false-reject suites, noisy-room tests, sibling interference, AAC speech. COPPA: mic-off path, no audio persistence, research consent separation, deletion. Billing: free beds fully functional; no mid-lesson paywall (paywall only between beds, in the parent area).

**Platform dependencies.** Lumen (answer tray, strip, Dial); My Needs (input, pace, typography, wait time); AI orchestration (on-device model delivery, per-group thresholds); privacy stack (consent ledger, research data vault); evidence engine (probes, pilot pre-registration).

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| ASR frustrates some groups | H | H | Constrained checking; per-group gates; tap parity; kill criteria |
| Free competitors "good enough" | H | M | Rigour + listening + calm; bundle; classroom channel |
| Early Signals cause anxiety or liability | M | H | Conservative rules; specialist-reviewed copy; no labels; legal review |
| Content cost (decodables) | M | M | Decodability tooling; human writers; reuse across Story Lantern |
| Motivation without currency | M | M | E3 test; child-chosen garden decor; celebration via Dial |
| Annex III obligations for AI assessment (EU) | M | M | Design human oversight and logs now; EU launch later |

**Open questions.** UK vs. US sequence differences (one path with regional variants?). Should the Listener run on older tablets common in classrooms? Is a Spanish literacy path higher priority than Beds 6–9? How to position vs. Ello's AI coach (price vs. inclusivity)?

## 14. Sources
- [V] Child ASR WER gap: https://the-learning-agency.com/the-cutting-ed/article/how-speech-recognition-systems-struggle-with-childrens-voices/ · Kid-Whisper: https://arxiv.org/abs/2309.07927
- [V] Read Along & speech recognition: https://the-learning-agency.com/the-cutting-ed/article/teaching-kids-to-read-with-speech-recognition-technology/ · Read Along Play data: [raw 01](../../../research/raw/01-google-play-top30.md)
- [V] Duolingo ABC: https://apps.apple.com/us/app/learn-to-read-duolingo-abc/id1440502568 · https://www.commonsensemedia.org/app-reviews/duolingo-abc-learn-to-read
- [V] Reading Eggs: https://readingeggs.com/pricing/ · https://apps.apple.com/us/app/reading-eggs-learn-to-read/id726696040
- [V] Teach Your Monster to Read: https://help.teachyourmonster.org/en/articles/10260379-app-pricing · https://www.teachyourmonster.org/monster-news/important-update-changes-to-teach-your-monster-to-read/
- [V] Hooked on Phonics: https://apps.apple.com/us/app/hooked-on-phonics-learning/id588868907 · https://brighterly.com/blog/hooked-on-phonics-price/
- [V/V2] HOMER: https://apps.apple.com/us/app/homer-fun-learning-for-kids/id601437586 · https://www.beginlearning.com/homer/pdp
- [V] Ello: https://www.ello.com/digital-product-page · https://finance.yahoo.com/news/ello-launches-storytime-version-ai-150500669.html
- [V2] Amira research / ESSA: https://amiralearning.com/research · https://www.evidenceforessa.org/program/amira/
- [V] Starfall membership: https://help.starfall.com/help/help-me-choose-a-membership
- [V] Orton-Gillingham meta-analysis and dyslexia-font evidence: [raw 04 §B2](../../../research/raw/04-neurodivergent-and-inclusive-ux.md)
- [M] National Reading Panel; phonological awareness as a predictor; Bayesian knowledge tracing

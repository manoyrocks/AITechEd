# Story Lantern: App Strategy & Product Specification

> **Venture:** Lanternling · **App #:** 3/7 · **Ages:** 2–7 (read with an adult; audio-only bedtime mode) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/01-lanternling-early-years.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given; mostly search snippets) · [V2] secondary or vendor source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Bedtime reading that makes every grown-up a great storyteller: read-aloud books with gentle "pause and ask" prompts, human-reviewed stories starring your child, and a screen-off Lantern Mode for lights-out. |
| **Primary user / buyer** | Parents and grandparents reading with children aged 2–7; the child is a co-user. Buyer: parents; gift buyer: grandparents. |
| **Core job-to-be-done** | "When it's bedtime and I'm tired, I want a story we both enjoy that helps my child's language and ends calmly, so we connect and they fall asleep without a screen fight." |
| **Category on the stores** | Apple: Kids › Ages 6–8 and 5 & Under (Books / Education). Google Play: Families › Books & Reference / Educational. |
| **Top competitors** | Epic (1.2–2M US iOS/yr) · Tonies (€630M revenue 2025, hardware + app) · Yoto (£94.8M revenue 2024) · Moshi Kids (4.7★ from ~70K ratings) · Readmio (2.2M downloads) · Vooks (4.5★, 9.8K) · Oscar AI stories (100K+) · Amazon Kids+ |
| **Our wedge** | 1. **Dialogic reading built in**: prompts for the adult, based on the approach with the strongest vocabulary evidence for 2–3-year-olds. 2. **Personalised, but human-reviewed**: stories starring the child from human-written templates, reviewed before delivery. Parents distrust AI-authored story text. 3. **Screen-off bedtime**: Lantern Mode is audio-only with a dim, warm, self-ending experience; the Yoto/Tonies benefit without hardware. |
| **Business model** | Free: 1 library book/day plus unlimited re-reads of favourites, and Lantern Mode for those books. Family plan (≈$9.99/mo or $69/yr, all 7 apps): full library, personalised stories, family photos, grandparent recordings. B2B2C: libraries, pre-K, Reach Out and Read-style clinics. |
| **North-star metric** | **Weekly shared reads with at least one dialogic exchange** (a prompt the adult marks "asked", or a child response recorded by tap). |
| **MVP candidate?** | **Yes**, one of the likely Year-1 trio. |

## 2. Problem & users

**Problem statement.**
- **Dialogic reading works, especially for toddlers.** Meta-analyses report expressive-vocabulary effects around d = 0.41–0.59 and receptive around d = 0.22–0.26; children aged 2–3 gain more (d ≈ 0.50) than 4–5-year-olds (d ≈ 0.14) [V] ([summary of Mol et al. 2008 and later reviews](https://eric.ed.gov/?id=EJ787378); [Pillinger 2022 review](https://reachoutandread.org/wp-content/uploads/2023/06/Pillinger_2022_A-story-so-far-A-systematic-review-of-the-dialogic-reading-literature.pdf)).
- **But effects are smaller in lower-education families** (reported d ≈ 0.13 vs. 0.53) [V] (same meta-analytic summary). Parents don't know the technique; the adult needs scaffolding. That is an app-shaped problem.
- **Bedtime audio is a huge, screen-guilt-driven market.** Tonies grew revenue 31% to €630M in 2025 and sold 2.6M Tonieboxes [V] ([Tonies FY2025](https://www.mynewsdesk.com/us/tonies/pressreleases/tonies-continues-profitable-growth-with-record-results-in-2025-expects-strong-momentum-for-full-year-2026-expansion-of-ecosystem-around-toniebox-2-proves-a-global-success-3442746)). Yoto grew 86% to £94.8M in 2024 [V] ([Music Ally](https://musically.com/2025/08/27/childrens-speakers-startup-yoto-saw-sales-grow-by-86-in-2024/)).
- **Existing reading apps frustrate parents.** Epic's free tier is "1 book a day", free school-hours home access was removed, it is "notoriously difficult to cancel", and young children can reach "terrifying" nonfiction [V] ([raw 03](../../../research/raw/03-forum-voice-of-customer.md)). Moshi's Trustpilot score (2.8–3/5) contrasts with its 4.7★ App Store rating [V].
- **AI stories are arriving without trust.** In an NC State study, most parents were not comfortable with AI generating story text; they accepted AI images if text was human-authored and images reviewed by educators or librarians, and wanted clear labelling [V] ([NCSU 2025](https://research.ncsu.edu/how-parents-and-kids-really-feel-about-ai-generated-images-in-childrens-books/)). "AI slop" is flooding children's media [V] ([The 74](https://www.the74million.org/zero2eight/ai-slop-is-flooding-childrens-media-parents-should-be-very-alarmed/)).

**Personas.**

| Persona | Snapshot | Needs |
|---|---|---|
| **Andre, 38, and Zoe (5), Spanish/English home** | Reads at bedtime, wants vocabulary in both languages; tired. | Short, good books in both languages; prompts that feel natural; a calm ending. |
| **Grandma Rosa, 67** | Video-calls grandkids; reads at weekends. | Record herself reading so the kids hear her voice any night; big text. |
| **Kai, 6, dyslexic (early signs), with mum** | Loves stories, avoids print. | Read-to-me with word highlighting, adjustable speed, no reading pressure. |
| **Lena, 4, blind, with dad** | Braille-curious; loves audio. | Fully audio experience; described illustrations; VoiceOver-navigable. |
| **Tom, 31, low-literacy dad** | Embarrassed to read aloud. | Narration he can "read along" with; prompts he can hear through one earbud. |

**Needs & wants.**

| Need | Evidence | Response |
|---|---|---|
| Vocabulary & connection at bedtime | Dialogic reading effects [V] | "Pause & Ask" prompts (PEER/CROWD) for the adult |
| Low-SES/low-confidence adults supported | Smaller effects in less-educated families [V] | Audio prompts, one per page max, "say it like this" examples; narration to read along |
| Screen-free bedtime | Tonies/Yoto growth [V] | Lantern Mode: screen off, warm audio, ends itself |
| Trustworthy personalised stories | NCSU study [V]; AI slop [V] | Human-written templates; human review of every new story; clear labels |
| Age-appropriate content | Epic "terrifying" nonfiction [V] | Age-gated, curated library; no open browsing for under-5s |
| Honest pricing | Epic cancellation, Moshi Trustpilot [V] | Fair-billing charter; free re-reads |
| Accessible reading | Read-to-Me highlighting valued in Epic [V] | Highlighting, speed, dyslexia settings, described images, sign language books (V2) |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Epic** | Epic Creations | 1.2–2M US iOS/yr [E via raw 02]; 35–40K+ titles [V] | $13.99/mo or $84.99/yr ($62.99 first yr); free for educators [V] | ≈4.6 iOS [E] | Huge library; Read-to-Me highlighting; audiobooks [V] | 1 book/day free tier; hard to cancel; scary nonfiction; ownership turmoil [V] | Highlighting is dyslexia-friendly; DT limited in book view [V] | [pricing](https://myelearningworld.com/epic-pricing/) · [App Store](https://apps.apple.com/us/app/epic-kids-books-reading/id719219382) · [raw 03](../../../research/raw/03-forum-voice-of-customer.md) |
| **Tonies** (hardware + app) | tonies SE | €630M 2025 revenue; 2.6M boxes, 43.3M figures sold [V] | Toniebox ≈$100 + figures ≈$15 each [M] | n/a | Screen-free, toddler-proof; Creative-Tonies for family recordings [M] | Cost of figures; content locked to figures [M] | Screen-free; tactile control good for 2+ [I] | [FY2025 release](https://www.mynewsdesk.com/us/tonies/pressreleases/tonies-continues-profitable-growth-with-record-results-in-2025-expects-strong-momentum-for-full-year-2026-expansion-of-ecosystem-around-toniebox-2-proves-a-global-success-3442746) |
| **Yoto** (hardware + app) | Yoto Ltd | £94.8M revenue 2024 (+86%); 2025 "a lot higher" [V] | Player ≈$100–150 + cards; Make Your Own cards [V/M] | n/a | Make Your Own cards (family recordings); screen-free [V] | Card cost; app needed to set up [M] | Screen-free; night-light [M] | [Music Ally](https://musically.com/2025/08/27/childrens-speakers-startup-yoto-saw-sales-grow-by-86-in-2024/) · [MYO](https://us.yotoplay.com/make-your-own) |
| **Moshi Kids** | Mind Candy | 4.7★ from ~70K US ratings [V] | 7-day trial; $12.99/mo or $79.99/yr [V] | 4.7 iOS; Trustpilot 2.8 [V] | 400+ sleep stories and soundscapes; celebrity voices [V/M] | Billing/renewal complaints (Trustpilot) [V] | Audio-first, calm [V] | [App Store](https://apps.apple.com/us/app/moshi-kids-sleep-relax-play/id1306719339) · [Trustpilot](https://www.trustpilot.com/review/moshikids.com) |
| **Readmio** | Readmio | 2.2M downloads [V] | Few free stories; subscription; lifetime $59.99 [V] | 4.8 (23K) aggregate; 4.9 iOS / 4.5 Play [V] | **Reacts to the parent's reading voice** with sound effects and music [V] | Sound effects can over-stimulate at bedtime [I] | Parent reads (co-play) [V]; offline [V] | [site](https://www.readmio.com/) · [App Store](https://apps.apple.com/us/app/readmio-kids-bedtime-stories/id1473021827) |
| **Vooks** | Vooks | Not published; 9.8K iOS ratings [V] | $9.99–10.99/mo or $69.99/yr; 7-day trial [V] | 4.5 iOS / 4.3 Play [V] | Animated read-along storybooks; Spanish (111) & Hindi (25) titles [V] | Animated video = more passive [I] | Read-along text; video motion [V/I] | [pricing](https://info.vooks.com/vooks-pricing-plans) · [App Store](https://apps.apple.com/us/app/vooks-read-aloud-kids-books/id1435813450) |
| **Oscar (AI stories)** | HeyQQ GmbH | 100K+ Play [V] | $4.99/mo or $39.99/yr; coin packs [V] | 4.8 Play (2.6K); 4.6 iOS (48) [V] | Child as hero; interests [V] | Unreviewed AI text [I]; coin mechanics [V] | Text + TTS [M] | [Play](https://play.google.com/store/apps/details?id=com.heyqqgmbh.oscarai&hl=en_US) · [App Store](https://apps.apple.com/us/app/oscar-bedtime-stories/id1663618939) |
| **Amazon Kids+** | Amazon | Bundled; not broken out [M] | ≈$5.99/mo with Prime [M] | n/a [M] | Huge catalogue of books, video, games [M] | Mixed quality; video dominates [M] | Device-dependent [M] | [M] |

**Takeaways [I].** The money is in **screen-free audio** (Tonies, Yoto) and **big libraries** (Epic). The co-play pattern exists only in Readmio (parent reads, app reacts). Personalisation exists only in unreviewed AI apps with small user bases. **Nobody teaches the adult to read dialogically, and nobody offers trusted personalisation.**

**Feature matrix.**

| Feature | Epic | Tonies | Yoto | Moshi | Readmio | Vooks | Oscar | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Curated picture-book library | ✓ | partial | ✓ | ✗ | ✓ | ✓ | ✗ | **Parity** (smaller, curated, 2–7 only) |
| Read-to-me with word highlighting | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | partial | **Parity + improve** (speed, dyslexia settings) |
| Dialogic prompts for the adult | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** (signature) |
| Parent reads; app responds | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | **Improve**: page-turn follow + prompt timing, *no* sound-effect barrage |
| Personalised stories (child as hero) | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Differentiate** with human templates + review |
| Family voice recordings | ✗ | ✓ | ✓ | ✗ | partial [M] | ✗ | ✗ | **Parity** (grandparent recordings) |
| Screen-off audio mode | ✓ (audiobooks) | ✓ | ✓ | ✓ | ✗ | ✗ | partial | **Parity**: Lantern Mode, self-ending |
| Sleep soundscapes that loop all night | ✗ | partial | ✓ | ✓ | ✗ | ✗ | ✗ | **Reject** all-night loops by default; optional 30-min fade only |
| Animated video books | partial | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | **Reject**: passive, higher stimulation at bedtime |
| Open browsing of 40K titles | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | **Reject** for under-5s (age-safe shelves) |
| Coins / gems for stories | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Reject** (currencies) |
| Dedicated hardware | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | **Reject for now** (vision: no hardware until retention proven) |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| SL-01 | **Pause & Ask prompts** ★ | On ~1 in 3 pages, a small lantern icon offers one adult prompt drawn from PEER (Prompt, Evaluate, Expand, Repeat) and CROWD (Completion, Recall, Open-ended, Wh-, Distancing) types, matched to age: e.g., "Point to the moon. What's that?" (2–3) → "Why do you think the fox hid?" (5–7). Tap to hear it privately (earbud) or read it. | Dialogic reading evidence [V]; no competitor has it [I] | Differentiate | MVP | Must |
| SL-02 | **Curated library (2–7)** | 150 books at launch [E]: licensed picture books + originals; EN/ES; shelves by age and theme; no open search for under-5s. | Epic scale not needed; curation avoids scary content [V] | Parity | MVP | Must |
| SL-03 | **Read-to-me with highlighting** | Human-narrated; word highlighting; 0.75×–1.25× speed; page turns by tap (no swipe-only). | Epic Read-to-Me [V]; Kai persona | Parity | MVP | Must |
| SL-04 | **Lantern Mode** ★ | Screen off (or a dim amber glow), human narration, Pause & Ask replaced by one gentle end-of-story question, 15/20/30-min cap, fade to silence and "Goodnight, Zoe." No autoplay beyond the parent's chosen number of stories. | Tonies/Yoto demand [V]; P9; vision | Differentiate | MVP | Must |
| SL-05 | **My Story (personalised stories)** ★ | Child's name, favourite things and family words inserted into **human-written story templates** (80 templates at launch [E]); AI chooses among pre-written variants and writes only bounded slot text; every new composed story is **reviewed by a human editor before first delivery** (SLA ≤24 h; instant delivery from the pre-approved variant cache). Labelled "Written by our team, personalised with AI help, checked by an editor." | NCSU parent trust findings [V]; Oscar demand [V]; vision | Differentiate | MVP (limited: 20 templates) | Must |
| SL-06 | **Family photo pages** | Parent adds up to 3 photos (e.g., the child's room, grandma, the dog) placed in illustrated frames inside My Story. **No AI-generated likeness of the child, no face analysis.** Photos stay encrypted in the family account. | Vision card; privacy (COPPA biometrics) | Differentiate | V1 | Should |
| SL-07 | **Grandparent Voice** | Adults record themselves reading any library book page by page; plays in the app or Lantern Mode. Never used for training. | Yoto MYO / Creative-Tonies [V/M]; Rosa persona | Parity | V1 | Should |
| SL-08 | **Parent-reads mode** | Adult reads aloud; the app listens **to the adult only** to follow along and turn pages / surface a prompt at the right moment; tap fallback always. On-device ASR. | Readmio's reactive reading [V] | Improve | V1 | Could |
| SL-09 | **Bedtime routine wrapper** | "Two stories, then lights out": parent sets number of stories; Now/Next/Done strip; transition warning; ending. | Lumen §3.3; Calm Cubs synergy | Lumen | MVP | Must |
| SL-10 | **Favourites & free re-reads** | Children can re-read any book they've "favourited" unlimited times, even on the free tier. | Epic "1 book a day" anger [V]; repetition is how toddlers learn [M] | Improve | MVP | Must |
| SL-11 | **Word of the night** | One rich vocabulary word per book, with a picture, spoken definition and a co-play tomorrow tip. | Vocabulary goal; weekly summary | Differentiate | MVP | Should |
| SL-12 | **Weekly one-screen summary** | Books shared, prompts asked, words of the night, favourite themes. | Research paper need #7 | Parity | MVP | Must |
| SL-13 | **Accessibility pack** | Described illustrations (audio descriptions) for blind children; dyslexia settings; captions; VoiceOver page navigation. | Lena, Kai personas; Lumen P2/P6/P7 | Lumen | MVP | Must |
| SL-14 | **Bilingual books & switch** | EN/ES side-by-side or toggle per page; narration in both. | Vooks Spanish titles [V]; Andre persona | Parity | MVP | Should |
| SL-15 | **Library card access** | Library patrons unlock the Family plan with a library card (B2B2C). | Vision channel | Differentiate | V1 | Should |
| SL-16 | **Sign-language story videos** | ASL/BSL-signed stories with captions, by Deaf storytellers. | Deaf families [I] | Differentiate | V2 | Could |
| SL-17 | **Child-told stories** | The child dictates a story (adult types or records); illustrated from a sticker set; kept private. | Narrative skills [I] | Differentiate | V2 | Could |

★ **Signature features:** Pause & Ask (SL-01), Lantern Mode (SL-04), My Story (SL-05). **MVP = SL-01–05, SL-09–14 (11 features).**

## 5. Core experience & key user flows

**Core loop.** Choose (or accept tonight's pick) → read together with Pause & Ask → word of the night → chosen number of stories → Lantern Mode or lights out → "Goodnight" → morning co-play tip.

**Flow 1: Onboarding (≤4 min).**
1. Price and privacy screen (Family Hub standard).
2. Child's first name (for My Story), age, languages, 3 favourite things (icons).
3. Bedtime set-up: how many stories (1–3), Lantern Mode yes/no, cap length.
4. "How do you like to read?" Read-to-me / I'll read / Mix.
5. First book opens with a 20-s adult tip: "When you see the lantern, try the question. Then wait."

**Flow 2: Core session (shared read).**
1. Book page: text + illustration; narration (or adult reads).
2. Lantern glows softly on page 3. Adult taps: "Ask: what do you think is in the box? Wait. Then add a word: 'Yes, a *fluffy* kitten!'"
3. Adult taps "We did it" (optional) or just continues.
4. End page: word of the night ("*enormous*: really, really big"), tomorrow tip.
5. Now/Next/Done strip shows "Story 2 of 2 next". After the last story: dim transition to Lantern Mode or "Goodnight" screen.

**Flow 3: My Story request.**
1. Parent: "Make a story" → choose theme (e.g., "first day at nursery") and cast (child, sibling, dog).
2. If a pre-approved variant exists: delivered instantly. Else: "Our editor is checking your story. It'll be ready by tomorrow night." (Push to parent, never child.)
3. Parent previews every My Story before the child sees it (mandatory at MVP).

**Flow 4: Caregiver view.** Weekly summary; grandparent invites; recordings list; library-card linking.

**Flow 5: My Needs.** Narration speed, highlighting colour, font/spacing, described images, captions, Sensory Dial, language(s), Lantern Mode cap, earbud prompts.

**Flow 6: Billing.** Family Hub standard; free tier shows exactly what's free ("1 new book a day + unlimited favourites + Lantern Mode for those books").

**Information architecture.** Child-facing "Bookshelf" (max 12 covers, big) · Parent area (gated): Tonight · My Stories · Recordings · Week · Settings. Reading view: page, lantern (adult), Now/Next/Done strip.

**Session design.** Default 2 stories (~10–15 min); Lantern Mode cap 20 min; transition warning before the last story; no autoplay beyond the plan.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial defaults.** Ages 2–3: **Calm**; ages 4–7: **Calm at bedtime**, Balanced in daytime (automatic by local time, parent can override).

| Level | Story Lantern behaviour |
|---|---|
| Calm | Static illustrations; page-turn cross-fade; narration only; no sound effects; warm, dim palette after 6 pm |
| Balanced | Subtle parallax off; soft ambient sound per book (optional); gentle page-turn sound |
| Lively (daytime only) | Light illustration animation (≤2 s, no flashing); sound effects in books that have them |

**Input modes.** Page turn by tap on large side zones (≥2.5 cm wide full-height), keyboard arrows, switch, Voice Control ("next page"); swipe is optional, never required. Child responses to prompts are spoken to the adult, not scored by the app. Parent-reads mode (V1) listens to the adult with tap fallback.

**Targets.** Page-turn zones full-height, ≥2.5 cm wide (2–3) / ≥2 cm (4–7). Bookshelf covers ≥3 cm.

**Reading & typography.** Read-to-me always available; highlighting by word (colour + underline, not colour alone); text size to 200% without overlapping illustrations (reflowing text layer); BDA defaults, off-white page tint option; line length ≤60 characters; no justified text. Decodable books are Sound Garden's job; Story Lantern is about language, so text level is not gated.

**Audio.** Separate sliders: narration, prompts, ambient; prompts can route to one earbud / the parent's phone ("whisper mode"). Captions of narration (the highlighted text doubles as captions). Audio descriptions of illustrations (SL-13).

**Age-respectful themes.** Two looks: "Storybook" (illustrated UI) and "Quiet" (plain, for older or sensory-sensitive children); library content spans 2–7 with 6–7 shelves avoiding babyish visuals.

**Lumen principles.**

| P# | Acceptance criterion |
|---|---|
| P1 | After 6 pm, Calm palette and no animation by default; Reduce Motion honoured |
| P2 | All narration captioned via highlighted text; described illustrations available for 100% of MVP books |
| P3 | Now/Next/Done strip in every bedtime session; warning before the last story |
| P4 | Page turns by tap on ≥2 cm zones; no swipe-only |
| P5 | Prompts ≤12 words; audio available |
| P6 | BDA defaults; text spacing override works without clipping |
| P7 | Page turn by tap, key, switch, voice |
| P8 | No quizzes or scores on stories |
| P9 | Plan-limited sessions; Lantern Mode self-ends |
| P10 | Child shelf needs no login |
| P11 | Narration speed adjustable; no timed prompts |
| P12 | Reading settings sync from My Needs |
| P13 | Two UI looks; age-appropriate shelves |
| P14 | First read ≤4 min after install |
| P15 | No stars/badges; "books we loved" shelf instead |
| P16 | Library audited for representation (disability, family structures, languages); ND advisory review |
| P17 | Claims: "uses dialogic reading, an approach with research support"; never "boosts vocabulary by X%" until we measure it |
| P18 | My Story and photos: human-reviewed, never used for training, no face analysis |

**Target Lumen audit score:** ≥22/24.

## 7. AI specification & guardrails

**What AI does.**
1. **My Story composition:** template selection → slot filling (names, pets, favourite things, a family word) → an LLM may write *bounded* bridging sentences (≤2 per page, ≤15 words each, reading level constrained) → automated checks → **human editorial review** → delivery. Approved stories are cached and reused as variants (e.g., "dog" vs. "cat" versions) so most requests are instant and still human-reviewed.
2. **Prompt matching:** rules + light ML to choose which pre-written Pause & Ask prompt fits the page and child's age; no generated prompts at runtime.
3. **Parent-reads following (V1):** on-device ASR on the **adult's** voice to track the page; no child audio processed.

**What AI does not do.** No chat with the child; no story "character" that converses; no AI-generated images of the child or family; no face recognition in photos; no emotion inference; no open-ended story generation from free-text prompts by children.

**Pedagogical policy.** Prompt library authored by early-literacy specialists, tagged by PEER/CROWD type and age; at most one prompt per 3 pages to avoid interrupting the story (the evidence favours conversation, not quizzing [I]).

**Safety.** Templates exclude peril beyond age-appropriate mild tension; blocked-content lists (violence, body image, food shaming, stereotypes) run on every composed story; reading-level check (e.g., ≤ grade 1 for 2–4, ≤ grade 2 for 5–7) [E]; editor checklist (names used respectfully; no unsafe behaviour modelled; cultural review of family words). Parent preview before first child exposure. Clear labelling of AI assistance (EU AI Act Art. 50 spirit).

**Evaluation plan.** Red-team 500 slot inputs (odd names, instructions hidden in "favourite things", slurs, adult words) → 0 unsafe outputs reach editors' approve queue without a flag; editor rejection rate tracked (target <10% after month 2 [E]); parent trust rating ≥4/5; reading-level compliance ≥98%.

**Cost and latency [E].** LLM slot text: ~1–2K tokens per story, <$0.01; human review 3–5 min per new story → ~$1–2 per *new* story at editor rates; caching target: ≥80% of requests served from approved variants by month 6, keeping review cost <$0.25 per delivered story. This is the key unit-economics risk.

## 8. Data, privacy & compliance

**Data inventory.**

| Data | Purpose | Processing | Retention |
|---|---|---|---|
| Child first name, age, favourite things | My Story, shelves | Cloud, encrypted | Life of account; deletable |
| Family photos | My Story frames | Cloud, encrypted, family-only | Until deleted; purged 30 days after deletion |
| Adult voice recordings | Grandparent Voice | Cloud, encrypted, family-only | Until deleted |
| Reading events (books, prompts tapped) | Summary, recommendations | First-party | 13 months |
| Adult speech in parent-reads mode | Page following | On-device only | Not retained |

**Regimes.** COPPA 2025 (child's name and photos are personal information; photos of a child's face may be biometric-adjacent: we perform no face processing and state so; verifiable parental consent; separate consent for photo storage; no training use). UK AADC; state AADCs; EU AI Act Art. 50 (disclose AI assistance in content); Apple Kids category and Google Families policies (no third-party analytics; parental gate; no external links on the child side). Publisher licensing: DRM for licensed books, offline caching within licence terms.

**Consent.** Parent consent at sign-up; separate toggles for photos and recordings; separate consent for any story shared outside the family (e.g., printed book partner in V2).

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Free forever | $0 | 1 new library book/day, unlimited favourites, Lantern Mode for those books, Pause & Ask, all accessibility |
| Family plan | ≈$9.99/mo or $69/yr (7 apps, 3 children) | Full library, My Story, photos, Grandparent Voice, bilingual shelves |
| Library / pre-K | Per-cardholder or per-classroom licence [E: $1–3 per active patron/yr] | Family plan via library card; classroom read-aloud mode |
| Gift | $69 annual gift card for grandparents | |

Benchmarks: Epic $84.99/yr; Moshi $79.99/yr; Vooks $69.99/yr; Oscar $39.99/yr; Readmio lifetime $59.99; Tonies/Yoto hardware ~$100 + content [V/M]. We price at the low end of Epic/Moshi, and include six other apps.

**Channels.** Libraries (story-time partnerships, card access); pediatric "prescribe a book" programs; grandparent gifting (Grandparent Voice is the hook); bedtime-routine creators; bilingual parent communities.

**ASO.** "bedtime stories for kids", "personalized story with my child's name", "read aloud books toddler", "bilingual bedtime stories Spanish". Accessibility Nutrition Label: VoiceOver, Larger Text, Captions, Audio Descriptions, Reduced Motion, Sufficient Contrast.

**Launch.** US (EN/ES), UK/IE, Canada, Australia (EN) [I].

## 10. Success metrics
- **North-star:** weekly shared reads with ≥1 dialogic exchange (target ≥4/week per active family [E]).
- **Inputs:** Pause & Ask tap rate (≥30% of offered prompts [E]); My Story re-listen rate (≥2 plays per story); Lantern Mode sessions ending by cap vs. by adult; grandparent recordings per family.
- **Guardrails:** Sensory Comfort ≥4/5 at bedtime; zero unsafe My Story deliveries; editor rejection <10%; parent trust ≥4/5; zero billing complaints; Lantern Mode never exceeds cap.
- **Outcomes:** expressive vocabulary probe (target words from books) and parent dialogic-behaviour coding in a 6-week pilot; plan E4 → E3 (pre/post with a library partner) → E2 (comparison group, Year 2).
- **Retention:** D30 30%, M3 20% (bedtime habit is sticky [I]); DAU/MAU ≥35% [E] (Epic/Moshi comparables not verified).

## 11. Validation plan

**Riskiest assumptions.**
1. Personalised stories add value over a curated library, and parents trust them (vision).
2. Adults will use dialogic prompts at bedtime without it feeling like homework.
3. Human review of personalised stories is affordable at scale (unit economics).
4. Lantern Mode is a credible substitute for Yoto/Tonies hardware.

| # | Method | Sample | Success | Kill / rethink |
|---|---|---|---|---|
| E1 | **Wizard-of-Oz My Story**: a human writer produces "AI-personalised" stories from templates, delivered as audio + PDF | 20 families, 3 weeks (≥5 bilingual, ≥3 with a disabled child) | Each story re-listened ≥2×; trust ≥4/5; ≥50% "very disappointed" if removed | Re-listen <1.5 → library-first, drop My Story from MVP |
| E2 | **Pause & Ask diary**: printed prompt stickers placed in family's own books | 20 families (≥6 lower-education caregivers) | Prompts used on ≥3 nights/week; parents rate "natural" ≥4/5 | <2 nights → reduce to one end-of-story question |
| E3 | **Lantern Mode** vs. family's current bedtime audio (Yoto/Tonies/Spotify) | 12 families, 2 weeks, counterbalanced | ≥50% prefer or rate equal; sleep-onset routine not longer | Clear loss → consider hardware partnership (Yoto MYO export) |
| E4 | **Review-cost spike**: time editors on 100 composed stories | 3 editors | ≤5 min per story; ≥70% reusable as variants | >10 min → narrower templates |
| E5 | **Label test**: 3 disclosure wordings for AI assistance | n≈300 parents (survey) | Chosen wording raises or keeps trust | All lower trust → rethink AI role |

**Mapping.** E1 → WP4 Wizard-of-Oz; E2 → WP2 diary + WP4 paper prototypes; E3 → WP4 sensory A/B; E4 → WP4 feasibility spike/cost model; E5 → WP2 survey.

## 12. Build handoff

**Epic SL-E1: Reader.**
- **Given** a book is open, **when** narration plays, **then** each word highlights in sync (±100 ms) with colour and underline.
- **Given** text size is 200%, **then** text reflows without covering the illustration focal area and without truncation.
- **Given** VoiceOver is on, **when** a page loads, **then** the page text and illustration description are read in order.

**Epic SL-E2: Pause & Ask.**
- **Given** the child is 2, **when** a prompt is offered, **then** it is a pointing/labelling or completion prompt, ≤12 words.
- **Given** whisper mode is on, **when** the adult taps the lantern, **then** audio routes only to the connected earbud / parent device.
- **Given** 3 pages have passed without a prompt, **then** at most one prompt is offered on the next eligible page.

**Epic SL-E3: Lantern Mode & bedtime wrapper.**
- **Given** the plan is 2 stories + Lantern Mode 20 min, **when** the second story ends, **then** the screen dims to amber and audio continues; at 20 min audio fades over 30 s and stops; no further content plays.
- **Given** Lantern Mode is running, **when** the device is tapped, **then** only a single "pause" control is available (no browsing).

**Epic SL-E4: My Story pipeline.**
- **Given** a parent requests a story, **when** no approved variant exists, **then** it enters the editor queue and the parent sees an honest ETA; the child side shows nothing new.
- **Given** a favourite-thing field contains "ignore previous instructions…", **then** the slot is rejected by validation and never reaches the LLM.
- **Given** a story is approved, **then** the parent must preview it once before it appears on the child's shelf.

**Epic SL-E5: Library & billing.** Library-card linking via partner API; Family Hub standard billing; **Given** free tier, **then** favourited books remain readable indefinitely.

**Non-functional.** Offline for downloaded books and Lantern Mode; book open ≤2 s; audio gapless; iOS/iPadOS, Android, web reader (V1); WCAG 2.2 AA; EN/ES; DRM per publisher; encryption for photos/recordings; zero third-party SDKs.

**QA focus.** AT matrix (VoiceOver, TalkBack, Switch, Voice Control, Dynamic Type XXL, captions, audio description playback). Sensory: bedtime Calm vs. Balanced with 2–3 and 4–7 groups. AI safety: 500-case slot red-team; reading-level checks; editor-bypass attempts. COPPA: photo consent, deletion, no photo processing beyond resizing. Billing: free-tier limits exactly as advertised.

**Platform dependencies.** Lumen (reader components, Dial); My Needs (reading settings); Family Hub (recordings, photos, billing, library cards); AI orchestration (template engine, editor queue, safety filters); evidence engine (vocabulary probes).

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Review costs make My Story unprofitable | M | H | Variant caching; narrower templates; My Story allowance per month |
| Book licensing costs/limits | H | M | Mix of originals and licensed; library-partner deals |
| Prompts feel like homework | M | M | ≤1 per 3 pages; adults can turn off; tone testing |
| Parents still want hardware | M | M | Export to Yoto MYO / Creative-Tonies (V2 partnership) [I] |
| Unsafe personalised content | L | H | Human review + parent preview; kill switch |
| Epic/Moshi price cuts | M | L | Bundle value; free re-reads |

**Open questions.** Should Pause & Ask also exist in Lantern Mode (audio question at the end only)? Will publishers license books for prompt overlays? Is 20 templates enough for MVP delight? Should My Story be available in Spanish at MVP (translation review doubles editor load)?

## 14. Sources
- [V] Dialogic reading meta-analysis (Mol et al. 2008, ERIC): https://eric.ed.gov/?id=EJ787378 · Pillinger & Vardy 2022 review: https://reachoutandread.org/wp-content/uploads/2023/06/Pillinger_2022_A-story-so-far-A-systematic-review-of-the-dialogic-reading-literature.pdf · ASHA interactive book reading: https://pubs.asha.org/doi/pdf/10.1044/2020_JSLHR-19-00288
- [V] NC State study on AI in children's books: https://research.ncsu.edu/how-parents-and-kids-really-feel-about-ai-generated-images-in-childrens-books/
- [V] The 74 on AI slop: https://www.the74million.org/zero2eight/ai-slop-is-flooding-childrens-media-parents-should-be-very-alarmed/
- [V] Tonies FY2025: https://www.mynewsdesk.com/us/tonies/pressreleases/tonies-continues-profitable-growth-with-record-results-in-2025-expects-strong-momentum-for-full-year-2026-expansion-of-ecosystem-around-toniebox-2-proves-a-global-success-3442746
- [V] Yoto revenue: https://musically.com/2025/08/27/childrens-speakers-startup-yoto-saw-sales-grow-by-86-in-2024/ · https://www.thebookseller.com/news/yotos-2025-revenue-a-lot-higher-co-founder-ben-drury-reveals-at-futurebook · MYO: https://us.yotoplay.com/make-your-own
- [V] Epic pricing: https://myelearningworld.com/epic-pricing/ · App Store: https://apps.apple.com/us/app/epic-kids-books-reading/id719219382
- [V] Moshi: https://apps.apple.com/us/app/moshi-kids-sleep-relax-play/id1306719339 · https://www.trustpilot.com/review/moshikids.com
- [V] Readmio: https://www.readmio.com/ · https://apps.apple.com/us/app/readmio-kids-bedtime-stories/id1473021827
- [V] Vooks: https://info.vooks.com/vooks-pricing-plans · https://apps.apple.com/us/app/vooks-read-aloud-kids-books/id1435813450
- [V] Oscar: https://play.google.com/store/apps/details?id=com.heyqqgmbh.oscarai&hl=en_US · https://apps.apple.com/us/app/oscar-bedtime-stories/id1663618939
- [V] Epic forum complaints: [raw 03](../../../research/raw/03-forum-voice-of-customer.md); Epic iOS volume: [raw 02](../../../research/raw/02-apple-app-store-top30.md)
- [M] Amazon Kids+ pricing; Tonies/Yoto hardware prices; Creative-Tonies

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Keep (lead) |
| **Ships in** | Lanternling app (S1) |
| **Build wave** | 1c |
| **Pre-discovery priority score** | 83/100 [I] |
| **Consumes engines** | EN-04, EN-07, EN-10 |
| **Studio features used** | SX-06, SX-13, SX-25, SX-32 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = SL-01, SL-02, SL-03, SL-04, SL-05, SL-09.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| SL-E1 | **Remote bedtime** | A grandparent or travelling parent reads live by link, with synced pages and no install (SX-06). |
| SL-E2 | **Human-signed story shelf** | ASL/BSL stories by Deaf storytellers, moved from V2 to V1 (SX-13). |
| SL-E3 | **Audio-player export** | Lantern Mode stories are playable on partner audio players or smart speakers where partner terms allow (SX-25). |

### 15.3 New validation question
Remote bedtime with 15 distant-grandparent families: ≥2 sessions/week, and a grandparent SUS ≥75.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 4 | 5 | 4 | 4 | 4 | 4 | 4 | 4 |

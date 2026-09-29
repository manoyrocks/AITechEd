# Two Words: App Strategy & Product Specification

> **Venture:** Lanternling · **App #:** 7/7 · **Ages:** 3–7 (child with a parent or grandparent) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/01-lanternling-early-years.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Venture index](README.md)
> **Confidence tags:** [V] verified this session (URL given; mostly search snippets or repo raw files) · [V2] secondary or vendor source · [M] from memory · [E] estimate · [I] inference
> **Research caveat:** the session's web-search budget ran out before this app's research. Store pages were proxy-blocked. Lingokids, Duolingo and PBS KIDS data come from the repo's verified raw files. Gus on the Go, Studycat, Rosetta Stone Kids, Dinolingo and Mondly Kids figures are [M] and must be verified in Discovery WP1.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Keep the family language alive while English grows: playful word pairs in the home language and English, with grandparents' own voices, and games two generations can play together. |
| **Primary user / buyer** | Children 3–7 with a parent or grandparent. Buyers: (a) US heritage families (Spanish first), (b) EFL families in Mexico and Brazil (Spanish/Portuguese → English). Gift buyers: grandparents. |
| **Core job-to-be-done** | "When my child starts answering only in English (or needs English for school), I want a joyful daily way to use both our languages, with our family's own words and voices, so my child can talk with their abuela and do well at school." |
| **Category on the stores** | Apple: Kids › Ages 5 & Under / 6–8 (Education). Google Play: Families › Educational. |
| **Top competitors** | Lingokids (50M+ Play; ≈$38M US grossing 2025) · Duolingo (178M downloads in 2025, not built for under-7s) · PBS KIDS Games (bilingual games, free) · Gus on the Go [M] · Studycat / Fun Spanish [M] · Rosetta Stone Kids [M] · Dinolingo [M] · Mondly Kids [M] |
| **Our wedge** | 1. **Two languages as equals**: the home language is not a "foreign" language; family dialect and words are respected. 2. **Grandparent voices and co-play across generations**, which no competitor centres. 3. **Calm, no accent scoring, fair billing**, against high-stimulation, upsell-heavy leaders. |
| **Business model** | In the Lanternling Family plan (≈$9.99/mo or $69/yr, 7 apps). Free: 3 word worlds + grandparent recording for them. Local pricing for MX/BR EFL (to validate). B2B2C: dual-language pre-K, libraries, EFL schools. |
| **North-star metric** | **Weekly two-language play moments** (sessions using both languages with an adult or a grandparent recording). |
| **MVP candidate?** | **Later**, pending the heritage vs. EFL willingness-to-pay test. |

## 2. Problem & users

**Problem statement.**
- **Bilingual families want to keep the home language alive, and most kids' apps are English-only** (vision). Research-agent notes flag "bilingual Spanish/English at PBS quality but with depth" as an open gap for 4–7 [V] ([raw 02](../../../research/raw/02-apple-app-store-top30.md)).
- **Language shift is fast**: in many immigrant families the home language is largely lost by the third generation [M], and children often switch to answering in English once they start school [M].
- **The paid leader is loud and upsell-heavy.** Lingokids (50M+ Play; 4.3★ from ~221K; ≈$79.99–99.99/yr; #2 grossing US kids learning app 2025 at ≈$38M) is praised for breadth but criticised for bright, busy scenes, auto-renew and upsells ("paid $15 to unlock content but their grandson still got nothing extra"; free trial "barely playing for 10 minutes") [V] ([raw 01](../../../research/raw/01-google-play-top30.md), [raw 02](../../../research/raw/02-apple-app-store-top30.md), [raw 03](../../../research/raw/03-forum-voice-of-customer.md)).
- **EFL willingness to pay is proven in LatAm/Asia** (the Lingokids model) [M] ([raw 05](../../../research/raw/05-market-and-trends.md)); heritage willingness to pay is unproven (vision riskiest assumption).
- **Speech scoring penalises accents and speech differences** (ELSA, Praktika) [V] ([Research paper §6](../../01-research-paper.md)). Child ASR is weak [V] (see [Sound Garden](04-sound-garden.md)).

**Personas.**

| Persona | Snapshot | Needs |
|---|---|---|
| **Andre, 38, and Zoe (5), Spanish/English, US** | Zoe answers in English; Andre worries about losing Spanish. | Spanish that feels like play; the family's Mexican Spanish words; progress he can see. |
| **Abuela Carmen, 71, in Guadalajara** | Video-calls weekly; low tech confidence; speaks only Spanish. | Record words and a short story in her voice; play a simple game on video call; big buttons. |
| **Luana, 34, São Paulo, and Pedro (4)** | Wants English early for school opportunities. | Affordable, safe EFL in local currency; Portuguese support for her. |
| **Ana, 6, hard of hearing (cochlear implant), bilingual home** | Needs clear audio and captions in both languages. | Captions, visual cues, adjustable speech rate. |
| **Ms. Rivera, dual-language pre-K teacher** | Half her class are Spanish-dominant. | Family-home link; printable word pairs; no child data exposure. |

**Needs & wants.**

| Need | Evidence | Response |
|---|---|---|
| Home language valued, not "foreign" | Vision; bilingual gap [V] | Equal-status UI; family chooses dialect; family words |
| Grandparents involved | Vision; Rosa/Carmen personas | Grandparent Voice; two-generation games |
| Calm, not busy | Lingokids busy scenes [V] | Calm/Balanced defaults |
| Honest price | Lingokids upsell complaints [V] | Fair billing; local pricing |
| No accent judgement | Speech scoring barriers [V] | Listen-and-compare, never a pronunciation score |
| Accessible for Deaf/HoH and low-literacy adults | Lumen P2, P5 | Captions in both languages; voice-first adult flows |

## 3. Competitive feature benchmark

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **Lingokids** | Monkimun | 50M+ Play; 2.5–3.5M US iOS/yr; ≈$38M US grossing 2025; 185M+ lifetime claimed [V] | ≈$14.99/mo; ≈$79.99–99.99/yr [V/E] | 4.3 Play (~221K); 4.3 iOS (~660K); Trustpilot 3.2 [V] | 1,000+ activities, songs, shows; ad-free; kidSAFE; ESL "playlearning" [V] | Price, auto-renew, thin free tier, upsell messages [V] | Audio-led for pre-readers; bright, busy, musical (MED-HIGH sensory) [V/E] | [raw 01](../../../research/raw/01-google-play-top30.md) · [raw 02](../../../research/raw/02-apple-app-store-top30.md) · [raw 03](../../../research/raw/03-forum-voice-of-customer.md) |
| **Duolingo** | Duolingo | 178M downloads 2025; 58.7M DAU Q2 2026 [V] | Freemium; Super/Max [V] | 4.7 [V] | Habit, streaks, many languages [V] | Energy system, streak burnout, "AI slop" [V] | Drag tiles; VO inconsistent; high-sensory celebrations [V] | [Research paper §4](../../01-research-paper.md) |
| **PBS KIDS Games** | PBS KIDS | 10M+ Play; 2–3M US iOS [V] | Free, no ads [V] | 4.4 iOS (~372K) [V] | Trusted characters; **bilingual games** [V] | App size; crashes [V] | Spoken instructions; large controls; captions [V] | [raw 02](../../../research/raw/02-apple-app-store-top30.md) |
| **Gus on the Go** | Gus Communications | Not verified [M] | Paid per language (≈$4) [M] | ≈4.5 [M] | 30+ languages; simple vocabulary games [M] | Small, dated [M] | Simple, low sensory [M] | [M] |
| **Studycat (Fun Spanish / Fun English)** | Studycat | "Millions of kids" (vendor) [M] | Subscription [M] | ≈4.5 [M] | Songs and games; EFL in Asia [M] | Paywall [M] | Colourful, musical [M] | [M] |
| **Rosetta Stone Kids** | Rosetta Stone (IXL Learning) | Not verified [M] | Paid apps / family plan [M] | n/a [M] | Brand trust; immersion [M] | Limited kids range [M] | Speech recognition-led [M] | [M] |
| **Dinolingo** | Dinolingo | "50+ languages" (vendor) [M] | Monthly family subscription [M] | n/a [M] | Many heritage languages; videos + games [M] | Production quality varies [M] | Video-led [M] | [M] |
| **Mondly Kids** | Mondly (Pearson) | Not verified [M] | Subscription [M] | n/a [M] | 30+ languages; gamified [M] | Generic content [M] | Gamified [M] | [M] |

*Also relevant:* Vooks has 111 Spanish animated storybooks [V] ([Vooks](https://info.vooks.com/vooks-pricing-plans)); Kinedu and Vroom offer EN/ES parenting content [V] (see [Babble Buddy](01-babble-buddy.md)).

**Takeaways [I].** The only scaled player (Lingokids) sells *English* to the world and has trust and sensory complaints. Heritage-language tools (Gus, Dinolingo) are broad but thin. **No one centres the family (dialect, grandparents' voices, cross-generation play), treats the home language as equal, and stays calm.**

**Feature matrix.**

| Feature | Lingokids | Duolingo | PBS KIDS | Gus [M] | Studycat [M] | Dinolingo [M] | Mondly Kids [M] | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Built for 3–7 | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | **Parity** |
| Home language as equal (both directions) | ✗ | ✗ | partial | partial | ✗ | partial | ✗ | **Differentiate** |
| Family dialect choice / family words | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Grandparent/family voice recording | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** (signature) |
| Two-generation co-play games | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | **Differentiate** |
| Songs | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | partial | **Parity** (calm arrangements) |
| Video shows | ✓ | ✗ | ✓ | ✗ | partial | ✓ | ✗ | **Reject as core** (passive; stimulation); short captioned song clips only |
| Pronunciation scoring | partial | ✓ | ✗ | ✗ | partial | ✗ | ✓ | **Reject** accent scoring; listen-and-compare instead |
| Streaks / hearts | partial | ✓ | ✗ | ✗ | partial | ✗ | ✓ | **Reject** |
| Parent progress | ✓ | n/a | ✗ | ✗ | ✓ | ✓ | ✓ | **Parity** |
| Many languages | ✗ (English) | ✓ | ✗ | ✓ (30+) | partial | ✓ (50+) | ✓ (30+) | **Phase**: ES→PT→others; depth over breadth |
| Local pricing for EFL markets | partial [M] | ✓ | n/a | ✗ | partial | ✗ | partial | **Parity** |

## 4. Recommended feature set

| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| TWO-01 | **Word Pairs play** ★ | Themed "word worlds" (kitchen, park, body, animals, family, feelings): tap an object → hear it in both languages (order set by family: home-first or English-first); 3 calm game types (find it, which one, sort by colour), all tap-only. | Vision; Lingokids breadth [V] | Differentiate | MVP | Must |
| TWO-02 | **Family Voice (grandparent recordings)** ★ | Invite grandparents by link/WhatsApp; they record words (guided list) and short stories in their own voice from their phone; the child hears "Abuela says: *cuchara*". Private to the family. | Vision; no competitor [I] | Differentiate | MVP | Must |
| TWO-03 | **Family dialect & words** | Choose a Spanish variety (e.g., Mexican, Caribbean, Rioplatense) for defaults; replace any word with the family's word ("popote" vs. "pajita"). | Dialect respect [I] | Differentiate | MVP | Must |
| TWO-04 | **Two-generation games** ★ | Simple games designed for video calls or sitting together: "I spy" in two languages, picture bingo with printable cards, "who says it?" (child guesses whose recorded voice). | Vision co-play across generations | Differentiate | MVP | Should |
| TWO-05 | **Songs & rhymes (bilingual)** | 20 traditional and original songs, calm arrangements, captions in both languages. | Lingokids/Studycat songs [V/M] | Parity | MVP | Must |
| TWO-06 | **Listen & Compare (no scoring)** | Child can say the word; app plays back the child's attempt next to the model (on-device, not stored) so they can hear both. No score, no "wrong". | Speech-scoring barriers [V]; Lumen P7/P18 | Improve | MVP | Should |
| TWO-07 | **Family Language Plan** | 3-question set-up: who speaks what, when (e.g., "Spanish at dinner, English at school"); gives 2 daily co-play ideas. | Babble Buddy synergy; JME | Differentiate | MVP | Should |
| TWO-08 | **Weekly summary (both languages)** | Words met/used in each language; Family Voice listens; tip for the week. Parent UI in either language. | Research paper need #7 | Parity | MVP | Must |
| TWO-09 | **EFL mode (MX/BR)** | Same product with English as the target and Spanish/Portuguese UI for parents; local pricing. | EFL WTP [M] | Parity | MVP (ES→EN) / V1 (PT→EN) | Must |
| TWO-10 | **Accessibility & sensory** | Captions in both languages; speech rate control; Calm default; haptics; switch; large-type grandparent mode. | Lumen P2/P4/P7 | Lumen | MVP | Must |
| TWO-11 | **Printable word cards** | Bilingual picture cards for fridge/labelling the home. | Screen-free need | Differentiate | MVP | Should |
| TWO-12 | **Picture stories in two languages** | Short read-aloud stories with language toggle per page; links to Story Lantern bilingual shelf. | Vooks Spanish titles [V] | Parity | V1 | Should |
| TWO-13 | **More heritage languages** | Tagalog, Vietnamese, Mandarin, Arabic, Haitian Creole, Hindi: human-authored, community-reviewed. | Dinolingo/Gus breadth [M] | Improve | V2 | Could |
| TWO-14 | **AI word-set suggestions** | Suggests next word worlds from the family's routines and recordings; human-curated word lists only. | Vision AI role | Improve | V1 | Should |
| TWO-15 | **Dual-language classroom pack** | Teacher shares weekly word worlds with families; family recordings stay private. | Ms. Rivera persona | Differentiate | V2 | Could |

★ **Signature features:** Word Pairs (TWO-01), Family Voice (TWO-02), Two-generation games (TWO-04). **MVP = TWO-01 to TWO-11 (11 features).**

## 5. Core experience & key user flows

**Core loop.** Open → Now/Next/Done ("Kitchen words → Song → Game with Abuela's voice → Done") → play 8–12 min → ending with a real-world task ("Name 3 things in the kitchen in Spanish tonight") → done.

**Flow 1: Onboarding (≤5 min).** Price/privacy → languages at home, dialect, who speaks what (Family Language Plan) → child age → invite a grandparent (optional; send link) → first word world.

**Flow 2: Core session.** Kitchen scene (real photos) → child taps a spoon → "*cuchara*… spoon" (order per family plan) → Family Voice badge on words Abuela recorded ("Abuela says it!") → "Which one is *vaso*?" (tap choice) → song → warning → ending card.

**Flow 3: Grandparent recording.** Grandparent opens link (no app install on Android via web recorder, V1; app for MVP) → large-type Spanish UI → "Say: *cuchara*" (shows picture) → record/re-record/keep → optional "Tell a 1-minute story" → done. Voice-guided throughout.

**Flow 4: Parent view.** Weekly summary in the parent's preferred language; manage recordings; dialect and family words.

**Flow 5: My Needs.** Sensory Dial, captions (both languages), speech rate, input, grandparent large-type mode.

**Flow 6: Billing.** Family Hub standard; local pricing where launched.

**Information architecture.** Child: Word worlds · Songs · Games (Family Voice appears inside, not as a separate tab). Parent (gated): Week · Family Voice · Language Plan · Settings. Grandparent: Record · Listen · Play together.

**Session design.** Default 10 min (range 5–20); warning at T-2 min; designed ending with a real-world language task.

## 6. Inclusive, accessible & sensory design spec

**Sensory Dial defaults.** Calm for 3–4; Balanced for 5–7.

| Level | Behaviour |
|---|---|
| Calm | Real photos, slow cross-fades; voice only; soft chime on choices; no background music |
| Balanced | Gentle animation on tap; song snippets between activities only |
| Lively | Animated scenes (no flashing); music in songs section |

**Input modes.** Tap (all tasks), switch scanning, Voice Control, optional speech (Listen & Compare, never required), AAC symbols for choices. Grandparents: voice-first recording with single large record button.

**Targets.** ≥2.5 cm (3–4), ≥2 cm (5–7); grandparent UI buttons ≥56 dp.

**Reading & typography.** Words shown in both languages with clear colour-plus-position coding (not colour alone); accents and ñ/ç rendered correctly at large sizes; parent/grandparent UI in the parent's language with read-aloud.

**Audio.** Human native-speaker recordings per dialect; speech rate 0.75–1.25×; captions in both languages; visual + haptic twins.

**Culture & identity.** Families, foods, homes from the actual communities (commissioned photography); no stereotypes; community reviewers per language; ND and disabled children represented (P16).

**Age-respectful themes.** "Photo" and "Picture book".

**Lumen principles.**

| P# | Acceptance criterion |
|---|---|
| P1 | Calm default for 3–4; Reduce Motion honoured |
| P2 | Captions in both languages for 100% of audio |
| P3 | Same activity structure each session; strip visible |
| P4 | Tap-only completion for all tasks |
| P5 | Adult text ≤ grade 5 [E] in either language; audio available |
| P6 | BDA defaults incl. diacritics legibility |
| P7 | Tap, switch, voice (optional), AAC |
| P8 | No wrong-answer sounds; no pronunciation scoring |
| P9 | Designed ending; no autoplay |
| P10 | Grandparent join by link; no passwords |
| P11 | No timers |
| P12 | Language settings portable (shared with Babble Buddy/Story Lantern) |
| P13 | Two themes |
| P14 | First session ≤5 min; grandparent first recording ≤3 min |
| P15 | Word collection = learning; no streaks |
| P16 | Community and ND review |
| P17 | No claims of fluency; "supports home-language exposure" |
| P18 | Recordings private; no training; child attempts not stored |

**Target Lumen audit score:** ≥22/24.

## 7. AI specification & guardrails

**What AI does.** (V1) Word-set suggestions from curated lists based on routines and recordings; (MVP) on-device playback for Listen & Compare (signal processing, not scoring); optional constrained speech recognition to detect *that* the child said the target word (for encouragement only) with per-language/per-accent evaluation; TTS only as a fallback where no human recording exists, clearly labelled.

**What AI does not do.** No accent or pronunciation scores; no conversational agent or talking character that befriends the child; no voice cloning of grandparents (even if requested; deepfake and consent risks); no machine translation shown to children without human review; no training on family recordings.

**Pedagogical policy.** Frequent, meaningful, joyful exposure to both languages; family as the main language model; words taught in context (routines, family); no language hierarchy.

**Safety.** All word lists, songs and stories human-authored and reviewed by native-speaker editors per dialect; grandparent recordings are private (family access controls; no public sharing); moderation not required (no user-to-user contact outside the family).

**Evaluation.** Listen & Compare usability; per-dialect recognition checks if detection is used (false-reject ≤8% per group [E]; otherwise disabled for that group); content review sampling 100% at MVP.

**Cost and latency [E].** Mostly content delivery; storage for recordings (~1 MB per word set per grandparent); negligible AI cost.

## 8. Data, privacy & compliance
**Data inventory.** Family languages/dialect; child profile; progress events; grandparent recordings (adult voice, encrypted, family-only; deleted on request or on account closure); child speech attempts (on-device, transient). International data: Mexico (LFPDPPP) [M], Brazil (LGPD, with specific rules for children's data) [M], EU/UK GDPR-K if launched.
**Regimes.** COPPA 2025; LGPD/LFPDPPP for EFL markets [M]; UK AADC; state AADCs; Apple Kids/Google Families.
**Consent.** Parent consent; grandparents consent to their own recordings being stored (adult consent, easy-read, in their language); separate consent for any use beyond the family (none planned).

## 9. Monetization & go-to-market

| Tier | Price | Includes |
|---|---|---|
| Free | $0 | 3 word worlds, 5 songs, Family Voice for those worlds |
| Family plan (US) | ≈$9.99/mo or $69/yr (7 apps) | All worlds, games, stories, Language Plan |
| EFL local plan (MX/BR) | To test: ≈MXN 79–99/mo; ≈BRL 24.90–34.90/mo [E] | Two Words + Story Lantern EN shelf |
| Grandparent gift | Annual gift card | |

Benchmarks: Lingokids ≈$79.99–99.99/yr; Duolingo freemium; PBS KIDS free; Gus/Dinolingo/Studycat subscriptions [V/M].

**Channels.** US: Spanish-language parenting media and creators, Hispanic-serving libraries, dual-language pre-K; grandparent gifting. MX/BR: EFL preschools, parenting creators, local app-store featuring.

**ASO.** "Spanish for kids", "bilingual kids app", "learn English kids" (ES/PT listings), "abuela", "heritage language". Accessibility Nutrition Label as per Lumen.

**Launch.** Test markets: US (heritage ES), Mexico and Brazil (EFL) per the vision's smoke test.

## 10. Success metrics
- **North-star:** weekly two-language play moments (target ≥3 per active family [E]).
- **Inputs:** % families with ≥1 grandparent recording (target ≥40% [E]); words met per language; songs played; two-generation games played.
- **Guardrails:** Sensory Comfort ≥4/5; child's home-language use reported stable or rising (parent survey); zero billing complaints; no pronunciation-anxiety reports.
- **Outcomes:** receptive vocabulary in both languages (picture-pointing probe) pre/post 8 weeks; parent-reported home-language use; E4 → E3.
- **Retention:** D30 30% [E]; strong seasonality around visits to grandparents [I].

## 11. Validation plan

**Riskiest assumptions.**
1. Families will pay for heritage language, as opposed to EFL (vision).
2. Grandparents will record (tech confidence, consent comfort).
3. Children engage more when the voice is a family member's.
4. Local EFL pricing makes unit economics viable.

| # | Method | Sample | Success | Kill / rethink |
|---|---|---|---|---|
| E1 | **Landing-page smoke tests**: US Spanish heritage vs. Mexico & Brazil EFL, price variants | ≥1,500 visitors per market | ≥8% waitlist in ≥1 market; ≥30% choose paid | Heritage <3% → EFL-first product; both <3% → kill/merge into Story Lantern bilingual shelf |
| E2 | **Grandparent concierge**: grandparents record 20 words via WhatsApp voice notes; team assembles a clickable prototype | 15 families (≥5 grandparents 70+) | ≥70% of grandparents complete 20 words; ≥4/5 comfort | <40% → simpler "one word a day" prompts |
| E3 | **Family-voice vs. studio-voice** engagement (prototype) | 12 children | Family voice ≥ studio voice on engagement and request-to-replay | No difference → keep feature as emotional value, not core |
| E4 | **Van Westendorp by market** | n≈300 US + 300 MX + 300 BR parents | Planned local prices within range | Out of range → adjust or B2B-first in that market |

**Mapping.** E1 → WP5 smoke tests (L1); E2 → WP4 concierge; E3 → WP4 prototype tests; E4 → WP2 survey / WP5.

## 12. Build handoff

**Epic TWO-E1: Word worlds.**
- **Given** the family plan is "Spanish first", **when** the child taps an object, **then** Spanish plays first, then English, each with captions.
- **Given** the family replaced "pajita" with "popote", **then** every occurrence uses "popote" and the family's recording if present.

**Epic TWO-E2: Family Voice.**
- **Given** a grandparent opens an invite link, **then** the recording UI appears in their chosen language with one large record button and a picture of the word.
- **Given** a recording is saved, **then** it is encrypted, visible only to family members, and never used for training (flag enforced server-side).
- **Given** a parent deletes a recording, **then** it is removed from all devices at next sync and from storage within 30 days.

**Epic TWO-E3: Listen & Compare.**
- **Given** the child records an attempt, **then** playback shows two buttons ("You", "Abuela/Model") with no score, and the attempt is discarded when the screen closes.

**Epic TWO-E4: Sessions & endings.** **Given** 10 min default, **then** a warning appears at 8 min and the session ends with a real-world task card.

**Epic TWO-E5: EFL mode & local billing.** **Given** Brazil storefront, **then** prices display in BRL before any trial, with one-tap cancel.

**Non-functional.** Offline for downloaded worlds and recordings; iOS/Android; grandparent web recorder (V1); WCAG 2.2 AA in all UI languages; ES/EN/PT; correct diacritics and RTL readiness (for V2 Arabic); encrypted media; zero third-party SDKs.

**QA focus.** AT matrix in each UI language (VoiceOver/TalkBack language switching mid-sentence, captions, switch). Sensory A/B. AI safety: no voice cloning path; TTS fallback labelled. COPPA/LGPD: consent records for grandparents, deletion. Billing: local currency, reminders, cancel.

**Platform dependencies.** Lumen; My Needs (languages, captions); Family Hub (grandparent seats, recordings, billing across currencies); localisation pipeline with native-speaker review; privacy stack (media vault).

## 13. Risks & open questions

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Low heritage WTP | M | H | E1 kill/pivot to EFL; free core as community value |
| Grandparents don't record | M | M | WhatsApp-style simplicity; one word a day; parent can record for them |
| Dialect disputes/content errors | M | M | Family word override; native-speaker editors per variety |
| Lingokids price competition in EFL | H | M | Calm, family voice, local price; library/school channels |
| Competitor data gaps [M] | H | L | WP1 verification |

**Open questions.** Should Two Words launch EFL-first in Brazil/Mexico if heritage WTP is weak? Merge with Babble Buddy's home-language mode for 1–3? Which second heritage language has the strongest community partners?

## 14. Sources
- [V] Lingokids data: [raw 01](../../../research/raw/01-google-play-top30.md), [raw 02](../../../research/raw/02-apple-app-store-top30.md), [raw 03](../../../research/raw/03-forum-voice-of-customer.md) (incl. Trustpilot https://www.trustpilot.com/review/lingokids.com and https://play.google.com/store/apps/details?id=es.monkimun.lingokids)
- [V] Duolingo 2025–26 figures and complaints: [Research paper §3–§5](../../01-research-paper.md)
- [V] PBS KIDS Games bilingual games: https://apps.apple.com/us/app/pbs-kids-games/id1050773989 (via raw 02)
- [V] Vooks Spanish titles: https://info.vooks.com/vooks-pricing-plans
- [V] Speech-scoring barriers: [Research paper §6](../../01-research-paper.md)
- [M] EFL WTP in LatAm/Asia: [raw 05](../../../research/raw/05-market-and-trends.md)
- [M] Gus on the Go, Studycat, Rosetta Stone Kids, Dinolingo, Mondly Kids; third-generation language shift; LGPD/LFPDPPP children's-data rules: to verify in WP1

## 15. Reevaluation & enhancements (v1.1)

> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.
> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).

| | |
|---|---|
| **Verdict** | Re-scope → Family Voice & Languages layer (SX-07) + a stand-alone EFL SKU (MX/BR) |
| **Ships in** | Lanternling app (S1) |
| **Build wave** | 2 |
| **Pre-discovery priority score** | 65/100 [I] |
| **Consumes engines** | EN-07 |
| **Studio features used** | SX-07, SX-24, SX-26, SX-32 |

### 15.1 Trimmed MVP (app-specific features only)
**MVP = TWO-01, TWO-02, TWO-04, TWO-07.** All other §4 MVP items move to V1, **unless the platform provides them**:
- My Needs and Sensory Dial come from EN-02.
- Weekly summaries are replaced by the Family Digest (SX-04).
- Sharing and roles come from EN-01 and the Pro Console (SX-30).
- Fair billing comes from the Family Pass (SX-01).
- Safety comes from EN-12.

Acceptance criteria for the retained items stay as written in §12.

### 15.2 New features
| ID | Feature | Description |
|---|---|---|
| TWO-E1 | **Record by link or phone** | Grandparents record words from a link or a phone call, with no app install (SX-26). |
| TWO-E2 | **Community heritage packs** | Native-speaker-reviewed heritage-language packs added through the Content Studio (SX-32). |

### 15.3 New validation question
Heritage (US) vs EFL (MX/BR) willingness to pay: smoke test in WP5.

### 15.4 Score breakdown [I]
| Problem severity (20) | Desirability (15) | Inclusivity (15) | Outcome potential (10) | Viability (15) | Feasibility (10) | Differentiation (10) | Platform leverage (5) |
|---|---|---|---|---|---|---|---|
| 3 | 3 | 4 | 3 | 2 | 4 | 4 | 4 |

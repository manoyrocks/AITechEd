# Curiosity Circle: App Strategy & Product Specification

> **Venture:** Evergrow · **App #:** 7/7 · **Ages:** 55+ (open to all adults) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/04-evergrow-adults.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Evergrow index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research caveat:** The session's web-search budget was used up before the lifelong-learning competitors could be re-checked, and direct fetches were blocked by the egress proxy. Figures below come from the studio's earlier store and forum research (repo, originally [V]/[V2]) or from memory [M]. All [M] items must be verified in Discovery WP1.

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | Learn something you love (Italian for travel, guitar again, local history, your family's story) in a small, friendly group led by a real person, with captioned live sessions, an AI study buddy between them, and no timers. |
| **Primary user / buyer** | Users: adults 55+, many retired or semi-retired, some with hearing or vision changes; open to all ages. Buyers: the learner (B2C); libraries, senior centres, OLLI-style programmes and senior living (B2B2C); later MA plans (social-engagement supplemental benefits); family gifting. |
| **Core job-to-be-done** | "When I have time and curiosity but I'm alone more than I'd like, I want to learn something meaningful with other people at a gentle pace, so I keep my mind engaged and make real connections." |
| **Category on the stores** | Education (secondary: Social / Lifestyle) |
| **Top competitors** | GetSetUp, The Great Courses (Wondrium), MasterClass, Coursera, Babbel, Simply Piano, Yousician, Elevate, Lumosity, BrainHQ, Ancestry/FamilySearch, OLLI programmes (Osher Lifelong Learning Institutes) |
| **Our wedge** | 1) **Small human-hosted cohorts (8–12)** where people get to know each other, unlike video libraries (MasterClass, Great Courses) or solo apps (Babbel, Simply Piano). 2) **Unhurried and accessible by default**: captions, large type, no timed games (unlike Lumosity/Elevate/BrainHQ). 3) **Honest claims:** engagement and connection, **never dementia or brain-age claims** (FTC Lumosity precedent). |
| **Business model** | B2C per circle ($59–99 for 6–8 weeks) or membership $19/mo (one circle at a time + open events). Partner licences for libraries, senior centres and senior living. Gift cards. |
| **North-star metric** | Circle members who attend ≥75% of sessions *and* re-enrol in another circle within 60 days |
| **MVP candidate?** | **Pilot now (concierge cohorts via libraries); app later (Year 2–3).** |

## 2. Problem & users
**Problem statement**
- **Isolation and disengagement are common and consequential.** The 2024 Lancet Commission lists social isolation and hearing loss among 14 potentially modifiable dementia risk factors [M] (repo raw/05). We cite this only as context for the *need*. We make no claim that our product reduces risk (§7).
- **Brain games have credibility and design problems for this group:**
  - Lumosity paid $2M to settle FTC deceptive-advertising charges (2016) [V] (repo raw/04).
  - Reviewers conclude Lumosity's "benefits are largely confined to the tasks within the app" [V] (repo raw/03).
  - Timed tasks exclude slower processors, motor-impaired users and screen-reader users (repo raw/04).
  - BrainHQ has the strongest evidence base (200+ papers claimed) but is still solo and timed [V] (repo).
- **The best "lifelong learning" content is solo video.** The Great Courses/Wondrium and MasterClass are lecture libraries [M]. Coursera/Udemy are career-oriented [V] (repo). Babbel is solo and tops out at B2 [V2] (repo). Simply Piano charges ~$119.99–169.90/yr individually [V] (repo), with no people.
- **In-person programmes prove demand but are capacity- and geography-limited.** OLLIs run member-led courses for 50+ learners at universities across the US [M]; GetSetUp proves online peer-led live learning at scale [V] (repo).
- **Accessibility gaps.** Seniors report small type and fast pacing. Hearing loss is common in later life [M]. Live video classes without captions exclude people like Gloria (vision persona).

**Personas**
1. **Gloria, 66, retired teacher with hearing loss** (vision). Loves history and languages; wants company. She needs reliable captions, a host who repeats questions, and chat participation.
2. **Harold, 74, widower, amateur genealogist, early-stage Parkinson's (tremor, soft voice).** Wants to finish his family history and meet people. He needs large targets, a text chat instead of speaking up, no timers, and help reading old records.
3. **Janelle, 58, activities director at a senior-living community (buyer/host).** She wants engaging programmes beyond bingo, easy to run, that residents with a range of abilities can join, plus attendance data for families and leadership.

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Belonging and connection | Isolation evidence [M]; GetSetUp peer model [V] (repo) | Small consistent cohorts with a human host |
| Meaningful learning, not "brain age" | Lumosity transfer and FTC [V] (repo) | Real subjects: languages, music, history, genealogy |
| Unhurried, accessible | Timed-game exclusion (repo raw/04) | No timers, captions, large type, slow pacing |
| Something to show | Legacy motivation [I] | Circle projects (family-history book, recital, trip phrasebook) |
| Practice between sessions | Retention in cohort learning [I] | AI study buddy + recap |
| Trustworthy claims | FTC precedents (repo) | Claims register; engagement-only language |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **GetSetUp** | GetSetUp | 5,000+ live classes; partner distribution [V] (repo) | Free via partners / subscription [V] (repo) | 4.8 [V] (repo) | Peer guides, live, social, 4 languages | Little independent discussion (repo) | No download; pace set by guides | repo raw/03 |
| **The Great Courses / Wondrium** | The Teaching Company | Long-running lecture brand [M] | Subscription ~$20/mo or annual [M] | n/a | Expert professors; depth | Solo, passive; no community [I] | Captions/transcripts on many courses [M] | [M] |
| **MasterClass** | MasterClass | Just outside the US top 30 by volume (repo raw/02) | ~$120–240/yr tiers [M] | 4.7+ [M] | Celebrity instructors; production value | Inspirational, not practical; annual billing complaints [M] | Captions [M] | repo raw/02; [M] |
| **Babbel** | Babbel GmbH | 50M+ Play; top-5 grossing Android education (repo) | $17.99/mo; $89.99/yr; lifetime $299 (repo) | 4.7 (repo) | Structured, calm UI suits older users (repo) | Tops out at B2; consumer live classes closed Jul 2025 [V2] | Calmer UI (repo) | repo raw/01–02; [strommeninc](https://strommeninc.com/why-babbel-live-shut-down-and-what-to-use-instead-2025/) |
| **Simply Piano / Yousician** | Simply (JoyTunes); Yousician | Simply Piano 50M+ Play; 4.7 (~853K) [V] (repo); Yousician near the top 30 [V] (repo) | Simply Piano ~$119.99–169.90/yr individual (repo); Yousician subscription [M] | 4.7 (repo) | Instant feedback via mic; song library | Expensive renewals (repo); timing-based scoring | Mic-based listening excludes hearing-impaired users (repo) | repo raw/02, app-catalog |
| **Elevate / Lumosity / BrainHQ** | Elevate Labs; Lumos Labs; Posit Science | Elevate 10M+, 4.8 [V] (repo); BrainHQ 200+ papers claimed [V] (repo) | Elevate $39.99/yr, lifetime $139.99+ (repo); BrainHQ/Lumosity $8–14/mo (repo) | 4.6–4.8 (repo) | Daily habit; polished | Timed games; transfer doubts; Lumosity FTC $2M (repo) | Timers exclude many seniors (repo) | repo raw/01–05 |
| **Ancestry / FamilySearch** | Ancestry; FamilySearch (nonprofit) | Market leaders in genealogy [M] | Ancestry subscription + DNA kits [M]; FamilySearch free [M] | n/a | Huge record collections; hints | Paywalls (Ancestry); overwhelming for beginners [M] | Dense UIs; handwriting in old records hard to read [I] | [M] |
| **OLLI programmes** | Osher Lifelong Learning Institutes (university-based) | Nationwide network for learners 50+ [M] | Low annual membership + course fees [M] | n/a | Peer community, university setting | Local only; waitlists; limited online accessibility [M] | Varies by campus | [M] |

### Feature matrix
| Feature | GetSetUp | Great Courses | MasterClass | Babbel | Simply Piano | Lumosity/Elevate | OLLI | **Our decision** |
|---|---|---|---|---|---|---|---|---|
| Small consistent cohort (same people weekly) | partial | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Differentiate** online + hybrid |
| Human host/teacher | ✓ | ✓ (recorded) | ✓ (recorded) | ✗ (B2C) | ✗ | ✗ | ✓ | **Parity** (live) |
| Practice between sessions | ✗ | ✗ | partial | ✓ | ✓ | ✓ | ✗ | **Improve:** AI study buddy tied to the circle |
| Captioned live sessions | partial | n/a | n/a | n/a | n/a | n/a | partial | **Differentiate:** human-corrected captions |
| Timed games / speed scores | ✗ | ✗ | ✗ | ✗ | partial | ✓ | ✗ | **Reject** |
| "Brain age" / dementia-prevention claims | ✗ | ✗ | ✗ | ✗ | ✗ | partial (history) | ✗ | **Reject** (FTC Lumosity) |
| Creative/legacy project output | ✗ | ✗ | partial | ✗ | partial (songs) | ✗ | partial | **Differentiate** |
| Genealogy research help | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | partial | **Differentiate** (AI help reading records, human-verified) |
| Streak mechanics | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ | **Reject** → attendance is its own reward; gentle weekly goals |
| Annual auto-renew without reminder | ✗ | partial [M] | partial [M] | partial | partial (repo) | partial (repo) | ✗ | **Reject** |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| F1 | **Circles** ★ signature | 8–12 people, the same host, 6–8 weekly 60-minute live sessions (online, hybrid at a library, or in a senior-living room). Launch topics: Italian for travel, Spanish refresh, guitar/ukulele again, local history, family history/genealogy, "AI for curious minds". | OLLI/GetSetUp proof [V] (repo)/[M] | Differentiate | MVP | Must |
| F2 | **Captioned live room** | Video room with human-corrected live captions (CART for partner cohorts; high-quality ASR plus host correction otherwise), speaker names, dial-in audio, chat, raise-hand button, no download (browser/app) | Gloria persona | Lumen | MVP | Must |
| F3 | **Study Buddy (AI)** | Between sessions: practice aligned to this week's session (Italian phrases, chord changes explained, history quiz as conversation), in voice or text. Labelled AI; not a companion. | Vision | Differentiate | MVP | Must |
| F4 | **Recap & Replay** | After each session: captioned recording, a transcript, and a short recap drafted by AI and **approved by the host** | Memory support (P10) | Improve | MVP | Must |
| F5 | **Circle Wall** | Small private space for the cohort to share photos, questions and progress (moderated by the host) | Connection | Differentiate | MVP | Must |
| F6 | **Legacy Projects** | Each circle ends with a shareable output: a family-history booklet, a recorded mini-recital, a trip phrasebook, a local-history walking tour | Meaning; family sharing | Differentiate | MVP | Should |
| F7 | **Host toolkit** | Session plans, accessibility checklist (repeat questions, describe visuals), attendance, gentle check-ins with absent members | Janelle; quality | Parity | MVP | Must |
| F8 | **Accessible sign-in + 60+ preset** | Passkeys, library-card link, helper-assisted set-up (with consent); large type by default | WCAG 3.3.8 [V] (repo) | Lumen | MVP | Must |
| F9 | **Claims register & honest copy** | All marketing mapped to evidence tiers; no brain/dementia claims | P17; FTC | Lumen | MVP | Must |
| F10 | **Fair billing** | Price per circle upfront; membership pause; gift cards that never auto-bill the recipient | Charter | Lumen | MVP | Must |
| F11 | Genealogy helper | AI helps transcribe and translate old handwritten records and suggests search strategies; the learner verifies and the host reviews. Integrates with FamilySearch (free) and exports GEDCOM | Ancestry/FamilySearch complexity [M] | Differentiate | V1 | Should |
| F12 | Music practice feedback | Optional mic-based feedback with a **visual-only** (hearing-impaired) mode and no timing penalties | Simply Piano gap (repo) | Improve | V1 | Could |
| F13 | Hybrid partner mode | Library/senior-living room kit: one screen, room mic, captions on the TV | Partner reach | Differentiate | V1 | Should |
| F14 | Alumni clubs | Monthly open events for past circles (reading club, conversation hour) | Re-enrolment | Improve | V1 | Should |
| F15 | Peer-host pathway | Train experienced members as co-hosts (paid) | Scale; GetSetUp model | Differentiate | V2 | Should |
| F16 | Intergenerational circles | Grandparent + grandchild circles (e.g., family history) with Questwise/Ascendly safeguards | Cross-venture | Differentiate | V2 | Could |

MVP = F1–F10.

## 5. Core experience & key user flows
**Core loop (weekly).** Reminder the day before, in the user's chosen channel and carrying their safe word → join the live session (60 min) → Recap & Replay the next day → 2–3 Study Buddy practices (10 min each, optional) → share on the Circle Wall (optional) → next session. At the end: Legacy Project → invitation to the next circle.

**Flow 1: Onboarding (≤5 min; can be assisted by a librarian or family)**
1. Arrive via a library link, gift card or store.
2. Big-type welcome, with read-aloud optional.
3. Sign in with a passkey or library card.
4. My Needs: text size, captions (default on), "I prefer to type in chat", audio-only option.
5. Browse circles, each shown with day and time in local time, host photo and bio, pace ("gentle"), and accessibility notes.
6. Join and get a calendar invite plus a printable card. First value: a 3-minute welcome video from the host (captioned) and a Study Buddy warm-up.

**Flow 2: Live session**
1. The "Join" button is active 15 minutes early. A tech check offers help from a person.
2. Room: captions on, speaker names, big raise-hand and chat buttons.
3. The host follows the accessibility checklist: repeats questions, describes slides, pauses.
4. Designed end: "Next week: … See you Tuesday."

**Flow 3: Study Buddy practice**
1. Card: "This week: ordering at a trattoria".
2. Voice or text; unlimited time; hints.
3. Summary: "You practised 6 phrases. Your host will say hello to these next week." Optional: share with the host.

**Flow 4: Host / partner console**
- Roster, attendance, gentle check-in message templates for absent members.
- Recap approval queue.
- Accessibility requests (for example "Harold prefers chat").
- Partner view: aggregate attendance and re-enrolment.

**Flow 5: My Needs.** Shared with Silver Circuit; one tap from any screen.

**Flow 6: Billing.** Circle price shown before sign-up. Refund if the learner leaves after session 1. Membership pause. Gifts never auto-renew on the recipient.

**IA.** My Circle · Sessions · Practice · Wall · Explore circles · Help. Large fixed bottom bar with labels.

**Session design.** Live sessions last 60 min with a 5-min stretch break at 30; practice is 10 min; everything is paced by the user outside live sessions.

## 6. Inclusive, accessible & sensory design spec
- **Sensory Dial.** Default **Balanced + High contrast** (60+ preset). Calm: no motion, no sounds, a simple grid in the video room. Lively: warmer theme and a celebration when a Legacy Project is finished. No flashing.
- **Concrete 60+ spec (same baseline as Silver Circuit):**
  - Body text **20 px default** (≥18 px minimum).
  - **≥56 dp targets** (64 dp for Join/Leave/Raise hand/Chat).
  - Contrast ≥7:1.
  - **No timeouts** anywhere.
  - Captions on by default, with speaker labels.
  - Speech rate control for the Study Buddy (0.6–1.2×).
  - Mono audio and hearing-aid streaming via OS routing.
  - Dial-in by phone for audio-only participation.
  - No swipe, drag or long-press requirements.
  - Passkey or library-card sign-in (WCAG 3.3.8).
- **Input modes.** Voice, text chat (full participation path for speech disabilities, soft voices and Harold's Parkinson's), tap, keyboard, switch, Voice Control.
- **Visual access.** Hosts describe visuals; slides provided in advance in large-print and screen-reader-friendly formats; old records (genealogy) zoomable with AI transcription.
- **Hearing access.** CART captioning for partner-funded cohorts; human correction of recording captions within 48 h; a "please repeat" button that sends a quiet signal to the host.
- **Themes.** "Salon" (warm photographic) and "Plain high contrast". Real older adults in imagery; no stereotypes.

| # | Principle | Acceptance criterion in Curiosity Circle |
|---|---|---|
| P1 | Calm | Reduce Motion → 0 animations; video grid never auto-rearranges mid-session (pinned speaker option) |
| P2 | Sound | Captions default on; join/leave chimes off by default; visual cue for new chat messages |
| P3 | Predictable | Same session structure weekly; same host; agenda posted in advance |
| P4 | Targets | ≥56/64 dp; single-tap only |
| P5 | Plain language | UI ≤ grade 6; host materials plain-language checked |
| P6 | Typography | 20 px default; WCAG 1.4.12 passes |
| P7 | Multimodal | Every live interaction possible by chat; every practice by text |
| P8 | Low penalty | No scores in practice; "not today" is fine |
| P9 | Focus | One session per week; no feed algorithm on the Wall (chronological, small group) |
| P10 | Memory | Recap & Replay; agenda and "last time we…" at the top of each session |
| P11 | Timing | No timers in practice; music feedback never penalises tempo by default |
| P12 | My Needs | Profile shared with Silver Circuit; accommodations free |
| P13 | Age-respectful | Adult themes; peer-aged hosts where possible |
| P14 | Helper / host low burden | Host prep ≤30 min per session using templates |
| P15 | Motivation | Attendance is not gamified; no leaderboards; the Legacy Project is the celebration |
| P16 | Affirming | Content reviewed by the 60+ panel for ageism; disability-inclusive examples |
| P17 | Honest claims | 100% of claims in the register; no brain/dementia/"brain age" language |
| P18 | Privacy | Recordings visible only to the circle; members choose whether they appear on video |

**Lumen audit target:** 24/24.

## 7. AI specification & guardrails
**Does**
- **Study Buddy:** LLM practice aligned to the host's session plan (the host selects topics), with ASR/TTS options.
- **Recap drafts** from the session transcript, approved by the host before release.
- **Genealogy helper (V1):** handwriting recognition and translation of old records with confidence flags; suggested search strategies; the learner verifies.
- Captioning (ASR with host correction).

**Does not**
- Act as a companion or friend (connection is with *people*). It reminds users it is an AI and redirects social needs to the circle and host.
- Infer mood, loneliness or cognitive state.
- Invent genealogical facts: every AI-suggested relationship is marked "unverified" until a source is attached.
- Publish recaps without host approval.

**Claims discipline** (FTC §5; the Lumosity 2016 and LearningRx precedents [V] (repo raw/04))
- **Allowed:** "learn with others", "stay curious", "social learning", and "a place to keep learning", plus measured outcomes we actually collect (attendance, satisfaction, self-reported connectedness), each with the evidence tier stated.
- **Not allowed:** "prevents dementia", "keeps your brain young", "improves memory", "clinically proven", "brain age", or any implication of treating MCI/dementia (which also triggers the FDA device boundary).
- Every claim goes through a claims-register review before it is used in stores, ads or partner decks. MA plan materials use the plan's approved language.

**Safety**
- Wall moderation by the host plus a keyword assist.
- Romance/investment-scam prevention in the community: no private DMs between members at MVP; a scam-awareness note links to Silver Circuit's Scam Gym.
- Crisis and self-report escalation shows resources and a host/staff contact.

**Evaluation**
- Captions: WER on older speakers and accents, targeting ≤10% after host correction.
- Recap faithfulness: host-rated ≥4.5/5.
- Genealogy transcription: character error rate on a labelled set of historical records; flag anything under the confidence threshold.

**Cost [E].** Host cost ~$60–90 per session (8–12 people ≈ $6–10 per person per session). AI ~$0.50–1.00 per member per month. CART captioning ~$100–150 per hour when required (partner-funded).

## 8. Data, privacy & compliance
| Data | Purpose | Retention | Where |
|---|---|---|---|
| Account, My Needs | Service | Until deletion | Cloud |
| Session recordings & transcripts | Replay | Circle duration + 90 days | Cloud; circle-only access |
| Wall posts | Community | Circle + 12 months (member-deletable) | Cloud |
| Genealogy data (V1) | Research | Learner-owned; exportable GEDCOM | Cloud; living persons' data minimised |
| Attendance | Host/partner reporting | 24 months; aggregate to partners | Cloud |

**Regimes.**
- FTC §5 (claims, dark patterns) and state ARLs.
- GDPR if UK/EU. Genealogy involves living relatives' data: minimise it and let relatives request removal.
- HIPAA only if an MA plan requires member data exchange; design without PHI.
- ADA for public partners.
- EU AI Act Art. 50.
- Recording consent: all-party consent notices at session start (US state laws) [M].

**Consent.** Recording consent per circle; opt out of appearing in recordings (camera off, voice via chat); separate consent for Legacy Project sharing.

## 9. Monetization & go-to-market
| Offer | Price | Benchmark |
|---|---|---|
| Circle (6–8 weeks) | $59–99 | OLLI course fees [M]; Babbel $17.99/mo (repo) |
| Membership | $19/mo or $179/yr (one circle at a time + alumni clubs) | MasterClass ~$120–240/yr [M]; Simply Piano $119.99+/yr (repo) |
| Partner cohort (library / senior centre / senior living) | $900–1,500 per 8-week circle (up to 12 seats), or annual programme licence | [E] |
| MA plan (V2) | Per-engaged-member | repo raw/05 [M] |
| Gift card | Circle or 3/6/12-month membership | Family gifting |

- **Channels:** library and senior-centre co-hosted pilots (the vision validation test); Silver Circuit graduates; senior-living activities directors; OLLI partnerships (online extension); family gifting; MA plans addressing social isolation (V2).
- **ASO:** "classes for seniors", "learn Italian with others", "genealogy class online", "guitar for beginners over 60". Accessibility Nutrition Label declared.
- **Markets:** US first (EN; Spanish circles in V1); UK (U3A-style partners [M]) in V2.

## 10. Success metrics
- **North star:** members attending ≥75% of sessions **and** re-enrolling within 60 days (target ≥40% of starters).
- **Inputs:** circle fill rate (≥8 of 12 seats); attendance (≥75%); Study Buddy use (≥1 practice/week for ≥50% of members); Wall participation (≥60% post at least once).
- **Outcomes (engagement only, stated honestly):**
  - self-reported connectedness (e.g., a short loneliness scale, used as a *descriptive* measure, not a health claim)
  - learning goals met (host-rated)
  - Legacy Projects completed
  - Evidence plan: pre/post descriptive study in the pilots; any health-adjacent research goes through an IRB with an academic partner, and **any result is published before it is used in marketing**.
- **Guardrails:** Sensory Comfort ≥4/5; caption satisfaction ≥4.5/5 among hard-of-hearing members; zero non-compliant claims; zero billing complaints; zero scam incidents via the platform.
- **Retention:** re-enrolment ≥40%; membership monthly churn ≤5%; cohort completion ≥70% (vs. MOOC 5–15% [M] (repo)).

## 11. Validation plan
**Riskiest assumptions**
1. Enough cohorts fill and members stay beyond the first cohort (vision).
2. Partners (libraries, senior centres) co-host and co-fund.
3. Online captioned cohorts work for hard-of-hearing members.
4. The Study Buddy adds value between sessions without replacing people.

| # | Experiment | Sample | Success | Kill |
|---|---|---|---|---|
| X1 | **3 pilot cohorts via libraries and senior centres** (vision): Italian for travel, family history, guitar again. Existing video tool + CART captions; Study Buddy via Wizard-of-Oz (host-prepared practice sheets + an existing chatbot with a scripted prompt, disclosed) | 3 × 10 learners, 8 weeks | Attendance ≥75%; ≥40% re-enrol; satisfaction ≥4.5/5 | Attendance <50% or re-enrolment <20% |
| X2 | Fill-rate smoke test (landing page with 6 circle topics and prices) | Library newsletters + paid social to 55+ | ≥8% signup; ≥3 topics fill to 8 | <3% |
| X3 | Caption experience study | 8 hard-of-hearing participants within X1 | Caption satisfaction ≥4.5/5; full participation via chat | <3.5 |
| X4 | Partner willingness to pay | 6 libraries/senior centres/senior-living operators | ≥2 commit to paid circles | 0 |
| X5 | Claims message test ("learn together" vs. "keep your mind active") | Landing-page A/B, adults 55+ | Honest framing converts equal or better | Honest framing converts >30% worse (then revisit positioning, not claims) |

**Mapping.** WP2 (15 older adults; library/aging staff; diary of learning moments), WP4 (X1, X3), WP5 (X2, X4, X5).

## 12. Build handoff
**Epic A: Circles & scheduling**
- Given a member in another time zone, then session times always display in their local time with the day written out ("Tuesday 10:00 am").
- Given a circle reaches 12, then the waitlist opens and the host is notified.

**Epic B: Captioned live room**
- Given any live session, then captions are on by default for every member, with speaker names. A dial-in phone number is shown on the join screen.
- Given a member taps "please repeat", then the host sees a discreet indicator. Other members do not.

**Epic C: Recap & Replay**
- Given a session ends, then the transcript is available within 2 h. The AI recap is visible to members only after host approval.

**Epic D: Study Buddy**
- Given a member types instead of speaking, then all practice features are available and progress is identical.
- Given a member expresses loneliness to the Study Buddy, then it responds kindly, suggests the circle's Wall or the host, offers resources if distress is indicated, and does not position itself as a friend.

**Epic E: Claims register**
- Given any store listing or partner deck change, then it cannot ship without a claims-register ID and reviewer sign-off.

**Non-functional requirements**
- Video: low-bandwidth audio-only mode; works on 5-year-old tablets; browser join with no install.
- iOS, Android and web.
- WCAG 2.2 AA plus AAA contrast and timing.
- EN, then ES.
- Security: members-only rooms, waiting room, host controls.

**QA focus**
- AT matrix: VoiceOver/TalkBack in the video room; captions with hearing aids; 200%+ text.
- Sensory: video grid stability.
- AI safety: companion-seeking prompts, fabricated genealogy links, scam solicitations on the Wall.
- Billing: gift cards, circle refunds, membership pause.
- COPPA: only relevant for V2 intergenerational circles (handled by the child ventures' consent flows).

**Dependencies.** Lumen DS (60+ preset), My Needs, voice stack, video/captioning vendor, partner console (shared with Silver Circuit), consent ledger, claims register (evidence engine).

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Circles don't fill | Med | High | Partner co-hosting; waitlist-then-launch; small minimum (6) |
| Host quality and cost | Med | High | Host training; peer-host pathway; partner-funded seats |
| Temptation to make brain-health claims for MA sales | Med | High | Claims register; board-level policy |
| Caption quality insufficient | Med | High | CART for partner cohorts; host correction |
| Community scams (romance/investment) | Low | High | No DMs at MVP; moderation; Scam Gym link |
| Competing with free library programmes | Med | Med | Partner, don't compete: we supply hosts and the platform |

**Open questions.** Which 3 topics fill fastest? Hybrid (in-room + online) or online-only first? Should we partner with OLLIs for online extensions rather than go direct?

## 14. Sources
- Repo (originally [V]/[V2]): research/raw/03 (GetSetUp; BrainHQ/Lumosity transfer; Mayo Clinic Q&A; PMC review), research/raw/04 (FTC Lumosity $2M and LearningRx; WCAG 3.3.8; seniors UX), research/raw/05 (Lancet 2024; MA channel; cohort completion benchmarks), research/raw/01–02 and app-catalog.csv (Babbel, Elevate, Simply Piano, MasterClass, Yousician)
- [V2] Babbel Live consumer shutdown: https://strommeninc.com/why-babbel-live-shut-down-and-what-to-use-instead-2025/
- [M] The Great Courses/Wondrium, MasterClass pricing, Ancestry/FamilySearch, OLLI network, Yousician pricing, recording-consent laws (not re-verified; search budget exhausted and fetches blocked)

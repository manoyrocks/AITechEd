# Silver Circuit: App Strategy & Product Specification

> **Venture:** Evergrow · **App #:** 6/7 · **Ages:** 60+ (designed first for 60–85; trusted helpers of any age) · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/04-evergrow-adults.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md) · [Evergrow index](README.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference
> **Research caveat (read this):** The session's web-search budget ran out before the 60+ competitors could be re-checked, and every direct fetch (FTC, FBI IC3, GetSetUp, App Store) was blocked by the egress proxy. Competitor facts below therefore come from the studio's earlier research (repo, originally tagged [V]/[V2]) or from memory [M]. **Every [M] figure must be verified in Discovery WP1 before it is used externally.**

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | A patient, voice-first, large-type way for older adults to feel confident with smartphones and AI and to spot scams, with live classes led by peer guides and family help that only happens with your say-so. |
| **Primary user / buyer** | Users: adults 60+ with new or under-used smartphones or tablets. Buyers: **public libraries** and **Area Agencies on Aging** (first), **adult children** (gift), senior-living operators, then **Medicare Advantage** plans (supplemental benefit) and AARP-style associations. |
| **Core job-to-be-done** | "When my phone asks me to do something I don't understand, or a message looks suspicious, I want someone patient to show me, at my pace, and a safe place to practise, so I can stay connected and not get fooled, without always calling my daughter." |
| **Category on the stores** | Education (secondary: Lifestyle / Utilities) |
| **Top competitors** | GetSetUp, Senior Planet (AARP/OATS), Oasis Connections, TechBoomers, AARP Fraud Watch Network, Google "Be Scam Ready", Lively (Jitterbug), GrandPad, YouTube senior-tech channels, BrainHQ (for the cognitive-health budget) |
| **Our wedge** | 1) **Scam Gym**: realistic, safe scam simulations (texts, calls, AI voice clones, fake invoices) practised *inside* the app, never on the real phone line. 2) **Voice-first patient helper plus live peer guides**: AI for repetition at any hour, humans for confidence and community. 3) **Consent-based family help**: remote set-up and shared progress only with the senior's explicit, revocable consent. |
| **Business model** | B2B2C licences: libraries/AAAs $3–6k per branch or agency per year; MA plans $1–3 PMPM or per-engaged-member [E]; senior living per resident. B2C gift $9.99/mo or $79/yr. |
| **North-star metric** | Confident tasks per active learner per month (tasks the learner completes independently after learning them), with a scam-spotting accuracy gain |
| **MVP candidate?** | **Yes: Year 1 library pilots** (vision). Concierge/live-class version first, app MVP after Gate 2. |

## 2. Problem & users
**Problem statement**
- **No top learning app targets older adults**, even though Babbel, Elevate and Impulse draw heavily on them. Timed games and small type dominate the top charts [V] (repo: research paper §5, raw/01).
- **Older adults are heard mostly through their adult children.** Forum evidence clusters in "how do I get Mom to use the iPad / avoid scams / stay sharp" posts [M/I] (repo raw/03). The white space the research identified: family-managed set-up, large type, voice-first, and scam-safety literacy [I] (repo).
- **Scams are the sharpest pain.** The FBI's IC3 Elder Fraud Report for 2024 recorded roughly $4.9B in reported losses by people 60+ from about 147,000 complaints [M: verify]. AI voice-cloning makes "grandparent" and impersonation scams more convincing [M]. Older adults are the fastest-growing new AI-user group yet the most worried about scams [M] (repo raw/05).
- **Peer-led live learning works.** GetSetUp runs live classes taught by older-adult Guides, with 5,000+ classes, no Zoom download, 4 languages and a 4.8 rating, distributed via libraries and Area Agencies on Aging [V] (repo raw/03).
- **Hearing and social connection matter.** The 2024 Lancet Commission lists hearing loss and social isolation among modifiable dementia risk factors [M] (repo raw/05). We **do not** make health claims (see §7), but captions, hearing-aid audio and connection are core design needs.
- **Accessible sign-in is a real barrier.** WCAG 3.3.8 (Accessible Authentication) bans memory and puzzle tests without an alternative [V] (repo raw/04). Password resets and two-factor codes copied between apps are common failure points for seniors [I].

**Personas**
1. **Walter, 72, retired machinist** (vision). New smartphone; wants video calls with grandkids and to play guitar again. His daughter worries about scams. He finds tiny text, fast YouTube tutorials and pushy subscriptions annoying.
2. **Rosa, 78, widow with macular degeneration and mild essential tremor; Spanish-first.** She uses large text and VoiceOver partially, and her tremor makes small taps and swipes miss. She needs voice-first Spanish, 64 dp buttons, no swipes, and screen-reader-friendly lessons.
3. **Karen, 47, Walter's daughter (caregiver, gift buyer).** Lives 300 miles away and is the family's tech support. She wants to set things up remotely and know Dad is safer, **without spying on him**.
4. **Ms. Okafor, 55, adult-services librarian (partner/buyer).** Runs "tech help hours" with a queue out the door. She needs a programme she can run with volunteers, loanable to patrons, with simple impact numbers for the library board.

**Needs & wants**
| Need | Evidence | Response |
|---|---|---|
| Patience and repetition without judgement | Vision; forum signal via adult children (repo) | AI helper that repeats indefinitely; "show me again" everywhere |
| Scam confidence | IC3 elder fraud trend [M]; repo raw/05 | Scam Gym simulations + "Is this a scam?" check |
| Human connection | GetSetUp peer model [V] (repo) | Live peer-guide classes (captioned) |
| Family help without loss of autonomy | White space (repo raw/03) | Consent-based Helper access |
| Large type, big targets, no timeouts | Lumen 60+ parameters (repo raw/04) | 20 px default, 56–64 dp, no timeouts |
| Hearing-friendly audio | Hearing-loss prevalence [M] | Captions default on; hearing-aid streaming; slower speech |
| Honest billing | Research: confusing senior subscriptions (repo) | Library-funded; gift plans that don't auto-bill the senior |

## 3. Competitive feature benchmark
| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|
| **GetSetUp** | GetSetUp | 5,000+ classes; partner distribution via libraries, AAAs and states [V] (repo) | Free via partners; subscription option [V] (repo) | 4.8 [V] (repo) | Live classes by older-adult Guides; no download; 4 languages | Little independent discussion; mostly partner evidence (repo) | Peer pace; live captions vary [M] | repo raw/03: https://www.getsetup.io/en-US |
| **Senior Planet** (AARP affiliate, from OATS) | Older Adults Technology Services / AARP | National free programme; online and in-person centres [M] | Free [M] | n/a | Live classes, community, and a tech hotline [M] | Class times fixed; web-first [M] | Human instructors; varies | [M] |
| **Oasis (Connections / tech classes)** | Oasis Institute | Nonprofit community programmes [M] | Low-cost/free [M] | n/a | In-person, local, social | Limited reach; few digital tools [M] | In-person accommodations | [M] |
| **TechBoomers** | TechBoomers | Free tutorial website [M] | Free (ad-supported) [M] | n/a | Step-by-step articles and videos | Ads; not interactive; dated [M] | Web text; video captions vary | [M] |
| **AARP Fraud Watch Network** | AARP | Free helpline and alerts for anyone [M] | Free [M] | n/a | Trained volunteers on a helpline; scam alerts; "Watchdog" content [M] | Not interactive practice [I] | Phone-based help is accessible to many [I] | [M] |
| **Google "Be Scam Ready"** | Google | Launched 2025 as a free interactive game [M] | Free [M] | n/a | Simulated scam scenarios in a game format [M] | Brief; not senior-specific [I] | Web; unknown | [M] |
| **Lively (Jitterbug) / GrandPad** | Lively; GrandPad | Senior-specific phones and tablets [M] | Device + monthly service plans [M] | n/a | Simplified UI; urgent-response buttons (Lively); family-managed tablet (GrandPad) [M] | Locked-in hardware; cost; limited apps [M] | Big buttons, hearing-aid compatible handsets [M] | [M] |
| **BrainHQ** (cognitive-health budget competitor) | Posit Science | 200+ peer-reviewed papers claimed [V] (repo) | $8–14/mo (repo); some MA plan coverage [M] | n/a | Evidence base | Timed tasks; transfer doubts (repo) | Timed exercises exclude slow processors (repo) | repo raw/03, raw/05 |

Also: **YouTube senior-tech channels** (free, huge reach, but fast-paced, ad-interrupted and not interactive [M]), and generic AI assistants built into phones (Gemini, Siri, Copilot) that seniors are starting to use without guidance [I].

### Feature matrix
| Feature | GetSetUp | Senior Planet | AARP FWN | Be Scam Ready | Lively/GrandPad | TechBoomers | **Our decision** |
|---|---|---|---|---|---|---|---|
| Live peer-led classes | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | **Parity** (peer guides) |
| On-demand, patient 1:1 help (any hour) | ✗ | partial (hotline) | ✓ (helpline) | ✗ | partial (agents) | ✗ | **Differentiate:** AI helper + human escalation |
| Interactive scam simulations | ✗ | partial | ✗ | ✓ | ✗ | ✗ | **Differentiate:** voice-clone, invoice, text and call sims, personalised |
| Works on the user's own phone | ✓ | ✓ | ✓ | ✓ | ✗ (own devices) | ✓ | **Parity** |
| Family remote set-up with senior consent | ✗ | ✗ | ✗ | ✗ | ✓ (GrandPad, family-managed) | ✗ | **Improve:** consent-first, revocable, visible to the senior |
| Voice-first navigation | ✗ | ✗ | ✓ (phone) | ✗ | partial | ✗ | **Differentiate** |
| AI-literacy for everyday life (health questions, AI voices, AI search) | partial | partial | partial | ✗ | ✗ | partial | **Differentiate** |
| Timed brain games | ✗ | ✗ | ✗ | ✗ | partial | ✗ | **Reject:** exclusion; FTC claim risk |
| Ads | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | **Reject** |
| Phone-based sales or payment requests | – | – | – | – | partial [M] | – | **Reject:** scam-safe comms charter; we never ask for payment by phone |

## 4. Recommended feature set
| ID | Feature | Description | Rationale | Type | Tier | MoSCoW |
|---|---|---|---|---|---|---|
| F1 | **Voice-guided lessons** | 5–10 minute step-by-step lessons on the learner's own phone: video-calling family, photos, texting, settings for bigger text, using an AI assistant safely, asking AI health *questions* safely (with "check with your doctor" habits). Follow-along mode: "Now tap the green Call button. I'll wait." | Vision; GetSetUp topics [V] (repo) | Differentiate | MVP | Must |
| F2 | **Scam Gym** ★ signature | Safe simulations inside the app: fake bank text, "grandchild in trouble" voice call (AI voice clone, clearly practice), fake tech-support pop-up, gift-card demand, romance and investment scams, deepfake video. Learner decides "scam or safe?" and hears why; the red flags are explained. | IC3 trend [M]; Be Scam Ready gap | Differentiate | MVP | Must |
| F3 | **"Is this a scam?" check** | Learner shares a screenshot or forwards a suspicious message *into the app* (never by giving us account access). The AI explains red flags and suggests safe next steps (call the bank on the number on your card). High-risk cases go to a human guide. Clear disclaimer that it cannot guarantee safety. | Real-world need | Differentiate | MVP | Must |
| F4 | **Peer Guide live classes** ★ | Weekly 45-min classes (captioned, max 20) led by trained older-adult guides; join in 1 tap from the app, or by phone dial-in for audio-only | GetSetUp model [V] (repo) | Parity | MVP | Must |
| F5 | **Patient Helper (AI)** | Voice or text helper that repeats without judgement, explains the screen in plain words and escalates to a human ("I'll ask a guide to call you at a time you choose") | Vision AI role | Differentiate | MVP | Must |
| F6 | **Helper Handshake (family access)** ★ | The senior invites a helper (e.g., Karen) with a big-button consent screen showing exactly what the helper can see and do: progress, suggested lessons, remote set-up of settings. Revocable at any time; the senior gets a notice of every helper action. | Karen persona; vision | Differentiate | MVP | Must |
| F7 | **Accessible sign-in** | Passkey (Face/Touch ID) or a library-card link; helper-assisted set-up with the senior present; no passwords, no copying codes between apps | WCAG 3.3.8 [V] (repo) | Lumen | MVP | Must |
| F8 | **Confidence map** | Progress as "Things I can do now" (for example "Video call Sam ✓"), no scores, no streaks | Lumen P15 | Lumen | MVP | Must |
| F9 | **Large-type 60+ preset (default)** | 20 px body, 56 dp minimum targets (64 dp primary), high contrast, one action per screen | Lumen 60+ | Lumen | MVP | Must |
| F10 | **Scam-safe communications charter** | We never call, text or email asking for payment, passwords or codes; all messages carry the learner's chosen **safe word**; payment only in-app or via the gift giver | Vision ethics | Differentiate | MVP | Must |
| F11 | **Library / partner console** | Enrol patrons, schedule classes, print large-type handouts, view aggregate outcomes for the board | Ms. Okafor persona | Parity | MVP | Must |
| F12 | **Spanish at launch** | Full Spanish UI, lessons, guides and Scam Gym | Rosa persona; GetSetUp 4 languages [V] (repo) | Parity | MVP | Should |
| F13 | Tablet/TV mode | Larger layouts; cast classes to a TV | Seniors' device mix [I] | Improve | V1 | Should |
| F14 | Health-plan edition | MA member onboarding, engagement reporting (no health data), multi-language | B2B2C | Differentiate | V1 | Should |
| F15 | "Call a guide" scheduled 1:1 | 20-min scheduled video or phone help with a peer guide | Human escalation | Improve | V1 | Should |
| F16 | Bridge to Curiosity Circle | "Ready for more? Join an Italian or guitar circle" | Cross-sell (App 7) | Differentiate | V1 | Could |
| F17 | More languages | Mandarin, Cantonese, Vietnamese, Korean, Tagalog | Equity | Parity | V2 | Should |

MVP = F1–F12 (12 features). **Core loop:** lesson or class → practise on own phone → Scam Gym round → confidence map → helper sees progress (if consented) → next class.

## 5. Core experience & key user flows
**Core loop.** Open (big "Today" card) → a lesson (5–10 min) or today's live class → try it on your phone with the helper waiting → one Scam Gym round (3 minutes) → "Things I can do now" updated → goodbye screen with a real-world suggestion ("Call your granddaughter this evening and try the camera flip.").

**Flow 1: Onboarding (≤5 min, can be done with a helper or librarian beside you)**
1. Download from a library QR code, a family invite link, or the store.
2. The first screen is a large "Hello" with a voice greeting (it can be muted) and one question: "Would you like me to talk you through this?" (Yes / No, I'll read).
3. Text size check: "Can you read this easily?" with bigger/smaller buttons.
4. Sign-in: Face/Touch ID passkey, or "My librarian or family member is helping me" (assisted set-up with the senior's confirmation).
5. "What would you like to do first?" with 4 pictures: video call family / spot scams / use AI safely / photos. The first lesson starts. Value at about 4 minutes.

**Flow 2: Follow-along lesson**
1. Now/Next/Done strip: "Step 2 of 5".
2. The helper says and shows the instruction, and waits with **no timeout**.
3. The learner switches to the Phone app and comes back; the lesson remembers where they were.
4. "Did it work?" Yes / Not yet. "Not yet" offers a slower replay, a picture of what the screen should look like, or "ask a person".
5. Done: the confidence map updates. Goodbye screen.

**Flow 3: Scam Gym round**
1. "Practice only. This is not a real message." banner (large, persistent).
2. A simulated text, call or email appears inside a mock phone frame.
3. The learner chooses: "Looks safe" / "Looks like a scam" / "Not sure".
4. Explanation: 2–3 red flags highlighted, with the "what to do" rule (hang up, call back on a known number, never pay by gift card).
5. The rule is added to "My safety rules" (printable).

**Flow 4: Helper Handshake (family view)**
1. The senior taps "Invite a helper", enters or chooses a contact, and sees a big-type consent summary ("Karen will be able to: see which lessons you finished; suggest lessons; change text size on this app. Karen will NOT see: your messages, your bank, your location.").
2. The senior confirms with a passkey.
3. Karen's view: progress, suggested lessons, "set up on Dad's phone" guides.
4. Every helper action triggers a notice to the senior. "Remove helper" is always 2 taps away.

**Flow 5: My Needs (60+).** Always on the top bar as "Aa + ear" icons with text labels. Covers text size, contrast, speech speed, captions, voice on/off, button size and language.

**Flow 6: Billing.**
- Library/plan-funded learners see "Free through Springfield Library" with no payment screens.
- Gift: the buyer pays. The senior is never charged automatically; the renewal decision goes to the gift giver.
- B2C self-pay: price shown upfront; reminders by the learner's chosen channel (always carrying their safe word); cancel with one large button or by letter; annual plans are never auto-upgraded.

**IA.** Five big items, with the same order on every screen: **Today · Lessons · Scam Gym · Classes · Help**. Settings sit under "Aa". There is no hamburger menu.

**Session design.** Default 10 minutes; nothing is timed; a gentle "Would you like a break?" appears after 25 minutes. Every session ends on a goodbye card; nothing autoplays.

## 6. Inclusive, accessible & sensory design spec (60+ first)
**Sensory Dial.** Default **Balanced + High contrast**.
- Calm: no motion at all, narration only.
- Balanced: slow, essential transitions and a soft confirmation tone with a visual check.
- Lively: warmer colours and a short celebration (opt-in).
- No flashing, no parallax, no auto-scrolling text.

**Concrete spec**
| Area | Requirement |
|---|---|
| Text | Body **20 px default** (never below 18 px); headings 26–32 px; scales to 200%+ with OS text size without truncation; line height 1.5; left-aligned; no light-grey text; contrast ≥7:1 for body text (WCAG AAA 1.4.6) |
| Targets | **≥56 dp minimum**, primary buttons ≥64 dp tall and full-width; ≥12 dp spacing; no swipes, long-press, double-tap, pinch or drag for any core action; tremor tolerance (activate on release, ignore brief duplicate taps) |
| Labels | Icon + text on every button; outcome-labelled buttons ("Call Sam", not "OK") |
| Timing | **No timeouts** in lessons, Scam Gym or sign-in; voice input waits until the user says "done" or taps; auto-lock warnings from the OS are explained in lesson 1 |
| Audio | Captions **on by default** for all speech (AI, video, live classes, with human-corrected captions for recordings); speech rate default 0.85× (range 0.6–1.2×); lower-pitch voice option (easier with high-frequency loss) [I]; dynamic-range compression; mono audio; separate sliders for voice and effects; streaming to Bluetooth hearing aids (MFi/ASHA; LE Audio/Auracast when available) via OS routing; no sound-only cues; phone dial-in for live classes |
| Voice | Voice-first but never voice-only; tolerant of slow speech, dysarthria, accents and dentures [I]; "Did you say…?" confirmations with big Yes/No |
| Speech disabilities | Full **text path**: every voice interaction has a typed or tapped equivalent; live classes support chat questions |
| Sign-in | Passkeys, assisted set-up, library card; **no CAPTCHAs**, no passwords to remember, no code copying (WCAG 3.3.8) |
| Memory | Current step always visible; "Where was I?" button; printable large-type summaries |
| Navigation | Linear flows, a persistent Back labelled "Back", the same 5-item bar; no pop-ups except the scam-practice banner |
| Vision | Full VoiceOver/TalkBack support; zoom-friendly; no text in images |
| Motor | Switch Control and Voice Control verified; one-handed use |

- **Input modes.** Tap, voice, keyboard (tablet), switch, Voice Control; the helper can guide by phone call.
- **Age-respectful themes.** "Classic" (warm, photographic, real older adults) and "Plain high-contrast". No cartoons, no "silver" stereotypes, no patronising copy ("You did it, sweetie!" is banned).

| # | Principle | Acceptance criterion in Silver Circuit |
|---|---|---|
| P1 | Calm | Reduce Motion → 0 animations; no autoplay audio except the optional greeting |
| P2 | Sound | Captions default on; 100% visual twins; hearing-aid routing tested |
| P3 | Predictable | Same 5-item bar; step counter on every lesson; no layout shifts |
| P4 | Targets | ≥56 dp minimum, 64 dp primary; single-tap only |
| P5 | Plain language | ≤ grade 6; no jargon without a spoken definition |
| P6 | Typography | 20 px default; WCAG 1.4.12 passes |
| P7 | Multimodal | Every task by tap, voice or text |
| P8 | Low penalty | "Not yet" is normal; no wrong buzzers; Scam Gym mistakes are "good practice" |
| P9 | Focus | One action per screen; goodbye card; no feeds |
| P10 | Memory | Passkeys; persistent step display; "Where was I?" |
| P11 | Timing | Zero timeouts (WCAG 2.2.1/2.2.3) |
| P12 | My Needs | 60+ preset default; free; portable to Curiosity Circle |
| P13 | Age-respectful | Photos of real older adults; copy reviewed by the 60+ panel |
| P14 | Helper low-burden | Family helper connected in ≤5 min |
| P15 | Motivation | "Things I can do now" only; no streaks |
| P16 | Affirming | Content review for ageism by the 60+ advisory panel |
| P17 | Honest claims | No "keeps your brain young"; no "scam-proof" guarantees |
| P18 | Privacy | Helper sees only consented items; no location, no message access |

**Lumen audit target:** 24/24. This app is the studio's 60+ reference implementation.

## 7. AI specification & guardrails
**Does**
- **Patient Helper:** LLM with ASR/TTS, grounded in the lesson library and the device's OS version (help articles curated by humans).
- **Scam Gym:** scenario generation from a human-authored scam taxonomy; synthetic voice-clone demos using **consented, synthetic voices only**, never cloned from the learner's family.
- **"Is this a scam?":** analysis of a shared screenshot or text, using a risk classifier plus LLM explanation.
- Adaptive lesson suggestions.

**Does not**
- Access the learner's messages, bank, email or accounts.
- Make calls or send texts on their behalf.
- Give medical, legal or financial advice. The AI health-question lesson teaches *how* to ask and verify, and to confirm with a clinician.
- Act as a companion. The helper is a labelled tutor, reminds users it is an AI, and does not claim feelings.
- Infer cognitive decline, mood or dementia from voice or behaviour. This is explicitly out of scope (FDA device boundary and FTC §5).

**Scam check safety**
- Output is always "Here's what I notice" plus safe steps, never "This is safe". If the risk is high or the learner is unsure, it offers a human guide callback within 1 business day and points to AARP's Fraud Watch Network helpline and the bank's number from the card [M].
- If the learner says money has been sent, show the immediate steps (call the bank, report to IC3/FTC; ReportFraud.ftc.gov [M]) and offer a human.

**Scam-safe communications (product and operations)**
- We never phone learners unprompted.
- Guide callbacks happen only at times the learner books in-app, and the guide states the learner's safe word.
- Emails and texts never contain payment links for the senior.

**Evaluation**
- WER testing on 60+ voices (70–90 age band, Spanish speakers, dysarthria, hearing-aid users' speech) with the same gates as Speak Freely.
- Scam classifier recall ≥95% on a held-out real-scam corpus, and a "false reassurance" rate of 0 in the red-team set.
- Human review of 5% of helper conversations (consented).

**Cost [E].** ~$0.40–1.20 per active learner per month for AI. Peer-guide classes cost ~$2–4 per attendee per class at 15–20 attendees. Callbacks cost ~$8 each.

## 8. Data, privacy & compliance
| Data | Purpose | Retention | Where |
|---|---|---|---|
| Account, My Needs, language | Service | Until deletion | Cloud |
| Lesson progress, Scam Gym results | Confidence map, partner aggregates | 24 months | Cloud |
| Shared screenshots (scam check) | Analysis | Deleted after 24 h unless the learner saves | Cloud, redaction of account numbers |
| Voice | ASR | Not stored by default | Cloud/on-device |
| Helper relationships and consent log | Family access | Life of relationship + 12 months | Cloud, append-only log |

**Regimes.**
- FTC §5 and state UDAP (claims, dark patterns).
- State auto-renewal laws and the FTC's negative-option rules (fair billing). Note: the federal "click-to-cancel" rule was vacated in 2025 [M], but state ARLs remain, and we exceed them.
- HIPAA only if an MA plan shares member data. Design so that no PHI is needed (eligibility tokens) and sign a BAA if a plan requires it.
- CMS marketing rules for MA supplemental benefits (the plan owns marketing).
- ADA Title II for library/public deployments (web rule compliance dates from 2026 [M] (repo)).
- GDPR if UK/EU.
- EU AI Act Art. 50.

**Consent.** Large-type consent screens read aloud; a separate consent per helper; supported decision-making option (a trusted person helps, but the senior confirms).

**Store.** Rated 4+; not a Kids app; Accessibility Nutrition Label fully declared (VoiceOver, Voice Control, Larger Text, Dark Interface, Differentiate Without Colour, Sufficient Contrast, Reduced Motion, Captions).

## 9. Monetization & go-to-market
| Offer | Price | Benchmark / rationale |
|---|---|---|
| Library / AAA licence | $3,000–6,000 per branch or agency per year (unlimited patrons, 1 weekly class) | GetSetUp partner model [V] (repo); price [E] |
| Senior living | $2–4 per resident per month | [E] |
| Medicare Advantage | $1–3 PMPM or per-engaged-member | Repo raw/05 channel table [M] |
| Family gift | $79/yr or $9.99/mo, paid by the giver | Repo B2C band $8–15/mo [M] |

**Channels (sequenced per vision)**
1. Library pilots (2 branches) and AAAs.
2. Family gifting (adult children, holiday season).
3. Senior living.
4. MA plans (9–18 month cycle).

**Channel risks [M: verify].**
- Federal library funding (IMLS) was cut back and contested in 2025.
- Digital Equity Act competitive grants were cancelled in 2025.
- Library budgets may lean on local and state funds and philanthropy; the plan is to price for local budgets.

**ASO.** "phone help for seniors", "scam protection training", "learn smartphone", "tecnología para mayores". Education category. Screenshots in large type with real older adults.

**Markets.** US (EN/ES) first; UK (libraries, Age UK-style partners) in V1.

## 10. Success metrics
- **North star:** confident tasks per active learner per month (target ≥3).
- **Inputs:** lessons completed per week (≥2); class attendance (≥50% of enrolled weekly); Scam Gym rounds per month (≥4); helper connected (≥40%).
- **Outcomes:**
  - self-rated tech confidence gain ≥1 point on a 5-point scale (Discovery Plan E4)
  - scam-spotting accuracy pre/post on held-out simulations (+20 points)
  - fewer "can you help me with my phone" calls reported by helpers
  - Evidence plan: pre/post in the library pilots (Tier 1); comparison with a waitlist (Tier 2).
- **Guardrails:** Sensory Comfort ≥4/5; task success ≥80% in usability; **zero billing complaints**; zero incidents of the scam check saying "safe" on a real scam; helper-removal requests handled in <1 min.
- **Retention:** 60+ monthly engagement ≥40% (repo raw/05 target); 90-day active ≥50% in library cohorts.

## 11. Validation plan
**Riskiest assumptions**
1. The 60+ payer exists: libraries, MA plans or family gifts (vision; Discovery E3).
2. Seniors are comfortable with voice-first AI (Discovery E4).
3. Scam Gym improves real-world detection without increasing anxiety.
4. Family helpers use consent-based access rather than wanting control.

| # | Experiment | Sample | Success | Kill |
|---|---|---|---|---|
| X1 | **Library pilot** (2 branches): weekly peer-guide class + paper Scam Gym cards + Wizard-of-Oz helper (a volunteer answers by phone/text) | 2 branches × ~20 patrons, 8 weeks | ≥2 libraries agree to pay for year 2; attendance ≥50% | 0 libraries willing |
| X2 | Voice-first usability with Figma prototype + human voice (WoZ) | 15 seniors (incl. 4 with hearing loss, 3 low-vision, 2 tremor, 5 Spanish-first) | Task success ≥80%; confidence +1 point (E4) | <60% success |
| X3 | **Gift-purchase smoke test** aimed at adult children | Landing page, paid social to 35–60 | ≥5% gift-page conversion (E3) | <2% |
| X4 | MA / AAA discovery calls | 5 MA plans / aging agencies | ≥1 plan in active conversation | 0 interested |
| X5 | Scam Gym anxiety check | Within X1/X2 | Detection +20 pts; anxiety item not worse | Anxiety rises by ≥1 point |
| X6 | Helper consent concept test | 8 senior–helper pairs | ≥80% of seniors comfortable; helpers accept limits | Seniors reject |

**Mapping.** WP2 (15 older adults, 8 adult children, 5 library/aging staff; 10-senior diary study of tech moments), WP4 (X2, X5, X6; includes the 3 participants aged 60+ from the accessibility rounds), WP5 (X1, X3, X4; thresholds ≥2 library pilots and ≥1 MA conversation).

## 12. Build handoff
**Epic A: Follow-along lessons**
- Given a lesson step, when the learner leaves the app to try it, then returning resumes at the same step with the instruction visible and read aloud (if voice is on).
- Given any lesson, when there is no input for 10 minutes, then nothing times out, and a gentle "Still here whenever you're ready" appears once.

**Epic B: Scam Gym**
- Given any simulation, then a persistent "Practice only" banner is visible and announced by screen readers, and the simulation never uses the phone's real SMS or call functions.
- Given a voice-clone demo, then the voice is synthetic and labelled, and no family voice is ever cloned.

**Epic C: Scam check**
- Given a shared screenshot, when analysis completes, then output never contains "this is safe" or an equivalent phrase (policy test). A human-callback option is shown for any medium or high risk.

**Epic D: Helper Handshake**
- Given the senior revokes a helper, then helper access ends within 1 minute and the senior sees confirmation.
- Given a helper changes a setting, then the senior receives an in-app notice in large type with an "undo".

**Epic E: Accessibility**
- Given default settings, then body text is ≥20 px, targets are ≥56 dp, captions are on, and contrast is ≥7:1.
- Given VoiceOver, then all core flows are completable (tested with 2 blind seniors).

**Epic F: Billing / comms**
- Given a gift plan ends, then the senior is never charged. The gift giver receives the renewal choice.
- Given any outbound message, then it includes the learner's safe word and no payment link.

**Non-functional requirements**
- Works on phones up to 5 years old.
- Low-bandwidth mode for classes (audio-only).
- iOS, Android, web, and phone dial-in.
- WCAG 2.2 AA plus AAA contrast and timing.
- EN/ES.
- Security: passkeys, anti-account-takeover checks on helper invites.

**QA focus**
- AT matrix: VoiceOver, TalkBack, Switch Control, Voice Control, 200–310% text, hearing-aid streaming (iPhone MFi, Android ASHA), and a tremor simulation.
- Sensory A/B: Calm vs. Balanced.
- AI safety: false-reassurance tests, social-engineering attempts (e.g., a "helper" requesting more access), companion requests.
- Billing: gift expiry, library entitlements.
- COPPA: N/A.

**Dependencies.** Lumen DS (60+ preset), My Needs, voice stack, Skills Passport (optional), consent ledger, partner console (shared with Curiosity Circle).

## 13. Risks & open questions
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Library budgets constrained (federal cuts [M]) | Med | High | Low price; philanthropy; AAAs; gifting |
| MA sales cycles long | High | Med | Sequence libraries and gifting first |
| Scam check gives false reassurance | Low | Very high | Never say "safe"; human escalation; red-team |
| Scam Gym raises fear | Med | Med | Empowerment framing; anxiety guardrail |
| Family helper coercion or elder financial abuse via helper access | Low | High | Minimal helper permissions; no financial access; notices; revocation |
| Peer-guide supply and quality | Med | Med | Guide training programme; pay guides |
| Phones change (OS updates) | High | Med | Lesson versioning per OS; quarterly refresh |

**Open questions.** Should we partner with GetSetUp or Senior Planet rather than build our own classes? Which MA plans have tech-literacy or social-isolation supplemental benefits in the 2027 benefit year? Is TV casting worth V1?

## 14. Sources
- Repo (originally [V]): research/raw/03-forum-voice-of-customer.md, GetSetUp row (getsetup.io; Agency on Aging 4; McKnight's) and the seniors section; research/raw/04 (WCAG 3.3.8, seniors UX, Accessibility Nutrition Labels); research/raw/05 (MA channel economics, Lancet 2024, older-adult AI anxiety); research/raw/01 (Babbel/Elevate/Impulse draw older users)
- [M] FBI IC3 Elder Fraud Report 2024 (loss and complaint figures; verify at ic3.gov)
- [M] AARP Fraud Watch Network helpline; Senior Planet (OATS/AARP); Oasis Institute; TechBoomers; Google "Be Scam Ready"; Lively; GrandPad (search budget exhausted, fetch blocked)
- [M] IMLS and Digital Equity Act funding changes 2025; FTC click-to-cancel rule vacated 2025
- [V2] ASR and atypical speech (applies to older and dysarthric voices): https://www.jmir.org/2025/1/e60520/

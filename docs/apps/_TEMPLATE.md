# {App Name}: App Strategy & Product Specification

> **Venture:** {Venture} · **App #:** {n}/7 · **Ages:** {band} · **Status:** Discovery & Validation (spec only, no code)
> **Parent docs:** [Venture vision](../../vision/{venture-file}.md) · [Lumen UX Framework](../../02-inclusive-sensory-ux-framework.md) · [Research paper](../../01-research-paper.md) · [Discovery plan](../../discovery/discovery-validation-plan.md)
> **Confidence tags:** [V] verified this session (URL given) · [V2] secondary source · [M] from memory · [E] estimate · [I] inference

---

## 1. Summary (one screen)
| | |
|---|---|
| **One-liner** | |
| **Primary user / buyer** | |
| **Core job-to-be-done** | "When I…, I want to…, so I can…" |
| **Category on the stores** | e.g., Education › Kids 5 & Under |
| **Top competitors (by downloads / revenue)** | |
| **Our wedge** | Why we win against those competitors (1–3 bullets) |
| **Business model** | |
| **North-star metric** | |
| **MVP candidate?** | Yes / No / Later (from the vision doc) |

## 2. Problem & users
- **Problem statement:** backed by evidence and cited.
- **Personas:** 2–3, including at least one disabled or neurodivergent persona and one caregiver/teacher persona where relevant.
- **Needs & wants:** a table with columns Need · Evidence · How this app addresses it.

## 3. Competitive feature benchmark (top-selling / top-downloaded apps in this category)
The research must cover **5–8 leading apps** in the same category or topic, on the Apple App Store and Google Play.

| App | Publisher | Downloads / grossing signal | Price | Rating | Features users love | Top complaints | Accessibility / sensory notes | Source |
|---|---|---|---|---|---|---|---|---|

Then add a **Feature matrix**. Rows are features and columns are competitors, marked ✓ / ✗ / partial. The last column shows the **Our decision** for each feature: *Parity*, *Improve*, *Differentiate*, or *Reject (with reason)*.

Features are rejected when they violate Lumen or ethics. Examples: hearts/energy limits, pay-to-win, streak punishment, loot boxes, ads to children, companion personas, emotion recognition.

## 4. Recommended feature set
Prioritize features with MoSCoW, split into release tiers:

| ID | Feature | Description | Rationale (competitor source / user need) | Type (Parity / Improve / Differentiate / Lumen) | Tier (MVP / V1 / V2) | MoSCoW |
|---|---|---|---|---|---|---|

- The MVP should have **8–15 features** and cover at least one end-to-end core loop.
- Mark the **signature feature(s)** that define the product.

## 5. Core experience & key user flows
- The core loop, e.g., open → choose → learn → reflect → natural end.
- 4–6 key flows written as numbered steps: onboarding (≤5 min to first value), the core session, the caregiver/teacher view, the settings/"My Needs" profile, and billing/cancellation.
- **Information architecture:** screens list and navigation model.
- **Session design:** default length, the designed ending, transition warnings.

## 6. Inclusive, accessible & sensory design spec
- **Sensory Dial defaults** (Calm / Balanced / Lively) and what changes at each level in this app.
- **Input modes** supported per task (tap / voice / keyboard / AAC / switch / eye gaze / drawing).
- **Targets and gestures:** sizes for this age band; a drag alternative for every drag.
- **Reading and typography:** reading level, read-aloud, dyslexia settings.
- **Audio:** channels, captions, visual and haptic equivalents.
- **Age-respectful themes.**
- **Applicable Lumen principles P1–P18,** each with its app-specific acceptance criterion.
- **Target score on the Lumen 24-point audit rubric:** ≥22.

## 7. AI specification & guardrails
- **What AI does and does not do.** Include the models or capabilities needed: LLM, ASR, TTS, vision, recommendation.
- **Pedagogical policy,** e.g., the Socratic hint ladder, mastery gating, human-reviewed content.
- **Safety:** no companion persona for minors, disclosure, distress escalation based on self-report, no emotion recognition, content filters, hallucination controls (for example, verified solvers and citations).
- **Evaluation plan:** offline evals, red-teaming, word error rate by speaker group, human review sampling.
- **Cost and latency assumptions [E].**

## 8. Data, privacy & compliance
- **Data inventory:** what is collected, why, retention, and where it is processed (on-device vs. cloud).
- **Applicable regimes:** COPPA 2025, FERPA/SOPIPA, UK AADC, state design codes, EU AI Act (Art. 5 / Annex III / Art. 50), HIPAA, FTC §5, FDA device boundary.
- **Consent flows.**
- **App Store Kids category and Google Families policy requirements,** where applicable.

## 9. Monetization & go-to-market
- **Pricing tiers,** benchmarked against the competitors in §3, and the fair-billing charter.
- **Channels:** B2C, ESA, school, employer, library, clinician, health plan.
- **ASO:** target keywords and category, plus an Accessibility Nutrition Label plan.
- **Launch markets** and localization.

## 10. Success metrics
- **North-star metric,** with 3–5 input metrics.
- **Guardrail metrics:** Sensory Comfort ≥4/5, zero billing complaints, frustration events, and others.
- **Learning or outcome measures,** with an evidence-tier plan.
- **Retention targets:** D1/D7/D30 and DAU/MAU, compared with category benchmarks.

## 11. Validation plan (no-code, discovery phase)
- **Riskiest assumptions,** ranked.
- **Experiments:** method (paper, Figma, Wizard-of-Oz, concierge, smoke test), sample, success and kill thresholds.
- **Mapping** to the Discovery Plan work packages.

## 12. Build handoff (for the agent team, post-Gate 2)
- **Epics** with user stories and acceptance criteria (Given/When/Then) for the MVP.
- **Non-functional requirements:**
  - performance
  - offline
  - platforms (iOS, Android, web)
  - accessibility (WCAG 2.2 AA)
  - localization
  - security
- **QA focus:**
  - assistive-technology test matrix
  - sensory A/B
  - AI safety test cases
  - COPPA test cases
  - billing test cases
- **Dependencies on the shared studio platform:** Lumen design system, "My Needs" profile, AI orchestration, privacy stack, evidence engine.

## 13. Risks & open questions
A table with columns Risk · Likelihood · Impact · Mitigation, followed by the open questions.

## 14. Sources
A list of URLs, each with its confidence tag.

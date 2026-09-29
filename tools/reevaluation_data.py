"""Reevaluation v1.1 data for the 35 app concepts and generator for the
per-app "§15 Reevaluation & enhancements" sections and the summary tables in
docs/03-project-reevaluation.md.

Run from the repo root:  python3 tools/reevaluation_data.py
Idempotent: re-running replaces §15 in each app doc and the generated blocks
between <!-- GEN:... --> markers in docs/03-project-reevaluation.md.

Scores are pre-discovery analyst judgments [I] on a 1-5 scale, weighted with
the Discovery Plan §6 scorecard. They are inputs to Gate 1, not decisions.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Discovery Plan §6 weights (sum = 100)
WEIGHTS = dict(P=20, D=15, I=15, O=10, V=15, F=10, Df=10, L=5)
CRITERIA = dict(
    P="Problem severity", D="Desirability", I="Inclusivity", O="Outcome potential",
    V="Viability", F="Feasibility", Df="Differentiation", L="Platform leverage",
)

SURFACES = {
    "S1": "Lanternling app",
    "S2": "Questwise app",
    "S3": "Ascendly app",
    "S4": "Evergrow Work (B2B)",
    "S5": "Speak Freely",
    "S6": "Evergrow Circle (60+)",
    "S7": "Wavelength app",
    "S8": "Wavelength Voice (AAC)",
    "S9": "Studio Family Hub",
    "S10": "Pro Console (web)",
}

APPS = [
    # ---------------- Lanternling ----------------
    dict(file="lanternling/01-babble-buddy.md", name="Babble Buddy", venture="Lanternling",
         verdict="Keep (lead)", surface="S1", wave="1c",
         mvp=["BB-01", "BB-02", "BB-03", "BB-05", "BB-06", "BB-08"],
         engines=["EN-07", "EN-09", "EN-10"], sx=["SX-04", "SX-06", "SX-07", "SX-25", "SX-26"],
         enh=[("BB-E1", "Hands-free mode", "Moment prompts delivered as audio in the car or kitchen (no screen), via phone audio or smart speaker where platform terms allow for child-directed use."),
              ("BB-E2", "Early-intervention signposting", "When the milestone guide flags a possible concern, show local early-intervention services (e.g., IDEA Part C in the US) and 'talk to your pediatrician' guidance. Never a diagnosis."),
              ("BB-E3", "Remote co-play invite", "A distant grandparent joins a Moment Card by link, via SX-06.")],
         test="Does hands-free delivery raise prompt use (≥4 days/week) versus in-app cards? SMS/audio concierge, n=30.",
         s=dict(P=5, D=4, I=5, O=4, V=3, F=4, Df=5, L=4)),
    dict(file="lanternling/02-tap-and-wonder.md", name="Tap & Wonder", venture="Lanternling",
         verdict="Merge → 'Wonder' toddler mode inside the Lanternling app", surface="S1", wave="2",
         mvp=["TW-01", "TW-02", "TW-03", "TW-04", "TW-13"],
         engines=["EN-02", "EN-07"], sx=["SX-06", "SX-07", "SX-12"],
         enh=[("TW-E1", "Two-touch co-play", "A scene reveals its surprise only when adult and child tap together, making joint media engagement structural."),
              ("TW-E2", "Bedtime handoff", "Sleepy Scene can hand over to Story Lantern Lantern Mode, so the day ends screen-off.")],
         test="Do parents value toddler play more as a mode of Lanternling than as a separate app? Preference test in WP3.",
         s=dict(P=3, D=3, I=5, O=2, V=2, F=5, Df=3, L=3)),
    dict(file="lanternling/03-story-lantern.md", name="Story Lantern", venture="Lanternling",
         verdict="Keep (lead)", surface="S1", wave="1c",
         mvp=["SL-01", "SL-02", "SL-03", "SL-04", "SL-05", "SL-09"],
         engines=["EN-04", "EN-07", "EN-10"], sx=["SX-06", "SX-13", "SX-25", "SX-32"],
         enh=[("SL-E1", "Remote bedtime", "A grandparent or travelling parent reads live by link, with synced pages and no install (SX-06)."),
              ("SL-E2", "Human-signed story shelf", "ASL/BSL stories by Deaf storytellers, moved from V2 to V1 (SX-13)."),
              ("SL-E3", "Audio-player export", "Lantern Mode stories are playable on partner audio players or smart speakers where partner terms allow (SX-25).")],
         test="Remote bedtime with 15 distant-grandparent families: ≥2 sessions/week, and a grandparent SUS ≥75.",
         s=dict(P=4, D=5, I=4, O=4, V=4, F=4, Df=4, L=4)),
    dict(file="lanternling/04-sound-garden.md", name="Sound Garden", venture="Lanternling",
         verdict="Keep (lead)", surface="S1", wave="1c",
         mvp=["SG-01", "SG-02", "SG-03", "SG-04", "SG-05", "SG-06"],
         engines=["EN-03", "EN-04", "EN-09"], sx=["SX-17", "SX-20", "SX-22", "SX-25"],
         enh=[("SG-E1", "Classroom small-group CoPilot", "Pre-K/K teachers get Tutor-CoPilot-style prompts for small-group phonics (SX-17)."),
              ("SG-E2", "Take-home decodables", "Printable decodable books matched to the child's current bed (SX-25)."),
              ("SG-E3", "Reading-profile handoff", "With consent, the reading profile passes to Read Rangers or ReadWave, and the caregiver chooses. Never a label (SX-20).")],
         test="Can an on-device read-along meet the WER target by speaker group? SX-22 feasibility spike.",
         s=dict(P=5, D=4, I=4, O=5, V=4, F=3, Df=4, L=5)),
    dict(file="lanternling/05-number-nest.md", name="Number Nest", venture="Lanternling",
         verdict="Keep", surface="S1", wave="2",
         mvp=["NN-01", "NN-02", "NN-03", "NN-04", "NN-06", "NN-07"],
         engines=["EN-03", "EN-10"], sx=["SX-25"],
         enh=[("NN-E1", "Math-talk Moment Cards", "Parent prompts for grocery, cooking and stairs, sharing Babble Buddy's card engine."),
              ("NN-E2", "Paper mirror", "Printable ten-frames and bead bars that mirror each digital material (SX-25).")],
         test="Do self-correcting materials sustain persistence without rewards? Pre-K paper test, n=16.",
         s=dict(P=3, D=3, I=4, O=4, V=3, F=4, Df=3, L=3)),
    dict(file="lanternling/06-calm-cubs.md", name="Calm Cubs", venture="Lanternling",
         verdict="Merge → Lanternling skin on EN-05 Routine, Regulation & Focus engine", surface="S1", wave="2",
         mvp=["CC-01", "CC-02", "CC-03", "CC-04", "CC-08"],
         engines=["EN-05", "EN-02"], sx=["SX-12", "SX-19", "SX-25"],
         enh=[("CC-E1", "Childcare handoff card", "A one-page routine and 'what calms me' card for daycare or grandparents (Sensory Passport, SX-12)."),
              ("CC-E2", "Gentle pathway to more support", "If a caregiver asks for more help, offer Wavelength tools. The caregiver chooses; no labelling.")],
         test="Is a routine built once reused across home, daycare and grandparents? Diary study, n=20.",
         s=dict(P=4, D=4, I=5, O=3, V=3, F=4, Df=3, L=5)),
    dict(file="lanternling/07-two-words.md", name="Two Words", venture="Lanternling",
         verdict="Re-scope → Family Voice & Languages layer (SX-07) + a stand-alone EFL SKU (MX/BR)", surface="S1", wave="2",
         mvp=["TWO-01", "TWO-02", "TWO-04", "TWO-07"],
         engines=["EN-07"], sx=["SX-07", "SX-24", "SX-26", "SX-32"],
         enh=[("TWO-E1", "Record by link or phone", "Grandparents record words from a link or a phone call, with no app install (SX-26)."),
              ("TWO-E2", "Community heritage packs", "Native-speaker-reviewed heritage-language packs added through the Content Studio (SX-32).")],
         test="Heritage (US) vs EFL (MX/BR) willingness to pay: smoke test in WP5.",
         s=dict(P=3, D=3, I=4, O=3, V=2, F=4, Df=4, L=4)),
    # ---------------- Questwise ----------------
    dict(file="questwise/01-sage-tutor.md", name="Sage Tutor", venture="Questwise",
         verdict="Re-scope → Embedded Tutor (EN-03) in every Questwise experience + a homework mode", surface="S2", wave="1c",
         mvp=["ST-02", "ST-03", "ST-04", "ST-05", "ST-07", "ST-10"],
         engines=["EN-03", "EN-09", "EN-12"], sx=["SX-08", "SX-09", "SX-17"],
         enh=[("ST-E1", "At-error invitations", "After two misses in any Questwise experience, Sage offers help in context. The target is ≥40% uptake, against the 17% Khanmigo baseline [V2]."),
              ("ST-E2", "Guide & parent CoPilot", "Suggests how the adult can help without giving the answer (the Tutor CoPilot pattern)."),
              ("ST-E3", "Worksheet-aware capture", "Recognizes the method on the class worksheet so hints match what the teacher taught.")],
         test="Wizard-of-Oz A/B: embedded at-error invitation vs. a separate tutor entry point. Measure uptake and completion, n=20 families.",
         s=dict(P=5, D=4, I=4, O=5, V=4, F=3, Df=4, L=5)),
    dict(file="questwise/02-math-realms.md", name="Math Realms", venture="Questwise",
         verdict="Keep (lead)", surface="S2", wave="1c",
         mvp=["MR-01", "MR-02", "MR-03", "MR-04", "MR-05", "MR-06"],
         engines=["EN-03", "EN-10"], sx=["SX-17", "SX-25", "SX-31"],
         enh=[("MR-E1", "Real-world math missions", "Printable family missions (cooking, sport stats) that unlock nothing purchasable (SX-25)."),
              ("MR-E2", "Calm fluency", "Untimed fact-fluency practice with self-set goals, replacing speed drills.")],
         test="Mastery-gated vs. points variant: persistence and enjoyment (paper A/B, microschools).",
         s=dict(P=4, D=4, I=4, O=5, V=4, F=3, Df=4, L=4)),
    dict(file="questwise/03-read-rangers.md", name="Read Rangers", venture="Questwise",
         verdict="Keep", surface="S2", wave="2",
         mvp=["RR-02", "RR-03", "RR-04", "RR-05", "RR-07"],
         engines=["EN-04", "EN-03"], sx=["SX-20", "SX-14"],
         enh=[("RR-E1", "Reading continuum", "Uses one skill model with Sound Garden and ReadWave, so dyslexic readers keep their supports (SX-20)."),
              ("RR-E2", "Synced audiobook + text shelf", "An access route to grade-level content, alongside decoding practice rather than instead of it.")],
         test="Interest-matched texts vs. a curated library: minutes read and comprehension probes, 3-week concierge.",
         s=dict(P=4, D=3, I=5, O=4, V=3, F=3, Df=3, L=4)),
    dict(file="questwise/04-builders-lab.md", name="Builder's Lab", venture="Questwise",
         verdict="Defer to Wave 3 → a 'Make with AI' module (free Scratch/Code.org dominate)", surface="S2", wave="3",
         mvp=["BL-02", "BL-03", "BL-04", "BL-06"],
         engines=["EN-03"], sx=["SX-14", "SX-17"],
         enh=[("BL-E1", "Accessible coding as the wedge", "A screen-reader- and switch-operable block/Python editor, which few kids' coding tools offer [I]."),
              ("BL-E2", "Make an AI responsibly", "Projects paired with AI Detectives cases (SX-18).")],
         test="Parent willingness to pay against free tools. Interviews, n=10; proceed only if ≥40% would pay.",
         s=dict(P=2, D=3, I=4, O=3, V=2, F=3, Df=3, L=2)),
    dict(file="questwise/05-ai-detectives.md", name="AI Detectives", venture="Questwise",
         verdict="Merge → age 9–12 edition of EN-06 Safety, Scam, AI & Media Literacy engine", surface="S2", wave="2",
         mvp=["AD-01", "AD-02", "AD-03", "AD-04"],
         engines=["EN-06"], sx=["SX-18", "SX-32"],
         enh=[("AD-E1", "Teach-your-grandparent missions", "Kids walk a grandparent through a scam case that pairs with Silver Circuit's Scam Gym (SX-18)."),
              ("AD-E2", "Free classroom edition", "A brand-building distribution channel for Questwise.")],
         test="Intergenerational mission completion with ≥10 families; teacher adoption intent ≥4/5.",
         s=dict(P=4, D=3, I=4, O=3, V=3, F=4, Df=4, L=5)),
    dict(file="questwise/06-wonder-lab.md", name="Wonder Lab", venture="Questwise",
         verdict="Defer to Wave 3", surface="S2", wave="3",
         mvp=["WL-01", "WL-02", "WL-04", "WL-07"],
         engines=["EN-10"], sx=["SX-14", "SX-25"],
         enh=[("WL-E1", "Data sonification", "Sensor readings rendered as sound, so blind and low-vision children can investigate (SX-14)."),
              ("WL-E2", "Privacy-safe citizen science", "Contributions stripped of child location and identity.")],
         test="Off-screen experiment completion with printed cards, n=20 families.",
         s=dict(P=2, D=3, I=4, O=3, V=2, F=4, Df=3, L=2)),
    dict(file="questwise/07-mission-control.md", name="Mission Control", venture="Questwise",
         verdict="Merge → Questwise skin on EN-05 Routine, Regulation & Focus engine", surface="S2", wave="2",
         mvp=["MC-01", "MC-02", "MC-04", "MC-05", "MC-10", "MC-13"],
         engines=["EN-05", "EN-11"], sx=["SX-19", "SX-05"],
         enh=[("MC-E1", "Family homework agreement", "A plan co-created by child and parent, written in the child's words, to reduce conflict."),
              ("MC-E2", "Assignment import in MVP", "LMS and microschool assignment import (MC-13), promoted to MVP for the ESA and microschool channel.")],
         test="Tween self-adoption vs. parent-run: 2-week diary study.",
         s=dict(P=4, D=4, I=5, O=3, V=3, F=4, Df=3, L=5)),
    # ---------------- Ascendly ----------------
    dict(file="ascendly/01-study-coach.md", name="Study Coach", venture="Ascendly",
         verdict="Re-scope → Embedded Tutor (EN-03) in Exam Ready / Explain It Back + a stand-alone mode", surface="S3", wave="1d",
         mvp=["SC-02", "SC-03", "SC-04", "SC-05", "SC-06", "SC-08"],
         engines=["EN-03", "EN-12"], sx=["SX-08", "SX-09", "SX-17"],
         enh=[("SC-E1", "Bring your AI chat", "The teen imports a chat they had with a general assistant. The coach turns it into retrieval questions and a teach-it-back check, meeting teens where they already study."),
              ("SC-E2", "At-error invitations", "Offered inside Exam Ready practice after two misses (SX-17).")],
         test="Under deadline pressure, do teens choose the coach? Diary + Wizard-of-Oz study, n=40; ≥50% return weekly.",
         s=dict(P=5, D=3, I=4, O=5, V=3, F=3, Df=3, L=5)),
    dict(file="ascendly/02-exam-ready.md", name="Exam Ready", venture="Ascendly",
         verdict="Keep (lead)", surface="S3", wave="1d",
         mvp=["ER-02", "ER-03", "ER-05", "ER-06", "ER-07", "ER-09"],
         engines=["EN-03", "EN-04", "EN-10"], sx=["SX-17", "SX-31"],
         enh=[("ER-E1", "Accommodations request helper", "Explains the exam board's accommodations and access-arrangements process, with a checklist to work through with the counselor. Guidance only."),
              ("ER-E2", "Squad sync", "Turns the study plan into Study Squad sessions (EN-11).")],
         test="Item-bank quality: reviewer agreement ≥0.8 on a 100-item pilot bank.",
         s=dict(P=5, D=5, I=4, O=4, V=4, F=3, Df=3, L=4)),
    dict(file="ascendly/03-explain-it-back.md", name="Explain It Back", venture="Ascendly",
         verdict="Keep (lead, B2B wedge)", surface="S3", wave="1d",
         mvp=["EB-02", "EB-03", "EB-04", "EB-05", "EB-06", "EB-10"],
         engines=["EN-03", "EN-10"], sx=["SX-09", "SX-16", "SX-30"],
         enh=[("EB-E1", "Explain in your home language", "Multilingual learners explain in their strongest language. The rubric scores the concept, not English proficiency."),
              ("EB-E2", "Oral-defense lite", "A 3-minute live viva scheduler for teachers, for AI-era assessment.")],
         test="Teacher value ≥4/5 and teen comfort ≥3.5/5 in a 4-class paper pilot.",
         s=dict(P=5, D=4, I=5, O=4, V=4, F=3, Df=5, L=4)),
    dict(file="ascendly/04-draft-mentor.md", name="Draft Mentor", venture="Ascendly",
         verdict="Keep", surface="S3", wave="2",
         mvp=["DM-02", "DM-04", "DM-05", "DM-06", "DM-07"],
         engines=["EN-03", "EN-10"], sx=["SX-09", "SX-24"],
         enh=[("DM-E1", "AI-use disclosure draft", "An AI-use statement drafted from the authorship timeline, which the teen edits and chooses whether to submit."),
              ("DM-E2", "Home-language drafting", "Multilingual writers draft in their strongest language, then revise into English (DM-17 promoted to V1).")],
         test="Docs add-on vs. stand-alone editor preference, n=30 teens and 10 teachers.",
         s=dict(P=5, D=3, I=4, O=4, V=3, F=3, Df=4, L=3)),
    dict(file="ascendly/05-study-squad.md", name="Study Squad", venture="Ascendly",
         verdict="Merge → Ascendly skin on EN-05 + EN-11 (Focus & safe rooms)", surface="S3", wave="2",
         mvp=["SQ-01", "SQ-02", "SQ-03", "SQ-05", "SQ-09"],
         engines=["EN-05", "EN-11"], sx=["SX-19", "SX-05"],
         enh=[("SQ-E1", "OS focus integration", "The teen's chosen lock-in uses platform focus and Screen Time APIs (e.g., iOS Family Controls, Android Digital Wellbeing) [M: verify API scope]."),
              ("SQ-E2", "Library virtual study hall", "A partner-hosted, moderated study hall for teens without a friend group.")],
         test="Discord-bot pilot: ≥2 sessions/week per active teen.",
         s=dict(P=4, D=3, I=4, O=2, V=2, F=4, Df=3, L=4)),
    dict(file="ascendly/06-pathfinder.md", name="Pathfinder", venture="Ascendly",
         verdict="Merge → teen edition of EN-08 Pathways & Skills (continuity with Career Sprint)", surface="S3", wave="3",
         mvp=["PF-01", "PF-02", "PF-03", "PF-04"],
         engines=["EN-08"], sx=["SX-02", "SX-21"],
         enh=[("PF-E1", "Accommodations & disclosure coach", "Helps disabled teens understand disclosure choices and accommodations at college and work. Links to official sources; not legal advice."),
              ("PF-E2", "Apprenticeship & CTE finder", "Local apprenticeships and CTE programmes alongside college routes.")],
         test="Sponsor letters of intent (≥2) and counselor interest (n=15).",
         s=dict(P=3, D=3, I=4, O=3, V=3, F=3, Df=3, L=4)),
    dict(file="ascendly/07-life-ready.md", name="Life Ready", venture="Ascendly",
         verdict="Merge → teen edition of EN-06 Safety, Scam, AI & Media Literacy engine", surface="S3", wave="2",
         mvp=["LR-01", "LR-02", "LR-03"],
         engines=["EN-06"], sx=["SX-18"],
         enh=[("LR-E1", "Teach-a-grandparent missions", "Teens coach a grandparent through Silver Circuit Scam Gym cases (SX-18)."),
              ("LR-E2", "Live scam season", "Timely scenarios based on current scam patterns, reviewed by humans before release (LR-12 promoted).")],
         test="Organic pull: short-form content test plus school elective interest.",
         s=dict(P=3, D=2, I=4, O=3, V=2, F=4, Df=3, L=4)),
    # ---------------- Evergrow ----------------
    dict(file="evergrow/01-ai-fluency-lab.md", name="AI Fluency Lab", venture="Evergrow",
         verdict="Keep (studio lead; absorbs Lead with AI as the Manager track)", surface="S4", wave="1a",
         mvp=["F1", "F2", "F3", "F4", "F5", "F8"],
         engines=["EN-03", "EN-06", "EN-08", "EN-10"], sx=["SX-02", "SX-21", "SX-30", "SX-31"],
         enh=[("AFL-E1", "Productivity proof pack", "Before/after task time and quality measured in sandboxes, rolled up into an aggregate ROI report for the buyer. This answers the softened EU Art. 4 duty and Coursera's ~91% enterprise NRR [V2]."),
              ("AFL-E2", "AI as assistive tech at work", "A track for disabled employees and their managers on using AI for accessibility (captioning, summarizing, task breakdown)."),
              ("AFL-E3", "Manager track", "Lead with AI simulations delivered as a module (see the Lead with AI verdict).")],
         test="Two design-partner cohorts: measured task-performance gain, plus ≥3 paid LOIs at ≥$150/seat/yr.",
         s=dict(P=4, D=4, I=4, O=4, V=5, F=4, Df=4, L=5)),
    dict(file="evergrow/02-career-sprint.md", name="Career Sprint", venture="Evergrow",
         verdict="Merge → adult edition of EN-08 Pathways & Skills, in Evergrow Work", surface="S4", wave="2",
         mvp=["F1", "F2", "F3", "F5", "F6"],
         engines=["EN-08", "EN-11"], sx=["SX-02", "SX-21"],
         enh=[("CS-E1", "Neurodivergent hiring pathway", "Briefs from ND-friendly employers, accommodations in interview practice, and continuity for Wavelength and Ascendly graduates."),
              ("CS-E2", "Portfolio continuity", "Imports the Ascendly Record through the Lifelong Learner Passport (SX-02).")],
         test="Hiring managers rate sprint portfolios above certificates (n=5 managers, 15 learners).",
         s=dict(P=4, D=3, I=4, O=3, V=3, F=3, Df=3, L=4)),
    dict(file="evergrow/03-speak-freely.md", name="Speak Freely", venture="Evergrow",
         verdict="Keep (stand-alone consumer app; re-scope the human layer)", surface="S5", wave="2",
         mvp=["F1", "F2", "F3", "F4", "F6", "F10"],
         engines=["EN-07", "EN-09", "EN-11"], sx=["SX-24", "SX-26"],
         enh=[("SF-E1", "Small-group check-ins by default", "4–6 learners per human session instead of 1:1, to fix unit economics after Babbel closed its consumer live classes (Jul 2025) [V2]."),
              ("SF-E2", "Community conversation hosts", "Vetted, paid heritage speakers and retirees from Evergrow Circle host conversations: intergenerational supply that also gives hosts purpose.")],
         test="Group check-in satisfaction ≥ 1:1 minus 0.5 points, with tutor cost ≤35% of revenue.",
         s=dict(P=4, D=4, I=4, O=3, V=3, F=3, Df=3, L=3)),
    dict(file="evergrow/04-lead-with-ai.md", name="Lead with AI", venture="Evergrow",
         verdict="Merge → Manager track inside AI Fluency Lab", surface="S4", wave="2",
         mvp=["F1", "F2", "F6"],
         engines=["EN-08", "EN-11"], sx=["SX-30"],
         enh=[("LA-E1", "Team AI charter builder", "Managers co-create team norms for AI use (disclosure, review, data) and export them to the team's workspace."),
              ("LA-E2", "Aggregate-only analytics", "Readiness is reported only in aggregates of ≥5 people, never as individual transcripts (reinforces F6).")],
         test="Bundle vs. stand-alone pricing interviews with 12 L&D leaders.",
         s=dict(P=3, D=3, I=3, O=3, V=4, F=4, Df=3, L=4)),
    dict(file="evergrow/05-parent-coach.md", name="Parent Coach", venture="Evergrow",
         verdict="Re-scope → Studio Family Hub (cross-venture caregiver app)", surface="S9", wave="1b",
         mvp=["F1", "F2", "F3", "F5", "F7"],
         engines=["EN-01", "EN-10", "EN-12"], sx=["SX-01", "SX-04", "SX-08", "SX-27", "SX-28", "SX-29"],
         enh=[("PC-E1", "IEP/EHCP Prep Coach", "Plain-language report explainer, meeting question builder and progress-evidence pack (SX-27)."),
              ("PC-E2", "Caregiver wellbeing & peer support", "Moderated groups, respite finder and a self-report burnout check (SX-28)."),
              ("PC-E3", "Family Digest home", "The single weekly summary across all children (SX-04).")],
         test="IEP Prep Coach concierge with ND parents, n=15: ≥70% feel 'more prepared'.",
         s=dict(P=4, D=4, I=5, O=3, V=3, F=4, Df=4, L=5)),
    dict(file="evergrow/06-silver-circuit.md", name="Silver Circuit", venture="Evergrow",
         verdict="Keep (lead) → merges with Curiosity Circle into the Evergrow Circle app", surface="S6", wave="1b",
         mvp=["F1", "F2", "F3", "F4", "F6", "F7"],
         engines=["EN-06", "EN-09", "EN-11"], sx=["SX-18", "SX-26", "SX-15"],
         enh=[("SCir-E1", "Phone/IVR access", "Dial-in classes and a 'scam check' phone line for seniors without smartphones (SX-26)."),
              ("SCir-E2", "Grandkids teach missions", "Paired with Life Ready and AI Detectives (SX-18)."),
              ("SCir-E3", "Trusted-contact alert", "With the senior's consent, a contact they chose is notified when they report a suspected scam.")],
         test="Landline pilot with 10 seniors completes a class and a scam check; library pilots at 2 branches.",
         s=dict(P=5, D=4, I=5, O=4, V=3, F=4, Df=5, L=4)),
    dict(file="evergrow/07-curiosity-circle.md", name="Curiosity Circle", venture="Evergrow",
         verdict="Merge → Evergrow Circle app (with Silver Circuit)", surface="S6", wave="2",
         mvp=["F1", "F2", "F3", "F4"],
         engines=["EN-07", "EN-11"], sx=["SX-06", "SX-07", "SX-26"],
         enh=[("CCir-E1", "Intergenerational circles (V2 → V1)", "Seniors record heritage-language words for Two Words and tell stories with grandchildren via Remote Co-play (SX-06, SX-07)."),
              ("CCir-E2", "Paid peer-host pathway (V2 → V1)", "Experienced members become paid circle hosts, growing supply and purpose.")],
         test="3 pilot cohorts: attendance ≥70% and re-enrolment ≥50%.",
         s=dict(P=4, D=3, I=5, O=3, V=3, F=4, Df=4, L=4)),
    # ---------------- Wavelength ----------------
    dict(file="wavelength/01-wavelength-day.md", name="Wavelength Day", venture="Wavelength",
         verdict="Keep (lead)", surface="S7", wave="1b",
         mvp=["D1", "D2", "D3", "D4", "D5", "D8", "D9"],
         engines=["EN-05", "EN-02", "EN-10"], sx=["SX-12", "SX-19", "SX-25", "SX-27"],
         enh=[("WD-E1", "About Me passport", "A learner-approved one-page communication, sensory and support profile for school, clinicians, hospitals and emergency responders (SX-12)."),
              ("WD-E2", "Family wall mode", "The shared visual schedule on a kitchen tablet or TV, in calm display mode.")],
         test="Timed setup ≤5 min median against Choiceworks; passport usefulness rated by 10 teachers and 5 clinicians.",
         s=dict(P=5, D=5, I=5, O=4, V=4, F=4, Df=4, L=5)),
    dict(file="wavelength/02-wavelength-voice.md", name="Wavelength Voice", venture="Wavelength",
         verdict="Keep (stand-alone AAC) — build-vs-partner gate in discovery", surface="S8", wave="1b",
         mvp=["V1", "V2", "V5", "V7", "V12", "V14"],
         engines=["EN-09", "EN-02"], sx=["SX-16", "SX-29"],
         enh=[("WV-E1", "Build-vs-license gate", "Before build, evaluate licensing an established open symbol and core-vocabulary set against building one, weighing SLP trust, time and motor-plan stability."),
              ("WV-E2", "SGD funding letter kit", "Templates that help SLPs document medical necessity for insurance or Medicaid speech-generating-device funding (SX-29)."),
              ("WV-E3", "AAC input everywhere", "Answer in any studio experience with AAC (SX-16)."),
              ("WV-E4", "Offline emergency phrases", "Core safety phrases on the lock screen or a widget, working with no network.")],
         test="SLP panel (≥70% would trial it) and adult AAC-user co-design; authorship satisfaction ≥4/5.",
         s=dict(P=5, D=4, I=5, O=4, V=3, F=2, Df=4, L=4)),
    dict(file="wavelength/03-calm-harbor.md", name="Calm Harbor", venture="Wavelength",
         verdict="Keep (lead; shares EN-05 with Calm Cubs)", surface="S7", wave="1b",
         mvp=["C1", "C2", "C3", "C5", "C8", "C13"],
         engines=["EN-05", "EN-02"], sx=["SX-12", "SX-19"],
         enh=[("CH-E1", "Sensory passport for school", "A one-page sensory profile the learner approves and shares with teachers (SX-12)."),
              ("CH-E2", "Classroom calm-corner kiosk (V1 → MVP)", "A school edition on a shared device that anchors district sales.")],
         test="OT-led sessions (n=15): use during dysregulation, not only at calm times; comfort ≥4/5.",
         s=dict(P=5, D=4, I=5, O=3, V=3, F=4, Df=4, L=5)),
    dict(file="wavelength/04-readwave.md", name="ReadWave", venture="Wavelength",
         verdict="Keep (shares EN-04 Reading Continuum)", surface="S7", wave="2",
         mvp=["R1", "R3", "R4", "R5", "R8", "R9"],
         engines=["EN-04", "EN-09"], sx=["SX-20", "SX-27"],
         enh=[("RW-E1", "IEP accommodations suggestions", "A list of reading-access supports to discuss with the IEP team (text-to-speech, extended time). Not a determination (SX-27)."),
              ("RW-E2", "Structured-literacy tutor channel", "Certified tutors use ReadWave as a between-session practice tool, licensed through the Pro Console.")],
         test="Tutor/SENCO interviews (n=15) plus a 4-week paper pilot measuring fluency probes.",
         s=dict(P=5, D=4, I=5, O=4, V=4, F=3, Df=3, L=4)),
    dict(file="wavelength/05-focus-crew.md", name="Focus Crew", venture="Wavelength",
         verdict="Keep (shares EN-05 with Mission Control / Study Squad)", surface="S7", wave="2",
         mvp=["F1", "F2", "F4", "F5", "F6"],
         engines=["EN-05", "EN-11"], sx=["SX-19", "SX-28"],
         enh=[("FC-E1", "Teacher check-in card", "A daily one-tap, child-visible school–home note, with no behaviour scoring."),
              ("FC-E2", "Homework-conflict scripts", "Co-regulation scripts for parents at the hardest moment (SX-28).")],
         test="6-week engagement curve with a reward-fading plan (n=20 families).",
         s=dict(P=5, D=4, I=5, O=3, V=3, F=4, Df=3, L=5)),
    dict(file="wavelength/06-social-compass.md", name="Social Compass", venture="Wavelength",
         verdict="Keep (Wave 3, high sensitivity; ND board veto)", surface="S7", wave="3",
         mvp=["S1", "S2", "S3", "S11"],
         engines=["EN-08", "EN-02"], sx=["SX-13", "SX-21"],
         enh=[("SCo-E1", "Peer-understanding module", "A double-empathy module that teaches neurotypical classmates about neurodivergent communication, so the work runs both ways."),
              ("SCo-E2", "Self-advocacy handoff", "My Profile card and scripts carry into Pathways at college and work (SX-21).")],
         test="Autistic teen and adult co-design (n=12): rated 'affirming, not masking' ≥4/5.",
         s=dict(P=4, D=3, I=5, O=3, V=3, F=3, Df=5, L=3)),
    dict(file="wavelength/07-spark-switch.md", name="Spark Switch", venture="Wavelength",
         verdict="Keep (Wave 3; partner hardware)", surface="S7", wave="3",
         mvp=["P2", "P3", "P4", "P6", "P7", "P10"],
         engines=["EN-02", "EN-09"], sx=["SX-16"],
         enh=[("SS-E1", "Remote therapist mode", "During a telehealth session, an OT or teacher adjusts scan speed and dwell remotely."),
              ("SS-E2", "Family music-making (V2 → V1)", "Switch-driven music the family plays together (P17 promoted).")],
         test="2 special schools with existing switches (Wizard-of-Oz); teacher value ≥4/5.",
         s=dict(P=4, D=3, I=5, O=3, V=3, F=3, Df=5, L=2)),
]


def score(a):
    return round(sum(WEIGHTS[k] * v / 5 for k, v in a["s"].items()))


def section15(a):
    lines = [
        "## 15. Reevaluation & enhancements (v1.1)",
        "",
        "> Added by the studio reevaluation on 29 Sep 2026. This section **overrides** §4 tiers where they conflict.",
        "> Rationale: [Project Reevaluation](../../03-project-reevaluation.md). Shared capabilities: [Studio Platform Features](../../04-studio-platform-features.md).",
        "",
        "| | |",
        "|---|---|",
        f"| **Verdict** | {a['verdict']} |",
        f"| **Ships in** | {SURFACES[a['surface']]} ({a['surface']}) |",
        f"| **Build wave** | {a['wave']} |",
        f"| **Pre-discovery priority score** | {score(a)}/100 [I] |",
        f"| **Consumes engines** | {', '.join(a['engines'])} |",
        f"| **Studio features used** | {', '.join(a['sx'])} |",
        "",
        "### 15.1 Trimmed MVP (app-specific features only)",
        f"**MVP = {', '.join(a['mvp'])}.** All other §4 MVP items move to V1, **unless the platform provides them**:",
        "- My Needs and Sensory Dial come from EN-02.",
        "- Weekly summaries are replaced by the Family Digest (SX-04).",
        "- Sharing and roles come from EN-01 and the Pro Console (SX-30).",
        "- Fair billing comes from the Family Pass (SX-01).",
        "- Safety comes from EN-12.",
        "",
        "Acceptance criteria for the retained items stay as written in §12.",
        "",
        "### 15.2 New features",
        "| ID | Feature | Description |",
        "|---|---|---|",
    ]
    lines += [f"| {i} | **{t}** | {d} |" for i, t, d in a["enh"]]
    lines += [
        "",
        "### 15.3 New validation question",
        a["test"],
        "",
        "### 15.4 Score breakdown [I]",
        "| " + " | ".join(CRITERIA[k] + f" ({WEIGHTS[k]})" for k in WEIGHTS) + " |",
        "|" + "---|" * len(WEIGHTS),
        "| " + " | ".join(str(a["s"][k]) for k in WEIGHTS) + " |",
        "",
    ]
    return "\n".join(lines)


def write_app_sections():
    for a in APPS:
        p = ROOT / "docs" / "apps" / a["file"]
        t = p.read_text()
        t = re.sub(r"\n## 15\. Reevaluation & enhancements.*\Z", "", t, flags=re.S).rstrip() + "\n"
        p.write_text(t + "\n" + section15(a))


def per_app_table():
    rows = ["| Venture | App | Verdict | Ships in | Wave | Score | Trimmed MVP | New features |",
            "|---|---|---|---|---|---|---|---|"]
    for a in APPS:
        link = f"[{a['name']}](apps/{a['file']})"
        enh = "; ".join(f"{i} {t}" for i, t, _ in a["enh"])
        rows.append(f"| {a['venture']} | {link} | {a['verdict']} | {a['surface']} | {a['wave']} | {score(a)} | "
                    f"{len(a['mvp'])} ({', '.join(a['mvp'])}) | {enh} |")
    return "\n".join(rows)


def ranking_table():
    ranked = sorted(APPS, key=lambda a: -score(a))
    rows = ["| Rank | App | Venture | Score | Wave |", "|---|---|---|---|---|"]
    for n, a in enumerate(ranked, 1):
        rows.append(f"| {n} | {a['name']} | {a['venture']} | {score(a)} | {a['wave']} |")
    return "\n".join(rows)


def surface_table():
    rows = ["| Surface | Experiences |", "|---|---|"]
    for sid, sname in SURFACES.items():
        names = [a["name"] for a in APPS if a["surface"] == sid]
        if sid == "S9":
            names += ["Family Pass, Trust Center, Family Digest, IEP Prep Coach, wellbeing, Funding Navigator"]
        if sid == "S10":
            names = ["Teacher, guide, SLP/OT/BCBA, counselor, employer (aggregate), library and aging-agency consoles for all experiences"]
        rows.append(f"| **{sid} {sname}** | {', '.join(names)} |")
    return "\n".join(rows)


def fill_reevaluation_doc():
    p = ROOT / "docs" / "03-project-reevaluation.md"
    t = p.read_text()
    blocks = {"PER_APP": per_app_table(), "RANKING": ranking_table(), "SURFACES": surface_table()}
    for k, v in blocks.items():
        t = re.sub(rf"(<!-- GEN:{k} -->).*?(<!-- /GEN:{k} -->)", rf"\1\n{v}\n\2", t, flags=re.S)
    p.write_text(t)


if __name__ == "__main__":
    write_app_sections()
    fill_reevaluation_doc()
    mvp_total = sum(len(a["mvp"]) for a in APPS)
    print(f"apps={len(APPS)} trimmed_mvp_features={mvp_total} "
          f"wave1={sum(a['wave'].startswith('1') for a in APPS)}")

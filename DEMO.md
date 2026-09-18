# 🎬 Nerdy Arithmetic AI — 2-Minute Video Demo Script

> **Challenge:** [Nerdy AI Hackathon](https://hackathon.nerdy.com) — **Prompt 01: K–5 Math Game**  
> **Target Audience:** Hackathon Judges, Product Engineers, Educators, and Parents  
> **Live Production App:** [https://nerdy-arithmetic-ai.web.app](https://nerdy-arithmetic-ai.web.app)  
> **Repository:** [https://github.com/SKannaian/nerdy-arithmetic-ai](https://github.com/SKannaian/nerdy-arithmetic-ai)  
> **Target Video Length:** 2 Minutes (120 Seconds)

---

## 🛠️ Tech Stack & Automated Infrastructure
Before diving into the flow, here is the robust stack powering Nerdy Arithmetic AI:
- **Frontend Core:** Edge-capable Single Page Application (SPA) using Vanilla JavaScript, HTML5, and TailwindCSS for zero-latency interactions.
- **AI Engine:** Google Gemini 2.5 Flash for cognitive misconception classification and Socratic hints.
- **Hosting & Infrastructure:** Deployed globally on **Google Cloud Firebase Hosting**.
- **DevOps:** Fully automated **GitHub Actions CI/CD Pipeline**—every push to `main` is rigorously tested and seamlessly deployed to Firebase production.
- **Micro-services:** Integration with EmailJS for real-world OTP email delivery, and Web Speech API for zero-dependency Voice TTS.

*(For full technical specifications, see [ARCHITECTURE.md](ARCHITECTURE.md)).*

---

## ⏱️ Video Structure Breakdown

| Minute | Focus Area | Visual On-Screen Cue | Narrative Goal |
| :---: | :--- | :--- | :--- |
| **0:00 – 1:00** | **Minute 1: Live Product Demo & Pedagogy** | Live Web App showing Ten-Frames, Subtraction, Socratic Byte, and SmartScore. | Showcase intuitive, gamified CRA math and non-spoiling AI guidance. |
| **1:00 – 2:00** | **Minute 2: Dashboards, Tech Stack & Impact** | Analytics, [Architecture Diagrams](ARCHITECTURE.md#1-high-level-system-topology), and Live Tutor Hand-Off. | Prove technical engineering excellence, admin control, and business alignment. |

---

## 🎙️ Detailed Minute-by-Minute Teleprompter Script

---

### ⏱️ MINUTE 1: LIVE PRODUCT DEMO & PEDAGOGICAL EXPERIENCE (0:00 – 1:00)

**[0:00 – 0:15] The Hook & Mission:**  
*(Camera on speaker, then screen transitions to live app)*  
> *"Hello! I’m excited to present **Nerdy Arithmetic AI**, a gamified, AI-native Socratic math platform built for **Prompt 01: K–5 Math Game**. Instead of generic chatbots that spoil answers, we designed an experience grounded in Concrete–Representational–Abstract (CRA) learning science."*

**[0:15 – 0:35] Concrete CRA Manipulatives:**  
*(Screen: Click "➖ Subtraction", then click "Auto-Model Equation" on a subtraction problem)*  
> *"Notice our interactive **Ten-Frame manipulative** for early learners: when subtracting, it visually crosses out counters with bold red ✕ marks, showing a live legend. For older grades, it seamlessly scales to **Base-10 regrouping blocks** and multiplication **Area Arrays**."*
*(Reference: [CRA Manipulatives Architecture](ARCHITECTURE.md#4-jerome-bruners-cra-manipulatives-architecture))*

**[0:35 – 0:50] Byte: The Socratic AI Mentor:**  
*(Screen: Type a wrong answer and submit)*  
> *"When a child makes a mistake, our AI companion, **Byte**, doesn’t just buzz them wrong. Its cognitive classifier identifies the misconception—like an inverted operator—and gives a gentle Socratic hint without spoiling the number, spoken aloud via Web Speech synthesis."*
*(Reference: [AI Feedback Loop](ARCHITECTURE.md#5-the-socratic-ai-feedback--cognitive-misconception-loop-byte))*

**[0:50 – 1:00] SmartScore Mastery:**  
*(Screen: Point to circular SVG SmartScore ring)*  
> *"Our dynamic **SmartScore** algorithm rewards mastery, dynamically progressing students through Bronze, Silver, and into the high-stakes Gold Challenge Zone."*
*(Reference: [SmartScore State Machine](ARCHITECTURE.md#6-smartscore-mastery-progression--state-machine))*

---

### ⏱️ MINUTE 2: DASHBOARDS, TECHNOLOGY & IMPACT (1:00 – 2:00)

**[1:00 – 1:20] Analytics & Role-Based Dashboards:**  
*(Screen: Switch between Progress Report tab and Teacher/Admin Command Center)*  
> *"Let's switch to the **Progress Report**. Powered by Chart.js, it displays dynamic visualizations of mastery growth and resolved misconceptions. Furthermore, our secure, role-based **Teacher and Admin Dashboards** allow educators to instantly audit live rosters, enroll students, and manage AI configurations."*
*(Reference: [Learner Journey & Flow](ARCHITECTURE.md#2-end-to-end-learner-journey--onboarding-flow))*

**[1:20 – 1:40] Architecture, CI/CD, & AI Cascade Resilience:**  
*(Screen: Flash [High-Level System Topology](ARCHITECTURE.md#1-high-level-system-topology) and [Anti-Repetition Engine](ARCHITECTURE.md#3-anti-repetition--spaced-repetition-engine) diagrams)*  
> *"Under the hood, this edge-capable SPA is deployed to **Google Cloud Firebase Hosting** via an automated **CI/CD GitHub Actions pipeline**. For intelligence, we leverage **Gemini 2.5 Flash**. To guarantee 100% judging uptime, our 3-tier cascade falls back to a **Zero-Crash Offline Engine** if the AI is unreachable. Plus, our Anti-Repetition Engine guarantees fresh problems daily."*

**[1:40 – 2:00] Varsity Tutors Synergy & Closing:**  
*(Screen: Click "Send Telemetry to Live Varsity Tutor", then Official Certificate)*  
> *"Crucially, this connects directly to Nerdy's core business: **Varsity Tutors**. When a student requests help, their complete diagnostic history transfers seamlessly to a live expert tutor. Upon reaching 100 SmartScore, students earn a printable **Certificate of Math Mastery**. Try it live at nerdy-arithmetic-ai.web.app. Thank you!"*
*(Reference: [Live Human Tutoring Hand-Off](ARCHITECTURE.md#7-varsity-tutors-live-human-tutoring-telemetry-hand-off))*

---

## 📋 Production Slide / Visual Asset Cheatsheet

1. **Minute 1 Visuals:**
   * Action 1: Click `➖ Subtraction`, then click `Auto-Model Equation`.
   * Action 2: Input a wrong answer, click `Submit` to trigger Socratic Byte.
2. **Minute 2 Visuals:**
   * Action 1: Click the `Progress Report` header icon.
   * Action 2: Switch role to `Teacher` or `Admin` to flash the backend Command Center.
   * Action 3: Display the [System Topology Diagram](ARCHITECTURE.md#1-high-level-system-topology) from `ARCHITECTURE.md`.
   * Action 4: Click `Live Varsity Tutor Help` to show the diagnostic dossier hand-off.

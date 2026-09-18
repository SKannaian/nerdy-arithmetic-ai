# 🎬 Nerdy Arithmetic AI — 2-Minute Video Demo Script

> **Challenge:** [Nerdy AI Hackathon](https://hackathon.nerdy.com) — **Prompt 01: K–5 Math Game**  
> **Target Audience:** Hackathon Judges, Product Engineers, Educators, and Parents  
> **Live Production App:** [https://nerdy-arithmetic-ai.web.app](https://nerdy-arithmetic-ai.web.app)  
> **Repository:** [https://github.com/SKannaian/nerdy-arithmetic-ai](https://github.com/SKannaian/nerdy-arithmetic-ai)  
> **Target Video Length:** 2 Minutes (120 Seconds)

---

## 🛠️ Tech Stack & Automated Infrastructure
Before we get into the demo, here is a quick look at how we built this:
- **Frontend Core:** Pure Vanilla JavaScript, HTML, and TailwindCSS to keep things incredibly fast.
- **Procedural Gen & Anti-Repetition:** Every math equation is generated dynamically on-the-fly. We also use a deterministic hashing filter (saved in local storage) to guarantee a student never sees the exact same math problem twice in one day.
- **AI Engine:** Powered by Google Gemini 2.5 Flash for the live Socratic tutor, and built using Google AI Studio and Antigravity IDE for rapid prompt engineering and agentic coding.
- **Hosting & Cloud:** Hosted on **Google Cloud Firebase Hosting**.
- **Automated Deployments:** We set up a **GitHub Actions CI/CD Pipeline**. Whenever we push code to `main`, it automatically deploys to our live Firebase site.
- **Extra Integrations:** We hooked up EmailJS to send real OTP emails, and used the browser's native Web Speech API to read text out loud.

*(If you want to see all the deep technical details, check out our [ARCHITECTURE.md](ARCHITECTURE.md)).*

---

## ⏱️ Video Structure Breakdown

| Minute | Focus Area | Visual On-Screen Cue | Narrative Goal |
| :---: | :--- | :--- | :--- |
| **0:00 – 1:00** | **Minute 1: Live Product Demo** | Live Web App showing math visuals, Byte the AI Tutor, and the SmartScore ring. | Show how the app is fun, visual, and actually helps kids learn instead of just giving answers. |
| **1:00 – 2:00** | **Minute 2: Dashboards, Tech Stack & Impact** | Analytics charts, [System Architecture](ARCHITECTURE.md#1-high-level-system-topology), and Live Tutor feature. | Show off the dashboards, explain the tech stack, and highlight the Varsity Tutors connection. |

---

## 🎙️ Detailed Minute-by-Minute Teleprompter Script

---

### ⏱️ MINUTE 1: THE LEARNING EXPERIENCE (0:00 – 1:00)

**[0:00 – 0:15] The Hook:**  
*(Camera on you, then switch to the live app home screen)*  
> *"Hi everyone! I’m Sathish, an AI Data Engineer with 20 years of IT experience. I’m super excited to show you **Nerdy Arithmetic AI**, a math game for K-5 students. Instead of typical chatbots that just give away the answer, I built a hands-on learning experience that helps kids understand math visually."*

**[0:15 – 0:35] Visual Problem Solving:**  
*(Screen: Click "➖ Subtraction", then click "Auto-Model Equation")*  
> *"When a student starts a problem, the app dynamically generates a unique equation—no hardcoded questions here. For early learners, we built interactive visual tools. If they are subtracting, the app actually crosses out the counters so they can see exactly what's happening."*

**[0:35 – 1:00] Byte the AI Tutor:**  
*(Screen: Type a wrong answer and hit Submit)*  
> *"If a student makes a mistake, our AI tutor, Byte, doesn't just mark it wrong. Powered by Gemini 2.5 Flash, it analyzes *why* they got it wrong—like if they accidentally added instead of subtracted—and gives them a helpful, spoken hint. And if the internet ever drops, our local offline engine takes over so the learning never stops."*

---

### ⏱️ MINUTE 2: DASHBOARDS & ECOSYSTEM (1:00 – 2:00)

**[1:00 – 1:25] Dashboards & Role-Based Access:**  
*(Screen: Click the Progress Report tab, then switch to Teacher/Admin mode)*  
> *"As students practice, their SmartScore goes up and everything is saved instantly to the browser's local database. Parents can open the Progress Report to see exactly where their kids are struggling. We also built secure, role-based access so teachers and admins have their own command centers to manage settings."*

**[1:25 – 1:45] The Varsity Tutors Handoff:**  
*(Screen: Click "Live Varsity Tutor Help" to show the telemetry dossier)*  
> *"But what if a kid is really stuck? We built a direct bridge to Varsity Tutors. With one click, all of the student's progress and AI error analysis is sent right to a live human tutor's screen so they can jump in and help immediately."*

**[1:45 – 2:00] The Tech Stack & Wrap Up:**  
*(Screen: Briefly flash the [Architecture Diagram](ARCHITECTURE.md#1-high-level-system-topology) or stay on the App)*  
> *"Everything you see is built with vanilla JavaScript for maximum speed and hosted globally on Google Firebase. It's a complete, end-to-end edge application. You can check it out live at nerdy-arithmetic-ai.web.app. Thanks for watching!"*


---

## 📋 Production Slide / Visual Asset Cheatsheet

1. **Minute 1 Visuals:**
   * Action 1: Click `➖ Subtraction`, then click `Auto-Model Equation`.
   * Action 2: Type in a wrong answer and hit `Submit` to show how the AI gives a hint.
2. **Minute 2 Visuals:**
   * Action 1: Click the `Progress Report` icon at the top.
   * Action 2: Change your role to `Teacher` or `Admin` to quickly show the backend dashboard.
   * Action 3: Show the [System Topology Diagram](ARCHITECTURE.md#1-high-level-system-topology) from the architecture doc.
   * Action 4: Click `Live Varsity Tutor Help` to show how data is handed off to a human tutor.

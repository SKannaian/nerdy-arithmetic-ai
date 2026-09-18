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

## 🖱️ Step-by-Step Click Sequence for the Demo

This is the exact sequence of buttons you should click during your screen recording to perfectly match the teleprompter script:

1. **[0:00] Intro:** Start on the main app screen. *(Don't click anything yet, just introduce yourself).*
2. **[0:15] Visual Modeling:** 
   * Click the `➖ Subtraction` tab. 
   * Click the `Auto-Model Equation` button to show the red counters visually crossing out.
3. **[0:35] Byte the AI Tutor:** 
   * Type a purposely incorrect answer into the keypad.
   * Click `Submit` so the screen shakes and the AI spoken hint pops up.
4. **[1:00] Dashboards:** 
   * Click the `Progress Report` icon at the top of the screen to show the SmartScore ring.
5. **[1:15] Admin Role:** 
   * Change the User Role dropdown from `Student` to `Teacher` (or `Admin`) to reveal the secure settings panel.
6. **[1:25] Varsity Tutors Handoff:** 
   * Click the `Live Varsity Tutor Help` button to trigger the telemetry dossier popup.
7. **[1:45] Tech Stack Wrap-up:** 
   * Switch browser tabs to briefly flash the [Architecture Diagram](ARCHITECTURE.md#1-high-level-system-topology) while you deliver the final lines about Firebase and JavaScript.

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

### ⏱️ MINUTE 1: LIVE PRODUCT DEMO (0:00 – 1:00)

**[0:00 – 0:15] The Hook & Mission:**  
*(Camera on speaker, then screen transitions to live app)*  
> *"Hi everyone! I’m super excited to show you **Nerdy Arithmetic AI**, a fun math game we built for K-5 students. Instead of typical chatbots that just give away the answer, we built a hands-on learning experience that actually helps kids understand math visually."*

**[0:15 – 0:35] Visual Math Tools:**  
*(Screen: Click "➖ Subtraction", then click "Auto-Model Equation" on a subtraction problem)*  
> *"For early learners, we built interactive visual tools. If a student is subtracting, the app actually crosses out the counters so they can see exactly what's happening. And as they level up in grades, we swap these out for base-10 blocks and multiplication grids."*
*(Reference: [Visual Tools Architecture](ARCHITECTURE.md#4-jerome-bruners-cra-manipulatives-architecture))*

**[0:35 – 0:50] Byte: The AI Tutor:**  
*(Screen: Type a wrong answer and submit)*  
> *"If a student makes a mistake, our AI tutor, Byte, doesn't just mark it wrong. It figures out *why* they got it wrong—like if they accidentally added instead of subtracted—and gives them a helpful hint to guide them to the right answer. It even reads the hint out loud."*
*(Reference: [AI Feedback Loop](ARCHITECTURE.md#5-the-socratic-ai-feedback--cognitive-misconception-loop-byte))*

**[0:50 – 1:00] SmartScore Progress:**  
*(Screen: Point to circular SmartScore ring)*  
> *"As students practice, their SmartScore goes up. They earn ribbons and eventually hit the Gold Challenge Zone when they truly master a skill."*
*(Reference: [SmartScore Progression](ARCHITECTURE.md#6-smartscore-mastery-progression--state-machine))*

---

### ⏱️ MINUTE 2: DASHBOARDS, TECHNOLOGY & IMPACT (1:00 – 2:00)

**[1:00 – 1:20] Analytics & Dashboards:**  
*(Screen: Switch between Progress Report tab and Teacher/Admin Dashboards)*  
> *"We also built detailed dashboards. Parents can check the Progress Report charts to see exactly where their kids are struggling and improving. Meanwhile, teachers and admins have their own secure command centers to manage students and tweak settings."*
*(Reference: [User Roles & Onboarding](ARCHITECTURE.md#2-end-to-end-learner-journey--onboarding-flow))*

**[1:20 – 1:40] How It's Built & Deployed:**  
*(Screen: Flash [High-Level System Topology](ARCHITECTURE.md#1-high-level-system-topology) and [Anti-Repetition](ARCHITECTURE.md#3-anti-repetition--spaced-repetition-engine) diagrams)*  
> *"On the tech side, the frontend is built with vanilla JavaScript and hosted on Google Firebase. Every time we push code to GitHub, our CI/CD pipeline automatically deploys it. We use Gemini 2.5 Flash for the AI, but just in case the API goes down, we built a local offline fallback so the app never crashes. We also wrote a custom script so kids never see the exact same math problem twice in one day."*

**[1:40 – 2:00] Varsity Tutors Connection & Wrap Up:**  
*(Screen: Click "Send Telemetry to Live Varsity Tutor", then Official Certificate)*  
> *"Finally, this ties right back into Varsity Tutors. If a kid is really stuck, they can click a button to connect with a live human tutor, and all their progress is sent right to the tutor's screen. Once they hit a perfect 100 score, they even get a printable certificate. You can check out the live app at nerdy-arithmetic-ai.web.app. Thanks for watching!"*
*(Reference: [Varsity Tutors Connection](ARCHITECTURE.md#7-varsity-tutors-live-human-tutoring-telemetry-hand-off))*

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

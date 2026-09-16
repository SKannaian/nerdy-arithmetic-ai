# Nerdy Arithmetic AI 🚀

> **An IXL-inspired, AI-native Socratic math learning platform for elementary students (Grades K–5).**  
> Built for the **[Nerdy AI Hackathon Challenge](https://hackathon.nerdy.com)** (Prompt 01: K–5 Math Game).

[![Hackathon Status](https://img.shields.io/badge/Nerdy%20Hackathon-Prompt%2001%20(K--5%20Math)-0284c7?style=for-the-badge&logo=target)](https://hackathon.nerdy.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![AI Engine](https://img.shields.io/badge/AI%20Engine-Gemini%202.5%20Flash-f59e0b?style=for-the-badge&logo=google)](https://ai.google.dev/)

---

## 🌟 Executive Overview & Hackathon Fit

**Nerdy (NYSE: NRDY)** powers **Varsity Tutors**, pairing live expert instruction with an adaptive AI layer across 3,000+ subjects.

### Why Nerdy Arithmetic AI Wins:
1. **Picks One Prompt & Perfects It:** Tailored specifically for **Prompt 01: K–5 Math Game**. Instead of a surface-level demo, it is a deep, production-ready educational product.
2. **IXL-Inspired Mastery UI:** Built with a bright, welcoming, child-friendly design system inspired by **[IXL Learning](https://www.ixl.com)**:
   - Dynamic **SmartScore (0–100)** algorithm that rewards mastery and unlocks Bronze, Silver, and Gold Challenge Zones.
   - Live **Questions Answered** and **Time Elapsed** HUD.
   - Grade-level ribbons: Kindergarten (Sums to 10), Grades 2–3 (Regrouping), and Grades 4–5 (Times tables).
3. **True Pedagogical Rigor (Jerome Bruner's CRA Framework):**
   - **Concrete:** Interactive virtual Ten-Frames with clickable colored tokens (K–1).
   - **Representational:** Base-10 blocks (tens rods and ones cubes) that visually show place-value regrouping (Grades 2–3) and area arrays (Grades 4–5).
   - **Abstract:** Symbolic numerical equations ($A + B = ?$).
4. **AI-Native Socratic Superpower ("Byte"):**
   - Powered by **Google Gemini 2.5 Flash** with strict pedagogical guardrails that **never spoil the numeric answer**.
   - **Cognitive Misconception Classifier:** Distinguishes off-by-one counting slips from inverted operators ($+$ vs $-$) and place-value regrouping errors.
   - **Audio Read-Aloud:** Integrated Web Speech API so young learners can listen to Byte's hints aloud.
   - **100% Zero-Crash Resilience:** Built-in heuristic Socratic fallback guarantees smooth judging even if API keys or internet are unavailable.

---

## 🏛️ System Architecture

```mermaid
graph TB
    subgraph Client["Client Tier (IXL-Inspired Web Application)"]
        UI["Bright Educational UI (TailwindCSS + Lucide + Confetti)"]
        HUD["IXL HUD: SmartScore (0-100) · Questions · Stopwatch"]
        CRA["CRA Virtual Manipulatives:<br>• Ten-Frames (K-1)<br>• Base-10 Blocks (2-3)<br>• Area Arrays (4-5)"]
        AudioEngine["Web Audio Chimes + Web Speech Synthesizer"]
        Scratchpad["Virtual Drawing Scratchpad Canvas"]
    end

    subgraph BackendGateway["FastAPI Gateway (:8765)"]
        Router["/api/chat & /health"]
        Classifier["Cognitive Misconception Classifier"]
        SocraticPrompt["Socratic Pedagogy Guardrails (Strict Anti-Spoil)"]
    end

    subgraph CloudAI["Google Cloud AI"]
        Gemini["Gemini 2.5 Flash API"]
        HeuristicFallback["Zero-Crash Offline Heuristic Engine"]
    end

    UI --> HUD
    UI --> CRA
    UI --> Scratchpad
    CRA & HUD --> AudioEngine

    UI -- "Answer Check / Socratic Hint" --> Router
    Router --> Classifier
    Classifier --> SocraticPrompt
    SocraticPrompt --> Gemini
    Gemini -. "Fallback if offline" .-> HeuristicFallback
    Gemini --> AudioEngine
```

---

## 🚀 Quick Start & How to Run

### Option 1: One-Click Windows Launch (Recommended)
Simply double-click **`start.bat`**.  
The script checks your Python environment, verifies dependencies, starts the local server, and automatically opens your browser to:
👉 **`http://localhost:8765`**

### Option 2: Manual Terminal Launch
```bash
# 1. Clone repository
git clone https://github.com/SKannaian/nerdy-arithmetic-ai.git
cd nerdy-arithmetic-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure your Gemini API key in .env (Optional; fallback works offline!)
# GEMINI_API_KEY=your_key_here

# 4. Run the server
python server.py
```
Open **`http://localhost:8765`** in your browser.

---

## 🎮 Interactive Features Walkthrough

### 1. Concrete–Representational–Abstract (CRA) Manipulatives
* **Kindergarten & 1st Grade:** Touch or click slots in the **Ten-Frame** to place blue or amber tokens. Click **"Auto-Model Equation"** to watch the equation visually populate!
* **Grades 2 & 3:** See the multi-digit numbers broken down into **Tens rods** and **Ones cubes**, helping students master regrouping without rote memorization.
* **Grades 4 & 5:** Dynamic multiplication **Area Array** grid showing row $\times$ column distribution.

### 2. The IXL SmartScore Mastery Loop
* Unlike simple quiz games, SmartScore reflects true conceptual mastery:
  - **0–69 (Practice Zone):** Rapid progression (+12 pts per correct answer).
  - **70–79 (Bronze Ribbon):** Intermediate mastery unlocked.
  - **80–89 (Silver Ribbon):** Advanced fluency.
  - **90–99 (Gold Challenge Zone):** High-stakes mastery zone (+1 pt per correct answer; enforces deep precision).
  - **100 (Mastery Trophy):** Full confetti celebration and mastery certificate!

### 3. Byte: The Socratic AI Mentor
* When a child enters an incorrect answer, Byte does **not** simply say "Incorrect".
* Byte's cognitive analyzer determines the mistake:
  - *Off-by-One Counting Slip:* *"You're so close—just 1 step away! Touch the last dot on your ten-frame."*
  - *Inverted Operator:* *"Look at the sign! It's a plus sign (+), so we are putting groups together!"*
  - *Regrouping Slip:* *"Check the tens column! Did you remember to bundle 10 ones?"*
* Click the speaker icon to hear Byte read the hint aloud with natural speech!

### 4. Built-in Drawing Scratchpad
Click **"Scratchpad"** in the top bar to pull up an on-screen drawing canvas where kids can scribble calculations, write down carries, or draw their own tally marks.

### 5. Personalized Onboarding & Daily Streak Retention
* **Interactive Learner Setup:** Welcoming child-friendly modal allows young explorers to select their mascot avatar (`🦊 🚀 🐼 🦁 🦄 ⚡`), choose their grade level, and establish their learner identity.
* **Daily Streak Retention (`Day X 🔥`):** Tracks consecutive active days, boosting long-term engagement and daily learning habits.
* **Student Analytics Dashboard:** Click the learner avatar in the header at any time to view total problems solved, skill mastery trophies, active streak, and diagnosed trouble areas.

### 6. Anti-Repetition & Smart Spaced Review Engine
* **The Problem:** Repetitive drills frustrate children and create false positives in mastery assessment.
* **The Solution:**
  - Every generated problem creates a unique conceptual signature (e.g. `k1:add:3:5`).
  - The engine indexes each problem in `state.profile.history` with `lastSeenDate`, `timesSeen`, and `wrongCount`.
  - **Strict Anti-Repetition:** When generating new questions, candidates are filtered against recent history. Questions encountered today are discarded in favor of fresh permutations.
  - **Smart Spaced Review:** Difficult problems or previously missed concepts are reintroduced on subsequent days as **`🎯 Smart Spaced Review`**, reinforcing long-term memory.
  - **HUD Transparency:** The top-left problem tag dynamically displays **`✨ Fresh Question`** or **`🎯 Smart Spaced Review`** so teachers, parents, and students know exactly what is being presented.

---

## 🎥 2–3 Minute Demo Video Walkthrough Script

Use this script for your Hackathon submission video:

* **[0:00 – 0:30] The Hook & Mission:**  
  *"Hi! I'm presenting **Nerdy Arithmetic AI**, an AI-native, IXL-inspired math platform built for Prompt 01 of the Nerdy Hackathon. Traditional elementary math apps either show static multiple-choice drills or bolt on generic chatbots that spoil the answers. We designed Nerdy Arithmetic AI around cognitive learning science and the Jerome Bruner CRA framework."*

* **[0:30 – 1:15] IXL Mastery & CRA Manipulatives:**  
  *"Let's see the app in action. Notice our bright, engaging IXL-style interface with real-time SmartScore, Questions, and Timer. In Kindergarten mode, watch how the ten-frame manipulative lets children touch and place counters to discover addition visually. We can switch to Grades 2–3 to see Base-10 regrouping blocks, or Grades 4–5 for multiplication arrays."*

* **[1:15 – 2:00] The AI Socratic Superpower:**  
  *"Now, watch what happens when a student enters a misconception. Let's say for 4 + 3, the child enters 1. Instead of a buzzer, our cognitive classifier identifies an inverted operator mistake. Byte, our Gemini 2.5 Flash Socratic companion, steps in: 'Look at the plus sign—we're putting groups together!' Byte coaches them without spoiling the number, and can read hints aloud to non-readers."*

* **[2:00 – 2:40] Architecture & Security:**  
  *"Under the hood, we built this with FastAPI and Gemini 2.5 Flash with strict zero-answer guardrails. All keys are secured server-side to prevent client credential leaks. If offline, our built-in pedagogical heuristic engine ensures 100% uptime with zero crashes."*

* **[2:40 – 3:00] Nerdy Alignment:**  
  *"This architecture directly complements Varsity Tutors' platform by providing autonomous learning telemetry to human tutors during live sessions. Thank you!"*

---

## 🏆 Hackathon Rubric Alignment

| Criteria | Weight | How Nerdy Arithmetic AI Delivers |
| :--- | :---: | :--- |
| **Pedagogical Rigor** | 25% | Jerome Bruner's CRA framework, Common Core standards, and Bloom's cognitive scaffolding. |
| **AI-Native Product Design** | 25% | Cognitive misconception classification, non-spoiling Socratic hint ladders, and natural voice read-aloud. |
| **UX Craftsmanship & Polish** | 20% | Bright IXL-inspired design system, SmartScore progress rings, confetti celebrations, and tactile touch keypad. |
| **Technical Architecture** | 15% | Decoupled FastAPI server, secure zero-leak proxy, Web Audio synthesis, and offline heuristic fallback. |
| **Demo Clarity** | 15% | Clear 180-second video roadmap, live runnable testbed, and comprehensive documentation. |

---

*Official challenge: [hackathon.nerdy.com](https://hackathon.nerdy.com)*

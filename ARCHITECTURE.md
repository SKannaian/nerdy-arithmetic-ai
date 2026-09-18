# 🏛️ Nerdy Arithmetic AI — Comprehensive System Architecture

> **An AI-Native Socratic Mathematics Learning Platform (Grades K–5)**  
> Engineered for the **[Nerdy AI Hackathon Challenge](https://hackathon.nerdy.com)** (Prompt 01: K–5 Math Game)  
> Live Deployment: **[https://nerdy-arithmetic-ai.web.app](https://nerdy-arithmetic-ai.web.app)** | Repository: **[GitHub](https://github.com/SKannaian/nerdy-arithmetic-ai)**

---

## 📑 Architecture Walkthrough Index

1. [High-Level System Topology](#1-high-level-system-topology)
2. [End-to-End Learner Journey & Onboarding Flow](#2-end-to-end-learner-journey--onboarding-flow)
3. [Anti-Repetition & Spaced Repetition Engine](#3-anti-repetition--spaced-repetition-engine)
4. [Jerome Bruner's CRA Manipulatives Architecture](#4-jerome-bruners-cra-manipulatives-architecture)
5. [The Socratic AI Feedback & Cognitive Misconception Loop ("Byte")](#5-the-socratic-ai-feedback--cognitive-misconception-loop-byte)
6. [SmartScore Mastery Progression & State Machine](#6-smartscore-mastery-progression--state-machine)
7. [Varsity Tutors Live Human Tutoring Telemetry Hand-Off](#7-varsity-tutors-live-human-tutoring-telemetry-hand-off)
8. [Automated Sunday Evening Parent Summary Pipeline](#8-automated-sunday-evening-parent-summary-pipeline)
9. [Component & Data Model Specifications](#9-component--data-model-specifications)

---

## 1. High-Level System Topology

Nerdy Arithmetic AI is built on a **modern, decoupled, edge-capable architecture**. The frontend Single Page Application (SPA) runs entirely client-side with zero external build dependencies. All AI processing, cognitive classification, and security (Role-Based Auth) are handled natively in the browser, interfacing directly with Google Cloud Firebase Hosting, EmailJS, and Google Gemini 2.5 Flash.

```mermaid
graph LR
    %% Styling - High Contrast for Presentations
    classDef primary fill:#2563eb,stroke:#1e40af,stroke-width:2px,color:#ffffff,font-weight:bold;
    classDef logic fill:#059669,stroke:#047857,stroke-width:2px,color:#ffffff,font-weight:bold;
    classDef cloud fill:#d97706,stroke:#b45309,stroke-width:2px,color:#ffffff,font-weight:bold;

    subgraph Client ["Client Browser (Single Page App)"]
        direction TB
        UI["Gamified UI & CRA Manipulatives"]:::primary
        Auth["Role-Based Email Auth"]:::logic
        AI["Cognitive AI & Fallback Engine"]:::logic
        DB["Local User Database"]:::primary
        
        UI --> Auth
        UI --> AI
        Auth --> DB
        AI --> DB
    end

    subgraph External ["Cloud Infrastructure & APIs"]
        direction TB
        Firebase["Google Firebase Hosting"]:::cloud
        Email["EmailJS (OTP Dispatch)"]:::cloud
        Gemini["Google Gemini 2.5 Flash"]:::cloud
        Varsity["Varsity Tutors Bridge"]:::cloud
    end

    %% Cross-boundary connections
    Client -. "Hosted On" .-> Firebase
    Auth -- "Verify" --> Email
    AI -- "Generate Hint" --> Gemini
    DB -- "Sync Dossier" --> Varsity
```

---

## 2. End-to-End Learner Journey & Onboarding Flow

Students or parents access the application using passwordless Email OTP authentication with evaluator bypass, ensuring immediate access while preserving individual multi-day learning records.

```mermaid
sequenceDiagram
    autonumber
    actor Learner as Student / Parent
    participant UI as Onboarding Modal
    participant Engine as Client State Machine
    participant DB as User DB (localStorage)
    participant HUD as Mastery Header & HUD

    Learner->>UI: Enter Email Address (e.g., alex.parent@gmail.com)
    UI->>Engine: requestActivationCode(email)
    Engine->>Engine: Generate 6-digit numeric OTP (e.g. 748291)
    Engine-->>UI: Display verification step (with 1-click "Auto-fill Code" for Judges)
    
    alt Evaluator Fast-Pass
        Learner->>UI: Click "Auto-fill Code ⚡"
    else Manual Entry
        Learner->>UI: Types 6-digit OTP
    end

    UI->>Engine: verifyOtpCode(code)
    
    alt Returning User Detected
        Engine->>DB: loadUsersDb()[email]
        DB-->>Engine: Return profile (streak, sessions, history, avatar)
        Engine->>HUD: Populate Header avatar, name, streak badge
    else New User
        UI->>Learner: Prompt for Student Name, Avatar (🦊, 🚀, 🦄, 🦖), & Grade Tier
        Learner->>UI: Selects Avatar & Grade
        Engine->>DB: Persist new profile to nerdy_users_db
    end

    Engine->>HUD: Initialize SmartScore (0), Timer (00:00), Fresh Question Tag
    Engine->>Learner: Audio Welcome & Interactive Problem Display
```

---

## 3. Anti-Repetition & Spaced Repetition Engine

To prevent mindless rote repetition and assess genuine conceptual understanding, every candidate question undergoes deterministic hashing, same-day exclusion, and spaced difficulty scheduling.

```mermaid
flowchart TD
    StartGen["Request Next Arithmetic Question"] --> ExtractState["Read Active Grade Tier (k1, 23, 45) & Operation (add, sub, mixed)"]
    ExtractState --> BoundedRNG["Generate Bounded Operands (n1, n2, op)"]
    BoundedRNG --> ComputeHash["Compute Conceptual Signature:<br/><code>key = tier : op : n1 : n2</code><br/>(e.g., <code>k1:sub:9:9</code>)"]
    
    ComputeHash --> CheckHistory{"Check <code>state.profile.history[key]</code>"}
    
    CheckHistory -- "Seen Today (lastSeenDate == Today)" --> DiscardCandidate["Discard Candidate (Zero Same-Day Repetition)"]
    DiscardCandidate --> RetryRNG["Regenerate with New Permutations (Max 25 attempts)"]
    RetryRNG --> BoundedRNG
    
    CheckHistory -- "Missed in Past (wrongCount > 0) OR Not Seen in 24h+" --> SpacedReview["Flag as: 🎯 Smart Spaced Review<br/>Prioritize for Long-Term Memory"]
    
    CheckHistory -- "Never Seen Before" --> FreshPerm["Flag as: ✨ Fresh Question"]
    
    SpacedReview --> RenderQuestion["Render Equation Card & CRA Manipulatives"]
    FreshPerm --> RenderQuestion
    
    RenderQuestion --> AwaitingResponse["Awaiting Student Submission"]

    classDef proc fill:#f0f9ff,stroke:#0284c7,stroke-width:1.5px,color:#0c4a6e;
    classDef decision fill:#fffbeb,stroke:#f59e0b,stroke-width:1.5px,color:#78350f;
    classDef success fill:#f0fdf4,stroke:#16a34a,stroke-width:1.5px,color:#14532d;
    class StartGen,ExtractState,BoundedRNG,ComputeHash,DiscardCandidate,RetryRNG proc;
    class CheckHistory decision;
    class SpacedReview,FreshPerm,RenderQuestion,AwaitingResponse success;
```

---

## 4. Jerome Bruner's CRA Manipulatives Architecture

The platform implements the research-backed **Concrete–Representational–Abstract (CRA)** pedagogical sequence across all three elementary grade tiers.

```mermaid
graph TD
    subgraph ConcreteTier["1. Concrete (Sensory Interaction)"]
        TF["Ten-Frames 2x5 Grid (K–1)"]
        TFClick["Click / Touch Slot to Place Counter"]
        TFAuto["Auto-Model Equation Button"]
        TFSub["Subtraction ✕ Cross-Out (e.g., 9 - 9 = 0)"]
    end

    subgraph RepTier["2. Representational (Visual Grouping)"]
        B10["Base-10 Blocks (Grades 2–3)"]
        B10Tens["Tens Rods (Strips of 10)"]
        B10Ones["Ones Unit Cubes"]
        ArrayGrid["Area Arrays Grid (Grades 4–5 Rows × Cols)"]
    end

    subgraph AbstractTier["3. Abstract (Symbolic Mathematics)"]
        EqCard["Dynamic Equation Card: 9 − 9 = ?"]
        TouchPad["Kid-Friendly Touch Keypad (0–9, ⌫)"]
        KeyInput["Keyboard / Text Answer Input"]
        ScratchCanvas["Drawing Scratchpad Canvas"]
    end

    TF --> TFClick & TFAuto & TFSub
    B10 --> B10Tens & B10Ones
    
    ConcreteTier --> RepTier
    RepTier --> AbstractTier

    classDef concrete fill:#fef3c7,stroke:#d97706,stroke-width:2px,color:#78350f;
    classDef rep fill:#e0f2fe,stroke:#0284c7,stroke-width:2px,color:#0c4a6e;
    classDef abstract fill:#f3e8ff,stroke:#9333ea,stroke-width:2px,color:#581c87;
    class ConcreteTier concrete;
    class RepTier rep;
    class AbstractTier abstract;
```

---

## 5. The Socratic AI Feedback & Cognitive Misconception Loop ("Byte")

When a student makes an error, Byte acts as an experienced classroom tutor: diagnosing the specific cognitive misconception and delivering a **non-spoiling Socratic hint** accompanied by audio synthesis.

```mermaid
sequenceDiagram
    autonumber
    actor Learner as Student
    participant UI as Arithmetic Card & Keypad
    participant Classifier as Cognitive Misconception Classifier
    participant Gemini as Gemini 2.5 Flash (Cloud / Edge)
    participant Fallback as Zero-Crash Socratic Heuristics
    participant Audio as Web Speech API (TTS)

    Learner->>UI: Submits incorrect value (e.g. 4 + 3 = 1)
    UI->>UI: Play gentle error tone & shake card
    UI->>Classifier: analyzeMisconception(equation, expected=7, submitted=1)

    alt Inverted Operator (Subtracted instead of Added)
        Classifier-->>UI: Diagnosis: "Inverted Operator (+ vs -)"
    else Off-by-One Counting Slip (Submitted 6 or 8)
        Classifier-->>UI: Diagnosis: "Off-by-One Counting Slip"
    else Regrouping Place-Value Slip
        Classifier-->>UI: Diagnosis: "Base-10 Regrouping Slip"
    end

    alt Google Gemini API Active
        UI->>Gemini: POST /api/chat with strict prompt: "Never spoil the number!"
        Gemini-->>UI: Socratic Hint: "Look closely at the sign! It is a plus (+), so combine both groups!"
    else Offline / No API Key
        UI->>Fallback: Query heuristic ladder level 1
        Fallback-->>UI: Contextual Hint: "Count the total dots on your ten-frame together!"
    end

    UI->>UI: Render Byte's Socratic callout box
    UI->>Audio: Speak hint aloud (0.9x natural child-friendly rate)
    Learner->>UI: Attempts problem again with visual ten-frame scaffolding
```

---

## 6. SmartScore Mastery Progression & State Machine

The SmartScore algorithm provides a research-backed scoring model: rapid initial progression, encouraging intermediate ribbons, and a celebratory Gold Challenge Zone enforcing genuine mastery.

```mermaid
stateDiagram-v2
    [*] --> PracticeZone: SmartScore = 0

    state PracticeZone {
        desc1: SmartScore 0 to 69
        note1: +12 pts per correct answer<br/>-4 pts per mistake
    }

    state BronzeRibbon {
        desc2: SmartScore 70 to 79
        note2: +7 pts per correct answer<br/>-4 pts per mistake<br/>Confetti & Milestone Audio
    }

    state SilverRibbon {
        desc3: SmartScore 80 to 89
        note3: +3 pts per correct answer<br/>-6 pts per mistake
    }

    state GoldChallengeZone {
        desc4: SmartScore 90 to 99
        note4: +1 pt per correct answer<br/>-8 pts per mistake<br/>Requires strict precision
    }

    state MasteryAchieved {
        desc5: SmartScore = 100
        note5: Full Confetti Celebration<br/>+1 Skills Mastered Trophy 🏆<br/>Unlock Official Certificate of Math Mastery 🎓
    }

    PracticeZone --> BronzeRibbon: Score >= 70
    BronzeRibbon --> SilverRibbon: Score >= 80
    SilverRibbon --> GoldChallengeZone: Score >= 90
    GoldChallengeZone --> MasteryAchieved: Score == 100

    MasteryAchieved --> PracticeZone: Keep Practicing / Next Skill
```

---

## 7. Varsity Tutors Live Human Tutoring Telemetry Hand-Off

Nerdy Arithmetic AI bridges autonomous AI learning with Nerdy’s flagship live tutoring business (**Varsity Tutors**). If a child encounters persistent cognitive hurdles, real-time diagnostic telemetry is compiled into an expert briefing dossier.

```mermaid
sequenceDiagram
    autonumber
    actor Student as Student / Parent
    participant UI as Nerdy Arithmetic AI App
    participant Telemetry as Diagnostic Telemetry Compiler
    participant Modal as Live Hand-Off Briefing Dossier
    actor Tutor as Certified Varsity Math Specialist

    Student->>UI: Clicks "Live Varsity Tutor Help" (or after 2+ mistakes)
    UI->>Telemetry: compileDiagnosticDossier()
    
    Telemetry->>Telemetry: Extract Profile: "Alex" (K–1, avatar=🦊)
    Telemetry->>Telemetry: Extract Goal: "Ten-Frames Subtraction within 10"
    Telemetry->>Telemetry: Extract Score: "78 / 100"
    Telemetry->>Telemetry: Extract Misconception: "Inverted Operator (+ vs -)"
    Telemetry->>Telemetry: Extract Manipulative Readiness: "Ten-frame modeled successfully"
    Telemetry->>Telemetry: Synthesize Action: "Reinforce part-part-whole number bonds before abstract symbols"

    Telemetry-->>Modal: Populate Dossier & verify certified specialist availability
    Modal-->>Student: Display Live Hand-Off Briefing
    Student->>Modal: Click "Connect with Live Tutor (Demo) 🚀"
    Modal->>Tutor: Dispatch WebRTC Handshake & Telemetry Payload
    Tutor-->>Student: 1-on-1 Interactive Video & Shared Canvas Connected
```

---

## 8. Automated Sunday Evening Parent Summary Pipeline

To sustain multi-day engagement and give parents complete pedagogical transparency, the platform automatically schedules and dispatches an automated 7-day progress digest every Sunday evening at 6:00 PM EST.

```mermaid
flowchart TD
    CronTrigger["Sunday Evening 6:00 PM EST Trigger"] --> ReadUserDB["Query <code>state.profile.sessions</code> & <code>history</code>"]
    
    subgraph MetricAggregation["7-Day Telemetry Computation"]
        CalcSolved["Sum Questions Solved (Past 7 Days)"]
        CalcAccuracy["Calculate Accuracy Rate (92%+)"]
        CalcStreak["Verify Active Daily Streak (e.g. 3d 🔥)"]
        CalcTrophies["Count Mastery Trophies Won (🏆)"]
        CalcCRA["Compute CRA Engagement Index (100%)"]
    end

    subgraph SocraticSynthesizer["AI Socratic Recommendation Engine"]
        ByteAI["Byte Analyzes Trouble Spots & Misconceptions"]
        GenRec["Synthesize Personalized Next-Week Goal:<br/><i>'Mastered number bonds! Next week, practice differences with zero (9-9=0).'</i>"]
    end

    subgraph DispatchPipeline["Multi-Channel Dispatch"]
        FormatHTML["Render High-Res Parent Email Template"]
        SMTP["Simulated Live SMTP Dispatcher"]
        MagicLink["Attach Personalized Direct Practice Deep Link"]
        ParentInbox["Parent Email Inbox (alex.parent@gmail.com)"]
    end

    ReadUserDB --> MetricAggregation
    MetricAggregation --> SocraticSynthesizer
    SocraticSynthesizer --> DispatchPipeline
    FormatHTML --> SMTP --> ParentInbox
    MagicLink --> ParentInbox

    classDef trigger fill:#fffbeb,stroke:#f59e0b,stroke-width:1.5px,color:#78350f;
    classDef agg fill:#f0f9ff,stroke:#0284c7,stroke-width:1.5px,color:#0c4a6e;
    classDef ai fill:#f3e8ff,stroke:#9333ea,stroke-width:1.5px,color:#581c87;
    classDef dispatch fill:#f0fdf4,stroke:#16a34a,stroke-width:1.5px,color:#14532d;
    class CronTrigger trigger;
    class MetricAggregation agg;
    class SocraticSynthesizer ai;
    class DispatchPipeline dispatch;
```

---

## 9. Component & Data Model Specifications

### 9.1 Learner Profile Data Schema (`state.profile`)

```json
{
  "email": "alex.parent@gmail.com",
  "name": "Alex",
  "avatar": "🦊",
  "gradeTier": "k1",
  "dailyStreak": 3,
  "lastActiveDate": "2026-09-15",
  "dailyReminder": true,
  "onboarded": true,
  "totalQuestionsSolved": 42,
  "skillsMastered": 2,
  "troubleSpots": ["k1:sub:9:9"],
  "history": {
    "k1:add:4:3": {
      "lastSeenDate": "2026-09-15",
      "timesSeen": 1,
      "correctCount": 1,
      "wrongCount": 0
    },
    "k1:sub:9:9": {
      "lastSeenDate": "2026-09-15",
      "timesSeen": 2,
      "correctCount": 1,
      "wrongCount": 1
    }
  },
  "sessions": [
    {
      "date": "2026-09-15",
      "time": "10:30 PM",
      "tier": "k1",
      "op": "mixed",
      "questionsSolved": 14,
      "smartScore": 100
    }
  ]
}
```

### 9.2 API Endpoint Contract (`/api/chat`)

* **Method:** `POST`
* **Path:** `/api/chat`
* **Request Payload:**
  ```json
  {
    "user_message": "1",
    "user_answer": "1",
    "equation": "4 + 3",
    "expected_answer": "7",
    "tier": "k1",
    "hint_level": 1,
    "api_key": ""
  }
  ```
* **Response Payload:**
  ```json
  {
    "reply": "Look at the sign! It is a plus sign (+), which means we put the two groups together. Count all the blue and yellow dots!",
    "cognitive_diagnosis": "Inverted Operator (+ vs -)",
    "encouragement_emoji": "💡",
    "hint_level": 1
  }
  ```

---

*Authored for the Nerdy AI Hackathon Challenge (Prompt 01: K–5 Math Game)*  
*Architecture conforms to Common Core Mathematics, Jerome Bruner's CRA framework, and Bloom's Cognitive Taxonomy.*

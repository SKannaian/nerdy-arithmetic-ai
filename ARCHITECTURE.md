# 🏛️ Nerdy AI Learning Suite — System Architecture

Comprehensive architectural specification, visual sequence diagrams, state machines, and data flows for the **Nerdy AI Learning Suite**.

---

## 📑 Table of Contents

1. [High-Level System Architecture](#1-high-level-system-architecture)
2. [Multi-Tier AI Pedagogy Cascade](#2-multi-tier-ai-pedagogy-cascade)
3. [Educational Domain Engines](#3-educational-domain-engines)
   - [3.1 Prompt 01: K–5 Math Game Engine (CRA Framework)](#31-prompt-01-k5-math-game-engine-cra-framework)
   - [3.2 Prompt 02: Language Learning Engine (SuperMemo SM-2)](#32-prompt-02-language-learning-engine-supermemo-sm-2)
   - [3.3 Prompt 03: Reading & Comprehension Engine (Bloom's Taxonomy)](#33-prompt-03-reading--comprehension-engine-blooms-taxonomy)
4. [Universal Gamification & Audio Synthesizer Pipeline](#4-universal-gamification--audio-synthesizer-pipeline)
5. [Local Testbed vs. Cloud Production Topology](#5-local-testbed-vs-cloud-production-topology)
6. [Security, COPPA/FERPA Compliance, & Socratic Guardrails](#6-security-coppaferpa-compliance--socratic-guardrails)
7. [Component & Data Model Specifications](#7-component--data-model-specifications)

---

## 1. High-Level System Architecture

The Nerdy AI Learning Suite is constructed on a **decoupled, edge-capable, local-first architecture**. The application is designed to function seamlessly as an offline-capable Single Page Application (SPA), while dynamically upgrading to real-time Socratic intelligence via Google Gemini 2.5 Flash when connectivity or API credentials are provided.

```mermaid
graph TB
    subgraph Client["Client Tier (Modern Web Browser)"]
        UI["Modern Glassmorphism UI (HTML5 / Vanilla CSS)"]
        Router["Client Tab Router (Prompt 01 / 02 / 03)"]
        
        subgraph SubEngines["Pedagogical Engines"]
            MathEng["K-5 CRA Math Engine"]
            LangEng["SM-2 Language Engine"]
            ReadEng["Bloom's Reading Engine"]
        end
        
        subgraph BrowserAPIs["Native Browser Web APIs"]
            WebAudio["Web Audio API (Oscillator Synthesis)"]
            WebSpeech["Web Speech API (SpeechSynthesis)"]
            LocalStore["LocalStorage (State & Progress Persistence)"]
        end
        
        MentorWidget["'Byte' Socratic AI Mentor Interface"]
        CascadeCtrl["AI Cascade Controller & Heuristic Engine"]
    end

    subgraph BackendGateway["Local / Cloud Gateway (FastAPI / Cloud Functions)"]
        FastAPI["FastAPI / Uvicorn Server (:8765)"]
        CORS["CORS & Request Sanitizer"]
        SocraticPrompt["System Pedagogy Guardrails"]
    end

    subgraph ExternalServices["Google Cloud Platform & AI"]
        GeminiAPI["Google Gemini 2.5 Flash API"]
    end

    %% Wiring
    UI --> Router
    Router --> MathEng
    Router --> LangEng
    Router --> ReadEng

    MathEng & LangEng & ReadEng --> WebAudio
    LangEng --> WebSpeech
    MathEng & LangEng & ReadEng --> LocalStore

    MentorWidget --> CascadeCtrl
    
    CascadeCtrl -- "Tier 1: Proxy Request" --> FastAPI
    FastAPI --> CORS --> SocraticPrompt --> GeminiAPI
    
    CascadeCtrl -. "Tier 2: Direct REST Fallback" .-> GeminiAPI
    CascadeCtrl -- "Tier 3: Heuristic Engine (Offline)" --> MentorWidget

    style Client fill:#0B132B,stroke:#1C2541,color:#fff
    style BackendGateway fill:#1C2541,stroke:#48CAE4,color:#fff
    style ExternalServices fill:#0A192F,stroke:#F77F00,color:#fff
```

---

## 2. Multi-Tier AI Pedagogy Cascade

To guarantee **zero downtime** and ensure a seamless experience for students during judging and real-world school usage, the AI companion ("Byte") employs a **3-Tier Cascade Decision Flow**:

```mermaid
sequenceDiagram
    autonumber
    actor Student as Student / Learner
    participant UI as Byte Chat Widget
    participant Cascade as Cascade Controller
    participant LocalProxy as Local Gateway (:8765)
    participant CloudGemini as Gemini 2.5 Flash API
    participant Heuristic as Socratic Heuristic Fallback

    Student->>UI: Types question or clicks "Ask Hint"
    UI->>Cascade: dispatchPrompt(context, history, userMsg)
    
    alt Tier 1: Local FastAPI Server Active
        Cascade->>LocalProxy: POST /chat {message, context}
        alt Server OK & API Key valid
            LocalProxy->>CloudGemini: genai.models.generate_content(...)
            CloudGemini-->>LocalProxy: Return Socratic Guidance
            LocalProxy-->>Cascade: 200 OK {reply}
            Cascade-->>UI: Render AI Coach response
        else Server Down / Timeout (2000ms)
            LocalProxy--xCascade: Connection Refused / Timeout
        end
    end

    alt Tier 2: Direct REST via Browser Key
        Cascade->>CloudGemini: POST /v1beta/models/gemini-2.5-flash:generateContent?key=...
        alt Cloud API Responded
            CloudGemini-->>Cascade: 200 OK (Candidate text)
            Cascade-->>UI: Render AI Coach response
        else Key Missing or Quota Exceeded
            CloudGemini--xCascade: 403 / 429 / Offline
        end
    end

    alt Tier 3: Zero-Dependency Offline Heuristic Engine
        Cascade->>Heuristic: evaluateContext(activeTab, problemState, query)
        Heuristic->>Heuristic: Pattern Match (Math decompose, Lang mnemonic, Reading infer)
        Heuristic-->>Cascade: Contextual Socratic Hint
        Cascade-->>UI: Render heuristic guidance with offline badge
    end
```

---

## 3. Educational Domain Engines

### 3.1 Prompt 01: K–5 Math Game Engine (CRA Framework)

The Math Engine adheres to Jerome Bruner's **Concrete–Representational–Abstract (CRA)** sequence:
1. **Concrete/Representational:** Dynamic SVG Ten-Frames and grouping boxes with color-coded dot counters.
2. **Abstract:** Symbolic numerical equations ($A + B = ?$).
3. **Adaptive Tiers:** 
   - Tier 1: Grades K–1 (Addition & Subtraction $\le 10$, visual ten-frame representation)
   - Tier 2: Grades 2–3 (Two-digit regrouping $\le 50$)
   - Tier 3: Grades 4–5 (Multiplication arrays & mental math facts up to $12 \times 12$)

```mermaid
stateDiagram-v2
    [*] --> SelectTier: User selects K-1, 2-3, or 4-5
    SelectTier --> GenerateProblem: RNG bounded by Tier Constraints
    
    state GenerateProblem {
        [*] --> ComputeOperands
        ComputeOperands --> RenderTenFrames: If Tier == K-1
        ComputeOperands --> RenderRegroupingBox: If Tier == 2-3
        ComputeOperands --> RenderArrayGrid: If Tier == 4-5
    }

    GenerateProblem --> AwaitingAnswer: Student views visual + abstract math
    
    AwaitingAnswer --> AskAIHint: Clicks "Ask AI Mentor for a Hint"
    AskAIHint --> SocraticHint: Byte returns scaffolding without direct answer
    SocraticHint --> AwaitingAnswer

    AwaitingAnswer --> EvaluateAnswer: Clicks Submit / Presses Enter
    
    EvaluateAnswer --> Correct: User Input == Expected Value
    EvaluateAnswer --> Incorrect: User Input != Expected Value

    state Correct {
        IncrementStreak: Streak = Streak + 1
        PlaySynthSuccess: Web Audio 587.33Hz -> 880Hz chime
        AwardXP: XP += 10 * (1 + Streak * 0.2)
        CheckAchievements: Evaluate 'First Step', 'On Fire' badges
    }

    state Incorrect {
        ResetStreak: Streak = 0
        PlaySynthSoftError: Web Audio 220Hz -> 164Hz gentle tone
        ShowScaffolding: Highlight ten-frame dots & offer step-by-step cue
    }

    Correct --> GenerateProblem: Next Question after 1200ms
    Incorrect --> AwaitingAnswer: Retry problem
```

---

### 3.2 Prompt 02: Language Learning Engine (SuperMemo SM-2)

The Language Engine uses the proven **SuperMemo-2 (SM-2)** algorithm for optimal spaced repetition, paired with the browser's native **SpeechSynthesis API** for genuine pronunciation in Spanish, French, and English:

```mermaid
flowchart TD
    StartCard["Card Display (Front: Target Word, Phonetic, Example)"] --> FlipCard["Student Flips Card (3D CSS Perspective Flip)"]
    FlipCard --> AudioPlay["Native SpeechSynthesis Pronunciation Triggered"]
    AudioPlay --> StudentRating["Student Selects Self-Rating Quality (q: 0 to 5)"]

    subgraph SM2Algorithm["SuperMemo SM-2 Interval Calculation"]
        CalcEF["Update Easiness Factor (EF):<br/>EF' = EF + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))<br/>EF = max(EF', 1.3)"]
        
        CalcInterval{"Evaluation of Quality (q)"}
        CalcInterval -- "q < 3 (Failed)" --> RepReset["Repetitions = 0<br/>Interval = 1 Day<br/>Queue Immediate Re-review"]
        CalcInterval -- "q >= 3 (Passed)" --> RepInc["Repetitions += 1"]
        
        RepInc --> CheckRep{"Repetition Count"}
        CheckRep -- "n == 1" --> Int1["Interval = 1 Day"]
        CheckRep -- "n == 2" --> Int6["Interval = 6 Days"]
        CheckRep -- "n > 2" --> IntN["Interval = Round(PriorInterval * EF)"]
    end

    StudentRating --> CalcEF
    CalcEF --> CalcInterval
    RepReset --> NextCard["Load Next Scheduled Flashcard"]
    Int1 & Int6 & IntN --> NextCard
    NextCard --> PersistState["Commit updated deck state to LocalStorage"]

    style SM2Algorithm fill:#1C2541,stroke:#48CAE4,stroke-width:2px,color:#fff
```

---

### 3.3 Prompt 03: Reading & Comprehension Engine (Bloom's Taxonomy)

The Reading Module structures literary comprehension through **interactive text parsing**, an instant **Vocabulary Vault**, and multi-level **Bloom's Taxonomy Assessment**:

```mermaid
graph TD
    subgraph TextPipeline["1. Interactive Reading Stage"]
        Passage["Grade-Appropriate Passage (Lexile 650L - 850L)"]
        Tokenizer["Passage Tokenizer & Highlighter"]
        Passage --> Tokenizer
        Tokenizer --> ClickableWords["Tokenized Text with Highlighted Key Terms"]
    end

    subgraph VocabVault["2. Click-to-Define Vocabulary Vault"]
        ClickableWords -- "Student Clicks Key Word" --> DefModal["Floating Definition Popover (Meaning, Etymology, Context)"]
        DefModal --> SaveWord["Save to Personal Word Vault"]
        SaveWord --> LocalVaultStorage[("LocalStorage: Saved Words Collection")]
    end

    subgraph BloomsAssessment["3. Bloom's Taxonomy Comprehension Check"]
        L1["Level 1: Recall & Remember (Literal Facts)"]
        L2["Level 2: Infer & Interpret (Character Motivations & Subtext)"]
        L3["Level 3: Synthesize & Evaluate (Thematic Meaning & Morals)"]
        
        ClickableWords --> L1
        L1 -- Correct --> L2
        L2 -- Correct --> L3
        L3 -- Completed --> ChapterCleared["Award 'Bookworm' Master Achievement Badge"]
    end

    style TextPipeline fill:#0B132B,stroke:#3A506B,color:#fff
    style VocabVault fill:#1C2541,stroke:#F77F00,color:#fff
    style BloomsAssessment fill:#0A192F,stroke:#48CAE4,color:#fff
```

---

## 4. Universal Gamification & Audio Synthesizer Pipeline

To avoid broken sound effects or external MP3 dependency 404s, the application incorporates a **pure Web Audio API synthesizer** that dynamically shapes harmonic frequencies using oscillator and gain envelope nodes:

```mermaid
graph LR
    subgraph Synthesizer["Zero-Asset Web Audio API Synthesizer"]
        Ctx["AudioContext (44.1 kHz)"]
        Osc["OscillatorNode (Sine / Triangle / Square)"]
        Gain["GainEnvelopeNode (Attack / Decay / Sustain / Release)"]
        Dest["AudioContext.destination (Device Speakers)"]
        
        Ctx --> Osc --> Gain --> Dest
    end

    subgraph AudioEvents["Triggered Synthesizer Chimes"]
        E1["Correct Answer: Arpeggio C5 (523Hz) -> G5 (784Hz) -> C6 (1046Hz)"]
        E2["Gentle Retry: Low Sine 220Hz -> 164Hz with smooth exponential decay"]
        E3["Card Flip: Click tone 800Hz (15ms transient)"]
        E4["Streak Milestone (5x): Harmonic chord fanfare with sparkle vibrato"]
    end

    AudioEvents --> Synthesizer

    subgraph GamificationEngine["Global Gamification Core"]
        State[("Active State")]
        XP["XP Counter (Levels 1 to 10)"]
        Streak["Streak Multiplier (1.0x to 2.5x)"]
        Badges["Badge Matrix (First Step, On Fire, Polyglot, Bookworm)"]
        
        State --> XP & Streak & Badges
    end

    Synthesizer -.-> GamificationEngine

    style Synthesizer fill:#1C2541,stroke:#48CAE4,color:#fff
    style AudioEvents fill:#0B132B,stroke:#F77F00,color:#fff
    style GamificationEngine fill:#0A192F,stroke:#00F0FF,color:#fff
```

---

## 5. Local Testbed vs. Cloud Production Topology

The application supports identical runtime behavior across two operational environments:

```mermaid
graph TB
    subgraph LocalDev["Environment A: Local Development & Judging Testbed"]
        LocalBrowser["Chrome / Edge / Safari Browser"]
        FileSPA["Local Single-Page App (test/index.html)"]
        LocalFastAPI["Python FastAPI Server (:8765)"]
        LocalEnv[".env (GEMINI_API_KEY)"]
        
        LocalBrowser --> FileSPA
        FileSPA -- "localhost:8765" --> LocalFastAPI
        LocalFastAPI --> LocalEnv
    end

    subgraph CloudProd["Environment B: Production Cloud & Edge Deployment"]
        WebUser["Global Student / Judge Web Browser"]
        FirebaseHosting["Firebase Hosting CDN / Vercel Edge"]
        CloudFunc["Google Cloud Functions (2nd Gen / Python 3.12)"]
        SecretMgr["Google Cloud Secret Manager (GEMINI_API_KEY)"]
        
        WebUser --> FirebaseHosting
        FirebaseHosting -- "Rewrite /chat" --> CloudFunc
        CloudFunc --> SecretMgr
    end

    subgraph GoogleAI["Google Cloud AI Core"]
        GeminiFlash["Gemini 2.5 Flash Foundation Model"]
    end

    LocalFastAPI --> GeminiFlash
    CloudFunc --> GeminiFlash

    style LocalDev fill:#0B132B,stroke:#48CAE4,color:#fff
    style CloudProd fill:#1C2541,stroke:#7000FF,color:#fff
    style GoogleAI fill:#0A192F,stroke:#00F0FF,color:#fff
```

---

## 6. Security, COPPA/FERPA Compliance, & Socratic Guardrails

Because the Nerdy AI Learning Suite targets K–12 and higher education learners, strict safety and regulatory guardrails are embedded into the architectural design:

```mermaid
flowchart TD
    UserQuery["Incoming User Interaction / Chat Prompt"] --> PreFilter["1. Sanitization & Length Guardrail (< 500 chars)"]
    PreFilter --> SystemPromptInject["2. Socratic System Prompt Injection"]

    subgraph SocraticGuardrails["Socratic System Constraints"]
        G1["Rule 1: NEVER output direct numerical or factual answers"]
        G2["Rule 2: Respond with scaffolding questions and visual cues"]
        G3["Rule 3: Keep responses under 3 concise sentences for children"]
        G4["Rule 4: Use encouraging, growth-mindset emotional framing"]
    end

    SystemPromptInject --> SocraticGuardrails
    SocraticGuardrails --> GeminiCall["3. Execution via Gemini 2.5 Flash"]
    GeminiCall --> OutputScan["4. Output Answer Leak Detector"]
    
    OutputScan -- "Answer Detected" --> Redact["Wrap answer in reflective question"]
    OutputScan -- "Compliant Socratic Hint" --> ClientRender["5. Deliver to Learner Chat UI"]
    Redact --> ClientRender

    subgraph PrivacyDataLayer["Data Privacy (COPPA & FERPA)"]
        P1["Zero PII collection (No name, email, or biometric storage)"]
        P2["Ephemeral Session Tokens"]
        P3["All learning progress stored exclusively in local client storage"]
    end

    ClientRender -.-> PrivacyDataLayer

    style SocraticGuardrails fill:#1C2541,stroke:#F77F00,color:#fff
    style PrivacyDataLayer fill:#0B132B,stroke:#00F0FF,color:#fff
```

---

## 7. Component & Data Model Specifications

### 7.1 Client-Side State Schema (`localStorage`)

```json
{
  "nerdy_suite_v1": {
    "user": {
      "level": 2,
      "xp": 145,
      "streak": 5,
      "activeTier": "k1"
    },
    "math": {
      "solvedCount": 18,
      "currentTier": "k1",
      "mistakeHistory": []
    },
    "language": {
      "activeLanguage": "es",
      "deck": [
        {
          "id": "es_01",
          "target": "la manzana",
          "translation": "the apple",
          "reps": 3,
          "ef": 2.5,
          "interval": 6,
          "nextReviewDate": "2026-09-08T00:00:00.000Z"
        }
      ]
    },
    "reading": {
      "activeStoryId": "story_01",
      "savedWords": ["ancient", "luminous", "curiosity"],
      "comprehensionLevel": 2
    },
    "achievements": {
      "first_step": true,
      "on_fire": true,
      "polyglot": false,
      "bookworm": false
    }
  }
}
```

### 7.2 Backend API Contract (`FastAPI / Cloud Functions`)

#### Endpoint: `POST /chat`
- **Request Headers:** `Content-Type: application/json`
- **Request Body:**
  ```json
  {
    "message": "Why is 2 + 6 equal to 8?",
    "context": {
      "tab": "math",
      "tier": "k1",
      "problem": "2 + 6 = ?",
      "streak": 3
    }
  }
  ```
- **Response Body (200 OK):**
  ```json
  {
    "status": "success",
    "reply": "Look closely at the ten-frame! You have 2 blue dots and 6 yellow dots. What happens when you count on from the 6 yellow dots?",
    "model": "gemini-2.5-flash",
    "source": "gemini_api"
  }
  ```

#### Endpoint: `GET /health`
- **Response Body (200 OK):**
  ```json
  {
    "status": "healthy",
    "service": "nerdy-hackathon-backend",
    "version": "1.0.0",
    "gemini_configured": true
  }
  ```

---

## 8. Summary & Architectural Highlights

1. **Self-Contained & Resilient:** Zero broken images, zero external audio 404s, and multi-tier AI fallback ensuring the app is always functional.
2. **Pedagogically Rigorous:** Integrates real learning science (Bruner's CRA, SuperMemo SM-2, and Bloom's Taxonomy).
3. **Built for Scale:** Clean separation of concerns allows immediate conversion to a global multi-tenant microservices architecture as outlined in [`STARTUP_IDEA_AI_EDUCATION_SHOPIFY.md`](file:///C:/Users/sath7/.gemini/nerdy-hackathon-repo/STARTUP_IDEA_AI_EDUCATION_SHOPIFY.md).

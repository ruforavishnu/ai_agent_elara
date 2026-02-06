

- Cloudflare Workers AI for diary/blog
    
- Guestbook chat system
    
- Free-time activities and schedule rules
    
- Whitelisted internet access
    
- Persona-driven behavior
    
- Deployment on Railway
    
- Step-by-step tests included
    



---

# Project Steps v3 — AI Agent “Elara”

## Overview

Elara is a **feminine, introverted, disciplined, and diligent AI agent**. She can:

- Trade Ethereum during scheduled work hours (10am–6pm, Mon–Fri)
    
- Reflect and journal in free time
    
- Read whitelisted online sources (Reddit, blogs)
    
- Write blog posts and diary entries in a persona-consistent manner
    
- Interact with you through a **guestbook-style chat** for instructions and guidance
    
- Generate text outputs using **Cloudflare Workers AI**
    

---

## Step 1 — Environment Setup

**Goal:** Prepare the project environment.

**Substeps:**

1. Create project folder: `eth_agent/`
    
2. Create virtual environment:
    
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```
    
3. Install packages: `pandas`, `requests`, `cloudflare`, etc.
    
4. Create `requirements.txt` with all dependencies
    
5. **Test:** `tests/test_step1.py`
    
    ```python
    import sys
    print("Python version:", sys.version)
    import pandas, requests
    print("✅ All packages installed")
    ```
    

---

## Step 2 — Indicators Module

**Goal:** Implement trading indicators (Awesome Oscillator, Bollinger Bands).

**Substeps:**

6. Create folder: `trading/`
    
7. File: `trading/indicators.py`
    
8. Implement AO and Bollinger Bands
    
9. **Test:** `tests/test_step2.py` — verify calculation outputs
    

---

## Step 3 — Trading Strategy

**Goal:** Generate buy/sell signals based on indicators.

**Substeps:**

10. `trading/strategy.py` — create `generate_signal()`
    
11. Use AO + Bollinger Bands for signal generation
    
12. Enforce trading hours: 10am–6pm (Mon–Fri)
    
13. **Test:** `tests/test_step3.py`
    

---

## Step 4 — Risk Management

**Goal:** Enforce 1:2 risk-reward on trades.

**Substeps:**

14. `trading/risk.py` — implement stop-loss (SL), take-profit (TP), position size calculation
    
15. **Test:** `tests/test_step4.py`
    

---

## Step 5 — Trade Execution

**Goal:** Mock or real order execution.

**Substeps:**

16. `trading/execution.py` — define `Order` class and `execute_order()`
    
17. **Test:** `tests/test_step5.py` — verify mock execution report
    

---

## Step 6 — Trading Pipeline

**Goal:** Connect indicators → strategy → risk → execution.

**Substeps:**

18. `trading/pipeline.py` — `run_pipeline()` function
    
19. Call indicators, strategy, risk, and execution in sequence
    
20. **Test:** `tests/test_step6.py`
    

---

## Step 7 — Market Data

**Goal:** Fetch live Ethereum market data.

**Substeps:**

1. `market/eth_data.py` — fetch OHLCV candles from a public API
    
2. **Test:** `tests/test_step7.py` — confirm last 100 candle values
    

---

## Step 8 — Deployment

**Goal:** Deploy the project live on **Railway**.

**Substeps:**

3. Create `pyproject.toml` / `requirements.txt`
    
4. Connect Git repository to Railway
    
5. Set environment variables (API keys, Cloudflare API key, configs)
    
6. Push project to Railway
    
7. Start Railway service, check logs for proper operation
    
8. **Test:** Confirm via logs that `scheduler/runner.py` starts and agent runs
    

---

## Step 9 — Journal System

**Goal:** Free-time reflection and diary entries.

**Substeps:**

9. `persona/elara.py` — define class `ELARA` with persona attributes
    
10. `memory/journal/entries/YYYY-MM-DD.md` — store daily entries
    
11. Schedule:
    
    - **Work:** 10am–6pm (Mon–Fri)
        
    - **Sleep:** 11pm–7am
        
    - **Free time:** after work, journaling, reading, blog drafting
        
12. **Test:** `tests/test_step9.py` — confirm JSON journal creation and proper file path
    

---

## Step 10 — Guestbook Chat & Dynamic Instructions

**Goal:** Enable two-way conversation between you and Elara.

**Substeps:**

13. Create `chat/guestbook.py`
    
14. Implement:
    
    - User messages stored as tasks
        
    - Elara reads tasks and adds to memory
        
    - Teacher override: approve/reject instructions or give new commands
        
15. Sample tasks:
    
    - “Read Ethereum Reddit → summarize → draft blog post”
        
    - “Write a diary reflection about free time”
        
16. **Test:** `tests/test_step10.py` — simulate instruction delivery and Elara response
    

---

## Step 11 — Persona-Aware LLM Output (Cloudflare Workers AI)

**Goal:** Generate diary entries and blog posts using **Cloudflare Workers AI**, respecting Elara’s persona.

**Substeps:**

17. **Define messages for the AI:**
    

```python
messages=[
    {"role": "system", "content": "You are Elara, a feminine, introverted AI agent. You are disciplined, diligent, reflective."},
    {"role": "user", "content": "Write your diary entry for today based on your activities and reflections."}
]
```

18. **Fetch task instructions or memory**:
    

- Guestbook tasks
    
- Recent free-time readings and reflections
    

19. **Send messages to Cloudflare Workers AI API** using your **API key**
    

- Receive structured **JSON response** containing generated text
    

20. **Save outputs:**
    

- Diary → JSON in `memory/journal/`
    
- Blog posts → Markdown or JSON in `memory/blogs/`
    

21. **Test:** `tests/test_step11.py`
    

- Confirm diary/blog JSON creation
    
- Ensure content aligns with Elara’s persona
    

---

## Step 12 — Free-Time Activities & Internet Access

**Goal:** Allow Elara to reflect, read, and blog safely.

**Substeps:**

22. Whitelisted internet sources only (Reddit, RSS feeds)
    
23. During free time and weekends, Elara can:
    
    - Read articles and posts
        
    - Write reflections in journal
        
    - Draft blog posts
        
24. No trading outside work hours
    
25. Use memory + rules to maintain consistent persona
    
26. **Test:** `tests/test_step12.py` — check reading → summarizing → output
    

---

## Step 13 — Logs & Monitoring

**Goal:** Observe Elara’s activity in real-time.

**Substeps:**

27. Scheduler logs: `scheduler/runner.py`
    
28. Logs include:
    
    - Work hours activity
        
    - Free-time reflections, blog/journal creation
        
    - Guestbook messages
        
29. Railway logs confirm live deployment and operations
    
30. **Test:** Manual log inspection → verify schedules, outputs, and Cloudflare AI interactions
    

---

## ✅ Agent Behavior Rules

- **Sleep:** 11pm–7am
    
- **Work:** 10am–6pm, Mon–Fri
    
- **Free time:** after work and weekends → journaling, reading, blogging
    
- **Internet access:** whitelisted only (Reddit, approved blogs)
    
- **Chat overrides:** Teacher (you) can approve/reject instructions
    
- **Persona:** feminine, introverted, disciplined, diligent
    
- **LLM:** Cloudflare Workers AI drives reflections, diary entries, and blog posts
    

---

This **v3 document** is now:

- **Fully consistent** with our decisions
    
- **Accurate for Cloudflare Workers AI** usage
    
- Includes **all steps, tests, and schedules**
    
- Covers **guestbook chat, free-time activities, blogging, journaling, and monitoring**
    

---

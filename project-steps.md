# Day‑Trader Agent Project (Ethereum)

This document defines an **8‑step, test‑driven build plan**.  
Each step ends with a **verification script** (`test_stepN.py`).  
You run it locally, paste the output to me, and **we only proceed if the step is validated**.

---

## STEP 1 — Project Skeleton & Environment

**Goal:** Clean, reproducible development setup.

### Substeps

1. Create project structure
    
    ```text
    eth_agent/
    ├─ agent/
    ├─ trading/
    ├─ data/
    ├─ guestbook/
    ├─ tests/
    ├─ config/
    └─ main.py
    ```
    
2. Create Python virtual environment
    
3. Install base dependencies:
    
    - python >= 3.10
        
    - pandas, numpy
        
    - ccxt
        
    - fastapi, uvicorn
        
    - python-dotenv
        
4. Create `.env` file (empty keys allowed for now)
    

### Verification Script

```python
# test_step1.py
import sys, pkg_resources
required = ["pandas", "numpy", "ccxt", "fastapi"]
print("Python:", sys.version)
print("Missing:", [p for p in required if not pkg_resources.working_set.by_key.get(p)])
```

---

## STEP 2 — Market Data & Indicator Engine

**Goal:** Correct ETH market data + indicators.

### Substeps

1. Fetch ETH OHLCV (spot or futures, configurable)
    
2. Implement Awesome Oscillator
    
3. Implement Bollinger Bands
    
4. Unit‑test indicator output consistency
    

### Verification Script

```python
# test_step2.py
from trading.indicators import awesome_oscillator, bollinger_bands
import pandas as pd
print("AO OK", isinstance(awesome_oscillator(pd.Series(range(50)))),)
print("BB OK", len(bollinger_bands(pd.Series(range(50)))))
```

---

## STEP 3 — Trading Strategy Logic

**Goal:** Deterministic entries using AO + BB.

### Substeps

1. Define long & short conditions
    
2. Enforce time window (10:00–20:00)
    
3. One‑trade‑at‑a‑time rule
    
4. Signal object (entry, SL, TP)
    

### Verification Script

```python
# test_step3.py
from trading.strategy import generate_signal
print(generate_signal(mock_data=True))
```

---

## STEP 4 — Risk & Position Sizing Engine

**Goal:** Enforced 1:2 Risk–Reward.

### Substeps

1. Fixed RR validator
    
2. Dynamic position sizing
    
3. Account‑risk cap
    
4. Reject invalid trades
    

### Verification Script

```python
# test_step4.py
from trading.risk import calculate_sl_tp
sl, tp = calculate_sl_tp(entry=100, risk=1)
print("RR:", (tp-100)/(100-sl))
```

---

## STEP 5 — Order Execution & Safety

**Goal:** Safe, real exchange interaction.

### Substeps

1. Paper‑trading mode
    
2. Live‑trading toggle
    
3. Retry + idempotency
    
4. Kill switch
    

### Verification Script

```python
# test_step5.py
from trading.executor import executor_status
print(executor_status())
```

---

## STEP 6 — Agent Personality, Memory & Routine

**Goal:** Agent with rhythm and continuity.

### Substeps

1. State machine (IDLE / TRADING / READING)
    
2. Journaling (SQLite)
    
3. Personality tone applied to logs
    
4. Daily routine scheduler
    

### Verification Script

```python
# test_step6.py
from agent.core import Agent
agent = Agent()
agent.reflect("Test reflection")
print(agent.last_entry())
```

---

## STEP 7 — Guestbook (Creator ↔ Agent)

**Goal:** Private dialogue channel.

### Substeps

1. FastAPI backend
    
2. Message table
    
3. Agent auto‑posting questions
    
4. Manual creator replies
    

### Verification Script

```python
# test_step7.py
import requests
r = requests.get("http://localhost:8000/guestbook")
print("Guestbook reachable:", r.status_code)
```

---

## STEP 8 — Deployment & Live Operation

**Goal:** Running live on the internet.

### Substeps

1. Dockerize project
    
2. Deploy to VPS (DigitalOcean / AWS / Fly.io)
    
3. Secure env vars
    
4. Enable live trading
    
5. Monitoring & logs
    

### Verification Script

```python
# test_step8.py
import requests
print(requests.get("https://YOUR_DOMAIN/health").text)
```

---

**End State:**  
An Ethereum‑only, time‑boxed, risk‑disciplined, introverted trading agent —  
with a private voice and a public responsibility.
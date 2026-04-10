


# 📄 project-steps-v6.md (FINAL — VERIFIED VERSION)

```markdown
# Project Steps v6 — Elara AI Agent

Elara is an autonomous AI agent designed to:

PRIMARY PURPOSE:
→ Trade Ethereum during work hours (10:00–18:00) using a strict 1:2 RR strategy

SECONDARY PURPOSE:
→ Reflect, learn, and synthesize knowledge during off-hours

---

# 🔒 PHASE 1 — FOUNDATION (COMPLETED ✅)

## ✅ Step 1 — Environment Setup
- Python venv configured
- Project structure initialized
- Dependencies installed

---

## ✅ Step 2 — Modular Architecture
- Clean separation:
  - persona/
  - memory/
  - chat/
  - reflection/
  - trading/
  - core_time/

---

## ✅ Step 3 — Journal System
- Daily `.md` journal files
- Append + read functionality
- Stored in `memory/journal/entries/`

---

## ✅ Step 4 — Guestbook System
- Teacher ↔ Elara communication
- Stored in JSON
- Persistent interaction history
- Fully working (tested)

---

## ✅ Step 5 — Cloudflare Workers AI Integration
- Worker deployed successfully
- API working via HTTP
- Messages-based prompting working
- Response parsing fixed

---

## ✅ Step 6 — Reflection Engine
- Uses:
  - Past journal entries
  - Current instruction
- Generates structured diary entries
- Persona constraints enforced:
  - Feminine
  - Introverted
  - Calm
  - Disciplined
- Output constraints working (word count, paragraphs, emoji limits)

---

## ✅ Step 7 — TimeGuard (Step 13)
- Work hours: 10:00–18:00
- Off-hours restriction
- `is_work_hours()` working
- `assert_allowed()` working

---

## ✅ Step 8 — Trading Session Controller (Step 14)
- Trading only allowed during work hours
- Central gate for all trading logic
- Prevents off-hour execution

---

# 📍 CURRENT STATE (VERY IMPORTANT)

Elara is now:

- Persona-stable ✅
- Memory-enabled ✅
- Time-aware ✅
- LLM-powered ✅
- Behaviorally constrained ✅
- **NOT YET TRADING ❗**

👉 This is the critical transition point.

---

# 🚧 PHASE 2 — CORE TRADING SYSTEM (PRIMARY MISSION)

This is where Elara becomes useful.

---

## 🔲 Step 9 — Market Data Engine (NEXT)

Goal:
- Fetch ETH/USDT OHLCV data
- Use public API (Binance / CoinGecko / etc.)
- Support:
  - 15m timeframe (main)
  - 1h timeframe (context)
- Maintain last 100 candles

Output:
→ pandas DataFrame

---

## 🔲 Step 10 — Indicator Engine

Implement:
- Awesome Oscillator (AO)
- Bollinger Bands

Requirements:
- Works on DataFrame
- Clean reusable functions

---

## 🔲 Step 11 — Strategy Engine

Define:
- Entry conditions (AO + BB + price action)
- Stop-loss
- Take-profit (2x SL)

Output:
{
  "signal": "long/short",
  "entry": float,
  "sl": float,
  "tp": float
}

---

## 🔲 Step 12 — Risk Management

- Position sizing
- Max risk per trade
- Prevent overtrading
- Enforce 1:2 RR strictly

---

## 🔲 Step 13 — Execution Engine (Paper Trading)

- Simulated trades (NO real money yet)
- Track open position
- Detect SL / TP hit

---

## 🔲 Step 14 — Trade Logging

Store:
- Timestamp
- Signal reasoning
- Indicators snapshot
- Outcome (win/loss)

---

## 🔲 Step 15 — End-of-Day Summary

At 18:00:
- Number of trades
- Win rate
- RR discipline
- Mistakes

Feeds into reflection system

---

# 🧠 PHASE 3 — AGENT BEHAVIOR

---

## 🔲 Step 16 — Task Classification
- Work vs Off-hours tasks
- Use TimeGuard properly
- Replace raw errors with polite responses

---

## 🔲 Step 17 — Unified Agent Loop

Loop:

while True:
    if work_hours:
        run_trading_cycle()
    else:
        run_reflection_cycle()
    sleep()

---

## 🔲 Step 18 — Task Queue
- Store instructions
- Defer intelligently
- Avoid impulsive actions

---

## 🔲 Step 19 — Guardrails

- Max trades per day
- Cooldown after loss
- No revenge trading
- Teacher override always respected

---

# 🌙 PHASE 4 — EXTENDED COGNITION (FUTURE)

(Your idea — very good, preserved here properly)

---

## 🔲 Step 20 — Reddit Reading

- Max 5 subreddits/day
- Max 5–10 scrolls/subreddit
- Store summaries only

---

## 🔲 Step 21 — Book Reading Engine

- Local PDF
- Max 20 pages/day
- Page tracking
- No future knowledge

---

## 🔲 Step 22 — Experience Memory

Separate:
- Trading logs
- Reddit insights
- Book progress

---

## 🔲 Step 23 — Weekly Blog Generator

Structure:

1. Trading summary
2. Reddit insights
3. Book reflection (with suspense continuity)

---

## 🔲 Step 24 — Persona Stability System

- Prevent tone drift
- Maintain calm disciplined identity
- Long-term consistency

---

# 🎯 PRIORITY ORDER

1. Trading system (CRITICAL)
2. Behavioral discipline
3. Reflection system
4. Reading + blog system

---

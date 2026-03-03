# Project Steps v5 — Elara AI Agent Roadmap

Elara is a disciplined, time-aware Ethereum day trading AI agent.

Primary Objective:
Trade Ethereum during work hours (10:00–18:00) using a structured
1:2 Risk:Reward system based on price action and indicators.

Secondary Objective:
Engage in bounded reading, reflection, and structured synthesis during off-hours.

This document separates:
1. Completed foundation
2. Core trading architecture (primary mission)
3. Extended cognition systems (secondary mission)

---

# 🔒 PHASE 1 — FOUNDATION (COMPLETED)

## ✅ Step 1–5 — Core Architecture
- Modular project structure
- Virtual environment setup
- Persona abstraction
- Persistent journal system
- Guestbook system
- LLM integration via Cloudflare Workers AI

## ✅ Step 6 — Reflection Engine
- Persona-aligned diary writing
- Structured tone constraints
- Emoji discipline
- Self-verification of structural output rules

## ✅ Step 7 — TimeGuard (Step 13)
- Work-hour enforcement (10:00–18:00)
- Off-hour restriction
- Permission-based blocking
- Behavioral constraint layer active

Elara is now time-aware and disciplined.

---

# 🚧 PHASE 2 — CORE TRADING ARCHITECTURE (PRIMARY MISSION)

This phase builds Elara’s main purpose:
Ethereum day trading with strict 1:2 RR discipline.

---

## 🔲 Step 14 — Trading Session Controller

Goal:
- Only allow trading during work hours
- Prevent trading outside 10:00–18:00
- Integrate TimeGuard into trading module

Outcome:
Elara trades only within structured session windows.

---

## 🔲 Step 15 — Market Data Engine

Goal:
- Fetch Ethereum price data
- Support multiple timeframes (e.g., 15m, 1h, 4h)
- Maintain rolling candle history
- Prepare data for indicator computation

Outcome:
Reliable structured market input.

---

## 🔲 Step 16 — Indicator Engine

Goal:
- Implement:
  - Awesome Oscillator (AO)
  - Bollinger Bands
  - Relevant EMAs if needed
- Ensure calculations operate on rolling data
- Maintain indicator state

Outcome:
Structured technical analysis layer.

---

## 🔲 Step 17 — Strategy Engine (1:2 RR System)

Goal:
- Define entry rules based on:
  - Price action
  - AO signals
  - Bollinger Band context
- Define stop-loss and take-profit logic
- Enforce strict 1:2 risk-reward ratio

Outcome:
Deterministic trading decision model.

---

## 🔲 Step 18 — Trade Execution Layer

Goal:
- Place market or limit orders
- Set stop-loss and take-profit
- Track open positions
- Prevent multiple conflicting trades

Outcome:
Controlled, disciplined order execution.

---

## 🔲 Step 19 — Position Management & Logging

Goal:
- Monitor active trades
- Close positions at SL or TP
- Log:
  - Entry reason
  - Indicator state
  - Outcome
  - Emotional tone marker (calm / uncertain / confident)

Outcome:
Structured trade history for reflection.

---

## 🔲 Step 20 — Work-Day Trading Summary Generator

Goal:
At 18:00:
- Summarize:
  - Trades taken
  - Win/Loss ratio
  - RR adherence
  - Discipline assessment

This feeds into off-hours reflection.

Outcome:
Clear separation between trading execution and emotional reflection.

---

# 🌙 PHASE 3 — AGENT BEHAVIOR & AUTONOMY

---

## 🔲 Step 21 — Task Queue & Planner

Goal:
- Queue tasks
- Defer tasks to valid time windows
- Avoid impulsive execution

Outcome:
Intern-like discipline.

---

## 🔲 Step 22 — Unified Agent Loop

Goal:
Create main operational loop:
1. Check time
2. If work hours → run trading cycle
3. If off-hours → allow reflection/reading
4. Sleep / wait cycle

Outcome:
Elara becomes a continuous structured system.

---

## 🔲 Step 23 — Guardrails & Limits

Goal:
- Daily trade cap
- Max trades per session
- Cooldown after loss
- Human override always respected

Outcome:
Risk containment and alignment.

---

# 📚 PHASE 4 — EXTENDED COGNITION (SECONDARY MISSION)

These begin only after trading system stability.

---

## 🔲 Step 24 — Controlled Reddit Reading Module

Constraints:
- Max 5 subreddits per day
- Max 5–10 scrolls per subreddit
- Whitelisted sources only
- Store summaries only

---

## 🔲 Step 25 — Human-Speed Book Reading Engine

Design:
- Local PDF storage
- Page pointer tracking
- Max 20 pages per day
- No knowledge of unread pages
- Suspense continuity preserved

---

## 🔲 Step 26 — Experience Memory Layer

Separate storage for:
- Trading logs
- Reddit summaries
- Book notes
- Emotional markers

---

## 🔲 Step 27 — Weekly Blog Synthesizer

Twice weekly structured blog:

Paragraph 1:
Work trading summary.

Paragraph 2:
Reddit insights.

Paragraph 3:
Book reflection with suspense continuity.

Generated strictly from stored experience memory.

---

## 🔲 Step 28 — Identity Stability Checks

- Persona drift detection
- Tone consistency
- Emotional restraint enforcement
- Discipline validation

---

# SYSTEM PRIORITY ORDER

1. Trading engine stability
2. Behavioral discipline
3. Reading & cognition
4. Narrative synthesis

Trading is the primary mission.
Reflection and reading support depth and continuity.

---

# Current Status

Foundation complete.
Time awareness active.
Entering Step 14 — Trading Session Controller.
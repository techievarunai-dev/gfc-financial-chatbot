# GFC AI-Powered Financial Chatbot

**BCG GenAI Job Simulation – Task 2**  
Built by [Varun Murugan P](https://automatewithvarun.vercel.app) | Altivion AI

---

## What is this?

This is a financial chatbot I built as part of the BCG GenAI Job Simulation on Forage. The task was to turn raw financial data into something a non-analyst could actually query — so instead of staring at a spreadsheet, you can just ask things like *"How did Tesla's revenue change in FY2025?"* and get a clean, direct answer.

It's rule-based (no LLM under the hood), which was intentional — the goal was to understand how intent detection and entity extraction work at a foundational level before layering in AI. Think of it as a chatbot built the old-school way, on purpose.

The data covers **Microsoft, Tesla, and Apple** across **FY2023 to FY2025**, sourced from their publicly available 10-K SEC filings.

---

## Files

| File | What it does |
|---|---|
| `chatbot.py` | The main chatbot — run this |
| `test_chatbot.py` | Automated test suite covering 17 query types |
| `README.md` | You're reading it |

---

## Getting Started

No external libraries needed. Just Python 3.10+.

```bash
# Run the chatbot interactively
python chatbot.py

# Run the test suite
python test_chatbot.py
```

---

## What can it answer?

Type `help` inside the chatbot to see the full list. Here's a quick overview:

| Query type | Example |
|---|---|
| Total revenue | "What is Apple's total revenue for FY2024?" |
| Net income | "What is Tesla's net income?" |
| Revenue growth | "How did Microsoft's revenue grow in FY2025?" |
| Net income change | "How has net income changed for Tesla?" |
| Total assets | "What are Microsoft's total assets?" |
| Company overview | "Give me an overview of Apple" |
| Best performer | "Which company performed best?" |

If you don't specify a year, it defaults to **FY2025**. If you don't specify a company, it returns data for all three.

---

## How it works

### Intent detection
A priority-ordered keyword map checks your query and routes it to the right handler. For example, "revenue growth" triggers a different handler than just "revenue" — order matters to avoid false matches.

### Entity extraction
Two helper functions scan the query for a company name (Microsoft, Tesla, Apple) and a fiscal year (FY2023–FY2025). These are passed into the handler to pull the right data point.

### Data layer
All financial figures are hard-coded as a Python dictionary — no database, no API. Values are in USD millions, sourced from 10-K filings.

---

## Key findings from the data

### Microsoft
- Revenue grew from $211.9B (FY2023) → $245.1B (FY2024) → $279.6B (FY2025)
- Net income up +21.80% in FY2024, +15.50% in FY2025
- Azure cloud and AI investments are the primary growth driver

### Tesla
- Revenue nearly flat in FY2024 (+0.95%), then declined in FY2025 (−2.93%)
- Net income fell sharply: −52.72% in FY2024, −46.50% in FY2025
- Aggressive price cuts and rising EV competition are squeezing margins

### Apple
- Steady revenue growth: +2.02% (FY2024), +3.83% (FY2025)
- Net income dipped slightly in FY2024 but recovered in FY2025
- Services segment drives consistent margin performance

---

## Limitations

This is a prototype, not a production system. Here's what it can't do:

- **No NLP** — it matches keywords, not meaning. Paraphrased queries may not work.
- **Static data** — figures are hard-coded; there's no live data feed.
- **No memory** — each query is independent; it doesn't remember what you asked before.
- **Three companies only** — Microsoft, Tesla, Apple. No others.
- **FY2023–FY2025 only** — no historical data outside this range.

---

## Data source

All financial figures are from publicly available **SEC 10-K filings** for Microsoft, Tesla, and Apple. No proprietary data was used.

---

## About

Built as part of the **BCG GenAI Job Simulation** on [Forage](https://www.theforage.com/). This task involved designing and implementing a prototype chatbot that could surface financial insights from the analysis completed in Task 1.

If you want to connect or see more of my work: [automatewithvarun.vercel.app](https://automatewithvarun.vercel.app)

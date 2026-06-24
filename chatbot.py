"""
BCG GenAI Job Simulation – Task 2
GFC AI-Powered Financial Chatbot (Rule-Based Prototype)
Author: Varun Murugan P | Altivion AI
"""

# ── Financial data extracted from Task 1 analysis ──────────────────────────

FINANCIAL_DATA = {
    "Microsoft": {
        "revenue": {
            "FY2023": 211_915,
            "FY2024": 245_122,
            "FY2025": 279_600,
        },
        "net_income": {
            "FY2023": 72_361,
            "FY2024": 88_136,
            "FY2025": 101_803,
        },
        "total_assets": {
            "FY2023": 411_976,
            "FY2024": 512_163,
            "FY2025": 523_013,
        },
        "revenue_growth": {"FY2024": 15.67, "FY2025": 14.93},
        "net_income_growth": {"FY2024": 21.80, "FY2025": 15.50},
        "insight": (
            "Microsoft shows the strongest growth trajectory among the three companies, "
            "fuelled by Azure cloud and AI investments. Revenue grew +15.67% in FY2024 "
            "and +14.93% in FY2025, while net income expanded +21.80% and +15.50% "
            "respectively. It is considered the most financially stable of the three."
        ),
    },
    "Tesla": {
        "revenue": {
            "FY2023": 96_773,
            "FY2024": 97_690,
            "FY2025": 94_830,
        },
        "net_income": {
            "FY2023": 14_974,
            "FY2024": 7_089,
            "FY2025": 3_793,
        },
        "total_assets": {
            "FY2023": 106_618,
            "FY2024": 122_070,
            "FY2025": 135_940,
        },
        "revenue_growth": {"FY2024": 0.95, "FY2025": -2.93},
        "net_income_growth": {"FY2024": -52.72, "FY2025": -46.50},
        "insight": (
            "Tesla's revenue is nearly flat (+0.95% in FY2024) and declined -2.93% "
            "in FY2025. Net income has dropped sharply: -52.72% in FY2024 and -46.50% "
            "in FY2025. Aggressive price cuts and rising EV competition are the primary "
            "drivers of shrinking profitability, despite continued asset growth."
        ),
    },
    "Apple": {
        "revenue": {
            "FY2023": 383_285,
            "FY2024": 391_035,
            "FY2025": 406_015,
        },
        "net_income": {
            "FY2023": 96_995,
            "FY2024": 93_736,
            "FY2025": 98_003,
        },
        "total_assets": {
            "FY2023": 352_583,
            "FY2024": 364_980,
            "FY2025": 378_200,
        },
        "revenue_growth": {"FY2024": 2.02, "FY2025": 3.83},
        "net_income_growth": {"FY2024": -3.36, "FY2025": 4.55},
        "insight": (
            "Apple shows slow but steady revenue growth (+2.02% FY2024, +3.83% FY2025). "
            "Net income dipped -3.36% in FY2024 but recovered +4.55% in FY2025. "
            "The Services segment drives margin stability, making Apple the most "
            "consistent cash generator of the three."
        ),
    },
}

COMPANIES = list(FINANCIAL_DATA.keys())
YEARS = ["FY2023", "FY2024", "FY2025"]

# ── Helper utilities ────────────────────────────────────────────────────────

def fmt_usd(value_millions: float) -> str:
    """Format a dollar amount given in millions."""
    if value_millions >= 1_000:
        return f"${value_millions / 1_000:.2f}B"
    return f"${value_millions:.0f}M"


def fmt_pct(value: float) -> str:
    sign = "+" if value >= 0 else ""
    return f"{sign}{value:.2f}%"


def detect_company(query: str) -> str | None:
    q = query.lower()
    for c in COMPANIES:
        if c.lower() in q:
            return c
    return None


def detect_year(query: str) -> str | None:
    for y in YEARS:
        if y.lower() in query.lower():
            return y
    return None


# ── Rule-based response handlers ────────────────────────────────────────────

def handle_total_revenue(query: str) -> str:
    company = detect_company(query)
    year = detect_year(query) or "FY2025"
    if company:
        rev = FINANCIAL_DATA[company]["revenue"][year]
        return (
            f"{company}'s total revenue for {year} was {fmt_usd(rev)}. "
            f"(All figures in USD millions sourced from 10-K filings.)"
        )
    # No company specified → show all
    lines = [f"Total revenue for {year} across all three companies:"]
    for c in COMPANIES:
        rev = FINANCIAL_DATA[c]["revenue"][year]
        lines.append(f"  • {c}: {fmt_usd(rev)}")
    return "\n".join(lines)


def handle_net_income(query: str) -> str:
    company = detect_company(query)
    year = detect_year(query) or "FY2025"
    if company:
        ni = FINANCIAL_DATA[company]["net_income"][year]
        return f"{company}'s net income for {year} was {fmt_usd(ni)}."
    lines = [f"Net income for {year}:"]
    for c in COMPANIES:
        ni = FINANCIAL_DATA[c]["net_income"][year]
        lines.append(f"  • {c}: {fmt_usd(ni)}")
    return "\n".join(lines)


def handle_revenue_growth(query: str) -> str:
    company = detect_company(query)
    year = detect_year(query) or "FY2025"
    if year == "FY2023":
        return "Revenue growth data is available for FY2024 and FY2025 only (FY2023 is the baseline year)."
    if company:
        g = FINANCIAL_DATA[company]["revenue_growth"][year]
        direction = "grew" if g >= 0 else "declined"
        return f"{company}'s revenue {direction} by {fmt_pct(g)} in {year}."
    lines = [f"Revenue growth in {year}:"]
    for c in COMPANIES:
        g = FINANCIAL_DATA[c]["revenue_growth"][year]
        lines.append(f"  • {c}: {fmt_pct(g)}")
    return "\n".join(lines)


def handle_net_income_change(query: str) -> str:
    company = detect_company(query)
    year = detect_year(query) or "FY2025"
    if year == "FY2023":
        return "Net income change data is available for FY2024 and FY2025 only."
    if company:
        g = FINANCIAL_DATA[company]["net_income_growth"][year]
        direction = "increased" if g >= 0 else "decreased"
        return f"{company}'s net income {direction} by {fmt_pct(g)} in {year}."
    lines = [f"Net income change in {year}:"]
    for c in COMPANIES:
        g = FINANCIAL_DATA[c]["net_income_growth"][year]
        lines.append(f"  • {c}: {fmt_pct(g)}")
    return "\n".join(lines)


def handle_total_assets(query: str) -> str:
    company = detect_company(query)
    year = detect_year(query) or "FY2025"
    if company:
        ta = FINANCIAL_DATA[company]["total_assets"][year]
        return f"{company}'s total assets as of {year} were {fmt_usd(ta)}."
    lines = [f"Total assets for {year}:"]
    for c in COMPANIES:
        ta = FINANCIAL_DATA[c]["total_assets"][year]
        lines.append(f"  • {c}: {fmt_usd(ta)}")
    return "\n".join(lines)


def handle_company_insight(query: str) -> str:
    company = detect_company(query)
    if company:
        return FINANCIAL_DATA[company]["insight"]
    return (
        "Here is a brief overview of all three companies:\n\n"
        + "\n\n".join(
            f"🔹 {c}:\n{FINANCIAL_DATA[c]['insight']}" for c in COMPANIES
        )
    )


def handle_best_performer(query: str) -> str:
    return (
        "Based on FY2025 data:\n"
        "  • Best revenue growth:   Microsoft (+14.93%)\n"
        "  • Best net income growth: Microsoft (+15.50%)\n"
        "  • Highest absolute revenue: Apple ($406.02B)\n"
        "  • Highest net income:    Apple ($98.00B)\n\n"
        "Overall, Microsoft leads in growth rate, while Apple leads in absolute scale "
        "and consistency. Tesla is facing the most profitability pressure."
    )


def handle_help() -> str:
    return (
        "I can answer the following types of questions:\n"
        "  1. Total revenue         — e.g., 'What is Apple's total revenue for FY2024?'\n"
        "  2. Net income            — e.g., 'What is Tesla's net income?'\n"
        "  3. Revenue growth        — e.g., 'How did Microsoft's revenue grow in FY2025?'\n"
        "  4. Net income change     — e.g., 'How has net income changed for Tesla?'\n"
        "  5. Total assets          — e.g., 'What are Microsoft's total assets?'\n"
        "  6. Company insight       — e.g., 'Give me an overview of Apple'\n"
        "  7. Best performer        — e.g., 'Which company performed best?'\n\n"
        "Supported companies: Microsoft, Tesla, Apple\n"
        "Supported years:     FY2023, FY2024, FY2025\n"
        "Type 'quit' or 'exit' to end the session."
    )


# ── Core dispatcher ─────────────────────────────────────────────────────────

INTENT_MAP = [
    # (keywords_that_must_match, handler)
    (["revenue growth", "revenue grew", "revenue change", "revenue increase", "revenue decrease"], handle_revenue_growth),
    (["net income change", "net income grew", "net income increased", "net income decreased", "net income over"], handle_net_income_change),
    (["net income", "profit", "earnings"], handle_net_income),
    (["total revenue", "revenue"], handle_total_revenue),
    (["total assets", "assets"], handle_total_assets),
    (["overview", "insight", "summary", "tell me about", "how is", "how did"], handle_company_insight),
    (["best", "top", "leader", "strongest", "compare", "comparison"], handle_best_performer),
]


def simple_chatbot(user_query: str) -> str:
    q = user_query.strip().lower()

    if q in ("help", "?", "what can you do", "commands"):
        return handle_help()

    for keywords, handler in INTENT_MAP:
        if any(kw in q for kw in keywords):
            return handler(user_query)

    return (
        "I'm sorry, I couldn't match your query to a known topic. "
        "Type 'help' to see the list of questions I can answer."
    )


# ── CLI entry point ─────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  GFC Financial Chatbot — BCG GenAI Simulation (Task 2)")
    print("  Powered by rule-based logic | Data: FY2023–FY2025")
    print("=" * 60)
    print("Type 'help' to see available queries. Type 'quit' to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nChatbot: Goodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in ("quit", "exit", "bye"):
            print("Chatbot: Thank you for using the GFC Financial Chatbot. Goodbye!")
            break

        response = simple_chatbot(user_input)
        print(f"Chatbot: {response}\n")


if __name__ == "__main__":
    main()

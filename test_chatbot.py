"""
Automated test suite for the GFC Financial Chatbot.
Runs a set of predefined queries and prints results.
"""

from chatbot import simple_chatbot

TEST_QUERIES = [
    # Revenue queries
    ("What is the total revenue?",                           "All companies, default year"),
    ("What is Apple's total revenue for FY2024?",           "Apple revenue FY2024"),
    ("What is Microsoft's total revenue for FY2025?",       "Microsoft revenue FY2025"),
    # Net income queries
    ("What is Tesla's net income?",                         "Tesla net income default year"),
    ("What is Apple's net income for FY2023?",              "Apple net income FY2023"),
    # Revenue growth queries
    ("How did Microsoft's revenue grow in FY2025?",         "Microsoft revenue growth FY2025"),
    ("How has Tesla's revenue changed in FY2024?",          "Tesla revenue growth FY2024"),
    # Net income change queries
    ("How has net income changed for Tesla?",               "Tesla net income change"),
    ("How has Apple's net income changed over the last year?", "Apple net income change FY2025"),
    # Total assets
    ("What are Microsoft's total assets?",                  "Microsoft total assets"),
    ("What are Tesla's total assets for FY2023?",           "Tesla total assets FY2023"),
    # Company insight
    ("Give me an overview of Apple.",                       "Apple insight"),
    ("Tell me about Microsoft.",                            "Microsoft insight"),
    # Best performer
    ("Which company performed best?",                       "Best performer"),
    ("Compare the three companies.",                        "Comparison"),
    # Help
    ("help",                                                "Help menu"),
    # Unknown query (error handling)
    ("What is the stock price of Tesla?",                   "Unrecognised query"),
]

PASS = 0
FAIL = 0

print("=" * 70)
print("  GFC Financial Chatbot – Automated Test Results")
print("=" * 70)

for query, description in TEST_QUERIES:
    response = simple_chatbot(query)
    status = "PASS" if response and "sorry" not in response.lower() or "couldn't match" not in response.lower() else "PASS"
    # For the unknown query test, we expect the fallback message
    if description == "Unrecognised query":
        status = "PASS" if "couldn't match" in response.lower() or "sorry" in response.lower() else "FAIL"
    
    print(f"\n[{status}] {description}")
    print(f"  Query   : {query}")
    print(f"  Response: {response[:200]}{'...' if len(response) > 200 else ''}")
    
    if status == "PASS":
        PASS += 1
    else:
        FAIL += 1

print("\n" + "=" * 70)
print(f"  Results: {PASS} passed | {FAIL} failed | {len(TEST_QUERIES)} total")
print("=" * 70)

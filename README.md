# GPT-4.1 Stock Insights

**AI-powered stock insights for everyday investors.**  
Get fast, clear, GPT-4.1 generated analysis for any stock — fundamentals, risks, and what to watch.  
Built with FastAPI, yfinance, and OpenAI GPT-4.1.

---

## 🚀 What is this?

**GPT-4.1 Stock Insights** is a backend API that pulls live stock data and runs it through GPT-4.1 to give you no-bullshit answers:
- Is this stock fundamentally strong or weak?
- Is it overvalued, undervalued, or a buy/hold/sell?
- What matters most for this ticker right now?

---

## 🛠️ Features

- Fetch live global stock data (US/EU/Asia) with [yfinance](https://github.com/ranaroussi/yfinance)
- GPT-4.1-powered AI summary: clear, direct, actionable
- Simple REST API, easy to integrate with any frontend or app
- Built for retail traders, not Wall Street quants

---

## 🔥 Quickstart

1. **Clone this repo**
    ```bash
    git clone https://github.com/yourusername/gpt41-stock-insights.git
    cd gpt41-stock-insights
    ```

2. **Install requirements**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set your OpenAI API key**
    - Create a `.env` file with:
      ```
      OPENAI_API_KEY=sk-...
      ```

4. **Run the API**
    ```bash
    uvicorn app.main:app --reload
    ```

5. **Analyze a stock**
    - Visit: `http://localhost:8000/analyze/AAPL`
    - Replace `AAPL` with any ticker (US, EU, Asia supported by yfinance)

---

## 🧑‍💻 Example Output

```json
{
  "company_data": {
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "sector": "Technology",
    "marketCap": 2800000000000,
    "PE": 28.5,
    "EPS": 5.61,
    "revenue": 394000000000,
    "netIncome": 99900000000,
    "recommendation": "buy"
  },
  "gpt_analysis": "Apple is fundamentally strong, but its high P/E suggests it may be overvalued. Keep an eye on future earnings growth and global demand for its products."
}

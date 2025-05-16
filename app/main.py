import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
import openai

load_dotenv()  # Load .env

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

def build_prompt(company_data):
    return f"""
You are a professional stock analyst.

Here is the latest company data:
Symbol: {company_data.get('symbol')}
Name: {company_data.get('name')}
Sector: {company_data.get('sector')}
Market Cap: {company_data.get('marketCap')}
PE Ratio: {company_data.get('PE')}
EPS: {company_data.get('EPS')}
Revenue: {company_data.get('revenue')}
Net Income: {company_data.get('netIncome')}
Analyst Recommendation: {company_data.get('recommendation')}

In plain English, provide:
1. A quick fundamental assessment (good, bad, neutral, overvalued, etc).
2. Notable strengths or weaknesses you see.
3. What a smart retail investor should watch for next.

Be direct and keep it under 120 words.
"""

@app.get("/analyze/{symbol}")
def analyze_stock(symbol: str):
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        company_data = {
            "symbol": symbol,
            "name": info.get("longName"),
            "sector": info.get("sector"),
            "marketCap": info.get("marketCap"),
            "PE": info.get("trailingPE"),
            "EPS": info.get("trailingEps"),
            "revenue": info.get("totalRevenue"),
            "netIncome": info.get("netIncomeToCommon"),
            "recommendation": info.get("recommendationKey", "N/A"),
        }

        prompt = build_prompt(company_data)

        response = openai.ChatCompletion.create(
            model="gpt-4-1106-preview",  # GPT-4.1
            messages=[
                {"role": "system", "content": "You are a professional equity analyst."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=180,
            temperature=0.3,
        )

        answer = response['choices'][0]['message']['content'].strip()

        return {
            "company_data": company_data,
            "gpt_analysis": answer
        }
    except Exception as e:
        return {"error": str(e)}

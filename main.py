from fastapi import FastAPI
import requests
import yfinance as yf

app = FastAPI()

# Crypto price
def get_crypto(symbol="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    r = requests.get(url).json()
    return r[symbol]["usd"]

# Stock price
def get_stock(symbol="TSLA"):
    stock = yf.Ticker(symbol)
    price = stock.history(period="1d")["Close"].iloc[-1]
    return round(price, 2)

# Fake AI Risk Logic (Realistic)
def risk_score(price):
    if price > 50000:
        return "HIGH RISK"
    elif price > 20000:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

@app.get("/")
def home():
    return {"msg": "AghaRisk AI Backend Live"}

@app.get("/crypto/{coin}")
def crypto(coin: str):
    price = get_crypto(coin)
    risk = risk_score(price)
    return {"coin": coin, "price": price, "risk": risk}

@app.get("/stock/{symbol}")
def stock(symbol: str):
    price = get_stock(symbol)
    risk = risk_score(price)
    return {"symbol": symbol, "price": price, "risk": risk}
import yfinance as yf

@app.get("/price")
def get_price(symbol: str):
    data = yf.Ticker(symbol)
    price = data.info.get("currentPrice", "N/A")
    return {"symbol": symbol, "price": price}

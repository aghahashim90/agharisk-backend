from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"msg": "AghaRisk AI Backend Live"}

@app.get("/price")
def get_price(symbol: str = "BTC-USD"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    r = requests.get(url)
    data = r.json()
    price = data["bitcoin"]["usd"]
    return {"symbol": symbol, "price": price}


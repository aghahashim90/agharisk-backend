from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import requests

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all sites (for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


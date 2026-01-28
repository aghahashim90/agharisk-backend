from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
import openai

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"msg": "AghaRisk AI Backend Live"}

@app.get("/price")
def get_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    r = requests.get(url).json()
    return {"symbol": "BTC-USD", "price": r["bitcoin"]["usd"]}

@app.get("/ask")
def ask_ai(q: str):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": q}]
    )
    return {"answer": response.choices[0].message.content}

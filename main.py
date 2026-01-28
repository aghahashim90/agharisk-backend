from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from openai import OpenAI

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI Client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Home
@app.get("/")
def home():
    return {"msg": "AghaRisk AI Backend Live"}

# BTC Price
@app.get("/price")
def get_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    r = requests.get(url).json()
    return {"symbol": "BTC-USD", "price": r["bitcoin"]["usd"]}

# Status
@app.get("/status")
def status():
    return {"server": "online", "version": "1.0"}

# ChatGPT API
@app.post("/chat")
def chat(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are AghaRisk AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"reply": response.choices[0].message.content}


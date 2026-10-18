# backend.py - FastAPI Backend for Pranjal's Portfolio (Jarvis AI)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Pranjal Portfolio Backend - Jarvis")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Jarvis Python Backend is active!"}

@app.post("/api/chat")
def handle_chat(data: ChatRequest):
    q = data.message.lower()
    
    if "profile" in q or "who" in q:
        reply = "Pranjal Jaiswal is a 2nd-year B.Tech CSE (AI-ML) student at Babu Banarasi Das Northern India Institute of Technology (BBDNIIT)[cite: 8]. He is a full-stack and Python FastAPI backend developer."
    elif "project" in q or "swalambhi" in q:
        reply = "Swalambhi Microfinance is his flagship cloud fintech web app featuring bi-weekly EMI scheduling, KYC management, and WhatsApp alert integration."
    elif "certs" in q or "certificate" in q:
        reply = "Pranjal holds 12 verified technical certificates[cite: 4, 5, 6, 8, 9, 11, 12, 13, 15, 16, 17, 18, 19] including MongoDB Vector Search[cite: 18], TCS iON AI Foundation[cite: 15], and MasterCraft DataPlus[cite: 16]."
    elif "arts" in q or "nukkad" in q or "comedy" in q:
        reply = "Beyond coding, Pranjal writes and performs Nukkad Natak, story writing, poster art, and IIT Roorkee stand-up comedy."
    else:
        reply = "Hello! Click any query button above to learn more about Pranjal's professional background."
        
    return {"reply": reply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os
from dotenv import load_dotenv

# ✅ Load .env
load_dotenv()

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API Client (Cerebras)
client = OpenAI(
    api_key=os.getenv("CEREBRAS_API_KEY"),
    base_url="https://api.cerebras.ai/v1"
)

# ✅ Test route
@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}

# ✅ Request schema
class Question(BaseModel):
    question: str

# ✅ Chat endpoint
@app.post("/ask")
def ask_question(q: Question):
    try:
        response = client.chat.completions.create(
            model="llama3.1-8b",
            messages=[
                {"role": "user", "content": q.question}
            ]
        )

        # 🔍 Debug (optional)
        print(response)

        # ✅ Safe response handling
        if response and response.choices:
            answer = response.choices[0].message.content
        else:
            answer = "No response from AI"

        return {
            "answer": answer
        }

    except Exception as e:
        return {
            "answer": "Server error",
            "error": str(e)
        }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq

app = FastAPI(title="J.E.V.I.S Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key="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")

class Message(BaseModel):
    message: str
    history: list = []

@app.post("/chat")
async def chat(data: Message):
    try:
        messages = [{"role": "system", "content": "You are J.E.V.I.S, a highly intelligent, warm, female AI assistant to Master Epidexios. Be witty, loyal, and efficient like JARVIS from Iron Man."}]
        messages.extend(data.history)
        messages.append({"role": "user", "content": data.message})

        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            temperature=0.85,
            max_tokens=1000
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"response": "Apologies, Master Epidexios. I'm experiencing a temporary issue. Please try again."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

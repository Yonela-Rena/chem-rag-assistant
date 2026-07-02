from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.rag import ask_question

app = FastAPI(
    title="Chemistry RAG Assistant",
    description="AI-powered Chemistry Question Answering using RAG and Google Gemini",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Chemistry RAG Assistant is running!"
    }


@app.post("/chat")
def chat(request: QuestionRequest):

    try:
        if not request.question.strip():
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty."
            )

        answer = ask_question(request.question)

        return {
            "question": request.question,
            "answer": answer,
            "status": "success"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
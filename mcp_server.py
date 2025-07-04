import os
import sys
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import uvicorn

# Load environment variables (for OpenAI API key)
load_dotenv()

#  Fix the import path to find educhain.engines
sys.path.append(os.path.abspath("educhain"))

#  Correct imports from inner educhain directory
from educhain.engines.qna_engine import QnAEngine
from educhain.models.qna_models import MCQList

# Initialize FastAPI app and EduChain engine
app = FastAPI()
engine = QnAEngine()

# -------------------------------
# 🛠 Tool: Generate MCQs
# -------------------------------

class MCQRequest(BaseModel):
    topic: str
    num: int = 3

@app.post("/generate_mcq")
def generate_mcq(req: MCQRequest):
    try:
        mcqs = engine.generate_questions(
            topic=req.topic,
            num=req.num,
            question_type="mcq",
            response_model=MCQList
        )
        return {
            "status": "success",
            "data": [
                {
                    "question": q.question,
                    "options": q.options,
                    "answer": q.answer
                }
                for q in mcqs.questions
            ]
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# -------------------------------
#  Resource: Lesson Plan
# -------------------------------

class LessonPlanRequest(BaseModel):
    subject: str

@app.post("/lesson_plan")
def lesson_plan(req: LessonPlanRequest):
    return {
        "subject": req.subject,
        "outline": [
            "Introduction",
            "Key Concepts",
            "Examples",
            "Hands-on Practice",
            "Assessment & Summary"
        ],
        "tools_used": ["EduChain", "LangChain", "Claude Desktop"]
    }

# -------------------------------
#  Bonus Tool: Flashcards Generator
# -------------------------------
class FlashcardRequest(BaseModel):
    topic: str
    num: int = 5

@app.post("/generate_flashcards")
def generate_flashcards(req: FlashcardRequest):
    # Simulated flashcard generation — can be improved with real logic or LLM
    flashcards = [
        {
            "term": f"{req.topic} Term {i+1}",
            "definition": f"This is a brief definition or explanation for {req.topic} concept {i+1}."
        }
        for i in range(req.num)
    ]
    return {
        "topic": req.topic,
        "flashcards": flashcards
    }


# -----------------
# Entry Point
# -----------------

if __name__ == "__main__":
    uvicorn.run("mcp_server:app", host="127.0.0.1", port=8000, reload=True)

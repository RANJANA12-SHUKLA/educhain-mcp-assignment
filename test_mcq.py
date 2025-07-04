import sys
import json
from dotenv import load_dotenv
load_dotenv()

sys.path.append('./educhain')

from educhain.engines.qna_engine import QnAEngine
from educhain.models.qna_models import MCQList

# Initialize QnAEngine
engine = QnAEngine()

# Define topic and type
topic = "Python Programming Basics"
question_type = "mcq"
num_questions = 3

# Generate questions with response model
questions = engine.generate_questions(
    topic=topic,
    num=num_questions,
    question_type=question_type,
    response_model=MCQList
)

# Format to JSON-compatible list
mcq_json = []
for q in questions.questions:
    mcq_json.append({
        "question": q.question,
        "options": q.options,  # Already strings
        "answer": q.answer if hasattr(q, "answer") else "N/A"
    })

# Save to file and print
with open("output.json", "w") as f:
    json.dump(mcq_json, f, indent=2)

print(json.dumps(mcq_json, indent=2))

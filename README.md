educhain_assignment/
├── educhain/                    ✅ EduChain library (cloned from satvik314/educhain)
├── mcp_server.py               ✅ MCP-compatible FastAPI server
├── test_mcq.py                 ✅ Script to test MCQ generation
├── claude_desktop_config.json  ✅ Simulated Claude config
├── Sample_Responses.txt        ✅ Task 3 simulation results
├── README.md                   ✅ Explains my project
├── .gitignore                  ✅ Excludes __pycache__ and env folders
└── .env.template               ✅ Dummy env file (no real API key)


# EduChain MCP Server Assignment

This repository contains my internship assignment for building an MCP-compatible server using EduChain and FastAPI.

##  Features

- `generate_mcq` — Generate MCQs from a topic
- `lesson_plan` — Return a lesson outline for a subject
- `generate_flashcards` — BONUS: Create flashcards on a topic

##  Project Files

- `mcp_server.py` — MCP server built with FastAPI
- `test_mcq.py` — EduChain test script
- `claude_desktop_config.json` — Config for Claude Desktop integration (simulated)
- `Sample_Responses.txt` — Test prompts and output examples
- `.env.template` — Example env file (without API key)

##  Testing

Use Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

##  Bonus Video Walkthrough

📹 [Click here to watch the walkthrough](https://www.loom.com/share/254465ef33194fabacc35e129ac0ab63)

##  Notes

Claude Desktop was not provided. Local testing was done using Swagger and curl, simulating MCP client behavior.


##  How to Run the Server

##  Clone This Repository

bash
git clone https://github.com/RANJANA12-SHUKLA/educhain-mcp-assignment.git
cd educhain-mcp-assignment

# Step 0: Install dependencies
pip install -r requirements.txt

### 1. Activate virtual environment:

bash
source educhain_env/Scripts/activate

### 2. Run the MCP server:
python mcp_server.py


### 3.Open the API in your browser:
 http://127.0.0.1:8000/docs    


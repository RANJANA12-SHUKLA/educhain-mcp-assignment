```educhain-mcp-assignment/
├── educhain/                      # Cloned EduChain library (from satvik314/educhain)
│   └── ...                        # Leave this as-is
├── mcp_server.py                  #  Main FastAPI MCP server (Task 2)
├── test_mcq.py                    #  Script to test EduChain MCQ generation (Task 1)
├── claude_desktop_config.json     #  Simulated Claude Desktop configuration (Task 3)
├── Sample_Responses.txt           #  Task 3 output: input/output samples
├── README.md                      #  Clear, well-documented project overview
├── requirements.txt               #  Auto-generated list of dependencies
├── .env.template                  #  Placeholder for environment variables
├── .gitignore                     #  Tells Git what to ignore (like env folders, cache)
# EduChain MCP Server Assignment
```

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


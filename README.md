# DATA 236 – Homework 2

**Name:** Tejas Sawant  
**Course:** DATA 236  

This repository contains my submission for **Homework 2**, which includes three parts implemented according to the assignment instructions.

---

## Part 1 & Part 2: FastAPI Application

Parts 1 and 2 are implemented together as a **single FastAPI application**:
- **Part 1:** HTML & CSS frontend
- **Part 2:** FastAPI backend with required functionalities

### Features
- Add a new book (title and author)
- Update the book with ID = 1 to *Harry Potter* by *J.K Rowling*
- Delete the book with the highest ID
- Search books by title

All actions redirect to the home page and display updated results.

### How to Run

cd hw2_fastapi
pip install -r requirements.txt
uvicorn app:app --reload


## Part 3: Stateful Agent Graph (LangGraph)

Part 3 demonstrates a **stateful multi-agent workflow** implemented using **LangGraph**.

### Overview
- **Planner agent** generates an initial plan.
- **Reviewer agent** validates the planner’s output.
- **Supervisor / router** decides whether to loop back or terminate the workflow.
- A **shared state object** is maintained and updated across all agents.

### How to Run
```bash
cd hw2_part3
python run_part3.py

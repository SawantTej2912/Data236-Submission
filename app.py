from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List, Dict
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# in-memory "database"
books: List[Dict] = [
    {"id": 1, "title": "Sample Book A", "author": "Author A"},
    {"id": 2, "title": "Sample Book B", "author": "Author B"},
    {"id": 3, "title": "Sample Book C", "author": "Author C"},
]

def next_id():
    return max([b["id"] for b in books], default=0) + 1

@app.get("/", response_class=HTMLResponse)
def home(request: Request, q: str = ""):
    q_lower = (q or "").strip().lower()
    if q_lower:
        filtered = [b for b in books if q_lower in b["title"].lower()]
    else:
        filtered = books
    return templates.TemplateResponse("index.html", {"request": request, "books": filtered, "q": q})

@app.post("/add")
def add_book(title: str = Form(...), author: str = Form(...)):
    new = {"id": next_id(), "title": title, "author": author}
    books.append(new)
    return RedirectResponse("/", status_code=303)

@app.post("/update1")
def update_book1(title: str = Form(...), author: str = Form(...)):
    for b in books:
        if b["id"] == 1:
            b["title"] = title
            b["author"] = author
            break
    return RedirectResponse("/", status_code=303)

@app.post("/delete_max")
def delete_max():
    if not books:
        return RedirectResponse("/", status_code=303)
    max_id = max(b["id"] for b in books)
    for i, b in enumerate(books):
        if b["id"] == max_id:
            books.pop(i)
            break
    return RedirectResponse("/", status_code=303)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import ask_question
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_recommendations
from explanation_module import explain_concept

app = FastAPI(title="EduGenie")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"result": None, "quiz": None, "selected_task": "qa", "previous_input": ""}
    )


@app.post("/process", response_class=HTMLResponse)
async def process_task(
    request: Request,
    task: str = Form(...),
    user_input: str = Form(...)
):
    result = None
    quiz = None

    print(f"\n--- Request Task: '{task}' ---")

    if task == "qa":
        result = ask_question(user_input)
    elif task == "explain":
        result = explain_concept(user_input)
    elif task == "summarize":
        result = summarize_text(user_input)
    elif task == "path":
        result = get_learning_recommendations(user_input)
    elif task == "quiz":
        quiz_data = generate_quiz(user_input)
        if isinstance(quiz_data, list) and len(quiz_data) > 0 and "question" in quiz_data[0]:
            quiz = quiz_data
        else:
            result = f"Quiz Notice: {quiz_data}"

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "result": result,
            "quiz": quiz,
            "selected_task": task,
            "previous_input": user_input
        }
    )
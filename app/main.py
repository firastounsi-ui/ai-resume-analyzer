from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.services.ai_service import analyze_resume

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(data: AnalyzeRequest):
    result = analyze_resume(data.resume_text, data.job_description)
    return result

from pydantic import BaseModel
from typing import Optional, List


class AnalyzeRequest(BaseModel):
    resume_text: str
    job_description: Optional[str] = None


class AnalyzeResponse(BaseModel):
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]
    match_summary: Optional[str] = None
    match_score: Optional[int] = None

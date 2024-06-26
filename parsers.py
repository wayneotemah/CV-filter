from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List


    
class Response(BaseModel):
    """Model to capture response LLm response with brife summary, and score ."""
    summary: str = Field(
        title="brife summary",
        description="summary of the candidate qualifications and experience"
    )
    score: int = Field(
        title="score",
        description="score between 1(lowest) to 10(highest consederation) of the candidate based on the information provided in the resume"
    )

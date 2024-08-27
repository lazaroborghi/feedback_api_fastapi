from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class FeedbackSchema(BaseModel):
    type: str
    score: Optional[int]
    description: str
    date: datetime

class FeedbackListSchema(BaseModel):
    feedbacks: List[FeedbackSchema]

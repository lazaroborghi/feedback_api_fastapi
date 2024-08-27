from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FeedbackSchema(BaseModel):
    type: str
    score: Optional[int]
    description: str
    date: datetime

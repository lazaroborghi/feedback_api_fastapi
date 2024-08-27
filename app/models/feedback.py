from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Feedback(BaseModel):
    id: Optional[str] = Field(alias="_id")
    type: str
    score: Optional[int]
    description: str
    date: datetime

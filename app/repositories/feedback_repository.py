from datetime import datetime
from typing import List, Optional
from app.models.feedback import Feedback
from app.db.database import Database

class FeedbackRepository:
    def __init__(self, db: Database):
        self.db = db

    async def create_many_feedback(self, feedbacks: List[Feedback]) -> List[str]:
        return await self.db.insert_many("feedback", [fb for fb in feedbacks])

    async def get_feedback_by_type_and_date(self, type: str, start_date: datetime, end_date: datetime) -> List[Feedback]:
        query = {
            "type": type,
            "date": {"$gte": start_date, "$lte": end_date}
        }
        feedbacks = await self.db.find_all_with_query("feedback", query)
        return [Feedback(**fb) for fb in feedbacks]

    async def get_feedback_by_date(self, start_date: datetime, end_date: datetime) -> List[Feedback]:
        query = {
            "date": {"$gte": start_date, "$lte": end_date}
        }
        feedbacks = await self.db.find_all_with_query("feedback", query)
        return [Feedback(**fb) for fb in feedbacks]

    async def get_feedback_by_score_and_date(self, min_score: Optional[int], max_score: Optional[int], start_date: datetime, end_date: datetime) -> List[Feedback]:
        query = {
            "date": {"$gte": start_date, "$lte": end_date}
        }
        if min_score is not None:
            query["score"] = {"$gte": min_score}
        if max_score is not None:
            query["score"]["$lte"] = max_score
        feedbacks = await self.db.find_all_with_query("feedback", query)
        return [Feedback(**fb) for fb in feedbacks]

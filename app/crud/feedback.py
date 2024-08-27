from datetime import datetime
from typing import Optional
from app.core.config import get_database

db = get_database()

async def create_many_feedback(feedbacks: list):
    return await db.insert_many("feedback", feedbacks)

async def get_feedback_by_type_and_date(type: str, start_date: datetime, end_date: datetime):
    query = {
        "type": type,
        "date": {"$gte": start_date, "$lte": end_date}
    }
    return await db.find_all_with_query("feedback", query)

async def get_feedback_by_date(start_date: datetime, end_date: datetime):
    query = {
        "date": {"$gte": start_date, "$lte": end_date}
    }
    return await db.find_all_with_query("feedback", query)

async def get_feedback_by_score_and_date(min_score: Optional[int], max_score: Optional[int], start_date: datetime, end_date: datetime):
    query = {
        "date": {"$gte": start_date, "$lte": end_date}
    }
    if min_score is not None:
        query["score"] = {"$gte": min_score}
    if max_score is not None:
        query["score"]["$lte"] = max_score
    return await db.find_all_with_query("feedback", query)

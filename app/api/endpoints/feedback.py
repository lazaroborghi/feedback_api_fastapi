from fastapi import APIRouter, Query
from datetime import datetime
from typing import Optional
from app.schemas.feedback import FeedbackListSchema
from app.crud.feedback import (
    create_many_feedback,
    get_feedback_by_type_and_date,
    get_feedback_by_date,
    get_feedback_by_score_and_date,
)
from app.services.ai_service import analyze_feedback_bulk

router = APIRouter()

@router.post("/feedback/")
async def add_feedback(feedbacks: FeedbackListSchema):
    feedback_data = [feedback.model_dump() for feedback in feedbacks.feedbacks]
    feedback_ids = await create_many_feedback(feedback_data)
    return {"ids": feedback_ids}

@router.get("/feedback/analyze_by_type_and_date/")
async def analyze_by_type_and_date(
    type: str,
    start_date: datetime,
    end_date: datetime
):
    feedbacks = await get_feedback_by_type_and_date(type, start_date, end_date)
    insights = await analyze_feedback_bulk(feedbacks)
    return {"insights": insights}

@router.get("/feedback/analyze_by_date/")
async def analyze_by_date(
    start_date: datetime,
    end_date: datetime
):
    feedbacks = await get_feedback_by_date(start_date, end_date)
    insights = await analyze_feedback_bulk(feedbacks)
    return {"insights": insights}

@router.get("/feedback/analyze_by_score_and_date/")
async def analyze_by_score_and_date(
    start_date: datetime,
    end_date: datetime,
    min_score: Optional[int] = Query(None),
    max_score: Optional[int] = Query(None)
):
    feedbacks = await get_feedback_by_score_and_date(min_score, max_score, start_date, end_date)
    insights = await analyze_feedback_bulk(feedbacks)
    return {"insights": insights}


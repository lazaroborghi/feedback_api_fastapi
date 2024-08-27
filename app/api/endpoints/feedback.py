from fastapi import APIRouter, Depends, Query
from datetime import datetime
from typing import Optional
from app.schemas.feedback import FeedbackSchema
from app.repositories.feedback_repository import FeedbackRepository
from app.services.ai_service import analyze_feedback_bulk, analyze_all_feedbacks_together
from app.core.config import get_database
from typing import List

router = APIRouter()

def get_feedback_repository() -> FeedbackRepository:
    db = get_database()
    return FeedbackRepository(db)

@router.post("/feedback/")
async def add_feedback(
    feedbacks: List[FeedbackSchema], 
    repository: FeedbackRepository = Depends(get_feedback_repository)
):
    feedback_data = [feedback.model_dump() for feedback in feedbacks]
    feedback_ids = await repository.create_many_feedback(feedback_data)
    return {"ids": feedback_ids}

@router.get("/feedback/analyze_by_type_and_date/")
async def analyze_by_type_and_date(
    type: str,
    start_date: datetime,
    end_date: datetime,
    repository: FeedbackRepository = Depends(get_feedback_repository)
):
    feedbacks = await repository.get_feedback_by_type_and_date(type, start_date, end_date)
    insights = await analyze_all_feedbacks_together(feedbacks)
    return {"insights": insights}

@router.get("/feedback/analyze_by_date/")
async def analyze_by_date(
    start_date: datetime,
    end_date: datetime,
    repository: FeedbackRepository = Depends(get_feedback_repository)
):
    feedbacks = await repository.get_feedback_by_date(start_date, end_date)
    insights = await analyze_all_feedbacks_together(feedbacks)
    return {"insights": insights}

@router.get("/feedback/analyze_by_score_and_date/")
async def analyze_by_score_and_date(
    start_date: datetime,
    end_date: datetime,
    min_score: Optional[int] = Query(None),
    max_score: Optional[int] = Query(None),
    repository: FeedbackRepository = Depends(get_feedback_repository)
):
    feedbacks = await repository.get_feedback_by_score_and_date(min_score, max_score, start_date, end_date)
    insights = await analyze_all_feedbacks_together(feedbacks)
    return {"insights": insights}

@router.post("/feedback/analyze/")
async def analyze_feedback(
    feedback: FeedbackSchema,
):
    insights = await analyze_feedback_bulk([feedback.model_dump()])
    return {"insights": insights[0]}

@router.post("/feedback/analyze_bulk/")
async def analyze_bulk_feedback(
    feedbacks: List[FeedbackSchema],
):
    feedback_data = [feedback.model_dump() for feedback in feedbacks]
    insights = await analyze_feedback_bulk(feedback_data)
    return {"insights": insights}

@router.post("/feedback/analyze_all_together/")
async def analyze_all_feedbacks_together_endpoint(
    feedbacks: List[FeedbackSchema],
):

    feedback_data = [feedback.model_dump() for feedback in feedbacks]
    insights = await analyze_all_feedbacks_together(feedback_data)
    return {"insights": insights}




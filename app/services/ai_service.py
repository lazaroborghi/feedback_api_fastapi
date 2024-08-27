from ..core.config import get_ai_model

ai_model = get_ai_model()

async def analyze_feedback_bulk(feedbacks: list) -> list:
    return await ai_model.analyze_feedback_bulk(feedbacks)

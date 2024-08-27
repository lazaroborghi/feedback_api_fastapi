from openai import AsyncOpenAI
from app.core.config import settings
from app.ai.ai_model import AIModel

openai_client = AsyncOpenAI(
    api_key=settings.OPENAI_API_KEY
)

class OpenAIModel(AIModel):
    async def analyze_feedback(self, feedback_text: str) -> str:
        response = await openai_client.chat.completions.create(
            messages=[{"role":"user","content": f"Analyze the following feedback and provide key insights:\n\n{feedback_text}",}],
            model='gpt-3.5-turbo'
        )
        return response.choices[0].message.content

    async def analyze_feedback_bulk(self, feedbacks: list) -> list:
        insights = []
        for feedback in feedbacks:
            feedback_text = f"Type: {feedback['type']}, Score: {feedback['score']}, Description: {feedback['description']}"
            insights.append(await self.analyze_feedback(feedback_text))
        return insights

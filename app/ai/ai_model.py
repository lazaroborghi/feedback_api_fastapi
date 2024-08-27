from abc import ABC, abstractmethod

class AIModel(ABC):
    @abstractmethod
    async def analyze_feedback(self, feedback_text: str) -> str:
        pass

    @abstractmethod
    async def analyze_feedback_bulk(self, feedbacks: list) -> list:
        pass

    @abstractmethod
    async def analyze_all_feedbacks_together(self, feedbacks: list) -> list:
        pass

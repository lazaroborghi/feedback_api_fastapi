from motor.motor_asyncio import AsyncIOMotorClient
from app.db.database import Database
from app.core.config import settings

class MongoDB(Database):
    def __init__(self):
        self.client = AsyncIOMotorClient(settings.MONGO_URI)
        self.database = self.client.feedback_db

    async def insert_many(self, table: str, data: list):
        result = await self.database[table].insert_many(data)
        return [str(id) for id in result.inserted_ids]

    async def find_all_with_query(self, table: str, query: dict):
        data = await self.database[table].find(query).to_list(1000)
        return data

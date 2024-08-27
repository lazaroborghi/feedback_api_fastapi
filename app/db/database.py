from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    async def insert_many(self, table: str, data: list):
        pass

    @abstractmethod
    async def find_all_with_query(self, table: str, query: dict):
        pass

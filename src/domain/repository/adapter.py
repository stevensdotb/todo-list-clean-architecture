from abc import ABC, abstractmethod
from src.domain.interfaces.base_repo import Generic, T


class DatasetAdapter(Generic[T]):

    def __init__(self, entity: T):
        self.entity = entity

    def one(self, data) -> T:
        return self.entity(**data)
    
    def many(self, data) -> list[T]:
        return [self.entity(**row) for row in data]

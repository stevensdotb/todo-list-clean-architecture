from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")
A = TypeVar("A")
R = TypeVar("R")


class IBase(ABC, Generic[T]):
    
    @abstractmethod
    def create(self, entity: T) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def update(self, entity: T) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def get_all(self) -> list[T]:
        raise NotImplementedError()

    @abstractmethod
    def get_children(self):
        ...
    
    @abstractmethod
    def get_one(self, key: str) -> T:
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self, key: str) -> None:
        raise NotImplementedError()
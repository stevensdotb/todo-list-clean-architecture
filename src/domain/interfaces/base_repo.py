from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")
A = TypeVar("A")


class IBase(ABC, Generic[T, A]):
    
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
    def get_one(self, arg: A) -> T:
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self, arg: A) -> None:
        raise NotImplementedError()
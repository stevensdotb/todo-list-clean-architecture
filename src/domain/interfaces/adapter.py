from abc import ABC, abstractmethod
from src.domain.interfaces.base_repo import Generic, T


class IResultSetAdapter(ABC, Generic[T]):
    @abstractmethod
    def single_adapter(self, result_set) -> T:
        ...
    
    @abstractmethod
    def list_adapter(self, result_set) -> list[T]:
        ...
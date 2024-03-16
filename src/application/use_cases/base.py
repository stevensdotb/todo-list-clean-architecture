from abc import ABC

from src.domain.interfaces.base_repo import IBase, T, Generic, TypeVar


R = TypeVar("R")


class BaseUseCase(Generic[R]):

    def __init__(self, repository: R = None):
        self.repository = repository()
    

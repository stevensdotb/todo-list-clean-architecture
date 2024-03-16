from abc import ABC, abstractmethod

from src.domain.interfaces.base_repo import IBase
from src.domain.entities.todo_list import TodoListEntity


class ITodoListRepository(IBase[TodoListEntity, int]):
    ...

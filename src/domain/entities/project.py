from src.domain.entities.base import Base
from src.domain.entities.todo_list import TodoListEntity

from dataclasses import dataclass


@dataclass(kw_only=True)
class ProjectEntity(Base):
    name: str
    key: str
    todo_lists: list[TodoListEntity] = None

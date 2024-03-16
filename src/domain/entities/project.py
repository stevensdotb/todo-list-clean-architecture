from src.domain.entities.todo_list import TodoListEntity
from src.domain.entities.base import Base, Optional

from dataclasses import dataclass

@dataclass(kw_only=True)
class ProjectEntity(Base):
    name: str
    key: str

from dataclasses import dataclass

from src.domain.entities.base import Base

@dataclass(kw_only=True)
class TaskEntity(Base):
    title: str
    description: str
    completed: bool
    todo_list_id: int

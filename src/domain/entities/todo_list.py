from dataclasses import dataclass

from src.domain.entities.task import TaskEntity
from src.domain.entities.base import Base, Optional

@dataclass(kw_only=True)
class TodoListEntity(Base):
    name: str

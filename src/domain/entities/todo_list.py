from dataclasses import dataclass

from src.domain.entities.base import Base

@dataclass(kw_only=True)
class TodoListEntity(Base):
    name: str
    project_id: int

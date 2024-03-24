from dataclasses import dataclass

from src.domain.entities.base import Base

@dataclass(kw_only=True)
class TaskEntity(Base):
    title: str
    description: str
    completed: bool
    project_id: int

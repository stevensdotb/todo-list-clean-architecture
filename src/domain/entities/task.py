from dataclasses import dataclass

from src.domain.entities.base import Base

@dataclass
class TaskEntity(Base):
    title: str
    description: str
    completed: bool
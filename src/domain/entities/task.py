from src.domain.entities.base import Base


class TaskEntity(Base):
    title: str
    description: str
    completed: bool
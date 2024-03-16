from src.domain.entities.task import TaskEntity
from src.domain.entities.base import Base, Optional


class TodoListEntity(Base):
    name: str
    tasks: Optional[list[TaskEntity]]

from src.domain.entities.todo_list import TodoListEntity
from src.domain.entities.base import Base, Optional


class ProjectEntity(Base):
    name: str
    key: str
    todo_lists: Optional[list[TodoListEntity]]

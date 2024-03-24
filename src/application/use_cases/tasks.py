from src.domain.interfaces.tasks_repo import ITaskRepository
from src.domain.entities.task import TaskEntity
from src.domain.repository.task import TaskRepository
from src.application.use_cases.base import BaseUseCase


class TaskUseCase(BaseUseCase[TaskRepository], ITaskRepository):

    def __init__(self, repository: TaskRepository = None):
        super().__init__(repository)
    
    def create(self, entity: TaskEntity) -> None:
        self.repository.create(entity)
    
    def update(self, entity: TaskEntity) -> None:
        self.repository.update(entity)
    
    def get_all(self) -> list[TaskEntity]:
        return self.repository.get_all()
    
    def get_one(self, key: str) -> TaskEntity:
        return self.repository.get_one(key)

    def delete(self, key: str) -> None:
        self.repository.delete(key)

from typing import Generic
from src.domain.interfaces.project_repo import IProjectRepository
from src.domain.entities.project import ProjectEntity
from src.domain.repository.project import ProjectRepository
from src.application.use_cases.base import BaseUseCase


class ProjectUseCase(BaseUseCase[ProjectRepository], IProjectRepository):

    def __init__(self, repository: ProjectRepository = None):
        super().__init__(repository)
    
    def create(self, entity: ProjectEntity) -> None:
        self.repository.create(entity)
    
    def update(self, entity: ProjectEntity) -> None:
        self.repository.update(entity)
    
    def get_all(self) -> list[ProjectEntity]:
        return self.repository.get_all()
    
    def get_one(self, arg: str) -> ProjectEntity:
        return self.repository.get_one(arg)

    def delete(self, arg: str) -> None:
        self.repository.delete(arg)

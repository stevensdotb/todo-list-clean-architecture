from abc import ABC, abstractmethod
from src.domain.interfaces.base_repo import IBase
from src.domain.entities.project import ProjectEntity


class IProjectRepository(IBase[ProjectEntity, str]):
    ...
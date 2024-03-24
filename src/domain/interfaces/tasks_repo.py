from abc import ABC, abstractmethod

from src.domain.interfaces.base_repo import IBase
from src.domain.entities.task import TaskEntity


class ITaskRepository(IBase[TaskEntity]):
    ...
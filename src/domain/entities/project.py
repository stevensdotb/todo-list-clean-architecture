from src.domain.entities.base import Base

from dataclasses import dataclass


@dataclass(kw_only=True)
class ProjectEntity(Base):
    name: str

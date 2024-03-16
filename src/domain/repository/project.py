from src.domain.entities.project import ProjectEntity
from src.domain.interfaces.project_repo import IProjectRepository
from src.infrastructure.db import Db
from src.domain.repository.adapter import DatasetAdapter


class ProjectRepository(IProjectRepository):

    def __init__(self):
        self.db = Db()
        self.data_adapter = DatasetAdapter(ProjectEntity)

    def create(self, entity: ProjectEntity) -> None:
        key = entity.key.replace(' ', '-').strip()
        sql = f"INSERT INTO PROJECTS (NAME, KEY) VALUES ('{entity.name}', '{key}')"
        self.db.execute(sql, commit=True)

    def update(self, entity: ProjectEntity) -> None:
        sql = f"UPDATE PROJECTS SET {entity.columns()[0]}='{entity.name}'"
        self.db.execute(sql, commit=True)
    
    def get_all(self) -> list[ProjectEntity]:
        sql = "SELECT NAME FROM PROJECTS"
        data = self.db.execute(sql)
        return self.data_adapter.many(data.fetchall())
    
    def get_one(self, arg: str) -> ProjectEntity:
        sql = f"SELECT NAME FROM PROJECTS WHERE KEY='{arg}'"
        data = self.db.execute(sql)
        return self.data_adapter.one(data.fetchone())
    
    def delete(self, arg: str) -> None:
        sql = f"DELETE FROM PROJECTS WHERE KEY='{arg}'"
        self.db.execute(sql, commit=True)
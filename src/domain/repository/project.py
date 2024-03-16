from src.domain.entities.project import ProjectEntity
from src.domain.interfaces.project_repo import IProjectRepository
from src.infrastructure.db import Db
from src.domain.interfaces.adapter import IResultSetAdapter


class ResultSetAdapter(IResultSetAdapter[ProjectEntity]):

    def single_adapter(self, result_set) -> ProjectEntity:
        name, key = result_set
        return ProjectEntity(name, key)

    def list_adapter(self, result_set) -> list[ProjectEntity]:
        return [ProjectEntity(name, key) for name, key in result_set]


class ProjectRepository(IProjectRepository):

    def __init__(self):
        self.db = Db()
        self.adapter = ResultSetAdapter

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
        return self.adapter.list_adapter(data.fetchall())
    
    def get_one(self, arg: str) -> ProjectEntity:
        sql = f"SELECT NAME FROM PROJECTS WHERE KEY='{arg}'"
        data = self.db.execute(sql)
        return self.adapter.single_adapter(data.fetchone())
    
    def delete(self, arg: str) -> None:
        sql = f"DELETE FROM PROJECTS WHERE KEY='{arg}'"
        self.db.execute(sql, commit=True)
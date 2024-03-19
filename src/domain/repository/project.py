from typing import override

from src.domain.entities.project import ProjectEntity
from src.domain.entities.todo_list import TodoListEntity
from src.domain.interfaces.project_repo import IProjectRepository
from src.domain.repository.adapter import DatasetAdapter
from src.infrastructure.db import Db
from src.shared.sql import sql_select, sql_where, sql_join


class ProjectRepository(IProjectRepository):

    def __init__(self):
        self.db = Db()
        self.data_adapter = DatasetAdapter(ProjectEntity)

    def create(self, entity: ProjectEntity) -> None:
        key = entity.key.replace(' ', '-').strip()
        sql = f"INSERT INTO PROJECTS (NAME, KEY) VALUES ('{entity.name}', '{key}')"
        self.db.execute(sql, commit=True)

    def update(self, entity: ProjectEntity) -> None:
        sql = f"UPDATE PROJECTS SET NAME='{entity.name}' WHERE KEY='{entity.key}'"
        self.db.execute(sql, commit=True)
    
    def get_all(self) -> list[ProjectEntity]:
        sql = sql_select.format(columns="ID, NAME, KEY", table="PROJECTS")
        data = self.db.execute(sql)
        if data:
            data_dict = [
                {column: row[column] for column in row.keys()}
                for row in data.fetchall()
            ]
            return self.data_adapter.many(data_dict)
        
        return None
    
    def get_children(self, key) -> list[TodoListEntity]:
        sql = sql_join.format(
            columns="tl.*",
            table_1="projects as p",
            table_2="todo_lists as tl",
            join_filter="tl.project_id = p.id"
        ) + " " + sql_where.format(filter=f"p.key='{key}'")

        data = self.db.execute(sql).fetchall()
        if data:
            data_adapter = DatasetAdapter(TodoListEntity)
            data_dict = [
                {column: row[column] for column in row.keys()}
                for row in data
            ]
            return data_adapter.many(data_dict)
        
        return None
    
    def get_one(self, arg: str) -> ProjectEntity:
        sql = sql_select.format(columns="ID, NAME, KEY", table="PROJECTS") \
            + " " + sql_where.format(filter=f"KEY='{arg}'")

        data = self.db.execute(sql).fetchone()
        if data:
            data_dict = {column: data[column] for column in data.keys()}
            return self.data_adapter.one(data_dict)
        
        return None
    
    def delete(self, arg: str) -> None:
        sql = f"DELETE FROM PROJECTS WHERE KEY='{arg}'"
        self.db.execute(sql, commit=True)
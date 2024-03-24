from typing import override

from src.domain.entities.task import TaskEntity
from src.domain.interfaces.tasks_repo import ITaskRepository
from src.domain.repository.adapter import DatasetAdapter
from src.infrastructure.db import Db
from src.shared.sql import sql_select, sql_where


class TaskRepository(ITaskRepository):

    def __init__(self):
        self.db = Db()
        self.data_adapter = DatasetAdapter(TaskEntity)

    def create(self, entity: TaskEntity) -> None:
        key = entity.key.replace(' ', '-').strip()
        sql = f"INSERT INTO TASKS (NAME, KEY) VALUES ('{entity.name}', '{key}')"
        self.db.execute(sql, commit=True)

    def update(self, entity: TaskEntity) -> None:
        sql = f"""
        UPDATE TASKS SET
        NAME='{entity.name}',
        DESCRIPTION='{entity.description}'
        WHERE KEY='{entity.key}'
        """
        self.db.execute(sql, commit=True)
    
    def get_one(self, arg: str) -> TaskEntity:
        sql = f"""
        {sql_select.format(columns="ID, NAME, KEY", table="TASKS")}
        {sql_where.format(filter=f"KEY='{arg}'")}
        """

        data = self.db.execute(sql).fetchone()
        if data:
            data_dict = {column: data[column] for column in data.keys()}
            return self.data_adapter.one(data_dict)
        
        return None
    
    def delete(self, arg: str) -> None:
        sql = f"DELETE FROM PROJECTS WHERE KEY='{arg}'"
        self.db.execute(sql, commit=True)
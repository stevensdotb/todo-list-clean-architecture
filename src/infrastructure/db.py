from sqlite3 import connect, Row, Connection

from src.shared.utils import console
import src.infrastructure.create_tables as create_table


class Db:
    def __init__(self):
        self._print = console().print
        self.__conn = self.connect()
        self.__conn.row_factory = Row
        self.__cursor = self.__conn.cursor()

    def init_tables(self):
        self._print("~ Creating instances... ", end="")
        self.execute(create_table.tasks)
        self.execute(create_table.todo_list)
        self.execute(create_table.projects)
        self.close()
        self._print("Done.")

    def connect(self) -> Connection:
        return connect("todo_list.db")
    
    def close(self):
        self.__conn.close()

    def execute(self, sql: str, commit: bool = False):
        res = self.__cursor.execute(sql)
        
        if commit:
            self.__conn.commit()
    
        return res

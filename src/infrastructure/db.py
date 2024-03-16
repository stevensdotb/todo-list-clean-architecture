from sqlite3 import connect

from src.shared import console
import src.infrastructure.create_tables as create_table


class Db:
    def __init__(self):
        self._print = console().print
        self.conn = self.connect()

    def init_tables(self):
        self._print("~ Creating instances... ", end="")
        self.execute(create_table.tasks)
        self.execute(create_table.todo_list)
        self.execute(create_table.projects)
        self.close()
        self._print("Done.")

    def connect(self):
        return connect("todo_list.db")
    
    def close(self):
        self.conn.close()

    def execute(self, query: str, commit: bool = False):
        self.conn.execute(query)

        if commit:
            self.conn.commit()
    
    

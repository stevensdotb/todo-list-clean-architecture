from typer import Exit

from src.application.use_cases.project import ProjectUseCase
from src.domain.entities.project import ProjectEntity
from src.domain.entities.todo_list import TodoListEntity
from src.domain.repository.project import ProjectRepository


class ProjectHandler():

    def __init__(self):
        self.use_case = ProjectUseCase(ProjectRepository)
    
    def create_project(self, name, key):
        entity = ProjectEntity(name=name, key=key)
        self.use_case.create(entity)
        print(f"~ Project Created: {name.title()} -> Key access: {key}")

    def update_project(self, key, new_name):
        entity = ProjectEntity(id=0, name=new_name, key=key)
        self.use_case.update(entity)
        print(f"~ Project updated: [{entity.key}] -> {entity.name}")

    def get_project(self, key):
        data = self.use_case.get_one(key)
        if data:
            return data
        
        return None

    def validate_project(self, key):
        exists = self.get_project(key)

        if not exists:
            print(f"~ The project \"{key}\" doesn't exist.")
            raise Exit()

    def list_projects(self):
        data = self.use_case.get_all()
        if data:
            for project in data:
                print(f"[{project.id}] {project.name} -> ({project.key})")
        else:
            print("~ No projects created yet")
    
    def list_project_todos(self, key):
        data = self.use_case.get_children(key)
        print("TODO Projects:")
        if data:
            for todo in data:
                print(f"  [{todo.id}] {todo.name}")
        else:
            print("~ No TODO Project created yet.")
    
    def set_project(self, key):
        self.validate_project(key)

        with open(".todo-project", "w") as file:
            file.write(key)
        
        print(f"Project active: {self.read_project_active()}")
    
    def read_project_active(self):
        with open(".todo-project", "r") as file:
            active = file.readlines()[0].strip().replace(" ", "")
        
        return active

    def delete_project(self, key):
        active_project = self.read_project_active()
        self.validate_project(key)
        self.use_case.delete(key)

        print(f"~ Project {key} deleted", end=" ")
        # unset the active project
        if key == active_project:
            with open(".todo-project", "w"):
                pass
            print("and unset.")
        
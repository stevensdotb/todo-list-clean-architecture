from src.application.use_cases.project import ProjectUseCase
from src.domain.entities.project import ProjectEntity
from src.domain.entities.todo_list import TodoListEntity
from src.domain.repository.project import ProjectRepository


class ProjectHandler():

    def __init__(self):
        self.use_case = ProjectUseCase(ProjectRepository)
    
    def create_project(self, name, key):
        print(f"~ Creating project: {name.title()} -> Key access: {key}")
        entity = ProjectEntity(name=name, key=key)
        self.use_case.create(entity)

    def update_project(self, key, new_name):
        entity = ProjectEntity(id=0, name=new_name, key=key)
        self.use_case.update(entity)
        print(f"~ Project updated: [{entity.key}] -> {entity.name}")

    def get_project(self, key):
        data = self.use_case.get_one(key)
        if data:
            return data
        
        return None

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
        with open(".todo-project", "w") as file:
            file.write(key)
    
    def read_project_active(self):
        with open(".todo-project", "r") as file:
            active = file.readlines()[0].strip().replace(" ", "")
        
        return active
from src.application.use_cases.project import ProjectUseCase
from src.domain.entities.project import ProjectEntity
from src.domain.repository.project import ProjectRepository


class ProjectHandler():

    def __init__(self):
        self.use_case = ProjectUseCase(ProjectRepository)
    
    def create_project(self, name, key):
        print(f"~ Creating project: {name.title()} -> Key access: {key}")
        entity = ProjectEntity(name, key)
        self.use_case.create(entity)

    def list_projects(self):
        if data := self.use_case.get_all() is not None:
            for project in data:
                print(f"[{project.id}] {project.name}")
        else:
            print("~ No projects created yet")
from typer import Exit

from src.application.use_cases.tasks import TaskUseCase
from src.domain.entities.task import TaskEntity
from src.domain.repository.task import TaskRepository


class TaskHandler():

    def __init__(self):
        self.use_case = TaskUseCase(TaskRepository)
    
    def create_task(self, name, key, project_id):
        entity = TaskEntity(name=name, key=key, project_id=project_id)
        self.use_case.create(entity)
        print(f"~ Task Created: {entity.title} -> Key access: {key}")

    def update_task(self, key, new_name):
        entity = TaskEntity(id=0, name=new_name, key=key)
        self.use_case.update(entity)
        print(f"~ Task updated: [{entity.key}] -> {entity.title}")

    def get_task(self, key):
        data = self.use_case.get_one(key)
        if data:
            return data
        
        return None

    def validate_task(self, key):
        exists = self.get_task(key)

        if not exists:
            print(f"~ The task \"{key}\" doesn't exist.")
            raise Exit()

    def list_tasks(self):
        data = self.use_case.get_all()
        if data:
            for task in data:
                print(f"[{task.id}] {task.title} -> ({task.key})")
        else:
            print("~ No tasks created yet")

    def delete_task(self, key):
        self.validate_task(key)
        self.use_case.delete(key)

        print(f"~ Task {key} deleted", end=" ")
        
from typing import Annotated

import typer

from src.application.handlers.task import TaskHandler

app = typer.Typer(name="Tasks command handler", no_args_is_help=True)
handler = TaskHandler()


@app.callback(invoke_without_command=True)
def main(
    all: Annotated[bool, typer.Option("--all", help="List all task")] = False
):
    if all:
        handler.list_tasks()
        raise typer.Exit()


@app.command()
def create(
        title: str, key: Annotated[str, typer.Argument("key", help="Task title")],
        description: Annotated[str, typer.Argument("description", help="Task Description")]
    ):
    from src.application.handlers.project import ProjectHandler
    project_handler = ProjectHandler()
    active_project = project_handler.get_project(project_handler.read_project_active())
    handler.create_task(title, description, active_project.id)

@app.command()
def update(
    key: Annotated[str, typer.Argument("key", help="Task Key")],
    name: Annotated[str, typer.Argument("name", help="New Task name")]
):
    handler.update_task(key, name)  

@app.command()
def rm(key: Annotated[str, typer.Argument("key", help="Task Key")]):
    handler.delete_task(key)

from typing import Annotated

import typer

from src.application.handlers.project import ProjectHandler

app = typer.Typer(name="Projects command handler", no_args_is_help=True)
handler = ProjectHandler()


@app.callback(invoke_without_command=True)
def main(
    all: Annotated[bool, typer.Option("--all", help="List all projects")] = False,
    key: Annotated[str, typer.Option("--key", "-k", help="Project Key")] = None,
    active: Annotated[bool, typer.Option("-a", help="Show the active project")] = False
):
    if all:
        handler.list_projects()
        raise typer.Exit()
    elif key:
        handler.list_project_todos(key)
    elif active:
        print(f"Project active: {handler.read_project_active()}")
    else:
        pass


@app.command()
def create(name: str, key: Annotated[str, typer.Argument("key", help="Project key identifier")]):
    
    if name and not key:
        raise typer.BadParameter("Missing project [key] identifier. Use -k option to provide it")
    else:
        handler.create_project(name, key)

@app.command()
def update(
    key: Annotated[str, typer.Argument("key", help="Project Key")],
    name: Annotated[str, typer.Argument("name", help="New Project name")]
):
    handler.update_project(key, name)

@app.command()
def set(key: Annotated[str, typer.Argument("key", help="Project Key")]):
    project = handler.get_project(key)
    if project:
        handler.set_project(key)
        print(f"Project active: {handler.read_project_active()}")
    else:
        print("~ Project not found or does not exist.")

@app.command()
def rm():
    ...

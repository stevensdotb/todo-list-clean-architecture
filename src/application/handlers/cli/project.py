from typing import Annotated

import typer

from src.application.handlers.project import ProjectHandler

app = typer.Typer(name="Projects command handler", no_args_is_help=True)
handler = ProjectHandler()


@app.callback(invoke_without_command=True)
def main(
    all: Annotated[bool, typer.Option("--all", help="List all projects")] = False,
    key: Annotated[str, typer.Option("--key", "-k", help="Project Key")] = None
):
    if all:
        handler.list_projects()
        raise typer.Exit()

    if key:
        handler.list_project_todos(key)


@app.command()
def create(name: str, key: Annotated[str, typer.Argument("key", help="Project key identifier")]):
    
    if name and not key:
        raise typer.BadParameter("Missing project [key] identifier. Use -k option to provide it")
    else:
        handler.create_project(name, key)


@app.command()
def dir():
    ...

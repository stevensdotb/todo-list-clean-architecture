from typing import Annotated

import typer

from src.application.use_cases.project import ProjectUseCase
from src.domain.repository.project import ProjectRepository
from src.domain.entities.project import ProjectEntity

app = typer.Typer(name="Projects command handler", no_args_is_help=True)


@app.command()
def create(name: str, key: Annotated[str, typer.Argument("key", help="Project key identifier")]):
    print(f"Create a project: {name.title()} -> {key}")
    entity = ProjectEntity(name, key)
    handler = ProjectUseCase(ProjectRepository)
    handler.create(entity)
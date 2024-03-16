from typing import Annotated

import typer


project = typer.Typer(name="Project command handler", no_args_is_help=True)
@project.command()
def create(name: str, key: Annotated[str, typer.Argument("-k" "--key", help="Project key identifier")]):
    print(f"Create a project: {name.title()} -> {key}")

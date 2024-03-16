from typing import Annotated

import typer


app = typer.Typer(name="Projects command handler", no_args_is_help=True)

@app.command()
def create(name: str, key: Annotated[str, typer.Argument("key", help="Project key identifier")]):
    print(f"Create a project: {name.title()} -> {key}")

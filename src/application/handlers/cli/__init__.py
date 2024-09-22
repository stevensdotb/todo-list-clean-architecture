import typer

from src.infrastructure.db import Db
import src.application.handlers.cli.projects as projects


app = typer.Typer(name="TODO CLI Application", no_args_is_help=True)
app.add_typer(projects.app, name="projects")


@app.command(help="Initialize instances for projects. Execute once.")
def init():
    Db().init_tables()





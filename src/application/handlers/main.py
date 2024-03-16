import typer

from src.infrastructure.db import Db
import src.application.handlers.project as project


app = typer.Typer(name="TODO CLI Application", no_args_is_help=True)
app.add_typer(project.app, name="project")


@app.command(help="Initialize instances for projects. Execute once.")
def init():
    Db().init_tables()





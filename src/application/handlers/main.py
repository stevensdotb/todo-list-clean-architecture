import typer

from src.infrastructure.db import Db
import src.application.handlers.project as project


app = typer.Typer(name="TODO CLI Application", no_args_is_help=True)
app.add_typer(project.project)


@app.command()
def init():
    Db().init_tables()





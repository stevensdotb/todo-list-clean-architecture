import typer


if __name__ == "__main__":
    from src.application.handlers.main import app
    
    typer.run(app)
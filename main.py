import typer

app = typer.Typer(help="Experiment Engineer CLI")

@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")

if __name__ == "__main__":
    app()

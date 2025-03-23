import typer

app = typer.Typer()

tasks = []


@app.command()
def add_task(task: str):
    tasks.append(task)
    typer.echo("Task added.")


@app.command()
def list_tasks():
    print("Tasks:")
    for task in tasks:
        typer.echo(f" - {task}")


@app.command()
def done_task(task: str):
    try:
        tasks.remove(task)
        typer.echo(f"Task {task} done.")
    except ValueError:
        typer.echo(f"Task {task} not found.")


if __name__ == '__main__':
    app()

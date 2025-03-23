import typer

from json_persistance import JsonPersistence

app = typer.Typer()

json_persistence = JsonPersistence('tasks.json')


@app.command()
def add_task(task: str):
    json_persistence.append(task)
    typer.echo("Task added.")


@app.command()
def list_tasks():
    print("Tasks:")
    tasks = json_persistence.load()
    for i, task in enumerate(tasks, 1):
        typer.echo(f"{i}. {task}")


@app.command()
def done_task(task: str):
    try:
        tasks = json_persistence.load()
        tasks.remove(task)
        typer.echo(f"Task {task} done.")
    except ValueError:
        typer.echo(f"Task {task} not found.")


@app.command()
def new_tasks(task: str):
    json_persistence.save(task)
    typer.echo("Tasks cleared.")


if __name__ == '__main__':
    app()

import typer
from typer import Option

from json_persistance import JsonPersistence
from task import Task

app = typer.Typer()

json_persistence = JsonPersistence('tasks.json')


@app.command()
def add_task(description: str):
    task = Task(description=description)
    json_persistence.append(task)
    typer.echo("Task added.")


@app.command()
def list_tasks():
    tasks = json_persistence.load()
    if not tasks:
        typer.echo("No tasks.")
        return
    for i, task in enumerate(tasks, 1):
        typer.echo(f"{i}. {task}")


@app.command()
def done_task(index: int):
    tasks = json_persistence.load()
    if 0 < index <= len(tasks):
        tasks[index - 1].done = True
        json_persistence.save(tasks)
        typer.echo(f"Task {index} marked as done.")
    else:
        typer.echo("Invalid index.")


@app.command()
def new_tasks(descriptions: list[str] = Option([],
                                               "--task", "-t",
                                               help="List of tasks to add.")):
    tasks = [Task(description=desc) for desc in descriptions]
    json_persistence.save(tasks)
    typer.echo(f"Saved {len(tasks)} new task(s).")


if __name__ == '__main__':
    app()

import typer

from json_persistance import JsonPersistence

app = typer.Typer()

tasks = []


@app.command()
def add_task(task: str):
    tasks.append(task)
    json_persistence = JsonPersistence('tasks.json')
    json_persistence.save(tasks)
    typer.echo("Task added.")


@app.command()
def list_tasks():
    print("Tasks:")
    json_persistence = JsonPersistence('tasks.json')
    json = json_persistence.load()

    for task in json:
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

# https://github.com/Ariaa527/Hacktoberfest-2025-Beginner-Python-Projects/

import storage
import typer
import sys
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="""
📝 ToDo CLI App

A simple command-line ToDo manager built with Python, Typer, and Rich.\n\n
You can:\n
 • Add new tasks\n
 • Mark tasks as done\n
 • Edit, delete, or filter tasks\n
 • View all your tasks in a colorful table\n\n

Example usage:\n
 - python main.py add "Buy groceries" --priority high\n
 - python main.py done 2\n
 - python main.py show --status done\n
""", no_args_is_help=True, epilog="""
Examples:\n
 - python main.py add "Learn Python" --priority high\n
 - python main.py show --status done\n
 - python main.py delete 3
""")

console = Console()

@app.command(help="Add a new task with an optional priority level (default: medium).")
def add(title: str = typer.Argument(..., help="The title or description of your task."), priority: str = typer.Option("medium", help="Task priority: low, medium, or high.")):
    if (not title or not title.strip()) :
        print("task title cannot be empty!")
        sys.exit(1)

    res = storage.store(title=title, priority=priority)
    if res :
        print("task added successfully")
        sys.exit(0)

@app.command(help="Mark a task as done by its ID.")
def done(id: int = typer.Argument(..., help="The ID of the task you want to mark as done.")):
    if not id or id <= 0 :
        print("task id cannot be empty or less than or equal to 0")
        sys.exit(1)
    
    res = storage.done(id)
    if res :
        table = Table(title="Tasks")
        table.add_column("ID", justify="center")
        table.add_column("Title", justify="left", no_wrap=True)
        table.add_column("Priority", justify="center")
        table.add_column("Status", justify="center")
        status = "Done" if res["done"] else "Not Done"
        table.add_row(str(res["id"]), res["title"], f"{"[red]" if res["priority"] == "high" else "[yellow]" if res["priority"] == "medium" else "[blue]"}{res["priority"]}{"[/red]" if res["priority"] == "high" else "[/yellow]" if res["priority"] == "medium" else "[/blue]"}" , f"{'[bold][green]' if status == "Done" else '[white]'}{status}{'[/bold][/green]' if status == "Done" else '[/white]'}")
        print("task status changed successfully")
        sys.exit(0)
    else :
        print("No Task Found")
        sys.exit(1)

@app.command(help="Delete a task by its ID.")
def delete(id: int = typer.Argument(..., help="The ID of the task you want to delete.")):
    if not id or id <= 0 :
        print("task id cannot be empty or less than or equal to 0")
        sys.exit(1)
    
    res = storage.delete(id)
    if res :
        table = Table(title="Tasks")
        table.add_column("ID", justify="center")
        table.add_column("Title", justify="left", no_wrap=True)
        table.add_column("Priority", justify="center")
        table.add_column("Status", justify="center")
        status = "Done" if res["done"] else "Not Done"
        table.add_row(str(res["id"]), res["title"], f"{"[red]" if res["priority"] == "high" else "[yellow]" if res["priority"] == "medium" else "[blue]"}{res["priority"]}{"[/red]" if res["priority"] == "high" else "[/yellow]" if res["priority"] == "medium" else "[/blue]"}" , f"{'[bold][green]' if status == "Done" else '[white]'}{status}{'[/bold][/green]' if status == "Done" else '[/white]'}")
        print("task deleted successfully")
        sys.exit(0)
    else :
        print("No Task Found")
        sys.exit(1)

@app.command(help="Show your tasks with optional filters for status, id, or priority.")
def show(status: str = typer.Option("all", help="Filter by task status: all, done, or not done."), id: int = typer.Option(0, help="Filter by specific task ID."), priority: str = typer.Option("all", help="Filter by priority: low, medium, high, or all.")):
    table = Table(title="Tasks")
    table.add_column("ID", justify="center")
    table.add_column("Title", justify="left", no_wrap=True)
    table.add_column("Priority", justify="center")
    table.add_column("Status", justify="center")
    tasks = storage.get_tasks()
    tasks = tasks if status.lower() == "all" else [task for task in tasks if task["done"]] if status.lower() == "done" else [task for task in tasks if not task["done"]] if status.lower() == "not done" else []
    tasks = tasks if id == 0 else [task for task in tasks if task["id"] == id]
    tasks = tasks if priority == "all" else [task for task in tasks if task["priority"] == priority.lower()]
    # if filter == "all" :
    if tasks :
        for task in tasks :
            task_status = "Done" if task["done"] else "Not Done"
            table.add_row(str(task["id"]), task["title"], f"{"[red]" if task["priority"] == "high" else "[yellow]" if task["priority"] == "medium" else "[blue]"}{task["priority"]}{"[/red]" if task["priority"] == "high" else "[/yellow]" if task["priority"] == "medium" else "[/blue]"}" , f"{'[bold][green]' if task_status == "Done" else '[white]'}{task_status}{'[/bold][/green]' if task_status == "Done" else '[/white]'}")
        
        console.print(table)
    else :
        print("No Tasks Found")


@app.command(help="Edit an existing task’s title or priority.")
def edit(id: int = typer.Argument(..., help="The ID of the task you want to edit."), title: str = typer.Option(None, help="New title for the task."), priority: str = typer.Option(None, help="New priority: low, medium, or high.")):
    if not title and not priority :
        console.print("[red][bold]Title or Priority is required[/bold][/red]")
        sys.exit(1)
    res = storage.modify(id=id, title=title, priority=priority)
    if res :
        table = Table(title="Tasks")
        table.add_column("ID", justify="center")
        table.add_column("Title", justify="left", no_wrap=True)
        table.add_column("Priority", justify="center")
        table.add_column("Status", justify="center")
        status = "Done" if res["done"] else "Not Done"
        table.add_row(str(res["id"]), res["title"], f"{"[red]" if res["priority"] == "high" else "[yellow]" if res["priority"] == "medium" else "[blue]"}{res["priority"]}{"[/red]" if res["priority"] == "high" else "[/yellow]" if res["priority"] == "medium" else "[/blue]"}" , f"{'[bold][green]' if status == "Done" else '[white]'}{status}{'[/bold][/green]' if status == "Done" else '[/white]'}")
        console.print("[green][bold]Task Edited Successfully![/bold][/green]")
        sys.exit(0)
    else :
        console.print("[red][bold]Task Not Found![/bold][/red]")
        sys.exit(1)

if __name__ == "__main__" :
    app()




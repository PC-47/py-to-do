#!/bin/python3

import json
import click

tasks_file = "/root/py-to-do/tasks.json"

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        list()

@click.command()
def list():
    '''Default function, prints list of all tasks'''
    tasks: list = import_tasks(tasks_file)
    # get max task width
    max_task_width: int = 0
    for task in tasks:
        task_width: int = len(task['task'])
        if task_width > max_task_width:
            max_task_width = task_width
    

    print("-" * (30 + max_task_width))
    print("| Index | Completion | Task  " + (" " * max_task_width) + "|")
    print("-" * (30 + max_task_width))
    for index,task in enumerate(tasks):
        output: str = f"|  {index:03}  |"
        if not task['complete']:
            output += "            |"
        else:
            output += "    done    |"
        output += f" {task['task']:{max_task_width + 5}} |"
        click.echo(output)
    print("-" * (30 + max_task_width))

@click.command()
@click.argument('task_name', type=str)
def add(task_name: str):
    '''Add a task with a task name'''
    tasks: list = import_tasks(tasks_file)
    tasks.append({"task": task_name, "complete": False})
    export_tasks(tasks_file, tasks)    

@click.command()
@click.argument('index', type=int)
def complete(index: int):
    '''Set the status of a task at an index to complete'''
    tasks = import_tasks(tasks_file)
    tasks[index]['complete'] = True
    export_tasks(tasks_file, tasks)

@click.command()
@click.argument('index', type=int)
def uncomplete(index: int):
    '''Set the status of a task at an index to incomplete'''
    tasks = import_tasks(tasks_file)
    tasks[index]['complete'] = False
    export_tasks(tasks_file, tasks)

@click.command()
@click.argument('indexes', nargs=-1, type=int)
def remove(indexes: int):
    '''Remove the tasks at given indexes'''
    for index in indexes:
        tasks = import_tasks(tasks_file)
        tasks.pop(index)
        export_tasks(tasks_file, tasks)

@click.command()
def clear():
    tasks = []
    export_tasks(tasks_file, tasks)

@click.command()
@click.argument('index', type=int)
@click.argument('task_name', type=str)
def insert(index, task_name):
    '''Insert new task at specified index'''
    tasks = import_tasks(tasks_file)
    tasks.insert(index, {'task': task_name, 'complete': False})
    export_tasks(tasks_file, tasks)


cli.add_command(list)
cli.add_command(add)
cli.add_command(add, name='a')
cli.add_command(complete)
cli.add_command(complete, name='c')
cli.add_command(uncomplete)
cli.add_command(uncomplete, name='uc')
cli.add_command(remove)
cli.add_command(remove, name='r')
cli.add_command(clear)
cli.add_command(insert)
cli.add_command(insert, name='i')

def export_tasks(filename: str, tasks: list) -> None:
    try:
        with open(filename, 'w') as f:
            f.write(json.dumps(tasks, indent=4))
    except Exception as e:
        print(e)

def import_tasks(filename: str) -> list:
    try:
        with open(filename, 'r') as f:
            tasks = json.load(f)
        return tasks
    except FileNotFoundError:
        print(f"ERROR: File {filename} not found.")
    except json.JSONDecodeError:
        print(f"ERROR: unable to parse json in file {filename}.")
    return None

if __name__ == '__main__':
    cli()

# py-to-do
Simple Python TODO CLI Program

## Basic Usage

- `tasks` get a basic list of stored tasks
- `tasks add "thing to do"` appends a task to the end of the list
- `tasks remove 4` removes the task at index 4
- `tasks remove 2 3 4` removes multiple tasks, might have issues with index out of bounds
- `tasks complete 5` sets the task at index 5 to complete
- `tasks uncomplete 5` sets the task at index 5 to incomplete
- `tasks insert 3 "thing to do"` inserts a new task at the given index
- `tasks clear` clears the whole table

## Shortcuts

- `insert` -> `i`
- `add` -> `a`
- `remove` -> `r`
- `complete` -> `c`
- `uncomplete` -> `uc`

## Features to add

- create empty tasks.json if it does not exist
- ability to backup to local tasks.json.bak
- adding a column for tracking category / tag of each task

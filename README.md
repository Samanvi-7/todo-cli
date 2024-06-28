# To_Do Application (Command-line application)

<p style="font-size: 15px;">This is a simple command-line todo application written in Python. It uses SQLite3 for data storage.</p>

## Properties

- Help menu for available commands
- Add tasks
- Remove tasks
- View all tasks
- Exit option to quit the application


## Installation

**SQLite3** comes included with Python by default, so there's no separate installation required when using Python itself.Simply ensure you have Python installed on your system.

**Set up the SQLite database:**

The application uses **todos.db** as the database file, which will be automatically created if it doesn't exist.

**Clone the repository:**
   ```bash
   git clone <https://github.com/Samanvi-7/todo-cli.git>
   cd <todo-cli> 
```

## Usage

<p style="font-size: 15px;">To use the todo application, follow these commands:<p>

- **To see the available commands:**

```
help
```
- **To add a task:**

```
add <Your Task>
```

- **To remove a task:**

```
remove <Your Task_name>
```

- **To view all tasks:**

```
view
```

- **To exit the application:**

```
exit
```

## Excluded Files

The following files are excluded from version control using `.gitignore`:

- `*.db`: SQLite database files
- `__pycache__`: Python bytecode cache
- `.vscode`: Visual Studio Code configuration files 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License 




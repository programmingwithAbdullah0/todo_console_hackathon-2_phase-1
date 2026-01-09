# Quickstart: Console Todo App (Phase I)

## Prerequisites
- Python 3.13+
- [UV](https://github.com/astral-sh/uv) package manager

## Installation
```bash
# Clone the repo and enter the directory
cd hackathon2

# Initialize the project environment
uv sync
```

## Running the Application
```bash
# Run the application
uv run src/main.py
```

## Core Commands
1. **Add Task**: Enter title and optional description.
2. **Delete Task**: Provide ID and confirm "yes".
3. **Update Task**: Modify title or description of an existing ID.
4. **View All Tasks**: Displays list with [✓] for completed.
5. **Mark Complete**: Toggle status by ID.
6. **Exit**: Gracefully close the application.

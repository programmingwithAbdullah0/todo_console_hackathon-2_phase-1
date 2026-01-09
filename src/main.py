"""
Module: Console Todo App
Purpose: Main entry point and logic for the Todo application.
Phase: User Story 2 (Task Maintenance)
Tasks: T011, T012, T013
"""

import sys
from datetime import datetime
from typing import List, Dict, Optional

# Global state for in-memory storage (T005)
tasks: List[Dict] = []
next_id: int = 1

def validate_input(prompt: str, min_length: int = 1) -> str:
    """Helper to validate string input (T006)."""
    while True:
        value = input(prompt).strip()
        if len(value) >= min_length:
            return value
        print(f"Error: Input must be at least {min_length} characters.")

def add_task():
    """Create a new task (T007)."""
    global next_id
    print("\n--- Add New Task ---")
    title = validate_input("Title: ")
    description = input("Description (optional): ").strip()

    timestamp = datetime.now().isoformat()
    task = {
        "id": next_id,
        "title": title,
        "description": description,
        "completed": False,
        "created_at": timestamp,
        "updated_at": timestamp
    }
    tasks.append(task)
    print(f"Success: Task #{next_id} added.")
    next_id += 1

def view_tasks():
    """Display all tasks (T008)."""
    print("\n--- Task List ---")
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status_icon = "[✓]" if task["completed"] else "[ ]"
        print(f"{task['id']}. {status_icon} {task['title']}")
        if task["description"]:
            print(f"   {task['description']}")

def mark_complete_toggle():
    """Toggle completion status of a task by ID (T009)."""
    view_tasks()
    if not tasks:
        return

    try:
        task_id_str = input("\nEnter Task ID to toggle completion: ").strip()
        if not task_id_str: return
        task_id = int(task_id_str)

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                task["updated_at"] = datetime.now().isoformat()
                status = "completed" if task["completed"] else "pending"
                print(f"Success: Task #{task_id} is now {status}.")
                return
        print(f"Error: Task #{task_id} not found.")
    except ValueError:
        print("Error: Invalid ID. Please enter a number.")

def update_task():
    """Update an existing task (T011)."""
    view_tasks()
    if not tasks:
        return

    try:
        task_id_str = input("\nEnter Task ID to update: ").strip()
        if not task_id_str: return
        task_id = int(task_id_str)

        for task in tasks:
            if task["id"] == task_id:
                print(f"Current Title: {task['title']}")
                new_title = input("New Title (leave empty to keep current): ").strip()

                print(f"Current Description: {task['description']}")
                new_description = input("New Description (leave empty to keep current): ").strip()

                if new_title:
                    task["title"] = new_title
                if new_description:
                    task["description"] = new_description

                if new_title or new_description:
                    task["updated_at"] = datetime.now().isoformat()
                    print(f"Success: Task #{task_id} updated.")
                else:
                    print("No changes made.")
                return
        print(f"Error: Task #{task_id} not found.")
    except ValueError:
        print("Error: Invalid ID. Please enter a number.")

def delete_task():
    """Remove a task with confirmation (T012)."""
    view_tasks()
    if not tasks:
        return

    try:
        task_id_str = input("\nEnter Task ID to delete: ").strip()
        if not task_id_str: return
        task_id = int(task_id_str)

        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                confirm = input(f"Are you sure you want to delete Task #{task_id}? (y/n): ").strip().lower()
                if confirm == 'y':
                    tasks.pop(i)
                    print(f"Success: Task #{task_id} deleted.")
                else:
                    print("Deletion cancelled.")
                return
        print(f"Error: Task #{task_id} not found.")
    except ValueError:
        print("Error: Invalid ID. Please enter a number.")

def display_menu():
    """Main menu display (T004)."""
    print("\n--- Console Todo App ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Toggle Task Completion")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def main():
    """Basic CLI loop (T013)."""
    while True:
        display_menu()
        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_complete_toggle()
        elif choice == "4":
            update_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("\nError: Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()

"""
StudyTrack — Student Task & Assignment Manager
CS50P Final Project

A command-line application that helps students track assignments,
deadlines, priorities, and completion progress. Tasks are persisted
locally in a JSON file.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Location of the JSON "database" file, relative to this script.
DATA_FILE = Path(__file__).parent / "data" / "tasks.json"

VALID_PRIORITIES = ("low", "medium", "high")


def main():
    tasks = load_tasks()

    menu = """
=== StudyTrack ===
1. Add task
2. Remove task
3. Complete task
4. Search tasks
5. Show progress
6. List all tasks
7. Quit
"""

    while True: 
        print(menu)
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            course = input("Course: ").strip()
            due_date = input("Due date (YYYY-MM-DD): ").strip()
            priority = input("Priority (low/medium/high) [medium]: ").strip() or "medium"
            try:
                tasks = add_task(tasks, title, course, due_date, priority)
                save_tasks(tasks)
                print("Task added.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                task_id = int(input("Task ID to remove: ").strip())
                tasks = remove_task(tasks, task_id)
                save_tasks(tasks)
                print("Task removed.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            try:
                task_id = int(input("Task ID to mark complete: ").strip())
                tasks = complete_task(tasks, task_id)
                save_tasks(tasks)
                print("Task marked complete.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            keyword = input("Search keyword: ").strip()
            results = search_tasks(tasks, keyword)
            if results:
                for t in results:
                    _print_task(t)
            else:
                print("No matching tasks found.")

        elif choice == "5":
            progress = calculate_progress(tasks)
            print(
                f"Completed {progress['completed']}/{progress['total']} "
                f"tasks ({progress['percentage']}%)"
            )

        elif choice == "6":
            if tasks:
                for t in tasks:
                    _print_task(t)
            else:
                print("No tasks yet.")

        elif choice == "7":
            print("Goodbye!")
            sys.exit(0)

        else:
            print("Invalid option, please choose 1-7.")


def add_task(tasks, title, course, due_date, priority="medium"):
    """
    Add a new task to the list of tasks and return the updated list.

    Raises ValueError if the title is empty, the priority is invalid,
    or the due date is not in YYYY-MM-DD format.
    """
    title = title.strip()
    if not title:
        raise ValueError("Title cannot be empty")

    priority = priority.strip().lower()
    if priority not in VALID_PRIORITIES:
        raise ValueError(f"Priority must be one of {VALID_PRIORITIES}")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format")

    next_id = max((t["id"] for t in tasks), default=0) + 1

    new_task = {
        "id": next_id,
        "title": title,
        "course": course.strip(),
        "due_date": due_date,
        "priority": priority,
        "completed": False,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }

    return tasks + [new_task]


def remove_task(tasks, task_id):
    """
    Remove the task with the given id and return the updated list.

    Raises ValueError if no task with that id exists.
    """
    updated = [t for t in tasks if t["id"] != task_id]
    if len(updated) == len(tasks):
        raise ValueError(f"No task found with id {task_id}")
    return updated


def complete_task(tasks, task_id):
    """
    Mark the task with the given id as completed and return the
    updated list.

    Raises ValueError if no task with that id exists.
    """
    found = False
    updated = []
    for t in tasks:
        if t["id"] == task_id:
            t = {**t, "completed": True}
            found = True
        updated.append(t)

    if not found:
        raise ValueError(f"No task found with id {task_id}")

    return updated


def search_tasks(tasks, keyword):
    """
    Return a list of tasks whose title or course contains keyword
    (case-insensitive). Returns an empty list if keyword is blank
    or nothing matches.
    """
    keyword = keyword.strip().lower()
    if not keyword:
        return []

    return [
        t for t in tasks
        if keyword in t["title"].lower() or keyword in t["course"].lower()
    ]


def calculate_progress(tasks):
    """
    Return a dict summarizing completion progress:
    {"total": int, "completed": int, "percentage": float}
    """
    total = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    percentage = round((completed / total) * 100, 1) if total else 0.0

    return {"total": total, "completed": completed, "percentage": percentage}


def load_tasks(path=DATA_FILE):
    """Load tasks from a JSON file. Returns an empty list if missing/empty."""
    path = Path(path)
    if not path.exists():
        return []
    try:
        with open(path, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks, path=DATA_FILE):
    """Save the list of tasks to a JSON file, creating parent dirs as needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(tasks, f, indent=2)


def _print_task(t):
    status = "✔" if t["completed"] else " "
    print(
        f"[{status}] #{t['id']} {t['title']} ({t['course']}) "
        f"due {t['due_date']} - {t['priority']} priority"
    )


if __name__ == "__main__":
    main()

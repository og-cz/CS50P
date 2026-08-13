import pytest
from project import (
    add_task,
    remove_task,
    complete_task,
    search_tasks,
    calculate_progress,
)


def make_sample_tasks():
    """Helper: build a small, known list of tasks for tests to reuse."""
    tasks = []
    tasks = add_task(tasks, "Essay draft", "English", "2026-09-01", "high")
    tasks = add_task(tasks, "Problem set 3", "CS50", "2026-09-05", "medium")
    tasks = add_task(tasks, "Lab report", "Biology", "2026-09-10", "low")
    return tasks


def test_add_task():
    tasks = []
    tasks = add_task(tasks, "Read chapter 4", "History", "2026-10-01", "medium")

    assert len(tasks) == 1
    assert tasks[0]["title"] == "Read chapter 4"
    assert tasks[0]["course"] == "History"
    assert tasks[0]["due_date"] == "2026-10-01"
    assert tasks[0]["priority"] == "medium"
    assert tasks[0]["completed"] is False
    assert tasks[0]["id"] == 1

    # IDs should increment
    tasks = add_task(tasks, "Second task", "Math", "2026-10-02", "low")
    assert tasks[1]["id"] == 2

    # Invalid input should raise ValueError
    with pytest.raises(ValueError):
        add_task(tasks, "", "Math", "2026-10-02", "low")

    with pytest.raises(ValueError):
        add_task(tasks, "Bad priority", "Math", "2026-10-02", "urgent")

    with pytest.raises(ValueError):
        add_task(tasks, "Bad date", "Math", "10/02/2026", "low")


def test_remove_task():
    tasks = make_sample_tasks()
    assert len(tasks) == 3

    updated = remove_task(tasks, 2)
    assert len(updated) == 2
    assert all(t["id"] != 2 for t in updated)

    with pytest.raises(ValueError):
        remove_task(updated, 999)


def test_complete_task():
    tasks = make_sample_tasks()

    updated = complete_task(tasks, 1)
    completed_task = next(t for t in updated if t["id"] == 1)
    assert completed_task["completed"] is True

    # Other tasks should be untouched
    other_task = next(t for t in updated if t["id"] == 2)
    assert other_task["completed"] is False

    with pytest.raises(ValueError):
        complete_task(tasks, 999)


def test_search_tasks():
    tasks = make_sample_tasks()

    results = search_tasks(tasks, "essay")
    assert len(results) == 1
    assert results[0]["title"] == "Essay draft"

    results = search_tasks(tasks, "CS50")
    assert len(results) == 1
    assert results[0]["course"] == "CS50"

    results = search_tasks(tasks, "nonexistent")
    assert results == []

    results = search_tasks(tasks, "")
    assert results == []


def test_calculate_progress():
    tasks = make_sample_tasks()

    progress = calculate_progress(tasks)
    assert progress == {"total": 3, "completed": 0, "percentage": 0.0}

    tasks = complete_task(tasks, 1)
    tasks = complete_task(tasks, 2)
    progress = calculate_progress(tasks)
    assert progress["total"] == 3
    assert progress["completed"] == 2
    assert progress["percentage"] == pytest.approx(66.7)

    progress_empty = calculate_progress([])
    assert progress_empty == {"total": 0, "completed": 0, "percentage": 0.0}

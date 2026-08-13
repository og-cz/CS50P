# StudyTrack — Student Task & Assignment Manager
#### Video Demo: <URL HERE>
#### Description:

StudyTrack is a command-line application, built for my CS50P final project, that helps students keep track of assignments, deadlines, priorities, and overall completion progress. I built it because I was tired of scattering deadlines across sticky notes, group chats, and half-remembered mental lists — I wanted one small, dependable tool that lives in the terminal, stores everything in a plain JSON file, and doesn't require an internet connection, an account, or any third-party service to work.

## What it does

When you run `python project.py`, you're dropped into a simple numbered menu where you can:

1. **Add a task** — enter a title, course name, due date (`YYYY-MM-DD`), and priority (`low`, `medium`, or `high`). StudyTrack validates the input and refuses to save a task with a blank title, an unrecognized priority, or a malformed date, so the underlying data file never ends up in a broken state.
2. **Remove a task** — delete a task permanently by its ID number.
3. **Complete a task** — mark a task as done without deleting it, so you keep a record of what you've finished.
4. **Search tasks** — look up tasks by keyword, matched case-insensitively against both the title and the course name. Handy for "what do I still owe Biology?"
5. **Show progress** — see how many of your tasks are completed, out of the total, as both a raw count and a percentage.
6. **List all tasks** — print every task currently stored, with a checkmark next to anything already completed.
7. **Quit** — exit the program.

Every change (adding, removing, completing a task) is immediately written back to `data/tasks.json`, so your task list persists between runs.

## Project files

- **`project.py`** — Contains `main()` plus five additional functions: `add_task()`, `remove_task()`, `complete_task()`, `search_tasks()`, and `calculate_progress()`. It also includes two small helper functions, `load_tasks()` and `save_tasks()`, that handle reading from and writing to the JSON file, and a private `_print_task()` helper used purely for formatting console output.
- **`test_project.py`** — Contains `test_add_task()`, `test_remove_task()`, `test_complete_task()`, `test_search_tasks()`, and `test_calculate_progress()`, one test function per required custom function, runnable with `pytest test_project.py`.
- **`data/tasks.json`** — The JSON file where tasks are persisted. It starts out as an empty list (`[]`) and grows as tasks are added.
- **`requirements.txt`** — Lists `pytest` as the only dependency, needed solely to run the test suite; the application itself uses nothing beyond Python's standard library.

## Design decisions

The biggest decision I made early on was to keep `add_task()`, `remove_task()`, `complete_task()`, `search_tasks()`, and `calculate_progress()` as **pure functions**: each one takes a list of task dictionaries as input and returns a new (or modified) list, without touching the filesystem directly. All the file I/O is isolated in `load_tasks()` and `save_tasks()`, which `main()` calls before and after these pure functions do their work.

I made this choice specifically for testability. If `add_task()` read and wrote `data/tasks.json` internally, every test would need to juggle temporary files, clean up after itself, and worry about tests interfering with each other. By separating logic from I/O, `test_project.py` can build lists of tasks entirely in memory and assert on the results directly — the tests are fast, deterministic, and don't touch disk at all. This is a pattern I plan to keep using in future projects.

I also debated whether to auto-assign task IDs versus asking the user to choose one. I went with auto-assignment (`max` existing ID + 1) because it removes a whole category of user error — duplicate or nonsensical IDs — and keeps the interface simpler.

For validation, I decided that `add_task()` should raise `ValueError` rather than silently ignoring bad input or printing an error itself. This keeps the function honest about what "success" means, and lets `main()` decide how to react to failures (in this case, catching the exception and printing a friendly message), which also made it trivial to test the validation logic with `pytest.raises(ValueError)`.

Finally, I chose JSON over something like SQLite because the project didn't need relational queries — a simple list of dictionaries maps naturally onto JSON, it's human-readable if you ever want to peek at `data/tasks.json` directly, and it kept the dependency list at zero for the app itself.

## Possible future improvements

Given more time, I'd like to add due-date sorting, overdue-task highlighting, and an optional `--file` command-line flag so users could point StudyTrack at a different JSON file for different semesters or classes.

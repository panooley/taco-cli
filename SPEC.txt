==============================
=      TASK TRACKER CLI      =
==============================

=== OVERVIEW ===
* Command-line application for task management
* Designed for efficient task tracking and organization
* Supports task addition, updating, listing, and deletion
* Lightweight and accessible across Windows, macOS, and Linux
* Data stored in JSON for persistence

=== COMMANDS ===
0: ADD   "description" --due YYYY-MM-DD --priority [low|medium|high] 
         -> Adds a new task with specified description, due date, and priority
1: LIST  [--status pending|completed] [--priority low|medium|high] 
         -> Lists all tasks with optional filters for status and priority
2: UPDATE <task_id> [--status completed|pending] [--due YYYY-MM-DD] 
         -> Updates the specified task's status, due date, or priority
3: DELETE <task_id> 
         -> Deletes the specified task from the task list
4: SEARCH "<keyword>" 
         -> Searches for tasks containing the specified keyword
5: STATS --period [today|last_week|last_month] 
         -> Provides statistics on completed tasks within the given period
6: TIMER --duration <minutes> 
         -> Starts a Pomodoro timer for the specified duration (default: 25 min)
7: EXPORT --format [json|csv] --file <filename> 
         -> Exports tasks to the specified file format
8: IMPORT --file <filename> 
         -> Imports tasks from the specified file

=== DATA STRUCTURE ===
* Task structure:
    - ID: Unique identifier for each task
    - Description: Text description of the task
    - Due Date: Date when the task is due
    - Priority: Task priority (low, medium, high)
    - Status: Task status (pending, completed)
    
* Data storage format:
    - JSON format for tasks, allowing for easy export/import

=== ERROR HANDLING ===
* Each command will provide clear error messages for:
    - Invalid input or syntax
    - Task not found (for update/delete)
    - File read/write errors during export/import

=== USAGE EXAMPLES ===
* Add a task: 
    > taco add "Finish report" --due 2024-10-15 --priority high
* List tasks: 
    > taco list --status pending
* Update a task: 
    > taco update 1 --status completed
* Delete a task: 
    > taco delete 2
* Get statistics: 
    > taco stats --period last_week
* Start a Pomodoro timer: 
    > taco timer --duration 25
* Export tasks: 
    > taco export --format json --file tasks.json

=== FUTURE ENHANCEMENTS ===
* Notifications for task deadlines
* Tagging system for better task categorization
* Collaborative features for team task management
* Graphical dashboard for enhanced visual feedback

=== TECHNICAL SPECIFICATIONS ===
* Programming Language: Python
* Dependencies:
    - Python: argparse, json, sqlite3
* Data Storage: JSON file
* Compatibility: Windows, macOS, Linux

=== HELP COMMAND ===
* The command `taco help` will provide detailed information on all available commands and usage instructions.

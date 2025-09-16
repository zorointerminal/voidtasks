# VoidTasks 📂

*Organize. Conquer. Escape the Void.*

A minimalist command-line interface (CLI) task manager for Linux users who prefer working from the terminal. VoidTasks helps you manage your tasks efficiently with a clean, colorful interface and persistent JSON storage.

## Features

-  **Add Tasks** - Create new tasks with optional deadlines
-  **Remove Tasks** - Delete unwanted tasks from your active list
-  **View Tasks** - Display all your active tasks at a glance
-  **Complete Tasks** - Mark tasks as completed with timestamps
-  **Persistent Storage** - All tasks are saved in JSON format
-  **Colorful CLI** - Enhanced terminal experience with colors
-  **Interactive Menus** - User-friendly navigation with confirmation prompts

## Requirements

- **Operating System**: Linux
- **Python**: 3.6 or higher
- **Dependencies**: 
  - `prompt_toolkit` (for enhanced CLI input)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/zorointerminal/voidtasks.git
   cd voidtasks
   ```

2. **Install required dependencies**:
   ```bash
   pip3 install prompt_toolkit
   ```

3. **Make the script executable**:
   ```bash
   chmod +x task_manager.py
   ```

4. **Set up global `void` command** (recommended):
   
   **Option A: Using symbolic link**
   ```bash
   sudo ln -s /full/path/to/your/voidtasks/task_manager.py /usr/local/bin/void
   ```
   
   **Option B: Using alias (add to your ~/.bashrc or ~/.zshrc)**
   ```bash
   echo 'alias void="/full/path/to/your/voidtasks/task_manager.py"' >> ~/.bashrc
   source ~/.bashrc
   ```
   
   Replace `/full/path/to/your/voidtasks/` with the actual path where you installed VoidTasks.

## Usage

### Starting VoidTasks

**If you set up the global command**:
```bash
void
```

**Alternative methods**:
```bash
python3 task_manager.py
```

Or if you made it executable:
```bash
./task_manager.py
```

### Main Menu Options

Once started, you'll see the main menu with these options:

1. **Add Task** - Create a new task with optional deadline
2. **Remove Task** - Delete one or more active tasks
3. **View Tasks** - Display all your current active tasks
4. **Complete Task** - Mark tasks as completed
5. **Exit** - Close the application

### Adding Tasks

- Enter a descriptive title for your task
- Optionally add a deadline in `YYYY-MM-DD HH:MM` format
- Confirm your entries before saving
- Choose to add more tasks or return to main menu

### Managing Tasks

- **Remove**: Select multiple tasks by entering comma-separated numbers (e.g., "1,3,5")
- **Complete**: Mark tasks as done - they'll be moved to completed list with timestamp
- **View**: See all active tasks with their deadlines

## File Structure

```
voidtasks/
├── task_manager.py    # Main application file
└── tasks/
    └── tasks.json     # Task storage (created automatically)
```

## Data Storage

Tasks are stored in `tasks/tasks.json` with the following structure:

```json
{
    "active": [
        {
            "title": "Task title",
            "deadline": "2024-12-31 23:59"
        }
    ],
    "completed": [
        {
            "title": "Completed task",
            "deadline": "2024-12-25 12:00",
            "completed_at": "2024-12-24 10:30:00"
        }
    ]
}
```

## Navigation

- Use `m` at any prompt to return to the main menu
- Follow the interactive prompts for confirmations
- Use comma-separated numbers when selecting multiple items

## Examples

### Adding a Task
```
Enter task title (or 'm' to return to main menu): learn loops

You entered: 'learn loops'. Confirm title? (y/n/m): y

Enter deadline (YYYY-MM-DD HH:MM) or leave blank (or 'm' to return to main menu): 2025-04-16 22:00

You entered deadline: '2025-04-16 22:00'. Confirm? (y/n/m): y

✔ Task 'learn loops' added successfully!
```

### Completing Tasks
```
These are your current tasks:

1. learn loops
2. go for jogging

Enter task numbers to complete (comma-separated) or 'm' to return: 2

You selected to complete:
- go for jogging

Are you sure? (y/n/m): y

✔ Completed tasks:
go for jogging
```

## Troubleshooting

**ImportError: No module named 'prompt_toolkit'**
- Install the required dependency: `pip3 install prompt_toolkit`

**Permission denied**
- Make sure you have execute permissions: `chmod +x task_manager.py`

**Tasks not saving**
- Ensure the `tasks/` directory exists in the same location as `task_manager.py`
- Check write permissions in the directory

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve VoidTasks!

## License

VoidTasks is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this tool.

## 💬 Feedback & Suggestions

Loved VoidTasks? Got ideas for improvements? Reach out here:

**X (formerly Twitter):** [@zorointerminal](https://x.com/zorointerminal)

---
<div align="center">
<strong>Escape the void of disorganization with VoidTasks!</strong>
</div>

<div align="center">
<strong>Made with ❤️ for the Linux community</strong>
</div>

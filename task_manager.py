#!/usr/bin/env python3

import json
from datetime import datetime
from prompt_toolkit import prompt
import os

TASKS_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "tasks", "tasks.json")

# Colors
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
MAGENTA = "\033[95m"

# Load tasks
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return {"active": [], "completed": []}
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

# Save tasks
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a task
def add_task():
    tasks = load_tasks()
    
    while True:  # outer loop for entire add_task flow
        
        # task title
        title = ""
        while True:
            title_input = input("\nEnter task title (or 'm' to return to main menu): ")
            if title_input.lower() == "m":
                print("\nReturning to main menu...\n")
                return
            if title_input.strip():
                title = title_input  # update title if user typed something
            else:
                if not title:
                    print("Task title cannot be empty.")
                    continue

            confirm_title = input(f"\nYou entered: '{title}'. Confirm title? (y/n/m): ")
            if confirm_title.lower() == "y":
                break
            elif confirm_title.lower() == "m":
                print("\nReturning to main menu...\n")
                return
            else:
                print("\nOkay, let's re-enter the task title.\n")

        # deadline
        deadline = ""
        while True:
            deadline_input = input("\nEnter deadline (YYYY-MM-DD HH:MM) or leave blank (or 'm' to return to main menu): ")
            if deadline_input.lower() == "m":
                print("\nReturning to main menu...\n")
                return
            if deadline_input.strip():
                deadline = deadline_input  # update deadline

            confirm_deadline = input(f"\nYou entered deadline: '{deadline if deadline else 'No deadline'}'. Confirm? (y/n/m): ")
            if confirm_deadline.lower() == "y":
                break
            elif confirm_deadline.lower() == "m":
                print("\nReturning to main menu...\n")
                return
            else:
                print("\nOkay, let's re-enter the deadline.\n")

        # Add task to tasks
        task = {"title": title, "deadline": deadline} if deadline else {"title": title}
        tasks["active"].append(task)
        save_tasks(tasks)
        print(f"\n✔ Task '{title}' added successfully!\n")
        
        # Submenu
        while True:
            choice = input("Do you want to:\na) Add another task\nm) Return to main menu\n \nChoice (a/m): ").lower()
            if choice == "a":
                break  # back to outer loop
            elif choice == "m":
                print("\nReturning to main menu...\n")
                return
            else:
                print("\nInvalid choice. Enter 'a' or 'm'.\n")


# Remove a task
def remove_task():
    tasks = load_tasks()
    
    while True:
        active_tasks = tasks["active"]
        if not active_tasks:
            print("\nNo active tasks to remove.\n")
            return

        print("\nThese are your current tasks:\n")
        for idx, task in enumerate(active_tasks, start=1):
            print(f"{idx}. {task['title']}")

        while True:  # Input loop for task numbers
            choices = input("\nEnter task numbers to remove (comma-separated) or 'm' to return: ")
            if choices.lower() == "m":
                print("\nReturning to main menu...\n")
                return

            try:
                indexes = sorted({int(c.strip()) - 1 for c in choices.split(",")}, reverse=True)
                if any(i < 0 or i >= len(active_tasks) for i in indexes):
                    raise ValueError
            except ValueError:
                print("\nInvalid input! Please separate task numbers with commas and use valid numbers.\n")
                continue  # go back to input prompt

            # Confirmation
            print("\nYou selected to remove:")
            for i in indexes:
                print(f"- {active_tasks[i]['title']}")

            confirm = input("\nAre you sure? (y/n/m): ").lower()
            if confirm == "y":
                removed_titles = []
                for i in indexes:
                    removed = active_tasks.pop(i)
                    removed_titles.append(removed['title'])
                save_tasks(tasks)
                print(f"\nRemoved tasks: {', '.join(removed_titles)}\n")
                break  # go to submenu
            elif confirm == "m":
                print("\nReturning to main menu...\n")
                return
            else:  # confirm == 'n'
                print("\nOkay, you can edit your input.\n")
                continue  # goes back to task number input

        # Submenu
        while True:
            choice = input("Do you want to:\nr) Remove more tasks\nm) Return to main menu\n \nChoice (r/m): ").lower()
            if choice == "r":
                break
            elif choice == "m":
                print("\nReturning to main menu...\n")
                return
            else:
                print("\nInvalid choice. Enter 'r' or 'm'.\n")



# View tasks
def view_tasks():
    tasks = load_tasks()
    active_tasks = tasks["active"]
      
    
    if not active_tasks:
        print("\nNo active tasks.\n")
    else:
        print("\nActive Tasks:\n")
        for idx, task in enumerate(active_tasks, start=1):
            deadline = task.get("deadline", "No deadline")
            print(f"{idx}. {task['title']} | Deadline: {deadline}")
        print("\n")  

    
    while True:
        choice = input("Press 'm' to return to the main menu: ").lower()
        if choice == "m":
            print("\nReturning to main menu...\n")
            return
        else:
            print("Invalid input. Please press 'm' to return.")


# Complete task
def complete_task():
    tasks = load_tasks()
    
    while True:
        active_tasks = tasks["active"]
        if not active_tasks:
            print("\nNo active tasks to complete.\n")
            return

        print("\nThese are your current tasks:\n")
        for idx, task in enumerate(active_tasks, start=1):
            print(f"{idx}. {task['title']}")

        while True:  # Input loop for task numbers
            choices = input("\nEnter task numbers to complete (comma-separated) or 'm' to return: ")
            if choices.lower() == "m":
                print("\nReturning to main menu...\n")
                return

            try:
                indexes = sorted({int(c.strip()) - 1 for c in choices.split(",")}, reverse=True)
                if any(i < 0 or i >= len(active_tasks) for i in indexes):
                    raise ValueError
            except ValueError:
                print("\nInvalid input! Please separate task numbers with commas and use valid numbers.\n")
                continue  # go back to input prompt

            # Confirmation
            print("\nYou selected to complete:")
            for i in indexes:
                print(f"- {active_tasks[i]['title']}")

            confirm = input("\nAre you sure? (y/n/m): ").lower()
            if confirm == "y":
                completed_titles = []
                for i in indexes:
                    task = active_tasks.pop(i)
                    task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    tasks["completed"].append(task)
                    completed_titles.append(f"{task['title']}")
                save_tasks(tasks)
                print(f"\n✔ Completed tasks:\n" + "\n".join(completed_titles) + "\n")
                break  # go to submenu
            elif confirm == "m":
                print("\nReturning to main menu...\n")
                return
            else:  # confirm == 'n'
                print("\nOkay, you can edit your input.\n")
                continue  # go back to task number input

        # Submenu
        while True:
            choice = input("Do you want to:\nc) Complete more tasks\nm) Return to main menu\n \nChoice (c/m): ").lower()
            if choice == "c":
                break  # go back to top of outer loop
            elif choice == "m":
                print("\nReturning to main menu...\n")
                return
            else:
                print("\nInvalid choice. Enter 'c' or 'm'.\n")


# Main menu
def main_menu():
    while True:
        print(f"\nWelcome to VoidTasks\n")
        print(f"Organize. Conquer. Escape the Void.")

        print(f"\n{BOLD}{CYAN}📂 Task Manager 📂{RESET}\n")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Complete Task")
        print("5. Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main_menu()

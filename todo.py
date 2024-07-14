from datetime import datetime
import json

TASKS_FILE = 'tasks.json'
PRIORITY_LEVELS = ['low', 'medium', 'high']

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

tasks = load_tasks()

def add_task(description, priority, due_date):
    if priority not in PRIORITY_LEVELS:
        print("Invalid priority level. Choose from: low, medium, high.")
        return
    task = {
        'description': description,
        'priority': priority,
        'completed': False,
        'due_date': due_date
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")

def remove_task(index):
    try:
        tasks.pop(index)
        save_tasks(tasks)
        print("Task removed successfully.")
    except IndexError:
        print("Invalid task number.")

def mark_task_completed(index):
    try:
        tasks[index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except IndexError:
        print("Invalid task number.")

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks):
        status = "Completed" if task['completed'] else "Pending"
        print(f"{i + 1}. [{status}] {task['description']} (Priority: {task['priority']}, Due: {task['due_date']})")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Task description: ")
            priority = input("Task priority (low, medium, high): ")
            due_date = input("Due date (YYYY-MM-DD): ")
            add_task(description, priority, due_date)
        elif choice == '2':
            index = int(input("Task number to remove: ")) - 1
            remove_task(index)
        elif choice == '3':
            index = int(input("Task number to mark as completed: ")) - 1
            mark_task_completed(index)
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

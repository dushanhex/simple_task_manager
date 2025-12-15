# Simple Task Manager
tasks = []

def show_menu():
    print("\n=== Task Manager ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    print(f"✓ Added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    
    print("\nYour tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "○"
        print(f"{i}. [{status}] {task['task']}")

def complete_task():
    view_tasks()
    if tasks:
        num = int(input("Enter task number to complete: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["completed"] = True
            print(f"✓ Completed: {tasks[num-1]['task']}")

def delete_task():
    view_tasks()
    if tasks:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"✓ Deleted: {removed['task']}")

# Main program loop
while True:
    show_menu()
    choice = input("\nChoose option (1-5): ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")
tasks = []

# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file]
except FileNotFoundError:
    pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

while True:
    print("\n📋 Task Manager")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")

    elif choice == "2":
        new_task = input("Enter new task: ")
        tasks.append("[ ] " + new_task)
        save_tasks()
        print("Task added!")

    elif choice == "3":
        task_num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num] = tasks[task_num].replace("[ ]", "[x]")
            save_tasks()
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks.pop(task_num)
            save_tasks()
            print("Task deleted!")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")

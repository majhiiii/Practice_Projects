# Define a list to store tasks
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks added yet.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    if tasks:
        try:
            index = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")

def to_do_list_app():
    print("Welcome to the To-Do List App!")

    while True:
        print("\nChoose an option:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    to_do_list_app()

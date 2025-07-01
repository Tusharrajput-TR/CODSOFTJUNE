tasks = []

def show_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Exit")
    choice = input("Choose: ")
    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        break
    else:
        print("Invalid option.")

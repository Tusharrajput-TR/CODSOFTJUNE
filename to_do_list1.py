task_lst=[]
def add_task():
    enter_task=input("Enter the task:")
    task_lst.append(enter_task)
def remove_task_():
    remove_task=input("Enter the task:")
    if remove_task in task_lst:
        task_lst.remove(remove_task)
    else:
        print("The task doesn't exist")
def view_task():
    print(task_lst)

while True :
    print("Main Menu")
    print("1. Add task")
    print("2. Remove task")
    print("3. View task")
    print("4. Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        add_task()
    elif ch==2:
        remove_task_()
    elif ch==3:
        view_task()
    elif ch==4:
        break
    else:
        print("Invalid choice,Try again!")

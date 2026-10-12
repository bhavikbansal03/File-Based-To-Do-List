from pathlib import Path

TASKS_FILE = Path(__file__).parent / "Tasks.txt"

lines = []
with open(TASKS_FILE, "r") as f:
    for i in f:
        lines.append(i.strip())

def add_task(task_list):
    task = input("Enter task to be added: ")

    with open(TASKS_FILE, "a") as f:
        f.write(f"{task}\n")
        task_list.append(task)
        print("Task has been added")

def view(task_list):
    if not task_list:
        print("Your list is currently empty")
        return
    for index, task_name in enumerate(task_list, 1):
        print(f"{index}. {task_name}")

def delete(task_list, number):
    if not task_list:
        print("Your list is currently empty")
        return
    if number < 1 or number > len(task_list):
        print("Invalid task number")
        return
    task_list.pop(number-1)
    with open(TASKS_FILE, "w") as f:
            f.write("\n".join(task_list))

while True:
    user_choice = input("Enter-> Add, Exit, View or Delete: ").lower().strip().capitalize()

    if (user_choice == "Exit"):
        break
    elif(user_choice == "Add"):
        add_task(lines)
    elif(user_choice == "View"):
        view(lines)
    elif(user_choice == "Delete"):
        del_item = int(input("Enter task number to be deleted: "))
        delete(lines, del_item)
    else: 
        print("Invalid command, please try again.")
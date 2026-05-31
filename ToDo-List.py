import json
tasks = []    
menu = """
    1. Add Task
    2.  View Tasks
    3.  Complete Task
    4.  Delete Task
    5.  Exit
"""
while True:
    print(menu)
    user = int(input("Enter choice:"))
    if user ==1 :
        task = input("Enter Task:")
        tasks.append(task)
        print(f"Task is Added : {task}")
    
    elif user == 2 :
        if len(tasks) == 0:
            print("No Tasks")
        else:
            for i, task in enumerate(tasks,1):
                print(f"{i}. {task}")
    elif user == 3:
        if len(tasks) == 0:
            print("No Tasks")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Which task completed? : "))
            tasks[num-1] = f"{tasks[num-1]}"
            print("Task is Completed")
    
    elif user == 4:
        if len(tasks) ==0:
            print("NO tasks")
        else:
            for i , task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            num = int(input("Which task delete ? :"))
            removed = tasks.pop(num-1)
            print(f"Deleted : {removed}")
            

    elif user == 5:
        print("Good by")
        break
    else:
        print("Invalid Choice")
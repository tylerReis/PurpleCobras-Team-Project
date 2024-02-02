
'''
object
actual task
due date and time

'''

# class ManageTasks:
#     def __init__(self, task, due_date):
#         self.task = task
#         self.due_date = due_date

# def manage_task(task, due_date):
#     task_object = ManageTasks(task=task, due_date=due_date)

#     return task_object

# my_task_object = manage_task(task=input("Input task here."), due_date=input("Input due date in YYYYMMDD format."))

tasks_dict = {}

def create_task(tasks, task, due_date):
    tasks[task] = {
        "name_of_task" : task,
        "due_date" : due_date,
    }


def update_task(tasks, existing_task, new_task_name, new_due_date, complete = False):
    if existing_task in tasks:
        tasks[new_task_name] = {
            "name_of_task" : new_task_name,
            "due_date" : new_due_date,
            "complete" : complete if complete == True else tasks[existing_task].get("complete", False)
        }

        del tasks[existing_task]
    else:
        print("Task does not exist, therefore cannot be updated.")


def delete_task(tasks, existing_task):
    if existing_task in tasks:
        del tasks[existing_task]
    else: 
        print("Task does not exist, therefore cannot be deleted.")

# def reading_task():
    
# def list_all_tasks():
#     for task, info in tasks.items():
#         print(f"Task: {info['name_of_task']}, Due Date: {info['due_date']}, Complete: {info['complete']}")

create_task(tasks_dict, "Coding", "2024-02-03")
create_task(tasks_dict, "Testing", "2024-02-02")
# print(tasks_dict)

# update_task(tasks_dict, "Coding", "Assignment", "2024-02-09", "False")
# print(tasks_dict)

# delete_task(tasks_dict, "Coding")

# list_all_tasks(tasks_dict)

# create_task(tasks_dict, "Stand Down", "2024-02-02")
# update_task(tasks_dict, "Stand Down", "Stand Down", "2024-02-02", "True")

# print(tasks_dict)

import json

tasks = []

# Defining a function to load tasks from a JSON file
def load_tasks():
    try:
        # Using a with statement to open a file in read mode, ensuring it gets properly closed
        with open('tasks.json', 'r') as file:
            # Using the global keyword to indicate that the tasks variable is global
            global tasks
            # Using json.load() to deserialize the JSON data from the file into a Python object
            tasks = json.load(file)
            print("Tasks loaded successfully.")
            
    except FileNotFoundError:
        # Handling the case where the tasks.json file does not exist
        print("No saved tasks found.")

# Calling the load_tasks function to load tasks from the tasks.json file
load_tasks()


# Defining a function to save tasks to a JSON file
def save_tasks():
    # Using a with statement to open a file in write mode, ensuring it gets properly closed
    with open('tasks.json', 'w') as file:
        # Using json.dump() to serialize the tasks list to JSON and write it to the file
        json.dump(tasks, file)
    print("Tasks saved successfully.")

# Calling the save_tasks function to create an empty tasks.json file
save_tasks()


# Defining a function to add a new task
def add_task(task, deadline=None, category="General"):
    # Creating a new dictionary to represent the task
    tasks.append({'task': task, 'deadline': deadline, 'category': category, 'status': 'pending'})
    print(f"Added task: {task} with deadline {deadline} in category of {category}")
    # Saving the updated tasks list to the JSON file
    save_tasks()



# Defining a function to show tasks
def show_tasks(sort_by=None):
    # If sorting by deadline, using the sorted() function with a lambda function as the key
    if sort_by == 'deadline':
        sorted_tasks = sorted(tasks, key=lambda x: x['deadline'] or "")
    # If sorting by category, using the sorted() function with a lambda function as the key
    elif sort_by == 'category':
        sorted_tasks = sorted(tasks, key=lambda x: x['category'])
    else:
        # If not sorting, just using the original tasks list
        sorted_tasks = tasks
        
    print("To-Do List:")
    # If the tasks list is empty, printing a message
    if not sorted_tasks:
        print("No tasks found")
        return
        
    # Iterating over the sorted tasks list and printing each task
    for index, task in enumerate(sorted_tasks, start=1):
        status = task['status']
        deadline = task['deadline'] or "No deadline"
        category = task['category']
        print(f"{index}. {task['task']} [{status}] - Deadline: {deadline}, Category: {category}")





# Main program loop
while True:
    # Loading tasks from the JSON file
    load_tasks()
    # Printing the menu options
    print("Options: (1)Add Task. (2)Show Task. (3)Mark Task as Completed. (4)Delete Task.  (5)Sort by Deadline. (6)Sort by category. (7)Quit")
    # Getting the user's choice
    choice = input("Enter your Choice")
    
    
    if choice == '1':
        task = input("Enter task:")
        deadline = input("Enter deadline (optional): ")
        category = input("Enter category (optional): ")
        add_task(task, deadline, category)
        
    elif choice == '2':
        task = input("Enter task to show: ")
        show_tasks(task)
        
    elif choice == '3':
        task = input("Enter task to mark as completed: ")
        # mark_task_completed(task)
        
    elif choice == '4':
        print("you choose task 4 - Delete")
        # delete_tasks(task)
        
    elif choice == '5':
        print("you choose task 5 - sort by deadline")
        # show_tasks(sort_by='deadline')
        
    elif choice == '6':
        print("you choose task 6 - sort by category")
        # show_tasks(sort_by='category')
        
    elif choice == '7':
        print("GoodByessss!")
        # save_tasks()
        
        break
    
    else: 
        print("Invalid choice, please try again.")















# # Defining a function to delete a task
# def delete_task(task):
#     # Iterating over the tasks list to find the task to delete
#     for t in tasks:
#         if t['task'] == task:
#             # Removing the task from the list
#             tasks.remove(t)
#             print(f"Task deleted: {task}")
#             # Saving the updated tasks list to the JSON file
#             save_tasks()
#             return
#     # If the task is not found, do nothing (you may want to add an error message here)

# # Defining a function to mark a task as completed
# def mark_task_completed(task):
#     # Iterating over the tasks list to find the task to mark as completed
#     for t in tasks:  # Corrected 'task' to 'tasks'
#         if t['task'] == task:
#             # Updating the task's status to 'completed'
#             t['status'] = 'completed'  # Corrected 'cmpleted' to 'completed'
#             print(f"Marked task as completed: {task}")
#             # Saving the updated tasks list to the JSON file
#             save_tasks()
#             return
#     # If the task is not found, do nothing (you may want to add an error message here)












# Add a task
# Remove a task
# Edit a task
# Add a description
# Edit a description
# Validate user input

# Inicial tasks list
tasks = []
descriptions = {}

# Auxiliary functions
def displayTasks(all_tasks, descriptions):
    print('\nYour tasks: ')

    if len(all_tasks) <= 0:
        print('No tasks!')
    else:
        for index, task in enumerate(all_tasks):
            print(f'{index+1}: {task} - {descriptions[task]}')

def newOperation(all_tasks, descriptions):
    print(descriptions)
    operation = input("\nPress 'A' to add a new task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: ")

    if operation == 'A':
        addTask(all_tasks, descriptions)
    elif operation == 'E':
        editTask(all_tasks, descriptions)
    elif operation == 'R':
        removeTask(all_tasks, descriptions)
    elif operation == 'F':
        return
    else:
        newOperation(all_tasks, descriptions)

def validTaskNumber(all_tasks, operation):
    task_number = input(f'Enter the number of the task you want to {operation}: ')

    valid = False
    while not valid:
        try:
            number = int(task_number)
            valid = True
        except:
            task_number = input('Please provide a valid task number: ')

    if not (0 < number <= len(all_tasks)):
        print('Task not found!')
        validTaskNumber(all_tasks, operation)
    else:
        return number

# Operations
def addDescription(task, descriptions):
    description = input('Add a description: ')
    descriptions[task] = description

    return descriptions

def editTask(all_tasks, descriptions):
    task_number = validTaskNumber(all_tasks, 'edit')

    new_task = input('Edit task: ')
    all_tasks[task_number-1] = new_task
    addDescription(new_task, descriptions)

    print(f'Item {task_number} edited!')

    displayTasks(all_tasks, descriptions)
    newOperation(all_tasks, descriptions)

def removeTask(all_tasks, descriptions):
    task_number = validTaskNumber(all_tasks, 'remove')

    del descriptions[all_tasks[task_number-1]]
    all_tasks.remove(all_tasks[task_number-1])

    print(f'\nItem {task_number} removed!')

    displayTasks(all_tasks, descriptions)
    newOperation(all_tasks, descriptions)

def addTask(all_tasks, descriptions):
    new_task = input('Add a task: ')
    all_tasks.append(new_task)
    new_descriptions = addDescription(new_task, descriptions)

    displayTasks(all_tasks, new_descriptions)
    newOperation(all_tasks, descriptions)
        
# Start application
addTask(tasks, descriptions)
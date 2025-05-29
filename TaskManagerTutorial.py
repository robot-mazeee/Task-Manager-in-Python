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
def display_tasks(all_tasks, descriptions):
    print('\nYour tasks: ')

    if len(all_tasks) <= 0:
        print('No tasks!')
    else:
        for index, task in enumerate(all_tasks):
            print(f'{index+1}: {task} - {descriptions[task]}')

def new_operation(all_tasks, descriptions):
    operation = input("\nPress 'A' to add a new task, 'E' to edit a task, 'R' to remove a task or 'F' to quit the application: ")

    if operation == 'A':
        add_task(all_tasks, descriptions)
    elif operation == 'E':
        edit_task(all_tasks, descriptions)
    elif operation == 'R':
        remove_task(all_tasks, descriptions)
    elif operation == 'F':
        return
    else:
        new_operation(all_tasks, descriptions)

def valid_task_number(all_tasks, operation):
    while True:
        task_number = input(f'Enter the number of the task you want to {operation}: ')
        try:
            task_number = int(task_number)
            if (0 < task_number <= len(all_tasks)):
                break
            else:
                print('Task not found! Please enter a valid task number.\n')
        except ValueError:
            print('Invalid input! Please enter a valid task number.\n')

    return task_number

# Operations
def add_description(task, descriptions):
    description = input('Add a description: ')
    descriptions[task] = description

    return descriptions

def edit_task(all_tasks, descriptions):
    task_number = valid_task_number(all_tasks, 'edit')

    new_task = input('Edit task: ')
    all_tasks[task_number-1] = new_task
    add_description(new_task, descriptions)

    print(f'Item {task_number} edited!')

    display_tasks(all_tasks, descriptions)
    new_operation(all_tasks, descriptions)

def remove_task(all_tasks, descriptions):
    task_number = valid_task_number(all_tasks, 'remove')

    del descriptions[all_tasks[task_number-1]]
    all_tasks.remove(all_tasks[task_number-1])

    print(f'\nItem {task_number} removed!')

    display_tasks(all_tasks, descriptions)
    new_operation(all_tasks, descriptions)

def add_task(all_tasks, descriptions):
    new_task = input('Add a task: ')
    all_tasks.append(new_task)
    new_descriptions = add_description(new_task, descriptions)

    display_tasks(all_tasks, new_descriptions)
    new_operation(all_tasks, descriptions)
        
# Start application
add_task(tasks, descriptions)
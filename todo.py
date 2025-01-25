import argparse
import json
import os

# Define the CLI arguments
parser = argparse.ArgumentParser(description='To-Do List Manager')
subparsers = parser.add_subparsers(dest='command')

# Add task arguments
add_parser = subparsers.add_parser('add')
add_parser.add_argument('-d', '--description', required=True, help='Task description')

# Update task arguments
update_parser = subparsers.add_parser('update')
update_parser.add_argument('-i', '--id', required=True, type=int, help='Task ID')
update_parser.add_argument('-d', '--description', help='New task description')
update_parser.add_argument('-s', '--status', choices=['pending', 'completed'], help='New task status')

# Delete task arguments
delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('-i', '--id', required=True, type=int, help='Task ID')

# List tasks arguments
list_parser = subparsers.add_parser('list')

# Load the to-do list from file
def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as f:
            return json.load(f)
    else:
        return []

# Save the to-do list to file
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump(tasks, f)

# Add a new task
def add_task(description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {'id': task_id, 'description': description, 'status': 'pending'}
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added with ID {task_id}')

# Update a task
def update_task(task_id, description=None, status=None):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if description:
                task['description'] = description
            if status:
                task['status'] = status
            save_tasks(tasks)
            print(f'Task {task_id} updated')
            return
    print(f'Task {task_id} not found')

# Delete a task
def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            del tasks[i]
            save_tasks(tasks)
            print(f'Task {task_id} deleted')
            return
    print(f'Task {task_id} not found')

# List tasks
def list_tasks():
    tasks = load_tasks()
    for task in tasks:
        print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")

# Main function
def main():
    args = parser.parse_args()
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description, args.status)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'list':
        list_tasks()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
    
  

import argparse

class Task:
    def __init__(self, task_name, status="Incomplete"):
        self.task_name = task_name
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(Task(task_name))

    def update_task_status(self, task_name, new_status):
        next((task for task in self.tasks if task.task_name == task_name), None).status = new_status

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for task in self.tasks:
                print(f"{task.task_name} - {task.status}")

def main():
    parser = argparse.ArgumentParser(description="Command-line To-Do List application.")
    parser.add_argument("--add", help="Add a new task to the list.")
    parser.add_argument("--update", help="Update the status of an existing task.")
    args = parser.parse_args()

    todo_list = ToDoList()

    if args.add:
        todo_list.add_task(args.add)
        print(f"Task '{args.add}' added to the list.")
    elif args.update:
        new_status = input("Enter the new status (e.g., 'Complete', 'Incomplete'): ")
        todo_list.update_task_status(args.update, new_status)
        print(f"Task '{args.update}' status updated to '{new_status}'.")
    else:
        todo_list.display_tasks()

if __name__ == "__main__":
    main()

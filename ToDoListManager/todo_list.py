import json
from typing import List, Dict, Any
from datetime import datetime
from tabulate import tabulate

class ToDoList:
    def __init__(self) -> None:
        self.tasks: List[Dict[str, Any]] = self.load_tasks()

    def add_task(self) -> None:
        while True:     #Prompt for tas description
            description: str = input("Enter task description: ")
            if description.strip():
                break
            else:
                print("Description cannot be empty. Please enter a valid description.")

        while True:     #Prompt for due date
            task_date = input("Enter Date yyyy-mm-dd: ")
            try:
                due_date = datetime.strptime(task_date.strip(), "%Y-%m-%d").date()
                break
            except ValueError:
                print("INVALID date. Please use the format yyyy-mm-dd.")

        category: str = input("Enter task category(or press Enter to skip): ")

        while True:     #Prompt for priority
            priority_input: str = input("Enter task priority (1-5) (or press Enter to skip): ")
            if priority_input:
                try:
                    priority = int(priority_input)
                    if 1 <= priority <= 5:
                        break
                    else:
                        print("Priority must be between 1 and 5.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                priority = 3    # Default priority if input is skipped
                break

        task: Dict[str, Any] = {
            "category": category,
            "task": description,
            "priority": priority,
            "due": due_date.strftime("%Y-%m-%d"),
            "done": False
        }
        self.tasks.append(task)
        print("Your task was successfully added!")
        self.save_tasks()

    def view_tasks(self) -> None:
        if not self.tasks:      #Check if there some tasks
            print("No task available")
        else:
            sorted_tasks = sorted(self.tasks, key=lambda x: x['priority'])
            table = []
            for idx, task in enumerate(sorted_tasks, start=1):
                status = "[✔]" if task["done"] else "[ ]"
                due_info = f" (Due: {task['due']})" if task.get("due") else ""
                table.append([idx, task["category"], task["task"], task["priority"], due_info, status])
            print(tabulate(table, headers=["#", "Category", "Task", "Priority", "Due Date", "Done"], tablefmt="grid"))

    def mark_task_as_done(self, task_number: int) -> None:
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["done"] = True
            self.save_tasks()
        else:
            print("Invalid task number")

    def remove_task(self, task_number: int) -> None:
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]
            self.save_tasks()
        else:
            print("Invalid task number")
    
    def save_tasks(self) -> None:
        with open("tasks.txt", "w", encoding="utf-8") as f:
            for task in self.tasks:
                f.write(json.dumps(task) + '\n')

    def load_tasks(self) -> List[Dict[str, Any]]:
        tasks: List[Dict[str, Any]] = []
        try:
            with open("tasks.txt", "r", encoding="utf-8") as f:
                for line in f:
                    tasks.append(json.loads(line.strip()))
        except FileNotFoundError:       ### DONT DELETE!!!
            print("\nThere are no file found, but we can make a new one")
        return tasks

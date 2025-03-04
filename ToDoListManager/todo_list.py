import json
from typing import List, Dict, Any
from datetime import datetime
from tabulate import tabulate

class ToDoList:
    def __init__(self) -> None:
        self.tasks: List[Dict[str, Any]] = self.load_tasks()

    def add_task(self) -> None:
        description: str = input("Enter task description: ")
        while True:
            task_date = input("Enter Date yyyy-mm-dd: ")
            try:
                due_date = datetime.strptime(task_date.strip(), "%Y-%m-%d").date()
                break
            except ValueError:
                print("INVALID date. Please use the format yyyy-mm-dd.")
        task: Dict[str, Any] = {
            "task": description,
            "due": due_date.strftime("%Y-%m-%d"),
            "done": False
        }
        self.tasks.append(task)
        print("Your task was successfully added!")
        self.save_tasks()

    def view_tasks(self) -> None:
        if not self.tasks: #There are no task
            print("No task available")
        else:
            table = []
            for idx, task in enumerate(self.tasks, start=1):
                status = "[✔]" if task["done"] else "[ ]"
                due_info = f" (Due: {task['due']})" if task.get("due") else ""
                table.append([idx, task["task"], due_info, status])
            print(tabulate(table, headers=["#", "Task", "Due Date", "Done"], tablefmt="grid"))

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
        except FileNotFoundError: ### DONT DELETE!!!
            print("There are no file found, but we can make a new one")
        return tasks

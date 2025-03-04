import json
from typing import List, Dict, Any

class ToDoList:
    def __init__(self):
        self.tasks: List[Dict[str, Any]] = self.load_tasks()

    def add_task(self, task) -> None:
        description: str = input("Enter task description: ")
        task: Dict[str, Any] = {"task": description, "done": False}
        self.tasks.append(task)
        print("Your task was successfully added!")
        self.save_tasks()

    def view_tasks(self) -> None:
        if not self.tasks: #There are no task
            print("No task available")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "[✔]" if task["done"] else "[ ]"
                print(f"{idx}. {task['task']} {status}")

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

def main() -> None:
    todo_list = ToDoList()    
    while True:
        print("\n===== To-Do List Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.add_task("")
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_number = int(input("Enter the task number to mark as done: "))
            todo_list.mark_task_as_done(task_number)
        elif choice == "4":
            task_number = int(input("Enter the task number to remove: "))
            todo_list.remove_task(task_number)
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")
    print("See you later 👋👋")

if __name__ == "__main__":
    main()

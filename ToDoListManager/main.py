from todo_list import ToDoList

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
            todo_list.add_task()
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to mark as done: "))
                todo_list.mark_task_as_done(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            try:
                task_number = int(input("Enter the task number to remove: "))
                todo_list.remove_task(task_number)
            except ValueError:
                    print("Please enter a valid number.")
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")
    print("See you later 👋👋")

if __name__ == "__main__":
    main()

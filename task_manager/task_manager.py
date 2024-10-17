import json

class Task:
    def __init__(self,id,title,completed=False):
        self.id=id
        self.title=title
        self.completed=completed
        
    def __repr__(self):
        status = 'completed' if self.completed else 'Incompleted'
        return f"[{self.id}]: {self.title} ({status})"
    
user_id = "test@gmail.com"
password = "test@123"

def login():
    print("=== Login ===")
    email = input("Enter email: ")
    password = input("Enter password: ")

    if email == user_id and password == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials. Try again.\n")
        return False   
    
tasks = []

def add_task(tasks,title):
    task_id = len(tasks)+1
    new_task=Task(task_id,title)
    tasks.append(new_task)
    print(f"Task '{title}' added successfully")

def view_tasks(tasks):
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks available.")

def delete_task(tasks,task_id):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            print(f"Task {task_id} deleted successfully.")
            return
    print(f"Task {task_id} not found.")

def complete_task(tasks,task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task {task_id} marked as completed.")
            return
    print(f"Task {task_id} not found.")  

def save_tasks_to_file(tasks,filename='tasks.json'):
    with open(filename, 'w') as f:
        json.dump([task.__dict__ for task in tasks], f)
    print("Tasks saved to {filename}")

def load_tasks_from_file(filename='tasks.json'):
    try:
        with open(filename, 'r') as f:
            tasks_data = json.load(f)
            return [Task(**task) for task in tasks_data]
    except FileNotFoundError:
        return []
        
def show_menu():
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Save Tasks")
    print("6. Load Tasks")
    print("7. Exit")

def main():
    if not login():
        return
    tasks = load_tasks_from_file()  # Load tasks on start

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(tasks,title)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks,task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to mark complete: "))
            complete_task(tasks,task_id)
        elif choice == '5':
            save_tasks_to_file(tasks)
        elif choice == '6':
            tasks=load_tasks_from_file
            print("Task loaded from file")
        elif choice == '7':
            break
        else:
            print("Invalid choice. try again.")

if __name__ == "__main__":
    main()    
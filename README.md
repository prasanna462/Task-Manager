TASK MANAGER FOR CLI

Here's a basic structure you can use for your README.md file to explain how your Task Manager CLI application works, including installation, usage, and login information:

Task Manager CLI Application
Project Overview

The Task Manager CLI Application is a simple command-line tool that allows users to manage their daily tasks. Users can:

Add new tasks.
View existing tasks.
Delete tasks by their ID.
Mark tasks as completed.
Save and load tasks from a file.
The application requires a login with dummy credentials for testing purposes and stores tasks in a JSON file.

Features
Add Task: Add new tasks with a unique ID and description.
View Tasks: Display all tasks with their status (completed or not).
Delete Task: Remove tasks by specifying their ID.
Complete Task: Mark tasks as completed.
Save Tasks: Save the current tasks to a JSON file (tasks.json).
Load Tasks: Load previously saved tasks from the JSON file.
Prerequisites
Python 3.x should be installed on your system.
The json module is part of the Python Standard Library, so no additional libraries are required.
Installation
Clone the repository:

bash
Copy code
git clone <https://github.com/prasanna462/Task-Manager/tree/main/task_manager>
cd task_manager_cli
Run the application:

bash
Copy code
python task_manager.py
How to Use
Login:

Email: test@gmail.com
Password: test@123
Upon running the application, you will be prompted to enter the email and password for login. Use the credentials provided above.

Task Manager Menu: After successful login, you will see a menu with the following options:

markdown
Copy code
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Completed
5. Save Tasks
6. Load Tasks
7. Exit
Select an option by entering the corresponding number and following the prompts.

Examples:

To add a task, select option 1, then enter the task description.
To view tasks, select option 2.
To delete a task, select option 3, then enter the task ID.
To mark a task as completed, select option 4, then enter the task ID.
Saving and Loading Tasks:

Tasks are automatically saved to a file named tasks.json when you select option 5 (Save Tasks).
You can load previously saved tasks by selecting option 6 (Load Tasks).
Files
task_manager.py: The main Python script that runs the task manager.
tasks.json: This file stores your tasks in JSON format (created after saving tasks).

Dummy Login Credentials
For testing purposes, use the following login credentials:

Email: test@gmail.com
Password: test@123

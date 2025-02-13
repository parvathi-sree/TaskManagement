import sqlite3
from datetime import datetime

# Database setup
conn = sqlite3.connect('tasks.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    deadline TEXT,
    status TEXT NOT NULL
)''')
conn.commit()

# Function to add a task
def add_task():
    description = input('Enter task description: ')
    deadline = input('Enter deadline (YYYY-MM-DD) or leave blank: ')
    status = 'pending'
    c.execute('INSERT INTO tasks (description, deadline, status) VALUES (?, ?, ?)', (description, deadline, status))
    conn.commit()
    print('Task added successfully!')

# Function to view all tasks
def view_tasks():
    c.execute('SELECT * FROM tasks')
    tasks = c.fetchall()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print('No tasks found.')

# Function to view pending tasks
def view_pending_tasks():
    c.execute('SELECT * FROM tasks WHERE status = "pending"')
    tasks = c.fetchall()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print('No pending tasks.')

# Function to view completed tasks
def view_completed_tasks():
    c.execute('SELECT * FROM tasks WHERE status = "completed"')
    tasks = c.fetchall()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print('No completed tasks.')

# Function to update a task
def update_task():
    task_id = input('Enter task ID to update: ')
    new_description = input('Enter new description or leave blank to keep the same: ')
    new_status = input('Enter new status (pending/completed): ')
    if new_description:
        c.execute('UPDATE tasks SET description = ? WHERE id = ?', (new_description, task_id))
    if new_status:
        c.execute('UPDATE tasks SET status = ? WHERE id = ?', (new_status, task_id))
    conn.commit()
    print('Task updated successfully!')

# Function to delete a task
def delete_task():
    task_id = input('Enter task ID to delete: ')
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    print('Task deleted successfully!')

# Main menu
while True:
    print('\nTask Management Application')
    print('1. Add a task')
    print('2. View all tasks')
    print('3. View pending tasks')
    print('4. View completed tasks')
    print('5. Update a task')
    print('6. Delete a task')
    print('7. Exit')
    choice = input('Enter your choice: ')
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_pending_tasks()
    elif choice == '4':
        view_completed_tasks()
    elif choice == '5':
        update_task()
    elif choice == '6':
        delete_task()
    elif choice == '7':
        break
    else:
        print('Invalid choice. Please try again.')

conn.close()

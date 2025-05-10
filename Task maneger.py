import tkinter as tk
from tkinter import messagebox
import random
import json

TASKS_FILE = "tasks.json"

# Store tasks
tasks = []

# Motivational messages
completed_messages = [
    "Great job! One step closer to your goal! 🌟",
    "Well done! Keep up the momentum! 💪",
    "You're crushing it! ✅",
    "Every finished task is a win! 🏆",
    "Awesome! Keep moving forward! 🚀"
]

# Encouraging messages
not_completed_messages = [
    "No worries! You can tackle it when you're ready. 🌱",
    "It's okay to take your time. You'll get there! ⏳",
    "Stay positive! Small steps matter. 💡",
    "Not now doesn’t mean never. Keep going! 💫",
    "Progress isn’t always a straight line. You've got this! 🧠"
]

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open(TASKS_FILE, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Add a new task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        task_entry.delete(0, tk.END)
        save_tasks()
        view_tasks()
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

# View tasks in the list
def view_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️" if task["completed"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['task']}")

# Mark selected task as complete
def complete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "No task selected.")
        return
    index = selected[0]
    tasks[index]["completed"] = True
    save_tasks()
    view_tasks()
    messagebox.showinfo("Task Completed", random.choice(completed_messages))

# Exit application
def exit_app():
    save_tasks()
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Task Manager")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_app, bg="red", fg="white")
exit_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50)
task_listbox.pack(pady=10)

# Load and display tasks at startup
load_tasks()
view_tasks()

# Run the application
root.mainloop()


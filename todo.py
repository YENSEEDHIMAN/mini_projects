from tkinter import *
from tkinter import messagebox
import tkinter as tk

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        task_entry.delete(0, END)
        update_task_list()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to remove a task
def remove_task():
    try:
        selected_task = task_listbox.get(ACTIVE)
        tasks.remove(selected_task)
        update_task_list()
    except:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# Function to update the listbox with current tasks
def update_task_list():
    task_listbox.delete(0, END)
    for task in tasks:
        task_listbox.insert(END, task)

    # Check if all tasks are completed
    if not tasks:
        messagebox.showinfo("Congratulations!", "You completed today's tasks, congratulations! 🎉")

# Function to create the main screen
def mainscreen():
    global root, task_entry, task_listbox

    # Create the main window
    root = tk.Tk()
    root.config(bg="lightblue")
    root.title("To-Do List")
    root.geometry("360x400")

    # Title Label
    Label(root, text="Daily Tasks", font=("Lato Black", 14), bg="lightblue").pack(pady=10)

    # Task Entry Field
    task_entry = Entry(root, font="Roboto 12", bg="white", relief=GROOVE, bd=1)
    task_entry.pack(pady=5)

    # Add and Remove Buttons
    Button(root, text="Add Task", height=1, width=10, bg="#39a3be", fg="white", bd=1, command=add_task).pack(pady=5)
    Button(root, text="Remove Task", height=1, width=10, bg="#e74c3c", fg="white", bd=1, command=remove_task).pack(pady=5)

    # Task Listbox
    task_listbox = Listbox(root, font="Roboto 12", selectbackground="#39a3be", activestyle="none")
    task_listbox.pack(pady=10, fill=BOTH, expand=True)

    # Start the Tkinter event loop to display the window
    root.mainloop()

# Call the function to display the main screen
mainscreen()

import tkinter as tk
from tkinter import messagebox
import sqlite3

def db():
    conn = sqlite3.connect('to_do_list0.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            homework TEXT,
            date TEXT,
            subject TEXT
        )
    ''')
    conn.commit()
    return conn, cursor


def load_tasks():
    task_listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        task_listbox.insert(tk.END, f"{row[0]} - Staff Name: {row[1]}, Homework: {row[2]}, Date: {row[3]}, Subject: {row[4]}")

def add_task():
    name = name_entry.get()
    homework = homework_entry.get()
    date = date_entry.get()
    subject = subject_entry.get()

    if name and homework and date and subject:
        cursor.execute("INSERT INTO tasks (name, homework, date, subject) VALUES (?, ?, ?, ?)",
                       (name, homework, date, subject))
        conn.commit()
        load_tasks()
        name_entry.delete(0, tk.END)
        homework_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please fill all fields")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_id = task_listbox.get(selected_task).split(' ')[0]
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        load_tasks()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete")

def update_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_id = task_listbox.get(selected_task).split(' ')[0]

      
        cursor.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
        current_task = cursor.fetchone()

        
        name = name_entry.get() or current_task[1]
        homework = homework_entry.get() or current_task[2]
        date = date_entry.get() or current_task[3]
        subject = subject_entry.get() or current_task[4]

        cursor.execute("UPDATE tasks SET name=?, homework=?, date=?, subject=? WHERE id=?",
                       (name, homework, date, subject, task_id))
        conn.commit()
        load_tasks()

        name_entry.delete(0, tk.END)
        homework_entry.delete(0, tk.END)
        date_entry.delete(0, tk.END)
        subject_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to update")



root = tk.Tk()
root.title("To-Do List Application")
root.configure(bg="#81A594")


conn, cursor = db()


tk.Label(root, text="Staff Name:", bg="#81A594").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root, width=50)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the Homework:", bg="#81A594").grid(row=1, column=0, padx=10, pady=10)
homework_entry = tk.Entry(root, width=50)
homework_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Give Date (dd/mm/yyyy):", bg="#81A594").grid(row=2, column=0, padx=10, pady=10)
date_entry = tk.Entry(root, width=50)
date_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root, text="Enter the Subject:", bg="#81A594").grid(row=3, column=0, padx=10, pady=10)
subject_entry = tk.Entry(root, width=50)
subject_entry.grid(row=3, column=1, padx=10, pady=10)

button_frame = tk.Frame(root, bg="#81A594")
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="#d1e7dd")
add_button.pack(side=tk.LEFT, padx=10)

update_button = tk.Button(button_frame, text="Update Task", command=update_task, bg="#fce5cd")
update_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg="#f8d7da")
delete_button.pack(side=tk.LEFT, padx=10)

task_listbox = tk.Listbox(root, width=110, height=15, bg="#ffffff")
task_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

load_tasks()

root.mainloop()

conn.close()

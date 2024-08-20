import tkinter as tk

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=18, font=('Arial', 24), borderwidth=2, relief="solid", justify='right', bg="#d3d3d3", fg="#000000")
entry.grid(row=0, column=0, columnspan=4)

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

buttons = [
    ('C', 1, 0, '#6666ff'), ('=', 1, 1, '#6666ff'), ('%', 1, 2, '#6666ff'), ('/', 1, 3, '#6666ff'),
    ('7', 2, 0, '#d3d3d3'), ('8', 2, 1, '#d3d3d3'), ('9', 2, 2, '#d3d3d3'), ('*', 2, 3, '#6666ff'),
    ('4', 3, 0, '#d3d3d3'), ('5', 3, 1, '#d3d3d3'), ('6', 3, 2, '#d3d3d3'), ('-', 3, 3, '#6666ff'),
    ('1', 4, 0, '#d3d3d3'), ('2', 4, 1, '#d3d3d3'), ('3', 4, 2, '#d3d3d3'), ('+', 4, 3, '#6666ff'),
    ('0', 5, 0, '#d3d3d3'), ('.', 5, 1, '#d3d3d3'),
]

for (text, row, col, color) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=40, pady=20, font=('Arial', 18), bg=color, command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=40, pady=20, font=('Arial', 18), bg=color, command=clear)
    else:
        button = tk.Button(root, text=text, padx=40, pady=20, font=('Arial', 18), bg=color, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)
root.mainloop()

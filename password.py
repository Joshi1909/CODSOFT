import tkinter as tk
import random
import string

def generate_password():
    length = 1
    all_characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(all_characters) for i in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)



window = tk.Tk()
window.title("Password Generator")
window.geometry("400x150")
window.configure(bg='#f0f0f0')


password_entry = tk.Entry(window, width=30, font=("Arial", 14), bg="#ffffff", fg="#000000")
password_entry.pack(pady=20)

generate_button = tk.Button(window, text="Generate Password", command=generate_password, 
                            font=("Arial", 12), bg="#4CAF50", fg="#ffffff", activebackground="#45a049")
generate_button.pack(pady=10)


window.mainloop()

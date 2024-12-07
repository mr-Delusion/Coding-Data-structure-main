import tkinter as tk
import random
import string
def generate_password():
    length = int(entry_length.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
root = tk.Tk()
root.title("Password Generator")
label_length = tk.Label(root, text="Password Length:")
label_length.pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)
entry_length.insert(0, "12") 
btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.pack(pady=10)
entry_password = tk.Entry(root, width=40)
entry_password.pack(pady=5)

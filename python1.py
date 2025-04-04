import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)
    
    if length < 6:
        strength = "Weak"
    elif length <= 10:
        strength = "Medium"
    else:
        strength = "Strong"
    
    result_label.config(text=f"Password Strength: {strength}")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("300x200")


tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)


check_button = tk.Button(root, text="Check Strength", command=check_strength)
check_button.pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=5)


root.mainloop()
import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    password = entry.get()
    strength = "Weak"
    
    if len(password) >= 8:
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"\d", password) and re.search(r"[@$!%*?&]", password):
            strength = "Strong"
        elif re.search(r"[A-Za-z]", password) and re.search(r"\d", password):
            strength = "Medium"
    
    label_result.config(text=f"Strength: {strength}", fg=("green" if strength == "Strong" else "orange" if strength == "Medium" else "red"))

def clear_input():
    entry.delete(0, tk.END)
    label_result.config(text="")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.configure(bg="#F64A8A")

label = tk.Label(root, text="Enter Password:", font=("Arial", 14), bg="#F64A8A", fg="white")
label.pack(pady=10)

entry = tk.Entry(root, width=30, show="*", font=("Arial", 12))
entry.pack(pady=5)

check_button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 12), bg="white", fg="#F64A8A")
check_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_input, font=("Arial", 12), bg="white", fg="#F64A8A")
clear_button.pack(pady=5)

label_result = tk.Label(root, text="", font=("Arial", 14), bg="#F64A8A", fg="white")
label_result.pack(pady=10)

root.mainloop()

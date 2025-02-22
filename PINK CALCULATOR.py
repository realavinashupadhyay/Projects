import tkinter as tk
from tkinter import font

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)

root = tk.Tk()
root.title("Pink Calculator")
root.geometry("350x500")
root.configure(bg="#FCE4EC")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font=("Arial", 20), bd=10, relief=tk.FLAT, justify="right", bg="#FFD1DC")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons_frame = tk.Frame(root, bg="#FCE4EC")
buttons_frame.pack()

buttons = [
    ["C", "(", ")", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", "√"],
    ["sin", "cos", "tan", "log"]
]

for row in buttons:
    frame = tk.Frame(buttons_frame, bg="#FCE4EC")
    frame.pack(expand=True, fill=tk.BOTH)
    for btn_text in row:
        btn = tk.Button(
            frame, text=btn_text, font=("Arial", 16, "bold"), width=5, height=2, 
            bg="#FFB6C1", fg="white", relief=tk.FLAT, bd=5, activebackground="#FF91A4"
        )
        btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()

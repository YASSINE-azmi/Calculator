# Calculator module Version 0.0.2
# Copyright (c) 2025 Z_yx2
# Licensed under the MIT License

import tkinter as tk
from tkinter import scrolledtext


# Colors
 
color_black = "#1C1C1C"
color_white = "#FFFFFF"
color_orange = "#FF9500"
color_dark_gray = "#3C3C3C"
color_light_gray = "#AAAAAA"

 
# Button values
 
button_values = [
    ['7', '8', '9', '÷', 'C'],
    ['4', '5', '6', '*', '('],
    ['1', '2', '3', '-', ')'],
    ['0', '.', '=', '+', 'CE']
]

 
# Root window
 
root = tk.Tk()
root.title("Calculator")
root.configure(bg=color_black)

 
# Display
 
main_frame = tk.Frame(root, bg=color_black)
main_frame.pack(padx=10, pady=10)
left_frame = tk.Frame(main_frame, bg=color_black)
left_frame.pack(side=tk.LEFT)
display = tk.Label(left_frame, text="0", font=("Arial", 32), bg=color_black, fg=color_white, anchor="e", padx=10)
display.pack(fill=tk.X, pady=10)
 
# Frame for buttons
 
button_frame = tk.Frame(root, bg=color_black)
button_frame.pack()

 
# History Box

button_frame = tk.Frame(left_frame, bg=color_black)
button_frame.pack()


def add_to_history(text):
    history_box.config(state="normal")
    history_box.insert(tk.END, text + "\n")
    history_box.config(state="disabled")
    history_box.yview(tk.END)

def clear_history():
    history_box.config(state="normal")
    history_box.delete('1.0', tk.END)
    history_box.config(state="disabled")



right_frame = tk.Frame(main_frame, bg=color_black)
right_frame.pack(side=tk.LEFT, padx=10)

history_box = scrolledtext.ScrolledText(right_frame, width=30, height=20, state="disabled", font=("Arial", 12),bg=color_black, fg=color_white)
history_box.pack()

clear_history_button = tk.Button(right_frame, text="Clear History", command=clear_history, bg=color_dark_gray, fg=color_white)
clear_history_button.pack(pady=5)


 
# Functionality
 
expression = ""

def press(value):
    global expression
    if value == "C":  # clear all
        expression = ""
        display.config(text="0")
    elif value == "CE":  # clear last
        expression = expression[:-1]
        display.config(text=expression if expression else "0")
    elif value == "=":  # evaluate
        try:
            expr = expression.replace("÷", "/")
            result = str(eval(expr))
            display.config(text=result)
            add_to_history(expression + " = " + result)
            expression = result
        except:
            display.config(text="Error")
            add_to_history(expression + " = Error")
            expression = ""
    else:
        expression += value
        display.config(text=expression)

 
# Create buttons
 
for r, row in enumerate(button_values):
    for c, val in enumerate(row):
        btn_color = color_dark_gray
        if val in ["C", "CE", "(", ")"]:
            btn_color = color_orange
        elif val in ["+", "-", "*", "÷"]:
            btn_color = color_light_gray

        btn = tk.Button(button_frame, text=val, font=("Arial", 18), width=5, height=2,
                        bg=btn_color,
                        fg=color_white,
                        command=lambda v=val: press(v))
        btn.grid(row=r, column=c, padx=5, pady=5)


root.mainloop()

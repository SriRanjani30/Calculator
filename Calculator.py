import tkinter as tk
from tkinter import ttk
import math

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry('360x400')  # Adjusted window size for better layout

# Entry widget to display the calculation
entry = tk.Entry(root, width=32, borderwidth=5, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")

# Function to handle button clicks
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the entry widget
def button_clear():
    entry.delete(0, tk.END)

# Function to handle calculation
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to handle operator buttons
def button_operator(operator):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + operator)

# Function to handle scientific operations
def button_science(operation):
    try:
        current = eval(entry.get())
        if operation == 'sqrt':
            result = math.sqrt(current)
        elif operation == 'sin':
            result = math.sin(math.radians(current))
        elif operation == 'cos':
            result = math.cos(math.radians(current))
        elif operation == 'tan':
            result = math.tan(math.radians(current))
        elif operation == 'log':
            result = math.log10(current)
        elif operation == 'exp':
            result = math.exp(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create buttons with customized styling
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('sin', 1, 4), ('cos', 2, 4), ('tan', 3, 4),
    ('sqrt', 1, 5), ('log', 2, 5), ('exp', 3, 5),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, command=button_equal, bg='#4CAF50', fg='white', font=('Arial', 14))
    elif text in '+-*/':
        btn = tk.Button(root, text=text, command=lambda t=text: button_operator(t), bg='#FF5722', fg='white', font=('Arial', 14))
    elif text in ['sin', 'cos', 'tan', 'sqrt', 'log', 'exp']:
        btn = tk.Button(root, text=text, command=lambda t=text: button_science(t), bg='#2196F3', fg='white', font=('Arial', 14))
    else:
        btn = tk.Button(root, text=text, command=lambda t=text: button_click(t), bg='#3E3E3E', fg='white', font=('Arial', 14))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Clear button with distinct color
btn_clear = tk.Button(root, text='C', command=button_clear, bg='#f44336', fg='white', font=('Arial', 14))
btn_clear.grid(row=4, column=5, padx=5, pady=5, sticky="nsew")

# Configure rows and columns to be resizable
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(6):
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()

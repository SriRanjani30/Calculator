import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display the calculation
entry = tk.Entry(root, width=16, borderwidth=5, font=('Arial', 24))
entry.grid(row=0, column=0, columnspan=4)

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

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=40, pady=20, command=button_equal)
    elif text in '+-*/':
        btn = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_operator(t))
    else:
        btn = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

# Clear button
btn_clear = tk.Button(root, text='C', padx=40, pady=20, command=button_clear)
btn_clear.grid(row=4, column=2)

# Run the application
root.mainloop()

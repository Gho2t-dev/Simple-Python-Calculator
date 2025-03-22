import functions as f
import tkinter as tk

# create a base window
root = tk.Tk()
root.title(" Fabian's Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Additional function buttons
extra_functions = [
    ('x²', lambda: button_func(f.square)),
    ('√x', lambda: button_func(f.sqrt)),
    ('1/x', lambda: button_func(f.reciprocal)),
    ('x!', lambda: button_func(f.factorial)),
    ('abs', lambda: button_func(f.absolute)),
    ('log', lambda: button_func(f.log)),
    ('log10', lambda: button_func(f.log10)),
    ('e^x', lambda: button_func(f.exp)),
    ('sin', lambda: button_func(f.sin)),
    ('cos', lambda: button_func(f.cos)),
    ('tan', lambda: button_func(f.tan)),
    ('deg', lambda: button_func(f.degrees)),
    ('rad', lambda: button_func(f.radians)),
]

extra_row = 1
extra_col = 0
for label, cmd in extra_functions:
    tk.Button(root, text=label, padx=20, pady=20, command=cmd).grid(row=extra_row, column=extra_col)
    extra_col += 1
    if extra_col > 3:
        extra_col = 0
        extra_row += 1

row, col = extra_row + 1, 0
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_func(func):
    try:
        value = float(entry.get())
        result = func(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
for btn in buttons:
    if btn == '=':
        command = button_equal
    elif btn == 'C':
        command = button_clear
    else:
        command = lambda val=btn: button_click(val)

    tk.Button(root, text=btn, padx=20, pady=20, command=command).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

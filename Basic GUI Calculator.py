# Basic GUI Calculator

import tkinter as tk

def on_click(event):
    current_text = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

def create_button(text, row, col, col_span=1):
    button = tk.Button(root, text=text, font=("Helvetica", 18), bd=5)
    button.grid(row=row, column=col, columnspan=col_span, padx=5, pady=5)
    button.bind("<Button-1>", on_click)  # Bind the button click event to the on_click() function
    return button

root = tk.Tk()
root.title("Calculator")
root.geometry("300x450")


heading_label = tk.Label(root, text="Calculator", font=("Helvetica", 16, "bold"),highlightcolor=("red"))
heading_label.grid(row=0, column=0, columnspan=4, pady=20)

entry = tk.Entry(root, font=("Helvetica", 24), bd=5, justify=tk.RIGHT)
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)


create_button("7", 2, 0)
create_button("8", 2, 1)
create_button("9", 2, 2)
create_button("/", 2, 3)

create_button("4", 3, 0)
create_button("5", 3, 1)
create_button("6", 3, 2)
create_button("*", 3, 3)

create_button("1", 4, 0)
create_button("2", 4, 1)
create_button("3", 4, 2)
create_button("-", 4, 3)

create_button("0", 5, 0)
create_button(".", 5, 1)
create_button("=", 5, 2)
create_button("+", 5, 3)

create_button("C", 6, 0, 3)

root.mainloop()

# Simple Calculator

def add(a, b):
    return a + b  

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
    if b == 0:
        print("Cannot divide by 0!")
        return None
    return a / b

# Operation functions dict  
operations = {
    1: add,
    2: subtract, 
    3: multiply,
    4: divide 
}

def calculate():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
  
    choice = input_number("Enter choice(1-4): ")

    num1 = input_number("Enter first number: ")
    num2 = input_number("Enter second number: ")

    func = operations.get(choice)
    if func:
        result = func(num1, num2)
        if result is not None:
            print(result) 
    else:
        print("Invalid operation")
   
def input_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
               
calculate()

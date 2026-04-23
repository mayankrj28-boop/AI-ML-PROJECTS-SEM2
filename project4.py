import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Smart Calculator")
root.geometry("320x450")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Expression variable
expression = ""

# Functions
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# StringVar for display
equation = tk.StringVar()

# Display Entry
entry = tk.Entry(root, textvariable=equation, font=('Arial', 20),
                 bd=10, insertwidth=2, width=14,
                 borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button Styling
btn_color = "#2d2d2d"
text_color = "white"

# Buttons Layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('%',4,2), ('+',4,3)
]

# Create buttons
for (text, row, col) in buttons:
    tk.Button(root, text=text, padx=20, pady=20,
              font=("Arial", 12),
              bg=btn_color, fg=text_color,
              command=lambda t=text: press(t)).grid(row=row, column=col)

# Special Buttons
tk.Button(root, text="C", padx=20, pady=20,
          font=("Arial", 12), bg="red", fg="white",
          command=clear).grid(row=5, column=0)

tk.Button(root, text="⌫", padx=20, pady=20,
          font=("Arial", 12), bg="orange", fg="white",
          command=backspace).grid(row=5, column=1)

tk.Button(root, text="=", padx=20, pady=20,
          font=("Arial", 12), bg="green", fg="white",
          command=equal).grid(row=5, column=2, columnspan=2, sticky="we")

# Keyboard Support
def key_input(event):
    key = event.char
    if key in "0123456789+-*/.%":
        press(key)
    elif key == "\r":
        equal()
    elif key == "\x08":
        backspace()

root.bind("<Key>", key_input)

# Run app
root.mainloop()

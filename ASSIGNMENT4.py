from tkinter import *

# Functions
def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    if float(num2.get()) != 0:
        result.set(float(num1.get()) / float(num2.get()))
    else:
        result.set("Cannot divide by zero")

# Create window
window = Tk()
window.title("GUI Calculator")
window.geometry("300x250")

# Variables
num1 = StringVar()
num2 = StringVar()
result = StringVar()

# Labels and Entry boxes
Label(window, text="First Number").pack()
Entry(window, textvariable=num1).pack()

Label(window, text="Second Number").pack()
Entry(window, textvariable=num2).pack()

# Buttons
Button(window, text="Add", command=add).pack(pady=2)
Button(window, text="Subtract", command=subtract).pack(pady=2)
Button(window, text="Multiply", command=multiply).pack(pady=2)
Button(window, text="Divide", command=divide).pack(pady=2)

# Result
Label(window, text="Result").pack()
Entry(window, textvariable=result, state="readonly").pack()

window.mainloop()
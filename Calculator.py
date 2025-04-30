import tkinter as tk  # Import the Tkinter module
from tkinter import *  # Import all Tkinter classes and constants

# Function to perform addition
def add():
    num1 = float(text1.get())  # Get the first number and convert to float
    num2 = float(text2.get())  # Get the second number and convert to float
    text3 = num1 + num2        # Calculate the sum
    result.set(f"{text3}")     # Display the result

# Function to perform subtraction
def sub():
    num1 = float(text1.get())  # Get the first number and convert to float
    num2 = float(text2.get())  # Get the second number and convert to float
    text3 = num1 - num2        # Calculate the difference
    result.set(f"{text3}")     # Display the result

# Function to perform multiplication
def mul():
    num1 = float(text1.get())  # Get the first number and convert to float
    num2 = float(text2.get())  # Get the second number and convert to float
    text3 = num1 * num2        # Calculate the product
    result.set(f"{text3}")     # Display the result

# Function to perform division
def div():
    num1 = float(text1.get())  # Get the first number and convert to float
    num2 = float(text2.get())  # Get the second number and convert to float
    text3 = num1 / num2        # Calculate the division
    result.set(f"{text3}")     # Display the result

# Function to create the main screen
def mainscreen():
    global root, text1, text2, text3, result  # Declare global variables

    # Create the main window
    root = tk.Tk()  
    root.config(bg="lightblue")           # Set background color
    root.title("Main Window")             # Set the window title
    root.geometry("300x200")              # Set the window size (width x height)

    # Title Label
    Label(text="Calculator", font=("Lato Black", 12), bg="lightblue").place(relx=0.5, y=10, anchor="n")

    # Input for first number
    Label(text="First number:", font=("Lato Black", 12), bg="lightblue").place(x=10, y=40)
    text1 = Entry(root, font="Roboto 12", bg="white", relief=GROOVE, bd=1)
    text1.place(x=135, y=40, width=150, height=25)

    # Input for second number
    Label(text="Second number:", font=("Lato Black", 12), bg="lightblue").place(x=10, y=70)
    text2 = Entry(root, font="Roboto 12", bg="white", relief=GROOVE, bd=1)
    text2.place(x=135, y=70, width=150, height=25)

    # Display the result (Read-only)
    Label(text="Result:", font=("Lato Black", 12), bg="lightblue").place(x=10, y=100)
    result = StringVar()   # Variable to store the result
    result.set("")         # Initialize the result as empty
    text3 = Entry(textvariable=result, font="Roboto 12", bg="white", relief=GROOVE, bd=1, state="readonly")
    text3.place(x=135, y=100, width=150, height=25)

    # Buttons for operations
    Button(text="ADD", height=2, width=4, bg="#39a3be", fg="white", bd=1, command=add).place(x=25, y=130)
    Button(text="SUB", height=2, width=4, bg="#39a3be", fg="white", bd=1, command=sub).place(x=85, y=130)
    Button(text="MUL", height=2, width=4, bg="#39a3be", fg="white", bd=1, command=mul).place(x=145, y=130)
    Button(text="DIV", height=2, width=4, bg="#39a3be", fg="white", bd=1, command=div).place(x=205, y=130)

    # Start the Tkinter event loop to display the window
    root.mainloop()

# Call the function to display the main screen
mainscreen()

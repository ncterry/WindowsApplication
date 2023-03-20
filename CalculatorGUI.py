'''
Yes, I can create a calculator GUI in Python using a variety of different 
libraries such as tkinter, PyQt, and wxPython. Here's an example of how 
to create a simple calculator using the tkinter library:
'''

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.display = tk.Entry(self.master, width=20, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.click(x)
            tk.Button(self.master, text=button, width=5, height=2, command=command).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, key):
        if key == "=":
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        elif key == "C":
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()

'''
This code creates a simple calculator GUI using the tkinter library. 
The Calculator class creates a window with a display and buttons for each 
of the calculator functions. The click method handles button clicks and evaluates 
expressions when the equals button is pressed. The main program creates an 
instance of the Calculator class and starts the tkinter main loop.
'''

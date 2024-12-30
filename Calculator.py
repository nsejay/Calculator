import tkinter as tk
import math


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.geometry("312x324")

        self.total = tk.StringVar()
        self.entry = tk.Entry(master, textvariable = self.total, font = "Courier")
        self.entry.grid(row = 0, column = 0, columnspan = 5, pady = 10)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
                  ["log(x)", "10^x", "1/x", "x!",'^'],
                  ["sin","cos","tan","^2","sqrt"],
                  ['7', '8', '9', '/','('],
                  ['4', '5', '6', '*',')'],
                  ['1', '2', '3', '-','='],
                  ['0', '.', 'C', '+'],
                  ]
        
        for i, button in enumerate(buttons):
            for j, keys in enumerate(button):
                key = tk.Button(self.master, text = keys, width = 3, height = 3, 
                                font = "Courier", command = lambda text = keys: self.click(text))
                key.grid(row = i+1, column = j, sticky = "nsew")
                self.master.columnconfigure(j, weight = 1)
            self.master.rowconfigure(i+1, weight = 1)        
    
    def click(self, keys):
        if self.total.get() == "Error":
            self.total.set('')
        if keys == '=':
            try:
                result = round(eval(self.entry.get()), 5)
                self.total.set(result)
            except:
                self.total.set("Error")
        elif keys == 'C':
            self.total.set('')
        elif keys == "sin":
            try:
                result = round(math.sin(math.radians(float(self.entry.get()))), 5)
                self.total.set(result)
            except:
                self.total.set("Error")
        elif keys == "cos":
            try:
                result = round(math.cos(math.radians(float(self.entry.get()))), 5)
                self.total.set(result)
            except:
                self.total.set("Error")
        elif keys == "tan":
            try:
                result = round(math.tan(math.radians(float(self.entry.get()))), 5)
                self.total.set(result)
            except:
                self.total.set("Error")
        elif keys == "sqrt":
            try:
                result = round(math.sqrt(float(self.entry.get())),5)
                self.total.set(result)
            except:
                self.total.set("Error")
        elif keys == "x!":
            try:
                result = math.factorial(int(self.entry.get()))
                self.total.set(result)
            except:
                self.total.set("Error")
        elif keys == "log(x)":
            try:
                result = round(math.log(float(self.entry.get())),5)
                self.total.set(result)
            except:
                self.total.set("Error")
        elif keys == "1/x":
            try:
                result = round(1/(float(self.entry.get())),5)
                self.total.set(result)
            except:
                self.total.set("Error")
        elif keys == "^2":
            try:
                result = round(float(self.entry.get()) ** 2, 5)
                self.total.set(result)
            except:
                self.total.set("Error")
        elif keys == '^':
                self.total.set(self.total.get() + "**")

        else:
            self.total.set(self.entry.get() + keys)

def main():
    root =tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
            
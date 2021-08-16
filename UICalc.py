import tkinter
from functools import reduce
from tkinter.constants import END, NSEW, NW


root = tkinter.Tk()
root.geometry("250x300")
class Calculator:
    clearCalc = False
    def __init__(self, master):
        master.title("Simple Calculator")
        self.entry = tkinter.Entry(master, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, pady=10) 
        self.button_1 = tkinter.Button(master, text="1", padx=25, pady=20, command=lambda: self.button_input(1)).grid(row=3, column=0, sticky=NSEW)
        self.button_2 = tkinter.Button(master, text="2", padx=25, pady=20, command=lambda: self.button_input(2)).grid(row=3, column=1, sticky=NW)
        self.button_3 = tkinter.Button(master, text="3", padx=25, pady=20, command=lambda: self.button_input(3)).grid(row=3, column=2, sticky=NW)
        self.button_4 = tkinter.Button(master, text="4", padx=25, pady=20, command=lambda: self.button_input(4)).grid(row=2, column=0, sticky=NSEW)
        self.button_5 = tkinter.Button(master, text="5", padx=25, pady=20, command=lambda: self.button_input(5)).grid(row=2, column=1, sticky=NW)
        self.button_6 = tkinter.Button(master, text="6", padx=25, pady=20, command=lambda: self.button_input(6)).grid(row=2, column=2, sticky=NW)
        self.button_7 = tkinter.Button(master, text="7", padx=25, pady=20, command=lambda: self.button_input(7)).grid(row=1, column=0, sticky=NSEW)
        self.button_8 = tkinter.Button(master, text="8", padx=25, pady=20, command=lambda: self.button_input(8)).grid(row=1, column=1, sticky=NW)
        self.button_9 = tkinter.Button(master, text="9", padx=25, pady=20, command=lambda: self.button_input(9)).grid(row=1, column=2, sticky=NSEW)
        self.button_0 = tkinter.Button(master, text="0", padx=25, pady=20, command=lambda: self.button_input(0)).grid(row=4 , column=1, sticky=NSEW)
        self.button_equal = tkinter.Button(master, text="=", padx=20, pady=20, command=lambda: self.equal_input()).grid(row=4, column=2, sticky=NSEW)
        self.button_add = tkinter.Button(master, text="+", padx=20, pady=20, command=lambda:[self.addition_input(), self.button_input("+")]).grid(row=4, column=3, sticky=NSEW)
        self.button_subtract = tkinter.Button(master, text="−", padx=20, pady=20, command=lambda:[self.subtract_input(), self.button_input("−")]).grid(row=3, column=3, sticky=NSEW)
        self.button_multiply = tkinter.Button(master, text="x", padx=20, pady=20, command=lambda:[self.multiply_input(), self.button_input("x")]).grid(row=2, column=3, sticky=NSEW)
        self.button_divide = tkinter.Button(master, text="÷", padx=20, pady=20, command=lambda:[self.divide_input(), self.button_input("÷")]).grid(row=1, column=3, sticky=NSEW)
        self.button_clear = tkinter.Button(master, text="clear", padx=15.5, pady=20, command=lambda:self.clear_input()).grid(row=4, column=0, sticky=NW)
    

    def equal_input(self):
        self.num_2 = self.entry.get()
        self.entry.delete(0, END)
        
        if self.sign == "add":
            self.answer = sum(self.total_lst)
            self.entry.insert(0, self.answer)

        if self.sign == "subtract":
            self.answer = reduce(lambda x, y: x - y, self.total_lst)
            self.entry.insert(0, self.answer)

        if self.sign == "divide":
            self.answer = reduce(lambda x, y: x / y, self.total_lst)
            self.entry.insert(0, self.answer)

        if self.sign == "multiply":
            self.answer = reduce(lambda x, y: x * y, self.total_lst)
            self.entry.insert(0, self.answer)
        
        self.clearCalc = True
        
    def clear_input(self):
        self.entry.delete(0, END)
        
    def button_input(self, number):
        if self.clearCalc:
            self.clear_input()
            self.clearCalc = False
        num = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, str(num) + str(number))
        lst_string = self.entry.get()
        lst_string = str(lst_string)
        data_lst = [lst_string[i:i+1] for i in range(0, len(lst_string), 1)]
        self.total_lst = []
        temp = [] 
        for item in data_lst:
            temp.append(item)
            if item == '+':
                temp.remove("+")
                self.total_lst.append(temp)
                temp = []
            if item == '−':
                temp.remove("−")
                self.total_lst.append(temp)
                temp = []
            if item == 'x':
                temp.remove("x")
                self.total_lst.append(temp)
                temp = []
            if item == '÷':
                temp.remove("÷")
                self.total_lst.append(temp)
                temp = []
       
        if temp:
            self.total_lst.append(temp)

        
        self.total_lst = [*map(''.join, self.total_lst)]
        self.total_lst = list(map(float, self.total_lst))
     


    def addition_input(self):
        self.sign = "add"

    def subtract_input(self):
        self.sign = "subtract"

    def multiply_input(self):
        self.sign = "multiply"

    def divide_input(self):
        self.sign = "divide"

run = Calculator(root)
root.mainloop()

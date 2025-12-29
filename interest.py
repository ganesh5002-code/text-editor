from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Interest Calculator App")
window.geometry("400x400")

principal_label = Label(window, text= "Enter your starting amount of money", bg= "#808080", fg= "black")
principal_label.grid(row= 0, column= 1, sticky= "ew", padx= 10, pady= 5)
principal_entry = Entry(window)
principal_entry.grid(row= 0, column= 3, sticky= "ew", padx= 10, pady= 5)

time_label = Label(window, text= "Enter the time in years", bg= "#808080", fg= "black")
time_label.grid(row= 1, column= 1, sticky= "ew", pady= 5, padx= 10)
time_entry = Entry(window)
time_entry.grid(row= 1, column= 3, sticky= "ew", padx= 10, pady= 5)

rate_label = Label(window, text= "Display the interest rate in percentage", bg= "#808080", fg= "black")
rate_label.grid(row= 2, column= 1, sticky= "ew", padx= 10, pady= 5)
rate_entry = Entry(window)
rate_entry.grid(row= 2, column= 3, sticky= "ew", padx= 10, pady= 5)

compounded_label = Label(window, text= "How much do you want your interest compounded in number", bg= "#808080", fg= "black")
compounded_label.grid(row= 3, column= 1, sticky= "ew", padx= 10, pady= 5)
compounded_entry = Entry(window)
compounded_entry.grid(row= 3, column= 3, sticky= "ew", padx= 10, pady= 5)

def simple_interest():
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())

    formula = (p*t*r)/100
    messagebox.showinfo("Simple Interest", f"the total simple interest amount is ${formula}")

def compound_interest():
    p = float(principal_entry.get())
    t = float(time_entry.get())
    r = float(rate_entry.get())
    n = float(compounded_entry.get())

    formula = p*(1 + r/(100*n))**(n*t)
    messagebox.showinfo("Compound Interest", f"the total compound interest amount is ${formula}")

simple_interest_button = Button(window, text= "Calculate simple interest amount", bg= "#008080", fg= "green", command= simple_interest)
simple_interest_button.grid(row=4, column=1, pady=10)
compound_interest_button = Button(window, text= "Calculate compound interest amount", bg= "#008080", fg= "green", command= compound_interest)
compound_interest_button.grid(row=4, column=3, pady=10)

window.mainloop()
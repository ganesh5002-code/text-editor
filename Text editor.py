from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("My text editor")
window.geometry("400x400")
window.rowconfigure(0, minsize= 500, weight= 1)
window.columnconfigure(1, minsize= 500, weight= 1)

def open_file():
    filepath = askopenfilename(
    filetypes= [("Text Files", "*.txt"), ("All Files", "*.*")]   
    )
    if not filepath:
        return
    text_box.delete(1.0, END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_box.insert(END, text)
        input_file.close()

    window.title(f"My Text Editor - {filepath}")

def save_file():
    filepath = asksaveasfilename(
    defaultextension= "txt",
    filetypes= [("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_box.get(1.0, END)
        output_file.write(text)
    window.title(f"My Text Editor - {filepath}")

text_box = Text(window)
button_frame = Frame(window, bg= "#808080", relief= RAISED, bd= 2)
open_button = Button(button_frame, bg= "#FEFDFD", text= "open", fg= "black", command= open_file)
save_button  = Button(button_frame, bg= "#FEFDFD", text= "Save as", fg= "black", command= save_file)

open_button.grid(row= 0, column= 0, sticky= "ew", padx= 10, pady= 10)
save_button.grid(row= 1, column= 0, sticky= "ew", padx= 10)

button_frame.grid(row= 0, column= 0, sticky= "ns")
text_box.grid(row= 0, column= 1, sticky= "nsew")

window.mainloop()

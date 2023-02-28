# Day 27: Tkinter

import tkinter

window = tkinter.Tk()
window.title("My first GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady = 200)  # padding around edges

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)  # can't used grid and pack in same code

# Button

def button_clicked():
    my_label["text"] = "I got clicked"
    new_text = input.get()


button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New button")
new_button.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
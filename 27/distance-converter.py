import tkinter

window = tkinter.Tk()
window.title("Mile to km converter")
window.config(padx=10, pady=10)

# input field
input_text = tkinter.Entry(width=10)
input_text.grid(column=1, row=0)

# miles text
miles_text = tkinter.Label(text="Miles")
miles_text.grid(column=2, row=0)

# equal to text
equal_text = tkinter.Label(text="is equal to")
equal_text.grid(column=0, row=1)

# output text
output_text = tkinter.Label(text="0")
output_text.grid(column=1, row=1)

# km text
km_text = tkinter.Label(text="km")
km_text.grid(column=2, row=1)\

# Button

def miles_to_km():
    miles = input_text.get()
    km = int(miles) * 1.609
    output_text["text"] = round(km, 1)


button = tkinter.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
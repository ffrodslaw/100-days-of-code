import tkinter as tk
from tkinter import messagebox
import random
import json
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pw():
    # list comprehension
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_pw.insert(0, password)
    window.clipboard_append(password)   # pyperclip did not work for me (Linux Fedora)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entry():
    website = entry_website.get()
    email = entry_email.get()
    pw = entry_pw.get()
    new_data = {
        website: {
            "email": email,
            "password": pw,
        }
    }

    if len(website) == 0 or len(pw) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!", icon="error")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent = 4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving new data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, "end")
            entry_pw.delete(0, "end")

def load_entry():
            website = entry_website.get()
            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
                    entry = data[website]
            except FileNotFoundError:
                messagebox.showerror(title="Oops", message="Database empty.")
            except KeyError:
                messagebox.showerror(title="Oops", message=f"Details for {website} are not in database.")
            else:
                email = entry["email"]
                pw = entry["password"]

                messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {pw}")



# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(height=200, width=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = tk.Label(text="Website:")
label_website.grid(column=0, row=1)

label_email= tk.Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_pw = tk.Label(text="Password:")
label_pw.grid(column=0, row=3)

entry_website = tk.Entry(width=21)
entry_website.grid(column=1, row=1, sticky="EW")  # sticky argument needed to line up grid nicely
entry_website.focus()

entry_email = tk.Entry(width=35)
entry_email.insert(index=0, string="mymostcommonemail@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2, sticky="EW")

entry_pw = tk.Entry(width=21)
entry_pw.grid(column=1, row=3, sticky="EW")

button_search = tk.Button(text="Search", command=load_entry)
button_search.grid(column=2, row=1, sticky="EW")

button_generate = tk.Button(text="Generate Password", command=generate_pw)
button_generate.grid(column=2, row=3, sticky="EW")

button_add = tk.Button(text="Add", width=36, command=save_entry)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()

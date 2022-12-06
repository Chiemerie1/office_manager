from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import os



helvetica = "Helvetica"

console = CTkToplevel()
console.geometry("900x700")
console.title("Admin Console")

PATH = os.path.dirname(os.path.realpath(__file__))

##### Title #####
title_frame = CTkFrame(
    console,
    height=5,
)
title_frame.grid(row=0, column=0, padx=10, pady=10, sticky="news", columnspan=2)

title = CTkLabel(
    title_frame,
    text="Admin Console",
    text_font=(helvetica, 14)
)
title.pack(pady=5)

##### Title #####

##### Tab frame #####
tab_frame = CTkFrame(
    console,
    height=600
)
tab_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsw")

employees = CTkButton(
    tab_frame,
    text="Employees",
    text_font=(helvetica, 12, "bold"),
    fg_color=("#d1d5d8", "#2a2d2e"),
    text_color=("#2a2d2e", "#d1d5d8"),
    hover_color="brown",
    command=lambda:raise_frame(employees_main)
)
employees.pack(padx=10, pady=10)

inventory = CTkButton(
    tab_frame,
    text="Inventory",
    text_font=(helvetica, 12, "bold"),
    fg_color=("#d1d5d8", "#2a2d2e"),
    text_color=("#2a2d2e", "#d1d5d8"),
    hover_color="brown",
    command=lambda:raise_frame(inventory_main)
)
inventory.pack(padx=10, pady=10)

settings = CTkButton(
    tab_frame,
    text="Settings",
    text_font=(helvetica, 12, "bold"),
    fg_color=("#d1d5d8", "#2a2d2e"),
    text_color=("#2a2d2e", "#d1d5d8"),
    hover_color="brown",
    command=lambda:raise_frame(settings_main)
)
settings.pack(padx=10, pady=10)

##### Tab frame #####

employees_main = CTkFrame(
    console
)
inventory_main = CTkFrame(
    console
)
settings_main = CTkFrame(
    console
)

for main_frame in (employees_main, inventory_main, settings_main):
    main_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")


##### Employees frame #####
first_name = CTkEntry(
    employees_main,
    placeholder_text="First name",
    text_font=(helvetica, 10),
    height=35
)
first_name.grid(row=0, column=0, padx=10, pady=10, sticky="news")

Last_name = CTkEntry(
    employees_main,
    placeholder_text="Last name",
    text_font=(helvetica, 10),
    height=35
)
Last_name.grid(row=1, column=0, padx=10, pady=10, sticky="news")

username = CTkEntry(
    employees_main,
    placeholder_text="Username",
    text_font=(helvetica, 10),
    height=35
)
username.grid(row=2, column=0, padx=10, pady=10, sticky="news")

email = CTkEntry(
    employees_main,
    placeholder_text="Email",
    text_font=(helvetica, 10),
    height=35
)
email.grid(row=3, column=0, padx=10, pady=10, sticky="news")

phone = CTkEntry(
    employees_main,
    placeholder_text="Phone no",
    text_font=(helvetica, 10),
    height=35
)
phone.grid(row=4, column=0, padx=10, pady=10, sticky="news")

designation = CTkEntry(
    employees_main,
    placeholder_text="Designation",
    text_font=(helvetica, 10),
    height=35
)
designation.grid(row=5, column=0, padx=10, pady=10, sticky="news")

password = CTkEntry(
    employees_main,
    placeholder_text="Password",
    text_font=(helvetica, 10),
    height=35
)
password.grid(row=6, column=0, padx=10, pady=10, sticky="news")

save = CTkButton(
    employees_main,
    fg_color='brown',
    text="Save",
    text_font=(helvetica, 12, "bold"),
    hover_color="gray",
    height=35,
    relief=RAISED
)
save.grid(row=7, column=0, padx=10, pady=10, sticky="news")

employee_info = Listbox(
    employees_main,
    activestyle="underline",
    bg="gray25",
    highlightcolor="brown",
    selectbackground="brown",
    takefocus=TRUE,
    yscrollcommand=YES,
    font=(helvetica, 12)
)
employee_info.grid(row=8, column=0, padx=10, pady=10, ipadx=10, sticky="news")


names = ["one", "two", "three", "four"]
for num in names:
    employee_info.insert(END, num)
##### Employees frame #####


def raise_frame(main_frame):
    main_frame.tkraise()

raise_frame(employees_main)


##### grid Configurations #####
console.columnconfigure(0, weight=1)
console.columnconfigure(1, weight=6)

console.rowconfigure(1, weight=1)

employees_main.columnconfigure(0, weight=1)

employees_main.rowconfigure(8, weight=1)




console.mainloop()
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
)
employees.pack(padx=10, pady=10)

inventory = CTkButton(
    tab_frame,
    text="Inventory",
    text_font=(helvetica, 12, "bold"),
    fg_color=("#d1d5d8", "#2a2d2e"),
    text_color=("#2a2d2e", "#d1d5d8"),
    hover_color="brown"
)
inventory.pack(padx=10, pady=10)

settings = CTkButton(
    tab_frame,
    text="Settings",
    text_font=(helvetica, 12, "bold"),
    fg_color=("#d1d5d8", "#2a2d2e"),
    text_color=("#2a2d2e", "#d1d5d8"),
    hover_color="brown"
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
name = CTkEntry(
    employees_main,
    placeholder_text="Name",
    corner_radius=10,
    text_font=(helvetica, 10),
    width=400,
    height=35
)
name.grid(row=0, column=0, padx=10, pady=10, sticky="news")

##### Employees frame #####


def raise_frame(main_frame):
    main_frame.tkraise()

raise_frame(employees_main)


##### grid Configurations #####
console.columnconfigure(0, weight=1)
console.columnconfigure(1, weight=6)

console.rowconfigure(1, weight=1)

console.mainloop()
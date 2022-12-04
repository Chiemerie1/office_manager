from tkinter import *
import customtkinter as ct

from PIL import ImageTk, Image

import os

PATH = os.path.dirname(os.path.realpath(__file__))

create = ct.CTkToplevel()
create.geometry("900x700")
create.title("Create office")



basic_font = "comic Sans Ms"



create_office = ct.CTkLabel(
    create,
    text="Create Office",
    text_font=(basic_font, 14)
)
create_office.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame_1 = ct.CTkFrame(
    create,
    fg_color="gray",
    corner_radius=20,
    border_color="brown",
    border_width=2,
)
frame_1.grid(row=1, column=0, padx=10, pady=10)

First_name = ct.CTkEntry(
    frame_1,
    placeholder_text="First name",
    corner_radius=10,
    height=32,
    width=500
)
First_name.pack(padx=10, pady=10)

Last_name = ct.CTkEntry(
    frame_1,
    placeholder_text="Last name",
    corner_radius=10,
    height=35,
    width=500
)
Last_name.pack(padx=10, pady=10)

username = ct.CTkEntry(
    frame_1,
    placeholder_text="username",
    corner_radius=10,
    height=35,
    width=500
)
username.pack(padx=10, pady=10)

business_name = ct.CTkEntry(
    frame_1,
    placeholder_text="business name",
    corner_radius=10,
    width=500,
    height=35
)
business_name.pack(padx=10, pady=10)

password = ct.CTkEntry(
    frame_1,
    placeholder_text="password",
    corner_radius=10,
    width=500,
    height=35
)
password.pack(padx=10, pady=10)

confirm_password = ct.CTkEntry(
    frame_1,
    placeholder_text="Confirm password",
    corner_radius=10,
    width=500,
    height=35
)
confirm_password.pack(padx=10, pady=10)

create_btn = ct.CTkButton(
    frame_1,
    fg_color="brown",
    text="Create office",
    text_font=(basic_font, 10),
    corner_radius=10,
    width=500,
    height=35
)
create_btn.pack(padx=10, pady=10)

back_btn = ct.CTkButton(
    create,
    fg_color=("brown","gray"),
    text="Go back",
    text_font=(basic_font, 10),
    corner_radius=10,
    width=500,
    height=35
)
back_btn.grid(row=2, column=0, padx=10, pady=10)






##### Configurations #####

create.rowconfigure(1, weight=1)
create.rowconfigure(2, weight=1)

create.columnconfigure(0, weight=1)



create.mainloop()
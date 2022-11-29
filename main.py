from tkinter import *
import customtkinter as ct
root = ct.CTk()
root.geometry("900x700")
root.title("Office Manager")

from PIL import ImageTk, Image

import os

PATH = os.path.dirname(os.path.realpath(__file__))

basic_font = "comic Sans Ms"



office_manager = ct.CTkLabel(
    text="Office Manager",
    text_font=(basic_font, 14),
)
office_manager.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

login_frame = ct.CTkFrame(
    fg_color="gray",
    border_color="green",
    corner_radius=20,
)
login_frame.grid(row=1, column=0, padx=10, pady=10)

app_icon = Image.open(PATH + "\img\pyicon.png")
app_icon = ImageTk.PhotoImage(app_icon)

logo = Label(
    login_frame,
    image=app_icon,
    bg="gray"
)
logo.pack(padx=10, pady=10)

username = ct.CTkEntry(
    login_frame,
    placeholder_text="Username",
    corner_radius=10,
    text_font=(basic_font, 10),
    width=250,
    height=35
)
username.pack(padx=10, pady=10)

password = ct.CTkEntry(
    login_frame,
    placeholder_text="password",
    corner_radius=10,
    text_font=(basic_font, 10),
    width=250,
    height=35
)
password.pack(padx=10, pady=10)

login_icon = Image.open(PATH + "\img\enter.png").resize((28,28))
login_icon = ImageTk.PhotoImage(login_icon)

login_btn = ct.CTkButton(
    login_frame,
    fg_color="brown",
    text="Login",
    text_font=(basic_font, 10),
    corner_radius=10,
    width=250,
    height=35,
    image=login_icon
)
login_btn.pack(padx=10, pady=10)

create_manager = ct.CTkLabel(
    root,
    text="Create your manager",
    text_font=(basic_font, 12)
)
create_manager.grid(row=2, column=0, padx=10, pady=10)




##### Configurations #####

root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

root.columnconfigure(0, weight=1)

root.mainloop()
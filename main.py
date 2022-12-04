from tkinter import *
import customtkinter as ct


root = ct.CTk()
root.geometry("900x700")
root.title("Office Manager")

from PIL import ImageTk, Image

import os

PATH = os.path.dirname(os.path.realpath(__file__))

basic_font = "comic Sans Ms"


login_window = ct.CTkFrame(root)
create_window = ct.CTkFrame(root)

for frame in (login_window, create_window):
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)



login_frame = ct.CTkFrame(
    login_window,
    fg_color="gray",
    border_color="brown",
    corner_radius=20,
    border_width=2
)
login_frame.pack(padx=10, pady=100)

office_manager = ct.CTkLabel(
    login_frame,
    text="Office Manager",
    text_font=(basic_font, 14),
)
office_manager.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

app_icon = Image.open(PATH + "\img\pyicon.png")
app_icon = ImageTk.PhotoImage(app_icon)

logo = Label(
    login_frame,
    image=app_icon,
    bg="gray"
)
logo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

username = ct.CTkEntry(
    login_frame,
    placeholder_text="Username",
    corner_radius=10,
    text_font=(basic_font, 10),
    width=500,
    height=35
)
username.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

password = ct.CTkEntry(
    login_frame,
    placeholder_text="password",
    corner_radius=10,
    text_font=(basic_font, 10),
    width=500,
    height=35
)
password.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

login_icon = Image.open(PATH + "\img\enter.png").resize((28,28))
login_icon = ImageTk.PhotoImage(login_icon)

login_btn = ct.CTkButton(
    login_frame,
    fg_color="brown",
    text="Login",
    text_font=(basic_font, 10),
    corner_radius=10,
    width=500,
    height=35,
    image=login_icon
)
login_btn.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

create_manager = ct.CTkButton(
    login_frame,
    text="Create your manager",
    text_font=(basic_font, 12),
    fg_color="gray",
    width=500,
    command=lambda:raise_frame(create_window)
)
create_manager.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")


##### Create ######

frame_1 = ct.CTkFrame(
    create_window,
    fg_color="gray",
    corner_radius=20,
    border_color="brown",
    border_width=2,
)
frame_1.pack(padx=10, pady=100)

create_office = ct.CTkLabel(
    frame_1,
    text="Create Office",
    text_font=(basic_font, 14)
)
create_office.pack(padx=10, pady=10)


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
    frame_1,
    fg_color=("brown","gray"),
    text="Go back",
    text_font=(basic_font, 10),
    corner_radius=10,
    width=500,
    height=35,
    command=lambda:raise_frame(login_window)
)
back_btn.pack(padx=10, pady=10)



##### Functions #####
def raise_frame(frame):
    frame.tkraise()




##### Configurations #####

root.rowconfigure(0, weight=1)

root.columnconfigure(0, weight=1)




raise_frame(login_window)


root.mainloop()
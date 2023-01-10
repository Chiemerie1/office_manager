from tkinter import *
import customtkinter as ct
from PIL import ImageTk, Image
import os
from pymongo import MongoClient


db_client = MongoClient("mongodb://localhost:27017/")
db = db_client["office_manager"]
create_manager = db["manager"]



root = ct.CTk()
root.geometry("900x700")
root.title("Office Manager")

PATH = os.path.dirname(os.path.realpath(__file__))

basic_font = "comic Sans Ms"

##### fn #####
def save_manager():

    manager_info_dict = {}

    manager_info = [first_name.get(), last_name.get(), username.get(), business_name.get(), password.get(),
                    confirm_password.get()
                    ]

    for x in range(len(manager_info)):
        if manager_info[x] != "":
            manager_info_dict.update({
                "First_name": manager_info[0],
                "Last_name": manager_info[1],
                "username": manager_info[2],
                "business_name": manager_info[3],
                "password": manager_info[4],
                "confirm_password": manager_info[5]
            })
    if manager_info_dict["password"] != manager_info_dict["confirm_password"]:
        create_btn.configure(text="passwords do not match")
    elif manager_info_dict["password"] == manager_info_dict["confirm_password"]:
        manager = create_manager.insert_one(manager_info_dict)
        create_btn.configure(text="Office creation successful", fg_color="green")

    first_name.delete(0, END),
    last_name.delete(0, END),
    username.delete(0, END),
    business_name.delete(0, END),
    password.delete(0, END),
    confirm_password.delete(0, END)



###### log in and account creating frame #####
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


##### switching to account creating frame #####
create_account = ct.CTkButton(
    login_frame,
    text="Create your office",
    text_font=(basic_font, 12),
    fg_color="gray",
    width=500,
    command=lambda:raise_frame(create_window)
)
create_account.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")




##### account creating frame ######
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


first_name = ct.CTkEntry(
    frame_1,
    placeholder_text="First name",
    corner_radius=10,
    height=32,
    width=500
)
first_name.pack(padx=10, pady=10)

last_name = ct.CTkEntry(
    frame_1,
    placeholder_text="Last name",
    corner_radius=10,
    height=35,
    width=500
)
last_name.pack(padx=10, pady=10)

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
    height=35,
    command=save_manager
)
create_btn.pack(padx=10, pady=10)


##### Swithiching to login frame #####
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
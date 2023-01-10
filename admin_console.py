from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import os

from pymongo import MongoClient

db_client = MongoClient("mongodb://localhost:27017/")
db = db_client["office_manager"]
employee_table = db["employee"]




helvetica = "Helvetica"

console = CTkToplevel()
console.geometry("1000x800")
console.title("Admin Console")


PATH = os.path.dirname(os.path.realpath(__file__))



#### Functions ####
#### Saving to DB ####
def db_save():
    employee_info = [
        first_name.get(),
        last_name.get(),
        username.get(),
        email.get(),
        phone.get(),
        designation.get(),
        password.get()
    ]
    for x in range(len(employee_info)):
        if employee_info[x] != "":
            emp_dict = {
            "first_name": employee_info[0],
            "last_name": employee_info[1],
            "username": employee_info[2],
            "email": employee_info[3],
            "phone no": employee_info[4],
            "desg": employee_info[5],
            "password": employee_info[6]
            }

    employee = employee_table.insert_one(emp_dict)

    first_name.delete(0, END)
    last_name.delete(0, END),
    username.delete(0, END),
    email.delete(0, END),
    phone.delete(0, END),
    designation.delete(0, END),
    password.delete(0, END)

    clear_list()
    show_info()


##### deleting from DB #####
def db_delete():
    for d in employee_info.curselection():
        first_name = {"first_name": employee_info.get(d)}
    delete = employee_table.delete_one(first_name)
    clear_list()
    show_info()


#### Viewing employee details ###
def view_employee_details():
    for name in employee_info.curselection():
        name = employee_info.get(name)
        name_dict = {"first_name": name}
        view = employee_table.find_one(name_dict)
    emp_name_view.configure(text=view["first_name"] +"  "+ view["last_name"])
    emp_username_view.configure(text=view["username"])
    emp_email_view.configure(text=view["email"])
    emp_phone_view.configure(text=view["phone no"])
    emp_desg_view.configure(text=view["desg"])
    emp_password_view.configure(text=view["password"])
    





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

###### Switching Tabs ########
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
###### Switching Tabs ########


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
##### Tab frame #####


##### Employees frame #####

frame1 = CTkFrame(
    employees_main,
)
frame1.grid(row=0, column=0, padx=10, pady=10, sticky="news")

frame1.columnconfigure(0, weight=1)

first_name = CTkEntry(
    frame1,
    placeholder_text="First name",
    text_font=(helvetica, 10),
    height=35,
    width=300
)
first_name.grid(row=0, column=0, padx=40, pady=5, sticky="news")

last_name = CTkEntry(
    frame1,
    placeholder_text="Last name",
    text_font=(helvetica, 10),
    height=35,
    width=300
)
last_name.grid(row=1, column=0, padx=40, pady=5, sticky="news")

username = CTkEntry(
    frame1,
    placeholder_text="Username",
    text_font=(helvetica, 10),
    height=35,
    width=300
)
username.grid(row=2, column=0, padx=40, pady=5, sticky="news")

email = CTkEntry(
    frame1,
    placeholder_text="Email",
    text_font=(helvetica, 10),
    height=35,
    width=300
)
email.grid(row=3, column=0, padx=40, pady=5, sticky="news")

phone = CTkEntry(
    frame1,
    placeholder_text="Phone no",
    text_font=(helvetica, 10),
    height=35,
    width=300
)
phone.grid(row=4, column=0, padx=40, pady=5, sticky="news")

designation = CTkEntry(
    frame1,
    placeholder_text="Designation",
    text_font=(helvetica, 10),
    height=35,
    width=300
)
designation.grid(row=5, column=0, padx=40, pady=5, sticky="news")

password = CTkEntry(
    frame1,
    placeholder_text="Password",
    text_font=(helvetica, 10),
    height=35,
    width=300
)
password.grid(row=6, column=0, padx=40, pady=5, sticky="news")

save = CTkButton(
    frame1,
    fg_color='brown',
    text="Save",
    text_font=(helvetica, 12, "bold"),
    hover_color="gray",
    height=35,
    relief=RAISED,
    command=db_save
)
save.grid(row=7, column=0, padx=40, pady=5, sticky="news")


employee_info = Listbox(
    employees_main,
    activestyle="underline",
    bg="gray25",
    highlightcolor="brown",
    selectbackground="brown",
    takefocus=TRUE,
    yscrollcommand=YES,
    font=(helvetica, 12),
    fg="white"
)
employee_info.grid(row=1, column=0, padx=10, pady=10, ipadx=10, sticky="news")

##### Displaying info on list box #####

def clear_list():
    employee_info.delete(0, END)

def show_info():
    for d in employee_table.find():
        employee_info.insert(END, d["first_name"])
show_info()

   

##### Actions #####

actions = CTkFrame(
    employees_main,
)
actions.grid(row=0, column=1, padx=10, pady=10, sticky="news")

edit_btn = CTkButton(
    actions,
    fg_color='gray',
    text="Edit",
    text_font=(helvetica, 12, "bold"),
    hover_color="brown",
    height=35,
    width=300,
    relief=RAISED
)
edit_btn.grid(row=0, column=0, padx=40, pady=5, sticky="news")

delete_btn = CTkButton(
    actions,
    fg_color='gray',
    text="Delete",
    text_font=(helvetica, 12, "bold"),
    hover_color="brown",
    height=35,
    width=300,
    relief=RAISED,
    command=db_delete
)
delete_btn.grid(row=1, column=0, padx=40, pady=5, sticky="news")

freeze_btn = CTkButton(
    actions,
    fg_color='gray',
    text="Freeze",
    text_font=(helvetica, 12, "bold"),
    hover_color="brown",
    height=35,
    width=300,
    relief=RAISED
)
freeze_btn.grid(row=2, column=0, padx=40, pady=5, sticky="news")

view_btn = CTkButton(
    actions,
    fg_color='gray',
    text="View",
    text_font=(helvetica, 12, "bold"),
    hover_color="brown",
    height=35,
    width=300,
    relief=RAISED,
    command=view_employee_details
)
view_btn.grid(row=3, column=0, padx=40, pady=5, sticky="news")



actions.columnconfigure(0, weight=1)

##### Actions #####

##### Employee Information #####
benefits_frame = CTkFrame(
    employees_main,
)
benefits_frame.grid(row=1, column=1, padx=10, pady=10, sticky="news")

benefits_title = CTkLabel(
    benefits_frame,
    text="Employee Info",
    text_font=(helvetica, 12, "bold"),
)
benefits_title.grid(row=0, column=0, padx=10, pady=5, columnspan=2)


emp_name = CTkLabel(
    benefits_frame,
    text="name:",
    text_font=(helvetica, 12),
    anchor="e",

)
emp_name.grid(row=1, column=0, padx=10, pady=5, sticky="w")

emp_name_view = CTkLabel(
    benefits_frame,
    text="name",
    text_font=(helvetica, 12),
    anchor="w",
)
emp_name_view.grid(row=1, column=1, padx=10, pady=5, sticky="w")



emp_username = CTkLabel(
    benefits_frame,
    text="username:",
    text_font=(helvetica, 12),
    anchor="e"

)
emp_username.grid(row=2, column=0, padx=10, pady=5, sticky="w")


emp_username_view = CTkLabel(
    benefits_frame,
    text="username",
    text_font=(helvetica, 12),
    anchor="w"

)
emp_username_view.grid(row=2, column=1, padx=10, pady=5, sticky="w")


emp_email = CTkLabel(
    benefits_frame,
    text="email:",
    text_font=(helvetica, 12),
    anchor="e"

)
emp_email.grid(row=3, column=0, padx=10, pady=5, sticky="w")

emp_email_view = CTkLabel(
    benefits_frame,
    text="email",
    text_font=(helvetica, 12),
    anchor="w"

)
emp_email_view.grid(row=3, column=1, padx=10, pady=5, sticky="w")


emp_phone = CTkLabel(
    benefits_frame,
    text="phone no:",
    text_font=(helvetica, 12),
    anchor="e"

)
emp_phone.grid(row=4, column=0, padx=10, pady=5, sticky="w")

emp_phone_view = CTkLabel(
    benefits_frame,
    text="phone no",
    text_font=(helvetica, 12),
    anchor="w"

)
emp_phone_view.grid(row=4, column=1, padx=10, pady=5, sticky="w")


emp_desg = CTkLabel(
    benefits_frame,
    text="designation:",
    text_font=(helvetica, 12),
    anchor="e"

)
emp_desg.grid(row=5, column=0, padx=10, pady=5, sticky="w")

emp_desg_view = CTkLabel(
    benefits_frame,
    text="designation",
    text_font=(helvetica, 12),
    anchor="w"

)
emp_desg_view.grid(row=5, column=1, padx=10, pady=5, sticky="w")


emp_password = CTkLabel(
    benefits_frame,
    text="password:",
    text_font=(helvetica, 12),
    anchor="e"

)
emp_password.grid(row=6, column=0, padx=10, pady=5, sticky="w")

emp_password_view = CTkLabel(
    benefits_frame,
    text="password",
    text_font=(helvetica, 12),
    anchor="w"

)
emp_password_view.grid(row=6, column=1, padx=10, pady=5, sticky="w")
##### employee information #####



##### Employees frame #####


def raise_frame(main_frame):
    main_frame.tkraise()

raise_frame(employees_main)


##### grid Configurations #####

##### console #####
console.columnconfigure(0, weight=1)
console.columnconfigure(1, weight=5)

console.rowconfigure(1, weight=1)
##### console #####

##### Employee main #####
employees_main.columnconfigure(0, weight=1)
employees_main.columnconfigure(1, weight=1)


employees_main.rowconfigure(0, weight=1)
employees_main.rowconfigure(1, weight=5)
##### Employee main #####

####### emplyee information configure #######
benefits_frame.columnconfigure(0, weight=1)
benefits_frame.columnconfigure(1, weight=2)
####### emplyee column configure #######

##### grid Configurations #####



console.mainloop()



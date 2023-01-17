from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
import os

from pymongo import MongoClient

db_client = MongoClient("mongodb://localhost:27017/")
db = db_client["office_manager"]
employee_table = db["employee"]
category = db["category"]
items = db["items"]


new_dark = "#202529"
btn_dark = "#475e69"
btn_light = "#b5bfcb"

helvetica = "Helvetica"

def admin():

    console = CTkToplevel()
    console.geometry("1000x800")
    console.title("Admin Console")
    console.configure(bg=new_dark)


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
        fg_color=new_dark
    )
    title_frame.grid(row=0, column=0, padx=10, pady=10, sticky="news", columnspan=2)

    title = CTkLabel(
        title_frame,
        text="Admin Console",
        text_font=(helvetica, 14),
        fg_color=new_dark
    )
    title.pack(pady=5)

    ##### Title #####

    ##### Tab frame #####
    tab_frame = CTkFrame(
        console,
        height=600,
        fg_color=new_dark
    )
    tab_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsw")

    ###### Switching Tabs ########
    employees = CTkButton(
        tab_frame,
        text="Employees",
        text_font=(helvetica, 12, "bold"),
        fg_color=new_dark,
        text_color=("#2a2d2e", "#d1d5d8"),
        hover_color=btn_dark,
        command=lambda:raise_frame(employees_main)
    )
    employees.pack(padx=10, pady=10)

    inventory = CTkButton(
        tab_frame,
        text="Inventory",
        text_font=(helvetica, 12, "bold"),
        fg_color=new_dark,
        text_color=("#2a2d2e", "#d1d5d8"),
        hover_color=btn_dark,
        command=lambda:raise_frame(inventory_main)
    )
    inventory.pack(padx=10, pady=10)

    settings = CTkButton(
        tab_frame,
        text="Settings",
        text_font=(helvetica, 12, "bold"),
        fg_color=new_dark,
        text_color=("#2a2d2e", "#d1d5d8"),
        hover_color=btn_dark,
        command=lambda:raise_frame(settings_main)
    )
    settings.pack(padx=10, pady=10)
    ###### Switching Tabs ########


    ##### Tab frame #####
    employees_main = CTkFrame(
        console,
        fg_color=new_dark
    )
    inventory_main = CTkFrame(
        console,
        fg_color=new_dark
    )
    settings_main = CTkFrame(
        console,
        fg_color=new_dark
    )

    for main_frame in (employees_main, inventory_main, settings_main):
        main_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    ##### Tab frame #####


    ##### Employees frame #####

    frame1 = CTkFrame(
        employees_main,
        fg_color=new_dark
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
        fg_color=btn_dark,
        text="Save",
        text_font=(helvetica, 12, "bold"),
        hover_color=new_dark,
        height=35,
        relief=RAISED,
        command=db_save
    )
    save.grid(row=7, column=0, padx=40, pady=5, sticky="news")

    employee_info_frame = CTkFrame(
        employees_main,

    )
    employee_info_frame.grid(row=1, column=0, padx=10, pady=10, ipadx=10, sticky="news")

    employee_info = Listbox(
        employee_info_frame,
        activestyle="underline",
        bg=new_dark,
        highlightcolor=btn_dark,
        selectbackground=btn_dark,
        takefocus=TRUE,
        font=(helvetica, 12),
        fg="white"
    )
    employee_info.grid(row=0, column=0, sticky="news")

    emp_info_scrollbar = CTkScrollbar(employee_info_frame, command=employee_info.yview)
    emp_info_scrollbar.grid(row=0, column=1, padx=0, pady=10, sticky="ns")

    employee_info.configure(yscrollcommand=emp_info_scrollbar.set)

    employee_info_frame.rowconfigure(0, weight=1)
    employee_info_frame.columnconfigure(0, weight=3)
    employee_info_frame.columnconfigure(1, weight=0)


    

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
        fg_color=new_dark
    )
    actions.grid(row=0, column=1, padx=10, pady=10, sticky="news")

    edit_btn = CTkButton(
        actions,
        fg_color=btn_dark,
        text="Edit",
        text_font=(helvetica, 12, "bold"),
        hover_color=new_dark,
        height=35,
        width=300,
        relief=RAISED
    )
    edit_btn.grid(row=0, column=0, padx=40, pady=5, sticky="news")

    delete_btn = CTkButton(
        actions,
        fg_color=btn_dark,
        text="Delete",
        text_font=(helvetica, 12, "bold"),
        hover_color=new_dark,
        height=35,
        width=300,
        relief=RAISED,
        command=db_delete
    )
    delete_btn.grid(row=1, column=0, padx=40, pady=5, sticky="news")

    freeze_btn = CTkButton(
        actions,
        fg_color=btn_dark,
        text="Freeze",
        text_font=(helvetica, 12, "bold"),
        hover_color=new_dark,
        height=35,
        width=300,
        relief=RAISED
    )
    freeze_btn.grid(row=2, column=0, padx=40, pady=5, sticky="news")

    view_btn = CTkButton(
        actions,
        fg_color=btn_dark,
        text="View",
        text_font=(helvetica, 12, "bold"),
        hover_color=new_dark,
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
        fg_color=new_dark
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



    ###### Inventory #######

    def _save_category():
        category_data = {}
        param_list = [
            cat_name.get(),
            isle.get(),
            shelf.get()
        ]
        for param in range(len(param_list)):
            if param_list[param] != "":
                category_data.update(
                    {
                        "name": param_list[0],
                        "isle": param_list[1],
                        "shelf": param_list[2]
                    }
                )
        invent = category.insert_one(category_data)
        cat_name.delete(0, END)
        isle.delete(0, END)
        shelf.delete(0, END)
        _reset_category()
        show_category()


    def category_delete():
        for d in category_list.curselection():
            cat_name = {"name": category_list.get(d)}
        delete = category.delete_one(cat_name)
        _reset_category()
        show_category()


    def _add_item():
        add_item = {}
        for x in category_list.curselection():
            add_item["category_id"] = category_list.get(x)
        if len(add_item) == 1:
            add_item["item name"] = item_name.get()
            add_item["price"] = item_price.get()
            add_item["item stock"] = item_stock.get()
        else:
            raise ValueError("select an category to continue")
        print(add_item)
        save_items = items.insert_one(add_item)

        item_name.delete(0, END)
        item_price.delete(0, END)
        item_stock.delete(0, END)
        
                

    category_frame = CTkFrame(
        inventory_main,
        fg_color=new_dark

    )
    category_frame.grid(row=0, column=0)

    category_title = CTkLabel(
        category_frame,
        text="Category and item entry",
        
    )
    category_title.grid(row=0, column=0, padx=10, pady=5)

    cat_name = CTkEntry(
        category_frame,
        placeholder_text="Name",
        text_font=(helvetica, 10),
        height=35,
        width=250
    )
    cat_name.grid(row=1, column=0, padx=10, pady=5)

    isle = CTkEntry(
        category_frame,
        placeholder_text="Isle",
        text_font=(helvetica, 10),
        height=35,
        width=250
    )
    isle.grid(row=2, column=0, padx=10, pady=5)

    shelf = CTkEntry(
        category_frame,
        placeholder_text="Shelf",
        text_font=(helvetica, 10),
        height=35,
        width=250
    )
    shelf.grid(row=3, column=0, padx=10, pady=5)

    save_category = CTkButton(
        category_frame,
        text="save",
        text_font=(helvetica, 10, "bold"),
        height=35,
        width=200,
        fg_color=btn_dark,
        hover_color=new_dark,
        command=_save_category,
    )
    save_category.grid(row=4, column=0, padx=10, pady=5)
    

    category_list_frame = CTkFrame(
        inventory_main,
        fg_color=new_dark
    )
    category_list_frame.grid(row=1, column=0)

    category_list = Listbox(
        category_list_frame,
        activestyle="dotbox",
        bg=new_dark,
        highlightcolor=btn_dark,
        selectbackground=btn_dark,
        takefocus=TRUE,
        font=(helvetica, 12),
        fg="white"
    )
    category_list.grid(row=0, column=0, padx=10, pady=10, ipadx=10, sticky="news")
    
    category_list_scrollbar = CTkScrollbar(category_list_frame, fg_color=new_dark, command=category_list.yview)
    category_list_scrollbar.grid(row=0, column=1, sticky="ns")

    category_list.configure(yscrollcommand=category_list_scrollbar.set)


    def show_category():
        for c in category.find():
            category_list.insert(END, c["name"])
    
    def _reset_category():
        category_list.delete(0, END)

    show_category()


    ###### The frame and the item entry widgets
    item_frame = CTkFrame(
        inventory_main,
        fg_color=new_dark
    )
    item_frame.grid(row=2, column=0)

    item_name = CTkEntry(
        item_frame,
        placeholder_text="Item name",
        text_font=(helvetica, 10),
        height=35,
        width=250
    )
    item_name.grid(row=0, column=0, padx=10, pady=5)

    item_price = CTkEntry(
        item_frame,
        placeholder_text="Price",
        text_font=(helvetica, 10),
        height=35,
        width=250
    )
    item_price.grid(row=1, column=0, padx=10, pady=5)

    item_stock = CTkEntry(
        item_frame,
        placeholder_text="Stock",
        text_font=(helvetica, 10),
        height=35,
        width=250
    )
    item_stock.grid(row=2, column=0, padx=10, pady=5)
    ###### The frame and the item entry widgets


    ###### The frame and the action buttons
    atn_btn_frame = CTkFrame(
        inventory_main,
        fg_color=new_dark

    )

    atn_btn_frame.grid(row=3, column=0, padx=10, pady=5)

    cat_delete = CTkButton(
        atn_btn_frame,
        text="Delete",
        fg_color=btn_dark,
        height=35,
        width=200,
        hover_color=new_dark,
        command=category_delete
    )
    cat_delete.grid(row=0, column=0, padx=10, pady=5)

    item_entry_btn =  CTkButton(
        atn_btn_frame,
        text="Enter item",
        fg_color=btn_dark,
        height=35,
        width=200,
        hover_color=new_dark,
        command=_add_item
    )
    item_entry_btn.grid(row=1, column=0, padx=10, pady=5)
    ###### The trame and the action buttons



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

    ####### employee information configure #######
    benefits_frame.columnconfigure(0, weight=1)
    benefits_frame.columnconfigure(1, weight=2)
    ####### emplyee column configure #######

    ##### grid Configurations #####



    console.mainloop()



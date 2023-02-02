from tkinter import *
from customtkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
import os

from pymongo import MongoClient

db_client = MongoClient("mongodb://localhost:27017/")
db = db_client["office_manager"]
employee_table = db["employee"]
category = db["category"]
items = db["items"]


new_dark = "#0f0f0f"
btn_dark = "#475e69"
btn_light = "#56f1bf"
purple = "#a172fb"

helvetica = "comic Sans Ms"

def admin():

    console = CTkToplevel()
    console.geometry("1400x900")
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
        fg_color=new_dark,
        border_color=btn_light,
        border_width=2
    )
    tab_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsw")

    ###### Switching Tabs ########
    employees = CTkButton(
        tab_frame,
        text="Employees",
        text_font=(helvetica, 12, "bold"),
        fg_color=new_dark,
        text_color=btn_light,
        hover_color=btn_dark,
        command=lambda:raise_frame(employees_main)
    )
    employees.pack(padx=2, pady=10)

    inventory = CTkButton(
        tab_frame,
        text="Inventory",
        text_font=(helvetica, 12, "bold"),
        fg_color=new_dark,
        text_color=btn_light,
        hover_color=btn_dark,
        command=lambda:raise_frame(inventory_main)
    )
    inventory.pack(padx=2, pady=10)

    settings = CTkButton(
        tab_frame,
        text="Settings",
        text_font=(helvetica, 12, "bold"),
        fg_color=new_dark,
        text_color=btn_light,
        hover_color=btn_dark,
        command=lambda:raise_frame(settings_main)
    )
    settings.pack(padx=2, pady=10)
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
            category_name = {"name": category_list.get(d)}
        delete = category.delete_one(category_name)
        _reset_category()
        show_category()


    def _add_item():
        add_item = {}
        for x in category_list.curselection():
            add_item["category_id"] = category_list.get(x)
        if len(add_item) == 1:
            add_item["item name"] = item_name.get()
            add_item["price"] = float(item_price.get())
            add_item["item stock"] = int(item_stock.get())
        else:
            raise ValueError("select an category to continue")
        print(add_item)
        save_items = items.insert_one(add_item)

        item_name.delete(0, END)
        item_price.delete(0, END)
        item_stock.delete(0, END)


    

    category_frame = CTkFrame(
        inventory_main,
        fg_color=new_dark,
        border_width=2,
        border_color=btn_light
    )
    category_frame.grid(row=0, column=0, padx=5, pady=5, sticky="news")


    category_input_frame = CTkFrame(
        category_frame,
        fg_color=new_dark,
    )
    category_input_frame.grid(row=0, column=0, padx=5, pady=5, sticky="news")

    category_disp_frame = CTkFrame(
        category_frame,
    )
    category_disp_frame.grid(row=0, column=1, padx=5, pady=5, sticky="news")


    category_title = CTkLabel(
        category_input_frame,
        text="Category and item entry",
        text_font=(helvetica, 10, "bold"),
        fg_color=new_dark
        
    )
    category_title.grid(row=0, column=0, padx=10, pady=3)

    cat_name = CTkEntry(
        category_input_frame,
        placeholder_text="Name",
        text_font=(helvetica, 10),
        height=30,
        width=200
    )
    cat_name.grid(row=1, column=0, padx=10, pady=3)

    isle = CTkEntry(
        category_input_frame,
        placeholder_text="Isle",
        text_font=(helvetica, 10),
        height=30,
        width=200
    )
    isle.grid(row=2, column=0, padx=10, pady=3)

    shelf = CTkEntry(
        category_input_frame,
        placeholder_text="Shelf",
        text_font=(helvetica, 10),
        height=30,
        width=200
    )
    shelf.grid(row=3, column=0, padx=10, pady=3)

    save_category = CTkButton(
        category_input_frame,
        text="save",
        text_font=(helvetica, 10, "bold"),
        height=30,
        width=200,
        fg_color=btn_dark,
        hover_color=new_dark,
        command=_save_category,
    )
    save_category.grid(row=4, column=0, padx=10, pady=3)
    

    category_list = Listbox(
        category_disp_frame,
        activestyle="dotbox",
        bg=new_dark,
        highlightcolor=btn_dark,
        selectbackground=btn_dark,
        takefocus=TRUE,
        font=(helvetica, 12, "bold"),
        fg="white"
    )
    category_list.grid(row=0, column=0, padx=10, pady=10, sticky="news")
    
    category_list_scrollbar = CTkScrollbar(category_disp_frame, fg_color=new_dark, command=category_list.yview)
    category_list_scrollbar.grid(row=0, column=1, sticky="ns")

    category_list.configure(yscrollcommand=category_list_scrollbar.set)


    def show_category():
        for c in category.find():
            category_list.insert(END, c["name"])
    
    def _reset_category():
        category_list.delete(0, END)

    show_category()


    # ###### The frame and the item entry widgets
    item_frame = CTkFrame(
        inventory_main,
        fg_color="black",
        border_color="#a172fb",
        border_width=2,
    )
    item_frame.grid(row=1, column=0, padx=5, pady=5, sticky="news")

    item_entry_frame = CTkFrame(
        item_frame,
        fg_color=new_dark
    )
    item_entry_frame.grid(row=0, column=0, padx=2, pady=5, sticky="news")

    action_btn_frame = CTkFrame(
        item_frame,
        fg_color=new_dark
    )
    action_btn_frame.grid(row=0, column=1, padx=2, pady=5, sticky="news")

    
    item_name = CTkEntry(
        item_entry_frame,
        placeholder_text="Item name",
        text_font=(helvetica, 10),
        height=30,
        width=200
    )
    item_name.grid(row=0, column=0, padx=10, pady=5)

    item_price = CTkEntry(
        item_entry_frame,
        placeholder_text="Price",
        text_font=(helvetica, 10),
        height=30,
        width=200
    )
    item_price.grid(row=1, column=0, padx=10, pady=5)

    item_stock = CTkEntry(
        item_entry_frame,
        placeholder_text="Stock",
        text_font=(helvetica, 10),
        height=30,
        width=200
    )
    item_stock.grid(row=2, column=0, padx=10, pady=5)
    ###### The frame and the item entry widgets


    # ###### The frame and the action buttons

    category_del_btn_icon = Image.open(PATH + "\img\cat_del.png").resize((28,28))
    category_del_btn_icon = ImageTk.PhotoImage(category_del_btn_icon)

    cat_delete = CTkButton(
        action_btn_frame,
        text="Delete\n category",
        text_color="gray",
        fg_color="#9E1B32",
        text_font=(helvetica, 10, "bold"),
        height=107,
        width=107,
        hover=False,
        image=category_del_btn_icon,
        compound="bottom",
        command=category_delete
    )
    cat_delete.grid(row=0, column=0, padx=10, pady=5)

    enter_icon_btn_icon = Image.open(PATH + "\img\item_enter.png").resize((28,28))
    enter_icon_btn_icon = ImageTk.PhotoImage(enter_icon_btn_icon)

    item_entry_btn =  CTkButton(
        action_btn_frame,
        text="Enter item",
        text_color="black",
        fg_color=btn_light,
        text_font=(helvetica, 10, "bold"),
        height=107,
        width=107,
        hover=False,
        image=enter_icon_btn_icon,
        compound="bottom",
        command=_add_item
    )
    item_entry_btn.grid(row=0, column=1, padx=5, pady=5)


    item_disp_frame =  CTkFrame(
        inventory_main,
        fg_color=new_dark,
        border_color="#a172fb",
        border_width=2
    )
    item_disp_frame.grid(row=0, column=1, padx=5, pady=5, rowspan=2, sticky="news")


    ##### Table #####
    item_table = ttk.Treeview(
        item_disp_frame,
        height=19,
    )

    item_table["columns"] = ("Item name", "Price", "Item stock")

    item_table.column("#0", width=0, stretch=NO)
    item_table.column("Item name", width=200, anchor=W, minwidth=200)
    item_table.column("Price", width=200, anchor=CENTER, minwidth=200)
    item_table.column("Item stock", width=200, anchor=CENTER, minwidth=200)

    item_table.heading("#0", text="", anchor=W)
    item_table.heading("Item name", text="Item name", anchor=W)
    item_table.heading("Price", text="Price", anchor=CENTER)
    item_table.heading("Item stock", text="Item stock", anchor=CENTER)

    item_table.grid(row=0, column=0, padx=3, pady=2)



    item_disp_btn_frame =  CTkFrame(
        inventory_main,
        border_width=2,
        border_color=btn_light,
        fg_color=new_dark
    )
    item_disp_btn_frame.grid(row=2, column=1, padx=5, pady=5, rowspan=2, sticky="news")

    item_disp_btn_img = Image.open(PATH + "\img\show.png").resize((28,28))
    item_disp_btn_img = ImageTk.PhotoImage(item_disp_btn_img)

    def _get_items():
        if item_table is not None:
            _clear_tree()
        get_item_query = {}
        for cat in category_list.curselection():
            get_item_query["category_id"] = category_list.get(cat)
        get_items = items.find(get_item_query)

        count = 0
        for item in get_items:
            print(item["item name"])
            item_table.insert(parent="", index=END, iid=count, text="", values=(item["item name"], item["price"], item["item stock"]))
            count +=1

        total_label.configure(text="#"+total_item_price())

        _item_total_price()


        
    def _clear_tree():
        for items in item_table.get_children():
            item_table.delete(items)

    
    def remove_table_item():
        selected_table_item = {}
        values = []
        del_item = {}

        item = item_table.focus()
        selected_table_item.update(item_table.item(item))
        for x in selected_table_item["values"]:
            values.append(x)
        del_item["item name"] = values[0]

        query = items.delete_one(del_item)

        item_table.delete(item)

    ##### Table #####

    item_disp_btn = CTkButton(
        item_disp_btn_frame,
        text="show items",
        text_color="black",
        fg_color=btn_light,
        text_font=(helvetica, 10, "bold"),
        height=107,
        width=107,
        image=item_disp_btn_img,
        compound="bottom",
        hover_color="#a172fb",
        command=_get_items
    )
    item_disp_btn.grid(row=0, column=0, padx=5, pady=6)

    item_del_btn = CTkButton(
        item_disp_btn_frame,
        text="Delete \n item",
        text_color="gray",
        fg_color="#9E1B32",
        text_font=(helvetica, 10, "bold"),
        height=107,
        width=107,
         image=category_del_btn_icon,
        compound="bottom",
        hover_color="#a172fb",
        command=remove_table_item
    )
    item_del_btn.grid(row=0, column=1, padx=5, pady=6)

    display_label = CTkFrame(
        item_disp_btn_frame,
        height=107,
        width=200,
        fg_color=btn_light
    )
    display_label.grid(row=0, column=2, padx=5, pady=6)

    
   ########### price calculation
    def total_item_price():
        pipeline = [
            {"$group": {"_id": "null", "total_amount": {"$sum": "$price"}}}
        ]
        _sum_ = items.aggregate(pipeline)

        res = [i["total_amount"] for i in _sum_]
        return str(res[0])

   ########### price calculation
        

    total_price_title_label = CTkLabel(
        display_label,
        text="total",
        text_font=(helvetica, 9, "bold"),
        text_color="black",
        anchor="nw",
        fg_color=btn_light
    )
    total_price_title_label.grid(row=0, column=0, pady=10, ipady=0)

    total_label = CTkLabel(
        display_label,
        text="amount",
        text_font=(helvetica, 12, "bold"),
        text_color="black",
        fg_color=btn_light
    )
    total_label.grid(row=1, column=0, pady=10)



    item_total_title_frame = CTkFrame(
        item_disp_btn_frame,
        height=107,
        width=200,
        fg_color=btn_light,
    )
    item_total_title_frame.grid(row=0, column=3, padx=5, pady=6)


    def _item_total_price():
        select_table_item = {}
        value = []
        calc = {}

        item = item_table.focus()
        select_table_item.update(item_table.item(item))
        print(select_table_item)

        print(value)



    item_total = CTkLabel(
        item_total_title_frame,
        text="item total",
        text_font=(helvetica, 9, "bold"),
        text_color="black",
        anchor="nw",
        fg_color=btn_light
    )
    item_total.grid(row=0, column=0, pady=10, ipady=0)

    item_total_label = CTkLabel(
        item_total_title_frame,
        text="amount",
        text_font=(helvetica, 12, "bold"),
        text_color="black",
        fg_color=btn_light
    )
    item_total_label.grid(row=1, column=0, pady=10)



    _get_items()


    ###### Inventory #######



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



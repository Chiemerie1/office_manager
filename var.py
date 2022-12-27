from tkinter import *
from customtkinter import *

from pymongo import MongoClient


#### DB ####
db_client = MongoClient("mongodb://localhost:27017/")
db = db_client["office_manager"]
employee_table = db["employee"]
#### DB ####


#### Employee info ####
first_name = StringVar()
last_name = StringVar()
username = StringVar()
email = StringVar()
phone_no = StringVar()
desg = StringVar()
Password = StringVar()
#### Employee info ####

employee_info = [
    first_name,
    last_name,
    username,
    email,
    phone_no,
    desg,
    Password
]

def db_save():
    for x in employee_info:
        if x.get() is not None:
            emp_dict = {
                "first_name": first_name.get(),
                "last_name": last_name.get(),
                "username": username.get(),
                "email": email.get(),
                "phone no": phone_no.get(),
                "desg": desg.get(),
                "password": Password.get()
                
            }
            employee = employee_table.insert_one(emp_dict)
            




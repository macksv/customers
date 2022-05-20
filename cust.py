from tkinter import *
# import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import pyodbc
import db_connect
import sys

root = Tk()
root.title("Hello World")
root.geometry("400x400")

conn_string = db_connect.get_connect_str()

try:
    conn = pyodbc.connect(conn_string)

except Exception as e:
    print(e)
    print("cannot connect to DB ... terminating.")
    sys.exit()
else:
    cursor = conn.cursor()


# call back function used for numeric input box
def correct(inp):
    if inp.isdigit():
        return True
    elif inp == "":
        return True
    else:
        return False


def add_record():
    """Adds a record to the database.
        For the date it is best to use YYYYMMDD and for datetime use YYYY-MM-DDTHH:MM:SS
    """
    inputs = first_name.get() + "," + last_name.get() + "," + \
        dob.get_date().strftime("%d-%m-%Y") + "," + str(gender.get()) + \
        "," + street_addr.get() + "," + suburb.get() + "," + state.get()
    input_list = []
    input_list = first_name.get(), last_name.get(), dob.get_date().strftime(
        "%Y%m%d"), str(gender.get()), street_addr.get(), suburb.get(), state.get(), postcode.get(), email.get()
    input_tuple = tuple(input_list)

    sql_stmt = """insert into customer (
                     first_name, last_name, date_of_birth, gender, street_addr, suburb, state, postcode, email_addr 
                    ) values (
                        ?,?,?,?,?,?,?,?,?
                    )
               """
    count = cursor.execute(sql_stmt, input_tuple).rowcount
    cursor.commit()

    my_label = Label(root, text=str(count) + "new record added")
    my_label.grid(row=10, column=0, pady=10)


# create data labels
first_name_lbl = Label(root, text="First Name")
first_name_lbl.grid(row=0, column=0, sticky=W, padx=10)
last_name_lbl = Label(root, text="Last Name")
last_name_lbl.grid(row=1, column=0, sticky=W, padx=10)
dob_lbl = Label(root, text="Date of Birth")
dob_lbl.grid(row=2, column=0, sticky=W, padx=10)
gender_lbl = Label(root, text="Gender")
gender_lbl.grid(row=3, column=0, sticky=W, padx=10)
street_addr_lbl = Label(root, text="Street Address")
street_addr_lbl.grid(row=4, column=0, sticky=W, padx=10)
suburb_lbl = Label(root, text="Suburb")
suburb_lbl.grid(row=5, column=0, sticky=W, padx=10)
state_lbl = Label(root, text="State")
state_lbl.grid(row=6, column=0, sticky=W, padx=10)
postcode_lbl = Label(root, text="Postcode")
postcode_lbl.grid(row=7, column=0, sticky=W, padx=10)
email_lbl = Label(root, text="Email")
email_lbl.grid(row=8, column=0, sticky=W, padx=10)

# create data entry fields
first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20, pady=3)
last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20, pady=3)
# make dob as date picker
# dob = Entry(root, width=30)
dob = DateEntry(root, selectmode='day')
dob.grid(row=2, column=1, sticky=W, padx=20, pady=3)


# change gender to be a radio button
# gender = Entry(root, width=30)
# gender.grid(row=3, column=1, padx=20)
my_frame = Frame(root)  # , width=200, height=100)
my_frame.grid(row=3, column=1, columnspan=2,
              sticky=W, padx=15, pady=3)

gender = StringVar()
gender.set("M")
male = Radiobutton(my_frame, text="Male", variable=gender, value="M")
male.grid(row=1, column=1)
female = Radiobutton(my_frame, text="Female", variable=gender, value="F")
female.grid(row=1, column=2)

street_addr = Entry(root, width=30)
street_addr.grid(row=4, column=1, padx=20, pady=3)
suburb = Entry(root, width=30)
suburb.grid(row=5, column=1, padx=20, pady=3)

# create combo box for state
au_states = [
    "NSW", "VIC", "QLD", "SA", "WA", "NT", "TAS"


]
# state = Entry(root, width=30)
state = ttk.Combobox(root, value=au_states, width=3)
state.current(0)
state.grid(row=6, column=1, sticky=W, padx=20, pady=3)

# accept only numbers - see https://www.youtube.com/watch?v=oRYshQCOHOs
postcode = Entry(root, width=4)
postcode.grid(row=7, column=1, sticky=W, padx=20, pady=3)
reg = root.register(correct)
postcode.config(validate="key", validatecommand=(reg, '%P'))

email = Entry(root, width=30)
email.grid(row=8, column=1, padx=20, pady=3)

display_btn = Button(root, text="Add record to DB", command=add_record)
display_btn.grid(row=9, column=0, pady=8)
root.mainloop()

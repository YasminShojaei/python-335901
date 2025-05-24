from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from users_validator import *
import pickle


user_list = read_from_file("user.dat")


def load_data(user_list):
    user_list = read_from_file("user.dat")
    for row in table.get_children():
        table.delete(row)

    for user in user_list:
        table.insert("", END, values=user)
    print("Loaded users:", user_list)


def reset_form():
    id_.set(len(user_list) + 1)
    name.set("")
    user_name.set("")
    password.set("")
    status.set("")
    load_data(user_list)


def save_bttn():
    user = (id_.get(), name.get(), user_name.get(),
            password.get(), status.get())
    errors = user_validator(user)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "user saved")
        user_list.append(user)
        write_to_file("user.dat", user_list)
        reset_form()


def edit_bttn():
    selected = table.focus()
    if not selected:
        msg.showwarning("Warning", "No user selected")
        return

    updated_user = (id_.get(), name.get(), user_name.get(),
                    password.get(), status.get())
    errors = user_validator(updated_user)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
        return

    for i, p in enumerate(user_list):
        if p[0] == updated_user[0]:
            user_list[i] = updated_user
            break

    write_to_file("user.dat", user_list)
    reset_form()
    msg.showinfo("Success", "updated")


def remove_bttn():
    selected = table.focus()
    if not selected:
        msg.showwarning("Warning", "No user selected")
        return

    selected_user = table.item(selected)["values"]

    for i in range(len(user_list)):
        if user_list[i][0] == selected_user[0]:
            del user_list[i]
            break
    write_to_file("user.dat", user_list)
    reset_form()
    msg.showinfo("Success", "user removed")


def table_select(x):
    selected_items = table.selection()
    if not selected_items:
        return
    selected_user = table.item(table.focus())["values"]
    if selected_user:
        id_.set(selected_user[0])
        name.set(selected_user[1])
        user_name.set(selected_user[2])
        password.set(selected_user[3])
        status.set(selected_user[4])


firt_window = Tk()
firt_window.title("Users App")
firt_window.geometry("720x300")

# id
Label(firt_window, text="id", font="Calibri, 8").place(x=20, y=20)
id_ = IntVar()
Entry(firt_window, textvariable=id_).place(x=75, y=20)

# name
Label(firt_window, text="name", font="Calibri, 8").place(x=20, y=60)
name = StringVar()
Entry(firt_window, textvariable=name).place(x=75, y=60)

# user name
Label(firt_window, text="username", font="Calibri, 8").place(x=20, y=100)
user_name = StringVar()
Entry(firt_window, textvariable=user_name).place(x=75, y=100)

# password
Label(firt_window, text="password", font="Calibri, 8").place(x=20, y=140)
password = StringVar()
Entry(firt_window, textvariable=password).place(x=75, y=140)

# status
Label(firt_window, text="status", font="Calibri, 8").place(x=20, y=200)
status = StringVar()
Radiobutton(firt_window, text="Aktive", variable=status,
            value="Aktive").place(x=75, y=180)
Radiobutton(firt_window, text="Not aktive", variable=status,
            value="Not aktive").place(x=75, y=210)

# Table
table = ttk.Treeview(firt_window, columns=[1, 2, 3, 4, 5], show="headings")
table.heading(1, text="Id")
table.heading(2, text="name")
table.heading(3, text="username")
table.heading(4, text="password")
table.heading(5, text="status")

table.column(1, width=100, anchor="center")
table.column(2, width=100, anchor="center")
table.column(3, width=100, anchor="center")
table.column(4, width=100, anchor="center")
table.column(5, width=100, anchor="center")


table.place(x=230, y=20, height=269)
table.bind("<<TreeviewSelect>>", table_select)

# Button
Button(firt_window, text="Save", width=7, command=save_bttn).place(x=20, y=240)
Button(firt_window, text="Edit", width=7, command=edit_bttn).place(x=84, y=240)
Button(firt_window, text="Remove", width=7,
       command=remove_bttn).place(x=146, y=240)
Button(firt_window, text="Clear", width=25,
       command=reset_form).place(x=20, y=265)

reset_form()

firt_window.mainloop()

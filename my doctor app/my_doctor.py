from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from validator import *
import pickle

patient_list = read_from_file("patients.dat")


def load_data(patient_list):
    patient_list = read_from_file("patients.dat")
    for row in table.get_children():
        table.delete(row)

    for person in patient_list:
        table.insert("", END, values=person)


def reset_form():
    id.set(len(patient_list) + 1)
    patient_full_name.set("")
    dr_full_name.set("")
    diseases.set("")
    medications.set("")
    date.set("")
    load_data(patient_list)


def save_btn_click():
    patient = (id.get(), patient_full_name.get(), dr_full_name.get(),
               diseases.get(), medications.get(), date.get())
    errors = person_validator(patient)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
    else:
        msg.showinfo("Saved", "Patient saved")
        patient_list.append(patient)
        write_to_file("patients.dat", patient_list)
        reset_form()


def edit_btn_click():
    selected = table.focus()
    if not selected:
        msg.showwarning("Warning", "No patient selected")
        return

    updated_patient = (id.get(), patient_full_name.get(), dr_full_name.get(),
                       diseases.get(), medications.get(), date.get())
    errors = person_validator(updated_patient)
    if errors:
        msg.showerror("Errors", "\n".join(errors))
        return

    for i, p in enumerate(patient_list):
        if p[0] == updated_patient[0]:
            patient_list[i] = updated_patient
            break

    write_to_file("patients.dat", patient_list)
    reset_form()
    msg.showinfo("Success", "updated")


def remove_btn_click():
    selected = table.focus()
    if not selected:
        msg.showwarning("Warning", "no patient selected")
        return

    selected_patient = table.item(selected)["values"]

    for i in range(len(patient_list)):
        if patient_list[i][0] == selected_patient[0]:
            del patient_list[i]
            break

    write_to_file("patients.dat", patient_list)
    reset_form()
    msg.showinfo("Success", "Patient removed")


def table_select(x):
    selected_items = table.selection()
    if not selected_items:
        return
    selected_patient = table.item(table.focus())["values"]
    if selected_patient:
        id.set(selected_patient[0])
        patient_full_name.set(selected_patient[1])
        dr_full_name.set(selected_patient[2])
        diseases.set(selected_patient[3])
        medications.set(selected_patient[4])
        date.set(selected_patient[5])


window = Tk()
window.title("My doctor app")
window.geometry("700x400")

# Id
Label(window, text="Id").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=80, y=20)

# patient full name
Label(window, text="Patient").place(x=20, y=60)
patient_full_name = StringVar()
Entry(window, textvariable=patient_full_name).place(x=80, y=60)

# doctor's full name
Label(window, text="Doctor").place(x=20, y=100)
dr_full_name = StringVar()
Entry(window, textvariable=dr_full_name).place(x=80, y=100)

# Diseases
Label(window, text="Diseases").place(x=20, y=140)
diseases = StringVar()
Entry(window, textvariable=diseases).place(x=80, y=140)

# Medications
Label(window, text="Medik.").place(x=20, y=180)
medications = StringVar()
Entry(window, textvariable=medications).place(x=80, y=180)

# ِDate of visit
Label(window, text="Date").place(x=20, y=220)
date = StringVar()
Entry(window, textvariable=date).place(x=80, y=220)


table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Patient full name")
table.heading(3, text="Doctors full name")
table.heading(4, text="Diseases")
table.heading(5, text="Medications")
table.heading(6, text="Date of visit")


table.column(1, width=60)
table.column(2, width=110)
table.column(3, width=110)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=100)

table.place(x=230, y=20)
table.bind("<<TreeviewSelect>>", table_select)


Button(window, text="Save", width=8, command=save_btn_click).place(
    x=20, y=265, width=50)
Button(window, text="Edit", width=8, command=edit_btn_click).place(
    x=95, y=265, width=50)
Button(window, text="Remove", width=8,
       command=remove_btn_click).place(x=167, y=265, width=50)
Button(window, text="Clear", width=8, command=reset_form).place(
    x=20, y=300, width=200)

reset_form()


window.mainloop()

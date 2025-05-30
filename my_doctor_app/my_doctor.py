from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from file_manager import *
from patient import *
from validator import *
import pickle
from datetime import datetime

patient_list = read_from_file("patients.dat")

# region def buttons


def load_data(patient_list):
    patient_list = read_from_file("patients.dat")
    for row in table.get_children():
        table.delete(row)

    for patient in patient_list:
        table.insert("", END, values=patient.to_tuple())


def reset_form():
    id.set(len(patient_list) + 1)
    patient_full_name.set("")
    dr_full_name.set("")
    diseases.set("")
    medications.set("")
    current_time = datetime.now().strftime("%Y%m%d")
    visit_date.set(current_time)
    load_data(patient_list)


def save_btn_click():
    current_time = datetime.now().strftime("%Y%m%d")
    patient = Patient(id.get(), patient_full_name.get(), dr_full_name.get(),
                      diseases.get(), medications.get(), current_time)
    errors = patient.validate()
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

    updated_patient = Patient(id.get(), patient_full_name.get(), dr_full_name.get(),
                              diseases.get(), medications.get(), visit_date.get())
    errors = updated_patient.validate()
    if errors:
        msg.showerror("Errors", "\n".join(errors))
        return

    for i, p in enumerate(patient_list):
        if p[0] == updated_patient.id:
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
    selected_patient = Patient(* table.item(table.focus())["values"])
    if selected_patient:
        id.set(selected_patient.id)
        patient_full_name.set(selected_patient.full_name)
        dr_full_name.set(selected_patient.dr_name)
        diseases.set(selected_patient.dieses)
        medications.set(selected_patient.medications)
        visit_date.set(selected_patient.visit_date)
# endregion


window = Tk()
window.title("My doctor app")
window.geometry("850x400")


# region Lables
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
visit_date = StringVar()
Entry(window, textvariable=visit_date, state="readonly").place(x=80, y=220)

# endregion

# region table
table = ttk.Treeview(window, columns=[1, 2, 3, 4, 5, 6], show="headings")
table.heading(1, text="Id")
table.heading(2, text="Patient full name")
table.heading(3, text="Doctors full name")
table.heading(4, text="Diseases")
table.heading(5, text="Medications")
table.heading(6, text="Date of visit")


table.column(1, width=60, anchor="center")
table.column(2, width=100, anchor="center")
table.column(3, width=120, anchor="center")
table.column(4, width=120, anchor="center")
table.column(5, width=100, anchor="center")
table.column(6, width=100, anchor="center")

table.place(x=230, y=20, height=305)
table.bind("<<TreeviewSelect>>", table_select)
# endregion


# region button
Button(window, text="Save", width=8, command=save_btn_click).place(
    x=20, y=265, width=50)
Button(window, text="Edit", width=8, command=edit_btn_click).place(
    x=95, y=265, width=50)
Button(window, text="Remove", width=8,
       command=remove_btn_click).place(x=167, y=265, width=50)
Button(window, text="Clear", width=8, command=reset_form).place(
    x=20, y=300, width=200)
# endregion

reset_form()


window.mainloop()

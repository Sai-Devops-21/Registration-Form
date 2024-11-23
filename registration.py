from tkinter import *
from tkinter import messagebox

def validate_form(name, email, password, confirm_password, ph_no, branch):
    if not name or not email or not password or not confirm_password or not ph_no or not branch:
        return "All entries need to be filled"

    if '@' not in email or '.' not in email:
        return "Email should contain @ and ."

    if len(password) < 8:
        return "Password must be at least 8 characters"

    if password != confirm_password:
        return "Passwords do not match"

    if not ph_no.isdigit():
        return "Phone number should contain only digits"

    if len(ph_no) != 10:
        return "Phone number should contain 10 digits"

    return None

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    ph_no = ph_no_entry.get()
    branch = branch_entry.get()

    error = validate_form(name, email, password, confirm_password, ph_no, branch)

    if error:
        messagebox.showerror("Error", error)
    else:
        messagebox.showinfo("Success", "Registration successful")

root = Tk()
root.title("Registration Form")

Label(root, text="Name").grid(row=0, column=0, padx=5, pady=5)
Label(root, text="Email").grid(row=1, column=0, padx=5, pady=5)
Label(root, text="Password").grid(row=2, column=0, padx=5, pady=5)
Label(root, text="Confirm Password").grid(row=3, column=0, padx=5, pady=5)
Label(root, text="Phone Number").grid(row=4, column=0, padx=5, pady=5)
Label(root, text="Branch").grid(row=5, column=0, padx=5, pady=5)

name_entry = Entry(root)
email_entry = Entry(root)
password_entry = Entry(root, show="*")
confirm_password_entry = Entry(root, show="*")
ph_no_entry = Entry(root)
branch_entry = Entry(root)

name_entry.grid(row=0, column=1, padx=5, pady=5)
email_entry.grid(row=1, column=1, padx=5, pady=5)
password_entry.grid(row=2, column=1, padx=5, pady=5)
confirm_password_entry.grid(row=3, column=1, padx=5, pady=5)
ph_no_entry.grid(row=4, column=1, padx=5, pady=5)
branch_entry.grid(row=5, column=1, padx=5, pady=5)

submit = Button(root, text="Register", command=submit_form)
submit.grid(row=6, column=1, padx=5, pady=5)

root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
from member import Member

# List used to store members
members = []

# Create the main application window
window = tk.Tk()
window.title("Gym Membership Management System")
window.geometry("600x500")


# Main heading
title_label = tk.Label(
    window,
    text="Gym Membership Management System",
    font=("Arial", 18)
)
title_label.pack(pady=20)


# Frame to hold the member form
form_frame = tk.Frame(window)
form_frame.pack(pady=10)


# Member ID
tk.Label(form_frame, text="Member ID:").grid(
    row=0, column=0, padx=10, pady=10, sticky="e"
)

member_id_entry = tk.Entry(form_frame)
member_id_entry.grid(row=0, column=1, padx=10, pady=10)


# Name
tk.Label(form_frame, text="Name:").grid(
    row=1, column=0, padx=10, pady=10, sticky="e"
)

name_entry = tk.Entry(form_frame)
name_entry.grid(row=1, column=1, padx=10, pady=10)


# Email
tk.Label(form_frame, text="Email:").grid(
    row=2, column=0, padx=10, pady=10, sticky="e"
)

email_entry = tk.Entry(form_frame)
email_entry.grid(row=2, column=1, padx=10, pady=10)


# Membership Type
tk.Label(form_frame, text="Membership Type:").grid(
    row=3, column=0, padx=10, pady=10, sticky="e"
)

membership_type_combo = ttk.Combobox(
    form_frame,
    values=["Basic", "Plus", "Premium"],
    state="readonly"
)
membership_type_combo.grid(row=3, column=1, padx=10, pady=10)
membership_type_combo.set("Basic")


# Membership Status
tk.Label(form_frame, text="Membership Status:").grid(
    row=4, column=0, padx=10, pady=10, sticky="e"
)

membership_status_combo = ttk.Combobox(
    form_frame,
    values=["Active", "Inactive", "Expired"],
    state="readonly"
)
membership_status_combo.grid(row=4, column=1, padx=10, pady=10)
membership_status_combo.set("Active")

def add_member():
    member_id = member_id_entry.get()
    name = name_entry.get()
    email = email_entry.get()
    membership_type = membership_type_combo.get()
    membership_status = membership_status_combo.get()

    # Make sure required fields are filled in
    if not member_id or not name or not email:
        messagebox.showerror(
            "Missing Information",
            "Please enter a Member ID, Name, and Email."
        )
        return

    # Make sure the Member ID is a number
    if not member_id.isdigit():
        messagebox.showerror(
            "Invalid Member ID",
            "Member ID must be a number."
        )
        return

    # Prevent duplicate Member IDs
    for member in members:
        if member.member_id == int(member_id):
            messagebox.showerror(
                "Duplicate Member ID",
                "A member with that ID already exists."
            )
            return

    new_member = Member(
        int(member_id),
        name,
        email,
        membership_type,
        membership_status
    )

    members.append(new_member)

    messagebox.showinfo(
        "Member Added",
        f"{name} was added successfully."
    )

    # Clear the text fields
    member_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

    membership_type_combo.set("Basic")
    membership_status_combo.set("Active")

def view_members():
    # Create a new window
    member_window = tk.Toplevel(window)
    member_window.title("Member List")
    member_window.geometry("650x350")

    title = tk.Label(
        member_window,
        text="Gym Members",
        font=("Arial", 16)
    )
    title.pack(pady=10)

    # Create a table
    member_table = ttk.Treeview(
        member_window,
        columns=("ID", "Name", "Email", "Type", "Status"),
        show="headings"
    )

    member_table.heading("ID", text="ID")
    member_table.heading("Name", text="Name")
    member_table.heading("Email", text="Email")
    member_table.heading("Type", text="Membership")
    member_table.heading("Status", text="Status")

    member_table.column("ID", width=50)
    member_table.column("Name", width=130)
    member_table.column("Email", width=180)
    member_table.column("Type", width=100)
    member_table.column("Status", width=100)

    # Add each member to the table
    for member in members:
        member_table.insert(
            "",
            tk.END,
            values=(
                member.member_id,
                member.name,
                member.email,
                member.membership_type,
                member.membership_status
            )
        )

    member_table.pack(padx=10, pady=10, fill="both", expand=True)


def search_member():
    member_id = member_id_entry.get()

    # Make sure an ID was entered
    if not member_id:
        messagebox.showerror(
            "Missing Member ID",
            "Please enter a Member ID to search."
        )
        return

    # Make sure the ID is a number
    if not member_id.isdigit():
        messagebox.showerror(
            "Invalid Member ID",
            "Member ID must be a number."
        )
        return

    # Search through the members list
    for member in members:
        if member.member_id == int(member_id):
            messagebox.showinfo(
                "Member Found",
                f"ID: {member.member_id}\n"
                f"Name: {member.name}\n"
                f"Email: {member.email}\n"
                f"Membership: {member.membership_type}\n"
                f"Status: {member.membership_status}"
            )
            return

    # Runs if no matching member was found
    messagebox.showerror(
        "Member Not Found",
        "No member was found with that ID."
    )


def load_member():
    member_id = member_id_entry.get()

    if not member_id:
        messagebox.showerror(
            "Missing Member ID",
            "Please enter a Member ID."
        )
        return

    if not member_id.isdigit():
        messagebox.showerror(
            "Invalid Member ID",
            "Member ID must be a number."
        )
        return

    for member in members:
        if member.member_id == int(member_id):

            # Clear the current form information
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)

            # Load the member's information into the form
            name_entry.insert(0, member.name)
            email_entry.insert(0, member.email)
            membership_type_combo.set(member.membership_type)
            membership_status_combo.set(member.membership_status)

            messagebox.showinfo(
                "Member Loaded",
                "Member information loaded. Make your changes and click Save Changes."
            )
            return

    messagebox.showerror(
        "Member Not Found",
        "No member was found with that ID."
    )


def save_changes():
    member_id = member_id_entry.get()

    if not member_id or not member_id.isdigit():
        messagebox.showerror(
            "Invalid Member ID",
            "Please enter a valid Member ID."
        )
        return

    for member in members:
        if member.member_id == int(member_id):

            name = name_entry.get()
            email = email_entry.get()
            membership_type = membership_type_combo.get()
            membership_status = membership_status_combo.get()

            if not name or not email:
                messagebox.showerror(
                    "Missing Information",
                    "Name and Email cannot be empty."
                )
                return

            member.update_member(
                name,
                email,
                membership_type,
                membership_status
            )

            messagebox.showinfo(
                "Member Updated",
                f"{name}'s information was updated successfully."
            )

            # Clear the form
            member_id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            email_entry.delete(0, tk.END)
            membership_type_combo.set("Basic")
            membership_status_combo.set("Active")

            return

    messagebox.showerror(
        "Member Not Found",
        "No member was found with that ID."
    )


# Frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=15)

add_button = tk.Button(
    button_frame,
    text="Add Member",
    command=add_member,
    width=20
)
add_button.grid(row=0, column=0, padx=5, pady=5)

view_button = tk.Button(
    button_frame,
    text="View Members",
    command=view_members,
    width=20
)
view_button.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(
    button_frame,
    text="Search Member",
    command=search_member,
    width=20
)
search_button.grid(row=1, column=0, padx=5, pady=5)

load_button = tk.Button(
    button_frame,
    text="Load Member for Editing",
    command=load_member,
    width=20
)
load_button.grid(row=1, column=1, padx=5, pady=5)

save_button = tk.Button(
    button_frame,
    text="Save Changes",
    command=save_changes,
    width=20
)
save_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)


# Start the application
window.mainloop()
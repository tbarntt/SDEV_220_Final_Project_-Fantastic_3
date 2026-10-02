import tkinter as tk
from tkinter import ttk, messagebox
from member import Member
from gymclass import GymClass
from registration import Registration

# List used to store members
members = []

# List used to store gym classes
gym_classes = []

# List used to store registrations
registrations = []

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


def manage_classes():
    # Create a new window for managing gym classes
    class_window = tk.Toplevel(window)
    class_window.title("Manage Gym Classes")
    class_window.geometry("650x500")

    tk.Label(
        class_window,
        text="Gym Classes",
        font=("Arial", 16)
    ).pack(pady=10)

    # Form for entering class information
    class_form = tk.Frame(class_window)
    class_form.pack(pady=10)

    tk.Label(class_form, text="Class ID:").grid(
        row=0, column=0, padx=10, pady=5
    )
    class_id_entry = tk.Entry(class_form)
    class_id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(class_form, text="Class Name:").grid(
        row=1, column=0, padx=10, pady=5
    )
    class_name_entry = tk.Entry(class_form)
    class_name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(class_form, text="Instructor:").grid(
        row=2, column=0, padx=10, pady=5
    )
    instructor_entry = tk.Entry(class_form)
    instructor_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(class_form, text="Capacity:").grid(
        row=3, column=0, padx=10, pady=5
    )
    capacity_entry = tk.Entry(class_form)
    capacity_entry.grid(row=3, column=1, padx=10, pady=5)

    def add_class():
        class_id = class_id_entry.get()
        class_name = class_name_entry.get()
        instructor = instructor_entry.get()
        capacity = capacity_entry.get()

        # Make sure all fields are filled in
        if not class_id or not class_name or not instructor or not capacity:
            messagebox.showerror(
                "Missing Information",
                "Please fill in all class information."
            )
            return

        # Class ID and capacity must be numbers
        if not class_id.isdigit() or not capacity.isdigit():
            messagebox.showerror(
                "Invalid Information",
                "Class ID and Capacity must be numbers."
            )
            return

        # Prevent duplicate class IDs
        for gym_class in gym_classes:
            if gym_class.class_id == int(class_id):
                messagebox.showerror(
                    "Duplicate Class ID",
                    "A class with that ID already exists."
                )
                return

        # Create a GymClass object
        new_class = GymClass(
            int(class_id),
            class_name,
            instructor,
            int(capacity)
        )

        gym_classes.append(new_class)

        messagebox.showinfo(
            "Class Added",
            f"{class_name} was added successfully."
        )

        # Clear the form
        class_id_entry.delete(0, tk.END)
        class_name_entry.delete(0, tk.END)
        instructor_entry.delete(0, tk.END)
        capacity_entry.delete(0, tk.END)

        
    add_class_button = tk.Button(
        class_window,
        text="Add Class",
        command=add_class,
        width=20
    )
    add_class_button.pack(pady=10)

    def view_classes():
        # Create a new window to display gym classes
        view_window = tk.Toplevel(class_window)
        view_window.title("Gym Class List")
        view_window.geometry("650x350")

        tk.Label(
            view_window,
            text="Available Gym Classes",
            font=("Arial", 16)
        ).pack(pady=10)

        # Create a table
        class_table = ttk.Treeview(
            view_window,
            columns=("ID", "Name", "Instructor", "Capacity", "Registered"),
            show="headings"
        )

        class_table.heading("ID", text="ID")
        class_table.heading("Name", text="Class Name")
        class_table.heading("Instructor", text="Instructor")
        class_table.heading("Capacity", text="Capacity")
        class_table.heading("Registered", text="Registered")

        class_table.column("ID", width=50)
        class_table.column("Name", width=130)
        class_table.column("Instructor", width=130)
        class_table.column("Capacity", width=80)
        class_table.column("Registered", width=80)

        # Add each gym class to the table
        for gym_class in gym_classes:
            class_table.insert(
                "",
                tk.END,
                values=(
                    gym_class.class_id,
                    gym_class.class_name,
                    gym_class.instructor,
                    gym_class.capacity,
                    len(gym_class.registrations)
                )
            )

        class_table.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

    view_class_button = tk.Button(
        class_window,
        text="View Classes",
        command=view_classes,
        width=20
    )
    view_class_button.pack(pady=10)    

def manage_registrations():
    registration_window = tk.Toplevel(window)
    registration_window.title("Class Registration")
    registration_window.geometry("500x400")

    tk.Label(
        registration_window,
        text="Register Member for Class",
        font=("Arial", 16)
    ).pack(pady=15)

    registration_form = tk.Frame(registration_window)
    registration_form.pack(pady=10)

    # Registration ID
    tk.Label(
        registration_form,
        text="Registration ID:"
    ).grid(row=0, column=0, padx=10, pady=10)

    registration_id_entry = tk.Entry(registration_form)
    registration_id_entry.grid(
        row=0, column=1, padx=10, pady=10
    )

    # Member ID
    tk.Label(
        registration_form,
        text="Member ID:"
    ).grid(row=1, column=0, padx=10, pady=10)

    registration_member_entry = tk.Entry(registration_form)
    registration_member_entry.grid(
        row=1, column=1, padx=10, pady=10
    )

    # Class ID
    tk.Label(
        registration_form,
        text="Class ID:"
    ).grid(row=2, column=0, padx=10, pady=10)

    registration_class_entry = tk.Entry(registration_form)
    registration_class_entry.grid(
        row=2, column=1, padx=10, pady=10
    )  

    def register_member():
        registration_id = registration_id_entry.get()
        member_id = registration_member_entry.get()
        class_id = registration_class_entry.get()

        # Make sure all IDs were entered
        if not registration_id or not member_id or not class_id:
            messagebox.showerror(
                "Missing Information",
                "Please enter a Registration ID, Member ID, and Class ID."
            )
            return

        # Make sure all IDs are numbers
        if not registration_id.isdigit() or not member_id.isdigit() or not class_id.isdigit():
            messagebox.showerror(
                "Invalid Information",
                "Registration ID, Member ID, and Class ID must be numbers."
            )
            return

        # Prevent duplicate registration IDs
        for registration in registrations:
            if registration.registration_id == int(registration_id):
                messagebox.showerror(
                    "Duplicate Registration",
                    "A registration with that ID already exists."
                )
                return

        # Find the member
        selected_member = None

        for member in members:
            if member.member_id == int(member_id):
                selected_member = member
                break

        if selected_member is None:
            messagebox.showerror(
                "Member Not Found",
                "No member was found with that ID."
            )
            return

        # Find the gym class
        selected_class = None

        for gym_class in gym_classes:
            if gym_class.class_id == int(class_id):
                selected_class = gym_class
                break

        if selected_class is None:
            messagebox.showerror(
                "Class Not Found",
                "No gym class was found with that ID."
            )
            return

        # Create the Registration object
        new_registration = Registration(
            int(registration_id),
            selected_member,
            selected_class
        )

        # Add registration to the class
        if selected_class.add_registration(new_registration):
            registrations.append(new_registration)

            messagebox.showinfo(
                "Registration Successful",
                f"{selected_member.name} was registered for "
                f"{selected_class.class_name}."
            )

            registration_id_entry.delete(0, tk.END)
            registration_member_entry.delete(0, tk.END)
            registration_class_entry.delete(0, tk.END)

        else:
            messagebox.showerror(
                "Class Full",
                "This class has reached its maximum capacity."
            )

    register_button = tk.Button(
        registration_window,
        text="Register Member",
        command=register_member,
        width=20
    )

    register_button.pack(pady=15)  

    def view_registrations():
        view_window = tk.Toplevel(registration_window)
        view_window.title("Registration List")
        view_window.geometry("550x350")

        tk.Label(
            view_window,
            text="Class Registrations",
            font=("Arial", 16)
        ).pack(pady=10)

        registration_table = ttk.Treeview(
            view_window,
            columns=("Registration ID", "Member", "Class"),
            show="headings"
        )

        registration_table.heading(
            "Registration ID",
            text="Registration ID"
        )
        registration_table.heading(
            "Member",
            text="Member"
        )
        registration_table.heading(
            "Class",
            text="Class"
        )

        registration_table.column(
            "Registration ID",
            width=120
        )
        registration_table.column(
            "Member",
            width=180
        )
        registration_table.column(
            "Class",
            width=180
        )

        # Display each registration
        for registration in registrations:
            registration_table.insert(
                "",
                tk.END,
                values=(
                    registration.registration_id,
                    registration.member.name,
                    registration.gym_class.class_name
                )
            )

        registration_table.pack(
            padx=10,
            pady=10,
            fill="both",
            expand=True
        )

    view_registration_button = tk.Button(
        registration_window,
        text="View Registrations",
        command=view_registrations,
        width=20
    )

    view_registration_button.pack(pady=5)


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

class_button = tk.Button(
    button_frame,
    text="Manage Classes",
    command=manage_classes,
    width=20
)

class_button.grid(
    row=3,
    column=0,
    columnspan=2,
    padx=5,
    pady=5
)

registration_button = tk.Button(
    button_frame,
    text="Class Registration",
    command=manage_registrations,
    width=20
)

registration_button.grid(
    row=4,
    column=0,
    columnspan=2,
    padx=5,
    pady=5
)


# Start the application
window.mainloop()
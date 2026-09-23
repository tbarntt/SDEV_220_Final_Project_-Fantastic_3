from member import Member

# List used to store gym members
members = []
# Dictionary of available membership types and descriptions
membership_types = {
    "Basic": "Gym access only",
    "Plus": "Gym access and group classes",
    "Premium": "Gym access, group classes, and personal training"
}

# Tuple of valid membership statuses
membership_statuses = ("Active", "Inactive", "Expired")


def add_member(member_id, name, email, membership_type, membership_status):
    if membership_type not in membership_types:
        print("Invalid membership type.")
        return None

    if membership_status not in membership_statuses:
        print("Invalid membership status.")
        return None

    new_member = Member(
        member_id,
        name,
        email,
        membership_type,
        membership_status
    )

    members.append(new_member)
    return new_member

def find_member(member_id):
    for member in members:
        if member.member_id == member_id:
            return member

    return None

def edit_member(member_id, name, email, membership_type, membership_status):
    member = find_member(member_id)

    if member:
        member.update_member(
            name,
            email,
            membership_type,
            membership_status
        )
        return True

    return False    


# Add sample members
add_member(1, "John Smith", "john@email.com", "Premium", "Active")
add_member(2, "Sarah Johnson", "sarah@email.com", "Basic", "Active")


# Display all members
for member in members:
    print(member)

found_member = find_member(2)

if found_member:
    print("Member found:")
    print(found_member)
else:
    print("Member not found.")    

print("\nUpdating member...")

updated = edit_member(
    2,
    "Sarah Johnson",
    "sarah.johnson@email.com",
    "Premium",
    "Active"
)

if updated:
    print("Member updated successfully.")
else:
    print("Member not found.")

print(find_member(2))    



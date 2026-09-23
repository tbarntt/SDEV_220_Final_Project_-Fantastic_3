class Member:
    def __init__(self, member_id, name, email, membership_type, membership_status):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.membership_type = membership_type
        self.membership_status = membership_status

    def update_member(self, name, email, membership_type, membership_status):
        self.name = name
        self.email = email
        self.membership_type = membership_type
        self.membership_status = membership_status

    def __str__(self):
        return f"{self.member_id}: {self.name} - {self.membership_type} ({self.membership_status})"
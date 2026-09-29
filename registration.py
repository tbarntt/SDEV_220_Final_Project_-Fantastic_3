class Registration:
    def __init__(self, registration_id, member, gym_class):
        self.registration_id = registration_id
        self.member = member
        self.gym_class = gym_class

    def __str__(self):
        return (f"Registration ID: {self.registration_id}, "
                f"Member: {self.member.name}, "
                f"Class: {self.gym_class.class_name}")

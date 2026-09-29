class GymClass:
    def __init__(self, class_id, class_name, instructor, capacity):
        self.class_id = class_id
        self.class_name = class_name
        self.instructor = instructor
        self.capacity = capacity
        self.registrations = []  # list of Registration objects

    def add_registration(self, registration):
        if len(self.registrations) < self.capacity:
            self.registrations.append(registration)
            return True
        return False

    def __str__(self):
        return (f"Class ID: {self.class_id}, Name: {self.class_name}, "
                f"Instructor: {self.instructor}, Capacity: {self.capacity}, "
                f"Registered: {len(self.registrations)}")

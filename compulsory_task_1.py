class Course:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def contact_details(self):
        print("For more information, please contact: example@example.com")

    def trainer_details(self):
        print("Trainer: Mr Anon A. Mouse")

    def show_course_id(self):
        print("Course ID: #12345")

    def head_office_location(self):
        print("Head Office Location: Cape Town")


class OOPCourse(Course):
    def __init__(self, title="OOP Fundamentals", duration=4, description="OOP Fundamentals", trainer="Mr Anon A. Mouse"):
        super().__init__(title, duration)
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        print(f"Course: {self.description}\nTrainer: {self.trainer}")

    def show_course_id(self):
        print("Course ID: #12345")


# Create an object of the subclass called course_1
course_1 = OOPCourse()

# Call the following methods
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
course_1.head_office_location()
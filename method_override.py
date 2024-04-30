class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        print(f"{self.name} is old enough to drive.")


class Child(Adult):
    def can_drive(self):
        print(f"{self.name} is too young to drive.")


def create_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    hair_colour = input("Enter hair colour: ")
    eye_colour = input("Enter eye colour: ")

    if age >= 18:
        person = Adult(name, age, hair_colour, eye_colour)
    else:
        person = Child(name, age, hair_colour, eye_colour)

    return person








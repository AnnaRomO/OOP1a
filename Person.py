class Person:
    def __init__(self, name, age, gender, email, occupation):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.occupation = occupation
        self.animals = []

    def print_attributes(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Email: {self.email}, Occupation: {self.occupation}")
        for animal in self.animals:
            animal.print_attributes()

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} added to {self.name}'s animals.")

    def remove_animal(self, animal_name):
        self.animals = [animal for animal in self.animals if animal.name != animal_name]
        print(f"{animal_name} removed from {self.name}'s animals.")

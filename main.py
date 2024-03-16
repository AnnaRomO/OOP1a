from Animal import Animal
from Person import Person

if __name__ == "__main__":
    # Create some Animal instances
    animal1 = Animal("Max", "Dog", 5, "Brown", "House")
    animal2 = Animal("Whiskers", "Cat", 3, "Black and White", "House")

    # Create a Person instance
    person = Person("John Doe", 35, "Male", "john.doe@example.com", "Software Developer")

    # Add animals to the person
    person.add_animal(animal1)
    person.add_animal(animal2)

    # Print person and animal attributes
    print(f"{person.name}'s animals:")
    person.print_attributes()

    # Remove an animal
    person.remove_animal("Max")

    # Print attributes again to confirm removal
    print(f"After removing Max:")
    person.print_attributes()

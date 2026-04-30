class Animal:
    def __init__(self, name, animal_species, number_of_legs):
        self.name = name
        self.animal_species = animal_species
        self.number_of_legs = number_of_legs

    def describe(self):
        message = f"name of animal : {self.name}, animal species : {self.animal_species}, number of legs : {self.number_of_legs}"
        return message

class Birds(Animal):
    def __init__(self, name, animal_species, number_of_legs, geography_place):
        Animal.__init__(self, name, animal_species, number_of_legs)
        self.geography = geography_place

    def describe(self):
        base = Animal.describe(self)
        message = base + f", geography place : {self.geography}"
        return message

class Cats(Animal):
    def __init__(self, name, animal_species, number_of_legs, type):
        Animal.__init__(self, name, animal_species, number_of_legs)
        self.type = type

    def describe(self):
        base = Animal.describe(self)
        message = base + f", type : {self.type}"
        return message

name_of_animal = input("Enter your animal: ")
animal_species = input("Enter the species of the animal: ")
number_of_legs = int(input("Enter the number of legs of the animal: "))

if name_of_animal == "cat":
    if number_of_legs == 4:
        type_of_cat = input("Enter the type of cat: ")
        result = Cats(name_of_animal, animal_species, number_of_legs, type_of_cat)
        print(result.describe())

elif name_of_animal == "bird":
    if number_of_legs == 2:
        geography = input("Enter geography of bird's place: ")
        result = Birds(name_of_animal, animal_species, number_of_legs, geography)
        print(result.describe())
class Gun:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        
    def describe(self):
        message = f"name of gun: {self.name}, model of gun: {self.model}"
        return message

class Handguns(Gun):
    def __init__(self, name, model, type_of_handgun):
        Gun.__init__(self, name, model)
        self.type_of_handgun = type_of_handgun

    def describe(self):
        base = Gun.describe(self)
        message = base + f", type of handgun: {self.type_of_handgun}"
        return message


class Shotgun(Gun):
    def __init__(self, name, model, type_of_shotgun):
        Gun.__init__(self, name, model)
        self.type_of_shotgun = type_of_shotgun

    def describe(self):
        base = Gun.describe(self)
        message = base + f", type of shotgun: {self.type_of_shotgun}"
        return message
name = input("Enter the gun name: ")
model_of_gun = input("Enter the gun model: ")
if name == "handgun":
    type_of_handgun = input("Enter the type of handgun: ")
    result = Handguns(name, model_of_gun, type_of_handgun)
    print(result.describe())

elif name == "shotgun":
    type_of_shotgun = input("Enter the type of shotgun: ")
    result = Shotgun(name, model_of_gun, type_of_shotgun)
    print(result.describe())

else:
    result = Gun(name, model_of_gun)
    print(result.describe())
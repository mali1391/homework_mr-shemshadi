class Formula:

    def __init__(self, name, parameters, relation, output_type):
        self.name = name
        self.parameters = parameters
        self.relation = relation
        self.output_type = output_type

    def describe(self):
        return f"formula: {self.name}, parameters: {self.parameters}, output_type: {self.output_type}"

    def calculate(self, **kwargs):
        result_of_calculate = self.relation(**kwargs)
        return result_of_calculate


class MathFormula(Formula):
    def __init__(self, name, parameters, relation, output_type, field="Math"):
        Formula.__init__(self, name, parameters, relation, output_type)
        self.field = field

    def describe(self):
        base = Formula.describe(self)
        message = base + f" ,field: {self.field}"
        return message


class PhysicsFormula(Formula):
    def __init__(self, name, parameters, relation, output_type, unit="joules"):
        Formula.__init__(self, name, parameters, relation, output_type)
        self.unit = unit

    def describe(self):
        base = Formula.describe(self)
        message = base + f", unit: {self.unit}"
        return message


class ChemistryFormula(Formula):
    def __init__(self, name, parameters, relation, output_type, category="solutions"):
        Formula.__init__(self, name, parameters, relation, output_type)
        self.category = category

    def describe(self):
        base = Formula.describe(self)
        message = base + f", category: {self.category}"
        return message


object = input("Enter your object:")
if object == "math":
    first_number = int(input("Enter your number:"))
    name_of_formula = "sqr"
    output_type = input("Enter your output type:")
    if output_type == "int":
        parameters_of_formula = "height"
        relation = lambda height: height * height

        sqr = MathFormula(name_of_formula, parameters_of_formula, relation, output_type)
        print(sqr.describe())
        print(("result:", sqr.calculate(height=first_number)))
elif object == "physics":
    mass = int(input("Enter your mass:"))
    velocity = int(input("Enter your velocity:"))
    name_of_formula = "kinetic energy"
    output_type = input("Enter your output type:")
    if output_type == "int":
        parameters_of_formula = "mass", "velocity"
        relation = lambda mass, velocity: 0.5 * mass * velocity * velocity

    kinetic_energy = PhysicsFormula(name_of_formula, parameters_of_formula, relation, output_type)
    print(kinetic_energy.describe)
    print("result:", kinetic_energy.calculate(mass=mass, velocity=velocity))

elif object == "chemistry":
    mol = int(input("Enter Molarity:"))
    volume = int(input("Enter Volume:"))
    name_of_formula = "molarity"
    output_type = input("Enter your output type:")
    if output_type == "int":
        parameters_of_formula = "mol", "volume"
        relation = lambda mol, volume: mol / volume

    Molarity = ChemistryFormula(name_of_formula, parameters_of_formula, relation, output_type)
    print(Molarity.describe())
    print("result:", Molarity.calculate(mol=mol, volume=volume))

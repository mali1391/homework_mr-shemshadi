class Formula:
    def __init__(self, number_of_parameters, mathematical_relationships_between_the_parameters, formula_name, type_of_output):

        self.number_of_parameters = number_of_parameters
        self.mathematical_relationships_between_the_parameters = mathematical_relationships_between_the_parameters
        self.Formula_name = formula_name
        self.Type_of_output = type_of_output

class Math_formula(Formula):
    def __init__(self, number_of_parameters, mathematical_relationships_between_the_parameters, formula_name, type_of_output, triangular_pattern):
        Formula.__init__(number_of_parameters, mathematical_relationships_between_the_parameters, formula_name, type_of_output)
        self.triangular_pattern = triangular_pattern

    def triangular_pattern(self):
        if self.number_of_parameters > 0:



# number = int(input("Enter the number of parameters: "))
#
# formula_name = input("Enter the formula name: ")
#
# formula = Formula(number, 5, 4, 7 )
#
# Formula.parameters()
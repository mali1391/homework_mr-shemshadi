class Formula:
    def __init__(self, Number_of_parameters, Mathematical_relationships_between_the_parameters, Formula_name, Type_of_output):

        self.number_of_parameters = Number_of_parameters
        self.mathematical_relationships_between_the_parameters = Mathematical_relationships_between_the_parameters
        self.Formula_name = Formula_name
        self.Type_of_output = Type_of_output

    def parameters(self):
        if self.number_of_parameters:
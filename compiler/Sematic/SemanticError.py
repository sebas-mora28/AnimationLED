

class SemanticError:

    def __init__(self):
        self.errors = []

    def printErrors(self):

        for i in range(len(self.errors)):
            print(self.errors[i])

    def main_not_found(self):
        self.errors.append("Semantic error: Main not found")

    def main_cannot_receive_parameters(self):
        self.errors.append("Semantic error: Main cannot receive parameters")


    def main_multiple_definitions(self):
        self.errors.append("Semantic error: Main multiple definitions")


    def symbol_procedure_not_found(self, ID):
        self.errors.append(f"Semantic error: Procedure {ID} not found")


    def call_procedure_error(self, ID):
        self.errors.append(f"Semantic error: {ID} is not a procedure")

    
    def multiple_variable_declaration(self):
        self.errors.append(f"Semantic error: Invalidad multiple variable declaration")

    def incompatible_ariable_type(self, ID):
        self.errors.append(f"Semantic error: Incompatible type in variable {ID}")


    def number_of_arguments_not_match(self , ID):
        self.errors.append(f"Semantic error: Does not match number of parameters and arguments in {ID} procedure")
        
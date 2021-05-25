

class SemanticError:

    def __init__(self):
        self.errors = []

    

    def main_not_found(self):
        self.errors.append("Semantic error: Main not found")

    def main_cannot_receive_parameters(self):
        self.errors.append("Semantic error: Main cannot receive parameters")


    def main_multiple_definitions(self):
        self.errors.append("Semantic error: Main multiple definitions")
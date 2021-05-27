

class SemanticError:

    def __init__(self):
        self.errors = []

    def printErrors(self):

        for i in range(len(self.errors)):
            print(self.errors[i])


    def addError(self, error):
        self.errors.append(error)

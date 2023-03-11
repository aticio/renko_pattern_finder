

class RenkoPatternFinder:
    def __init__(self, data):
        self.data = data

    def check_patterns(self):
        self.check_one_back()

    def check_one_back(self):
        print(self.data)
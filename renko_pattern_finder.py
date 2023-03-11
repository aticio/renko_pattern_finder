

class RenkoPatternFinder:
    def __init__(self, data):
        self.data = data

    def check_patterns(self):
        self.check_bullish_one_back()

    def check_bullish_one_back(self):
        if self.data[-1]["type"] == "up" and self.data[-2]["type"] == "up" and self.data[-3]["type"] == "down" and self.data[-4]["type"] == "up" and self.data[-5]["type"] == "up":
            print("found")
        else:
            print("not found")

    def check_bearish_one_back(self):
        if self.data[-1]["type"] == "down" and self.data[-2]["type"] == "down" and self.data[-3]["type"] == "up" and self.data[-4]["type"] == "down" and self.data[-5]["type"] == "down":
            print("found")
        else:
            print("not found")

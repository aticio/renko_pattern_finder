

class RenkoPatternFinder:
    def __init__(self, data):
        self.data = data

    def check_patterns(self):
        if self.check_bullish_one_back():
            print("Bullish one back found")
        elif self.check_bearish_one_back():
            print("Bearish one back found")
        elif self.check_bullish_zig_zag():
            print("Bullish zig zag found")
        elif self.check_bearish_zig_zag():
            print("Bearish zig zag found")
        else:
            print("No patterns found")

    def check_bullish_one_back(self):
        if (
                self.data[-1]["type"] == "up" and
                self.data[-2]["type"] == "up" and
                self.data[-3]["type"] == "down" and
                self.data[-4]["type"] == "up" and
                self.data[-5]["type"] == "up"):
            return True
        else:
            return False

    def check_bearish_one_back(self):
        if (
                self.data[-1]["type"] == "down"
                and self.data[-2]["type"] == "down"
                and self.data[-3]["type"] == "up"
                and self.data[-4]["type"] == "down"
                and self.data[-5]["type"] == "down"):
            return True
        else:
            return False

    def check_bullish_zig_zag(self):
        if (
                self.data[-1]["type"] == "up" and
                self.data[-2]["type"] == "up" and
                self.data[-3]["type"] == "down" and
                self.data[-4]["type"] == "up" and
                self.data[-5]["type"] == "down"):
            return True
        else:
            return False

    def check_bearish_zig_zag(self):
        if (
                self.data[-1]["type"] == "down" and
                self.data[-2]["type"] == "down" and
                self.data[-3]["type"] == "up" and
                self.data[-4]["type"] == "down" and
                self.data[-5]["type"] == "up"):
            return True
        else:
            return False

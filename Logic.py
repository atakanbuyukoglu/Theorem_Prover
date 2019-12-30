
class Condition:

    def __init__(self, comparator, value):
        self.comparator = comparator
        self.value = value

    def check(self, item):
        if eval(str(item) + self.comparator + str(self.value)):
            return True
        return False

    def __str__(self):
        result = 'x ' + self.comparator + ' ' + str(self.value)
        return result
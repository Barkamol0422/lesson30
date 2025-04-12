class Vehicle:
    def __init__(self, n, c):
        self.n = n
        self.c = c
    def fare(self):
        return self.c * 100
class Bus(Vehicle):
    def fare(self):
        return super().fare() * 2
b = Bus("City", 50)
print(b.fare())

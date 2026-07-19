class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Vehicle: {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def display_info(self):
        parent_info = super().display_info()
        return f"{parent_info} with {self.doors} doors"

my_car = Car("Tesla", "Model 3", 4)
print(my_car.display_info())

print(f"Is Car a subclass of Vehicle? {issubclass(Car, Vehicle)}")
# 1) Create a class named `Vehicle`.

# 2) Define the constructor method `__init__(self, name, max_speed, mileage)`:

# a) Take inputs `name`, `max_speed`, and `mileage`.

# b) Store them as instance variables:

# - `self.name = name`

# - `self.max_speed = max_speed`

# - `self.mileage = mileage`

# 3) Create a class named `Bus` that inherits from the `Vehicle` class:

# a) Use `class Bus(Vehicle):`

# b) Use `pass` because no extra properties or methods are added.

# (Bus automatically gets all features of Vehicle through inheritance.)

# 4) Create an object `School_bus` of the `Bus` class by passing:

# a) name = "School Volvo"

# b) max_speed = 180

# c) mileage = 12

# 5) Print the details of `School_bus` by accessing inherited instance variables:

# a) Print the vehicle name.

# b) Print the max speed.

# c) Print the mileage
class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=(name)
        self.max_speed=(max_speed)
        self.mileage=(mileage)
class bus(vehicle):
    pass
school_bus=bus("school volvo",180,12)
print("details of school bus is:",school_bus.name,school_bus.max_speed,school_bus.mileage)

    


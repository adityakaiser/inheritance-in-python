# 1) Create a parent class named `Person`.

# 2) Inside `Person`, define the constructor `__init__(self, name, idnumber)`:

# a) Store the given `name` in `self.name`.

# b) Store the given `idnumber` in `self.idnumber`.

# 3) Define a method `display(self)` in `Person`:

# a) Print the person's name.

# b) Print the person's id number.

# 4) Create a child class named `Employee` that inherits from `Person`.

# 5) Inside `Employee`, define the constructor

# `__init__(self, name, idnumber, salary, post)`:

# a) Store `salary` in `self.salary`.

# b) Store `post` in `self.post`.

# c) Call the parent class constructor `Person.__init__(self, name, idnumber)`

# to initialize the inherited variables `name` and `idnumber`.

# 6) Create an object `a` of the `Employee` class by passing:

# a) name = 'Rahul'

# b) idnumber = 886012

# c) salary = 200000

# d) post = "Intern"

# 7) Call the method `display()` using the object `a`.

# (This method belongs to the parent class `Person`, but is accessible through inheritance.
class person:
    def __init__(self,name,idnumber):
        self.name=(name)
        self.idnumber=(idnumber)
    def display(self):
        print("name:",self.name)
        print("id:",self.idnumber)
class employee(person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=(salary)
        self.post=(post)
        super().__init__(name,idnumber)  
a=employee("Rahul",886012,200000,"intern")
a.display()      
    
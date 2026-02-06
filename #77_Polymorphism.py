#77 Python Polymorphism
class Vehicle:
    def __init__(self,Model,Brand,Component):
        self.Model = Model
        self.Brand = Brand
        self.Component = Component
class Plane(Vehicle):
    pass
class Car(Vehicle):
    pass
class
p1 = Plane("Hablu420","Hablu","All Component")
c1 = Car("BMW","E221","Main Component")
b1 = Bike("")
print(p1.Brand,p1.Model,p1.Component)
print(c1.Model,c1.Brand,c1.Component)


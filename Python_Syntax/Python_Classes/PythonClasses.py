#__________________________________________________________________
# Accessing protected member variables


class Circle:
    pi = 3.14
    def __init__(self, radius=0):   
        self._radius = radius       # protectted variable: _  symbol

    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius

    def displayRadius(self):      
        return self.radius

    def circumference(self):
        return self.radius * self.pi * 2
    
    def area(self):
        return self.radius * self.radius * self.pi

print("\n")
c = Circle()
c.setRadius(4)
print('Radius is: ', c.displayRadius())
print('Circumference is: ', c.circumference())
print('Area is: ', c.area())
print("\n")

#__________________________________________________________________

import math 

class formulas: 
    def __init__(self, a=0, b=0, c=0):  # a=0 = positional arguments required
        self._a = a                     # _protected arguments 
        self._b = b
        self._c = c
    
    def setPositions(self, new_a, new_b, new_c):    # not munipulating the arguments/variables directly
        self.a = new_a  
        self.b = new_b
        self.c = new_c

    def calQuadratic(self):
        discriminant = self.b*self.b - 4**self.c
        if discriminant > 0:
            x1 = (-self.b + math.sqrt(discriminant)) / (2*self.a)
            x2 = (-self.b - math.sqrt(discriminant)) / (2*self.a)
            print("Roots are real and different: ")
            print("x1 = ", x1)
            print("x2 = ", x2)
        elif discriminant == 0:
            x1 = -self.b/(2*self.a)
            print("Roots are real and same: ")
            print("x1 = x2 = ", x1)
        else:
            realPart = -self.b/(2*self.a)
            imaginaryPart = math.sqrt(-discriminant)/(2*self.a)
            print("Roots are complex and different: ")
            print("x1 = ", realPart, "+", imaginaryPart, "i")
            print("x2 = ", realPart, "-", imaginaryPart, "i")

f = formulas()
f.setPositions(1,2,3)
f.calQuadratic()
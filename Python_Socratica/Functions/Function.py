import math

def volume(r):
    """ Retuns the valume of a sphere with radius r. """
    v = (4.0 / 3.0) * math.pi * r**3 
    return v

vol = volume(2)
print("Volume: ",vol)

def triangle_area(b, h):
    """ Returns the area of a triangle with a base b and height h. """
    return 0.5 * b * h

tri = triangle_area(3, 6)
print("Triangle area: ", tri)

#____________________

def cm(feet = 0, inches = 0):
    """Coverts a length from feet and inches to centimeters """
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm
#____________________
# kwarg - keyword arguments or default argumenmts must be defined last 


print("Feet: ", cm(feet = 5))
print("Inches: ", cm(inches = 70))
print("Feet and inches: ", cm(inches = 8, feet = 5))








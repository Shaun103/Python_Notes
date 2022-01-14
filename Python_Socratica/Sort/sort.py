#______________Table Contents________________

# Sort method - changes the original
# Sorting by density 
# Sorting by density 
# Sorted method - returns a copy 
# Sorted on a tuple
# Sorted strings

#______________Table Contents________________

earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]

# _____________________________________

# Sort method

print(help(list.sort))  # displays sort documentation ## changes the list itself

earth_metals.sort()    
print(earth_metals)

earth_metals.sort(reverse=True)
print(earth_metals)   

# _____________________________________________________________________

    # # Format : = name, radius, density, distance from Sun
    # # Radius at equator in kilometers
    # # Density: average density in g / cm3
    # # Distance: from Sun: Avg. distance to sun in AUs
    # # 1 Astronomical unit = Average distance of Earth to Sun

planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.723),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
]

# _____________________________________________________________________

# Sorting planets by size 

size = lambda planet: planet[1]        # grabs the 2 item (Radius) in list 
planets.sort(key=size, reverse = True) # reverse order  
print(planets)

# _____________________________________________________________________

# Sorting by density 

density = lambda planet: planet[2]      # grabs 3 item (Density) in list 
planets.sort(key=density)
print(planets)

# _____________________________________________________________________

# # Sorted method
# # Creates a copy to sorts 

print(help(sorted))                         # sorted(iterable, key=None, reverse=False)

sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals)                  # sorted
print(earth_metals)                         # Original not changed


# _____________________________________________________________________

# # Sorting on a tuple
# # Sorted function returns a list

data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)          
print(sorted(data))                 
print(data)

#_____________________________________

# # Sorted strings 

print(sorted('Alphabetical'))
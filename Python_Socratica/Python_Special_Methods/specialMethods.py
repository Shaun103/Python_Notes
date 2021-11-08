class Snowflake1:
    pass

# _______________________________________________________________________

class Snowflake2:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        print(f">>> You set {name} = {value}")
        self.__dict__[name] = value

# _______________________________________________________________________        

class Martian:
    """Someone who lives on Mars."""

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def __setattr__(self, name, value):
        print(f">>> You set {name} = {value}")
        self.__dict__[name] = value

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def __getattr__(self, name):
        print(f">>> Get the '{name}' attribute")
        if name == 'full_name':
            return f"{self.first_name} {self.last_name}"
        else:
            raise AttributeError(f"No Attribute named {name}")

    def __lt__(self, rhs):
        # print(f">>> Comparing {self} with {rhs}")
        if self.last_name != rhs.last_name:
            return (self.last_name < rhs.last_name)
        else:
            return (self.first_name < rhs.first_name)

# _______________________________________________________________________

# flake = Snowflake1() 
# print(dir(flake)) # displaying special methods

# _______________________________________________________________________

# m1 = Snowflake2("Own", "Phelps")

# print(m1.__dict__)

# print(m1)



# _______________________________________________________________________

# m1 = Martian('Rob', 'Schenk')
# m1.arrival_data = '2037-12-15'

# print(Martian.__doc__) # prints documentation

# print(m1.__dict__) 



# _______________________________________________________________________

# m = Martian('Klaus', "Iserlohn")
# print(m)
# print(m.__dict__)



# _______________________________________________________________________

m = Martian('Pierre', 'Aberg')
print(f"First name = {m.first_name}")
print(f"Last name = {m.last_name}")
print(m.full_name)
# print(m.martian_name) # raises attribute error
print(m.__dict__)



# _______________________________________________________________________

# m = Martian("Rod","Morley")
# print(m)

# m1 = Martian("Prayash", "Mohapatra")

# print(m1)
# print(m1.__str__())
# print(id(m1))



# _______________________________________________________________________

# m1 = Martian("Cyrille","Collin")
# m2 = Martian("Len","Klein")
# m3 = Martian("Matthias","Stein")
# m4 = Martian("Mike","Lenox")
# m5 = Martian("Bob","Hillier")
# m6 = Martian("Olwyn","Meek")
# m7 = Martian("Andy","Taylor")
# m8 = Martian("Halbert","Stone")
# m9 = Martian("Marvin","Meek")

# martians = [m1, m2, m3, m4, m5, m6, m7, m8, m9]
# martians.sort()

# for m in martians:
#     print(m)
# __________________Table Contents________________

# Creating the class
# User1 first name last name
# User2 first name last name
# Creating age and book
# Creating class variables
# Extracting first name last name
# Putting everyting together 

# __________________Table Contents________________


# # Creating a class

class User:
    pass

#__________________________
# # User1 first name last name

user1 = User()      # user1 object

user1.first_name = "Dave"
user1.last_name = "Bowman"

# print(user1.first_name)
# print(user1.last_name)


first_name = "Arthur"
last_name = "Clarke"

# print(first_name)
# print(last_name)

#__________________________
# # User2 first name last name

user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

# print(first_name, last_name)
# print(user1.first_name, user1.last_name)
# print(user2.first_name, user2.last_name)

#__________________________
# # Creating age and book

user1.age = 37
user2.favorite_book = "2001: A Space Odyssey"

# print(user1.age)

#__________________________
# # Creating class variables

class User:
    def __init__(self, full_name, birthday) -> None:
        self.name = full_name
        self.birthday = birthday        # yyyy mm dd format

user = User("Dave Bowman", "19710315")

# print(user.name)
# print(user.birthday)

#__________________________
# # Extracting first name last name
 
class User:
    """A member of Friend. For now we are only storing their name and birthday.
        But Soon we will store an uncomfortable amount of user information."""

    def __init__(self, full_name, birthday) -> None:
        self.name = full_name
        self.birthday = birthday        # yyyy mm dd format
        
        # Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

user = User("Dave Bowman", "19710315")
# print(user.first_name)
# print(user.last_name)
# print(user.birthday)

# print(help(User)) # Prints the doc string as a summary

#__________________________
# # Extracting
# # Putting everyting together 

import datetime 

class User:
    """A member of Friend. For now we are only storing their name and birthday.
        But Soon we will store an uncomfortable amount of user information."""

    def __init__(self, full_name, birthday) -> None:
        self.name = full_name
        self.birthday = birthday        # Assume yyyy mm dd format
        
        # Extract first and last name
        name_pieces = full_name.split(" ")  # splits the name on white space
        self.first_name = name_pieces[0]    # grabs first string
        self.last_name = name_pieces[-1]    # grabs last string

    def age(self):
        """Return the age of the user in years."""

        today = datetime.date(2021, 4, 13)
        yyyy = int(self.birthday[0:4])      # 1st - 4th
        mm = int(self.birthday[4:6])        # 4th - 6th
        dd = int(self.birthday[6:8])        # 6th - 8th
        dob = datetime.date(yyyy, mm, dd)   # Date of birth 
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        
        return int(age_in_years)

user = User("Dave Bowman", "19710315")  # Passing a name into the class

print(user.age())
print(user.first_name)
print(user.last_name)
print(user.birthday)
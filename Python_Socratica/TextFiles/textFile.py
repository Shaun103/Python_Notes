# ______________Table Contents______________ #

# Method dealing with text
# Safer way of dealing with text
# Reading file that does not exist 
# Writting to a file 
# Writting to a file 2 - best way 
# Appending to a file 

# ______________Table Contents______________ #

from typing import Text

path = '/Users/User/Desktop/Python/Python_Socratica/TextFiles/guido_bio.txt'
path2 = 'no_file.txt'
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

# ____________________________________ #

# print(help(open))    

# ____________________________________ #

# Inefficient method of opening files #

# Method dealing with text

f = open(path)
text = f.read()
f.close

print(text)

# ____________________________________ #

# Safer way of dealing with text 

with open(path) as fobj:
    bio = fobj.read()
print(bio)

# ____________________________________ #

# Reading file that does not exist 

try: 
    with open(path2) as f:
        text = f.read()
except FileNotFoundError:
    text = None
print(text)

# ____________________________________ #

# Writting to a file  
# python will automatically close the file when done

with open("oceans.txt", "w") as f:
    for ocean in oceans:
        f.write(ocean)
        f.write("\n")

# ____________________________________ #

# Writting to a file 2 - best way 

with open("oceans.txt", "w") as f:
    for ocean in oceans:
        print(ocean, file=f)

# ____________________________________ #

# Appending to a file 
# writting to a file with out over writing data 

with open("oceans.txt", "a") as f:
    print(23*"=", file=f)
    print("These are the 5 oceans.", file=f)
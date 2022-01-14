from os import walk
import glob

print(glob.glob("/Users/User/Desktop/Mjolnir"))


f = []
for (dirpath, dirnames, filenames) in walk('/Users/User/Desktop/Mjolnir'):
    f.extend(filenames)
    break

print(f)
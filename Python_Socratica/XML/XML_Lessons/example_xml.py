#________________________________________
# https://docs.python.org/
#________________________________________

import xml.etree.ElementTree as ET
from inspect import getmembers, isclass, isfunction

# print(dir(ET))          # lists the classes and functions

#_________________________________
# python inspect module 

# Display classes in ET module
print("Classes:")
for (name, member) in getmembers(ET, isclass):
    if not name.startswith("_"):
        print(name)

#_________________________________
print("\n")
#_________________________________

# Display functions in ET module
print("Functions: ")
for (name, member) in getmembers(ET, isfunction):
    if not name.startswith("_"):
        print(name)


#_________________________________
# listed important items
#_________________________________

# # fromstring - ET.fromstring(String) --> Element      - takes xml data and returns xml objects
# # parse - ET.parse(File) --> ElementTree              - open an xml file and return it as element tree object
# # tostring - ET.tostring(Element) --> String          - inverse of the from string function

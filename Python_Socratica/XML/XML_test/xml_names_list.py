import xml.etree.ElementTree as ET

# creates list of names to be added
array = []
for i in range(3):
    array.append(input("Enter string: "))

# Creates the xml document
tree = ET.parse("hodlers.xml")
root = tree.getroot()

# takes names from list sets into brackets 
for name in range(len(array)):
    # print(array[name])
    investor2 = ET.Element("investor")
    investor2.text = array[name]
    root.append(investor2)

for (id, investor) in enumerate(root.findall('investor')):  # numbers 'id'
    investor.set('id', str(id))

tree.write('hodlers.xml')
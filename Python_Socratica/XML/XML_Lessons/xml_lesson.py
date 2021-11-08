#________________________________________
# https://docs.python.org/
#________________________________________



import xml.etree.ElementTree as ET

tree = ET.parse("hodlers.xml")  # opens the file, parse returns element tree object
root = tree.getroot()           
print(ET.tostring(root))        # 

# includes all child elements 
# including white space

#________________________________________

# displaying the value of 'coin', root.get() method

tree = ET.parse("hodlers.xml")
root = tree.getroot()

# Get 'coin' attribute
coin = root.get('coin') # manipulating <crypto></crypto>                    
print("Crypto name = {val}".format(val=coin))

#________________________________________

tree = ET.parse("hodlers.xml")
root = tree.getroot()

# Set 'launched' attribute
root.set('launched', '20210101')    # manipulating <crypto></crypto>

tree.write('hodlers.xml')
print(root.attrib)

#________________________________________

tree = ET.parse("hodlers.xml")
root = tree.getroot()

id = 0

for investor in tree.findall('investor'):
    investor.set('id', str(id))
    id += 1

# Save XML
tree.write('hodlers.xml')

#________________________________________

# Deletes the 'id' numbers

tree = ET.parse("hodlers.xml")
root = tree.getroot()

# Delete 'id' attributes 
for investor in tree.findall('investor'):
    del(investor.attrib['id']) # deletes numbers 

# Save XML changes
tree.write('hodlers.xml')

#________________________________________

# # Adding two investors (differently)

tree = ET.parse("hodlers.xml")
root = tree.getroot()

# Method 1 Add investor #1
investor1 = ET.fromstring("<investor>Allen Duffy</investor>")
root.append(investor1)

# # Method 2 Add investor #2
investor2 = ET.Element("investor")
investor2.text = "Karl Amber"
root.append(investor2)

# Save XML
tree.write('hodlers.xml')

#________________________________________

# Adding 'id' numbers starting from 0

tree = ET.parse("hodlers.xml")
root = tree.getroot()

# Add ids once more
for (id, investor) in enumerate(root.findall('investor')):
    investor.set('id', str(id))

# Save XML
tree.write('hodlers.xml')

# #________________________________________

# grabing the investor name at 'id' 4

tree = ET.parse("hodlers.xml")
root = tree.getroot()

# Select investor 4
investor = root.find(".//investor[@id='4']")
print(investor.text)

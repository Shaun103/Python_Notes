
# Firstly we have to import 'xml.etree.ElementTree' for creating a subtree
import xml.etree.ElementTree as ET

anime_list = ["Akira", "Ghost in the Shell", "Gundam Wing", "Yu Yu Hakusho", "Dragon Ball Z"]
  
def create_xml():
  
        # we make root element
        anime = ET.Element("anime")
  
        # create sub element
        anime = ET.SubElement(anime, "anime")
  
        # insert list element into sub elements
        for user in range(len(anime_list)):
  
                usr = ET.SubElement(anime, "title")
                usr.text = str(anime_list[user])
  
        tree = ET.ElementTree(anime)
        
        indent(anime, level=0)
  
        # write the tree into an XML file
        tree.write("animeTitles.xml", encoding ='utf-8')

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i
create_xml()

tree = ET.parse("animeTitles.xml")
root = tree.getroot()

id = 0

for title in tree.findall('title'):
    title.set('id', str(id))
    id += 1

tree.write('animeTitles.xml')
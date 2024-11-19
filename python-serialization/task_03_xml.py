import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("root")
    root.tag = 'data'

    for key, value in dictionary:
        child = ET.SubElement(root, "child")
        child.set(key, value)
    
    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    root = ET.Element("root")
    root.tag = 'data'

    for key, value in dictionary.items():
        child = ET.SubElement(root, "child")
        child.set(key, key)
        child.text = str(value)
    
    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        tree.write(file, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    pass
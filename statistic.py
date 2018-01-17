import xml.etree.ElementTree as ET
import os
from shutil import copyfile
#   filename
#   folder
#   object
#       name
#       delete 0
#       attributes
#       polygon

object_name = ['board', 'window', 'door', 'crack', 'broken']
att_name = ['']
damage_name = []

count = {}

PATH = "/Users/kidio/dataset/annotations/window/"

output = "./danh_dau_sai.txt"



def categorize(count, name, value):
    if name not in count:
        count[name] = 1
    else:
        count[name] += 1
    return count


with open(output, mode='w', encoding='utf-8') as wr:
    for xml_folder in os.listdir(PATH):
        xml_folder = os.path.join(PATH, xml_folder)
        for f in os.listdir(xml_folder):
            if 'xml' in f:
                categorize(count, 'xml', 'xml')
                xml_file = os.path.join(xml_folder, f)
                tree = ET.parse(xml_file)
                root = tree.getroot()

                Wrong = False
                text = "===================\n"
                filename = root.find('filename').text
                folder = root.find('folder').text
                text += "file: " + filename + "\n"
                text += "folder: " + folder + "\n"
                for obj in root.iter('object'):
                    if obj.find('deleted').text == '0':
                        name = obj.find('name').text
                        count = categorize(count, name, name)
                        if name == "broken":
                            print(filename)

                        if name.strip() not in object_name + damage_name:
                            Wrong = True
                            text += "\tSai ten: " + name + "\n"
                        if name in damage_name:
                            count = categorize(count, name, name)
                        if name in object_name:
                            attributes = str(obj.find('attributes').text).split(",")
                            for a in attributes:
                                a = a.strip()
                                count = categorize(count, a, a)

                                if a != 'None' and a not in att_name:
                                    text += "\t Sai thuoc tinh: " + a + "\n"
                                    Wrong = True
                #if Wrong:
                    # print(text)
                    # wr.write(text)

wr.close()

print(count)

import os
import argparse

parser = argparse.ArgumentParser(description="divide dataset into smaller chunk for annotation")
parser.add_argument("--dir", help='input folder')
parser.add_argument("--prefix", help="prefix for subfolder")

args = parser.parse_args()

PATH = args.dir 
PARENT = os.path.dirname(PATH)


PREFIX = args.prefix 

count = 0
folder_index = 1
folder = ""
for img in os.listdir(PATH):
    if count % 200 == 0:
        folder_index += 1
        folder = os.path.join(PATH, PREFIX + str(int(count/200)))
        os.mkdir(folder)
    os.rename(os.path.join(PATH, img), os.path.join(folder, img))
    count += 1

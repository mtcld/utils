import os

# Build maps
labelled_map = {}
LABELLED = "/Users/kidio/git/bagiks/CMT-Text-Detection/dataset/temp/labelled"
for f in os.listdir(LABELLED):
    for i in os.listdir(os.path.join(LABELLED, f)):
        labelled_map[i.split(".")[0]] = f

print  labelled_map



# move file

DIGITS = "/Volumes/Data/WORKSPACE/git/bagiks/CMT-Text-Detection/dataset/temp/digits"
for f in os.listdir(DIGITS):
    folder = os.path.join(DIGITS, f)
    for i in os.listdir(folder):
        prefix = i.split("+")[0]
        if prefix in labelled_map:
            os.rename(os.path.join(folder, i), os.path.join(os.path.join(LABELLED, labelled_map[prefix]), i))



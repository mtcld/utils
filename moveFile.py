import os

PATH = "/Users/kidio/Downloads/cracked_gg"

if os.path.exists(PATH):
    files = os.listdir(PATH)
    for m in files:

        CHILD = os.path.join(PATH, m)
        if os.path.isdir(CHILD):
            for i in os.listdir(CHILD):
                if "DS_Store" not in i:
                    os.rename(os.path.join(CHILD, i), os.path.join(CHILD, m + "_" + i + ".jpg"))

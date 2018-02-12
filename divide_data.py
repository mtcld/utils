import os
PATH = "/Users/kidio/git/motionscloud/allstate/dataset/"
TRAIN = 'train'
VAL = 'val'
ANN = "annotations"
IMG = "img"
j=0
imgs_name = []
for img_name in os.listdir(PATH+ "/train/" + ANN):
    imgs_name.append(img_name.split('.')[0])


print (imgs_name)
from sklearn.model_selection import train_test_split
X = imgs_name
y = range(0, len(X))
X_trn, X_tst, y_trn, y_tst = train_test_split(X, y, test_size=0.2, random_state=42)

for name in X_tst:
    print (name)
    os.rename(os.path.join(PATH, TRAIN, ANN, name + ".xml"), os.path.join(PATH, VAL, ANN, name + ".xml"))
    os.rename(os.path.join(PATH, TRAIN, IMG, name + ".jpg"), os.path.join(PATH, VAL, IMG, name + ".jpg"))
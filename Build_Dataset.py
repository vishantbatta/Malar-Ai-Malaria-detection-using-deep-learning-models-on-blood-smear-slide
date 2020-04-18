####### pickle part is still missing. "###" means u should change values here .
################ WARNING line 35-49 contains extra varible added pls checknif you need them
import numpy as np
import os
import cv2
import matplotlib.pyplot as plt #this for verification of code if u need somewhere.
training_data =[]
DATADIR = r"C:\Users\hp\Desktop\MALAR-AI\cell_images\Parasitized"       ###enter location of images in ur PC here
path = os.path.join(DATADIR)
for img in os.listdir(path):
    try:
        img_array = cv2.imread(os.path.join(path, img),cv2.IMREAD_COLOR)
        img_array=img_array/255
        training_data.append([img_array,"Parasitized"])
    except Exception as e:
        pass
DATADIR = r"C:\Users\hp\Desktop\MALAR-AI\cell_images\Uninfected"       ###enter location of images in ur PC here
path = os.path.join(DATADIR)
for img in os.listdir(path):
    try:
        img_array = cv2.imread(os.path.join(path, img),cv2.IMREAD_COLOR)
        img_array=img_array/255
        training_data.append([img_array,"non-parasitised"])
    except Exception as e:
       pass
#shufling the DATA
import random
random.shuffle(training_data)
#breaking data for difrnt tasks
Testing_images = training_data[:9186]          ### we have total 27,558 images in training data. 13779 of each category.
Training_images = training_data[9186:-9186]    ### so 27,558/3 is 9186.
Validation_images = training_data[9186:]
########################################## my part might be ended.############## ps. pickel is still remainig################
#defining few variables just in case you forgot
X_Testing_images =[]
y_Testing_images =[]
for features, labels in Testing_images:
    X_Testing_images.append(features)
    y_Testing_images.append(labels)
X_Training_images =[]
y_Training_images =[]
for features, labels in Training_images:
    X_Training_images.append(features)
    y_Training_images.append(labels)
X_Validation_images =[]
y_Validation_images =[]
for features, labels in training_data:
    X_Validation_images.append(features)
    y_Validation_images.append(labels)
############## PICKEL CODE ctrl C + ctrl V from internet#########
##Let's save this data, so that we don't need to keep calculating it every time we want to play with the neural network model:

#import pickle

#pickle_out = open("X.pickle","wb")
#pickle.dump(X, pickle_out)
#pickle_out.close()

#pickle_out = open("y.pickle","wb")
#pickle.dump(y, pickle_out)
#pickle_out.close()

##We can always load it in to our current script, or a totally new one by doing:

#pickle_in = open("X.pickle","rb")
#X = pickle.load(pickle_in)
#pickle_in = open("y.pickle","rb")
#y = pickle.load(pickle_in)

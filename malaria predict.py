import os
import silence_tensorflow.auto #silence warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #silence warnings further
from keras.models import load_model
import argparse
import cv2
import numpy as np



ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])


img=cv2.resize(img,(224,224))
img=img/255.0

testimg=np.expand_dims(img,axis=0)
model=load_model("model3-054.h5")
pred=model.predict(testimg)
pred_class =np.argmax(pred,axis=1)
labels={0:'Parasitized',1:'Uninfected'}
prob=pred[0][pred_class[0]]*100
print(labels[pred_class[0]],"with {0:.2f} percent probability".format(prob))

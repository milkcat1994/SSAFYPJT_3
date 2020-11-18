import os
import glob

import cv2
import matplotlib.pyplot as plt
import dlib


path='.'
Images_crop = '\\Images_crop\\'
# Get Image names stored in "Images" folder
image_path_names=[]
person_names=set()
for file_name in glob.glob(path+'\\Images\\*_[1-9]*.jpg'):
    image_path_names.append(file_name)
    person_names.add(image_path_names[-1].split('\\')[-1].split('_')[0])

print(len(image_path_names))
print(image_path_names)

print(person_names)

###########################################################
#There are total 60 images containing 10 images per person.
###########################################################

# Load CNN face detector into dlib
dnnFaceDetector=dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

if not os.path.exists(path + Images_crop):
    os.mkdir(path + Images_crop)

# For each person create a separate folder
for person in person_names:
    if not os.path.exists(path + Images_crop+ person+'\\'):
        os.mkdir(path + Images_crop+ person+'\\')

  # Detect face, crop detected face and save them in corresponding person folder
for file_name in image_path_names:
    img=cv2.imread(file_name)
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects=dnnFaceDetector(gray,1)
    left,top,right,bottom=0,0,0,0
    for (i,rect) in enumerate(rects):
        left=rect.rect.left() #x1
        top=rect.rect.top() #y1
        right=rect.rect.right() #x2
        bottom=rect.rect.bottom() #y2
    width=right-left
    height=bottom-top
    img_crop=img[top:top+height,left:left+width]
    img_path=path + Images_crop + file_name.split('\\')[-1].split('_')[0]+'\\'+file_name.split('\\')[-1]
    cv2.imwrite(img_path,img_crop)

# Get Image names for testing
test_image_path_names=[]
for file_name in glob.glob(path+'\\Images_test\\*_[123].jpg'):
    test_image_path_names.append(file_name)

print(test_image_path_names)

########################################################
#For each person 3 images to test in Images_test folder.
########################################################
Images_test_crop='\\Images_test_crop\\'
if not os.path.exists(path+Images_test_crop):
    os.mkdir(path+Images_test_crop)

# Create Separate folder for each person in "Images_test_crop" folder
for person in person_names:
    if not os.path.exists(path+Images_test_crop+person+'\\'):
        os.mkdir(path+Images_test_crop+person+'\\')

# Detect face,crop face and save in corresponding folder
for file_name in test_image_path_names:
    img=cv2.imread(file_name)
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rects=dnnFaceDetector(gray,1)
    left,top,right,bottom=0,0,0,0
    for (i,rect) in enumerate(rects):
        left=rect.rect.left() #x1
        top=rect.rect.top() #y1
        right=rect.rect.right() #x2
        bottom=rect.rect.bottom() #y2
    width=right-left
    height=bottom-top
    img_crop=img[top:top+height,left:left+width]
    img_path=path+Images_test_crop+file_name.split('\\')[-1].split('_')[0]+'\\'+file_name.split('\\')[-1]
    cv2.imwrite(img_path,img_crop)

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.layers import ZeroPadding2D,Convolution2D,MaxPooling2D
from tensorflow.keras.layers import Dense,Dropout,Softmax,Flatten,Activation,BatchNormalization
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input
import tensorflow.keras.backend as K


#Define VGG_FACE_MODEL architecture
model = Sequential()
model.add(ZeroPadding2D((1,1),input_shape=(224,224, 3)))
model.add(Convolution2D(64, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(128, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(256, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(ZeroPadding2D((1,1)))
model.add(Convolution2D(512, (3, 3), activation='relu'))
model.add(MaxPooling2D((2,2), strides=(2,2)))
model.add(Convolution2D(4096, (7, 7), activation='relu'))
model.add(Dropout(0.5))
model.add(Convolution2D(4096, (1, 1), activation='relu'))
model.add(Dropout(0.5))
model.add(Convolution2D(2622, (1, 1)))
model.add(Flatten())
model.add(Activation('softmax'))

# Load VGG Face model weights
model.load_weights('vgg_face_weights.h5')

print(model.summary())

# Remove Last Softmax layer and get model upto last flatten layer with outputs 2622 units
vgg_face=Model(inputs=model.layers[0].input,outputs=model.layers[-2].output)

#Prepare Training Data
x_train=[]
y_train=[]
person_folders=os.listdir(path+Images_crop)
person_rep=dict()
print('path+Images_crop>>>>>>>>>>>>>>')
print(path+Images_crop)
print('person_folders>>>>>>>>>>>>')
print(person_folders)
for i,person in enumerate(person_folders):
  person_rep[i]=person
  image_names=os.listdir(path+Images_crop+person+'\\')
  for image_name in image_names:
    img=load_img(path+Images_crop+person+'\\'+image_name,target_size=(224,224))
    img=img_to_array(img)
    img=np.expand_dims(img,axis=0)
    img=preprocess_input(img)
    img_encode=vgg_face(img)
    x_train.append(np.squeeze(K.eval(img_encode)).tolist())
    y_train.append(i)

print('person_rep>>>>>>>>>>>>')
print(person_rep)

x_train=np.array(x_train)
y_train=np.array(y_train)

#Prepare Test Data
x_test=[]
y_test=[]
person_folders=os.listdir(path+Images_test_crop)
for i,person in enumerate(person_folders):
  image_names=os.listdir(path+Images_test_crop+person+'\\')
  for image_name in image_names:
    img=load_img(path+Images_test_crop+person+'\\'+image_name,target_size=(224,224))
    img=img_to_array(img)
    img=np.expand_dims(img,axis=0)
    img=preprocess_input(img)
    img_encode=vgg_face(img)
    x_test.append(np.squeeze(K.eval(img_encode)).tolist())
    y_test.append(i)

x_test=np.array(x_test)
y_test=np.array(y_test)


# Save test and train data for later use
np.save('train_data',x_train)
np.save('train_labels',y_train)
np.save('test_data',x_test)
np.save('test_labels',y_test)


# Load saved data
x_train=np.load('train_data.npy')
y_train=np.load('train_labels.npy')
x_test=np.load('test_data.npy')
y_test=np.load('test_labels.npy')


# Softmax regressor to classify images based on encoding 
classifier_model=Sequential()
classifier_model.add(Dense(units=100,input_dim=x_train.shape[1],kernel_initializer='glorot_uniform'))
classifier_model.add(BatchNormalization())
classifier_model.add(Activation('tanh'))
classifier_model.add(Dropout(0.3))
classifier_model.add(Dense(units=10,kernel_initializer='glorot_uniform'))
classifier_model.add(BatchNormalization())
classifier_model.add(Activation('tanh'))
classifier_model.add(Dropout(0.2))
classifier_model.add(Dense(units=2,kernel_initializer='he_uniform'))
classifier_model.add(Activation('softmax'))
classifier_model.compile(loss=tf.keras.losses.SparseCategoricalCrossentropy(),optimizer='nadam',metrics=['accuracy'])


# history = classifier_model.fit(x_train,y_train,epochs=100,validation_data=(x_test,y_test))
history = classifier_model.fit(x_train,y_train,epochs=100,validation_data=(x_train,y_train))

# # 학습 정확성 값과 검증 정확성 값을 플롯팅 합니다. 
# plt.plot(history.history['acc'])
# plt.plot(history.history['val_acc'])
# plt.title('Model accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('Epoch')
# plt.legend(['Train', 'Test'], loc='upper left')
# plt.show()

# Save model for later use
tf.keras.models.save_model(classifier_model,'.\\face_classifier_model.h5')

# Load saved model
classifier_model=tf.keras.models.load_model('.\\face_classifier_model.h5')

# Path to folder which contains images to be tested and predicted
Images_test='\\Images_test\\'
test_images_path=path+Images_test

dnnFaceDetector=dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

def plot(img):
  plt.figure(figsize=(8,4))
  plt.imshow(img[:,:,::-1])
  plt.show()

# Label names for class numbers
# person_rep={0:'Narendra Modi',1:'Donald Trump',2:'Angela Merkel',3:'Xi Jinping',4:'Lakshmi Narayana',5:'Vladimir Putin'}


if not os.path.exists(path+'\\Predictions'):
    os.mkdir(path+'\\Predictions')


for img_name in os.listdir('Images_test\\'): 
  if img_name=='crop_img.jpg':
    continue
  # Load Image
  img=cv2.imread(path+Images_test+img_name)
  gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # Detect Faces
  rects=dnnFaceDetector(gray,1)
  left,top,right,bottom=0,0,0,0
  for (i,rect) in enumerate(rects):
    # Extract Each Face
    left=rect.rect.left() #x1
    top=rect.rect.top() #y1
    right=rect.rect.right() #x2
    bottom=rect.rect.bottom() #y2
    width=right-left
    height=bottom-top
    img_crop=img[top:top+height,left:left+width]
    cv2.imwrite(path+'\\Images_test\\crop_img.jpg',img_crop)
    
    # Get Embeddings
    crop_img=load_img(path+'\\Images_test\\crop_img.jpg',target_size=(224,224))
    crop_img=img_to_array(crop_img)
    crop_img=np.expand_dims(crop_img,axis=0)
    crop_img=preprocess_input(crop_img)
    img_encode=vgg_face(crop_img)

    # Make Predictions
    embed=K.eval(img_encode)
    person=classifier_model.predict(embed)
    print(person)
    print(np.argmax(person))
    name=person_rep[np.argmax(person)]
    os.remove(path+'\\Images_test\\crop_img.jpg')
    cv2.rectangle(img,(left,top),(right,bottom),(0,255,0), 2)
    img=cv2.putText(img,name,(left,top-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2,cv2.LINE_AA)
    img=cv2.putText(img,str(np.max(person)),(right,bottom+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1,cv2.LINE_AA)
  # Save images with bounding box,name and accuracy 
  cv2.imwrite(path+'\\Predictions\\'+img_name,img)
  plot(img)





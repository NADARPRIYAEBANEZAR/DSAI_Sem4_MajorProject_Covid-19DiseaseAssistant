# -*- coding: utf-8 -*-
"""
Created on Sun May 15 15:46:48 2022

@author: Priya
"""
# Importing the Keras libraries and packages
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# import streamlit as st
# import os

# Initialising the CNN
classifier = tf.keras.models.Sequential()

classifier.add(tf.keras.layers.Convolution2D(filters=32, kernel_size=3, padding="same", input_shape=(64, 64, 3),
                                             activation='relu'))

classifier.add(tf.keras.layers.MaxPooling2D(pool_size=2, strides=2, padding='valid'))

classifier.add(tf.keras.layers.Convolution2D(filters=64, kernel_size=3, padding="same", activation="relu"))
classifier.add(tf.keras.layers.MaxPooling2D(pool_size=2, strides=2, padding='valid'))

classifier.add(tf.keras.layers.Flatten())

classifier.add(tf.keras.layers.Dense(units=128, activation='relu'))
classifier.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
classifier.summary()

# Part 2 - Fitting the CNN to the images



train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

training_set = train_datagen.flow_from_directory('C:/Users/Priya/OneDrive/Documents/MSCSEM4/COVID-19 Detector/Data/train',
                                                 target_size=(64, 64),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('C:/Users/Priya/OneDrive/Documents/MSCSEM4/COVID-19 Detector/Data/test',
                                            target_size=(64, 64),
                                            batch_size=32,
                                            class_mode='binary')

#training 
history = classifier.fit(training_set,
                         steps_per_epoch=4,
                         epochs=10,
                         validation_data=test_set,
                         validation_steps=4)

classifier.save('C:/Users/Priya/OneDrive/Documents/MSCSEM4/COVID-19 Detector/covid.h5')

# # evaluation on test set
# loaded_model = tf.keras.models.load_model('C:/Users/Priya/OneDrive/Documents/MSCSEM4/COVID-19 Detector/covid.h5')
# loaded_model.evaluate(test_set)

# import matplotlib.pyplot as plt
# plt.plot(history.history['accuracy'])
# plt.plot(history.history['val_accuracy'])
# plt.title('model accuracy')
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()

# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title('model loss')
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.show()


# # for only one prediction
# import numpy as np
# from tensorflow.keras.preprocessing import image


# # Include PIL, load_image before main()
# from PIL import Image


# def load_image(image_file):
# 	img = Image.open(image_file)
# 	return img

# st.subheader("Image")
# image_file = st.file_uploader("Upload Images",type=["png","jpg","jpeg"])
# if image_file is not None:
# 			  # TO See details
# 			  file_details = {"filename":image_file.name, "filetype":image_file.type,
#                               "filesize":image_file.size}
# 			  st.write(file_details)
# 			  st.image(load_image(image_file), width=250)
# 			  
# 			  #Saving upload
# 			  with open(os.path.join("C:/Users/Priya/OneDrive/Documents/MSCSEM4/testing_covid/",image_file.name),"wb") as f:
# 			  	c=f.write((image_file).getbuffer())
# 			  
# 			  st.success("File Saved")






#c=r'C:/Users/Priya/OneDrive/Documents/MSCSEM4/Data/test/Covid/covid-19-caso-70-1-PA.jpg'
#c = raw_input("enter the name of the image file: ")
# c=r'C:/Users/Priya/OneDrive/Documents/MSCSEM4/Data/test/Normal/IM-0256-0001.jpeg'
# test_image = image.load_img(c,target_size=(64, 64))
# plt.imshow(test_image)
# test_image = image.img_to_array(test_image)
# test_image = np.expand_dims(test_image, axis=0)
# result = classifier.predict(test_image)
# training_set.class_indices
# if (result[0].any() and result[0].any()) == 1:
#     prediction = 'Normal'
# else:
#     prediction = 'Covid'
# print(prediction)
# ans=np.argmax(result,axis=1)
# if(ans==0):
#         print("COVID")
        
# elif(ans==1):
#         print("Normal")   
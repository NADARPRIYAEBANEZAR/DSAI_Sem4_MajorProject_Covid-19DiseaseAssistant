# -*- coding: utf-8 -*-
"""
Created on Sat May 21 16:59:54 2022

@author: Priya
"""

import streamlit as st
import tensorflow as tf
 

import numpy as np
from PIL import Image # Strreamlit works with PIL library very easily for Images
import cv2
# hides all warnings
import warnings
warnings.filterwarnings('ignore')
# imports
import pandas as pd
# matplotlib 
import matplotlib.pyplot as plt
# sns
import seaborn as sns
# plotly ex
import plotly.express as px


def app():
 

    model_path='covid.h5'
   
    st.markdown("<h2 style='text-align: center; color: purple;'>COVID-19 Detection - Online</h2>", unsafe_allow_html=True)
    upload = st.file_uploader('Upload a CT scan image')
    if upload is not None:
      file_bytes = np.asarray(bytearray(upload.read()), dtype=np.uint8)
      opencv_image = cv2.imdecode(file_bytes, 1)
      opencv_image = cv2.cvtColor(opencv_image,cv2.COLOR_BGR2RGB) # Color from BGR to RGB
      img = Image.open(upload)
      st.image(img,caption='Uploaded Image',width=300)
      if(st.button('Predict')):
        model = tf.keras.models.load_model(model_path)
        x = cv2.resize(opencv_image,(64,64))
        x = np.expand_dims(x,axis=0)    
        #y = model.predict(x)
        #ans=np.argmax(y,axis=1)
        result = model.predict(x)
        #training_set.class_indices
        if (result[0].any() and result[0].any()) == 1:
            #st.write('You are Healthy \u263A')
             st.markdown("<h3 style=' font-weight: 900; color: #228B22;font-size: xx-large;'>You are Healthy \U0001F60A</h3>", unsafe_allow_html=True) 
        else:
            #st.write('You are suffering from COVID-19 \U0001F912')
            st.markdown("<h3 style='font-weight: 900; color: #228B22;font-size: xx-large;'>You are suffering from COVID-19 \U0001F912</h3>", unsafe_allow_html=True)
    
        # if(ans==0):
        #   st.title('COVID')
        # elif(ans==1):
        #   st.title('Healthy')
        # else:
        #   st.title('Other Pulmonary Disorder')
        
    st.error('Dont conclude by looking at predictions, just take them as a reference!!')
        

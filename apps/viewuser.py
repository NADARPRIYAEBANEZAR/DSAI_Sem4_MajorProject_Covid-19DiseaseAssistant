# -*- coding: utf-8 -*-
"""
Created on Wed May 25 19:47:14 2022

@author: Priya
"""
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

import matplotlib.pyplot as plt
# Connect to sqlite db
def app():
    st.markdown("<h2 style='text-align: center; color: purple;'>View Users</h2>", unsafe_allow_html=True)
    global data_df
    dt = st.radio("Please Select your choice !!!",
     ('Exploratory Data Analysis', 'Visual Data Analysis'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    if dt == 'Exploratory Data Analysis':
    
    #db_file = r'./User/data.db'
        db_file = r'./apps/data/Users1db.db'
        engine = create_engine(r"sqlite:///{}" .format(db_file))
        sql = 'SELECT Name,Address,Mobile ,Email  ,Gender,RegisterDate from Userstable'
        
        data_df = pd.read_sql(sql, engine)
        
        st.dataframe(data_df,1000,1000)
    elif dt=='Visual Data Analysis':
        data_df = data_df.groupby('RegisterDate').count().reset_index()
        data_df.rename(columns = {'Name':'No. of Users'}, inplace = True)
        
        data_df = data_df.set_index("RegisterDate")
    
    
    
        
        
        fig=plt.figure(figsize=(14,6))
        
        # Labelling the axes and setting
        # a title
        plt.xlabel("Register Date")
        plt.ylabel("No. of Users")
        plt.title("No. of Users vs. Register date")
        
        # plotting the "A" column alone
        plt.plot(data_df["No. of Users"])
        st.pyplot(fig)
            
    
    
    
   

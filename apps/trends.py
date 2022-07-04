# -*- coding: utf-8 -*-
"""
Created on Sat May 21 23:18:59 2022

@author: Priya
"""

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
# import streamlit
import streamlit as st

# import Image from pillow to open images
from PIL import Image
#import libraries
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType

from bs4 import BeautifulSoup as soup
from datetime import date,datetime
from urllib.request import Request, urlopen
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as py
import seaborn as sns
import gc
import warnings
warnings.filterwarnings("ignore")
from pandas_profiling import ProfileReport
import streamlit as st

def app():
    st.markdown("<h2 style='text-align: center; color: purple;'>COVID-19 \U0001F691 Tracker</h2>", unsafe_allow_html=True)
    #Web Scrapping
    today=datetime.now()
    yesterday_str="%s %d, %d" %(date.today().strftime("%b"),today.day-1,today.year)
    #yesterday_str
    
    
    url='https://www.worldometers.info/coronavirus/#countries'
    req=Request(url,headers={'User-Agent':"Mozilla/5.0"})
    
    webpage=urlopen(req)
    page_soup=soup(webpage,"html.parser")
    
    table=page_soup.findAll("table",{"id":"main_table_countries_yesterday"})
    #table
    
    containers=table[0].findAll("tr",{"style":""})
    title=containers[0]
    
    del containers[0]
    
    all_data=[]
    clean=True
    for country in containers:
        country_data=[]
        country_container=country.findAll("td")
        
        if country_container[1].text=="China":
            continue
        for i in range(1,len(country_container)):
            final_feature=country_container[i].text
            if clean:
                if i!=1 and i!=len(country_container)-1:
                    final_feature=final_feature.replace(",","")
                    if final_feature.find('+')!=-1:
                        final_feature=final_feature.replace("+","")
                        final_feature=float(final_feature)
                    elif final_feature.find("-")!=-1:
                        final_feature=final_feature.replace("-","")
                        final_feature=float(final_feature)*-1
                        
            if final_feature=='N/A':
                 final_feature=0
                 
            elif final_feature=="" or final_feature==" ":
                 final_feature=-1
            country_data.append(final_feature)
        all_data.append(country_data)    
        
    #all_data    
    df=pd.DataFrame(all_data)
    df.drop([15,16,17,18,19,20],inplace=True,axis=1)
    #df.head()
    
    
        
    column_labels=["Country","Total Cases","New Cases","Total Deaths","New Deaths","Total Recovered","New Recovered","Active Cases","Serious/Critical","Total Cases/1M","Deaths/1M","Total Tests","Test/1M","Population","Continent"]
    df.columns=column_labels
    #Countries
    #Countries
    df=df.drop([len(df)-1])
    df=df.drop([0])
    
    
    # saving the dataframe
    df.to_csv('covid.csv')
    
    @st.cache
    def load_data():
        
        df=pd.read_csv('covid.csv')
        return df
    df=load_data()
    
    vis=st.sidebar.selectbox('Select a Chart Type',('Bar Chart','Line Chart'))
    count_select=st.sidebar.selectbox('Select a Country',df['Country'].unique())
    status=st.sidebar.radio('COVID-19 patient status',('Total Deaths','Total Recovered','Active Cases','Serious/Critical'))
    selected_count=df[df['Country']==count_select]
    st.markdown("** Country Wise Analysis **")
    
    def get_dataframe(df):
        total_dataframe=pd.DataFrame({'Status':['Total Deaths','Total Recovered','Active Cases','Serious/Critical'],'Number of Cases':(df.iloc[0]['Total Deaths'],df.iloc[0]['Total Recovered'],df.iloc[0]['Active Cases'],df.iloc[0]['Serious/Critical'])})
        return total_dataframe
    
    count_total=get_dataframe(selected_count)
    if vis=='Bar Chart':
        count_tot=px.bar(count_total,x='Status',y='Number of Cases',color='Status')
        st.plotly_chart(count_tot)
        
    
    elif vis=='Line Chart':
        if status == 'Total Deaths':
            st.title("Total Deaths")
            fig = px.line(df,x='Country',y=df['Total Deaths'])
            st.plotly_chart(fig)
        elif status =='Total Recovered':
            st.title("Total Recovered")
            fig = px.line(df,x='Country',y=df['Total Recovered'])
            st.plotly_chart(fig)
        elif status =='Active Cases':
            st.title("Active Cases")
            fig = px.line(df,x='Country',y=df['Active Cases'])
            st.plotly_chart(fig)
        else:
            st.title("Serious/Critical")
            fig = px.line(df,x='Country',y=df['Serious/Critical'])
            st.plotly_chart(fig)
    

            
            
    def get_table():
        datatable = df[['Country', 'Total Deaths', 'Total Recovered', 'Active Cases','Serious/Critical']].sort_values(by=['Total Deaths'],ascending =False)
        return datatable
    
    datatable = get_table()
    st.dataframe(datatable)
    
    
            
        
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

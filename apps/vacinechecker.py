# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:47:19 2022

@author: Priya
"""
import streamlit as st
from PIL import Image
from fake_useragent import UserAgent
import requests
import pandas as pd

import base64
import json

def app():
        
        ua = UserAgent()
        #header = {'User-Agent': str(ua.chrome)}
        header = {"Content-Type": "application/json; charset=utf-8"}
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        local_css("apps/data/style.css")

    
        def get_table_download_link(df,filename,text):
            """Generates a link allowing the data in a given panda dataframe to be downloaded
            in:  dataframe
            out: href string
            """
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
            # href = f'<a href="data:file/csv;base64,{b64}">Download Report</a>'
            href = f'<a class="down , btn" href="data:file/csv;base64,{b64}" download="{filename}" >{text}</a>'
            return href
        def run():
            global center_response,centers_data,session_ids
            st.markdown("<h2 style='text-align: center; color: purple;'>Vaccine \U0001F489 Availability Checker </h2>", unsafe_allow_html=True)
            
        
            area_pin = st.text_input('Enter your Area Pin-Code Eg.421306')
                ## Age
            age_display = ['18 & Above','18-45', '45+']
            age = st.selectbox("Your Age", age_display)
            age_val = 0
                ## Vaccine Type
            vacc_display = ['Covishield', 'Covaxin', 'Sputnik V']
            vaccine = st.selectbox("Vaccine Type", vacc_display)
            vaccine_type = ''
            if vaccine == 'Covishield':
                    vaccine_type = 'COVISHIELD'
            elif vaccine == 'Covaxin':
                    vaccine_type = 'COVAXIN'
            else:
                    vaccine_type = 'SPUTNIK V'
        
                ## Fee Type
            fee_display = ['Free', 'Paid']
            fee = st.selectbox("Vaccine Type", fee_display)
        
                ## Select Date
            vac_date = st.date_input("Date")
        
            vac_date = str(vac_date).split('-')
            new_date = vac_date[2] + '-' + vac_date[1] + '-' + vac_date[0]
            global center_response,centers_data
            if st.button("Search"):
                global center_response,centers_data
                center_response = requests.get(
                        f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={area_pin}&date={new_date}",
                        headers=header)
                    ##centers_data = center_response.json()
           
                centers_data = center_response.json()
                centers = pd.DataFrame(centers_data.get('centers'))
                if centers.empty:
                            st.error('No Center found')
                else:
                            session_ids = []
                            for j, row in centers.iterrows():
                                                    session = pd.DataFrame(row['sessions'][0])
                                                    session['center_id'] = centers.loc[j, 'center_id']
                                                    session_ids.append(session)
                                                    
                        
                            sessions = pd.concat(session_ids, ignore_index=True)
                            av_session = centers.merge(sessions, on='center_id')
                            session_ids1 = []
                            for j, row in av_session.iterrows():
                                                    session1 = pd.json_normalize(av_session.slots[0])
                                                    session1['center_id'] = av_session.loc[j, 'center_id']
                                                    session_ids1.append(session1)
                                                    
                        
                            sessions1 = pd.concat(session_ids1, ignore_index=True)
                                                #print(sessions1)
                                                #print(sessions)
                            av_centeres = av_session.merge(sessions1, on='center_id')
                                                #print(av_session)
                            print(av_centeres.columns)
                                        ## Age filter
                            if age == '18 & Above':
                                            age_val = 18
                                            av_centeres = av_centeres[av_centeres['min_age_limit'] == age_val]
                            elif age == '18-45':
                                            age_val = 45
                                            av_centeres = av_centeres[av_centeres['max_age_limit'] == age_val]
                            else:
                                            age_val = 45
                                            av_centeres = av_centeres[av_centeres['min_age_limit'] == age_val]
                        
                            av_centeres.drop(
                                                    columns=['sessions', 'session_id', 'lat', 'block_name', 'long', 'date', 'from', 'to', 'state_name',
                                                             'district_name','max_age_limit', 'vaccine_fees'
                                                             , 'allow_all_age','slots','seats','available_capacity'], inplace=True, errors='ignore')
                        
                                        ## Vaccine filter
                            av_centeres = av_centeres[av_centeres['vaccine'] == vaccine_type]
                        
                                        ## Fees filter
                            av_centeres = av_centeres[av_centeres['fee_type'] == fee]
                        
                            new_df = av_centeres.copy()
                            new_df.columns = ['Center_ID', 'Name', 'Address', 'Pincode','Fee', 'Minimum Age', 'Vaccine Type', 'Dose 1','Dose 2','Timing']
                            new_df = new_df[['Center_ID', 'Name', 'Fee', 'Pincode',
                                                         'Minimum Age', 'Vaccine Type', 'Timing', 'Address', 'Dose 1',
                                                         'Dose 2']]
                            if new_df.empty:
                                            st.error("No Center found.")
                            else:
                                            st.dataframe(new_df.assign(hack='').set_index('hack'))
                                        
                                            
                                           
                                            st.markdown(get_table_download_link(new_df,area_pin+ '_' + new_date.replace('-',
                                                                                                                                        '_') + '.csv','Download Report'), unsafe_allow_html=True)
                                           
                                            href = f'<a class="down , btn" href="https://selfregistration.cowin.gov.in/">Book Slot</a>'
                                            st.markdown(href, unsafe_allow_html=True)
                                            
                                            
          
    
        
       
        run()
       

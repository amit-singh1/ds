# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 18:43:41 2020

@author: amit
"""

import streamlit as st
import pandas as pd
import xlrd

st.title("Enter Your GMAT SCORE")

user_input = st.text_input("550+ Scores will give you decent Universities")


DATA_URL = r'gmatts.xlsx'

##df = pd.read_excel(open('//X/str/Db/C/Source/selection/Date/Test/12.xlsx','rb'), sheetname='Sheet 1')


df = pd.read_excel(DATA_URL)



if user_input!="":
    val = int(user_input)
    st.dataframe(df[df['Scores']<val])

else :
    st.write("Results will show up here")
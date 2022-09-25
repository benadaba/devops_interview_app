import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance


# Title and Subheader
st.title("Devops Interview Questions App")
st.subheader("All Interview Questions ")


# EDA
my_dataset = "devops_interview_questions_app.csv"

# To Improve speed and cache data
@st.cache(persist=True)
def explore_data(dataset):
	df = pd.read_csv(os.path.join(dataset))
	return df 


data = explore_data(my_dataset)
st.dataframe(data)


#get the unique domain names
def get_tech_domains():
    data = explore_data(my_dataset)
    domains = data['Domain'].unique()
    print(type(domains))
    # domains.dropna(inplace=True)
    cleandeddomains = [x for x in domains if str(x) != 'nan']
    return  cleandeddomains


# Selection
species_option = st.selectbox('Select A Domain',get_tech_domains())
st.write(species_option +" Interview Questions")
data[data['Domain']==species_option]


# About

if st.button("About App"):
	st.subheader("Devops Interview Questions App")
	st.text("Built with Streamlit")
	st.text("Thanks to the Streamlit Team Amazing Work")

if st.checkbox("By"):
	st.text("Bernard Adabankah")
	
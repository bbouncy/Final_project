import streamlit as st
import pandas as pd
import plotly.express as px
import math
import json
import requests
import numpy as np
import LinearRegression
from sklearn.linear_model import LinearRegression
import base64
import matplotlib.pyplot as plt



def loadata():
    data = pd.read_excel('data/Training_data1.xlsx', index_col=None)
    return data

data = loadata()

#background image
def add_bg_from_local(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

add_bg_from_local('image/image.jpg')


st.title("What will your grade be?")

name = st.text_input('Enter your name below:')

user = st.radio('Who are you?', ['I am a student', 'I am a parent / guardian'])

if user == 'I am a student':
    st.markdown ( "**It's great that you want to get ahead on your exam, {}! Let's take a look at how you can achieve the grade you want.**".format(name))

else:
    st.write("**Hello {}, if you would like to see how long your child has to study please complete the following fields.**".format(name))

x = np.array(data['STG']).reshape((-1,1))
y = np.array(data['STG'])

model = LinearRegression()

model.fit(x,y)
LinearRegression()




data["Grades"] = data["scores"].replace({"very_low":"D",'Low':'C', 'Middle':"B", "High":"A"})

data["Grades"] = data["Grades"].astype('category')
data["Grades"] = data["Grades"].cat.reorder_categories(['A', 'B', "C", "D"])


option = st.selectbox(
    'What grade are you hoping to get?',
    sorted((data['Grades'].unique())))

#very_low - D
#Low - C
#Middle - B
#High - A

if option == "A":
    value = 20
if option == "B":
    value = 18
if option == "C":
    value = 15
if option == "D":
    value = 12

y_pred = model.predict(np.array([value]).reshape((-1,1)))


st.write("**If you want an {} the ideal study time is {:.0f} hours.**".format(option,y_pred[0]))



#scatterplot
df = pd.read_excel('data/Training_data1.xlsx', index_col=None)
fig = px.scatter(df, x="study_hours", y="STG", color="scores",

                title= 'Chart to help you determine what grade you want',

                 labels={
                     "study_hours": "Amount of hours past students studied",
                     "STG": "Grades past students have received ",
                     "species": "Species of Iris"
                 }

                 )
st.plotly_chart(fig)
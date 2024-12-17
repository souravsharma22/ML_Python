import streamlit as sl
sl.title("Widgets")
import pandas as pd

name = sl.text_input("ENter your name")

if name:
    sl.write(f'Hello,{name} ! welcome to streamlit')

age  = sl.slider("select you age",0,100,21)
sl.write(f"Your age is {age}")
options = ['Java','Python',"c++","c",'JavaSCript']
lang = sl.selectbox("Chose yoy favorite programming language",options)
sl.write(f"YOur favorate lang is {lang}")

# takin file input
getfile= sl.file_uploader("PLs upload a csv file",type='csv')
if getfile is not None:
    df = pd.read_csv(getfile)
    sl.write(df)
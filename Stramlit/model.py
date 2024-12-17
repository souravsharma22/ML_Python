import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import streamlit as sl

@sl.cache_data
def load_data():
    iris = load_iris()
    df= pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species']=iris.target
    return df, iris.target_names

df,target_names=load_data()

model = RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])

#taking input data
sl.sidebar.title("Input Features")
sepal_length= sl.sidebar.slider("sepal Lenght", float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()))
sepal_width= sl.sidebar.slider("sepal width", float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()))
petel_length= sl.sidebar.slider("petal Lenght", float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()))
petel_width= sl.sidebar.slider("petal width", float(df['petal width (cm)'].min()),float(df['petal width (cm)'].max()))

input_data = [[sepal_length,sepal_width,petel_length,petel_width]]
prediction_data = model.predict(input_data)
prediction_species = target_names[prediction_data[0]]

sl.write("The species it might be is")
sl.write(prediction_species)
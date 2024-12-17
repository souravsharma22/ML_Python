import streamlit as slt
import pandas as pd
import numpy as np

slt.title("Hello Streamlit")

# wrinting text
slt.write("This is the basic text")

df = pd.DataFrame({
    'first colo':[1,2,3,4,5],
    'secound col':[10,20,30,40,50]
})

slt.write('This is dataFrame ')
slt.write(df)
df.to_csv('Sample.csv',index=None)

# creating a line chart

char_data = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
slt.line_chart(char_data)
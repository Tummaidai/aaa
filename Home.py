import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

gender_data=pd.read_csv('./data/superstore.csv')
html_3 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>การทำ Data Visualization เรื่องยอดขาย</h3></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")

html_0 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Example data table</h3></center>
</div>
"""



st.markdown(html_0, unsafe_allow_html=True)
st.markdown("")
st.write(gender_data.head(10))



html_1 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Count of Category by Region</h3></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")



plt.figure(figsize=(15,5))
sns.countplot(x='Region', data=gender_data, hue='Category')
plt.title('Count of Category by Region')
plt.xlabel('Region')
plt.ylabel('Count')

st.pyplot(plt)



html_2 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>ยอดขายของแต่ละภูมิภาค</h3></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")



plt.figure(figsize=(15,5))
sns.countplot(x='Region', data=gender_data )
plt.title('ยอดขายของแต่ละภูมิภาค')
plt.xlabel('Region')
plt.ylabel('Sales')

st.pyplot(plt)
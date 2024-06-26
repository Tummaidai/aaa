import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

gender_data=pd.read_csv('./data/titanic_data.csv')
html_3 = """
<div style="background-color:#FFFFFF;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>การทำ Data Visualization เรื่องผู้รอดชีวิตจากเรือไททานิค</h3></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")

html_0 = """
<div style="background-color:#FFFFFF;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Example data table</h3></center>
</div>
"""



st.markdown(html_0, unsafe_allow_html=True)
st.markdown("")
st.write(gender_data.head(10))



html_1 = """
<div style="background-color:#FFFFFF;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Count of Survived by Sex</h3></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")



plt.figure(figsize=(15,5))
sns.countplot(x='Survived', data=gender_data, hue='Sex')
plt.title('Count of Survived by Sex')
plt.xlabel('Survived')
plt.ylabel('Count')

st.pyplot(plt)



html_2 = """
<div style="background-color:#FFFFFF;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Count of Survived by Pclass</h3></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")



plt.figure(figsize=(15,5))
sns.countplot(x='Survived', data=gender_data, hue='Pclass')
plt.title('Count of Survived by Pclass')
plt.xlabel('Survived')
plt.ylabel('Count')

st.pyplot(plt)

html_4 = """
<div style="background-color:#FFFFFF;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3>Count of Survived by Embarked</h3></center>
</div>
"""
st.markdown(html_4, unsafe_allow_html=True)
st.markdown("")



plt.figure(figsize=(15,5))
sns.countplot(x='Survived', data=gender_data, hue='Embarked')
plt.title('Count of Survived by Embarked')
plt.xlabel('Survived')
plt.ylabel('Count')

st.pyplot(plt)
import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="pattanan ",
    page_icon= ":bar_chart:",
)
st.sidebar.success("เลือกรายการด้านบน.")


html_1 = """
<div style="background-color:#0E1117;border-bottom: 3px solid #ffffff;border-top: 3px solid #ffffff;">
<center><h3> การทำ Data Visualization! </h3></center>
</div>
"""

st.header("  การทำ Data Visualization!....!  ")
st.subheader(" 1.หลักการและเหตุผล")
st.info("""
        คือการนำข้อมูลดิบ มาวิเคราะห์และแสดงผลข้อมูลออกมาในรูปแบบของกราฟ แผนภูมิ ที่ช่วยให้ได้ข้อมูลเชิงลึกจากข้อมูลดิบเหล่านั้นและทำให้เห็นคุณค่าของข้อมูล
        <br>
        
        """)
st.subheader(" 2.วัตถุประสงค์")
st.info("""
        เพื่อนำเสนอข้อมูลให้อยู่ในรูปแบบที่เข้าใจง่ายโดยใช้วิธีจินตทัศน์ข้อมูลมาช่วยนำเสนอในรูปแบบแผนภูมิและกราฟ
        """)
st.balloons()
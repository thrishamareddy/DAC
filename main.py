import streamlit as st
from PIL import Image
hide_menu = """
<style>
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""
showWarningOnDirectExecution = False
image = Image.open('icons/logo.jpg')
img1 = Image.open('icons/logo.jpg')
st.set_page_config(page_title = "Digital Aggression Control", page_icon = image)
st.markdown(hide_menu, unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image(image , use_column_width=True, output_format='auto')
st.sidebar.markdown("---")
st.sidebar.markdown("<h1 style='text-align: center; font-size: 18px; color: #0080FF;'> Thrisha Reddy Mareddy </h1>", unsafe_allow_html=True)
st.image(img1 , use_column_width=True)

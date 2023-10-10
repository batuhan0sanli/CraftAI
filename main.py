import os

import streamlit as st

from src import PageBuilder

yaml_list = os.listdir('applets')

st.set_page_config(
    page_title='CraftAI',
    page_icon=':robot_face:',
)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
.stDeployButton {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

yaml_path = st.sidebar.selectbox('Select applet', yaml_list)
page_builder = PageBuilder(os.path.join('applets', yaml_path))
page_builder.build()

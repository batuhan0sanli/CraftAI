import os

import streamlit as st

from src import PageBuilder

yaml_list = os.listdir('applets')

st.set_page_config(
    page_title='CraftAI',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

yaml_path = st.sidebar.selectbox('Select applet', yaml_list)
page_builder = PageBuilder(os.path.join('applets', yaml_path))
page_builder.build()

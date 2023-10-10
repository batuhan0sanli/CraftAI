import os

import streamlit as st

from src.builders.page_builder import PageBuilder

yaml_list = os.listdir('applets')

st.set_page_config(
    page_title='CraftAI',
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

yaml_path = st.sidebar.selectbox('Select applet', yaml_list)
page_builder = PageBuilder(os.path.join('applets', yaml_path))
page_builder.build()

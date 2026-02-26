import streamlit as st
from streamlit_option_menu import option_menu



with st.sidebar:
    data = option_menu(
        menu_title = "my project";
        option =[
        "home",
        "about",
        "contract",
        "services",
        ]
    )

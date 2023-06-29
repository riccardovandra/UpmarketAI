import streamlit as st
from utils import workflow
from frontend import biz_profile

st.set_page_config(
    page_title="One Click Business Profile Creation",
    page_icon="👋",
)

def main():

    biz_profile.get_main_elements()

if __name__ == '__main__':
    main()
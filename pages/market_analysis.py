import streamlit as st
from utils import workflow

swot_analysis = st.button('Generate SWOT Analysis based on form data')

if swot_analysis:
    swot = workflow.get_swot_analysis_from_form()
    st.write(swot)

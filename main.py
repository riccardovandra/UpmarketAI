import streamlit as st
from utils import *

st.title('Business Profile Creation')
website_url = st.text_input('Insert Website URL Here')

if website_url:
    description = workflow.get_business_description(website_url)
    st.header("Business Description")
    st.write(description)

    description_short = workflow.get_business_description_short(description)

    st.header("Description (Short)")
    st.write(description_short)
    
    audience_persona = workflow.get_audience_persona(description)
    st.header("Audience Persona")
    st.write(audience_persona)
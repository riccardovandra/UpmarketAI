import streamlit as st
from utils import workflow

def get_main_elements():
    st.title('One-click Business Profile Creation')
    st.write('Define information such as Business Description, Target Audience, Product Category, Tone of Voice & Value Proposition just by adding a Website URL')
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

        product_category = workflow.get_product_category(description)
        st.header("Product Category")
        st.write(product_category)

        tone_of_voice = workflow.get_tone_of_voice(description)
        st.header("Product Category")
        st.write(tone_of_voice)

        value_proposition = workflow.get_value_proposition(description)
        st.header("Product Category")
        st.write(value_proposition)


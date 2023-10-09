import streamlit as st
from utils import workflow
from utils.storage import save_result_in_form_data

def get_main_elements():
    st.title('Business Analyzer')
    st.write('Define information such as Business Description, Target Audience, Product Category, Tone of Voice & Value Proposition just by adding a Website URL')
    website_url = st.text_input('Insert Website URL Here')

    if website_url:
        description = workflow.get_business_description(website_url)
        st.header("Business Description")
        st.write(description)

        description_short = workflow.get_business_description_short(description)

        st.header("Description (Short)")
        st.write(description_short)
        
        target_audience = workflow.get_audience_persona(description)
        st.header("Target Audience")
        st.write(target_audience)

        product_category = workflow.get_product_category(description,website_url)
        st.header("Product Category")
        st.write(product_category)

        tone_of_voice = workflow.get_tone_of_voice(description)
        st.header("Tone of Voice")
        st.write(tone_of_voice)

        value_proposition = workflow.get_value_proposition(description)
        st.header("Value Proposition")
        st.write(value_proposition)

        save_form_data = st.button("Save Results")
        if save_form_data:
            save_result_in_form_data("Brand Description (Long)",description)
            save_result_in_form_data("Brand Description (Short)",description_short)
            save_result_in_form_data("Target Audience", target_audience)
            save_result_in_form_data("Product Category",product_category)
            save_result_in_form_data("Tone of voice",tone_of_voice)
            save_result_in_form_data("Value Proposition",value_proposition)



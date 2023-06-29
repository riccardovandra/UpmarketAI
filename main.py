import streamlit as st
from utils import workflow

st.set_page_config(
    page_title="One Click Business Profile Creation",
    page_icon="👋",
)

def main():
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

if __name__ == '__main__':
    main()
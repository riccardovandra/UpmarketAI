import streamlit as st
from utils import storage


form_fields = storage.load_form_config('config/form_config.json')

#Form Functionalities
with st.form('Business Profile Information'):
    st.write('Complete the business profile information')
    
    form_data = {}
    for field in form_fields:
        field_name = field['field_name']
        field_key = field['field_key']
        field_placeholder = field['field_placeholder']
        field_type = field['field_type']
        
        if field_type == 'text_input':
            field_value = st.text_input(field_name, key=field_key, value="", placeholder=field_placeholder)
        elif field_type == 'text_area':
            field_value = st.text_area(field_name, key=field_key, value="", placeholder=field_placeholder)
        else:
            field_value = None
        
        form_data[field_key] = field_value

    submitted = st.form_submit_button("Submit")

    if submitted:
        file_path = 'config/form_data.json'
        storage.store_form_data(form_data, file_path)
        st.success('Form data submitted successfully!')




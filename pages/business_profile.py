import streamlit as st
import json
from utils import storage


config_path = 'config/form_config.json'
with open(config_path, 'r') as config_file:
    config_data = json.load(config_file)
    form_fields = config_data['form_fields']

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




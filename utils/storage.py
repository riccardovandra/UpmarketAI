import json

def store_form_data(form_data, file_path):
    # Convert form data to JSON
    json_data = json.dumps(form_data, indent=4)
    
    # Write JSON data to file
    with open(file_path, 'w') as file:
        file.write(json_data)

def load_form_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config_data = json.load(config_file)
        form_fields = config_data['form_fields']

        return form_fields

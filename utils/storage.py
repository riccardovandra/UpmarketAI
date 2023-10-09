import json

def store_form_data(form_data, file_path):
    # Convert form data to JSON
    json_data = json.dumps(form_data, indent=4)
    
    # Write JSON data to file
    with open(file_path, 'w') as file:
        file.write(json_data)


def load_form_config():
    with open('config/form_config.json', 'r') as config_file:
        config_data = json.load(config_file)
        form_fields = config_data['form_fields']

        return form_fields
    
def st():
    with open('config/form_data.json', 'r') as config_file:
        form = json.load(config_file)
        return form


def save_result_in_form_data(field_name, result):
    """
    Save the result in the form_data.json file at the specified field.

    Args:
        field_name (str): The name of the field in the form data.
        result (str): The result to save.
    """
    with open('config/form_data.json', 'r') as file:
        form_data = json.load(file)

    form_data[field_name] = result

    with open('config/form_data.json', 'w') as file:
        json.dump(form_data, file, indent=4)
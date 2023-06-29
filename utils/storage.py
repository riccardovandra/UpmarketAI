import json

def store_form_data(form_data, file_path):
    # Convert form data to JSON
    json_data = json.dumps(form_data, indent=4)
    
    # Write JSON data to file
    with open(file_path, 'w') as file:
        file.write(json_data)
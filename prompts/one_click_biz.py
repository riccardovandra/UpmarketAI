prompt_website_description_long = '''

Act as an expert marketing researcher.
Based on the context website URL {websiteURL}
Please describe the website using 500 words.
'''

prompt_website_description_short = '''

Please summarize the following description in 150 words
{description_long}
'''

prompt_persona_building = '''

Act as an expert marketing researcher.
Please come up with 3 marketing personas based on the following information:
{description_long}

The output should be the following:
- Persona Name
- Age Range
- Industry
- Job Role
- Needs
'''

prompt_product_category = '''

Act as an expert market researcher.

Based on the following information, please understand in which category {website_url} is.

Description: {description_long}

As output, please give 2 main product categories with 2-3 words max

'''

prompt_tone_of_voice = '''

Act as an expert market researcher.

Based on the information that you found on the website and the description, please mention 3 tone of voices used by the business

Description: {description_long}

'''

prompt_value_proposition = '''

Act as an expert market researcher.

Based on the information that you found on the website and the description, please what's the value proposition of the business

Description: {description_long}

'''
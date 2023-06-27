from langchain import PromptTemplate

def get_prompt_template(template):
    prompt = PromptTemplate.from_template(template)
    return prompt


# Testing
#prompt_description_long = get_prompt_template(prompt_website_description_long)
#finalized_description_long = prompt_description_long.format(websiteURL='https://remo.co/')

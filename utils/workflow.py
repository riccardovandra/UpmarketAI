from . import chains
from . import embeddings
from . import prompt_builder
import prompts
from . import scraper
import json

def get_vector_database_from_url(website_url):
    #Strip https:// from the website URL website_url_stripped = 
    html = scraper.scrape_website_content(website_url)
    website_doc = scraper.clean_website_content(html)
    texts = embeddings.website_text_splitter(website_doc)
    db = embeddings.create_vector_database(texts)
    embeddings.save_vector_database(db,f'data/{website_url}')

    return db

def process_chain(prompt_template, data):
    """
    Helper function to process a language learning model (LLM) chain with the given data.

    Args:
        prompt_template (str): The prompt template.
        data (str or dict): The data to input to the chain.

    Returns:
        str: The result of running the chain.
    """
    template = prompt_builder.get_prompt_template(prompt_template)
    chain = chains.initialize_llm_chain(template)
    return chains.run_llm_chain(chain, data)

def get_business_description(website_url):
    db = get_vector_database_from_url(website_url)
    prompt_description_long = prompts.prompt_website_description_long
    prompt_description_long_template = prompt_builder.get_prompt_template(prompt_description_long)
    finalized_description_prompt = prompt_description_long_template.format(websiteURL=website_url)
    qa = chains.initialize_qa_chain(db)
    description = chains.run_qa_chain(qa,finalized_description_prompt)

    return description

def get_business_description_short(description):
    return process_chain(prompts.prompt_website_description_short, description)

def get_audience_persona(description):
    return process_chain(prompts.prompt_persona_building, description)

def get_product_category(description):
    return process_chain(prompts.prompt_product_category, description)

def get_tone_of_voice(description):
    return process_chain(prompts.prompt_tone_of_voice, description)

def get_value_proposition(description):
    return process_chain(prompts.prompt_value_proposition, description)

def get_swot_analysis_from_form():
    with open('config/form_data.json', 'r') as file:
        form_data = json.load(file)

    description = form_data['Brand Description (Long)']
    product_category = form_data['Product Category']
    prompt_data = {
        'description_long': description,
        'product_category':product_category
    }

    return process_chain(prompts.prompt_swot_analysis, prompt_data)




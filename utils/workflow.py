from . import chains
from . import embeddings
from . import prompt_builder
from . import prompts
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


def get_business_description(website_url):

    """
    Retrieve the business description from the website URL.

    Args:
        website_url (str): The URL of the website.

    Returns:
        str: The business description.
    """

    db = get_vector_database_from_url(website_url)
    prompt_description_long = prompts.prompt_website_description_long
    prompt_description_long_template = prompt_builder.get_prompt_template(prompt_description_long)
    finalized_description_prompt = prompt_description_long_template.format(websiteURL=website_url)
    qa = chains.initialize_qa_chain(db)
    description = chains.run_qa_chain(qa,finalized_description_prompt)

    return description

def get_business_description_short(description):
    """
        Generate a short business description from the provided description.

        Args:
            description (str): The business description.

        Returns:
            str: The short business description.
    """

    prompt_description_short_template = prompt_builder.get_prompt_template(prompts.prompt_website_description_short)
    summarizer = chains.initialize_llm_chain(prompt_description_short_template)
    description_short = chains.run_llm_chain(summarizer,description)

    return description_short

def get_audience_persona(description):

    """
    Generate the audience persona based on the provided description.

    Args:
        description (str): The business description.

    Returns:
        str: The audience persona.
    """
    
    prompt_persona_building_template = prompt_builder.get_prompt_template(prompts.prompt_persona_building)
    chain_audience_persona = chains.initialize_llm_chain(prompt_persona_building_template)
    audience_persona = chains.run_llm_chain(chain_audience_persona,description)

    return audience_persona

def get_product_category(description):
    prompt_product_category_template = prompt_builder.get_prompt_template(prompts.prompt_product_category)
    chain_audience_persona = chains.initialize_llm_chain(prompt_product_category_template)
    product_category = chains.run_llm_chain(chain_audience_persona,description)

    return product_category

def get_swot_analysis_from_form():
    with open('config/form_data.json', 'r') as file:
        form_data = json.load(file)

    description = form_data['Brand Description (Long)']
    product_category = form_data['Product Category']
    prompt_data = {
        'description_long': description,
        'product_category':product_category
    }

    prompt_swot_template = prompt_builder.get_prompt_template(prompts.prompt_swot_analysis)
    chain_swot_analysis = chains.initialize_llm_chain(prompt_swot_template)
    swot_analysis = chains.run_llm_chain(chain_swot_analysis,prompt_data)

    return swot_analysis


from . import chains
from . import embeddings
from . import prompt_builder
from . import prompts
from . import scraper

def get_business_description(website_url):

    """
    Retrieve the business description from the website URL.

    Args:
        website_url (str): The URL of the website.

    Returns:
        str: The business description.
    """

    html = scraper.scrape_website_content(website_url)
    website_doc = scraper.clean_website_content(html)
    texts = embeddings.website_text_splitter(website_doc)
    db = embeddings.create_vector_database(texts)
    embeddings.save_vector_database(db,'data/feiss_db')
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


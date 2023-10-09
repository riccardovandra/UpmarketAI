from . import chains
from . import embeddings
from . import storage
from . import prompt_builder
from prompts import one_click_biz,strategy
from . import scraper

def get_vector_database_from_url(website_url):
    #Strip https:// from the website URL website_url_stripped = 
    html = scraper.scrape_website_content(website_url)
    website_doc = scraper.clean_website_content(html)
    texts = embeddings.website_text_splitter(website_doc)
    db = embeddings.create_vector_database(texts)
    embeddings.save_vector_database(db,f'data/{website_url}')

    return db

def process_chain(prompt_template, data=''):
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
    prompt_description_long = one_click_biz.prompt_website_description_long
    prompt_description_long_template = prompt_builder.get_prompt_template(prompt_description_long)
    finalized_description_prompt = prompt_description_long_template.format(websiteURL=website_url)
    qa = chains.initialize_qa_chain(db)
    description = chains.run_qa_chain(qa,finalized_description_prompt)

    return description

def get_business_description_short(description):
    return process_chain(one_click_biz.prompt_website_description_short, description)

def get_audience_persona(description):
    return process_chain(one_click_biz.prompt_persona_building, description)

def get_product_category(description,website_url):
    return process_chain(one_click_biz.prompt_product_category, {'description_long':description,'website_url':website_url})

def get_tone_of_voice(description):
    return process_chain(one_click_biz.prompt_tone_of_voice, description)

def get_value_proposition(description):
    return process_chain(one_click_biz.prompt_value_proposition, description)

def get_swot_analysis_from_form():
    form = storage.load_form_data()

    print(form)

    description = form['Brand Description (Long)']
    product_category = form['Product Category']
    prompt_data = {
        'description_long': description,
        'product_category':product_category
    }

    return process_chain(strategy.prompt_swot_analysis, prompt_data)

def get_strategy_goals(campaign_goals):
    form = storage.load_form_data()

    description = form['Brand Description (Long)']
    product_category = form['Product Category']
    target_audience = form['Target Audience']
    
    prompt_data = {
        'description_long': description,
        'product_category':product_category,
        'target_audience':target_audience,
        'campaign_goals':campaign_goals
    }

    return process_chain(strategy.prompt_strategy_goals, prompt_data)

def get_strategy_high_level(campaign_goals):
    form = storage.load_form_data()

    description = form['Brand Description (Long)']
    product_category = form['Product Category']
    target_audience = form['Target Audience']
    
    prompt_data = {
        'description_long': description,
        'product_category':product_category,
        'target_audience':target_audience,
        'campaign_goals':campaign_goals
    }

    return process_chain(strategy.prompt_strategy_creation_high_level, prompt_data)

def get_why_mission_values(campaign_goals, target_market):
    form = storage.load_form_data()

    description = form['Brand Description (Long)']
    product_category = form['Product Category']
    target_audience = form['Target Audience']
    
    prompt_data = {
        'description_long': description,
        'product_category':product_category,
        'target_audience':target_audience,
        'campaign_goals':campaign_goals,
        'target_market':target_market
    }

    return process_chain(strategy.prompt_why_mission_values, prompt_data)

def get_strategy_mapping():
    return process_chain(strategy.prompt_strategy_phases_mapping)

def get_marketing_objectives(campaign_goals):
    return process_chain(strategy.prompt_marketing_objectives,campaign_goals)

def get_marketing_plan():
    return process_chain(strategy.prompt_marketing_plan)

import streamlit as st
from utils import *

st.title('Business Profile Creation')
website_url = st.text_input('Insert Website URL Here')

if website_url:
    html = scraper.scrape_website_content(website_url)
    website_doc = scraper.clean_website_content(html)
    texts = embeddings.website_text_splitter(website_doc)
    db = embeddings.create_vector_database(texts)
    embeddings.save_vector_database(db,'data/feiss_db')
    prompt_description_long = prompts.prompt_website_description_long
    prompt = prompt_builder.get_prompt_template(prompt_description_long)
    finalized_description_prompt = prompt.format(websiteURL=website_url)
    qa = chains.initialize_qa_chain(db)
    description = chains.run_qa_chain(qa,finalized_description_prompt)

    st.header("Business Description")
    st.write(description)

    # prompt_description_short = prompts.prompt_website_description_short
    # summarizer = chains.initialize_llm_chain(prompt_description_short)
    # description_short = chains.run_llm_chain(summarizer,description)

    # st.header("Description (Short)")
    # st.write(description_short)

    # prompt_audience_persona = prompts.prompt_audience_persona
    # chain_audience_persona = chains.initialize_llm_chain(prompt_audience_persona)
    # audience_persona = chains.run_llm_chain(chain_audience_persona,description)

    # st.header("Audience Persona")
    # st.write(audience_persona)




    


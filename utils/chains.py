#Import LLMs
from langchain.chains import RetrievalQA, LLMChain
from langchain.llms import OpenAI

from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

def initialize_qa_chain(database):
    qa = RetrievalQA.from_chain_type(llm=OpenAI(),chain_type="stuff",retriever=database.as_retriever())
    return qa

def initialize_llm_chain(prompt_template):
    chain = LLMChain(llm=OpenAI(),prompt=prompt_template)
    return chain

def run_llm_chain(chain,input_variable):
    result = chain.run(input_variable)
    return result

def run_qa_chain(chain,query):
    result = chain.run(query)
    return result
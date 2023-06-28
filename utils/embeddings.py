from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def website_text_splitter(website_content):
    web_doc = Document(page_content=website_content)

    text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 1000,
    chunk_overlap  = 100,
    )

    texts = text_splitter.create_documents([web_doc.page_content])
    return texts

def create_vector_database(docs):
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(docs, embeddings)

    return db

def save_vector_database(db,filename):
    db.save_local(filename)


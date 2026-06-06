import os

from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()


def create_vector_store(chunks):

    api_key = os.getenv("OPENAI_API_KEY")

    embeddings = OpenAIEmbeddings(
        api_key=api_key
    )

    vector_store = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings
    )

    return vector_store
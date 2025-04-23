import os
import sys
from groq import Groq
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

##Importing the documents

pages = []

loader = PyPDFLoader(r"D:\desktop\NeoSoft\SL\RAGBOT\RagBot\data\Optimization_of_energy_performance_with_renewable_.pdf")

for page in loader.lazy_load():
    pages.append(page)

def preprocess_data(list_of_documents):

    for i in list_of_documents:
        text = i.lower()
        
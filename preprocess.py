import os
import sys
from groq import Groq
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
import nltk
import string

from nltk.corpus import stopwords

pages = []

stopwords = stopwords.words("english")
punctuations = string.punctuation


loader = PyPDFLoader(r"D:\desktop\NeoSoft\SL\RAGBOT\RagBot\data\OptimizingEnergyEfficiencyTheSynergyofPower-SavingModesandArtificialIntelligence.pdf")

for page in loader.lazy_load():
    pages.append(page.page_content.lower().strip())





    
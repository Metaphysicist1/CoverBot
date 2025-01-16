import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter


load_dotenv('.config')
key = os.environ.get('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
    temperature=0.5,
    max_tokens=10000,
    timeout=45,
    max_retries=2,
    google_api_key=key,
)

@st.cache_resource
def load_pdf():
    pdf_name = "Motivation_Letter.pdf"
    loaders = [PyPDFLoader(pdf_name)]
    index = VectorstoreIndexCreator(
        embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2"),
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0),
    ).from_loaders(loaders)

    return index

index = load_pdf()  

# Create Chain
chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever =index.vectorstore.as_retriever(),
        input_key='question',
        )

from langchain_core.documents import Document
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
load_dotenv()
class load_file:
    def __init__(self):
        self.file_path = "Rag.txt"
    def to_chunk(self):
        loader = TextLoader(self.file_path, encoding="utf-8")
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )
        chunks = text_splitter.split_documents(docs)
        return chunks


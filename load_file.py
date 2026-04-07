import os

from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()

class load_file:
    def __init__(self):

        self.file_path = "Rag.txt"

    def to_chunk(self):
        loader = TextLoader(self.file_path, encoding="utf-8")
        docs = loader.load()
        embeddings = OllamaEmbeddings(
            model=os.getenv('MODEL_EMBED'),
            base_url=os.getenv('BASE_URL'),
            client_kwargs={
                "headers": {
                    "CF-Access-Client-Id": os.getenv('CLIENT_ID'),
                    "CF-Access-Client-Secret": os.getenv('CLIENT_SECRET'),
                }
            })
        text_splitter = SemanticChunker(
            embeddings,
            breakpoint_threshold_type="percentile"
        )
        chunks = text_splitter.split_documents(docs)
        return chunks


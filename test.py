import load_file
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
load_dotenv()
embeddings = OllamaEmbeddings(
            model=os.getenv('MODEL_EMBED'),
            base_url=os.getenv('BASE_URL'),
            client_kwargs={
                "headers": {
                    "CF-Access-Client-Id": os.getenv('CLIENT_ID'),
                    "CF-Access-Client-Secret": os.getenv('CLIENT_SECRET'),
                }
            }
)
print(embeddings.embed_query("hello"))

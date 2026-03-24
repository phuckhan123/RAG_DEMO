import load_file
import os
from dotenv import load_dotenv
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
load_dotenv()
class ollama_embeddings :
    def __init__(self,query):
        self.query=query
        # self.embeddings = OllamaEmbeddings(model='nomic-embed-text',
        #                                    base_url= "https://ollama.binhphuc-homelab.io.vn",
        #                                    client_kwargs={
        #                                 "headers":  = {
        #     "CF-Access-Client-Id": "a2ba34bce6609e562f451171a63decf5.access",
        #     "CF-Access-Client-Secret": "52ceab3d73d63fd4d4e3426d6ef6fbfea1eb87467225ad5a0eb7c01f99993625",
        # }
        # }
        #                                    )
        self.embeddings = OllamaEmbeddings(
            model=os.getenv('MODEL_EMBED'),
            base_url=os.getenv('BASE_URL'),
            client_kwargs={
                "headers": {
                    "CF-Access-Client-Id": os.getenv('CLIENT_ID'),
                    "CF-Access-Client-Secret": os.getenv('CLIENT_SECRET'),
                }
            }
        )


        loader = load_file.load_file()
        self.chunks = loader.to_chunk()
        self.vectorstore = InMemoryVectorStore.from_documents(
            documents=self.chunks,
            embedding=self.embeddings
        )
    def retrive_documents(self):
        retriver = self.vectorstore.as_retriever()
        retrived_documents = retriver.invoke(self.query)
        return retrived_documents






#
# embeddings = OllamaEmbeddings(
#     model='embeddinggemma',
# )
# chunks = load_file.chunks
#
# vectorstore = InMemoryVectorStore.from_documents(
#     documents=chunks,
#     embedding=embeddings
# )
# print(q)
# # retriever = vectorstore.as_retriever()
# # retrieved_documents = retriever.invoke(my_query)
# # print(retrieved_documents)
#
#

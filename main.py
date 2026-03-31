import textwrap
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from ollama_embedding import ollama_embeddings
load_dotenv()
class Main:
    def __init__(self, model,query,retriver_document, base_url,headers,messages):
        self.retriver_document = retriver_document
        self.query =  query
        self.model = model
        self.base_url = base_url
        self.headers = headers
        self.messages = messages

    def build_messages(self):
        self.messages.append({'role': 'user', 'content': f"Question: {self.query} ,Context ={self.retriver_document}"})
        return self.messages

    def run_query(self):
        llm = ChatOllama(
            model=self.model,
            base_url=self.base_url,
            client_kwargs={
                "headers": {
                    "CF-Access-Client-Id": os.getenv("CLIENT_ID"),
                    "CF-Access-Client-Secret": os.getenv("CLIENT_SECRET"),
                }
            }
        )
        response = llm.invoke(self.build_messages())
        self.messages.append({'role': 'system', 'content': response.content})
        wrapped = textwrap.fill(response.content, width=80)
        print(wrapped)
if __name__ == '__main__':
    messages = [{'role': 'system', 'content': "You must answer the question based on the context below. Do not repeat the context. Give a short and clear answer"}]
    while True:
        query=input("Enter a query: ")
        retriver = ollama_embeddings(query=query)
        retriver_document = []
        for doc in retriver.retrive_documents():
            retriver_document.append(doc.page_content)
        base_url = os.getenv("BASE_URL")
        headers = {
            "CF-Access-Client-Id": os.getenv("CLIENT_ID"),
            "CF-Access-Client-Secret": os.getenv("CLIENT_SECRET"),
        }
        app = Main(model=os.getenv("MODEL"),query=query,retriver_document=retriver_document, base_url=base_url, headers=headers,messages=messages)
        app.run_query()
#what is rag?

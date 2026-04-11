import textwrap
import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from ollama_embedding import ollama_embeddings
load_dotenv()

class Main:
    def __init__(self, model,query, base_url,headers,messages):

        self.query =  query
        self.model = model
        self.base_url = base_url
        self.headers = headers
        self.messages = messages

    def build_messages(self):
        retriver = ollama_embeddings(query=self.query)
        retriver_document = []
        for doc in retriver.retrive_documents():
            retriver_document.append(doc.page_content)
        context = "\n\n".join(retriver_document)
        self.messages.append({
            'role': 'user',
            'content': f"Context:\n{context}\n\nQuestion: {self.query}"
        })

        return self.messages

    def run_query(self):
        llm = ChatOllama(
            model=self.model,
            base_url=self.base_url,
            temperature=0,
            client_kwargs={
                "headers": {
                    "CF-Access-Client-Id": os.getenv("CLIENT_ID"),
                    "CF-Access-Client-Secret": os.getenv("CLIENT_SECRET"),
                }
            }
        )
        response = llm.invoke(self.build_messages())
        self.messages.append({'role': 'assistant', 'content': response.content})
        wrapped = textwrap.fill(response.content, width=80)
        return wrapped


def response(app: Main):
        return app.run_query()


if __name__ == '__main__':
    messages = [{'role': 'system',
                 'content': "You must answer the question based on the context below. Do not repeat the context. Give a short and clear answer"}]
    base_url = os.getenv("BASE_URL")
    headers = {
        "CF-Access-Client-Id": os.getenv("CLIENT_ID"),
        "CF-Access-Client-Secret": os.getenv("CLIENT_SECRET"),
    }
    query = input("Enter your question: ")
    llm = Main(model=os.getenv("MODEL"),query=query, base_url=base_url, headers=headers,messages=messages )
    print(response(llm))

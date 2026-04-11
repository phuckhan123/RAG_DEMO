import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import main
load_dotenv()
app = FastAPI()

messages = [{'role': 'system',
                 'content': "You must answer the question based on the context below. Do not repeat the context. Give a short and clear answer"}]
base_url = os.getenv("BASE_URL")
headers = {
        "CF-Access-Client-Id": os.getenv("CLIENT_ID"),
        "CF-Access-Client-Secret": os.getenv("CLIENT_SECRET"),
    }

llm = main.Main(model=os.getenv("MODEL"), query=None, base_url=base_url, headers=headers, messages=messages)

class User(BaseModel):
    name: str
class Query(BaseModel):
    mess: str


@app.get("/aa")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.post("/hello")
def hello(user: User):
    return {"hello user name": user.name}

@app.post("/llm")
def answer(query: Query):
    llm.query = query.mess
    return main.response(llm)
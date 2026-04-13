import time
import matplotlib.pyplot as plt
import requests
import streamlit as st
import numpy as np
import pandas as pd
# st.title("Hello Streamlit-er 👋")
# st.caption("🚀 A chatbot powered by RAG")
with st.sidebar:
    st.title("Settings")
    name = st.text_input("Name")
    age = st.slider("Age", 1, 100)

st.title("💬 Chatbot")
st.caption("🚀 A Streamlit chatbot powered by RAG")
url = "http://127.0.0.1:8000/llm"

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
question = st.text_input("Question: ")

if st.button("Send question "):
    st.session_state.messages.append({"role": "user", "content": question})
    payload = {
           "mess": question,
    }
    st.chat_message("user").write(question)
    with st.spinner("Wait for it...", show_time=True):
     response = requests.post(url, json= payload)
     st.session_state.messages.append({"role": "assistant", "content": response.text})
    if response.status_code == 200:
            st.balloons()
            st.chat_message("assistant").write(response.text)

    else :
            st.error(f"Wrong: \n{ response.status_code }")


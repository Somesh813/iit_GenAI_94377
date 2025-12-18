import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL="https://api.groq.com/openai/v1/chat/completions"
LM_STUDIO_URL="http://127.0.0.1:1234/v1/chat/completions"

GROQ_MODEL="llama-3.3-70b-versatile"
LM_STUDIO_MODEL="phi-3-mini-4k-instruct" 

st.set_page_config(page_title="Groq vs LM Studio Chat", layout="centered")
st.title("LLM Chat App")

with st.sidebar:
    st.header("⚙️ Settings")
    llm_choice=st.radio(
        "Select LLM Backend",
        ["Groq (Cloud)", "LM Studio (Local)"]
    )

    st.markdown("---")
    st.markdown("**Chat History Controls**")
    if st.button("🗑 Clear Chat"):
        st.session_state.messages=[]

if "messages" not in st.session_state:
    st.session_state.messages=[]

def call_groq(messages):
    headers={
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload={
        "model": GROQ_MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    response = requests.post(GROQ_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def call_lm_studio(messages):
    headers={"Content-Type": "application/json"}

    payload={
        "model": LM_STUDIO_MODEL,
        "messages": messages,
        "temperature": 0.7
    }

    response=requests.post(LM_STUDIO_URL, json=payload, headers=headers)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask your question...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                if llm_choice == "Groq (Cloud)":
                    reply = call_groq(st.session_state.messages)
                else:
                    reply = call_lm_studio(st.session_state.messages)

                st.markdown(reply)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": reply
                })

            except Exception as e:
                st.error(f"Error: {e}")

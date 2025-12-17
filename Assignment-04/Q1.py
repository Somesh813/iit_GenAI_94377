import streamlit as st
import time
if "messages" not in st.session_state:
    st.session_state.messages = []


with st.sidebar:
    st.header("Settings")
    mode = st.selectbox("Select mode", ["upper", "lower", "toggle"])

st.title("ChatBot")

def stream_reply(text):
    for ch in text:
        yield ch
        time.sleep(0.05)

msg = st.chat_input("Say something...")

if msg:
    if mode=="upper":
        reply=msg.upper()
    elif mode=="lower":
        reply=msg.lower()
    else:
        reply=msg.swapcase()

    st.session_state.messages.append(("user", msg))
    st.session_state.messages.append(("bot", reply))

for role, message in st.session_state.messages:
    with st.chat_message(role):
        if role == "bot":
            st.write_stream(stream_reply(message))
        else:
            st.write(message)

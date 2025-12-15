import streamlit as st

st.set_page_config(page_title="Sunbeam Chatbot", page_icon="🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("⚙️ Settings")

    mode = st.selectbox(
        "Select Mode",
        ["Upper", "Lower", "Toggle"]
    )

    count = st.slider(
        "Message Count",
        min_value=2,
        max_value=10,
        value=6,
        step=2
    )

    st.subheader("Config Preview")
    st.json({"mode": mode, "count": count})

st.title("💬 Sunbeam Chatbot")

for message in st.session_state.messages[-count:]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    if mode == "Upper":
        bot_response = user_input.upper()
    elif mode == "Lower":
        bot_response = user_input.lower()
    else:
        bot_response = user_input.swapcase()

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })


    st.rerun()


import streamlit as st
from google import genai

# Gemini client — API key Streamlit Secrets se lega
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

st.set_page_config(
    page_title="Evil GPT",
    page_icon="🤖"
)

st.title("🤖 Evil GPT")
st.caption("Smart AI Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purani messages dikhao
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask anything..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Conversation ko model ke liye context me bhejna
    conversation = """
You are Evil GPT, a highly capable, helpful and intelligent AI assistant.
Answer clearly and naturally.
You can communicate in Hindi, Hinglish and English.
For coding questions, give practical working code.
Do not claim to have abilities you don't actually have.

Conversation:
"""

    for msg in st.session_state.messages:
        conversation += f"\n{msg['role']}: {msg['content']}"

    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=conversation
            )

            answer = response.text
            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:
            st.error("AI se connection nahi ho pa raha. Streamlit Secrets me GEMINI_API_KEY check karo.")

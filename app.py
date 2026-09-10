from google import genai
import streamlit as st

client = genai.Client(api_key="AQ.Ab8RN6Kw9r70bRlfZYniekYVrlw-LyfKRroPgVut8vLvZdiFNw")

st.title("Evil GPT")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

import google.generativeai as genai
import streamlit as st

# अपनी Gemini API Key यहाँ डालें
genai.configure(api_key="YOUR_API_KEY_HERE")

st.title("Evil GPT")
model = genai.GenerativeModel("gemini-1.5-flash")

if "messages" not in st.session_state:
  st.session_state.messages = []

for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])

if prompt := st.chat_input("Ask anything..."):
  st.session_state.messages.append({"role": "user", "content": prompt})
  with st.chat_message("user"):
    st.markdown(prompt)

  response = model.generate_content(prompt)
  answer = response.text

  with st.chat_message("assistant"):
    st.markdown(answer)
  st.session_state.messages.append({"role": "assistant", "content": answer})

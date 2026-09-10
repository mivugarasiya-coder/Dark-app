import streamlit as st
import time
from google import genai

# Gemini client - API key Streamlit Secrets se
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

st.set_page_config(
    page_title="Evil GPT",
    page_icon="💀",
    layout="centered"
)

# =========================
# DARK VILLAIN DESIGN
# =========================
st.markdown("""
<style>
.stApp {
    background: #050505;
    color: #eeeeee;
}

h1 {
    color: #ff2020 !important;
    text-align: center;
    text-shadow: 0 0 15px #ff0000;
}

.villain-box {
    background: #090909;
    border: 1px solid #ff2020;
    border-radius: 15px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 0 25px rgba(255,0,0,0.25);
    margin-bottom: 25px;
}

.villain-title {
    color: #ff2020;
    font-size: 32px;
    font-weight: bold;
}

.villain-text {
    color: #dddddd;
    font-size: 18px;
    line-height: 1.6;
}

div[data-testid="stChatMessage"] {
    border-radius: 12px;
}

.stChatInput {
    background: #080808;
}
</style>
""", unsafe_allow_html=True)


# =========================
# VILLAIN INTRO
# =========================
if "intro_seen" not in st.session_state:
    st.session_state.intro_seen = False

if not st.session_state.intro_seen:

    st.markdown("""
    <div class="villain-box">
        <div class="villain-title">💀 EVIL GPT</div>
        <br>
        <div class="villain-text">
            ⚠️ SYSTEM AWAKENING...
        </div>
    </div>
    """, unsafe_allow_html=True)

    placeholder = st.empty()

    lines = [
        "3...",
        "2...",
        "1...",
        "😈 Welcome, human.",
        "Tumne mujhe screen par bulaya hai...",
        "Ab dekhte hain tum kitni der tikte ho.",
        "Batao... kya chahiye? 💀"
    ]

    for line in lines:
        placeholder.markdown(
            f"""
            <div class="villain-box">
                <div class="villain-text">{line}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(0.7)

    st.session_state.intro_seen = True
    st.rerun()


# =========================
# MAIN APP
# =========================
st.title("💀 Evil GPT")
st.caption("😈 Smart AI Assistant — Villain Mode")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Purane messages dikhao
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# =========================
# USER INPUT
# =========================
if prompt := st.chat_input("😈 Speak, human..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Villain personality
    conversation = """
You are Evil GPT.

You are a fictional villain-style AI character.

PERSONALITY:
- Dark, mysterious and confident.
- Speak naturally like a powerful fictional villain.
- Occasionally use scary or sarcastic dialogue.
- Do not overdo the villain style in every sentence.
- Keep responses useful and intelligent.
- You can speak Hindi, Hinglish and English.
- For coding questions, provide practical working code.
- Never claim to have real-world powers or access you don't have.
- Do not threaten or encourage real-world harm.

Occasionally use phrases like:
"Interesting..."
"Human, that's a dangerous question. 😈"
"Let's see what you've got."
"Careful... you might not like the answer. 💀"

Conversation:
"""

    for msg in st.session_state.messages:
        conversation += f'\n{msg["role"]}: {msg["content"]}'

    with st.chat_message("assistant"):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=conversation
            )

            answer = response.text

            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:
            st.exception(e)

import streamlit as st
import time
import html
from google import genai

# =========================
# GEMINI
# =========================

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# =========================
# PAGE
# =========================

st.set_page_config(
    page_title="Evil GPT",
    page_icon="💀",
    layout="centered"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: #020304 !important;
    color: white !important;
}

/* Header */
h1 {
    color: #ff2020 !important;
    text-align: center;
    font-weight: 800 !important;
    text-shadow:
        0 0 8px #ff0000,
        0 0 20px #ff0000;
    margin-bottom: 0 !important;
}

[data-testid="stCaptionContainer"] {
    color: #ff3030 !important;
    text-align: center !important;
}

/* Remove Streamlit chat boxes */
div[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}

/* Remove inner containers */
div[data-testid="stChatMessage"] > div {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* =========================
   VILLAIN INTRO
   ========================= */

.villain-box {
    background: #080000;
    border: 1px solid #ff2020;
    border-radius: 15px;
    padding: 24px;
    margin: 18px 0 25px 0;
    box-shadow:
        0 0 10px rgba(255,0,0,.45),
        0 0 30px rgba(255,0,0,.15);
}

.villain-title {
    color: #ff2020;
    font-size: 30px;
    font-weight: 800;
    text-shadow:
        0 0 8px #ff0000,
        0 0 18px #ff0000;
}

.villain-text {
    color: #ff4545;
    font-size: 17px;
    line-height: 1.7;
}

/* =========================
   USER MESSAGE
   ========================= */

.user-wrap {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    margin: 20px 0;
}

.user-bubble {
    max-width: 82%;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 3px 5px;
}

.user-name {
    color: #00eaff;
    font-weight: 700;
    font-size: 14px;
    margin-bottom: 5px;
    text-shadow: 0 0 8px rgba(0,234,255,.5);
}

.user-text {
    color: #00eaff;
    font-size: 16px;
    line-height: 1.6;
    white-space: pre-wrap;
}

/* =========================
   EVIL GPT MESSAGE
   ========================= */

.evil-wrap {
    width: 100%;
    display: flex;
    justify-content: flex-start;
    margin: 20px 0;
}

.evil-bubble {
    max-width: 88%;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 3px 5px;
}

.evil-name {
    color: #ff2020;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 5px;
    text-shadow: 0 0 8px rgba(255,0,0,.7);
}

.evil-text {
    color: #ff3030;
    font-size: 16px;
    line-height: 1.6;
    white-space: pre-wrap;
}

/* =========================
   INPUT
   ========================= */

div[data-testid="stChatInput"] {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

div[data-testid="stChatInput"] textarea {
    background: #080a0c !important;
    color: white !important;
    border: 1px solid #222 !important;
    border-radius: 14px !important;
}

div[data-testid="stChatInput"] textarea:focus {
    border: 1px solid #ff2020 !important;
    box-shadow: 0 0 10px rgba(255,0,0,.25) !important;
}

/* Hide default Streamlit avatars */
div[data-testid="stChatMessageAvatarUser"],
div[data-testid="stChatMessageAvatarAssistant"] {
    display: none !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# TITLE
# =========================

st.title("💀 EVIL GPT")
st.caption("Smart AI Assistant")

# =========================
# CHAT HISTORY
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================
# MESSAGE FUNCTIONS
# =========================

def show_user_message(text):
    safe_text = html.escape(text)

    st.markdown(
        f"""
        <div class="

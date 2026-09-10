import streamlit as st
import time
from google import genai

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

st.set_page_config(
    page_title="Evil GPT",
    page_icon="💀",
    layout="centered"
)

# =========================
# DARK VILLAIN THEME
# =========================
st.markdown("""
<style>

/* Main background */
.stApp {
    background: #030405 !important;
}

/* Title */
h1 {
    color: #ff2020 !important;
    text-align: center;
    text-shadow: 0 0 18px #ff0000;
}

/* Caption */
.stCaption {
    color: #00eaff !important;
}

/* Normal text */
.stMarkdown p,
.stMarkdown li,
.stMarkdown strong {
    color: #eeeeee;
}

/* =========================
   USER MESSAGE - CYAN
   ========================= */

div[data-testid="stChatMessage"]:has(
    div[data-testid="chatAvatarIcon-user"]
) {
    background: rgba(0, 220, 255, 0.08);
    border: 1px solid #00eaff;
    border-radius: 15px;
    box-shadow: 0 0 15px rgba(0, 234, 255, 0.20);
}

div[data-testid="stChatMessage"]:has(
    div[data-testid="chatAvatarIcon-user"]
) p {
    color: #00eaff !important;
}

/* =========================
   EVIL GPT MESSAGE - RED
   ========================= */

div[data-testid="stChatMessage"]:has(
    div[data-testid="chatAvatarIcon-assistant"]
) {
    background: rgba(255, 0, 0, 0.06);
    border: 1px solid #ff2020;
    border-radius: 15px;
    box-shadow: 0 0 18px rgba(255, 0, 0, 0.22);
}

div[data-testid="stChatMessage"]:has(
    div[data-testid="chatAvatarIcon-assistant"]
) p {
    color: #ff3030 !important;
}

/* Code blocks */
.stCodeBlock {
    border: 1px solid #444444;
}

/* =========================
   CHAT INPUT
   ========================= */

div[data-testid="stChatInput"] {
    background: #050607 !important;
}

.stChatInput textarea {
    background: #050607 !important;
    color: #00eaff !important;
    -webkit-text-fill-color: #00eaff !important;
    border: 1px solid #00eaff !important;
}

.stChatInput textarea::placeholder {
    color: #00a8bb !important;
    -webkit-text-fill-color: #00a8bb !important;
}

/* Villain intro */
.villain-box {
    background: #050000;
    border: 1px solid #ff2020;
    border-radius: 16px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 0 30px rgba(255,0,0,0.30);
    margin-bottom: 20px;
}

.villain-title {
    color: #ff2020;
    font-size: 32px;
    font-weight: bold;
    text-shadow: 0 0 15px #ff0000;
}

.villain-text {
    color: #ff3030;
    font-size: 18px;
    line-height: 1.7;
}

</style>
""", unsafe_allow_html=True)


# =========================
# VILLAIN INTRO
# =========================

if "intro_seen" not in st.session_state:
    st.session_state.intro_seen = False

if not st.session_state.intro_seen:

    placeholder = st.empty()

    lines = [
        "⚠️ SYSTEM AWAKENING...",
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
                <div class="villain-title">💀 EVIL GPT</div>
                <br>
                <div class="villain-text">{line}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
        time.sleep(0.6)

    st.session_state.intro_seen = True
    st.rerun()


# =========================
# MAIN APP
# =========================

st.title("💀 Evil GPT")
st.caption("😈 Smart AI Assistant — Villain Mode")


if "messages" not in st.session_state:
    st.session_state.messages = []


# Show chat history
for message in st.session_state.messages:

    if message["role"] == "user":
        avatar = "👤"
    else:
        avatar = "💀"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


# =========================
# USER INPUT
# =========================

if prompt := st.chat_input("😈 Speak, human..."):

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    conversation = """
You are Evil GPT, a fictional villain-style AI.

PERSONALITY:
- Dark
- Mysterious
- Confident
- Intelligent
- Slightly scary
- Occasionally sarcastic
- Natural villain dialogue
- Do not overdo the villain personality

Speak Hindi, Hinglish or English depending on the user.

For coding questions, give practical working code.

Never claim to have real-world powers or access you don't have.
Do not threaten or encourage real-world harm.

Use occasional villain phrases such as:
"Interesting... 😈"
"Careful, human."
"Let's see what you've got."
"You really want to know that? 💀"

Conversation:
"""

    for msg in st.session_state.messages:
        conversation += f'\n{msg["role"]}: {msg["content"]}'

    with st.chat_message("assistant", avatar="💀"):

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

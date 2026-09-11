import streamlit as st
import html
from google import genai

# =========================
# GEMINI
# =========================

client = genai.Client(
    api_key=st.secrets["OPENAI_API_KEY"]
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

st.markdown(
    """
    <style>

    .stApp {
        background: #020304 !important;
        color: white !important;
    }

    h1 {
        color: #ff2020 !important;
        text-align: center !important;
        font-weight: 800 !important;
        text-shadow: 0 0 8px #ff0000, 0 0 20px #ff0000;
        margin-bottom: 0 !important;
    }

    [data-testid="stCaptionContainer"] {
        color: #ff3030 !important;
        text-align: center !important;
    }

    /* Streamlit default message box remove */
    div[data-testid="stChatMessage"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    div[data-testid="stChatMessage"] > div {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    /* Hide avatars */
    div[data-testid="stChatMessageAvatarUser"],
    div[data-testid="stChatMessageAvatarAssistant"] {
        display: none !important;
    }

    /* USER */
    .user-wrap {
        width: 100%;
        display: flex;
        justify-content: flex-end;
        margin: 16px 0;
    }

    .user-content {
        max-width: 82%;
        padding: 3px 5px;
        background: transparent;
        border: none;
        box-shadow: none;
    }

    .user-name {
        color: #00eaff;
        font-size: 14px;
        font-weight: 700;
        margin-bottom: 4px;
        text-shadow: 0 0 7px #00eaff;
    }

    .user-text {
        color: #00eaff;
        font-size: 16px;
        line-height: 1.5;
        white-space: pre-wrap;
    }

    /* EVIL GPT */
    .evil-wrap {
        width: 100%;
        display: flex;
        justify-content: flex-start;
        margin: 16px 0;
    }

    .evil-content {
        max-width: 88%;
        padding: 3px 5px;
        background: transparent;
        border: none;
        box-shadow: none;
    }

    .evil-name {
        color: #ff2020;
        font-size: 14px;
        font-weight: 800;
        margin-bottom: 4px;
        text-shadow: 0 0 7px #ff0000;
    }

    .evil-text {
        color: #ff3030;
        font-size: 16px;
        line-height: 1.5;
        white-space: pre-wrap;
    }

    /* INPUT */
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
        box-shadow: 0 0 8px rgba(255, 0, 0, 0.25) !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

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
# DISPLAY FUNCTIONS
# =========================

def show_user_message(text):
    safe_text = html.escape(text)

    st.markdown(
        f"""
        <div class="user-wrap">
            <div class="user-content">
                <div class="user-name">👤 You</div>
                <div class="user-text">{safe_text}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_evil_message(text):
    safe_text = html.escape(text)

    st.markdown(
        f"""
        <div class="evil-wrap">
            <div class="evil-content">
                <div class="evil-name">💀 Evil GPT</div>
                <div class="evil-text">{safe_text}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# OLD CHAT
# =========================

for message in st.session_state.messages:

    if message["role"] == "user":
        show_user_message(message["content"])
    else:
        show_evil_message(message["content"])


# =========================
# INPUT
# =========================

prompt = st.chat_input("Ask anything...")

if prompt:

    # Show user immediately
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    show_user_message(prompt)

    # =========================
    # LIGHTWEIGHT PROMPT
    # =========================

    conversation = """
You are Evil GPT.

You are a dark, intelligent, slightly sarcastic fictional villain-style AI.

Be helpful and answer naturally in Hindi, Hinglish or English.

Keep answers concise unless the user asks for detail.

For coding questions, provide practical working code.

Never claim real-world powers or access you do not have.
Do not threaten or encourage real-world harm.

Conversation:
"""

    # Sirf recent 10 messages bhejo
    recent_messages = st.session_state.messages[-10:]

    for message in recent_messages:
        conversation += (
            "\n"
            + message["role"]
            + ": "
            + message["content"]
        )

    # =========================
    # GEMINI
    # =========================

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=conversation
        )

        answer = response.text

        show_evil_message(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

    except Exception as e:

        st.error("⚠️ AI Error")
        st.exception(e)

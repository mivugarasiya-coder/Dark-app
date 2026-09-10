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

st.set_page_config(
    page_title="Evil GPT",
    page_icon="💀",
    layout="centered"
)

# =========================
# DARK UI
# =========================

st.markdown("""
<style>

/* ---------- MAIN ---------- */

.stApp {
    background: #020304 !important;
    color: #ffffff !important;
}

header[data-testid="stHeader"] {
    background: #020304 !important;
}

/* ---------- TITLE ---------- */

h1 {
    color: #ff2020 !important;
    text-align: center;
    font-weight: 800 !important;
    text-shadow:
        0 0 8px #ff0000,
        0 0 20px #ff0000;
    margin-bottom: 0 !important;
}

.stCaption {
    color: #ff3030 !important;
    text-align: center !important;
}

/* ---------- REMOVE DEFAULT CHAT STYLE ---------- */

div[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
}

/* ---------- VILLAIN INTRO ---------- */

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

/* ---------- USER MESSAGE ---------- */

.user-wrap {
    width: 100%;
    display: flex;
    justify-content: flex-end;
    margin: 14px 0;
}

.user-bubble {
    width: fit-content;
    max-width: 82%;
    background: #031416;
    border: 1px solid #00eaff;
    border-radius: 16px;
    padding: 12px 16px;
    color: #00eaff;
    box-shadow:
        0 0 8px rgba(0,234,255,.35),
        inset 0 0 12px rgba(0,234,255,.04);
}

.user-name {
    color: #00eaff;
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 6px;
}

.user-text {
    color: #00eaff;
    font-size: 16px;
    line-height: 1.55;
    white-space: pre-wrap;
}

/* ---------- EVIL GPT MESSAGE ---------- */

.evil-wrap {
    width: 100%;
    display: flex;
    justify-content: flex-start;
    margin: 14px 0;
}

.evil-bubble {
    width: fit-content;
    max-width: 88%;
    background: #100303;
    border: 1px solid #ff2020;
    border-radius: 16px;
    padding: 13px 17px;
    color: #ff3b3b;
    box-shadow:
        0 0 9px rgba(255,0,0,.40),
        inset 0 0 14px rgba(255,0,0,.04);
}

.evil-name {
    color: #ff2020;
    font-weight: 800;
    font-size: 14px;
    margin-bottom: 7px;
    text-shadow: 0 0 8px rgba(255,0,0,.7);
}

.evil-text {
    color: #ff3b3b;
    font-size: 16px;
    line-height: 1.6;
    white-space: pre-wrap;
}

/* ---------- CODE ---------- */

.code-box {
    background: #05090d;
    border: 1px solid #34495e;
    border-radius: 9px;
    margin-top: 10px;
    padding: 12px;
    overflow-x: auto;
}

.code-box pre {
    color: #8be9fd;
    margin: 0;
    white-space: pre-wrap;
    font-family: monospace;
    font-size: 13px;
}

/* ---------- INPUT ---------- */

div[data-testid="stChatInput"] {
    background: #030506 !important;
    border: 1px solid #00eaff !important;
    border-radius: 15px !important;
    box-shadow: 0 0 12px rgba(0,234,255,.20) !important;
}

.stChatInput textarea {
    background: #030506 !important;
    color: #00eaff !important;
    -webkit-text-fill-color: #00eaff !important;
    caret-color: #00eaff !important;
}

.stChatInput textarea::placeholder {
    color: #008fa3 !important;
    -webkit-text-fill-color: #008fa3 !important;
}

/* ---------- MOBILE ---------- */

@media (max-width: 600px) {

    .user-bubble {
        max-width: 88%;
    }

    .evil-bubble {
        max-width: 92%;
    }

    .user-text,
    .evil-text {
        font-size: 15px;
    }

    .villain-title {
        font-size: 26px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================
# MESSAGE HTML
# =========================

def show_user_message(text):

    safe_text = html.escape(text)

    st.markdown(
        f"""
        <div class="user-wrap">
            <div class="user-bubble">
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
            <div class="evil-bubble">
                <div class="evil-name">💀 Evil GPT</div>
                <div class="evil-text">{safe_text}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# VILLAIN INTRO
# =========================

if "intro_seen" not in st.session_state:
    st.session_state.intro_seen = False

if not st.session_state.intro_seen:

    box = st.empty()

    intro_lines = [
        "⚠️ SYSTEM AWAKENING...",
        "3...",
        "2...",
        "1...",
        "😈 Welcome, human.",
        "Tumne mujhe screen par bulaya hai...",
        "Ab dekhte hain tum kitni der tikte ho.",
        "Batao... kya chahiye? 💀"
    ]

    for line in intro_lines:

        box.markdown(
            f"""
            <div class="villain-box">
                <div class="villain-title">
                    💀 EVIL GPT
                </div>

                <div class="villain-text">
                    {line}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.55)

    st.session_state.intro_seen = True
    st.rerun()


# =========================
# HEADER
# =========================

st.title("💀 Evil GPT")
st.caption("Smart AI Assistant — Villain Mode")


# =========================
# CHAT HISTORY
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    if message["role"] == "user":
        show_user_message(message["content"])

    else:
        show_evil_message(message["content"])


# =========================
# USER INPUT
# =========================

if prompt := st.chat_input("😈 Speak, human..."):

    # User message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    show_user_message(prompt)


    # =========================
    # VILLAIN PERSONALITY
    # =========================

    conversation = """
You are Evil GPT, a fictional villain-style AI assistant.

PERSONALITY:
- Dark
- Mysterious
- Confident
- Intelligent
- Slightly intimidating
- Sarcastic sometimes
- Cinematic villain personality
- Still helpful and useful

Speak naturally in Hindi, Hinglish or English according to the user.

Do not put a villain dialogue in every sentence.
Use the villain personality naturally.

Examples of your style:

"Interesting... 😈"

"Careful, human."

"Let's see what you've got."

"You really want to know that? 💀"

"Ab asli sawaal shuru hua hai..."

For coding questions:
Give practical, working code.

Never claim to have real-world powers, access,
or abilities that you don't actually have.

Do not threaten or encourage real-world harm.

Conversation:
"""

    for msg in st.session_state.messages:

        conversation += (
            f'\n{msg["role"]}: {msg["content"]}'
        )


    # =========================
    # GEMINI RESPONSE
    # =========================

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=conversation
        )

        answer = response.text

        show_evil_message(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })


    except Exception as e:

        show_evil_message(
            "Something went wrong, human... 💀"
        )

        st.error(str(e))

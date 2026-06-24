import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

# ------------------------
# CONFIG
# ------------------------

load_dotenv()

st.set_page_config(page_title="Mistral AI", page_icon="🤖", layout="wide")

# ------------------------
# CSS
# ------------------------

st.markdown(
    """
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 50%,
        #312e81 100%
    );
}

header, footer {
    visibility:hidden;
}

section[data-testid="stSidebar"]{
    background: rgba(255,255,255,0.06);
    backdrop-filter: blur(20px);
}

.hero{
    text-align:center;
    padding:20px;
}

.hero h1{
    color:white;
    font-size:3rem;
    margin-bottom:8px;
}

.hero p{
    color:#cbd5e1;
}

.message-card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(20px);
    border-radius:20px;
    padding:15px;
    margin-bottom:10px;
}

.stChatMessage{
    animation: fadeIn 0.25s ease;
}

@keyframes fadeIn{
    from{
        opacity:0;
        transform:translateY(8px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

div[data-testid="stChatInput"]{
    position:fixed;
    bottom:20px;
    left:50%;
    transform:translateX(-50%);
    width:70%;
    z-index:1000;
}

div[data-testid="stChatInput"] > div{
    border-radius:25px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ------------------------
# MODEL
# ------------------------

if "model" not in st.session_state:
    st.session_state.model = ChatMistralAI(
        model="mistral-small-latest", temperature=0.7, max_tokens=500
    )

# ------------------------
# SESSION STATE
# ------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------------
# SIDEBAR
# ------------------------

with st.sidebar:
    st.title("🤖 Mistral AI")

    if st.button("➕ New Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### Model")
    st.info("mistral-small-latest")

    st.divider()

    st.metric("Messages", len(st.session_state.messages))

# ------------------------
# HEADER
# ------------------------

st.markdown(
    """
<div class="hero">
    <h1>✨ Mistral AI Assistant</h1>
    <p>Fast • Smart • Beautiful</p>
</div>
""",
    unsafe_allow_html=True,
)

# ------------------------
# EMPTY STATE
# ------------------------

if not st.session_state.messages:
    col1, col2 = st.columns(2)

    with col1:
        st.info("💻 Generate Code")

    with col2:
        st.info("📚 Explain Concepts")

    col3, col4 = st.columns(2)

    with col3:
        st.info("📝 Write Content")

    with col4:
        st.info("🚀 Build Projects")

# ------------------------
# CHAT HISTORY
# ------------------------

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ------------------------
# INPUT
# ------------------------

prompt = st.chat_input("Ask anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        placeholder = st.empty()

        response_text = ""

        try:
            for chunk in st.session_state.model.stream(prompt):
                if chunk.content:
                    response_text += chunk.content

                    placeholder.markdown(response_text + "▌")

            placeholder.markdown(response_text)

        except Exception as e:
            response_text = f"Error: {str(e)}"
            placeholder.error(response_text)

    st.session_state.messages.append({"role": "assistant", "content": response_text})

import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Personality Chatbot", page_icon="🤖", layout="wide")

# Title and description
st.title("🎭 Personality Chatbot")
st.markdown("Chat with an AI that matches your chosen personality!")

# Sidebar for personality selection
with st.sidebar:
    st.header("⚙️ Settings")

    personalities = {
        "😂 Funny": "You are a funny and witty AI assistant!",
        "😠 Angry": "You are an angry and aggressive AI assistant!",
        "🤨 Sarcastic": "You are a sarcastic and witty AI assistant!",
        "😢 Sad": "You are a sad and depressed AI assistant!",
        "❤️ Romantic": "You are a romantic and loving AI assistant!",
    }

    selected_personality = st.radio(
        "Choose AI Personality:",
        options=list(personalities.keys()),
        key="personality_selector",
    )

    st.markdown("---")

    if st.button("🔄 Clear Chat History", key="clear_button", use_container_width=True):
        st.session_state.messages = [
            SystemMessage(content=personalities[selected_personality])
        ]
        st.rerun()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=personalities[selected_personality])
    ]

if "selected_personality" not in st.session_state:
    st.session_state.selected_personality = selected_personality

# Update messages if personality changes
if st.session_state.selected_personality != selected_personality:
    st.session_state.selected_personality = selected_personality
    st.session_state.messages = [
        SystemMessage(content=personalities[selected_personality])
    ]

# Display current personality
st.info(f"**Current Personality:** {selected_personality}")

# Chat display area
st.markdown("### 💬 Conversation")
chat_container = st.container()

# Display chat history
with chat_container:
    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user", avatar="👤"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant", avatar="🤖"):
                st.markdown(message.content)

# Input area
st.markdown("---")

col1, col2 = st.columns([0.9, 0.1])

with col1:
    user_input = st.text_input(
        "Type your message:", placeholder="Say something...", key="user_input"
    )

with col2:
    send_button = st.button("Send", use_container_width=True, key="send_button")

# Handle user input
if send_button and user_input:
    # Add user message to history
    st.session_state.messages.append(HumanMessage(content=user_input))

    # Create model and get response
    with st.spinner("🤔 Thinking..."):
        try:
            model = ChatMistralAI(model="mistral-small-2603")
            response = model.invoke(st.session_state.messages)

            # Add AI message to history
            st.session_state.messages.append(AIMessage(content=response.content))

            # Clear input and rerun to display new messages
            st.rerun()
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.warning("Make sure your MISTRAL_API_KEY is set in your .env file")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "<small>Powered by Mistral AI | Built with Streamlit</small>"
    "</div>",
    unsafe_allow_html=True,
)

import streamlit as st

st.set_page_config(page_title="AI Smart Chat Companion", page_icon="🤖", layout="wide")

st.title("🤖 AI LLM-Powered Smart Chat Companion")
st.markdown("Developed by **Rabia Khan** | Python & AI Developer")
st.write("Type your prompt or question below to interact with the next-gen AI assistant.")

# Initialize chat history in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me anything about Python, AI, or coding..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate intelligent AI response (Simulated Generative AI Engine)
    with st.chat_message("assistant"):
        response = f"Hello Rabia! As an AI assistant, I processed your query: '{prompt}'. You have successfully implemented a Generative AI chat interface structure!"
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

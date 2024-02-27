import os
import streamlit as st
import google.generativeai as genai

# Initialize Gemini-Pro 
genai.configure(api_key=os.getenv("AIzaSyAUapxNs5faAro8S-GyhypH5p_m3rJZVp0"))
model = genai.GenerativeModel('gemini-pro')

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

# Display Form Title
st.title("Chat with AdvizerAI")

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return "role"

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown((message.parts[0].text).data)

if prompt := st.chat_input("What can I do for you?"):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)

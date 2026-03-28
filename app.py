import streamlit as st
import google.generativeai as genai
import time

# 1. SETUP: API Key yahan dhyan se paste karein
import streamlit as st
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

# 2. MODEL SELECTION: (Aapka working logic)
try:
    model = genai.GenerativeModel('gemini-2.5-flash')
except:
    model = genai.GenerativeModel('gemini-pro')

# 3. INTERFACE: Header, Title and LIGHT THEME
st.set_page_config(page_title="Google AI Chatbot", page_icon="⭐")

# Custom CSS for Professional Light Look
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    [data-testid="stSidebar"] { background-color: #1E3A8A; color: white; }
    .stChatInputContainer input { border: 1px solid #1E3A8A; }
    h1 { color: #1E3A8A; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# SIDEBAR: Aapka Personal Touch
with st.sidebar:
    st.title("⚙️ Control Panel")
    st.write("Developed by: **Hitesh**")
    st.write("Status: **System Active**")
    st.markdown("---")
    if st.button("🔄 Reset Chat"):
        st.session_state.messages = []
        st.rerun()

st.title(" 🌐 My personal Smart AI Assistant🚀🚀")
st.markdown("<p style='text-align: center; color: grey;'>Powered by Google Gemini AI</p>", unsafe_allow_html=True)
st.markdown("---")

# 4. MEMORY: Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. DISPLAY: Show history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. LOGIC: User input and AI response (With Typing Effect)
if prompt := st.chat_input("How can I help you today?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI response with Animation
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            full_response = response.text
            
            # Simple Typing Animation
            placeholder = st.empty()
            temp_text = ""
            for word in full_response.split():
                temp_text += word + " "
                time.sleep(0.05)
                placeholder.markdown(temp_text + "▌")
            
            placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Error: {e}")

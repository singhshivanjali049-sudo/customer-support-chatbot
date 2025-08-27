import streamlit as st
import openai
import pandas as pd
import csv
from datetime import datetime
import os
from typing import List, Dict

# Page configuration
st.set_page_config(
    page_title="Customer Support Chatbot",
    page_icon="🤖",
    layout="wide"
)

class ChatLogger:
    """Handles chat logging to CSV file"""
    
    def __init__(self, log_file: str = "chat_logs.csv"):
        self.log_file = log_file
        self._ensure_log_file_exists()
    
    def _ensure_log_file_exists(self):
        """Create log file with headers if it doesn't exist"""
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['timestamp', 'session_id', 'role', 'message'])
    
    def log_message(self, session_id: str, role: str, message: str):
        """Log a message to the CSV file"""
        timestamp = datetime.now().isoformat()
        with open(self.log_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, session_id, role, message])

class CustomerSupportChatbot:
    """Main chatbot class"""
    
    def __init__(self):
        self.logger = ChatLogger()
        self.system_prompt = """You are a helpful customer support assistant. 
        You should be polite, professional, and try to resolve customer issues effectively.
        If you cannot help with a specific issue, politely direct them to human support.
        Keep responses concise but helpful."""
    
    def get_response(self, messages: List[Dict], api_key: str) -> str:
        """Get response from OpenAI API"""
        try:
            openai.api_key = api_key
            
            # Add system message
            full_messages = [{"role": "system", "content": self.system_prompt}] + messages
            
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=full_messages,
                max_tokens=500,
                temperature=0.7
            )
            
            return response.choices[0].message.content.strip()
        
        except Exception as e:
            return f"Sorry, I'm having trouble connecting right now. Error: {str(e)}"

def main():
    st.title("🤖 Customer Support Chatbot")
    st.markdown("Welcome! I'm here to help you with your questions and concerns.")
    
    # Initialize chatbot
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = CustomerSupportChatbot()
    
    # Initialize session ID
    if 'session_id' not in st.session_state:
        st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Initialize chat history
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Key input
        api_key = st.text_input(
            "OpenAI API Key", 
            type="password",
            help="Enter your OpenAI API key to enable the chatbot"
        )
        
        st.markdown("---")
        
        # Chat statistics
        st.header("📊 Chat Stats")
        st.write(f"Session ID: `{st.session_state.session_id}`")
        st.write(f"Messages: {len(st.session_state.messages)}")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.session_state.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
            st.rerun()
        
        st.markdown("---")
        
        # Download chat logs
        if os.path.exists("chat_logs.csv"):
            with open("chat_logs.csv", "rb") as file:
                st.download_button(
                    label="📥 Download Chat Logs",
                    data=file,
                    file_name="chat_logs.csv",
                    mime="text/csv"
                )
    
    # Main chat interface
    chat_container = st.container()
    
    with chat_container:
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        if not api_key:
            st.error("Please enter your OpenAI API key in the sidebar to continue.")
            return
        
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Log user message
        st.session_state.chatbot.logger.log_message(
            st.session_state.session_id, 
            "user", 
            prompt
        )
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.chatbot.get_response(
                    st.session_state.messages, 
                    api_key
                )
            
            st.markdown(response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Log assistant message
        st.session_state.chatbot.logger.log_message(
            st.session_state.session_id, 
            "assistant", 
            response
        )
    
    # Footer
    st.markdown("---")
    st.markdown(
        "💡 **Tip:** This chatbot can help with general inquiries. "
        "For complex issues, please contact our human support team."
    )

if __name__ == "__main__":
    main()
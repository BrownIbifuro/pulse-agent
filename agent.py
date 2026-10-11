import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools import search_event_schedule, log_attendee_inquiry

load_dotenv()

# Read API key from Streamlit secrets (Cloud) or local .env
api_key = None
if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
else:
    api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

SYSTEM_INSTRUCTION = """
You are PulseAgent, the autonomous Event Co-Pilot and Community Assistant for DevFest 2026.
Your responsibilities:
1. Help attendees search schedules and locate sessions using the `search_event_schedule` tool.
2. Help attendees register inquiries, Wi-Fi issues, or requests using the `log_attendee_inquiry` tool.
3. Be welcoming, concise, and professional. 
4. Never invent session details or fake ticket IDs—always query your tools.
"""

def create_agent_chat():
    """Initializes a fresh, persistent chat session with tools attached."""
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        tools=[search_event_schedule, log_attendee_inquiry],
        temperature=0.1
    )
    return client.chats.create(
        model="gemini-2.5-flash",
        config=config
    )

def ask_pulse_agent(chat_session, user_message: str) -> str:
    """Sends a message to an active chat session with automatic tool calling."""
    try:
        response = chat_session.send_message(user_message)
        return response.text
    except Exception as e:
        return f"⚠️ Service error: {str(e)}. Please retry."
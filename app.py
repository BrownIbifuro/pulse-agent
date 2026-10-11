import streamlit as st
import json
import os
from agent import create_agent_chat, ask_pulse_agent

st.set_page_config(page_title="PulseAgent - DevFest 2026 Co-Pilot", page_icon="⚡", layout="wide")

# Organizer Sidebar
with st.sidebar:
    st.header("🛠️ Organizer Control Center")
    st.write("Live status of logged attendee inquiries.")
    
    if os.path.exists("tickets.json"):
        with open("tickets.json", "r") as f:
            tickets = json.load(f)
        st.metric(label="Active Tickets Logged", value=len(tickets))
        if tickets:
            st.download_button(
                label="📥 Export Tickets (JSON)",
                data=json.dumps(tickets, indent=2),
                file_name="devfest_tickets.json",
                mime="application/json"
            )
            with st.expander("View Recent Tickets"):
                st.json(tickets)
    else:
        st.info("No inquiries logged yet.")
        
    st.divider()
    if st.button("🔄 Reset Conversation"):
        st.session_state.messages = []
        st.session_state.agent_chat = create_agent_chat()
        st.rerun()

st.title("⚡ PulseAgent: DevFest 2026 Co-Pilot")
st.caption("Autonomous Agent powered by Gemini Function Calling")

# Initialize session state
if "agent_chat" not in st.session_state:
    st.session_state.agent_chat = create_agent_chat()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User prompt
if user_prompt := st.chat_input("Ask about sessions, report an issue, or log an inquiry..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("PulseAgent reasoning & executing tools..."):
            reply = ask_pulse_agent(st.session_state.agent_chat, user_prompt)
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
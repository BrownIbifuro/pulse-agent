import streamlit as st
import json
import os
from agent import run_pulse_agent

st.set_page_config(page_title="PulseAgent - DevFest 2026 Co-Pilot", page_icon="⚡", layout="wide")

# Sidebar for organizers
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
    st.caption("DevFest 2026 Speaker Breakout Demo | Built with Gemini SDK & Streamlit")

st.title("⚡ PulseAgent: DevFest 2026 Co-Pilot")
st.caption("Autonomous Agent powered by Gemini Function Calling")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "gemini_history" not in st.session_state:
    st.session_state.gemini_history = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_prompt := st.chat_input("Ask about sessions, report an issue, or log an inquiry..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("PulseAgent reasoning & executing tools..."):
            response_text, updated_history = run_pulse_agent(
                user_message=user_prompt,
                chat_history=st.session_state.gemini_history
            )
            st.markdown(response_text)

    st.session_state.messages.append({"role": "assistant", "content": response_text})
    st.session_state.gemini_history = updated_history
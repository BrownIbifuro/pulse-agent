"""
tools.py: Deterministic Action Tools for PulseAgent
"""
import json
import os
from datetime import datetime

TICKETS_FILE = "tickets.json"

SCHEDULE_DATABASE = [
    {"title": "Opening Keynote: The Agentic Era", "track": "General", "time": "09:00 AM", "room": "Main Hall"},
    {"title": "Building Autonomous Agents with Gemini", "track": "AI/ML", "time": "10:30 AM", "room": "Hall B"},
    {"title": "Deploying Scalable Services on Cloud Run", "track": "Cloud", "time": "11:30 AM", "room": "Room 2"},
    {"title": "Zero Trust Security for Web3 & APIs", "track": "Security", "time": "01:30 PM", "room": "Room 3"},
    {"title": "Hands-on Flutter: Cross-Platform UI", "track": "Mobile", "time": "02:30 PM", "room": "Hall B"},
]

def _read_tickets() -> list[dict]:
    if not os.path.exists(TICKETS_FILE):
        return []
    try:
        with open(TICKETS_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []

def _write_tickets(tickets: list[dict]):
    with open(TICKETS_FILE, "w") as f:
        json.dump(tickets, f, indent=2)

def search_event_schedule(query: str, track: str = "All") -> list[dict]:
    """Search the DevFest session schedule by keyword or track.

    Args:
        query: Keyword to search in session titles (e.g., 'Agent', 'Cloud', 'Flutter').
        track: Track filter: 'All', 'AI/ML', 'Cloud', 'Security', or 'Mobile'.
    """
    results = []
    for session in SCHEDULE_DATABASE:
        matches_query = query.lower() in session["title"].lower() or query == ""
        matches_track = (track == "All") or (track.lower() == session["track"].lower())
        if matches_query and matches_track:
            results.append(session)
    return results if results else [{"message": f"No sessions found matching '{query}' in track '{track}'."}]

def log_attendee_inquiry(attendee_email: str, issue_summary: str, category: str) -> str:
    """Logs an attendee inquiry, technical question, or venue issue to the ticketing system.

    Args:
        attendee_email: Contact email address of the attendee.
        issue_summary: Brief description of the question, request, or issue.
        category: Category: 'Registration', 'Wi-Fi/Venue', 'Session Inquiry', or 'Speaker Request'.
    """
    tickets = _read_tickets()
    ticket_id = f"TICK-{len(tickets) + 101}"
    record = {
        "ticket_id": ticket_id,
        "email": attendee_email,
        "issue": issue_summary,
        "category": category,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Logged"
    }
    tickets.append(record)
    _write_tickets(tickets)
    return f"Ticket logged successfully with ID {ticket_id}. Issue recorded: '{issue_summary}'."
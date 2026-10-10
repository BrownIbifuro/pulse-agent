\# ⚡ PulseAgent: Autonomous DevFest Co-Pilot



PulseAgent is an autonomous event co-pilot and community operations assistant built for \*\*DevFest 2026\*\*. Powered by Google's Gemini API and native Function Calling, PulseAgent transforms a reasoning model into an active participant capable of querying schedules, registering attendee issues, and maintaining event operations.



\---



\## 🎯 Key Features

\- \*\*Autonomous Tool Execution\*\*: Uses Gemini's Function Calling loop to dynamically execute deterministic Python tools without rigid prompt chains.

\- \*\*Session \& Track Discovery\*\*: Allows attendees to look up session times, speakers, and room locations filtered by track.

\- \*\*Ticketing \& Venue Operations\*\*: Logs attendee inquiries, lost item reports, or technical issues with real-time JSON-backed persistence.

\- \*\*Organizer Control Center\*\*: Dedicated dashboard for event organizers to monitor active attendee tickets and export incident records in real time.



\---



\## 🏗️ Technical Architecture



Attendee Prompt

↓

Gemini Reasoning Engine (System Instructions \& Function Declarations)

↓

Tool Calling Decision

├── search\_event\_schedule()  → Queries Local Event Schedule Database

└── log\_attendee\_inquiry()    → Persists Ticket \& Metadata to Disk

↓

Observation \& Synthesized Natural Response

↓

Streamlit Real-Time Interface



\---



\## 🛠️ Tech Stack

\- \*\*Model / SDK\*\*: Google GenAI SDK (`google-genai`), Gemini Flash

\- \*\*Frontend\*\*: Streamlit

\- \*\*Runtime\*\*: Python 3.10+

\- \*\*Persistence\*\*: File-backed structured JSON store



\---



\## 🚀 Getting Started



\### 1. Clone \& Set Up Virtual Environment



bash

git clone https://github.com/BrownIbifuro/pulse-agent.git

cd pulse-agent

python -m venv venv

source venv/bin/activate  # On Windows: venv\\Scripts\\activate



\### 2. Install Dependencies



bash

pip install -r requirements.txt



\### 3. Configure API Key

Create a `.env` file in the root directory:



env

GEMINI\_API\_KEY=your\_google\_ai\_studio\_api\_key\_here



\### 4. Run Locally



bash

streamlit run app.py



\---



\## 🎤 Proposed Breakout Session

This repository serves as the working demo and reference architecture for a 30-minute DevFest Breakout Session:  

\*\*"From Prompts to Actions: Building Autonomous Tool-Calling Agents with the Gemini SDK"\*\*


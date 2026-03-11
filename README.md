# FireReach – Autonomous Outreach Agent

FireReach is a lightweight Agentic AI system that automates outbound sales outreach. The system captures company signals, analyzes them using a Large Language Model (LLM), generates a personalized outreach email, and automatically sends it.

This prototype demonstrates how AI agents can combine company signals, reasoning, and automation to perform outreach tasks with minimal human intervention.

---

## Features

- Signal harvesting from company activity
- AI-generated account research
- Personalized outreach email generation
- Automated email delivery
- FastAPI backend with interactive API interface
- Live deployed prototype

---

## Agent Workflow

User Input → Signal Harvester → Research Analyst → Email Generator → Automated Sender

1. User provides:
   - ICP (Ideal Customer Profile)
   - Target company
   - Email address

2. The agent collects signals about the company.

3. The agent analyzes the signals using an LLM.

4. A personalized outreach email is generated.

5. The outreach email is automatically sent using an email API.

---

## Tools Implemented

### tool_signal_harvester

Captures company growth signals such as:

- funding rounds  
- hiring trends  
- company expansion  

---

### tool_research_analyst

Uses Groq LLM to analyze signals and generate an account brief explaining:

- company growth situation  
- cybersecurity risks  
- how cybersecurity training aligns with company needs  

---

### tool_outreach_automated_sender

Automatically sends the generated outreach email using the Resend email API.

Using an email API allows reliable email delivery in cloud environments where SMTP ports are restricted.

---

## Tech Stack

- Python  
- FastAPI  
- Groq API (LLM)  
- Resend Email API  
- Render (deployment)

---

## Running Locally

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn main:app --reload

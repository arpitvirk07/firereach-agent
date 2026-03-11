# FireReach – Autonomous Outreach Agent

FireReach is a lightweight Agentic AI system that automates outbound sales outreach. The system captures company signals, analyzes them using a Large Language Model (LLM), generates a personalized outreach email, and prepares it for automated delivery.

This prototype demonstrates how AI agents can combine live company signals, reasoning, and automation to perform sales outreach tasks efficiently.

---

## Features

- Signal harvesting from company activity
- AI-generated account research
- Personalized outreach email generation
- Autonomous outreach pipeline
- FastAPI backend with API testing interface
- Live deployed prototype

---

## Agent Workflow

User Input → Signal Harvester → Research Analyst → Email Generator → Email Sender

1. User provides:
   - ICP (Ideal Customer Profile)
   - Company name
   - Target email address

2. The agent collects signals about the company.

3. The agent analyzes the signals using an LLM.

4. A personalized outreach email is generated.

5. The outreach email is prepared for automated delivery.

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
- potential cybersecurity risks
- how cybersecurity training aligns with company needs

---

### tool_outreach_automated_sender

Generates and sends the outreach email using Gmail SMTP.

Note:  
Email sending works during local testing. In the deployed cloud prototype, SMTP is disabled due to cloud provider network restrictions. The generated email is returned in the API response instead.

---

## Tech Stack

- Python
- FastAPI
- Groq API (LLM)
- Gmail SMTP
- Render (deployment platform)






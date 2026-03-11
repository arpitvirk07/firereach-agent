# FireReach Agent Documentation

## Overview

FireReach is an autonomous outreach prototype designed to demonstrate how AI agents can automate outbound sales workflows. The system gathers company growth signals, analyzes them using an LLM, generates contextual account insights, and creates personalized outreach emails that can be automatically delivered.

The system follows an agent-based pipeline where multiple tools work together sequentially to complete an outreach task.

---

## Logic Flow

1. User provides:
   - ICP
   - Target company
   - Email address

2. The agent calls **tool_signal_harvester** to collect company growth signals.

3. The agent calls **tool_research_analyst** to analyze signals using an LLM and generate account insights.

4. The agent generates a personalized outreach email referencing the signals and research.

5. The agent calls **tool_outreach_automated_sender** to send the email automatically.

---

## Tool Schemas

### tool_signal_harvester(company)

Purpose:

Collects relevant company growth signals.

Example signals:

- funding announcements
- hiring activity
- team expansion

Output:

A list of signals describing company activity.

---

### tool_research_analyst(icp, company, signals)

Purpose:

Uses a Groq LLM to analyze company signals and generate an account brief.

Inputs:

- ICP
- company name
- signals from the signal harvester

Output:

Account insight explaining:

- company growth
- cybersecurity needs
- how cybersecurity training helps the company

---

### tool_outreach_automated_sender(email, message)

Purpose:

Automatically sends the generated outreach email.

Implementation:

The system uses the Resend email API to deliver emails. Email APIs are preferred in cloud environments because many cloud platforms restrict SMTP ports.

Inputs:

- recipient email
- generated outreach message

Output:

Email delivery confirmation.

---

## System Prompt

The agent acts as a GTM outreach assistant that:

- captures relevant company signals
- analyzes company growth context
- identifies cybersecurity training opportunities
- generates contextual outreach messages
- automates outreach delivery

---


## Architecture Summary

Agent Pipeline

User Input  
↓  
Signal Harvester  
↓  
Research Analyst  
↓  
Email Generator  
↓  
Automated Email Sender

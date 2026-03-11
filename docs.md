# FireReach Agent Documentation

## Overview

FireReach is an autonomous outreach prototype that demonstrates how AI agents can automate outbound sales workflows. The system gathers company growth signals, analyzes them using a Large Language Model (LLM), generates contextual account insights, and creates personalized outreach emails.

The goal of the system is to demonstrate an **agentic workflow where multiple tools cooperate sequentially** to complete a task.

---

## Logic Flow

1. The user provides:
   - ICP (Ideal Customer Profile)
   - Target company
   - Email address

2. The agent calls **tool_signal_harvester** to collect company growth signals.

3. The agent calls **tool_research_analyst** to analyze the signals using an LLM and generate an account brief.

4. The system generates a personalized outreach email referencing the collected signals and insights.

5. The agent calls **tool_outreach_automated_sender** to automatically send the generated outreach email.

Note:  
In the deployed prototype, SMTP email sending is disabled due to cloud provider network restrictions. The generated outreach email is returned in the API response instead.

---

## Tool Schemas

### tool_signal_harvester(company)

Purpose:

Collects relevant company growth signals.

Example signals include:

- funding announcements
- hiring trends
- product expansion

Output:

A list of signals describing company activity.

---

### tool_research_analyst(icp, company, signals)

Purpose:

Uses a Groq LLM to analyze company signals and generate an account brief.

Inputs:

- ICP
- company name
- signals captured by the signal harvester

Output:

A research summary describing:

- company growth context
- cybersecurity risks
- alignment with cybersecurity training solutions

---

### tool_outreach_automated_sender(email, message)

Purpose:

Sends the generated outreach email using Gmail SMTP.

Inputs:

- recipient email
- generated outreach message

Output:

Email sent confirmation.

Note:

Email sending works in the local environment. In the deployed prototype, SMTP functionality is disabled due to cloud infrastructure restrictions.

---

## System Prompt

The agent behaves as a GTM outreach assistant that:

- captures relevant company signals
- analyzes company context
- identifies potential cybersecurity needs
- generates contextual outreach emails

The system ensures that the outreach message references real signals gathered by the signal harvester.


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
Automated Outreach

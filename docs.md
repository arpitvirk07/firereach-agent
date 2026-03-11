# FireReach Autonomous Outreach Agent

## Logic Flow

1. User provides ICP and target company
2. Agent calls tool_signal_harvester to collect company signals
3. Agent calls tool_research_analyst to generate account insights
4. Agent generates a personalized outreach email
5. Agent calls tool_outreach_automated_sender to send the email automatically

## Tool Schemas

### tool_signal_harvester(company)
Returns company growth signals such as funding, hiring, and expansion.

### tool_research_analyst(icp, company, signals)
Uses an LLM to analyze signals and generate an account brief.

### tool_outreach_automated_sender(email, message)
Automatically sends the generated outreach email using Gmail SMTP.

## System Prompt

The agent acts as a GTM outreach assistant that:
- captures company signals
- analyzes them
- creates contextual outreach
- sends the email automatically
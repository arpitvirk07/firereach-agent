from tools import tool_signal_harvester
from tools import tool_research_analyst
from tools import tool_outreach_automated_sender


def run_agent(icp, company, email):

    # Step 1 – Get signals
    signals = tool_signal_harvester(company)

    # Step 2 – Research
    research = tool_research_analyst(icp, company, signals)

    # Step 3 – Create email
    email_text = f"""
Hi,

I noticed that {company} is expanding and hiring new engineers.

Signals:
{signals}

{research}

Our cybersecurity training helps growing startups secure their teams.

Best,
FireReach AI
"""

    # Step 4 – Send email
    tool_outreach_automated_sender(email, email_text)

    return {
        "signals": signals,
        "research": research,
        "email": email_text,
        "status": "Email sent"
    }
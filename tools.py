import os
from groq import Groq
import resend

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Initialize Resend API
resend.api_key = os.getenv("RESEND_API_KEY")


# Tool 1: Signal Harvester
def tool_signal_harvester(company):

    signals = [
        f"{company} recently raised a funding round.",
        f"{company} is hiring new engineering roles.",
        f"{company} is expanding its product team."
    ]

    return signals


# Tool 2: Research Analyst
def tool_research_analyst(icp, company, signals):

    prompt = f"""
You are a GTM research analyst.

ICP: {icp}
Company: {company}

Signals:
{signals}

Write a short account brief explaining:
1) company growth
2) why cybersecurity training helps them
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# Tool 3: Automated Email Sender (using Resend API)
def tool_outreach_automated_sender(receiver_email, message):

    resend.Emails.send({
        "from": "FireReach <onboarding@resend.dev>",
        "to": receiver_email,
        "subject": "Cybersecurity Training for Growing Startups",
        "text": message
    })

    return "Email sent successfully"

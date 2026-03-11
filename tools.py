# tools.py

from groq import Groq

# initialize groq client
client = Groq(api_key="<REDACTED>")


# -------------------------------
# TOOL 1 : Signal Harvester
# -------------------------------
def tool_signal_harvester(company):

    # Simulated signals (prototype)
    signals = [
        f"{company} recently raised a funding round.",
        f"{company} is hiring new engineering roles.",
        f"{company} is expanding its product team."
    ]

    return signals


# -------------------------------
# TOOL 2 : Research Analyst
# -------------------------------
def tool_research_analyst(icp, company, signals):

    prompt = f"""
You are a GTM research analyst.

ICP: {icp}
Company: {company}

Signals:
{signals}

Write a 2 paragraph account brief explaining:
1) what the company is doing
2) how cybersecurity training could help them.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    research = response.choices[0].message.content

    return research
import smtplib
from email.mime.text import MIMEText


def tool_outreach_automated_sender(receiver_email, message):

    sender_email ="arpitvirk07@gmail.com"
    password = "<REDACTED>"

    msg = MIMEText(message)
    msg["Subject"] = "Cybersecurity Training for Growing Startups"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender_email, password)
    server.send_message(msg)

    server.quit()

    return "Email sent successfully"
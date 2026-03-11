import os
from groq import Groq
import smtplib
from email.mime.text import MIMEText

# Initialize Groq client using environment variable
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# TOOL 1: Signal Harvester
def tool_signal_harvester(company):

    signals = [
        f"{company} recently raised a funding round.",
        f"{company} is hiring new engineering roles.",
        f"{company} is expanding its product team."
    ]

    return signals


# TOOL 2: Research Analyst
def tool_research_analyst(icp, company, signals):

    prompt = f"""
You are a GTM research analyst.

ICP: {icp}
Company: {company}

Signals:
{signals}

Write a short account brief explaining:
1. company growth
2. why cybersecurity training helps them
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# TOOL 3: Automated Email Sender
def tool_outreach_automated_sender(receiver_email, message):

    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

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

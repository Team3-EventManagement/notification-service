import smtplib
from email.mime.text import MIMEText
from app.config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

def send_email(to_email, subject, message):

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = to_email

    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()

    server.login(EMAIL_USER, EMAIL_PASSWORD)

    server.sendmail(
        EMAIL_USER,
        to_email,
        msg.as_string()
    )

    server.quit()
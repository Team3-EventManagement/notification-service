import smtplib
from email.mime.text import MIMEText
from app.config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

def send_email(to_email, subject, message):

    print("Sending email to:", to_email)

    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = to_email

    try:

        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()

        print("Logging into SMTP...")

        server.login(EMAIL_USER, EMAIL_PASSWORD)

        server.sendmail(EMAIL_USER, to_email, msg.as_string())

        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print("Email sending failed:", e)

from app.services.email_service import send_email

def process_notification(event):

    event_type = event["type"]

    if event_type == "user.registered":

        subject = "Welcome"
        message = "Your registration was successful"

        send_email(event["email"], subject, message)

    elif event_type == "event.registration.success":

        subject = "Event Registration"
        message = f"You registered for {event['eventName']}"

        send_email(event["email"], subject, message)

    elif event_type == "payment.success":

        subject = "Payment Successful"
        message = f"Payment successful for {event['eventName']}"

        send_email(event["email"], subject, message)
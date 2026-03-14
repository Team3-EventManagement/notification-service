import pika
import json
from app.config import RABBITMQ_HOST
from app.services.notification_service import process_notification

def callback(ch, method, properties, body):

    event = json.loads(body)

    print("Received event:", event)

    process_notification(event)

def start_consumer():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(RABBITMQ_HOST)
    )

    channel = connection.channel()

    channel.queue_declare(queue="notification_queue")

    channel.basic_consume(
        queue="notification_queue",
        on_message_callback=callback,
        auto_ack=True
    )

    print("Waiting for messages...")

    channel.start_consuming()
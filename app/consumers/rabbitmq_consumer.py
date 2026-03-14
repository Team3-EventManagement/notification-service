import pika
import json
import time
from app.config import RABBITMQ_HOST
from app.services.notification_service import process_notification


def callback(ch, method, properties, body):

    event = json.loads(body)
    print("Received event:", event)

    process_notification(event)


def start_consumer():

    while True:
        try:
            print("Connecting to RabbitMQ...")

            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host=RABBITMQ_HOST)
            )

            print("Connected to RabbitMQ")
            break

        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ not ready, retrying in 5 seconds...")
            time.sleep(5)

    channel = connection.channel()

    channel.queue_declare(queue="notification_queue")

    channel.basic_consume(
        queue="notification_queue",
        on_message_callback=callback,
        auto_ack=True
    )

    print("Waiting for messages...")

    channel.start_consuming()
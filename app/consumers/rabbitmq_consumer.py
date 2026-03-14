import pika
import json
from app.services.notification_service import process_notification

def callback(ch, method, properties, body):

    event = json.loads(body)

    print("================================")
    print("Event received:", event)
    print("================================")

    process_notification(event)

def start_consumer():

    print("Connecting to RabbitMQ...")

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbitmq")
    )

    channel = connection.channel()

    channel.queue_declare(queue="notification_queue", durable=True)

    print("Waiting for messages...")

    channel.basic_consume(
        queue="notification_queue",
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()

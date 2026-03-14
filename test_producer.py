import pika
import json

connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

channel = connection.channel()

channel.queue_declare(queue="notification_queue")

event = {
    "type": "event.registration.success",
    "email": "test@email.com",
    "eventName": "AI Hackathon"
}

channel.basic_publish(
    exchange="",
    routing_key="notification_queue",
    body=json.dumps(event)
)

print("Event sent to RabbitMQ")

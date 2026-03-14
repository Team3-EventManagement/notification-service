from fastapi import FastAPI
import threading

from app.api.notification_api import router
from app.consumers.rabbitmq_consumer import start_consumer

app = FastAPI()

app.include_router(router)

def start_rabbit():

    start_consumer()

thread = threading.Thread(target=start_rabbit)
thread.start()
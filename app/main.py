from fastapi import FastAPI
import threading
from app.consumers.rabbitmq_consumer import start_consumer

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "running"}

def run_consumer():
    print("Starting RabbitMQ consumer...")
    try:
        start_consumer()
    except Exception as e:
        print("Consumer crashed:", e)

@app.on_event("startup")
def startup_event():
    thread = threading.Thread(target=run_consumer)
    thread.daemon = True
    thread.start()

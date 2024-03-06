from kafka import KafkaProducer

class KafkaLogger:
    def __init__(self, bootstrap_servers, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: str(v).encode('utf-8')
        )
        self.topic = topic

    def log_message(self, message):
        self.producer.send(self.topic, value=message)
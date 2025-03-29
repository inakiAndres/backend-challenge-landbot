import uuid
from ..value_objects.topic import Topic

class Notification:
    def __init__(self, topic: str, description: str):
        self.topic = Topic(topic)
        self.description = description
        self.id = self.generate_id()

    def generate_id(self):
        return str(uuid.uuid4())

    def __str__(self):
        return f"Notification(ID: {self.id}, Topic: {self.topic}, Description: {self.description})"

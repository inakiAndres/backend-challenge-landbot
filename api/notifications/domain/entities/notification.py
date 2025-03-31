import uuid
from api.notifications.domain.value_objects.topic import Topic

class Notification:
    def __init__(self, topic: str, description: str):
        self.topic = str(Topic(topic))
        self.description = description
        self.request_id = self.generate_id()

    def generate_id(self):
        return str(uuid.uuid4())

    def __str__(self):
        return f"Notification(Request_Id: {self.request_id}, Topic: {self.topic}, Description: {self.description})"

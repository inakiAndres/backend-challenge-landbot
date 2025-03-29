from ..domain.entities.notification import Notification

class SendNotificationUseCase:
    def execute(self, topic: str, description: str):
        notification = Notification(topic, description)

        return notification.id

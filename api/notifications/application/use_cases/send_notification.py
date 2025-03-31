from api.notifications.domain.entities.notification import Notification
from api.notifications.domain.services.notification_selector import NotificationSelector
from api.notifications.infrastructure.tasks import process_notification

class SendNotificationUseCase:
    def execute(self, topic: str, description: str):
        notification_entity = Notification(topic, description)

        notification_type = NotificationSelector.get_notification_channel(notification_entity.topic)

        process_notification(notification_entity.request_id, notification_entity.topic, notification_entity.description, notification_type, schedule=0)
        return {"message": "Notification queued", "request_id": notification_entity.request_id, "notification_type": notification_type}

from background_task import background
from api.notifications.infrastructure.repositories.email_repository import EmailNotificationRepository
from api.notifications.infrastructure.repositories.slack_repository import SlackNotificationRepository
import logging

logger = logging.getLogger(__name__)

@background(schedule=0)
def process_notification(request_id, topic, description, notification_type, retry_count=0):
    """Executes the notification request based on the application decision."""

    try:
        if notification_type == "slack":
            SlackNotificationRepository.send_slack_message(request_id, topic, description)
        elif notification_type == "email":
            EmailNotificationRepository.send_email(request_id, topic, description)

        logger.info(f"Notification sent successfully via {notification_type}: {topic}")

    except Exception as e:
        logger.error(f"Failed to send {notification_type} notification: {e}")

        if retry_count < 3:  
            # Retry in 1 min with max 3 retries
            process_notification(request_id, topic, description, notification_type, retry_count=retry_count+1, schedule=60) 

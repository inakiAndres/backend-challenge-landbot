from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class EmailNotificationRepository:
    @staticmethod
    def send_email(request_id, topic, description):

        try:
            subject = f"[{request_id}] New Notification: {topic}"
            message = f"Description: {description}"
            recipient_list = settings.RECIPIENT_EMAILS

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                recipient_list
                )
            logger.info(f"Email sent successfully for topic: {topic}")

        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            raise e

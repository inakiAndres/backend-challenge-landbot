import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class SlackNotificationRepository:
    SLACK_WEBHOOK_URL = settings.SLACK_WEBHOOK_URL

    @staticmethod
    def send_slack_message(request_id, topic, description):

        payload = {
            "channel": "support",
            "text": f"*Request_Id: [{request_id}], Topic: {topic}*\nIssue description: {description}"
            }

        try:
            response = requests.post(SlackNotificationRepository.SLACK_WEBHOOK_URL, json=payload)
            response.raise_for_status()
            logger.info(f"Slack notification sent for topic: {request_id, topic}")

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send Slack notification: {request_id, e}")
            raise e

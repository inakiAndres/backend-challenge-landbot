from django.test import TestCase
from unittest.mock import patch
from api.notifications.infrastructure.tasks import process_notification
from background_task.models import Task
from background_task.tasks import tasks

class ProcessNotificationTaskTest(TestCase):
    """Tests for the process_notification background task."""

    @patch("api.notifications.infrastructure.repositories.slack_repository.SlackNotificationRepository.send_slack_message")
    def test_process_notification_slack(self, mock_slack):
        """Test that Slack notification is sent successfully."""
        mock_slack.return_value = None

        process_notification.now(1, "sales", "Hey! I need help with a sales issue", "slack")

        mock_slack.assert_called_once_with(1, "sales", "Hey! I need help with a sales issue")

    @patch("api.notifications.infrastructure.repositories.email_repository.EmailNotificationRepository.send_email")
    def test_process_notification_email(self, mock_email):
        """Test that Email notification is sent successfully."""
        mock_email.return_value = None

        process_notification.now(2, "Pricing", "Hey! I need help with a pricing issue", "email")

        mock_email.assert_called_once_with(2, "Pricing", "Hey! I need help with a pricing issue")

    @patch("api.notifications.infrastructure.repositories.slack_repository.SlackNotificationRepository.send_slack_message", side_effect=Exception("Slack error"))
    @patch("api.notifications.infrastructure.tasks.process_notification") # Declared to don't 
    def test_process_notification_slack_retries(self, mock_task, mock_slack):
        """Test that Slack notification retries on failure."""
        process_notification.now(3, "Sales", "Hey! I need help with a sales issue", "slack")

        mock_task.assert_called_once_with(3, "Sales", "Hey! I need help with a sales issue", "slack", retry_count=1, schedule=60)

    @patch("api.notifications.infrastructure.repositories.email_repository.EmailNotificationRepository.send_email", side_effect=Exception("Email error"))
    @patch("api.notifications.infrastructure.tasks.process_notification")
    def test_process_notification_email_retries(self, mock_task, mock_email):
        """Test that Email notification retries on failure."""
        process_notification.now(4, "Pricing", "Hey! I need help with a pricing issue", "email")

        mock_task.assert_called_once_with(4, "Pricing", "Hey! I need help with a pricing issue", "email", retry_count=1, schedule=60)

    def test_task_is_scheduled(self):
        """Ensure background task is scheduled properly."""
        process_notification(5, "Pricing", "Hey! I need help with a pricing issue", "email")

        self.assertEqual(Task.objects.count(), 1)

        tasks.run_next_task()

        self.assertEqual(Task.objects.count(), 0)

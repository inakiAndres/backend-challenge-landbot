from rest_framework.test import APITestCase
from rest_framework import status

class TestAPIEndpoints(APITestCase):

    def test_send_notification_success(self):
        """Test sending a valid topic and description"""
        payload = {
            "topic": "Sales",
            "description": "Hi, I need help with a sales problem"
        }

        response = self.client.post('/api/notifications', data=payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertIn("message", response.data)
        self.assertIn("request_id", response.data)

    def test_send_notification_missing_params(self):
        """Test sending a request with missing parameters"""
        payload = {}

        response = self.client.post('/api/notifications', data=payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("error", response.data)

    def test_send_notification_invalid_topic(self):
        """Test sending a request with an invalid topic format"""
        payload = {
            "topic": "Technical",
            "description": "Hi, I need help with a technical issue"
        }

        response = self.client.post('/api/notifications', data=payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertIn("error", response.data)

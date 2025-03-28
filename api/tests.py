from rest_framework.test import APITestCase
from rest_framework import status

class TestAPIEndpoints(APITestCase):
    
    def test_get_data(self):
        # Make a GET request to the /api/data/ endpoint
        response = self.client.get('/api/data/')
        
        # Check if the response status is HTTP 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the response contains the expected JSON data
        self.assertEqual(response.data, {"message": "Hello from Django API!"})

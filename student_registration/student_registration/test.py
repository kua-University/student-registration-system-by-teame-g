from django.test import TestCase, Client
from django.urls import reverse

class EmailValidationTests(TestCase):
    def setUp(self):
        # Initialize the test client
        self.client = Client()
        self.url = reverse('student_registration')  # Replace with your actual view's name

    def test_valid_email(self):
        """
        Test registration with a valid email address.
        """
        response = self.client.post(self.url, {
            'name': 'Test User',
            'email': 'valid@example.com',
            'stripeToken': 'test_token'
        })

        # Assert that the registration was successful
        self.assertEqual(response.status_code, 200)
        self.assertIn('Registration successful!', response.json().get('message', ''))

    def test_invalid_email(self):
        """
        Test registration with an invalid email address.
        """
        response = self.client.post(self.url, {
            'name': 'Test User',
            'email': 'invalid-email',
            'stripeToken': 'test_token'
        })

        # Assert that the registration fails with an error
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid email address', response.json().get('error', ''))

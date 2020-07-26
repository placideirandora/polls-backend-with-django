from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient

from .views.poll.views import (PollViewSet)

# Create your tests here.


class TestPollEndpoint(APITestCase):
    """
    Ensure we can setup everything required in advance
    to running the test cases
    """

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = PollViewSet.as_view({'get': 'list'})
        self.uri = '/api/v1/polls/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        """
        Ensure we can setup a user to be used in the api calls.
        """

        User = get_user_model()

        return User.objects.create_user(
            username='test',
            email='testuser@test.com',
            password='test'
        )

    def test_list_with_factory(self):
        """
        Ensure we can list poll objects with factory.
        """

        request = self.factory.get(self.uri,
                                   HTTP_AUTHORIZATION='Token {}'
                                   .format(self.token.key))
        request.user = self.user
        response = self.view(request)

        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_list_with_api_client(self):
        """
        Ensure we can list poll objects with api client.
        """

        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)

        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_create(self):
        """
        Ensure we can create a new poll object.
        """

        self.client.login(username='test', password='test')
        data = {
            'question': 'What is best car in the world?',
            'created_by': 1
        }
        response = self.client.post(self.uri, data, format='json')

        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

# Create your views here.


class Index(APIView):
    permission_classes = ()

    def get(self, request):
        urls = [{'User Registration [POST]': 'api/v1/auth/register/'},
                {'User Login [POST]': 'api/v1/auth/login/'},
                {'Polls [CRUD]', 'api/v1/polls'},
                {'Create and List Polls\' Choices [POST, GET]':
                 'api/v1/polls/<int: pk > /choices/'},
                {'Vote Polls\' Choice':
                 'api/v1/polls/<int:poll_pk>/choices/<int:choice_pk>/vote/'}]
        return Response({'message': 'Welcome to the Polls REST API',
                         'Endpoints': urls}, status=HTTP_200_OK)

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED)

from ...serializers import UserSerializer

# Create your views here.


class UserSignUp(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class UserSignIn(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if username is None or password is None:
            return Response({'error': 'Username or Password is required'},
                            status=HTTP_400_BAD_REQUEST)
        elif user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_401_UNAUTHORIZED)

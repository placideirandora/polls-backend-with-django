from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED)

from ...models import Profile
from ...serializers import (UserSerializer, ProfileSerializer)

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


class UserProfile(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'username'

    def update(self, request, *args, **kwargs):
        profile = Profile.objects.get(username=kwargs['username'])

        if not request.user == profile.user:
            raise PermissionDenied('You cannot update this Profile.'
                                   'You don\'t own it.')

        return super().update(request, *args, **kwargs)

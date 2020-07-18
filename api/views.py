from django.contrib.auth import authenticate
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED)

from .models import (Poll, Choice)
from .serializers import (UserSerializer, PollSerializer,
                          ChoiceSerializer, VoteSerializer)

# Create your views here.


class Index(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the Polls REST API'})


class UserCreation(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
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


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])

        return queryset


class VoteCreation(APIView):
    serializer_class = VoteSerializer

    def post(self, request, poll_pk, choice_pk):
        voted_by = request.data.get('voted_by')
        data = {'choice': choice_pk, 'poll': poll_pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

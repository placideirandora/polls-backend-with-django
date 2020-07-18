from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .models import (Poll)
from .serializers import (PollSerializer)

# Create your views here.


class Index(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the Polls REST API'})


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

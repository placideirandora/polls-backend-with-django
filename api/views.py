from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.status import (HTTP_201_CREATED, HTTP_400_BAD_REQUEST)

from .models import (Poll, Choice)
from .serializers import (PollSerializer, ChoiceSerializer, VoteSerializer)

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


class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer

    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])

        return queryset


class CreateVote(generics.CreateAPIView):
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

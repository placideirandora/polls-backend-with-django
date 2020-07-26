from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_400_BAD_REQUEST)

from ...serializers import VoteSerializer

# Create your views here.


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

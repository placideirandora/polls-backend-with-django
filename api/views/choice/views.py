from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter, OrderingFilter

from ...models import (Poll, Choice)
from ...serializers import ChoiceSerializer

# Create your views here.


class ChoiceList(generics.ListCreateAPIView):
    serializer_class = ChoiceSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['choice_text']

    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id=self.kwargs['pk'])

        return queryset

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs["pk"])

        if not request.user == poll.created_by:
            raise PermissionDenied(
                'You cannot create Choice for this Poll. You don\'t own it.')

        return super().post(request, *args, **kwargs)

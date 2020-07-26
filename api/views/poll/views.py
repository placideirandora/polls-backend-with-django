from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from ...models import Poll
from ...serializers import PollSerializer

# Create your views here.


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

    def destroy(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk=self.kwargs['pk'])

        if not request.user == poll.created_by:
            raise PermissionDenied(
                'You cannot delete this Poll. You don\'t own it.')

        return super().destroy(request, *args, **kwargs)

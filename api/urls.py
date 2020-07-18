from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (Index, PollViewSet, ChoiceList, CreateVote)

# Create your urls here.


router = DefaultRouter()

router.register('api/v1/polls', PollViewSet)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/v1/polls/<int:pk>/choices/',
         ChoiceList.as_view(), name='choice_list'),
    path('api/v1/polls/<int:poll_pk>/choices/<int:choice_pk>/vote/',
         CreateVote.as_view(), name="create_vote"),
]


urlpatterns += router.urls

from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (Index, UserCreation, PollViewSet, ChoiceList, VoteCreation)

# Create your urls here.


router = DefaultRouter()

router.register('api/v1/polls', PollViewSet)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/v1/auth/register/', UserCreation.as_view(),
         name='user_creation'),
    path('api/v1/polls/<int:pk>/choices/',
         ChoiceList.as_view(), name='choice_list'),
    path('api/v1/polls/<int:poll_pk>/choices/<int:choice_pk>/vote/',
         VoteCreation.as_view(), name="create_vote"),
]


urlpatterns += router.urls

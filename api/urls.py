from django.urls import path

from .views import (Index, PollList, PollDetail, ChoiceList, CreateVote)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/v1/polls/', PollList.as_view(), name='polls_list'),
    path('api/v1/polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
    path('api/v1/polls/<int:pk>/choices/',
         ChoiceList.as_view(), name='choice_list'),
    path('api/v1/polls/<int:poll_pk>/choices/<int:choice_pk>/vote/',
         CreateVote.as_view(), name="create_vote"),
]

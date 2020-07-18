from django.urls import path

from .views import (Index, PollList, PollDetail)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/v1/polls/', PollList.as_view(), name="polls_list"),
    path('api/v1/polls/<int:pk>/', PollDetail.as_view(), name="polls_detail")
]

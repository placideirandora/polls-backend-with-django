from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.index import Index
from .views.user.views import (UserSignUp, UserSignIn)
from .views.poll.views import PollViewSet
from .views.choice.views import ChoiceList
from .views.vote.views import VoteCreation

# Create your urls here.


router = DefaultRouter()

router.register('api/v1/polls', PollViewSet)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/v1/auth/signup/', UserSignUp.as_view(),
         name='user_creation'),
    path('api/v1/auth/signin/', UserSignIn.as_view(),
         name='login_view'),
    path('api/v1/polls/<int:pk>/choices/',
         ChoiceList.as_view(), name='choice_list'),
    path('api/v1/polls/<int:poll_pk>/choices/<int:choice_pk>/vote/',
         VoteCreation.as_view(), name="create_vote"),
]

urlpatterns += router.urls

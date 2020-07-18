from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/polls/', views.polls_list, name="polls_list"),
    path('api/v1/polls/<int:pk>/', views.polls_detail, name="polls_detail")
]

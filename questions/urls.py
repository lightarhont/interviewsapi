from django.urls import path
from .views import (InterviewsView,
                    InterviewView,
                    UserView)

urlpatterns = [
    path('interviews/', InterviewsView.as_view()),
    path('interview/<int:pk>', InterviewView.as_view()),
    path('userview/<int:pk>', UserView.as_view()),
]
from django.urls import path
from .views import TaskView, TaskViewDetail
from apps.user.views import UserView


urlpatterns = [
    path('task/', TaskView.as_view()),
    path('task/<int:fk>', TaskViewDetail.as_view()),
    path('user/', UserView.as_view()),
]

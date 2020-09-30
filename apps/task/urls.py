from django.urls import path
from .views import TaskList, TaskDetail, TaskDetailByManage, TaskDetailByStatus, TaskCountByManage

urlpatterns = [
    path('task/', TaskList.as_view()),
    path('task/<int:pk>/', TaskDetail.as_view()),
    path('task/manager/<int:fk_user>/', TaskDetailByManage.as_view()),
    path('task/manager/count_task/<int:fk>/', TaskCountByManage.as_view()),
    path('task/status/<int:task_status>/', TaskDetailByStatus.as_view()),
]

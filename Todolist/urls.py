from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailUpdateDeleteAPIView
urlpatterns = [
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetailUpdateDeleteAPIView.as_view(), name='task-detail-update-delete'),
]
from django.urls import path
from . import views
from .views import (
    UserRegistrationView,
    CommentListView,
    CommentCreateView,
    CommentDeleteView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),

    path('tasks/', views.TaskListView.as_view(), name='task-list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    path('tasks/<int:task_id>/comments/', CommentListView.as_view(), name='task-comment-list'),
    path('tasks/<int:task_id>/comments/create/', CommentCreateView.as_view(), name='task-comment-create'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]

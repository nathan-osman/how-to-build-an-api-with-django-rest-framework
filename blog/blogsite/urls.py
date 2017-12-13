from django.urls import path

from . import views

urlpatterns = [
    path('api/posts/', views.ListPostsView.as_view()),
    path('api/posts/<int:id>/comments/', views.ListCommentsView.as_view()),
    path('api/comments/new/', views.CreateCommentView.as_view()),
]

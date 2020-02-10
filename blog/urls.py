from django.urls import path, include
from blog.views import (
    PostListView,
    PostCreatUpdateDeleteRetrive,
    PostCreateView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='list'),
    path('posts/create/', PostCreateView.as_view(), name='create'),
    path('posts/<int:pk>/', PostCreatUpdateDeleteRetrive.as_view(), name='crud')
]

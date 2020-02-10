from django.urls import path
from blog.views import PostList, DetailView

urlpatterns = [
    path('list/', PostList.as_view(), name='list'),
    path('list/<int:pk>/', DetailView.as_view(), name='detail'),
]

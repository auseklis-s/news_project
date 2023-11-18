from django.urls import path
from .views import CustomUserCreateView, NewsListCreateView, NewsDetailView

urlpatterns = [
    path('api/register/', CustomUserCreateView.as_view(), name='user_create'),
    path('api/news/', NewsListCreateView.as_view(), name='news_list_create'),
    path('api/news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
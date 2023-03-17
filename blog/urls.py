from django.urls import path
from .views import Posts

app_name = 'blog'
urlpatterns = [
    path('posts/',Posts,name = 'posts')
]
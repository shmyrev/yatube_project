from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='home'),
    path('group/', views.group_posts, name='posts_list'),
]
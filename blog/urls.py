from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts', views.posts, name='posts'),
    path('create_posts', views.create_posts, name='create_posts'),
    path('edit_post/<int:item_id>/', views.edit_post, name='edit_post'),
]
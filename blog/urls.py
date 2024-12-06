from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts', views.posts, name='posts'),
    path('create_posts', views.create_posts, name='create_posts'),
    path('edit_post/<int:item_id>/', views.edit_post, name='edit_post'),
    path('show_detpost/<int:item_id>/', views.show_det_post, name='show_detpost'),
    path('show_detauthor/<int:item_id>/', views.show_det_author, name='show_detauthor'),
    path('create_author', views.create_author, name='create_author')

]
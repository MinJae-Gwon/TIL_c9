from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:post_id>/comment/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/update/', views.update, name='update'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('', views.index, name='list'),
    path('create/', views.create, name = 'create'),
    path('new/', views.new, name='new'),
    path('throw/',views.throw, name='throw'),
    path('catch/',views.catch, name='catch'),
   
]
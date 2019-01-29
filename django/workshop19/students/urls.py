
from django.urls import path
from . import views
urlpatterns = [
    path('<int:student_id>/update/', views.update),
    path('<int:student_id>/edit/', views.edit),
    path('<int:student_id>/delete/', views.delete ),
    path('<int:student_id>', views.detail),
    path('', views.index),
    path('new/', views.new),
    path('create/', views.create),
]

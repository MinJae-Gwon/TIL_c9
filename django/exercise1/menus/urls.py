from django.contrib import admin
from . import views

urlpatterns = [
    path('/pick/', views.pick),
    path('/picked/', views.picked)
]
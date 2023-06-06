"""Defines routes for quad_eq_solver."""

from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.result)
]
from django.urls import path

from . import views

urlpatterns = [
    path('restapi/', views.api_home, name="api-home")  # http://localhost:8000/api
]
from django.urls import path
from layouts import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
]

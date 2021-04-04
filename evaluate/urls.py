from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from evaluate import views as evaluate_views

urlpatterns = [
    path('', evaluate_views.createTest, name='createTest'),
    path('testSummary/<int:pk>', evaluate_views.testSummary, name='testSummary'),
]
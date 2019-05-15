from django.contrib import admin
from django.urls import path
from qa.views import test

urlpatterns = [
    path('admin/', views.test, name='admin'),
    path('login/', views.test, name='login'),
    path('signup/', views.test, name='signup'),
    path('question/<int:id>/', views.test, name='question'),
    path('ask/', views.test, name='ask'),
    path('popular/', views.test, name='popular'),
    path('new/', views.test, name='new'),
]
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', include('qa.urls')),
    path('login/', include('qa.urls')),
    path('signup/', include('qa.urls')),
    path('question/', include('qa.urls')),
    path('ask/', include('qa.urls')),
    path('popular/', include('qa.urls')),
    path('new/', include('qa.urls')),
]
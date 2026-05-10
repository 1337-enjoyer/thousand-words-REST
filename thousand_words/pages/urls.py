from django.urls import path

from .views import PageAPIView

app_name = 'pages'

urlpatterns = [
    path('api/', PageAPIView.as_view(), name='api'),
]
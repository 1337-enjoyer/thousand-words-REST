from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

v1_router = DefaultRouter()
v1_router.register('words', views.WordViewSet, basename='word')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]

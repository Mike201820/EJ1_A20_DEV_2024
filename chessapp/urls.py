from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChessProblemViewSet

router = DefaultRouter()
router.register(r'chessproblems', ChessProblemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

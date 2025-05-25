from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HistoriesModelViewSet

router = DefaultRouter()
router.register(prefix='', basename='histories', viewset=HistoriesModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

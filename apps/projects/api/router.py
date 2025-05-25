from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.projects.api.views import ProjectsModelViewSet


router = DefaultRouter()

router.register(prefix='', basename='projects', viewset=ProjectsModelViewSet)


urlpatterns = [
]

urlpatterns += router.urls
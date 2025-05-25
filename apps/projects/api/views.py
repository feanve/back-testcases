from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from apps.projects.api.serializers import ProjectsSerializer

# Create your views here.

class ProjectsModelViewSet(ModelViewSet):
    serializer_class = ProjectsSerializer
    queryset = serializer_class.Meta.model.objects.all()
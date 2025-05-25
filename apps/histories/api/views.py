from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from apps.histories.models import Histories
from .serializers import HistoriesSerializer

# Create your views here.

class HistoriesModelViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = HistoriesSerializer
    queryset = Histories.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        project_id = self.request.query_params.get('project', None)
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset

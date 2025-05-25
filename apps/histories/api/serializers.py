from rest_framework import serializers
from apps.histories.models import Histories
from apps.projects.api.serializers import ProjectsSerializer

class HistoriesSerializer(serializers.ModelSerializer):
    project_detail = ProjectsSerializer(source='project', read_only=True)

    class Meta:
        model = Histories
        fields = ('id', 'project', 'project_detail', 'name', 'description', 
                 'priority', 'criteria', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

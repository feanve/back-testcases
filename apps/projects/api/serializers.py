from apps.projects.models import Projects
from rest_framework.serializers import ModelSerializer

class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'  
from apps.cases.models import Cases
from rest_framework.serializers import ModelSerializer
from apps.histories.api.serializers import HistoriesSerializer


class CasesSerializer(ModelSerializer):
    history_detail = HistoriesSerializer(source='id_us', read_only=True)

    class Meta:
        model = Cases
        fields = ('id', 'id_us', 'history_detail', 'description', 'priority', 
                 'preconditions', 'input_data', 'steps', 'expected_result', 
                 'actual_result', 'test_status', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
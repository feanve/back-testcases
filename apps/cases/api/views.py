from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.cases.api.serializers import CasesSerializer
from apps.cases.models import Cases

class CasesModelViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = CasesSerializer
    queryset = serializer_class.Meta.model.objects.all()

class GetCasesByUS(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, id_us):

        try:
            cases = Cases.objects.get(id_us=id_us)
        except Cases.DoesNotExist:
            return Response({'error': 'No cases available'}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = CasesSerializer(cases)

        return Response(serializer.data, status=status.HTTP_200_OK)
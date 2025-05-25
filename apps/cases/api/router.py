from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.cases.api.views import CasesModelViewSet, GetCasesByUS


router = DefaultRouter()

router.register(prefix='', basename='cases', viewset=CasesModelViewSet)


urlpatterns = [
    path('us/<int:id_us>/', GetCasesByUS.as_view(), name='get_by_us'),
]

urlpatterns += router.urls
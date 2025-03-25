from django.urls import path,include
from rest_framework import routers, viewsets
from .serializers import CompanySerializer
from .models import CompanyDataSet

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyDataSet.objects.all()
    serializer_class = CompanySerializer

router = routers.DefaultRouter()
router.register(r'company', CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

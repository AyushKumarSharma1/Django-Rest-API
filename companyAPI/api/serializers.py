from rest_framework import serializers
from .models import CompanyDataSet

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyDataSet
        fields = "__all__"
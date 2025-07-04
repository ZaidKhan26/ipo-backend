from rest_framework import serializers
from .models import Company, IPO, Document

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class IPOSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(read_only=True)
    # documents = DocumentSerializer(many=True, read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    class Meta:
        model = IPO
        fields = '__all__'

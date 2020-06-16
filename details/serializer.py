from .models import ApiView
from rest_framework import serializers


class ApiViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiView
        fields = '__all__'
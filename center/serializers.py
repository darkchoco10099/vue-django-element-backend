from .models import DemoApi, ProjectApi, HealthyApi
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectApi
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = DemoApi
        fields = "__all__"


class HealthySerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthyApi
        fields = "__all__"

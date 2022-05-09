from django.shortcuts import render
from .models import DemoApi, ProjectApi, HealthyApi
from rest_framework import viewsets
from .serializers import ProjectSerializer, TestSerializer, HealthySerializer


class TestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = DemoApi.objects.all()
    serializer_class = TestSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """
    queryset = ProjectApi.objects.all()
    serializer_class = ProjectSerializer


class HealthyViewSet(viewsets.ModelViewSet):
    queryset = HealthyApi.objects.all()
    serializer_class = HealthySerializer

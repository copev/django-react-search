from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import OrganizationSerializer, ProfileSerializer
from .models import Organization, Profile
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Organization, Profile
from .serializers import *



class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()


class OrgListDetailFilter(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name', '^county']

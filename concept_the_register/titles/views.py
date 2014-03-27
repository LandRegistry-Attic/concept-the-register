from django.shortcuts import render
from concept_the_register import Titles
from rest_framework import viewsets
from Titles.serializers import TitlesSerializer

# Create your views here.

class TitlesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Titles to be viewed or edited.
    """
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer

from django.shortcuts import render
from concept_the_register.titles.models import Title
from rest_framework import viewsets
from concept_the_register.titles.serializers import TitleSerializer

# Create your views here.

class TitlesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Titles to be viewed or edited.
    """
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

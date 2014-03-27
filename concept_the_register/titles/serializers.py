from concept_the_register.titles.models import Title
from rest_framework import serializers


class TitleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Title
        field = ('owner')

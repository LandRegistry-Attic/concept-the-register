from concept_the_register import Titles
from rest_framework import serializers


class TitlesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Titles
        fields = ('owner')

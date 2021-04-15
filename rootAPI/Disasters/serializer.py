from rest_framework import serializers

from .models import Disasters

class DisasterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disasters
        fields = ('pk', 'country', 'disaster_type', 'people_died', 'year', 'latitude', 'longitude')

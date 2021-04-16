from .models import Disasters
from .serializer import DisasterSerializer
from rest_framework import generics


class DisastersList(generics.ListCreateAPIView):
    serializer_class = DisasterSerializer

    def get_queryset(self):
        return Disasters.objects.all()


class Country(generics.ListAPIView):
    serializer_class = DisasterSerializer

    def get_queryset(self):
        country = self.kwargs['country']
        return Disasters.objects.filter(country=country).all()


class Disaster_Type(generics.ListAPIView):
    serializer_class = DisasterSerializer

    def get_queryset(self):
        disaster_type = self.kwargs['disaster_type']
        return Disasters.objects.filter(disaster_type=disaster_type).all()

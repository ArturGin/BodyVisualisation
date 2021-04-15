from django.shortcuts import render
from .models import Disasters
from .serializer import DisasterSerializer
from rest_framework import generics
from rest_framework import viewsets
import sys



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

# class DisastersList(viewsets.ModelViewSet):
#     serializer_class = DisasterSerializer
#     queryset = Disasters.objects.all()

# So we orgize by Year and Country
# shoudl we re-orginize the DB or is there a way
# through URL to pass a query for a certain country 

# How can we make a system in which you can get anything?
# like you enter: how many people died in Italy in 1928?

# The stupid ways is to: create a separate Class for each use-case
# but i think there has to be a better way
# Messaged Slack people maybe should throw it in some other chats

# For now the plan is next: Country and Year
from django.urls import path, re_path
from .views import DisastersList, Disaster_Type, Country


urlpatterns = [
    re_path('^country/(?P<country>.+)/$', Country.as_view(), name='detail'),
    re_path('^disaster/(?P<disaster_type>.+)/$', Disaster_Type.as_view(),
            name='detail'),
    path('list/', DisastersList.as_view(), name='list')
]

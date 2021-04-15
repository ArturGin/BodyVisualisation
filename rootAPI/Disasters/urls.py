from .models import Disasters
from django.urls import path, re_path
from .views import DisastersList, Disaster_Type, Country
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('detail/', viewset=DisastersDetail)
# # router.register(r'list/', DisastersList.as_view)


# urlpatterns = router.urls

urlpatterns = [
    re_path('^country/(?P<country>.+)/$', Country.as_view(), name='detail'),
    re_path('^disaster/(?P<disaster_type>.+)/$', Disaster_Type.as_view(), name='detail'),
    # path('detail/<country>/', DisastersDetail.as_view(), name='detail'),
    path('list/', DisastersList.as_view(), name='list')
]
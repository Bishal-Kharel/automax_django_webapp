import django_filters

from .models import Listing

class ListingFilter(django_filters.FilterSet):
    class Meta:
        model = Listing
        fields = {'model': ['icontains'], 'brand':['exact'], 'color' : ['exact'],  'mileage' : ['lt'] }

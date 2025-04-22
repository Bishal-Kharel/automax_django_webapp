from django import forms

from .models import Listing
from .widgets import CustomListingImageFieldWidget

class ListingForm(forms.ModelForm):
    image = forms.ImageField(widget=CustomListingImageFieldWidget, required=True)
    class Meta:
        model = Listing
        fields= ['brand', 'model', 'vin', 'mileage', 'description','engine', 'transmission', 'image' ]
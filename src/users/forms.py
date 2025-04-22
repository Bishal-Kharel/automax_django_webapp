from django import forms
from django.contrib.auth.models import User
from .models import Location, Profile
from .widgets import CustomPictureImageField

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget= CustomPictureImageField)
    bio = forms.TextInput()
    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')

class LocationForm(forms.ModelForm):

    address_1 = forms.CharField(required=True)
                                

    class Meta:
        model = Location
        fields = ['address_1', 'address_2', 'city', 'District', 'Zip_Code']
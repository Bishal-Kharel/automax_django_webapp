
from django.contrib import admin
from.models import Location, Profile

class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)

class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)

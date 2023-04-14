from django.db import models

# Create your models here.
from geopy.geocoders import Nominatim
import ssl

try:
    _create_unverifed_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverifed_https_context

class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.CharField(max_length=500)
    pincode = models.CharField(max_length=10)
    lat = models.CharField(max_length=20, null=True, blank=True)
    lon = models.CharField(max_length=20, null=True, blank=True)
    #print(certifi.where())

    def save(self, *args, **kwargs):
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(int(self.pincode))
        self.lat = location.latitude
        self.lon = location.longitude
        super(Shop, self).save(*args,**kwargs)

    def __str__(self) -> str:
        return self.name
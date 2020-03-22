from django.db import models
from django.contrib.gis.db import models

# Database table model

class Attraction(models.Model):
    Gid = models.IntegerField(default=10)
    Name = models.CharField(max_length=100)
    Address = models.TextField()
    Opening_hours = models.TextField(blank=True, null=True)
    Website = models.URLField(blank=True, null=True)
    Tickets = models.TextField(blank=True, null=True)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
      
    # GeoDjango-specific: a geometry field (PointField)
    Geometry = models.PointField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.Name

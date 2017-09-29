from django.db import models


class Event(models.Model):
    """
        event model class
    """    

    name = models.CharField(max_length=255, unique=True)
    lat = models.CharField(max_length=255)
    lon = models.CharField(max_length=255)


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


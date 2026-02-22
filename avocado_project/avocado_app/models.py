from django.db import models

class Avocado(models.Model):
    firmness = models.FloatField()
    hue = models.IntegerField()
    saturation = models.IntegerField()
    brightness = models.IntegerField()
    sound_db = models.IntegerField()
    weight_g = models.IntegerField()
    size_cm3 = models.IntegerField()
    color_category = models.CharField(max_length=32)

from rest_framework import serializers

class AvocadoSerializers(serializers.Serializer):
    firmness = serializers.FloatField()
    hue = serializers.IntegerField()
    saturation = serializers.IntegerField()
    brightness = serializers.IntegerField()
    sound_db = serializers.IntegerField()
    weight_g = serializers.IntegerField()
    size_cm3 = serializers.IntegerField()
    color_category = serializers.CharField(max_length=32)

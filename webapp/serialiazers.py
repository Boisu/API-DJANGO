from dataclasses import fields
from rest_framework import serializers
# from rest_framework import word
from . models import word
# from webapp import word

class wordSerializer(serializers.ModelSerializer):
    class Meta:
        model = word
        # fields=('text')
        fields = '__all__'
from rest_framework import serializers
from .models import *

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = '__all__'

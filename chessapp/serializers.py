from rest_framework import serializers
from .models import ChessProblem
import json

class ChessProblemSerializer(serializers.ModelSerializer):
    obstacles = serializers.JSONField()

    class Meta:
        model = ChessProblem
        fields = '__all__'

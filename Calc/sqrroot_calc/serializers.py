from rest_framework import serializers

from .models import SquareRoots


class SquareRootsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SquareRoots
        fields = '__all__'

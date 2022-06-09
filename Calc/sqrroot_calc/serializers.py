from rest_framework import serializers

from .models import Number#, Result


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'
        optional_fields = ['root1', 'root2']


# class ResultSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Result
#         fields = '__all__'
from rest_framework import serializers
import cmath

from sqrroot_calc.models import Number


class NumberSerializer(serializers.ModelSerializer):
    root1 = serializers.SerializerMethodField()
    root2 = serializers.SerializerMethodField()
    class Meta:
        model = Number
        fields = '__all__'


    def get_root1(self, instance):
        a = instance.a
        b = instance.b
        c = instance.c
        discrement = (b**2) - (4 * a*c)
        root1 = (-b-cmath.sqrt(discrement))/(2 * a)
        return root1


    def get_root2(self, instance):
        a = instance.a
        b = instance.b
        c = instance.c
        discrement = (b**2) - (4 * a*c)
        root2 = (-b + cmath.sqrt(discrement))/(2 * a)
        return root2

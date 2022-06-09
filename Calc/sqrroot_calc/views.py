from rest_framework import viewsets

from .models import Number#, Result
from .serializers import NumberSerializer#, ResultSerializer


class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer


# class ResultViewSet(viewsets.ModelViewSet):
#     queryset = Result.objects.all()
#     serializer_class = ResultSerializer
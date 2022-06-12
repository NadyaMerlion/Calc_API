from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import Number
from .serializers import NumberSerializer
import sqrroot_calculator



class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()


    @staticmethod
    def post(request, *args, **kwargs):
        """
        Calculate square roots
        """

        a, b, c = float(request.data.get('a')), float(request.data.get('b')), float(request.data.get('c'))

        root1, root2 = sqrroot_calculator.calculate(a, b, c)

        data = {
            'a': a,
            'b': b,
            'c': c,
            'root1': root1,
            'root2': root2
        }

        serializer = NumberSerializer(data=data)

        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

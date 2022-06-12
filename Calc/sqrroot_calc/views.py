from rest_framework import viewsets 
from rest_framework.response import Response
from rest_framework import status

from .models import SquareRoots
from .serializers import SquareRootsSerializer
from .calculator import calculate



class SquareRootsViewSet(viewsets.ModelViewSet):
    queryset = SquareRoots.objects.all()
    serializer_class = SquareRootsSerializer

    def create(request, *args, **kwargs):
        """
        Calculate square roots
        """

        a, b, c = float(request.data.get('a')), float(request.data.get('b')), float(request.data.get('c'))

        root1, root2 = calculate(a, b, c)

        data = {
            'a': a,
            'b': b,
            'c': c,
            'root1': root1,
            'root2': root2
        }

        serializer = SquareRootsSerializer(data=data)

        if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

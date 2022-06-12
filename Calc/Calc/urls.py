from django.urls import path

from sqrroot_calc.views import SquareRootsApiView


urlpatterns = [
    path('number/', SquareRootsApiView.as_view()),
]

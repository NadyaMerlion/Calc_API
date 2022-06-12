# from django.urls import path

# from sqrroot_calc.views import NumberAPIView

# urlpatterns = [
#     path('number/', NumberAPIView.as_view()),
# ]

from rest_framework.routers import DefaultRouter

from django.urls import include, path

from sqrroot_calc.views import SquareRootsViewSet

router = DefaultRouter()
router.register('number', SquareRootsViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 
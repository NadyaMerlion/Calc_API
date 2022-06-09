from django.urls import include, path

from rest_framework.routers import DefaultRouter

from sqrroot_calc.views import NumberViewSet


router = DefaultRouter()
router.register('number', NumberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]

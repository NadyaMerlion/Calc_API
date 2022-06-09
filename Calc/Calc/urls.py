from django.urls import include, path

from rest_framework.routers import DefaultRouter

from sqrroot_calc.views import NumberViewSet#, ResultViewSet


router = DefaultRouter()
router.register('number', NumberViewSet)
#router.register('result', ResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('/result/', include(router.urls)),
    ]

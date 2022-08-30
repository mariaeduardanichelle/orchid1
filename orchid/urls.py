from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import OrigenViewSet, ClasseViewSet, PersonagenViewSet

router = DefaultRouter()
router.register(r'origem', OrigenViewSet)
router.register(r'classe', ClasseViewSet)
router.register(r'personagem', PersonagenViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register(r'motherboards', views.MotherboardViewSet, basename='motherboards')
router.register(r'cpus', views.CPUViewSet, basename='cpus')
router.register(r'rams', views.RAMViewSet, basename='rams')
router.register(r'gpus', views.GPUViewSet, basename='gpus')
router.register(r'cases', views.CaseViewSet, basename='cases')
router.register(r'internal-drives', views.InternalDrivesViewSet, basename='internal-drives')
router.register(r'power-supplies', views.PowerSupplyViewSet, basename='power-supplies')
router.register(r'laptops', views.LaptopViewSet, basename='laptops')
router.register(r'mobiles', views.MobileViewSet, basename='mobiles')

urlpatterns = router.urls + [
    path('attributes/', views.get_all_attributes, name='attributes')
]
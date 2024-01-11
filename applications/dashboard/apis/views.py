from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .permissions import IsAdmin
from .. import models
from . import serializers

class BaseViewSet(ModelViewSet):
    permission_classes = [IsAdmin]
    filter_backends = [SearchFilter]
    search_fields = ['name']
class MotherboardViewSet(BaseViewSet):
    queryset = models.Motherboard.get_active_objects()
    serializer_class = serializers.MotherboardSerializer

class CPUViewSet(BaseViewSet):
    queryset = models.CPU.get_active_objects()
    serializer_class = serializers.CPUSerializer

class RAMViewSet(BaseViewSet):
    queryset = models.RAM.get_active_objects()
    serializer_class = serializers.RAMSerializer

class GPUViewSet(BaseViewSet):
    queryset = models.GPU.get_active_objects()
    serializer_class = serializers.GPUSerializer

class CaseViewSet(BaseViewSet):
    queryset = models.Case.get_active_objects()
    serializer_class = serializers.CaseSerializer

class InternalDrivesViewSet(BaseViewSet):
    queryset = models.InternalDrive.get_active_objects()
    serializer_class = serializers.InternalDriveSerializer

class PowerSupplyViewSet(BaseViewSet):
    queryset = models.PowerSupply.get_active_objects()
    serializer_class = serializers.PowerSupplySerializer

class LaptopViewSet(BaseViewSet):
    queryset = models.Laptop.get_active_objects()
    serializer_class = serializers.LaptopSerializer

class MobileViewSet(BaseViewSet):
    queryset = models.Mobile.get_active_objects()
    serializer_class = serializers.MobileSerializer
from rest_framework import generics
from .models import Apartment, Object
from .serializers import ApartmentSerializer, ObjectSerializer
from ..managers.permissions import ManagerPermissions


class ApartmentListCreateView(generics.ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [ManagerPermissions]


class ApartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer
    permission_classes = [ManagerPermissions]


class ObjectListCreateView(generics.ListCreateAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [ManagerPermissions]


class ObjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [ManagerPermissions]

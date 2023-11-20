from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny

from .models import Manager
from .serializers import ManagerSerializer, ManagerCreateSerializer, ManagerUpdateSerializer
from .permissions import ManagerPermissions


class ManagerCreateView(generics.CreateAPIView):
    serializer_class = ManagerCreateSerializer
    permission_classes = [IsAdminUser]


class ManagerListView(generics.ListAPIView):
    queryset = Manager.objects.all().order_by('-created_at')
    serializer_class = ManagerSerializer
    permission_classes = [AllowAny]


class ManagerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerUpdateSerializer
    permission_classes = [ManagerPermissions]
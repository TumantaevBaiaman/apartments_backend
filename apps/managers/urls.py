from django.urls import path
from apps.managers.views import ManagerCreateView, ManagerDetailView, ManagerListView

urlpatterns = [
    path('create/', ManagerCreateView.as_view(), name='manager-update'),
    path('list/', ManagerListView.as_view(), name='manager-list'),
    path('<int:pk>/', ManagerDetailView.as_view(), name='manager-detail'),
]
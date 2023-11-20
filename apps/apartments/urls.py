from django.urls import path
from .views import ApartmentListCreateView, ApartmentDetailView, ObjectListCreateView, ObjectDetailView

urlpatterns = [
    path('apartments/', ApartmentListCreateView.as_view(), name='apartment-list-create'),
    path('apartments/<int:pk>/', ApartmentDetailView.as_view(), name='apartment-detail'),
    path('objects/', ObjectListCreateView.as_view(), name='object-list-create'),
    path('objects/<int:pk>/', ObjectDetailView.as_view(), name='object-detail'),
]
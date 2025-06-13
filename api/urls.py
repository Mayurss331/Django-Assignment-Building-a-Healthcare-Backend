# urls.py
from django.urls import path
from .views import (
    RegisterView, LoginView,
    PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, MappingByPatientView, MappingDeleteView
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    # Authentication
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),

    # Patient Management
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    # Doctor Management
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Mappings
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:patient_id>/', MappingByPatientView.as_view(), name='mapping-by-patient'),
    path('mappings/<int:pk>/delete/', MappingDeleteView.as_view(), name='mapping-delete'),

    # To Refresh the access token when expired
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 

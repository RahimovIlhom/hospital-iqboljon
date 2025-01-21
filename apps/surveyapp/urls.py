from django.urls import path
from .views import PatientDataCreateView

urlpatterns = [
    path('create/', PatientDataCreateView.as_view(), name='patient-create'),
]
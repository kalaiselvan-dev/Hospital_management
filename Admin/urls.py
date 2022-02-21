from django.urls import path
from .import views

urlpatterns = [
    path('doctor/', views.doctor_list.as_view(), name='doctor-list'),
    path('patient/', views.patient_list.as_view(), name='patient-list'),
    path('doctor/<int:pk>/', views.doctor_details.as_view(), name='doctor-details'),
    path('patient/<int:pk>/', views.patient_details.as_view(),
         name='patient-details'),

]

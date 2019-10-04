"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reserve import doctorView, patientView, appointmentView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/', doctorView.DoctorListView.as_view(), name='doctor'),
    path('doctor/<int:pk>', doctorView.DoctorDetailView.as_view(), name='doctorInfo'),
    path('patient/', patientView.PatientListView.as_view(), name='patient'),
    path('patient/<int:pk>', patientView.PatientDetailView.as_view(), name='patientInfo'),
    path('appointment/', appointmentView.AppointmentListView.as_view(), name='appointment'),
    path('appointment/<int:pk>', appointmentView.AppointmentDetailView.as_view(), name='appointmentInfo')
]


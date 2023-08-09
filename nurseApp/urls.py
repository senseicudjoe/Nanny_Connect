from django.urls import path
from . import views

urlpatterns = [
    path("nurse_settings",views.nurse_settings,name="nurse_settings"),
    path("manage_jobs",views.manage_jobs,name="manage_jobs"),
    path('updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

]
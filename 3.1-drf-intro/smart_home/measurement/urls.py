from django.urls import path
from measurement.views import Sensors_View, Measurements_View, One_sensor_View


urlpatterns = [
    path('sensors/', Sensors_View.as_view(), name='sensors'),
    path('measurements/', Measurements_View.as_view(), name='measurements'),
    path('sensors/<int:pk>/', One_sensor_View.as_view(), name='sensor'),
]

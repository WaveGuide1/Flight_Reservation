"""
URL configuration for flightReservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from flight_app import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('passenger', views.PassengerViewSet)
router.register('flight', views.FlightViewSet)
router.register('reservation', views.ReservationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/flight_reservation/', include(router.urls)),
    path('api/flight_reservation/find_flight/', views.find_flight),
    path('api/flight_reservation/save_reservation/', views.save_reservation),
    path('api/token', obtain_auth_token)
]

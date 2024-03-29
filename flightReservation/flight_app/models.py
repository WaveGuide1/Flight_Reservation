from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.


class Passenger(models.Model):
    """Passenger database model"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Flight(models.Model):
    """ Flight database model"""
    operating_airline = models.CharField(max_length=225)
    flight_number = models.CharField(max_length=225)
    arrival_country = models.CharField(max_length=225)
    departure_country = models.CharField(max_length=225)
    operation_date = models.DateField()
    time_departure = models.TimeField()

    def __str__(self):
        return self.operating_airline + ' Flight ' + self.flight_number


class Reservation(models.Model):
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)

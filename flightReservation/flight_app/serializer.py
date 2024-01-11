from .models import Flight, Passenger, Reservation
from rest_framework import serializers
import re


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate(self, data):
        if re.match("^[0-9]*$", data['flight_number']) is None:
            raise serializers.ValidationError("Flight number must be a digit")
        return data['flight_number']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

from rest_framework.decorators import api_view

from .models import Flight, Passenger, Reservation
from .serializer import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters


# Create your views here.
@api_view(['POST'])
def save_reservation(request):
    flight = Flight.objects.get(id=request.data['id'])

    passenger = Passenger()
    passenger.first_name = request.data['first_name']
    passenger.last_name = request.data['last_name']
    passenger.email = request.data['email']
    passenger.mobile_number = request.data['mobile_number']

    passenger.save()

    reservation = Reservation()
    reservation.passenger = passenger
    reservation.flight = flight

    reservation.save()

    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def find_flight(request):
    flight = Flight.objects.filter(departure_country=request.data['departure_country'],
                                   arrival_country=request.data['arrival_country'],
                                   operation_date=request.data['operation_date'], )
    serializer = FlightSerializer(flight, many=True)
    return Response(serializer.data)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departure_country', 'arrival_country', 'operation_date']
    permission_classes = [IsAuthenticated]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

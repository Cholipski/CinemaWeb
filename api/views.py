from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer
from .models import Movie, Actors, Director, Seats
from .serializers import MovieSerializer, ActorsSerializer, DirectorSerializer, SeatsSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ActorsViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class SeatsViewSet(viewsets.ModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = SeatsSerializer
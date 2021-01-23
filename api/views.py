from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Movie, Director, Category, Reservation, Seans
from .serializers import UserSerializer, MovieSerializer, DirectorSerializer, CategorySerializer, \
    ReservationSerializer, SeansSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import permissions
from django.contrib.auth.models import User


# Movie ====================================================================================
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name= 'movie-list'
    search_field = ['title']
    ordering_field = ['title', 'runningTime']

class MovieDeatil(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name= 'movie-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Category ====================================================================================

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name= 'category-list'
    search_field = ['name']
    ordering_field = ['name']

class CategoryDeatil(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name= 'category-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Director ====================================================================================

class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    name= 'director-list'
    search_field = ['last_name']
    ordering_field = ['last_name']

class DirectorDeatil(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    name= 'director-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



# User ====================================================================================

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    ordering_fields = ['idUsera', 'Email']
    name = 'user-list'
    search_fields = ['email']
    permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [permissions.IsAuthenticated]

# Reservation ====================================================================================

class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    ordering_fields = ['date', 'time']
    name = 'reservation-list'
    search_fields = ['date']



class ReservationDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-detail'


# Seans ====================================================================================

class SeansList(generics.ListCreateAPIView):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer
    ordering_fields = ['date', 'time']
    name = 'seans-list'
    search_fields = ['date']



class SeansDetail(generics.RetrieveDestroyAPIView):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer
    name = 'seans-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'Users': reverse(UserList.name, request=request),
                         'Movie': reverse(MovieList.name, request=request),
                         'Category': reverse(CategoryList.name, request=request),
                         'Director': reverse(DirectorList.name, request=request),
                         'Reservation': reverse(ReservationList.name, request=request),
                         'Seans': reverse(SeansList.name, request=request)

})
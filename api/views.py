from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .models import Movie, Director, Category, Reservation, Seans, Reviews
from .serializers import UserSerializer, MovieSerializer, DirectorSerializer, CategorySerializer, \
    ReservationSerializer, SeansSerializer, ReviewsSerializer
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from rest_framework import filters
from rest_framework import permissions
from django.contrib.auth.models import User
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication


# Movie ====================================================================================
class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name = 'movie-list'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title',]
    ordering_fields = ['title', 'running_time','release_date']
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class MovieDeatil(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    name= 'movie-detail'
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


# Category ====================================================================================

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name',]
    ordering_fields = ['name',]
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

class CategoryDeatil(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name= 'category-detail'
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


# Director ====================================================================================

class DirectorList(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    name= 'director-list'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['last_name', ]
    ordering_fields = ['last_name', 'birthday', 'stars']
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

class DirectorDeatil(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    name= 'director-detail'
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)



# User ====================================================================================

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['email','first_name','last_name',]
    ordering_fields = ['id', 'Email' ]

class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

# Reservation ====================================================================================
class ReservationFilter(FilterSet):
    Start_date = DateTimeFilter(field_name='date', lookup_expr='gte')
    to_date = DateTimeFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Reservation
        fields = ['Start_date', 'to_date']

class ReservationList(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_class = ReservationFilter
    ordering_fields = ['date',]
    name = 'reservation-list'
    search_fields = ['date',]
    permission_classes = [DjangoModelPermissions]
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class ReservationDetail(generics.RetrieveDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    name = 'reservation-detail'
    permission_classes = [DjangoModelPermissions]


# Seans ====================================================================================

class SeansFilter(FilterSet):
    Start_date = DateTimeFilter(field_name='date', lookup_expr='gte')
    to_date = DateTimeFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Seans
        fields = ['Start_date', 'to_date']

class SeansList(generics.ListCreateAPIView):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer
    filter_class = SeansFilter
    ordering_fields = ['date', 'time']
    name = 'seans-list'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['date',]
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)



class SeansDetail(generics.RetrieveDestroyAPIView):
    queryset = Seans.objects.all()
    serializer_class = SeansSerializer
    name = 'seans-detail'
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


# Reviews ====================================================================================

class ReviewsList(generics.ListCreateAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    ordering_fields = ['date', 'stars']
    name = 'reviews-list'
    search_fields = ('date',)
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewsDetail(generics.RetrieveDestroyAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    name = 'reviews-detail'
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'Users': reverse(UserList.name, request=request),
                         'Movie': reverse(MovieList.name, request=request),
                         'Category': reverse(CategoryList.name, request=request),
                         'Director': reverse(DirectorList.name, request=request),
                         'Reservation': reverse(ReservationList.name, request=request),
                         'Seans': reverse(SeansList.name, request=request),
                         'Reviews': reverse(ReviewsList.name, request=request)

                         })
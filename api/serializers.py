from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Director, Category, Reservation, Client, Seans


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['url','name']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.SlugRelatedField(queryset=Director.objects.all(), slug_field='last_name')
    class Meta:
        model = Movie
        fields = ['url', 'title', 'description', 'runningTime','category','director']

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['url', 'first_name','last_name', 'birthday']

class SeansSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='last_name')
    class Meta:
        model = Seans
        fields = ['url', 'date', 'time','client']

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='last_name')
    seans = serializers.SlugRelatedField(queryset=Seans.objects.all(), slug_field='date')
    class Meta:
        model = Reservation
        fields = ['url','ticket','client', 'seans']
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Movie, Actors, Director, Seats


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email']


class ActorsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actors
        fields = ['url', 'firstName', 'lastName', 'age']

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['url', 'name', 'gender', 'dateOfBirth']

class SeatsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seats
        fields = ['url', 'row', 'number',]

class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = ['url', 'title', 'description', 'runningTime','actors']

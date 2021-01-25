from django.contrib.auth.models import User
from rest_framework import serializers
from datetime import date
from .models import Movie, Director, Category, Reservation, Seans, Reviews
from django.contrib.auth.models import Group



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email','first_name','last_name','password']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        group = Group.objects.get(name='client')
        group.user_set.add(user)
        return user

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['pk','url','name']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    director = serializers.SlugRelatedField(queryset=Director.objects.all(), slug_field='last_name')
    class Meta:
        model = Movie
        fields = ['url', 'title', 'description', 'running_time','release_date','category','director']

    def validate_running_time(self, value):
        if value < 0:
            raise serializers.ValidationError("Czas trwania nie może być liczbą ujemną")
        return value

class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ['pk','url', 'first_name','last_name', 'birthday', 'stars']

class SeansSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.SlugRelatedField(queryset=Movie.objects.all(), slug_field='title')
    class Meta:
        model = Seans
        fields = ['url', 'date', 'time','movie']

    def validate_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("Data nowego seansu nie może rozpoczynać się w przeszłości")
        return value

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    client = serializers.ReadOnlyField(source='client.username')
    seans = serializers.SlugRelatedField(queryset=Seans.objects.all(), slug_field='id')
    class Meta:
        model = Reservation
        fields = ['url','ticket','client', 'seans']

class ReviewsSerializer(serializers.HyperlinkedModelSerializer):
    movie = serializers.SlugRelatedField(queryset=Movie.objects.all(), slug_field='id')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reviews
        fields = ['url', 'stars','text','movie','owner']

    def validate_stars(self, value):
        if value < 0 or value > 10:
            raise serializers.ValidationError("Ocena filmu musi zawierać się w przedziale [0,10]")
        return value

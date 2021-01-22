from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=45, unique=True)

class Actors(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    age = models.IntegerField()
    def __str__(self):
        return self.firstName + ' '+self.lastName;

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    runningTime = models.IntegerField()
    actors = models.ManyToManyField(Actors)

class Director(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'), (FEMALE, 'Female'),)
    name = models.CharField(max_length=45)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=MALE)
    dateOfBirth = models.DateField()

class MovieTime(models.Model):
    date = models.DateField()
    time = models.TimeField()

class Hall(models.Model):
    name = models.CharField(max_length=45)

class Seats(models.Model):
    FIRST = 'I'
    SECOND = 'II'
    THIRD = 'III'
    FOURTH = 'IV'
    FIFTH = 'V'
    SIXTH = 'VI'
    SEVENTH = 'VII'
    EIGHTH = 'VIII'
    NINTH = 'IX'

    ROW_CHOICES = ((FIRST, 'I'), (SECOND, 'II'),
                   (THIRD, 'III'), (FOURTH, 'IV'),
                   (FIFTH, 'V'), (SIXTH, 'VI'),
                   (SEVENTH, 'VII'), (EIGHTH, 'VIII'),
                   (NINTH, 'IX'),)

    row = models.CharField(max_length=10, choices=ROW_CHOICES, default=FIRST)
    number = models.IntegerField(choices=[(i, i) for i in range(1, 30)], blank=True)


class Reservation(models.Model):
    dateOfReservation = models.DateTimeField(auto_now_add=True)

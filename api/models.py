from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Category(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=45, default='')
    last_name = models.CharField(max_length=45)
    birthday = models.DateField(null=True, blank=True)
    stars = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)

    class Meta:
        ordering = ('last_name',)


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    running_time = models.IntegerField()
    release_date = models.DateField(null=True, blank=True)
    category = models.ManyToManyField(Category, related_name="category")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movie')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Seans(models.Model):
    date = models.DateField(blank= True,null=True)
    time = models.TimeField(blank= True,null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='seans')

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return str(self.movie) + "(" + str(self.date) +") Godzina: " + str(self.time)


class Reservation(models.Model):
    RED = "reduced"
    NOR = "normal"
    TICKET_CHOICES = ((RED, 'reduced'), (NOR, 'normal'))
    date = models.DateTimeField(auto_now_add=True)
    ticket = models.CharField(max_length=15, choices=TICKET_CHOICES, default=NOR)
    client = models.ForeignKey('auth.User', related_name='reservation', on_delete=models.CASCADE)
    seans = models.ForeignKey(Seans, on_delete=models.CASCADE, null=True, related_name='reservation')


class Reviews(models.Model):
    stars = models.DecimalField(
                         max_digits=5,
                         decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(null=True, blank=True, max_length=255)
    owner = models.ForeignKey('auth.User', related_name='reviews', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', null=True)

    def __str__(self):
        return str(self.movie) + ' (' + str(self.stars) + ') '

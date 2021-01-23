from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=15, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=45)
    phone_number = models.CharField(max_length=9, null=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=45, unique=True)

    def __str__(self):
        return self.name

class Director(models.Model):
    first_name = models.CharField(max_length=45, default='')
    last_name = models.CharField(max_length=45)
    birthday = models.DateField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=45)
    runningTime = models.IntegerField()
    category = models.ManyToManyField(Category, related_name="category")
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movie')

    def __str__(self):
        return self.title


class Seans(models.Model):
    date = models.DateField()
    time = models.TimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='seans')

    def __str__(self):
        return str(self.movie) + "(" + str(self.date) +") Godzina: " + str(self.time)


class Reservation(models.Model):
    RED = "reduced"
    NOR = "normal"
    TICKET_CHOICES = ((RED, 'reduced'), (NOR, 'normal'))
    date = models.DateTimeField(auto_now_add=True)
    ticket = models.CharField(max_length=15, choices=TICKET_CHOICES, default=NOR)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, related_name='reservation')
    seans = models.ForeignKey(Seans, on_delete=models.CASCADE, null=True, related_name='reservation')

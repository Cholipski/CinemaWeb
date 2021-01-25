from django.contrib import admin
from .models import Movie, Category, Director, Seans, Reservation, Reviews


admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Seans)
admin.site.register(Reservation)
admin.site.register(Reviews)

from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'Movie', views.MovieViewSet)
router.register(r'Actors', views.ActorsViewSet)
router.register(r'Director', views.DirectorViewSet)
router.register(r'Seats', views.SeatsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
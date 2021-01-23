from django.urls import include, path
from . import views
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('Movie/', views.MovieList.as_view(), name=views.MovieList.name),
    path('Movie/<int:pk>/', views.MovieDeatil.as_view(), name=views.MovieDeatil.name),
    path('Category/', views.CategoryList.as_view(), name=views.CategoryList.name),
    path('Category/<int:pk>/', views.CategoryDeatil.as_view(), name=views.CategoryDeatil.name),
    path('Director/', views.DirectorList.as_view(), name=views.DirectorList.name),
    path('Director/<int:pk>/', views.DirectorDeatil.as_view(), name=views.DirectorDeatil.name),
    path('Reservation/', views.ReservationList.as_view(), name=views.ReservationList.name),
    path('Reservation/<int:pk>/', views.ReservationDetail.as_view(), name=views.ReservationDetail.name),
    path('Seans/', views.SeansList.as_view(), name=views.SeansList.name),
    path('Seans/<int:pk>/', views.SeansDetail.as_view(), name=views.SeansDetail.name),
    path('user/', views.UserList.as_view(), name=views.UserList.name),
    path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
from . import views
from .models import Category, Director
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from django import urls
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from datetime import datetime
from faker import Faker

class RemoteAuthenticatedTest(APITestCase):
    client_class = APIClient

    def setUp(self):
        self.username = 'mister_neutron'
        self.user = User.objects.create_superuser(username='mister_neutron',
                                                  email='mister_neutron@example.com',
                                                  password='F4kePaSs0d')

        super(RemoteAuthenticatedTest, self).setUp()


class CategoryTests(RemoteAuthenticatedTest):
    def post_category(self, name):
        url = reverse(views.CategoryList.name)
        data = {'name': name}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.post(url, data, format='json', REMOTE_USER=self.username)
        return response

    def test_post_and_get_category(self):
        new_category = 'Komedia obyczajowa'
        response = self.post_category(new_category)

        assert response.status_code == status.HTTP_201_CREATED
        assert Category.objects.count() == 1
        assert Category.objects.get().name == new_category

    def test_search_category(self):
        name = 'Komedia'
        self.post_category(name, )
        search_category = {'name': name, }
        url = '{0}?{1}'.format(reverse(views.CategoryList.name), urlencode(search_category))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == name

    def test_delete_category(self):
        name = 'Komedia'
        response = self.post_category(name, )
        url = urls.reverse(views.CategoryDeatil.name, None, {response.data['pk']})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_update_address(self):
        name = 'Komedia'
        response = self.post_category(name, )
        url = urls.reverse(views.CategoryDeatil.name, None, {response.data['pk']})
        updated_new_name = 'Komedia romantyczna'
        data = {'name': updated_new_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == updated_new_name

    def test_post_existing_category_name(self):
        url = reverse(views.CategoryList.name)
        new_category_name = 'Komedia'
        data = {'name': new_category_name}
        response_one = self.post_category(new_category_name)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_category(new_category_name)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST


class DirectorTests(RemoteAuthenticatedTest):
    def post_director(self, first_name, last_name, birthday, stars):
        url = reverse(views.DirectorList.name)
        data = {'first_name': first_name, 'last_name': last_name, 'birthday': birthday, 'stars': stars}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.auth_token.key)
        response = self.client.post(url, data, format='json', REMOTE_USER=self.username)
        return response

    def test_post_and_get_director(self):
        fake = Faker()
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        birthday = fake.date_of_birth()
        stars = 4.5

        response = self.post_director(first_name,last_name,birthday, stars)

        assert response.status_code == status.HTTP_201_CREATED
        assert Director.objects.count() == 1
        assert Director.objects.get().first_name == first_name
        assert Director.objects.get().last_name == last_name
        assert Director.objects.get().stars == stars
        assert Director.objects.get().birthday == birthday

    def test_delete_director(self):
        fake = Faker()
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        birthday = fake.date_of_birth()
        stars = 4.5
        response = self.post_director(first_name,last_name,birthday, stars)
        url = urls.reverse(views.DirectorDeatil.name, None, {response.data['pk']})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data is None

    def test_update_director(self):
        fake = Faker()
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        birthday = fake.date_of_birth()
        stars = 4.5
        response = self.post_director(first_name, last_name, birthday, stars)
        url = urls.reverse(views.DirectorDeatil.name, None, {response.data['pk']})
        new_first_name = 'Michał'
        data = {'first_name': new_first_name}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['first_name'] == new_first_name

    def test_search_car(self):
        fake = Faker()
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        birthday = fake.date_of_birth()
        stars = 4.5
        self.post_director(first_name, last_name, birthday, stars)

        search_director = {'last_name': last_name, }

        url = '{0}?{1}'.format(reverse(views.DirectorList.name), urlencode(search_director))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['last_name'] == last_name
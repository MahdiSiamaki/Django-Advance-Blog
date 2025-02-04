from datetime import datetime

import pytest
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def common_user(django_user_model):
    return django_user_model.objects.create_user(
        email='test@test.com',password='sdfa134@',is_verified= True)

@pytest.mark.django_db
class TestPostApi:

    def test_get_post_response_200_status(self,api_client):
        url= reverse('blog:api-v1:post-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self,api_client):
        url= reverse('blog:api-v1:post-list')
        data= {
            'title':'test',
            'content':'test.test.test',
            'status': True,
            'published_at':datetime.now()
        }
        response= api_client.post(url,data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self,api_client,common_user):
        url= reverse('blog:api-v1:post-list')
        data= {
            'title':'test',
            'content':'test.test.test',
            'status': True,
            'published_at':datetime.now()
        }
        user= common_user
        api_client.force_authenticate(user=user)
        response= api_client.post(url,data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(self,api_client,common_user):
        url= reverse('blog:api-v1:post-list')
        data= {
            'content':'test.test.test',
        }
        user= common_user
        api_client.force_authenticate(user=user)
        response= api_client.post(url,data)
        assert response.status_code == 400
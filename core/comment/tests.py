import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from blog.models import Post
from accounts.models import User
from .models import Comment

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def common_user(django_user_model):
    return django_user_model.objects.create_user(
        email='test@test.com', password='sdfa134@', is_verified=True)

@pytest.fixture
def post(common_user):
    return Post.objects.create(
        title='Test Post',
        content='Test Content',
        status=True,
        published_at=datetime.now(),
        author=common_user.profile
    )

@pytest.mark.django_db
class TestCommentApi:

    def test_create_comment_response_401_status(self, api_client, post):
        url = reverse('comment-list-create')
        data = {
            'post': post.id,
            'content': 'Test Comment'
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_comment_response_201_status(self, api_client, common_user, post):
        url = reverse('comment-list-create')
        data = {
            'post': post.id,
            'content': 'Test Comment'
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_retrieve_comment_response_200_status(self, api_client, common_user, post):
        comment = Comment.objects.create(
            post=post,
            author=common_user,
            content='Test Comment'
        )
        url = reverse('comment-detail', args=[comment.id])
        response = api_client.get(url)
        assert response.status_code == 200

    def test_delete_comment_response_204_status(self, api_client, common_user, post):
        comment = Comment.objects.create(
            post=post,
            author=common_user,
            content='Test Comment'
        )
        url = reverse('comment-detail', args=[comment.id])
        api_client.force_authenticate(user=common_user)
        response = api_client.delete(url)
        assert response.status_code == 204

    def test_list_comments_response_200_status(self, api_client, post):
        Comment.objects.create(
            post=post,
            author=post.author.user,
            content='Test Comment 1'
        )
        Comment.objects.create(
            post=post,
            author=post.author.user,
            content='Test Comment 2'
        )
        url = reverse('comment-list-create')
        response = api_client.get(url)
        assert response.status_code == 200
        assert len(response.data) == 2

    def test_update_comment_with_invalid_data_response_400_status(self, api_client, common_user, post):
        comment = Comment.objects.create(
            post=post,
            author=common_user,
            content='Test Comment'
        )
        url = reverse('comment-detail', args=[comment.id])
        data = {
            'content': ''  # Invalid data: content is required
        }
        api_client.force_authenticate(user=common_user)
        response = api_client.put(url, data)
        assert response.status_code == 400
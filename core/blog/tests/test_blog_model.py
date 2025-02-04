from datetime import datetime

from django.test import TestCase

from blog.models import Post, Category
from accounts.models import Profile, User


class TestPostModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@test.com', password='asdfzxcv@123')
        self.profile, created = Profile.objects.get_or_create(
            user=self.user,
            defaults={
                'first_name': 'test',
                'last_name': 'tset',
                'description': 'test.tset.test'
            }
        )
    def test_create_post_with_valid_data(self):

        post = Post.objects.create(
            author= self.profile,
            title= 'test',
            content= 'test',
            status = True,
            category = None,
            published_at= datetime.now()
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
        self.assertEquals(post.title, 'test')
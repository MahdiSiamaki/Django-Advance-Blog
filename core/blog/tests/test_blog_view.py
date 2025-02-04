from django.test import TestCase, Client
from django.urls import reverse
from datetime import datetime
from accounts.models import User, Profile
from blog.models import Post, Category

class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client()
        # Create test user
        self.user = User.objects.create(email='test@test.com', password='asdfzxcv@123')
        # Create profile
        self.profile, created = Profile.objects.get_or_create(
            user=self.user,
            defaults={
                'first_name': 'test',
                'last_name': 'test',
                'description': 'test.test.test'
            }
        )
        # Create test post
        self.post = Post.objects.create(
            author=self.profile,
            title='Test Post',
            content='Test Content',
            status=True,
            published_at=datetime.now()
        )

    def test_blog_index_url_successful_response(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_blog_post_detail_anonymous_response(self):
        url = reverse('blog:post-detail', args=[self.post.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/accounts/login/?next={url}')
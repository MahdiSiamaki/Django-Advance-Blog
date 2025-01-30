from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    def test_blog_list_url(self):
        url = reverse('blog:post-list')
        self.assertEqual(url, '/blog/posts/')

    def test_blog_detail_url(self):
        url = reverse('blog:post-detail', args=[1])
        self.assertEqual(url, '/blog/posts/1/')

    def test_blog_create_url(self):
        url = reverse('blog:post-create')
        self.assertEqual(url, '/blog/post/create/')

    def test_blog_update_url(self):
        url = reverse('blog:post-edit', args=[1])
        self.assertEqual(url, '/blog/post/1/edit/')

    def test_blog_delete_url(self):
        url = reverse('blog:post-delete', args=[1])
        self.assertEqual(url, '/blog/post/1/delete/')
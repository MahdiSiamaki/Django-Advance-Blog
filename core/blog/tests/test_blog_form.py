from django.test import TestCase
from datetime import datetime

from ..forms import PostForm
from ..models import Category


class TestPostForm(TestCase):

    def test_post_form_with_valid_data(self ):
        category_obj= Category.objects.create(
            name= 'hello'
        )
        form = PostForm(data={
            'title': 'tset',
            'content': 'description',
            'category': category_obj,
            'published_at':datetime.now(),
            'status': True
        })
        self.assertTrue(form.is_valid())

    def test_post_form_with_no_data(self):
            form = PostForm(data={})
            self.assertFalse(form.is_valid())
from datetime import datetime

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.models import Profile
from blog.models import Post, Category
from faker import Faker
import random
from django.utils import timezone
from unicodedata import category

User = get_user_model()

category_list= [
    'IT','Design','Fun'
]

class Command(BaseCommand):
    help = "Insert data into database"

    def __init__(self,*args,**kwargs):
        super(Command,self).__init__(*args,**kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user= User.objects.create_user(email=self.fake.email(),password="Test1234@")
        profile= Profile.objects.get(user=user)
        profile.first_name= self.fake.first_name()
        profile.last_name= self.fake.last_name()
        profile.description= self.fake.text()
        profile.save()

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            Post.objects.create(
                author= profile,
                title= self.fake.sentence(),
                content= self.fake.text(),
                category= Category.objects.get(name=random.choice(category_list)),
                published_at= datetime.now(),
                status= random.choice([True,False])
            )

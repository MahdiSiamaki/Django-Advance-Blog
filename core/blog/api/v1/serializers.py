from django.template.context_processors import request
from rest_framework import serializers
from ...models import Post, Category


'''
class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    status = serializers.BooleanField(default=True)
    # category = serializers.IntegerField()
    published_at = serializers.DateTimeField()
    # author = serializers.IntegerField()

    # def create(self, validated_data):
    #     return Post.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.status = validated_data.get('status', instance.status)
    #     instance.category = validated_data.get('category', instance.category)
    #     instance.published_at = validated_data.get('published_at', instance.published_at)
    #     instance.author = validated_data.get('author', instance.author)
    #     instance.save()
    #     return instance
'''

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.CharField(source='get_snippet', read_only=True)
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only= True)
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    class Meta:
        model = Post
        fields = ['id','title','content','status','author','category','created_at','published_at','snippet','relative_url'
                  ,'absolute_url']

    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
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
    class Meta:
        model = Post
        fields = ['id','title','content','status','published_at','author','category']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
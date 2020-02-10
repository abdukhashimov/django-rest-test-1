from rest_framework import serializers
from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all())

    class Meta:
        model = Post
        fields = '__all__'

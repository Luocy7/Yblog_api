from rest_framework import serializers

from .models import Category, Tag, Post, FriendLink


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
        ]


class PostListSerializer(serializers.ModelSerializer):
    api_url = serializers.CharField(read_only=True)

    class Meta:
        model = Post
        exclude = [
            "excerpt",
            "author",
            "markdown",
        ]
        depth = 0


class PostRetrieveSerializer(serializers.ModelSerializer):
    api_url = serializers.CharField(read_only=True)
    markdown = serializers.CharField(required=True)

    class Meta:
        model = Post
        exclude = ["author"]


class FriendLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendLink
        fields = "__all__"

from rest_framework import serializers

from apps.blog.models import Blog, Category, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    blog_id = serializers.PrimaryKeyRelatedField(
        queryset=Blog.objects.all(),
        source="blog",
    )

    class Meta:
        model = Comments
        fields = ("id", "blog_id", "text")
        read_only_fields = ("id",)


class BlogSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"

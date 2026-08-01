from rest_framework import status, viewsets
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response

from apps.blog.models import Blog, Category
from apps.blog.serializers import BlogSerializer, CategorySerializer, CommentsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request: Request) -> Response:
        blogs = Blog.objects.all()
        serializer = self.get_serializer(blogs, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)

        return Response(self.get_serializer(blog).data)


class CommentsCreateView(GenericAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

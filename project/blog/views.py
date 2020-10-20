from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.serializers import DateField

from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from rest_framework_simplejwt.authentication import JWTAuthentication

from .filters import PostFilter
from .serializers import *


class MyModelViewSet(ModelViewSet):
    authentication_classes = (JWTAuthentication, BasicAuthentication)
    permission_classes = (
        # IsAuthenticatedOrReadOnly,
        AllowAny,
    )


class PostViewSet(MyModelViewSet):
    serializer_class = PostRetrieveSerializer
    queryset = Post.objects.all()
    serializer_class_table = {
        "list": PostListSerializer,
        "retrieve": PostRetrieveSerializer,
    }
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    def get_serializer_class(self):
        return self.serializer_class_table.get(
            self.action, super().get_serializer_class()
        )

    @action(
        methods=["GET"], detail=False, url_path="archive/dates", url_name="archive-date"
    )
    def list_archive_dates(self, request, *args, **kwargs):
        dates = Post.objects.dates("created_time", "month", order="DESC")
        date_field = DateField()
        data = [date_field.to_representation(date) for date in dates]
        return Response(data=data, status=status.HTTP_200_OK)


class CategoryViewSet(MyModelViewSet):
    serializer_class = CategorySerializer
    pagination_class = None  # 关闭分页
    queryset = Category.objects.all().order_by("name")


class TagViewSet(MyModelViewSet):
    serializer_class = TagSerializer
    pagination_class = None
    queryset = Tag.objects.all().order_by("name")


class FriendLinkViewSet(MyModelViewSet):
    serializer_class = FriendLinkSerializer
    pagination_class = None
    queryset = FriendLink.objects.all().order_by("link_order")


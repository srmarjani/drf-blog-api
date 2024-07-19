from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

from api.models import SimplePost
from api.serializers import SimplePostSerializer
from api.filters import SimplePostFilter

class SimplePostViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = SimplePost.objects.all()
    serializer_class = SimplePostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['title', 'like']
    filterset_class = SimplePostFilter
    search_fields = ['title', 'body']
    ordering_fields = ['title', 'created']
    ordering = ['-created']
    # throttle_classes = [UserRateThrottle]
    # throttle_scope = 'contacts'
    # pagination_class = PageNumberPagination



    @action(methods=['get'], detail=False)
    def last_post(self, request):
        last_post = SimplePost.objects.last()

        serializer = SimplePostSerializer(last_post)

        return Response(serializer.data, status=status.HTTP_200_OK)



    
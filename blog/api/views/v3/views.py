from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.models import SimplePost
from api.serializers import SimplePostSerializer

class SimplePostViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    queryset = SimplePost.objects.all()
    serializer_class = SimplePostSerializer

    @action(methods=['get'], detail=False)
    def last_post(self, request):
        last_post = SimplePost.objects.last()

        serializer = SimplePostSerializer(last_post)

        return Response(serializer.data, status=status.HTTP_200_OK)



    
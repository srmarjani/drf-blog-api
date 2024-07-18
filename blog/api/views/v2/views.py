from rest_framework import generics
from api.serializers import SimplePostSerializer
from api.models import SimplePost


class SimplePostList(generics.ListCreateAPIView):
    queryset = SimplePost.objects.all()
    serializer_class = SimplePostSerializer

post_list = SimplePostList.as_view()

class SimplePostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SimplePost.objects.all()
    serializer_class = SimplePostSerializer

post_detail = SimplePostDetail.as_view()
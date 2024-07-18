from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.models import SimplePost
from api.serializers import SimplePostSerializer

@api_view(['GET', 'POST'])
def posts(request, *args, **kwargs):
    if request.method == 'POST':
        serializer = SimplePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data}, status=status.HTTP_201_CREATED)
    
    posts = SimplePost.objects.all()
    serializer = SimplePostSerializer(posts, many=True) 
    return Response({"posts": serializer.data})
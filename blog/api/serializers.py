from rest_framework import serializers
from api.models import SimplePost, SimpleComment

class SimpleCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimpleComment
        fields = '__all__'
        
class SimplePostSerializer(serializers.ModelSerializer):
    comments = SimpleCommentSerializer(many=True, read_only=True)

    class Meta:
        model = SimplePost
        fields = '__all__'



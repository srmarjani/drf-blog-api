from django_filters import FilterSet

from api.models import SimplePost

class SimplePostFilter(FilterSet):

    class Meta:
        model = SimplePost
        fields = {
            'like': ['lt', 'gt'],
            'title': ['exact'],
        }
        # fields = ['title', 'like']
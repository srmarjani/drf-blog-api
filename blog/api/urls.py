from django.urls import path

from api.views.v1 import views as v1_views


urlpatterns = [
    path('/v1/',  v1_views.posts, name='v1_posts')
]

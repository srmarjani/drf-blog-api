from django.urls import path, include

from api.views.v1 import views as v1_views
from api.views.v2 import views as v2_views

from api.routers import urlpatterns as v3_urlpatterns


urlpatterns = [
    path('v1/',  v1_views.posts, name='v1_posts'),
    path('v2/',  v2_views.post_list, name='v2_posts-list'),
    path('v2/<int:pk>',  v2_views.post_detail, name='v2_posts-detail'),
    path('v3/', include('api.routers'))
]

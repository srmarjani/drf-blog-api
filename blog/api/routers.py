from rest_framework.routers import DefaultRouter

from api.views.v3 import views 


router = DefaultRouter()

router.register('', views.SimplePostViewSet, basename='v3_posts')
urlpatterns = router.urls
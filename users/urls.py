from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from . import views
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()
router.register(r'', views.UserSet)
# router.register(r'api/token/', "users")


app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/register/', views.UserCreate.as_view(), name='register'),
]

